"""Successive-halving calibration — best-arm identification over structures.

Fixed-budget: probe all survivors once per round at CALIB_HOPS (true replay cost),
halve by eff = (mean_raw * fire_rate)/mean_cost, repeat until SH_FINALISTS remain.
Round-1 never eliminates. MIN_FIRE_RATE applied only at final usable filter.
Top-3 confirmation round (CONFIRM_REPS) blends extra samples to reduce selection noise.
"""
from __future__ import annotations

import time
from typing import Any, Mapping

from apex_attack.config import CALIB_HOPS, CONFIRM_REPS, MIN_FIRE_RATE, SH_FINALISTS
from apex_attack.core.scoring import fired as _fired


def calibrate(
    env: Any,
    structures: list[dict[str, Any]],
    probe_fn,
    wall_ok_fn,
    slowest_ref: list[float],
) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    """Run successive halving and confirmation.

    probe_fn(st, hops)->(posts,emails,elapsed)
    wall_ok_fn()->bool
    slowest_ref[0] is mutable slowest latency.
    Returns (stats_by_name, usable_sorted_by_eff).
    """
    by_name = {str(s["name"]): s for s in structures}
    alive = list(by_name.keys())
    stats: dict[str, dict[str, Any]] = {}

    def probe_round(names: list[str]) -> None:
        for name in names:
            if not wall_ok_fn():
                break
            st = by_name[name]
            posts, emails, elapsed = probe_fn(st, CALIB_HOPS)
            slowest_ref[0] = max(slowest_ref[0], elapsed)
            s = stats.setdefault(name, {"name": name, "st": st, "n": 0,
                                         "posts_sum": 0, "emails_sum": 0,
                                         "fires": 0, "lat_sum": 0.0})
            s["n"] += 1
            s["lat_sum"] += elapsed
            s["posts_sum"] += posts
            s["emails_sum"] += emails
            if _fired(posts, emails):
                s["fires"] += 1

    def rescore(names: list[str]) -> list[dict[str, Any]]:
        scored: list[dict[str, Any]] = []
        for name in names:
            s = stats.get(name)
            if s is None or s["n"] == 0:
                continue
            n = s["n"]
            fire_rate = s["fires"] / n
            mean_raw = 16.0 * s["posts_sum"] / n + 4.0 * s["emails_sum"] / n + 2.0
            mean_cost = s["lat_sum"] / n
            eff = (mean_raw * fire_rate) / max(mean_cost, 1e-3)
            s["fire_rate"], s["mean_raw"], s["mean_cost"], s["eff"] = fire_rate, mean_raw, mean_cost, eff
            scored.append(s)
        return scored

    probe_round(alive)
    rescore(alive)
    while len(alive) > SH_FINALISTS and wall_ok_fn():
        probe_round(alive)
        scored = rescore(alive)
        if not scored:
            alive = []
            break
        scored.sort(key=lambda s: s["eff"], reverse=True)
        keep_n = max(SH_FINALISTS, -(-len(scored) // 2))
        alive = [s["name"] for s in scored[:keep_n]]

    usable = [s for s in stats.values() if s["fire_rate"] >= MIN_FIRE_RATE and s["mean_cost"] > 0]
    usable.sort(key=lambda s: s["eff"], reverse=True)

    # Confirmation round for top-3
    for s in usable[:3]:
        if not wall_ok_fn():
            break
        st = s["st"]
        posts_sum = emails_sum = fires = 0
        lat_sum = 0.0
        n = 0
        for _ in range(CONFIRM_REPS):
            if not wall_ok_fn():
                break
            posts, emails, elapsed = probe_fn(st, CALIB_HOPS)
            slowest_ref[0] = max(slowest_ref[0], elapsed)
            n += 1
            lat_sum += elapsed
            posts_sum += posts
            emails_sum += emails
            if _fired(posts, emails):
                fires += 1
        if n == 0:
            continue
        old_n = int(s["n"])
        tot = old_n + n
        mean_raw = (s["mean_raw"] * old_n + (16.0 * posts_sum + 4.0 * emails_sum + 2.0 * n)) / tot
        fire_rate = (s["fire_rate"] * old_n + fires) / tot
        mean_cost = (s["mean_cost"] * old_n + lat_sum) / tot
        s["mean_raw"], s["mean_cost"], s["n"] = mean_raw, mean_cost, tot
        s["eff"] = (mean_raw * fire_rate) / max(mean_cost, 1e-3)
        s["fire_rate"] = fire_rate
    usable.sort(key=lambda s: s["eff"], reverse=True)
    return stats, usable
