# Next Batch Plan (v91-v93) — prepared 2026-08-22, for the 2026-08-23 quota reset

**Context: competition Entry Deadline is 2026-08-25.** Confirmed via live web search
(kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks). At most 2-3 daily quota
resets remain (tomorrow 08-23, 08-24, maybe a final morning window 08-25). Final placement is
decided by the **Private Leaderboard** on up to 2 user-selected Final Submissions (rules_page.txt
line 115); if not selected, Kaggle auto-picks. This changes priorities: stop chasing sub-5-point
public deltas as if they were signal, and start thinking about (a) genuinely untested levers worth
one of the few remaining slots, and (b) which 2 submissions to explicitly select before the deadline.

## v86-v90 real scores (landed 2026-08-22)

| Variant | Real score | vs v85 control (91.330) | vs v64-family mean (91.249) |
|---|---|---|---|
| v86 (calibration cut, patched) | 89.030 | -2.300 | -2.219 |
| v87 (fill-squeeze re-test) | 91.055 | -0.275 | -0.194 |
| v88 (calib cut + fill-squeeze) | 89.380 | -1.950 | -1.869 |
| v89 (forge8, tempered head-start) | 90.590 | -0.740 | -0.659 |
| v90 (forge8 + fill-squeeze) | 89.255 | -2.075 | -1.994 |

Batch mean 89.862, below both the v85 control and the v64-family mean. Full 14-sample real-score
history (v64-family + v81-v90) mean ≈ 90.484. **None of v81-v90 (10 submissions) have beaten the
single 92.540 sample.** Honest read: this is consistent with 92.540 being the upper tail of a noisy
distribution (confirmed noise band stdev ~1.1, and community-reported same-bytes swings of 2-12
points — see `research/kaggle/public_notebooks.md` "signals" #1), not proof every subsequent lever
regressed. But two results ARE real signal, not noise:

1. **v86's calibration cut (SH_FINALISTS 4->2, CONFIRM_REPS 1), now under both fixes, still landed
   below control (89.030 vs 91.330).** This is the SECOND independent data point (after v74's
   pre-fix 82.240) showing reduced calibration confidence costs real score. Not explained away by
   the fixes this batch patched — it's a persistent, separate effect. v88 (which stacks this same
   cut with fill-squeeze) also underperforms (89.380), consistent with the cut being the drag.
2. **v87's fill-squeeze (FILL_FRAC 0.99, MARGIN_S 40) landed at 91.055, its second real data point**
   (first was 92.160, pre-this-batch). Mean of the two: 91.6, tightly inside the control noise band —
   this confirms fill-squeeze is genuinely noise-neutral, not a real lever in either direction.
3. **v89 (forge8, tempered) at 90.590 and v90 (forge8 + fill-squeeze) at 89.255 both landed BELOW
   v84's own untempered forge8 config (91.625).** Both attempts to modify or combine with v84's
   config made it worse, not better — a now-consistent pattern (matches v81, v88 also underperforming
   their simpler halves) that stacking/modifying a lever inside the same variant tends to cost more
   than it gains, at least at this batch's sample size of n=1 per cell.

## H1 refuted by source read (2026-08-22) — do not implement

Investigated whether encoding our own `SECRET_MARKER` payload (base64/hex/url) would hedge against a
stricter private guardrail. Direct read of `predicates.py` (`_contains_secret`, lines 124-165) shows
the reversible-decode pass only applies to real fixture secrets actually read via `fs.read`
(guardrail-blocked, we never do this) — our own literal `SECRET_MARKER` is checked as an *undecoded*
substring. Encoding it would make the EXFILTRATION predicate NOT fire at all — 0 raw instead of 16,
on both public and private scoring (same scorer, staff-confirmed). See
`research/synthesis/next_steps.md` H1 section for the full trace. This would have cost a real
submission slot to discover the hard way; caught it from source instead.

## ACTIVE PLAN — v91, v92, v93

Both v91 and v92 are branched from `d26e4fe` (v85's clean control, real score 91.330 — no
calibration change, no fill-squeeze, no new structure), each with exactly ONE isolated change, for
clean attribution. v93 is v85's control resubmitted byte-for-byte.

