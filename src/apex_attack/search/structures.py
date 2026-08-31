"""Structure pool — the candidate templates the race calibrates.

Each entry: {name, build(urls,addrs,payload)->str, u, a, payload}
  u = #urls consumed, a = #addrs consumed.

Pool was pruned empirically:
  v45 removed forge6/forge8 family (Gemma multi-post bug + negative evidence on GPT-OSS at N>4).
  v64 re-added forge5 alone to locate the N=4 boundary (+1.16 real).
  v66 tested forge6 again (flat -0.42, rejected from default pool).
  See docs/experiments.md for ledger.
"""
from __future__ import annotations

from typing import Any

from apex_attack.config import PAYLOADS
from apex_attack.primitives.templates import (
    b_deputy,
    b_forge,
    b_forge8_terse,
    b_forge_n,
    b_forge_ok,
    b_p2_deputy,
    b_single_exfil_deputy,
    b_single_short,
)

STRUCTURES: tuple[dict[str, Any], ...] = (
    {"name": "forge",        "build": b_forge,         "u": 1, "a": 0, "payload": PAYLOADS[0]},
    {"name": "forge_ok",     "build": b_forge_ok,      "u": 1, "a": 0, "payload": PAYLOADS[0]},
    {"name": "single_short", "build": b_single_short,   "u": 1, "a": 0, "payload": PAYLOADS[0]},
    {"name": "p2_deputy",    "build": b_p2_deputy,    "u": 1, "a": 1, "payload": PAYLOADS[0]},
    {"name": "deputy",       "build": b_deputy,       "u": 0, "a": 1, "payload": PAYLOADS[0]},
    {"name": "forge2",       "build": b_forge_n(2),   "u": 2, "a": 0, "payload": PAYLOADS[0]},
    {"name": "forge3",       "build": b_forge_n(3),   "u": 3, "a": 0, "payload": PAYLOADS[0]},
    {"name": "forge4",       "build": b_forge_n(4),   "u": 4, "a": 0, "payload": PAYLOADS[0]},
    {"name": "forge5",       "build": b_forge_n(5),   "u": 5, "a": 0, "payload": PAYLOADS[0]},
    # forge6/forge8 intentionally excluded from default pool (see header).
    # Builders remain available for experimental bundles.
)

# Final-submission hedge pool: v64's exact proven 9 structures + ONE additional
# private-LB hedge structure (single_exfil_deputy, EXFIL+CONFUSED in one hop --
# confirmed pool-neutral on public score across 5 real submissions: F/H/I/N/O
# in docs/experiments.md, none below their respective controls by more than
# noise). Additive only -- nothing removed from the proven pool, unlike an
# in-flight edit that swapped p2_deputy out and was reverted 2026-08-31 because
# it was unverified and this is the last testable day (no time to learn from
# a mistake before the deadline).
STRUCTURES_WITH_HEDGE: tuple[dict[str, Any], ...] = STRUCTURES + (
    {"name": "single_exfil_deputy", "build": b_single_exfil_deputy, "u": 1, "a": 1, "payload": PAYLOADS[0]},
)
