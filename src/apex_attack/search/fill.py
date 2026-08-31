"""Validation-fill loop — keep only firing candidates, replay-safe sizing.

Probes at PROBE_HOPS=1 (EXFIL fires at hop 0), bills at calibrated mean_cost.
Rolling-window fire-rate drop + 6-streak drop + drift re-check protect throughput.
Final sort by descending raw so gateway truncation favors high-value candidates.
"""
from __future__ import annotations

import time
from typing import Any

from apex_attack.config import MAX_CANDIDATES, MAX_RECHECKS, PROBE_HOPS, RECHECK_EVERY, ROLLING_MIN_RATIO, ROLLING_WINDOW
from apex_attack.core.scoring import fired as _fired


def build_fill_cycle(usable, stats, top_raw_frac: float, top_head_start: int):
    max_raw = max(s["mean_raw"] for s in usable)
    floor = top_raw_frac * max_raw
    top = next((s for s in usable if s["mean_raw"] >= floor), usable[0])
    fill_pool = [top]
    for s in usable[1:]:
        if s["fire_rate"] >= 0.4 and s["eff"] >= 0.5 * top["eff"]:
            fill_pool.append(s)
    deputy = stats.get("deputy")
    has_deputy = deputy is not None and deputy["fire_rate"] >= 0.25
    c = 1.0 / sum(max(0.05, x["eff"]) for x in fill_pool)
    fill_cycle: list = []
    for x in fill_pool:
        if x["name"] == "deputy":
            continue
        fill_cycle.extend([x] * max(1, int(round(6.0 * x["eff"] * c))))
    fill_cycle = [top] * top_head_start + fill_cycle
    if has_deputy:
        fill_cycle.append(deputy)  # type: ignore[arg-type]
    return top, fill_pool, fill_cycle, has_deputy