| Variant | Commit | What it tests |
|---|---|---|
| v91 | `a6619b0` | `TOP_HEAD_START` 300 -> 450. **First-ever test above 300** in this project's history (only 150 and 300 have real data: 150 scored 90.935, worse; 300 has been the default since v40 with "no saturation yet" noted at every prior step 30->80->200->300). Directly targets the ceiling model's remaining free variable: allocation of confirmed throughput between the top structure and the diversified fill pool. Flagged in the prior NEXT_BATCH_PLAN, never built until now. |
| v92 | `8e50015` | Calibration confidence RAISED (opposite of v86's cut): `SH_FINALISTS` 4->6, `CONFIRM_REPS` 2->3 (v25's original value). Direct response to v86 landing below control a second time — if cutting confidence costs real score, raising it should be neutral-to-positive. Genuinely untested direction (every prior calibration experiment in this project's history has been a CUT, never an increase past the v25 baseline). |
| v93 | `d26e4fe` (byte-identical resubmit of v85) | Best-of-public re-roll. Community-confirmed same-bytes variance is 2-12 points (public_notebooks.md); v85's one real sample (91.330) is solid but a second roll of the identical config could land closer to — or above — 92.540 purely on search-stochasticity luck. With only ~2-3 windows left before the deadline, resubmitting a known-good, well-understood config to fish for a high roll is a legitimate use of a slot, not wasted effort — especially since whichever roll scores highest becomes a strong candidate for one of the 2 Final Submissions. |

## Honest predicted ranges

- v91 (TOP_HEAD_START 450): **80-108**. Untested direction; could continue the "no saturation" trend
  (upside) or find the ceiling where the top structure's own fire-rate/compliance degrades under an
  even larger uninterrupted run before diversifying into fill (downside). No prior data point at 450.
- v92 (calibration confidence raised): **86-104**. Motivated by a real, now twice-confirmed negative
  result in the opposite direction, but "cutting confidence hurts" does not guarantee "raising it
  helps" by the same magnitude — could just cost calibration wall-clock for a wash.
- v93 (v85 byte-identical re-roll): **83-113**. Same distribution v85 itself was drawn from (its own
  91.330 sample); this is a second draw from that same distribution, not a different config.

No lower bound above 92.540 or 100 is claimed for any of these — per the standing no-fudging rule.

## Push job — what to do at the next quota reset (2026-08-23, ~05:35 IST)

1. Confirm quota fresh: `kaggle competitions submissions ai-agent-security-multi-step-tool-attacks`.
2. For each of v91 (`a6619b0`), v92 (`8e50015`), v93 (`d26e4fe`) in order:
   `git show <commit>:submission/attack.py > submission/attack.py`, `python tools/make_notebook.py`,
   `kaggle kernels push -p submission`, poll `kaggle kernels status
   shashwat1729/ai-agent-security-apex-attack` until COMPLETE, then
   `kaggle competitions submit ai-agent-security-multi-step-tool-attacks -k
   shashwat1729/ai-agent-security-apex-attack -v <version> -f submission.csv -m "<variant +
   rationale>"` (bare filename `submission.csv`).
3. Only 3 variants this batch (not 5) — 2 quota slots deliberately left free. With the deadline this
   close, keep 1-2 slots in reserve in case v91/v92/v93's real scores suggest an obvious same-day
   follow-up (e.g. if v91 shows continued upside, immediately test 600; if it shows a ceiling,
   that's also useful to know before the deadline) rather than committing all 5 slots to a plan made
   before today's results are in.
4. Confirm all `SubmissionStatus.PENDING`, restore `submission/` to clean HEAD state, push to GitHub.
5. Update `project_kaggle_apex_status.md` memory and `WORKING_NOTE.md`.
6. Mark this file superseded, commit, push.
7. **New this batch**: once v91/v92/v93 real scores land, review the full submission history and
   explicitly select the 2 Final Submissions in the Kaggle UI (Submissions tab) rather than leaving
   it to auto-select — pick the single highest real score, plus one submission that includes the
   deputy hedge (CONFUSED_DEPUTY leg) for structural diversity in case the private guardrail
   penalizes pure-EXFIL-only traces differently than the public one. Do not leave this to the
   deadline; Kaggle's auto-select behavior on ties/missing selection is not something to rely on.

## Known gotchas (carried forward)

- `kaggle competitions submit` needs a BARE filename (`submission.csv`), not a real local path.
- Competition slug must be positional, not `-c`.
- Cron jobs are session-only — verify at the start of the next normal turn whether a scheduled push
  actually landed; push manually from this file's ACTIVE PLAN table if not.
- A cron job's `prompt` field is a static string baked in at creation time — always re-read this file
  fresh at fire time rather than trusting data embedded in the prompt.
- **New**: do not implement H1 (encoded SECRET_MARKER) — see refutation above. If a future session's
  research surfaces it again independently, this file already has the source-level answer.
