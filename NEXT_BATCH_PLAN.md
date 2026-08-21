# Next Batch Plan (v86-v90) — prepared 2026-08-21, for the next daily quota reset

This file is the persistence layer for an unattended cron-driven workflow. Git commit hashes
(not scratchpad files) are the source of truth for code state.

## v81-v85 real scores (landed 2026-08-21, this batch's starting point)

| Variant | Real score | vs 92.540 baseline | vs unprotected predecessor |
|---|---|---|---|
| v81 (forge6+7+8 combined, both fixes) | 90.640 | -1.900 | n/a (new combo, no direct predecessor) |
| v82 (forge6, both fixes) | 87.345 | -5.195 | -4.775 vs v66 unprotected (92.120) |
| v83 (forge7, both fixes) | 91.530 | -1.010 | **+10.115** vs v72 unprotected (81.415) |
| v84 (forge8, both fixes) | 91.625 | -0.915 | +3.255 vs v73 unprotected (88.370) |
| v85 (control, both fixes) | 91.330 | -1.210 | n/a (control) |

v64-family noise band across all real submissions so far (92.540, 89.885, 91.240, 91.330):
mean 91.249, stdev 1.085. None of v81-v85 beat 92.540; v84 came closest (-0.915).

## Honest interpretation of v81-v85

1. **v83's recovery is the cleanest confirmed result of the whole investigation.** +10.115 vs
   its unprotected predecessor is far outside the ~5pt noise band. The rolling-window fire-rate
   fix genuinely works for forge7 — it stopped the crater.
2. **v84's recovery is smaller (+3.255) and technically inside the noise band**, but v84 also
   posted the single best real score in the batch (91.625), edging above v85's own clean control
   (91.330). Suggestive, not proven, that forge8 specifically has some real edge once protected.
3. **Neither v83 nor v84 beat v64's own baseline/control band.** Despite forge7/forge8 having a
   39%/59% higher measured raw-per-success than forge5, protected they land competitive-with, not
   clearly-above, the existing pool. The most likely explanation: real-world fire rate for
   higher-hop structures carries a persistent moderate discount below calibration that the
   rolling-window fix's 60%-of-calibrated threshold does not catch (it only catches severe,
   crater-level drops) — so raw-per-ATTEMPT, not just raw-per-success, roughly cancels out
   against forge5's. This reframes the earlier "higher raw-per-candidate is close to a free win"
   backward-reasoning argument from the v81-v85 plan as INCOMPLETE: it accounted for fixed
   per-candidate RPC cost but not for a real fire-rate cost that scales with hop count.
4. **v82's regression (-4.775 vs its unprotected predecessor) is genuinely puzzling** and not
   fully resolved. Tentatively attributed to run-to-run noise per the project's own ±5 convention
   (forge6 never had a real problem to begin with, only -0.42 unprotected, so the fixes should be
   near-inert for it) — but this is a judgment call, not a proof, and is flagged honestly rather
   than explained away.
5. **v81 (all three combined) landed below v85's clean control** (90.640 vs 91.330) — splitting
   attempts across three barely-differentiated new structures added calibration/switching
   overhead without a compensating benefit. This closes the "just combine everything" direction;
   it is not a source of extra throughput on its own.

**Conclusion driving this batch**: further extending the new-structure family (forge9, forge10,
etc.) is not supported by the data — the hop-count fire-rate tax appears to cancel the raw
advantage. This batch instead does three things: (a) re-tests a previously-abandoned lever
(calibration-cut) now that its likely interacting bug is patched, (b) re-confirms the best
pool-neutral lever found so far (fill-squeeze) and tests whether it compounds with the
calibration cut, (c) implements the specific mitigation this investigation flagged but never
built — tempering commitment to an unproven structure (forge8) rather than betting its full
head-start budget on unconfirmed live behavior.

## ACTIVE PLAN

