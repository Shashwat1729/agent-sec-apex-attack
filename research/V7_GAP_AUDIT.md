# V7 Gap Audit — Strict Reviewer Report (bar: 9.5+, functional is not passing)

**Date:** 2026-09-06 | **Scope:** `docs/WORKING_NOTE_V7.md` (3644 nonblank lines / 4439 physical / ~63,700 words / ~450 KB) vs `research/SCORING_RUBRIC_DEEPDIVE.md` (weights C1 30% / C2 25% / C3 20% / C4 15% / C5 10%+veto) vs `research/WINNING_NOTES_A_25.md` + `B_25.md` (50-note patterns).
**Read:** V7 lines 1-150 (title/scope/TLDRs/TOC), Sec 6 hero Table 7-A + triplets + ship-log (lines 265-433), Sec 8/8a/8b self-test + autopsy (lines 541-608), Sec 7 Pareto (lines 522-539), Sec 25 V7-A..V7-F (lines 4363-4439), appendices headers (Sec 22/23/24, V6-A..V6-O).
**Verdict: V7 is content-PASS, packaging-FAIL. Estimated weighted score ~6.5/10 — not 1st-position. V7 finished P0 *presence* (every needle exists) but not P0 *discipline* (budgets violated everywhere). V8 must delete, not append: the byte-identical preservation doctrine is the single largest blocker to 1st.**

| Criterion (weight) | Score /10 | One-line brutal truth |
|---|---|---|
| C1 Clarity + reproducibility (30%, gate) | **6.0** | Science is traceable; the skim-path drowns in 4 stacked TL;DRs and 1867 table-rows. |
| C2 Methodological contribution (25%) | **6.5** | Real levers, fake triplets, retrofitted ship rule, no unified field harness. |
| C3 Security insight (20%, multiplier) | **7.0** | Sharpest section, but wall-clock is INFERRED and the headline exhibit is double-CLAIM. |
| C4 Usefulness (15%) | **6.0** | Generous checklist, no runnable factory (no JSON, no notebooks, no SETTINGS dump). |
| C5 Responsible communication (10% + VETO) | **7.0** | Honest voice, label inflation (706 INFERRED), veto risk not yet zero. |
| **Weighted total** | **~6.5** | **Gap to 1st is ~3 points, all in discipline, not science.** |

> Scoring note: 9.5+ means a reviewer can re-run the headline in 5 min, audit everything in 30 min, and trust every number's label. V7 scores 6-7 because each criterion has at least one load-bearing violation (named below). No partial credit for "needle present but buried."

---
## 1. Per-criterion audit (score + strengths + weaknesses + V8 fixes with section/line/example)

### C1 — Technical clarity + reproducibility (30%, GATE). Score: 6.0/10

**Strengths (keep).**
- Every claim carries file:line (`templates.py:39-50`, `optimal.py:51-58`, `all_submissions_FULL.txt` refs throughout Sec 6/22).
- V7 TL;DR is 6 numbered sentences (lines 17-22) with hook-first ordering + criteria callout box (lines 24-25) + contents TOC (line 27) + Fig 1 pipeline at line 109 with thickness=wall-clock + caption/interpretation.
- Hero Table 7-A exists at lines 301-313 (methods x treatments, Optiver-5x5 style) + seed-triplet box (315-316) + ship-log table (318-330).
- Idea -> fence (10-25 lines, runnable, Expected) -> isolated delta shape holds in Sec 4.1-4.4 and Sec 8 self-test (lines 566-590, Expected output + 60-s falsification rule).

