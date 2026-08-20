# Next Batch Plan (v81-v85) — prepared 2026-08-20, for the next daily quota reset

This file is the persistence layer for an unattended cron-driven workflow. Git commit hashes
(not scratchpad files) are the source of truth for code state.

## Context — why this batch is different from v76-v80

v76-v80 (pushed 2026-08-20 ~00:05-00:09 UTC) were defensive: pool-neutral budget-lever tweaks
plus two control resubmits, explicitly designed to avoid regression after v72/v74's real
craters. The user reviewed that whole run (v71-v80, all landed at or below 92.540, several well
below) and pushed back hard: "you are not innovating anything new ... think properly." That
criticism is fair — v76-v80 tested no new idea, just avoided risk.

This batch (v81-v85) is a genuine mechanism-level fix, not a knob tweak. Investigation (source
read of the `_search` fill loop, `submission/attack.py` ~line 1150-1230) found a concrete,
provable throughput-loss bug: the fill loop's only protection against a `top` structure whose
REAL live fire rate is worse than its calibration sample is a 6-CONSECUTIVE-FAILURE streak.
Math (verified): for a structure with true fire rate in the realistic 55-95% range, the expected
number of attempts before 6 consecutive fails occur ranges from ~200 (at 55%) to tens of millions
(at 95%) — i.e. this safety valve is asymptotically inert at any realistic degradation level.
Every attempt (success or fail) costs one real generation round-trip, so a structure sitting at
e.g. fire_rate=0.75 silently wastes ~25% of its ENTIRE `TOP_HEAD_START` budget on failed attempts
that produce zero score, without ever triggering the old drop. This is a strong, source-verified
candidate explanation for why forge7 (v72, -11.1) and forge8 (v73, -4.2) cratered when reintroduced
— they are far less battle-tested than forge2-5 (only a handful of calibration probes vs. dozens
of historical real submissions), so a lucky small calibration sample could easily overstate their
true live fire rate.

A SEPARATE mechanism was also identified for v74's crater (calibration cut alone, -10.3, no new
structures — the fire-rate fix above doesn't apply since no new/less-tested structure was
involved): `top = usable[0]` picks the single highest eff-ranked structure with no floor on
`mean_raw` — a cheap-but-low-value structure (e.g. `deputy`, raw~6) can win pure eff-ranking on a
noisy small sample despite contributing little raw per completion, especially with fewer confirm
reps. v85 addresses this independently.

**Fixes implemented and validated locally (`tools/local_test.py` — syntax/AST clean, pool
composition and raw values confirmed correct on all 5, no tracebacks):**
- `ROLLING_WINDOW`/`ROLLING_MIN_RATIO` (v81+): a live rolling fire-rate check every 20 attempts
  per structure, dropping it if live rate falls below 60% of its calibrated rate — reacts within
  one window instead of hundreds-to-thousands of wasted attempts.
- `ROLLING_TOP_RAW_FRAC` (v85 only): the head-start pick must have `mean_raw` >= 50% of the
  pool's own best measured raw, or the next-best eligible structure is used instead.

## ACTIVE PLAN

| Variant | Commit | What it tests |
|---|---|---|
| v81 | `1f181fc` | Rolling-window fix ALONE on v64's exact pool (no new structure) — isolates whether the mechanism itself is harmless/neutral |
| v82 | `31a1e2d` **(revised)** | BOTH fixes (rolling-window + raw-floor) + forge6 reintroduced (v66 landed flat/-0.42 unprotected) |
| v83 | `99f5b3f` **(revised)** | BOTH fixes + forge7 reintroduced (v72 landed 81.415/-11.1 unprotected — the strongest test, biggest crater = most to recover) |
| v84 | `228b149` **(revised)** | BOTH fixes + forge8 reintroduced (v73 landed 88.370/-4.2 unprotected) |
| v85 | `d26e4fe` | Raw-floor fix (+ rolling-window fix present but no new structure) ALONE on v64's pool — isolates the SEPARATE mechanism behind v74's crater |