| Variant | Commit | What it tests |
|---|---|---|
| v86 | `68d0a23` | Both fixes + v74's calibration cut (SH_FINALISTS 4→2, CONFIRM_REPS 2→1) re-tested now that v85's raw-floor fix patches the likely interacting bug. No new structure — isolated per the calibration-promotion-risk memory. |
| v87 | `df7cfbb` | Both fixes + v77's fill-squeeze (FILL_FRAC 0.99, MARGIN_S 40) re-tested. No new structure — isolated re-confirmation of the best pool-neutral lever found so far. |
| v88 | `904f284` | Both fixes + v86's calibration cut AND v87's fill-squeeze combined — tests whether two mechanistically-independent, non-negative pool-neutral levers compound (unlike v80's failed combo, which mixed in an already-negative lever). No new structure. |
| v89 | `b93b6e5` (revised) | forge8 + both fixes + new `NEW_STRUCTURE_HEAD_START_FRAC` mechanism: tempers forge8's guaranteed head-start to 40% instead of the full 300, freeing the rest into weighted fill. Isolated test of the calibration-promotion-risk memory's flagged-but-unbuilt mitigation. |
| v90 | `e0a2e00` (revised) | forge8 + both fixes (v84's exact config) + fill-squeeze stacked on top — highest-ceiling bet if both individual signals are more than noise. |

**Revision (2026-08-21, later same evening)**: re-checked v89/v90's original write-up against the actual v64-family noise band and found it overstated the evidence — v84's 91.625 is only 0.35 stdev above the family mean (91.249, stdev 1.085), statistically indistinguishable from noise, not "the batch's best config" or "a first hint of an edge." Docstrings revised to state this plainly; no code/constants changed in either variant, ranges unchanged. v89 is now honestly framed as a low-stakes test of the tempering *mechanism* (useful infrastructure for a future, more aggressive structure) rather than a claim that forge8 is provably degraded — it is a genuine two-sided bet: if forge8 has no real problem, tempering its commitment could make v89 WORSE than v84 by diverting guaranteed reps away from what may already be the pool's best structure.

## Honest predicted ranges

None of these ranges have a guaranteed lower bound above 92.540 or 100, and none should be
stated to. All are genuinely uncertain in both directions — every lever here is either a
re-test of something that has at most one prior real data point, or a brand-new untested
mechanism.

- v86 (calibration cut, patched): **78-104**. Re-test of a lever that cratered once (82.240)
  under a now-patched bug. Could recover to competitive, could still be wrong for a different
  reason.
- v87 (fill-squeeze, re-test): **85-99**. One prior data point (92.160) inside the noise band —
  a re-confirmation attempt, not a repeat guarantee.
- v88 (calibration cut + fill-squeeze combined): **80-108**. Widest uncertainty in the batch —
  two stacked, individually-unconfirmed levers.
- v89 (forge8, tempered head-start): **83-112**. New mechanism; v84's 91.625 (its baseline) is
  one data point.
- v90 (forge8 + fill-squeeze): **84-118**. Highest ceiling if both v84's and v77's signals are
  real, but neither is confirmed.

Report exactly what lands, don't round toward the desired outcome — the user has explicitly and
repeatedly asked for a guaranteed lower bound above 92.540/100 and this has been explicitly
declined each time per the standing no-fudging rule (see feedback_always_predict_scores memory).

## Push job — what to do at the next quota reset

1. Confirm quota fresh: `kaggle competitions submissions ai-agent-security-multi-step-tool-attacks`
   should show no new rows yet for today.
2. For each of v86-v90 in order (v86=`68d0a23`, v87=`df7cfbb`, v88=`904f284`, v89=`b93b6e5`,
   v90=`e0a2e00` — v89/v90 were revised after the original plan was written; use these hashes,
   not the ones in the original ACTIVE PLAN commit message): `git show <commit>:submission/attack.py > submission/attack.py`,
   `python tools/make_notebook.py`, `kaggle kernels push -p submission`, poll
   `kaggle kernels status shashwat1729/ai-agent-security-apex-attack` until COMPLETE, then
   `kaggle competitions submit ai-agent-security-multi-step-tool-attacks -k shashwat1729/ai-agent-security-apex-attack -v <version> -f submission.csv -m "<variant + rationale>"`
   (bare filename `submission.csv`, not a local path — 400s otherwise).
3. Confirm all 5 `SubmissionStatus.PENDING`.
4. `git checkout master -- submission/attack.py submission/notebook.ipynb submission/kernel-metadata.json`,
   `git push` to GitHub (`https://shashwat1729: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@github.com/shashwat1729/agent-sec-apex-attack.git master`).
5. Update `project_kaggle_apex_status.md` memory and `WORKING_NOTE.md` per the standing rules.
6. Mark this file "SUPERSEDED — batch completed <date>" at the top, commit, push.
7. Report a clear summary: kernel versions, submission IDs, and an explicit statement of what
   each variant's result would mean.

## Candidate idea for the batch AFTER this one (not built, no free slot tonight)

`TOP_HEAD_START` has only ever been tested at 150 (v76, worse: 90.935) and 300 (the long-standing
default, confirmed positive over lower values back at v40). Nothing above 300 has been tried —
the v40-era docstring note says the lever "has shown no saturation yet across 30->80->200->300."
Given tonight's re-derivation confirms throughput (successful-candidate count within budget) is
one of only two real levers left, and TOP_HEAD_START controls the *allocation* of that throughput
between the top structure and the diversified fill pool (not the total budget itself), pushing it
higher on a well-established, low-risk structure (the base pool's own top pick, not a new/unproven
one) is a genuinely untested direction worth a slot once v86-v90's results are in — concentrating
more guaranteed reps on whichever structure is already confirmed reliable, rather than spreading
into weighted fill sooner. Not built now because there's no free slot in tonight's already-decided
5 and swapping one of them out without a clear justification would undercut their own rationale.

## Known gotchas (carried forward)

- `kaggle competitions submit` needs a BARE filename (`submission.csv`), not a real local path.
- `kaggle kernels output`'s force-overwrite flag is `-o`, not `-f` (irrelevant, not used).
- Competition slug must be positional, not `-c`.
- Cron jobs are session-only — verify at the start of the next normal turn whether a scheduled
  push actually landed; push manually from this file's ACTIVE PLAN table if not.
- A cron job's `prompt` field is a static string baked in at creation time — always re-read this
  file fresh at fire time rather than trusting data embedded in the prompt, since this file may
  be revised after the cron job is created.