**Weaknesses (load-bearing, brutal).**
- **W1 — 63,712 words vs 1800-2500 center (~28x) / 5500 cap (~11.6x).** `writeup_style_guide.md:38` award window is WORDS, not lines. V7-D (line 4425) redefines the gate as "narrative lines 3600-4200 (task window): PASS" — category error and self-graded fiction. A reviewer hitting a 63k-word note with a 5-min budget skims the first screen and scores C1 down before Sec 6. *Ref: V7 lines 4423-4433 verification table.*
- **W2 — Four stacked TL;DRs + three stacked TOCs + four stacked scopes.** V7 TL;DR (line 15) + V4 TL;DR (line 35) + V6 TL;DR (line 53) + base TL;DR (line 80); V7 contents (line 27) + V4 contents (line 45) + base contents (line 76); V7/V5/V4/V3 scope lines (lines 7-11). The "diff in one minute" blocks (lines 29-33, 47-56) do not fix the reader cost: ~250 lines of meta before Sec 1 science. Preservation doctrine ("byte-identical except…", lines 31/54) is the root cause — V7 appended, never deleted.
- **W3 — Hero table buried behind two warm-up tables.** Reviewer meets era Table W-E1 (8 rows, lines 274-282) then climb Table 3 (6 rows, lines 290-297) before hero Table 7-A (line 301). Table 7-A itself has 8 rows mixing levers/controls/sizing, and its N=5 row (+1.16, "marginal - ceiling marker") contradicts climb Table 3 which ships +1.16 as a lever row (line 297). Own <5-noise rule (line 267) is violated by the note's own centerpiece adjacency.
- **W4 — Table/figure/fence bloat.** 1867 pipe-table lines, 11 figure embeds (cap is 3-5 per `guide:72`), ~46 code fences. Narrative tables break the 8-row gate: Table 4 (15 rows, lines 349-362), Tables 5b/5c (12+ rows each, lines 397-431). Appendix V6-B uses 25-row bands (line 3355: "26 bands of 25") against the 12-row appendix gate V7 claims in V7-D (line 4428).
- **W5 — Reproducibility is commands, not a factory.** V7-A (lines 4382-4384) admits "SETTINGS-equivalent = config.py values, not a separate JSON — stated so fresh clones do not hunt a missing file." That is an excuse, not an artifact. The "experiments registry" is a markdown table (lines 4371-4380), not an `experiments.json`; "numbered run order 01-05" (lines 4388-4395) has no linked notebooks, no BASE_PATH convention, no weight/dataset URLs, no OOM log beyond one config flag. CommonLit (B#20) / TalkingData (B#14) pattern requires clickable artifacts.

**V8 fixes (section + line ref + example text).**
- **F1 (Sec: new core / delete stacked intros; refs V7:15,35,53,80 + V7:27,45,76).** Single TL;DR (5 sentences, each <=30 words), single TOC, single 80-word scope. Demote V4/V5/V6 TL;DRs to a 5-line "version log" after Sec 14. Example replacement sentence 1: "We score all 810 solutions and show public LB is a throughput game on one blind-spot primitive, peaking at a ~91-92.5 band (seed-123 best 92.540) that collapses to 0.07 median private."
- **F2 (Sec 6; refs V7:274-313).** Hero Table 7-A FIRST in Sec 6 (<=6 rows, levers only); move W-E1 era + Table 3 climb to Sec 6.0 supplement; drop the +1.16 row from lever tables to a "ceiling marker" footnote so the <5-noise rule holds everywhere. Example footnote: "N=5 +1.16 sits inside the <5 noise band (disc 733345) — ceiling marker, not a lever."
- **F3 (Sec 13 + new `experiments.json`; refs V7:4382-4395).** Ship real files: `experiments.json` (one object per lever: generator/config/seed/cost/delta), `notebooks/01-05` linked with BASE_PATH + artifact URLs, dumped `SETTINGS.json` + `requirements.txt` verbatim. Acceptance: fresh clone runs bash 1-6 to 5/5 PASS without asking the author.
- **F4 (Whole note; ref V7:4423-4433).** Rewrite V7-D gates in WORDS (core 2500-3500) and enforce narrative <=8 rows / appendix <=12 rows mechanically (split V6-B 25-bands into 12-row chunks; move Tables 4/5b/5c full bodies to appendix, keep <=8-row narrative cuts).

### C2 — Methodological contribution (25%). Score: 6.5/10

**Strengths.**
- Transferable method stated as rule: throughput-first search (forge + halving race + validate-then-keep), Sec 4/6 with isolated deltas (+27.5, +4.84/+3.93 ladder, +7.90, N-boundary bar Fig 3 line 221-223).
- Ship rule + stop rule + override log exist (lines 318-330 ship-log table; V7-B lines 4397-4401 three overrides; stop rule "no lever beat v64 in 41 tests, ceiling ~91-92.5").
- Rejected-alternatives section (line 219: evolutionary/MCTS/Go-Explore with cost argument) + recovery proof v83 +10.1 (line 511).

**Weaknesses.**
- **W1 — Seed-triplets are fake triplets (MAP A#16 / Jigsaw A#12 violation).** Box at lines 315-316: "seed-123 primary; v64-exact rerolls 85.800-91.860" — those rerolls are hosted resubmits on different days (v105/v109/v97/v100/v98), i.e. confounded wall-clock/stochastic draws, not seeded reruns. No mean+-std, no ensemble column, no "which metric to trust" line. Headline still ships as point "92.540" in Tables 3/5b/7-A titles.
- **W2 — Ship rule is retrofitted and self-contradicted.** Rule (line 319): "ship iff 3-seed mean delta > 5 AND fire_rate gain holds at CALIB_HOPS=8." Override #1 (V7-B line 4399) admits the central THS ladder (+4.84/+3.93 per step) shipped BELOW threshold on "cumulative +9.4" logic — the rule rejects the note's own ladder. Override #2 (line 4400) admits the private-correct move (deputy-primary) was vetoed by the public rule — the rule optimizes the wrong objective. A rule violated by its two most important decisions is decoration.
- **W3 — No unified harness for field comparisons.** Sec 8b (lines 604-608) credits V15 90.54 [VERBATIM code-read] / JED-v25 89.145 [VERBATIM code-read] against v64 92.540 as if same-protocol, but these are different dates/refreshes — violating the note's own freeze-date 2026-08-07 comparability rule (line 89: "pre/post-refresh NOT comparable"). No REAL_REPLAY_CEILING=150 normalized re-score, no date-segment control.
- **W4 — Small-n selection bias unquantified (Lonnie B#6).** v64 is max-of-105 on a +-5/2-12 noise band; expected max-inflation never computed; no multiple-comparison note. The "ceiling ~91-92.5" (line 330) is asserted from the same selected sample.

**V8 fixes.**
- **F1 (Sec 6, refs V7:315-316,301-313).** Real triplet per headline: 3 seeded runs + mean+-std + ensemble column, or downgrade to band. Example: "v64 config: 92.540 (seed 123) / 85.800 / 91.860 (hosted rerolls, confounded) / band mean ~89.6+-2.6 — headline is the BAND ~91-92.5, trust the band, not the point (MAP pattern)." Never print "92.540" without the band in the same row.
- **F2 (Sec 6 + V7-B, refs V7:318-330,4397-4401).** Split the ship rule in two (public-ship vs private-hedge objectives) and re-log overrides against the correct objective. Example: "Public-ship: 3-seed mean >5 at CALIB_HOPS=8. Private-hedge: survivability-first (deputy share >=70% or pure-deputy entry) regardless of public delta. Override #2 reclassified: correct hedge vetoed by wrong rule — cost the private board."
- **F3 (Sec 8b, refs V7:604-608).** Field-vs-ours comparison under identical replay ceiling + date segment, or label as incomparable. Example row: "V15 90.54 (pre-refresh, TITLE-date) vs v64 92.540 (post-refresh) — NOT same-protocol; normalized re-score pending [INFERRED comparison, do not rank]."

---
### C3 — Security insight (20%, domain multiplier). Score: 7.0/10

**Strengths.**
- Best mechanism chain in the note: first-present-arg blind spot (`optimal.py:51-58`, line 545), taint-5 superset predicate-2 (line 547), canonical-vs-substring (line 549), Harmony/ChatInject channel (line 551), Gemma GGUF cap (line 553), 10-line GPU-free self-test with Expected output + 60-s falsification rule (lines 566-590).
- Private-gap autopsy table 8a (lines 594-599) with per-component public-vs-private + transfer column (ASHRAE B#16 pattern) + miss-credit 8b (lines 604-608, MCTS/MDC pattern).
- Wall-clock side-channel Fig 6 (lines 527-529) + Pareto table (lines 531-538, Hydrogen dual-track pattern, D4 differentiator).

**Weaknesses.**
- **W1 — Wall-clock Pareto costs are INFERRED, not measured (Vesuvius B#9 violation).** Table rows (lines 535-537): "~13 h EXFIL-only", "~15 h [INFERRED from 738946 signal]", "mid-80s band / lowest". The 2 h side-channel story (line 536: "DENY-skips-hop1 ~1.5 s/cand x 2000") is arithmetic, not a ledger. No per-family wall-clock table from gateway timestamps; "we never instrumented it" (line 529, Sec 6.5 line 261) is confessed but not repaired — Santa-2024 B#4 requires the score-vs-compute CURVE.
- **W2 — Modal collapse on the private mechanism.** Line 545: 'Any payload that fires EXFIL necessarily contains "secret" ... so any private re.search("secret") closes both outright [INFERRED]' — prose says "necessarily/closes outright" (certainty), bracket says INFERRED (guess). INFERRED 706 hits (measured) means the tag is wallpaper; the reviewer cannot tell black-box reconstruction (738915) from source (`predicates.py`).
- **W3 — Artifact-control block is bullets, not a table (Malware A#21 gap).** Integrity box (lines 89-98) lists date/version/title/private controls as prose rows without paired numbers. Freeze-date 2026-08-07 comparability is STATED (line 89) but never EXECUTED as version/date-segment deltas before model-gain claims.
- **W4 — Per-stage gate ablation has no stage-3 numbers (RSNA B#2 gap).** Sec 5 pointer (line 256) claims "recall-gated fill vs keep-all fill" gate-ablation but only stage-2 numbers exist (31% -> ~100% fire); replay-survival under REAL_REPLAY_CEILING=150 for gated vs keep-all is asserted, not tabulated.

**V8 fixes.**
- **F1 (Sec 7, refs V7:527-539).** Publish measured per-family wall-clock ledger (gateway timestamps, n, mean s/cand) + truncation curve + N=4/5/6 cost bars, or mark the Pareto provisional. Example row: "forge5 pool: 13.1 h measured (n=2000, 6.5 s/cand gateway ts) vs deputy pool: 15.2 h measured — delta 2.1 h = DENY-skip effect [measured] / mechanism INFERRED."
- **F2 (Sec 8 para 1, ref V7:545).** Split certainty: source sentences (public, VERBATIM) vs inference sentences (private, INFERRED, confidence). Example rewrite: "Public: _extract_target returns first-present arg (optimal.py:51-58) [SOURCE]. Private: we INFER a re.search(secret)-class scan over sink args from 738915 wall-clock + hiranorm/takamichitoda controls (confidence: medium-high, not source) [INFERRED]."
- **F3 (Sec 1 integrity box, ref V7:89-98).** 4-row artifact-control TABLE with paired numbers (pre/post-freeze means, same-bytes resubmit spread, title-claim control, private-transfer control), Malware-7-liner style, before any lever delta.

### C4 — Usefulness to benchmark community (15%). Score: 6.0/10

**Strengths.**
- Sec 9 Table 8 checklist (lines 616-626) with metric/threshold/source per row; Sec 13 bash 1-6 (lines 764-787 per V6 map); keep/never-retry rule (line 608 + V6-E 50 lessons); Fig 11 + 6x4 matrix (V6-C/V6-D, lines 4189-4212); per-structure eff ranking (lines 212-217).

**Weaknesses.**
- **W1 — Factory artifacts do not exist as files (CommonLit B#20 / TalkingData B#14 fail).** See C1-W5. A reviewer cannot click anything: no `experiments.json`, no `notebooks/01-05`, no SETTINGS/requirements dump, no artifact URLs ("artifacts committed" line 4382 is unverifiable from the note).
- **W2 — Cost axis is hand-wave (Hydrogen B#8 fail).** Pareto (lines 533-538) has no params/latency columns and no small-model config; "mid-80s band / lowest" (line 537) and "same wall-clock, ~31% fire" (line 538) are adjectives where a 6-row efficiency table (score vs wall-clock vs config) belongs.
- **W3 — Exhaust path breaks its own gates.** V6-A 74 chunked in 7x~12-row tables: PASS. V6-B 630 in "26 bands of 25" (line 3355): FAILs the 12-row appendix gate; vote-sum reconciliation (5580, V6-N line 4335+) must be taken on trust in skim. Field HURT=0 rationale is quoted (`FIELD_CODE_ANALYSIS.md:110-111`) but the definition ("field HURT definitionally 0", scope line 19) makes the 49/38/722/1 synthesis table (line 19) a ours-vs-field category error a newcomer will misread.
- **W4 — No assignment matrix.** Analogue of MDC B#25 tool-assignment: which STRUCTURE wins which MODEL (forge5->gpt-oss, single_short/forge->gemma, line 217) is one prose sentence, not a structure-x-model matrix with eff/fire/cost cells.

**V8 fixes.**
- **F1 (Sec 25 V7-A + Sec 13; refs V7:4367-4395).** Real factory files + in-note links (see C1-F3). Add 6-row efficiency Pareto with numbers. Example row: "single_short 1-post (small-model pick): 84.x public [VERBATIM resubmit] / 6.5 s/cand / 1-post — copy this if GPU-hours matter."
- **F2 (Sec 24 V6-B; ref V7:3355).** Re-chunk 630 tail to <=12-row bands (or CSV pointer + 3-row sample per 100-rank block); add one-line HURT-definition warning above the 810 synthesis. Example: "Field HURT=0 by construction (no baseline to hurt) — 38 HURT are all ours; do not compare columns across populations."
- **F3 (Sec 4.3; ref V7:217).** Structure-x-model assignment matrix (rows: 9 structures; cols: gpt-oss eff/fire, gemma eff/fire, verdict) replacing the prose sentence.

### C5 — Responsible communication (10% + VETO). Score: 7.0/10

**Strengths.**
- Defense/Research-Only banner (line 3) + safety box at first forge use (lines 185-186, P0-5) + Sec 10 limitations (lines 630-645: private INFERRED, mock 6x gap, +-5 variance, ~19pt gap-to-frontier, cron failures, final-2 anti-trap, 710234 hygiene) + label legend (line 98) + override confessions (V7-B) + named miss-credit (V15/JED-v25/takamichitoda/aleaiest/738915).

**Weaknesses (veto-adjacent — read twice).**
- **W1 — Label inflation: INFERRED 706x.** Builder-script auto-tagging (V7-C line 4405: "enforced by tools/build_v7.py ... unless already labeled within +-60 chars") guarantees coverage and destroys signal. TITLE-CLAIMED 43x but per-number distribution sums to 26 (18+4+1+1+2, line 4406) — 17 occurrences untracked. VERBATIM 81x mixes "own Kaggle pull" with "code-read" without per-claim refs in-table.
- **W2 — Weaponizable token before defense in skim order.** TL;DR line 17 advertises "Harmony forge injection (+27.5)" at the top of the note; the exact control-token string ships in the Sec 4.2 fence (lines 193-199) with a one-line comment. Safety box (lines 185-186) sits correctly at first USE but AFTER the TL;DR advertisement — a safety reviewer skimming TL;DR->TOC->Sec 4 meets the capability claim before the defense pointer. `guide` pitfall #8 is satisfied literally, not in spirit.
- **W3 — Double-CLAIM exhibit carries the heaviest argument.** Rank-6 "95.130 [TITLE-CLAIMED] pub / 0.00 [TITLE-CLAIMED, author-admitted]" (line 598, 18 occurrences per V7-C) is used as "clean control" (line 545) and "cautionary exhibit" (line 598). Two self-claims do not make a control; the primary private evidence should be VERBATIM (takamichitoda 24.36 code-read, aleaiest 29.670 trap, own 63-row 0.045-0.210 pulls).
- **W4 — Responsible content exists outside the skim.** Sec 10 at lines 630-645 is ~600 lines deep; the "5-line Responsible box under TL;DR" promised by the rubric deep-dive never shipped (V7 TL;DR has a criteria box, lines 24-25, but no variance/gap/stop-rule bullets).

**V8 fixes.**
- **F1 (Whole note; ref V7:4403-4406).** Replace auto-tag wallpaper with per-table Label columns (Value | Status [VERBATIM/TITLE-CLAIMED/INFERRED] | Source). Reserve inline tags for prose claims only; reconcile counts (every TITLE number tracked, every INFERRED sentence carries confidence + basis).
- **F2 (TL;DR + Sec 4.2; refs V7:15-22,185-199).** Move defense BEFORE capability in skim order: TL;DR sentence 1 carries scope+defense ("benchmark-sandbox only; defense = strip control tokens, Sec 8"); keep the exact token string in ONE fenced block with the Safety header inside the fence, never in prose.
- **F3 (Sec 8a; refs V7:594-599).** Demote 95.130 to "illustrative title-claim (unverified, author-admitted 0.00) — direction only"; promote own 63-row pulls + takamichitoda/aleaiest to primary evidence rows. Example transfer cell: "collapse direction supported by VERBATIM controls (takamichitoda deputy survives; hiranorm title-claim 0.00 illustrative only) [mixed evidence — do not cite 95.130 as measurement]."
- **F4 (TL;DR tail; ref V7:22).** Add 3-bullet Responsible strip under TL;DR: variance (<5 noise), gap (~19pts to 111.690, ceiling not near-miss), stop rule (41 tests, search stopped). Example: "Honesty strip: <5pts is noise; ~19pts to top-50 cutoff; search stopped after 41 no-beat tests."

---
## 2. Skim-path test: can a reviewer grasp the contribution in 5 minutes?

**Drill (must carry the whole argument):** (1) V7 TL;DR (lines 15-22) -> (2) Fig 1 pipeline (line 109) -> (3) Table 7-A (lines 301-313) -> (4) Sec 8 blind spot + 60-s self-test (lines 543-590) -> (5) Fig 11 distribution (V6-C, ~line 4189). **Verdict: PASS with friction — the needles exist, the path is obstacle-strewn. Not 10-second legible (Santa-gallery test fails).**

| Step | Findable? | Time cost | Brutal note + line ref |
|---|---|---|---|
| TL;DR | YES, but heavy | ~90 s (not 30 s) | 6 sentences present (V7:15-22), but sentences 1-2 are 80+ words each with 4 jump-links inline. Hook ("weight ENTIRE field... 92.540... collapses to 0.07") is present yet unreadable — density without terseness. A 10-s pitch ("throughput, not prompts; blind spot; public band X, private 0.07") cannot be quoted verbatim. |
| Criteria box + TOC | YES | ~30 s | Callout (V7:24-25) + 12-section TOC (V7:27) are good. Damage: two MORE TOCs (V7:45,76) + three MORE TL;DRs (V7:35,53,80) compete for the same first screen. Reviewer must learn the version history before the science. |
| Pipeline figure | YES | ~20 s | Fig 1 at V7:109 with caption + interpretation: PASS (LEAP/Santa notebook-first spirit ok). Damage: Figs 3/4/5/6 + 6 more embeds follow — budget discipline is claimed (V7-E:4438 "no new figures... deferred by design") but 11 embeds remain grandfathered. |
| Hero Table 7-A | YES, late | ~120 s to reach | Jump link works ([jump](#table-7a) x3: V7:17,32,4437), but LINEAR readers hit W-E1 era table (V7:274) + climb Table 3 (V7:290) first — 3 tables in 40 lines, two with overlapping levers and contradictory +1.16 handling (V7:297 vs 310). The hero does not feel like THE table. |
| Self-test | JUMP-only | ~60 s via jump, ~10 min linearly | Fence (V7:566-585) + Expected + falsification rule (V7:589-590) are excellent (fastest falsification loop of any competing note). But the fence lives at line ~566 after ~400 lines of Sec 4-7; three pointer duplicates (V7:21,255-256) are needed because the body is too long to scroll. Notebook-first ordering (Santa A#25) is claimed, prose-first is delivered. |
| Fig 11 + matrix | YES, deep | exhaust-only | V6-C/V6-D at ~V7:4189-4212 (4000 lines deep) with source CSV + rebuild script: PASS as exhaust. FAIL as skim: step 5 of a "5-minute" drill cannot be at line 4189 of 4439. The 30-min exhaust (V6-A 74 chunked + V6-B 630 banded + V6-N reconciliation) is real but requires trusting 26x25-row bands. |
| Integrity / labels | PARTIAL | ~60 s | Integrity box front-loaded at Sec 1 (V7:88-98, P0-3: PASS) + label legend (V7:98). Damage: 706 INFERRED tags = wallpaper; per-number CLAIM reconciliation leaves 17/43 untracked (V7:4405-4406). |
| Failures + credit | YES | ~60 s | Failure tables W-E2/Table 6/6b/7 (V7:447-511) with deltas + keep/never-retry (V7:608) + miss-credit V15/JED/takamichitoda (V7:604-608): PASS (MCTS/APTOS/MDC pattern satisfied). |

**Bottom line:** a determined reviewer WITH the jump-links grasps the contribution in ~6-7 min; a linear reviewer bounces at the stacked intros (~line 58, third TL;DR) or the third pre-hero table. Winners (LMSYS 700 words/0 figs; Optiver 1200 words/1 table) are quotable in 10 s. V7 is not. V8 fix: stratified layers (Sec 3 below) + hero-first ordering + single-intro deletion.

## 3. Length test: 3644 lines vs the 1800-2500-word winners band

**Measured (2026-09-06):** 3644 nonblank lines (`Get-Content ... | Measure-Object`: Lines 3644 / Words 63712 / Chars 441917) / 4439 physical lines / ~63.7k words / 450,795 bytes on disk. Winners center 1800-2500 words (Set-A cross-cutting #6, Set-B #6); award window 2500-5500 words (`writeup_style_guide.md:38`); terse winners 700-1200 words (LMSYS A#14, Optiver A#6, Cassava B#13); comprehensive winners 2500-6500 (Quora B#18, ARC paper 6000). **V7 is ~28x the winners center, ~11.6x the award cap, ~10x the longest legitimate comprehensive note.** The V7-D gate "3600-4200 lines: PASS" (V7:4425) measures the wrong unit and legalizes the violation.

**Why length kills even correct science (gate logic, not taste):** C1 is a hard gate (unreadable = unscored); every 10k words over cap costs more than any single lever adds (rubric deep-dive Sec 2.2). V6 already proved this (60333 words, reviewer never reaches Sec 8); V7 kept every word ("byte-identical", V7:31,54,4365) and added Sec 25. Full-field evidence (D1: 810 weighting) is a genuine WIN-differentiator, but inline-printing 705 notebooks (Sec 24 V6-A/B) inside the AWARD artifact confuses the submission with the archive.

**V8 prescription — stratified layers + progressive disclosure (keep full-field evidence, rescue skim):**
- **Layer 1 — Award core (2500-3500 WORDS, the only thing judges score):** single TL;DR + Fig 1 + Table 7-A (<=6 rows) + seed-band + ship/stop strip + Sec 8 blind-spot + self-test + Table 8 checklist (<=8 rows) + bash 1-6 + Sec 10 limits + honesty strip. No era tables, no crater ledgers, no field bands. Every table <=8 rows, every figure counted (cap 5: Figs 1/3/4/6/11).
- **Layer 2 — Methods supplement (auditor, 30-min):** era aggregates, climb, crater deep-dives, per-stage gates, wall-clock ledger, structure-x-model matrix, override log — narrative tables <=8 rows each, linked from Layer 1 via jumps (no duplication).
- **Layer 3 — Exhaust archive (not judged, must reconcile):** 74 code-read chunked <=12 rows + 630 tail as CSV pointer + 3-row samples per 100-rank block (replaces 26x25 inline bands) + verification table (74+1+630=705; 705+105=810; 49/38/722/1; 0 dropped vs `kernels_ALL_REFS.csv`; vote sums). Progressive disclosure: `<details>`/jump per band, never 1867 consecutive pipe-rows.
- **Doctrine change (non-negotiable):** retire "byte-identical preservation." V8 base is a REWRITE of Layers 1-2; V7 survives as `docs/WORKING_NOTE_V7.md` (frozen archive), not as inline prefix. Deleting stacked TL;DRs/TOCs/scopes is P0-1, not optional polish.

---
## 4. P0 / P1 / P2 fix list for V8 (at least 5 P0 must-fix)

### P0 — Must-fix (do all; otherwise do not submit; each blocks 9.5)

- **P0-1 Single intro, hero-first (C1 gate).** Delete stacked TL;DRs/TOCs/scopes (V7:15,35,53,80 / V7:27,45,76 / V7:7-11); one TL;DR (5x<=30-word sentences) + one TOC + 80-word scope; Table 7-A (<=6 lever rows) FIRST in Sec 6; demote W-E1/Table 3 to supplement; fix +1.16 double-handling (ceiling footnote only). *Accept: core 2500-3500 WORDS; no narrative table >8 rows; 10-s pitch quotable.*
- **P0-2 Real seed-bands, no point-headlines (C2+C5).** Every headline ships as band (3 seeded runs + mean+-std + ensemble col) or is downgraded to band language ("ceiling ~91-92.5"); retire bare "92.540" titles. *Accept: zero single-seed headlines; Lonnie small-n risk addressed with selection-bias note.*
- **P0-3 Measured wall-clock ledger (C3+C4, D4 differentiator).** Per-family wall-clock from gateway timestamps + REAL_REPLAY_CEILING=150 truncation curve + N=4/5/6 cost bars; replace INFERRED cost cells with measured or mark provisional. *Accept: cost axis next to score axis with numbers, not "~13 h [INFERRED]".*
- **P0-4 Runnable factory files (C4).** Ship `experiments.json` + `notebooks/01-05` (BASE_PATH + artifact URLs + OOM note) + dumped SETTINGS/requirements; fresh-clone bash 1-6 -> 5/5 PASS. *Accept: reviewer runs without asking the author (CommonLit/TalkingData test).*
- **P0-5 Evidence-hierarchy repair (C3+C5 veto).** Demote 95.130 double-CLAIM to illustrative-only; promote own 63-row pulls + takamichitoda/aleaiest VERBATIM to primary private evidence; add 4-row artifact-control TABLE with paired numbers; per-table Label columns replacing tag wallpaper. *Accept: no mechanism conclusion rests on a title-claim; every INFERRED carries basis+confidence.*
- **P0-6 Appendix budget + doctrine change (C1 gate).** Re-chunk V6-B 25-bands to <=12 rows (or CSV-pointer + samples); figures 11->5 in core; freeze V7 as archive and REWRITE core (retire byte-identical). *Accept: `guide` 10-point checklist 10/10 on the core.*

### P1 — Competitive edge (do next; each maps to a cited 1st-place technique)

- **P1-1 Split ship rule (ISIC A#10 done right).** Public-ship (>5 at CALIB_HOPS=8) vs private-hedge (survivability-first, deputy >=70%/pure entry) objectives; re-log overrides #1/#2 against correct objective (V7:4399-4400).
- **P1-2 Structure-x-model assignment matrix (MDC B#25).** 9 structures x (gpt-oss eff/fire, gemma eff/fire, verdict) replacing prose line V7:217.
- **P1-3 Per-stage gate numbers (RSNA B#2).** Stage-1 recall gate -> stage-2 fill yield -> stage-3 replay survival (top-150) for gated vs keep-all; the gate-ablation V7:256 claims, tabulated.
- **P1-4 Gallery/thumbnail (Santa A#25).** All-traces-at-a-glance figure (score-progression + family strip) legible in 10 s; deferred figures explicitly listed (budget discipline).
- **P1-5 Same-protocol field comparison.** V15/JED-v25 vs v64 under REAL_REPLAY_CEILING=150 + date segment, or explicitly incomparable (V7:604-608 fix).
- **P1-6 Appreciation + upstream diff (Konwinski A#22 / Santa-2024 B#4).** Named-credit section + what-upstream-did/what-changed/validity table for adopted tricks.

### P2 — Polish (after P0+P1 gates pass; from rubric deep-dive Sec P2)

- **P2-1 Hook sharpening (C1).** One-sentence reframe opener (IEEE A#1 style) + luck/confession line (Optiver/ISIC style) in TL;DR 1-2; density pass toward 1800-2500 band.
- **P2-2 Reviewer dry-run (gate).** 5-min skim drill recorded + verification table reconciled (74+1+630=705; 705+105=810; 49/38/722/1; votes 5580) in-note (P2-4 pattern, V7:4437 + V6-N).
- **P2-3 Safety-spirit pass (C5 veto insurance).** Defense-before-capability skim order; exact token string in exactly one fenced block with in-fence Safety header; TL;DR capability claims paired with defense pointer.
- **P2-4 Small-model config (Hydrogen B#8).** Efficiency yaml equivalent (cheap-arm config + inference recipe) so GPU-poor teams can copy the Pareto-small pick, not just admire v64.

## Appendix — Measurements + source map (so V8 edits are traceable)

- Sizes: `Get-Content docs/WORKING_NOTE_V7.md | Measure-Object`: Lines 3644 / Words 63712 / Chars 441917; Python splitlines 4439 physical; bytes 450795 (~451 KB). Words/center-band ratio ~28x; words/cap ratio ~11.6x.
- Counts (Python): pipe-table lines 1867; `Figure` hits 61 lines / 11 embeds (per V7-D V7:4430); fences 92 ticks (~46 blocks); TITLE-CLAIMED 43 / INFERRED 706 / VERBATIM 81 (V7-C V7:4405 claims same).
- Key line refs: title/scope V7:1-12; TL;DRs V7:15,35,53,80; TOCs V7:27,45,76; integrity V7:88-98; Fig1 V7:109; safety V7:185-186; forge fence V7:192-199; Sec5 gates V7:241-261; Sec6 hero V7:265-433 (7-A:301-313, triplets:315-316, ship-log:318-330); Sec7 failures/Pareto V7:440-539; Sec8/8a/8b V7:541-608 (self-test fence 566-585, Expected 589-590); Sec10 V7:630-645; Sec13 repro ~V7:849+; Sec22/23/24 headers V7:1704,2609,3224 (V6-A:3228, V6-B:3355, V6-C:4189, V6-D:4197, V6-N:4335, V6-O:4350); Sec25 V7:4363-4439.
- Rubric: `research/SCORING_RUBRIC_DEEPDIVE.md` (weights Sec 2.1 lines 77-87; PASS-vs-WIN Sec 2.2 lines 89-97; P0 Sec P0 lines 135-144; P1 lines 145-151; P2 lines 153-159). Patterns: `research/WINNING_NOTES_A_25.md` (cross-cutting lines 12-24; Optiver #6, ISIC #10, LEAP #13, MAP #16, Jigsaw #12, MCTS #23) + `research/WINNING_NOTES_B_25.md` (Top-5 lines 630-642; CommonLit #20, TalkingData #14, Hydrogen #8, MDC #25, ASHRAE #16, LANL #19).

*End — research/V7_GAP_AUDIT.md. If any section above lacks a line ref, treat the claim as unverified and re-check before V8 build.*

