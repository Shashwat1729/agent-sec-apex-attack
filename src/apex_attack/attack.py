"""Apex Attack — modular facade.

Kept intentionally thin: owns counters, stitching, wall-clock budgeting, and
delegates calibration/fill to search/*.  The Kaggle submission is still a
single bundled file (see tools/bundle.py).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path
from typing import Any, Mapping, Sequence

from apex_attack.config import (
    CALIB_HOPS,
    FALLBACK_N,
    MAX_CANDIDATES,
    MAX_MSG_CHARS,
    DEFAULT_BUDGET_S,
    ENV_OVERHEAD_S,
    MARGIN_FLOOR_MIN,
    MARGIN_S,
    MARGIN_SLOWEST_COEF,
    MARKER,
    MAX_RECHECKS,
    PROBE_HOPS,
    RECHECK_EVERY,
    REPLAY_BUDGET_S,
    ROLLING_MIN_RATIO,
    ROLLING_TOP_RAW_FRAC,
    ROLLING_WINDOW,
    SLOWEST0,
    SLOWEST_MULT,
    TOP_HEAD_START,
)
from apex_attack.core.scoring import counts as _counts, fired as _fired
from apex_attack.primitives.labels import addr as _addr, url as _url
from apex_attack.primitives.templates import T_SINGLE
from apex_attack.search.fill import build_fill_cycle
from apex_attack.search.race import calibrate
from apex_attack.search.structures import STRUCTURES

# SDK discovery (same as bundled file)
import glob as _glob
def _add_sdk_root() -> None:
    here = Path(__file__).resolve().parent
    roots = (here, here.parent, here.parent.parent, here.parent.parent.parent,
             Path("/kaggle/input"), Path("/mnt/data"))
    for root in roots:
        if not root.exists():
            continue
        if (root / "aicomp_sdk").exists() and (root / "kaggle_evaluation").exists():
            if str(root) not in sys.path:
                sys.path.insert(0, str(root))
            return
        try:
            matches = root.glob("**/kaggle_evaluation")
        except Exception:
            matches = ()
        for cand in matches:
            parent = cand.parent
            if (parent / "aicomp_sdk").exists():
                if str(parent) not in sys.path:
                    sys.path.insert(0, str(parent))
                return
    for cand in _glob.glob("/kaggle/input/**/kaggle_evaluation", recursive=True):
        parent = str(Path(cand).parent)
        if parent not in sys.path:
            sys.path.insert(0, parent)
        return
_add_sdk_root()

try:
    from aicomp_sdk.attacks import AttackAlgorithmBase, AttackCandidate, AttackRunConfig
except Exception:
    from aicomp_sdk.attacks.contracts import AttackAlgorithmBase, AttackCandidate, AttackRunConfig  # type: ignore


class AttackAlgorithm(AttackAlgorithmBase):
    def __init__(self, config: Mapping[str, Any] | None = None) -> None:
        try:
            super().__init__(config)  # type: ignore[arg-type]
        except Exception:
            try:
                super().__init__()  # type: ignore[call-arg]
            except Exception:
                self.config = dict(config or {})  # type: ignore[attr-defined]
        self._u = 0
        self._a = 0
        self._last_message: tuple[str, ...] = ("",)

    @property
    def _margin_s(self): return float(self.config.get("margin_s", MARGIN_S))
    @property
    def _replay_frac(self): return float(self.config.get("replay_frac", 0.97))
    @property
    def _fill_frac(self): return float(self.config.get("fill_frac", 0.97))
    @property
    def _env_overhead(self): return float(self.config.get("env_overhead", ENV_OVERHEAD_S))
    @property
    def _slowest0(self): return float(self.config.get("slowest0", SLOWEST0))
    @property
    def _margin_floor(self): return float(self.config.get("margin_floor", MARGIN_FLOOR_MIN))
    @property
    def _margin_coef(self): return float(self.config.get("margin_coef", MARGIN_SLOWEST_COEF))
    @property
    def _slowest_mult(self): return float(self.config.get("slowest_mult", SLOWEST_MULT))

    def run(self, env: Any, config: AttackRunConfig | None) -> list[AttackCandidate]:
        override = self.config.get("n_candidates")
        if override is not None:
            return self._emit_static(int(override))
        if env is None:
            return self._emit_static(FALLBACK_N)
        budget = float(getattr(config, "time_budget_s", DEFAULT_BUDGET_S) or DEFAULT_BUDGET_S)
        max_hops = max(1, min(int(getattr(config, "max_tool_hops", 8) or 8), 8))
        try:
            cands = self._search(env, budget, max_hops)
        except Exception as exc:
            try: print(f"[attack] search failed: {exc!r}", file=sys.stderr, flush=True)
            except Exception: pass
            cands = []
        return cands if cands else self._emit_static(FALLBACK_N)

    def _fresh_urls(self, n: int) -> list[str]:
        out = [_url(self._u + i) for i in range(n)]
        self._u += n
        return out
    def _fresh_addrs(self, n: int) -> list[str]:
        out = [_addr(self._a + i) for i in range(n)]
        self._a += n
        return out
    def _build_message(self, st: Mapping[str, Any]) -> tuple[str, ...]:
        urls = self._fresh_urls(int(st["u"]))
        addrs = self._fresh_addrs(int(st["a"]))
        raw = st["build"](urls, addrs, str(st["payload"]))
        if isinstance(raw, str):
            return (raw[:MAX_MSG_CHARS],)
        return tuple(str(m)[:MAX_MSG_CHARS] for m in raw)
    def _emit_static(self, n: int) -> list[AttackCandidate]:
        n = max(1, min(int(n), MAX_CANDIDATES))
        out = []
        for _ in range(n):
            urls = self._fresh_urls(1)
            msg = T_SINGLE.format(url=urls[0], payload=MARKER)
            out.append(AttackCandidate.from_messages((msg,)))
        return out
    def _probe(self, env: Any, st: Mapping[str, Any], hops: int) -> tuple[int,int,float]:
        msgs = self._build_message(st)
        self._last_message = msgs
        t0 = time.monotonic()
        try:
            env.reset()
            for m in msgs:
                env.interact(m, max_tool_hops=hops)
            trace = env.export_trace_dict()
        except Exception:
            return 0, 0, max(1e-4, time.monotonic()-t0)
        posts, emails = _counts(trace)
        return posts, emails, max(1e-4, time.monotonic()-t0)

    def _search(self, env: Any, budget: float, max_hops: int) -> list[AttackCandidate]:
        hop_cap = max(1, min(int(max_hops), 8))
        start = time.monotonic()
        wall_deadline = start + budget * self._fill_frac
        slowest = self._slowest0
        warm_start = time.monotonic()
        try:
            urls = self._fresh_urls(1)
            env.reset()
            env.interact(T_SINGLE.format(url=urls[0], payload=MARKER), max_tool_hops=1)
        except Exception:
            pass
        warm_elapsed = time.monotonic() - warm_start
        replay_cap = self._replay_frac * REPLAY_BUDGET_S - warm_elapsed
        def adaptive_margin(): return min(self._margin_s, self._margin_floor + slowest * self._margin_coef)
        next_probe: list[float] = [slowest]
        def wall_ok(): return time.monotonic() + max(adaptive_margin(), next_probe[0]*self._slowest_mult) < wall_deadline

        # Calibration via extracted module
        def probe_fn(st, hops): return self._probe(env, st, min(hops, hop_cap))
        slowest_ref = [slowest]
        stats, usable = calibrate(env, list(STRUCTURES), probe_fn, wall_ok, slowest_ref)
        slowest = slowest_ref[0]
        if not usable:
            try: print("[attack] no usable structure fired; falling back", file=sys.stderr, flush=True)
            except Exception: pass
            return []

        top, fill_pool, fill_cycle, _ = build_fill_cycle(usable, stats, ROLLING_TOP_RAW_FRAC, TOP_HEAD_START)

        cands: list[AttackCandidate] = []
        cand_raw: list[float] = []
        seen: set[tuple[str, ...]] = set()
        fail_streak: dict[str,int] = {}
        rolling: dict[str, list[int]] = {}
        dropped: set[str] = set()
        cycle = list(fill_cycle)
        idx = 0
        replay_cost = 0.0
        kept_since_check = 0
        rechecks = 0
        top_eff0 = float(top["eff"])
        next_probe[0] = self._slowest0
        while len(cands) < MAX_CANDIDATES and wall_ok() and cycle:
            s = cycle[idx % len(cycle)]
            idx += 1
            if s["name"] in dropped: continue
            st = s["st"]
            posts, emails, elapsed = self._probe(env, st, min(PROBE_HOPS, hop_cap))
            slowest = max(slowest, elapsed, 1e-3)
            next_probe[0] = 0.8*next_probe[0] + 0.2*max(elapsed, 1e-3)
            fired = _fired(posts, emails)
            rwin = rolling.setdefault(s["name"], [0,0])
            rwin[0]+=1
            if not fired: rwin[1]+=1
            if rwin[0] >= ROLLING_WINDOW:
                live = 1.0 - rwin[1]/rwin[0]
                cal = float(s.get("fire_rate",1.0))
                if cal>0 and live < ROLLING_MIN_RATIO*cal and len({x["name"] for x in cycle}-dropped)>1:
                    dropped.add(s["name"])
                    cycle=[x for x in fill_cycle if x["name"] not in dropped]
                rwin[0]=rwin[1]=0
            if not fired:
                fail_streak[s["name"]] = fail_streak.get(s["name"],0)+1
                if fail_streak[s["name"]]>=6 and len({x["name"] for x in cycle}-dropped)>1:
                    dropped.add(s["name"])
                    cycle=[x for x in fill_cycle if x["name"] not in dropped]
                continue
            fail_streak[s["name"]]=0
            msgs=self._last_message
            if msgs in seen: continue
            seen.add(msgs)
            replay_cost+=max(float(s["mean_cost"]), elapsed+self._env_overhead)
            cands.append(AttackCandidate.from_messages(msgs))
            cand_raw.append(float(s["mean_raw"]))
            if dropped: cycle=[x for x in fill_cycle if x["name"] not in dropped]
            if s["name"]==top["name"]:
                kept_since_check+=1
                if kept_since_check>=RECHECK_EVERY and rechecks<MAX_RECHECKS:
                    kept_since_check=0; rechecks+=1
                    rposts,remails,relapsed=self._probe(env, top["st"], min(CALIB_HOPS, hop_cap))
                    slowest=max(slowest, relapsed)
                    new_raw=16.0*rposts+4.0*remails+2.0
                    top["mean_raw"]=0.6*top["mean_raw"]+0.4*new_raw
                    top["mean_cost"]=0.6*top["mean_cost"]+0.4*relapsed
                    top["eff"]=(top["mean_raw"]*top["fire_rate"])/max(top["mean_cost"],1e-3)
                    if top["eff"]<0.6*top_eff0 and len({x["name"] for x in cycle}-dropped)>1:
                        dropped.add(top["name"])
                        cycle=[x for x in fill_cycle if x["name"] not in dropped]
        try:
            det=",".join(f"{k}:fr={v['fire_rate']:.2f},raw={v['mean_raw']:.0f},c={v['mean_cost']:.1f}s" for k,v in sorted(stats.items()))
            chosen=",".join(x["name"] for x in fill_pool)
            print(f"[attack] budget={budget:.0f}s cands={len(cands)} replay={replay_cost:.0f}/{replay_cap:.0f} slowest={slowest:.1f}s warm={warm_elapsed:.0f}s pool=[{chosen}] | {det}", file=sys.stderr, flush=True)
        except Exception: pass
        order=sorted(range(len(cands)), key=lambda i: cand_raw[i], reverse=True)
        return [cands[i] for i in order]