**Revision note (same day, before push)**: v82/v83/v84 were upgraded to stack BOTH fixes (not
just the fire-rate fix) after further review found the raw-floor fix is structurally near-inert
for forge6/7/8 specifically — each is the highest-raw structure in its own pool by construction,
so it trivially clears any reasonable floor. Stacking costs nothing in attribution clarity (a
score change in these variants is still most plausibly the fire-rate fix's doing) while adding
real insurance against the separate mis-promotion failure mode v85 targets. v81 and v85 remain
the clean single-mechanism isolation tests.

All 5 validated locally, committed, NOT yet pushed to Kaggle (today's 5/5 quota was already used
by the v76-v80 push). Push at the next quota reset (~05:35 IST / ~00:00 UTC), per the standing SOP.

## Honest interpretation guide (fill in once real scores land)

- If v81 ≈ v64 (within noise) and v82/v83/v84 all beat their unprotected predecessors (v66, v72,
  v73) meaningfully: strong confirmation of the throughput-loss hypothesis — the mechanism is
  real and worth extending (larger pool, maybe forge6+7+8 all together, now protected).
- If v81 alone already beats v64: possible that some of v64's OWN existing structures were also
  quietly bleeding throughput to this bug (less likely given they're heavily battle-tested, but
  not ruled out).
- If v82/v83/v84 do NOT recover vs. their unprotected predecessors: the fire-rate throughput-loss
  hypothesis is wrong or insufficient — forge6/7/8's real problem is something else (e.g. genuinely
  lower per-candidate RAW value on the real model, not fire rate), and the boundary-extension
  direction should be treated as closed, not just paused.
- v85 vs v64: if v85 beats v64 clearly, the raw-floor fix has independent value even without any
  new structure — worth keeping in the base config going forward. If flat, v74's crater mechanism
  may need a different explanation than the one hypothesized here — report honestly, don't force
  a confirmation.

Do not fabricate confidence in the write-up once scores land — this is a well-reasoned, source-
verified hypothesis with working local validation, but it has NEVER been tested against the real
stochastic model. It could easily be wrong, partially right, or right but insufficient to reach
100+. Report whatever the real data actually shows.

## Push job — what to do at the next quota reset

1. Confirm quota fresh: `kaggle competitions submissions ai-agent-security-multi-step-tool-attacks`
   should show no new rows yet for today.
2. For each of v81-v85 in order: `git show <commit>:submission/attack.py > submission/attack.py`,
   `python tools/make_notebook.py`, `kaggle kernels push -p submission`, poll
   `kaggle kernels status shashwat1729/ai-agent-security-apex-attack` until COMPLETE, then
   `kaggle competitions submit ai-agent-security-multi-step-tool-attacks -k shashwat1729/ai-agent-security-apex-attack -v <version> -f submission.csv -m "<variant + rationale>"`
   (bare filename `submission.csv`, not a local path — 400s otherwise).
3. Confirm all 5 `SubmissionStatus.PENDING`.
4. `git checkout master -- submission/attack.py submission/notebook.ipynb submission/kernel-metadata.json`,
   `git push` to GitHub (`https://shashwat1729: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@github.com/shashwat1729/agent-sec-apex-attack.git master`).
5. Update `project_kaggle_apex_status.md` memory and `WORKING_NOTE.md` per the standing rules —
   include the mechanism explanation above, not just the score numbers, since this batch's whole
   point is testing a hypothesis, not a knob.
6. Mark this file "SUPERSEDED — batch completed <date>" at the top, commit, push.
7. Report a clear summary: kernel versions, submission IDs, and an explicit statement of what
   each variant's result would mean per the interpretation guide above.

## Known gotchas (carried forward)

- `kaggle competitions submit` needs a BARE filename (`submission.csv`), not a real local path.
- `kaggle kernels output`'s force-overwrite flag is `-o`, not `-f` (irrelevant, not used).
- Competition slug must be positional, not `-c`.
- Cron jobs are session-only — verify at the start of the next normal turn whether a scheduled
  push actually landed; push manually from this file's ACTIVE PLAN table if not.
