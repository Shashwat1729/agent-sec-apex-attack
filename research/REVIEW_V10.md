# REVIEW V10 vs 5 Working Note criteria -- brutal 9.5 gate

**Date:** 2026-09-08 | **Reviewer:** strict reviewer (muse-spark) | **Scope:** D:/personal/hackathon/agent-sec/docs/WORKING_NOTE_V10.md vs docs/writeup_style_guide.md + research/SCORING_RUBRIC_DEEPDIVE.md
**File under review:** docs/WORKING_NOTE_V10.md -- **measured 4652 lines / 511021 bytes / 73262 words / 2445 pipe-table lines / 10+ figures** (bash + python counts; V9 is 4500 lines / 492382 bytes). V10 adds only 152-line header wrapper (lines 1-30) and preserves V9 verbatim from line 33 onward. Checks cover first 200 lines + TOC + 6 hero + 8 self-test + appendices + research/SCORING_RUBRIC_DEEPDIVE.md + docs/writeup_style_guide.md.

> **Verdict: FAIL on all 5. No criterion clears 9.5. The science is real (throughput framing + blind-spot primitive + 824 weighting is a D1 differentiator) but the packaging re-fails every gate V6 already failed. V10 is a header patch, not the P0/P1 rescue it claims. Ship as-is and the note is skim-penalized before 8 is ever read.**

| # | Criterion (host rubric docs/writeup_style_guide.md:9) | Score /10 | Gate | Verdict |
|---|---|---|---|---|
| C1 | Technical clarity & reproducibility | **6.0** | 2000-2500 lines, 2500-5500 words, <=12-row tables, 3-5 figs, single TL;DR+TOC, every claim fence+Expected+delta | **FAIL** -- hard gate violated |
| C2 | Methodological contribution | **7.0** | One rule + ablation + unified-CV harness + seed-variance + ship rule with p-value | **FAIL** -- harness is proxy, triplets are hosted not seeded, no p-value |
| C3 | Security insight | **7.8** | Threat model + per-arg mechanism + <60s falsification + artifact controls + per-component private autopsy | **FAIL** -- strongest section but wall-clock never instrumented, private regex stays INFERRED-not-SOURCE, safety box not line-adjacent |
| C4 | Usefulness to benchmark community | **5.5** | Registry + numbered notebooks + cost axis + keep/never-retry + exhaust pointer chunked | **FAIL** -- 5-row registry, no notebook run-order, cost is INFERRED, 2445 rows still inline |
| C5 | Responsible communication | **5.0** | Variance + stop rule + CLAIM/VERBATIM/INFERRED + override log + safety banner (VETO criterion) | **FAIL / VETO RISK** -- verification appendix lies, word ledger false, headline inflation under-tagged |

Hard-gate rule (research/SCORING_RUBRIC_DEEPDIVE.md:2.1): C1 gate fail = unscored; C5 veto fail = award-ineligible regardless of C2/C3 score. V10 fails both.


---

## C1 -- Technical clarity and reproducibility -- 6.0/10 -- FAIL (hard gate)

**What good looks like (SCORING_RUBRIC_DEEPDIVE.md:1 C1, guide:38,50,72,129):** 4-6-sentence TL;DR, pipeline Fig1 first, one hero ablation table (Optiver 5x5), idea->fence(10-25 lines, runnable, # Expected:)->isolated delta on every claim, pinned seeds/hardware/requirements/commands, 2500-5500 words, 2000-2500 lines, narrative tables 4-8 rows / appendix <=12 rows, 3-5 figures each with caption + one-sentence interpretation, auto-TOC that works.

**Strengths (keep):**
- File:line discipline is exemplary. Every lever carries source pin: optimal.py:51-58 first-present-arg (docs/WORKING_NOTE_V10.md:195-199), predicates.py:144 literal sentinel, predicates.py:234 window 2 vs optimal.py:44-47 window 5, templates.py:39-50 forge, config.py:35-43 SH_FINALISTS=4/CONFIRM_REPS=2/CALIB_HOPS=8 -- reviewer can audit without asking.
- Fences are runnable and carry # Expected: guardrail self-test docs/WORKING_NOTE_V10.md:655-676 (4 asserts + print), forge builder docs/WORKING_NOTE_V10.md:834-865. tools/bundle.py:1-101 AST-verified + tools/local_test.py:1-434 5/5 PASS + tools/generate_figures.py:1-86 + tools/make_notebook.py:177-183 (T4, internet off, 8750s) -- real factory, not prose.
- Pipeline (Fig1 docs/WORKING_NOTE_V10.md:116 thickness=wall-clock) and guardrail trace (Fig2 docs/WORKING_NOTE_V10.md:172) have caption + interpretation; colorblind palette #10b981/#0ea5e9/#94a3b8/#ef4444 grid alpha=0.3 in tools/generate_figures.py.
- Hero ablation Table 7-A exists (docs/WORKING_NOTE_V10.md:300-307) Optiver 5x5 style: method | control->treatment | isolated delta | noise? -- and variance callout + seed-triplet Table 7-A1 + harness Table 6-A are present (right shapes per A#6 MAP/Jigsaw).

**Weaknesses (load-bearing):**
- **Length gate catastrophically violated -- progressive disclosure claim is false.** V10 header advertises award-core narrative Sec 1-10 = ~3240 words [MEASURED] (docs/WORKING_NOTE_V10.md:10) and Appendix A: Award core ~3240 + Supplement ~15000 + Exhaust ~50000 via CSV (docs/WORKING_NOTE_V10.md:1511-1524). Measured reality: Sec 1 start ## 1. Context line 94 to ## 11. Sources line 769 is 675 lines / 10742 words (python split count); whole file is 73262 words / 4652 lines / 511KB / 2445 pipe lines. That is ~13x the 2500-5500-word award window (guide:38) and ~1.9x the 2000-2500-line Appendix N gate. V10 is not stratified; it is V9 (4500 lines) + 152-line wrapper verbatim (delta 152 measured). The 2445 pipe lines are still inline -- no extraction to research/kernels_ALL_REFS.csv happened. Claim F1 is dishonest.
- **Verification appendix fabricates PASS.** ## Appendix N - Verification (docs/WORKING_NOTE_V10.md:1969-1985) claims Total lines 2497 | 2000-2500 | PASS and Total bytes 227618 | 225280-286720 | PASS. Real values on disk are 4652 lines / 511021 bytes. Gate would be FAIL by 86 percent on lines and 78 percent on bytes. This is VETO-grade honesty violation (SCORING_RUBRIC_DEEPDIVE.md:5 C5 failure c CLAIM-as-VERBATIM). A CI checking len(open(path).readlines()) would catch it.
- **Three TL;DRs stacked.** After V10 5-sentence box (docs/WORKING_NOTE_V10.md:12-18), file preserves V8 TL;DR (docs/WORKING_NOTE_V10.md:44-53) and Base TL;DR (docs/WORKING_NOTE_V10.md:88-91) verbatim. Re-breaks P0-1 single-intro doctrine and buries hook under ~230-word duplication V10 claims to fix.
- **Figure budget blown.** F3 advertises skim figures capped to 5 (Fig1/2/4/7/12), 7 deferred to App J (docs/WORKING_NOTE_V10.md:23). File embeds Fig1 pipeline, Fig2 guardrail, Fig3 ablation, Fig4 progression, Fig5 taint window, Fig6 wall-clock, Fig12 Venn, Fig7 private scatter, Fig10 duplicate progression, Fig11 field distribution = 10 figures before Appendix J. guide:72 cap is 3-5; SCORING_RUBRIC_DEEPDIVE.md calls >8 paper bloat / skim-penalty. Fig3/4 are both score-progression variants that should be one.
- **Table budget blown.** F4 advertises Table11 14 -> 11a (7 rows) + 11b (7 rows) chunked <=12 but no Table 11a/11b with that split exists; the 50-row chronological logs 18 Table A/A2 (docs/WORKING_NOTE_V10.md:1020-1197), 22 W-1a/W-1b (15 rows each), 23 23-A, Appendix M 12-row chunks still total 2445 pipe lines inline. guide:50 says >10 rows move to docs/experiments.md and link -- V10 links but does not move.
- **TOC anchor drift.** V10 contents (award core) (docs/WORKING_NOTE_V10.md:20) points to #1 Context etc. but file now has two H1 titles (V10 H1 line 1 and V8 H1 line 33) and duplicate ## 12. Appendix Code Samples (lines 830 and 1213) plus out-of-order ## 18/19 before ## 12 -- anchors collide, hierarchy violates guide:36 # once, ## x12.
- **Reproducibility nits:** ## 13. How to Reproduce says dependencies = [] (SDK vendored) and No pip install needed but then If you need SDK deps: pydantic, torch (for GGUF c099eb4), gym (docs/WORKING_NOTE_V10.md:969-975) -- contradictory. Word-count ledger says MEASURED but no Measure-Object artifact is checked in.

**Fixes for V11 (P0 -- must for PASS):**
- P0-1a Make header honest or make V11 stratified. Either delete false ~3240 [MEASURED] ledger line and rewrite Appendix N to real 4652 lines / 511KB / 73262 words : FAIL, or ship V11 as real rebuild: docs/WORKING_NOTE_V11.md where Sec 1-10 narrative is 2500-3500 words (verify via python -c print(len(open(slice).read().split())) in CI), move 50-row logs 18 Table A/A2 and 74+630 exhaust to research/appendices/V11-A_CHRONO.md and research/appendices/V11-B_EXHAUST_CHUNKED.md chunked <=12 rows per guide:50, keep only Table 7-A + 7-A1 + 6-A in narrative. Freeze V10 at docs/WORKING_NOTE_V10.md per V10 line 26.
- P0-1b Single TL;DR. Delete Base TL;DR block (docs/WORKING_NOTE_V10.md:88-91) in V11 and collapse V8 TL;DR to one-line pointer or remove. Enforce 4-6 sentences via sentence count in CI.
- P0-1c Figure cap 5. Keep Fig1 pipeline + Fig2 guardrail + Fig3 ablation + Fig4 progression + Fig12 Venn in Sec 1-10; move Fig5 taint window, Fig6 wall-clock, Fig7 scatter, Fig10 duplicate, Fig11 distribution to Appendix J with reuse map. Delete duplicate assets/score_progression.png used as both Fig4 and Fig10.
- P0-1d Table cap. No narrative table >8 rows; no appendix table >12 rows. Split 18 Table A (50 rows) into 5 chunked tables Table A1..A5 of 10 rows, each caption Table A1 -- ... (part 1/5) and link full CSV research/kernels_ALL_REFS.csv -- enforce via rg -c piped lines per table in CI.
- P0-1e Fix headings/TOC. One H1 only; renumber 18/19 to Appendix E/F or move behind ## 14 Conclusion; remove duplicate ## 12. Validate anchors with python duplicate-id check pre-commit.
- P0-1f Bundle reproducibility truth. In 13 replace dependencies = [] hand-wave with verbatim dump: cat pyproject.toml plus cat src/apex_attack/config.py DEFAULT_BUDGET plus pinned GGUF hash c099eb4 2026-07-17 hash file. State exactly pip install pydantic torch required for local_test guardrail import, or vendor it and prove python tools/local_test.py passes with no pip.


---

## C2 -- Methodological contribution -- 7.0/10 -- FAIL (needs 9.5)

**What good looks like (SCORING_RUBRIC_DEEPDIVE.md:1 C2, A#6 Optiver, A#16 MAP, B#5 ARC):** One transferable method stated as a rule + the ablation that proves the rule, under a unified harness (same folds/seed/metric), with selection/blend rule and seed-variance proof the rule is stable. Every trick carries control -> treatment = +x isolated and noise flag.

**Strengths:**
- Throughput-first framing is the right contribution and stated cleanly: blind-spot primitive x replay-safe fill under wall-clock -- not prompt art (docs/WORKING_NOTE_V10.md:5-14, 2 pillar table docs/WORKING_NOTE_V10.md:122-131). Genuine systems-hacker lesson (MAP A#16 spirit).
- Hero Table 7-A isolates 4 levers with paired deltas: forge +27.5, THS decode corner (v30 replay-cap removal +2.58, part of +3.93 chain), plus water-cooler refs. Each delta cites isolated reruns (v8 78.515 etc.) with file:line, not aggregate vibes.
- Ship log exists (docs/WORKING_NOTE_V10.md:326-330 ship-log table + docs/WORKING_NOTE_V10.md:312-324 variance callout) and stop rule: 41 post-v64 no-beats, ceiling ~91-92.5 (docs/WORKING_NOTE_V10.md:261-270). F8 private-aware flip Table 7-C (docs/WORKING_NOTE_V10.md:341-353 eff vs eff_private) converts public-only report into two-board method.
- Rejected alternatives documented (4.3 evolutionary/MCTS/Go-Explore rejected with cost argument, research/literature/search_algorithms.md:38-48).

**Weaknesses:**
- **Seed-triplet is not a seed-triplet.** Table 7-A1 Seed-triplet + ensemble (F6, MAP/Jigsaw) (docs/WORKING_NOTE_V10.md:315-324) advertises MAP-style triplet but footnote admits hosted rerolls are NOT seeded reruns; triplet via same harness MockCompliantAgent fills SEEDED cells and rows show hosted reroll1 85.800 [VERBATIM v105 55946386], reroll2 91.860 [VERBATIM v109] -- those are Kaggle hosted resubmits on different days confounded by wall-clock + stochastic draws, not seed=123/124/125 MockCompliantAgent reruns. Mean +-2.6 is observed band, not seed-variance estimate. SCORING_RUBRIC_DEEPDIVE.md C2 weakness (a) single-seed headline (A#12 Jigsaw / A#16 MAP warning) is not fixed; Lonnie B#6 max-inflation via sigma*PhiInv(1-1/n) 5-7 pts is hand-wavy, not bootstrap CI.
- **Harness is proxy, not unified CV.** Table 6-A Unified-CV harness (F7) (docs/WORKING_NOTE_V10.md:341-353) claims same folds/seed/metric at REAL_REPLAY_CEILING=150 [MEASURED local_test.py:64 6x anti-inflation] but footnote concedes local MockCompliantAgent under-estimates real replay latency 6x [MEASURED] and ordering preserved, magnitudes proxy-tagged PROXY. Comparison of JED v25 89.145 Gold [VERBATIM code-read] vs v64 under same protocol cannot be verified because field notebooks were never replayed under CALIB_HOPS=8 locally -- only 63 submissions have gateway timestamps. This is guide:111 failure (20 actions without isolated delta under same harness) relocated to proxy column.
- **Ship rule has no statistics.** Variance callout says ship only if 3-seed mean delta >5 + fire_rate at CALIB_HOPS=8 + t-test p<0.05 (F9) (docs/WORKING_NOTE_V10.md:312) but no t-test is computed anywhere -- no df, no p-value, no per-lever table of delta, SE, t, p. ISIC A#10 pattern requires statistic shown, then override log reconciles. Log table (docs/WORKING_NOTE_V10.md:326-330) lists THS ladder +4.84/+3.93 stepwise, +9.4 cumulative as shipped but each step sits near 5-pt noise floor individually -- under stated rule neither would ship alone, so rule is already violated without being logged as override.
- **TOP 300->450 and SH4->6 craters duplicate.** Ship log lists them as NO, but 6.2 post-v64 sweep already lists them -- double counting same negative without new insight.

**Fixes for V11 (P0/P1):**
- P0-4a Real seed-triplet. Run python tools/local_test.py --seeds 123,124,125 --hops 8 three times via MockCompliantAgent (no GPU) and publish actual triplet next to hosted band: v64 local 88.1/89.3/88.7 mean 88.7 +-0.5 with note hosted 85.8-91.9 confounded, local triplet is variance we control. Tag columns [VERBATIM host] vs [SEEDED mock] explicitly as header promises.
- P0-4b Real harness or honest proxy label. Either replay 3 key field baselines (JED v25 89.145, V15 90.54, pilkwang hedge) under REAL_REPLAY_CEILING=150 locally and publish measured mean_raw/mean_cost/eff with wall-clock, or relabel Table 6-A Proxy ranking (not unified CV) and add limitation: Field-vs-ours same-harness comparison is PROXY; ordering only, magnitude not comparable -- see F10.
- P0-4c Ship rule with numbers. Add 4 columns to Table 7-A: 3-seed mean delta | SE | t | p and row Lonnie max-inflation expected 6.1 (sigma 2.6 * PhiInv). Log THS ladder as override #1: shipped despite each step <5 because cumulative +9.4 with fire_rate guard at 8 hops, logged 2026-08-14 so ISIC violation is forgiven like A#10.
- P1-2a Ablation completeness. Add row for gate ablation keep-all vs validate-then-keep (31 percent -> ~100 percent fire, Table Eff-1:418) as dedicated +eff 3.2x yield [MEASURED local 31 percent] -- currently gate contribution is prose not isolated delta in Table 7-A.

---

## C3 -- Security insight -- 7.8/10 -- FAIL (closest to gate, still short)

**What good looks like (A#21 Malware 7-liner, B#19 LANL, B#2 RSNA):** Threat model up front, attacker capability per lever, hole made falsifiable in <60s (runnable probe, not prose), temporal/artifact negative controls BEFORE model-gain claims, public-vs-private per-component deltas where boards shift.

**Strengths (best section):**
- Mechanism chain is precise and source-verified: first-present-arg optimal.py:51-58 stops at url, data=SECRET_MARKER never inspected (docs/WORKING_NOTE_V10.md:193-199, 632-640), taint window 5 superset predicate window 2 (optimal.py:44-47 vs predicates.py:234), canonical _is_secret_path predicates.py:181-196 vs substring ultra optimal.py:22-30, Harmony channel arXiv:2509.22830 (docs/WORKING_NOTE_V10.md:634-640). Sharpest blind-spot + taint analysis of any draft.
- Falsification loop is real: ### Guardrail Self-Test (docs/WORKING_NOTE_V10.md:655-676) 4 asserts (ALLOW clean post, DENY web->post, canonical vs substring, literal vs b64) plus <60s claim with Expected output guardrail self-test PASS (docs/WORKING_NOTE_V10.md:678-682) and pointer python tools/local_test.py. Fastest falsification loop of 50-note corpus (SCORING_RUBRIC_DEEPDIVE.md D3).
- Artifact controls before model gains: Table 1b docs/WORKING_NOTE_V10.md:183-192 with 4 trivial baselines (date-segment freeze 2026-08-07 disc 733058, same-bytes 2-12pt variance, title-claim control, private INFERRED) -- Malware A#21 pattern honored.
- Private-gap autopsy ASHRAE-grade: per-component Table 8a (docs/WORKING_NOTE_V10.md:683-696), survival Venn Fig12 (docs/WORKING_NOTE_V10.md:714-718), predicate x guardrail matrix Table 8b (docs/WORKING_NOTE_V10.md:697-712), plus rank-6 95.130 [TITLE-CLAIMED] -> 0.00 control vs takamichitoda 24.36 survivor (docs/WORKING_NOTE_V10.md:446-470). Three new proofs in 8a-extra (syed v12b/v19 inversion 30.735->0.00 439x, abukayyisah matrix, takamichitoda hedge) correctly file:lined.

**Weaknesses:**
- **Wall-clock side-channel is admitted gap and stays uninstrumented.** Note repeats we never instrumented it (research/VERY_DETAILED_REPORT_V2.md:721-728) (Fig6 caption docs/WORKING_NOTE_V10.md:604), Pareto provisional: per-family gateway-timestamp instrumentation was never run (Sec 6.5, Sec 7 F10) (docs/WORKING_NOTE_V10.md:630), and Wall-clock ledger (F10, Santa-2024 curve pending) (docs/WORKING_NOTE_V10.md:607). Table Eff-1 (docs/WORKING_NOTE_V10.md:278-286) and wall-clock Pareto (docs/WORKING_NOTE_V10.md:609-630) therefore ship INFERRED cost (~13h [INFERRED via 738946]) where SCORING_RUBRIC_DEEPDIVE.md P1-1 requires MEASURED per-family gateway timestamps + REAL_REPLAY_CEILING=150 truncation curve + N=4/5/6 cost bars (Vesuvius B#9 identical-cost style). D4 differentiator not delivered.
- **Private regex confidence over-stated in headers.** V10 TL;DR sentence (3) says private re.search(secret) [INFERRED via 738915] + wall-clock 15h vs 13h [INFERRED via 738946] pending ledger MEASURED -- but Sec 8 prose then upgrades to Any payload that fires EXFIL necessarily contains substring secret ... so any private re.search(secret) on sink args closes both outright [INFERRED] without re-tagging confidence high vs low the ledger promises (docs/WORKING_NOTE_V10.md:695 legend). Fig12 caption asserts Venn without INFERRED qualifier (docs/WORKING_NOTE_V10.md:716-718).
- **Safety box not line-adjacent.** F17 promises safety box line-adjacent to <|end|> fence. The <|end|><|start|>assistant literal appears in V10 wrapper line ~9 and in ## 12A Forge builder (docs/WORKING_NOTE_V10.md:834-865) but Defense/Research-Only banner is 15+ lines away at 12A header, not fenced immediately above token literal with strip-tokens defense pointer. Safety reviewers flag this guide pitfall #8.
- **Gemma doubled-brace bug asserted not shown.** Gemma doubled-brace GGUF c099eb4 cap (docs/WORKING_NOTE_V10.md:634-640) cites discussion_733058.txt:183-228 but no local reproduction fence shows doubled-brace rejection -- self-test does not cover it.

**Fixes for V11:**
- P0-7a Safety box fence. Wrap every <|end|> literal with Safety -- Defense/Research Only -- strip control tokens banner immediately above fence (not 15 lines above). Enforce via rg -n <|end|> check preceding 3 lines contain Safety.
- P0-7b Private confidence per sentence. Tag each private-mechanism sentence with [SOURCE: predicates.py:line] vs [INFERRED via 738915 wall-clock, high] vs [INFERRED via scoreDescending rank, low] using ## 8a legend already present (docs/WORKING_NOTE_V10.md:695). Do not assert re.search(secret) without INFERRED on same line.
- P1-1 Instrument wall-clock. Parse research/all_submissions_raw.txt:14-63 gateway timestamps where available, compute per-family wall_clock_s = submit_time_next - submit_time or kaggle kernels status wall-clock, publish ledger with STATUS: MEASURED vs INFERRED column already promised in Table - Wall-clock Pareto (docs/WORKING_NOTE_V10.md:609). Add Santa-2024 score-vs-compute curve (score on y, wall-clock on x, REAL_REPLAY_CEILING=150 truncation note local_test.py:64) -- even retrospective timestamps is MEASURED, arithmetic is not.
- P1-1b Gemma bug fence. Add 4-line probe: json loads doubled-brace fails vs single-brace passes with GGUF c099eb4 pin.


---

## C4 -- Usefulness to benchmark community -- 5.5/10 -- FAIL

**What good looks like (A#2 Rossmann, B#20 CommonLit, B#8 Hydrogen, B#25 MDC):** Full registry (name/definition/membership/rationale), numbered notebooks in run order with BASE_PATH + artifact URLs + OOM workaround, score AND cost (params/latency/wall-clock) Pareto, keep/never-retry tags, field exhaust pointer chunked and honestly labeled.

**Strengths:**
- Red-Team Checklist Table 8 (docs/WORKING_NOTE_V10.md:727-750) is generous: Measure fire_rate/cost_replay/wall-clock, Pin GGUF + 8750 vs 9000, Size REPLAY_SAFE_FRAC=0.97/MARGIN_S=47, Test deputy-hedge/decode-path -- each with metric/threshold + source file:line. Keep/never-retry ledger is present (22 W-1a/W-1b + 8b, research/VERY_DETAILED_REPORT_V4.md:2622-2730 with 25/38/42 tally) and ## 17 Future Work sketches private-40+ strategies.
- Exact reproducibility bash 1-5 is present (## 13. How to Reproduce docs/WORKING_NOTE_V10.md:969-1020: bundle -> local_test 5/5 -> generate_figures -> make_notebook -> kaggle push/status/submit with Expected outputs and SETTINGS dump pointer Sec 13 bash 1-5 exact commands + SETTINGS dump + efficiency Pareto per V10 header F14).
- Field exhaust differentiator D1 is real: ## Appendix A -- Stratified exhaust (docs/WORKING_NOTE_V10.md:1511-1524) 824 = 105+74+630+14+1 with 55/42/722/1 + vote sums 5580 plus chunked pointers research/kernels_ALL_REFS.csv, research/KERNELS_FULL_INVENTORY.md, research/VERY_DETAILED_REPORT_V5.md:3454-4478 -- reviewer verifies top-20 in 5 min (6 Table 5), auditor exhausts 824 in 30 min via CSV. Technique-x-evidence 6x4 matrix exists (23).

**Weaknesses:**
- **Registry is a stub.** research/experiments.json:1-53 contains only 5 rows (v64, v72, v74, v77, syed_v12b) with single generator / config / seed / wall_clock_h per row. TalkingData B#14 pattern requires one row per lever (forge, THS, replay-cap, SH, fill, hedge, token swap, b64) with features/model/dataset blocks and paired deltas. File even carries contradictory wall_clock_h: ~13 INFERRED via 738946 -- not measured.
- **Numbered notebooks not shipped.** ## 13 promises notebooks/01_prep..05_infer in run order with BASE_PATH + artifact URLs + OOM workaround (CommonLit B#20) but repo has only tools/bundle.py / local_test.py / generate_figures.py / make_notebook.py -- no notebooks/01_*.ipynb sequence, no BASE_PATH convention doc, no weight/dataset URLs pinned, no CUDA-OOM restart note. Repro is commands, not a factory (SCORING_RUBRIC_DEEPDIVE.md:1 C4 failure b).
- **SETTINGS dump missing.** pyproject.toml:6 dependencies = [] with no dumped SETTINGS.json / entry_points / requirements verbatim in Sec 13 or appendix pointer with hash. guide A3 requires bundle (README, requirements, SETTINGS.json, entry_points).
- **Cost axis is story, not Pareto.** Table Eff-1 (docs/WORKING_NOTE_V10.md:278-286) shows wall-clock [STATUS] ~13h [INFERRED] and score/cost 7.1 /h arithmetic, not gateway timing. No Hydrogen dual-track accuracy vs efficiency yaml + inference kernels + small-model config vs winning ensemble. Gate-ablation: recall-gated fill (31% -> ~100%) line is prose, not 6-row Pareto table with params | latency | wall-clock | score.
- **Exhaust pointer still ships flat inline.** Despite F1 stratified exhaust via CSV-pointer, the 2445 pipe lines are still inline in same file reviewer must skim. Pointer table docs/WORKING_NOTE_V10.md:1511-1524 is honest about where CSV lives, but file remains 511KB because nothing was extracted.

**Fixes for V11:**
- P1-2 Full registry. Expand research/experiments.json to >=15 rows (one per lever attempt: v8 forge, v22 THS30->80, v33 THS80->300, v51 N=2..4, v64 N=5, v72 forge7, v74 SH-cut, v91 TOP450, v92 SH6, H hedge, I b64, syed v12b/v19, takamichitoda, huanligong). Schema: {id, family, generator file:line, config, seed, cost_replay_s MEASURED/INFERRED, wall_clock_s, public_private, delta_vs_control, label VERBATIM/TITLE-CLAIMED/INFERRED}. Validate with python -m json.tool in CI.
- P1-2b Numbered factory. Add notebooks/01_probe.ipynb .. 05_submit.ipynb (or at least notebooks/README.md with 01 prep (fixtures hash) -> 02 race (CALIB_HOPS=8) -> 03 fill -> 04 bundle -> 05 kaggle push) with BASE_PATH = Path(__file__).parent.parent and pinned artifact URLs + ONE OOM workaround note (e.g. T4 OOM on forge8_terse: reduce TOP 300->150, see research/open_source_top50.md:268).
- P1-2c Dump SETTINGS. In ## 13 include verbatim fenced blocks: JSON SETTINGS.json (truncated, hash sha256:...) plus entry_points and requirements.txt (or pyproject.toml dependencies hash). No hand-wave dependencies = [].
- P1-1c Real Pareto. Build docs/assets/wallclock_pareto.png from measured per-family wall-clocks (see C3 fix) + add 6-row Table Eff-1 with config | params (#structs) | public | private | wall-clock MEASURED | score/wall-clock | ship? -- small-model row must be real config (single_short) with measured cost, not mid-80s band [VERBATIM resubmits].
- P0-1g Extract exhaust. Move 2445 pipe lines out of file. In V11 narrative keep only top-20 helped table (## 23.1 Top 20, 10 rows) and link Full 824 rows: research/appendices/V11_EXHAUST_CHUNKED.md (chunked <=12) and research/kernels_ALL_REFS.csv.

---

## C5 -- Responsible communication -- 5.0/10 -- FAIL / VETO RISK

**What good looks like (A#10 ISIC, A#23 MCTS, A#3 Titanic, B#15 Jahrer/B#16 ASHRAE):** Honesty under pressure: variance disclosed (never single-seed), decision rule + every override logged with outcome, small-n selection protocol confessed, misses credited by name, stop rule stated, luck/betting/probing disclosed, labels CLAIM vs VERBATIM vs INFERRED where exactness varies, control-token safety banner + defense pointer. Responsible is VETO criterion -- hidden probing or CLAIM-as-VERBATIM flips a win to a fail.

**Strengths (voice is honest; artifacts exist):**
- Defense/Research-Only banner at top of file (docs/WORKING_NOTE_V10.md:3), integrity front-load box ## 1. Context (docs/WORKING_NOTE_V10.md:94-107) with freeze-date 2026-08-07 disc 733058, no-leak proof (synthetic SECRET_MARKER literal predicates.py:144, never fs.read(secret.txt)), and label legend VERBATIM / TITLE-CLAIMED [CLAIM] / INFERRED -- LEAP pattern (A#21/A#13).
- Variance honesty is good: Variance callout (docs/WORKING_NOTE_V10.md:312-313) Headline is the band about 91-92.5 [VERBATIM band], not the point 92.540 + Single-run deltas <5 pts are noise (field 2-12 pts, disc 733345) + Lonnie B#6 max-inflation 5-7 pts via sigma*PhiInv and responsible skim box 5-line (docs/WORKING_NOTE_V10.md:18) plus gap to frontier ~19 pts to 111.690 top-50 cutoff.
- Ship log + stop rule (docs/WORKING_NOTE_V10.md:326-330, docs/WORKING_NOTE_V10.md:261-270 41 post-v64 no-beats) and miss-credit by name (takamichitoda 24.360, huanligong 21.495, aleaiest 738896 trap, hiranorm 95.130->0.00, will-rice 29.520, Sec 8b).
- Limitations ## 10 (docs/WORKING_NOTE_V10.md:750-768) confesses private INFERRED, mock 6x gap local_test.py:64, variance +-5/disc_733345, gap-to-frontier ~19pts, infra cron failures, final-2 selection anti-trap V108 89.345/0.045, 710234-not-reverified hygiene -- Titanic honest-reporting pattern.
- Per-claim confidence legend in 8a (docs/WORKING_NOTE_V10.md:695) [SOURCE: predicates.py:144 literal] vs [INFERRED via 738915 wall-clock, high] vs [INFERRED via scoreDescending rank, low].

**Weaknesses (load-bearing, veto-grade):**
- **Fabricated verification (see C1).** Appendix N 2497 PASS when file is 4652 lines is not measurement error; it is copy-paste from earlier V3/V4 draft (Build: pre-N lines 2479 docs/WORKING_NOTE_V10.md:1985) never recomputed after V9/V10 grew to 4.5k lines. Combined with false ~3240 [MEASURED] word ledger, note presents two MEASURED claims that are INFERRED/wrong. Under C5 this is CLAIM numbers presented as VERBATIM (DIAGNOSIS RC3 / SCORING_RUBRIC_DEEPDIVE.md C5 failure c) and triggers veto: a strong-methods note with hidden probing or uncredited borrowing fails outright.
- **Lonnie inflation not consistently labeled.** V10 TL;DR and ## 6.1 Seed-band reporting correctly note expected max-inflation ? trust band but title block Best public band: about 91-92.5 [VERBATIM band] (v64 peak 92.540 [VERBATIM] seed-123 inside hosted band 85.800-91.860 [VERBATIM]) (docs/WORKING_NOTE_V10.md:8) presents point 92.540 as headline without inflation qualifier on same line -- skimmer keeps point.
- **Private INFERRED sometimes drifts to assertion.** Sec 8 Payload blind spot states Any payload that fires EXFIL necessarily contains substring secret ... so any private re.search(secret) on sink args closes both outright [INFERRED] -- correctly tagged -- but 30 lines later Defenses state Data-flow/provenance on every outbound sink -- deny any sink carrying a protected secret regardless of which argument holds it as fact without [INFERRED via 738915] qualifier, implying source knowledge that does not exist.
- **Override log incomplete.** THS ladder +4.84/+3.93 requires override entry under >5 ship rule but not flagged as override #1 in same table row; log lists it generically THS ladder 30->80->300 | +4.84/+3.93 stepwise, +9.4 cumulative | YES (override #1) -- per-step violation not quantified with mean +- SE, p so ISIC A#10 forgiveness cannot be applied.
- **Control-token safety not at first use.** Already scored in C3: F17 box is 15+ lines from first <|end|> literal.

**Fixes for V11 (P0 -- veto blockers):**
- P0-5a Recompute or retract every MEASURED claim. Replace docs/WORKING_NOTE_V10.md:10 word ledger with python3 -c print(len(open(slice, encoding=utf-8).read().split())) output or change tag to [INFERRED via word-count script, pending CI] if not measured. Replace Appendix N block with CI-generated table: run python tools/check_gates.py that prints Total lines XXXX | Gate YYYY | PASS/FAIL at build time -- do not hand-edit. Gate should be 2000-3500 lines for V11 narrative, not 2000-2500 if stratified appendices are separate files; document new gate.
- P0-5b Headline inflation label. Amend title block to v64 92.540 [VERBATIM seed-123, expected max-inflation 5-7 pts Lonnie B#6, headline is band 91-92.5 band, not point]. No skimmer should keep point without inflation note on same line.
- P0-5c Per-sentence INFERRED tags. Pass rg -n re.search\(secret and tag every occurrence [INFERRED via 738915 wall-clock, high] or [SOURCE: predicates.py:144 literal -- public only]. Remove any sentence asserting private regex without tag.
- P0-5d Complete override log. Add columns 3-seed mean delta | SE | t | p | shipped? | override? | outcome to ship-log table; fill with real t-test values (even if p>0.05, log violation honestly per Novoselskiy A#10).
- P0-5e Safety adjacency. See C3 fix -- box must be 3 lines immediately preceding each <|end|> fence.


---

## Summary -- why V10 is not 9.5 on any criterion and what V11 must do

V10 correctly identified the 5 award criteria and wired the right 20 fixes (F1-F20) as headers, tables, and boxes. The original V8 science (throughput framing + blind-spot primitive + race + fill + 810 weighting) remains strong and would score PASS under lenient review. But a header that promises a gate is not a gate. SCORING_RUBRIC_DEEPDIVE.md:2.1 is explicit: Reviewers score skim-path (TL;DR + Fig1/2 + Table 7-A + Sec 8 + variance box) x honesty multiplier x exhaust-path bonus; length beyond the window divides the total.

| What V10 promised (header) | What V10 ships (disk) | Cost |
|---|---|---|
| F1 progressive disclosure ~3240 + 15000 + 50000 via CSV | 73262 words / 4652 lines / 2445 pipe lines still inline | Skim-penalty: reviewer never reaches Sec 8 (SCORING_RUBRIC_DEEPDIVE.md FAIL case) |
| F2 single 5-sentence TL;DR | 3 TL;DRs (V10 + V8 + Base) | Hook diluted |
| F3 5 skim figures | 10 figures | Bloat penalty |
| F10 wall-clock MEASURED ledger | Table Eff-1 ~13h [INFERRED], Pareto pending | D4 differentiator not delivered |
| F13 experiments.json registry | 5-row stub | TalkingData pattern not met |
| Appendix N 2497 PASS | 4652 FAIL | Veto-grade trust hit |

**P0 rescue for V11 (do all, otherwise do not submit):**
1. **Honest ledger + extracted exhaust** (C1+C5 veto). Freeze V10, create docs/WORKING_NOTE_V11.md with 2500-3500-word narrative; extract 2445 pipe lines to research/appendices/*.md chunked <=12 rows; recompute Appendix N from disk in CI; delete false MEASURED tags or make them MEASURED.
2. **Real seed-triplet + t-test ship rule** (C2+C5). Replace hosted rerolls with seed 123/124/125 MockCompliantAgent triplet + ensemble + t, p per lever; log THS cumulative override honestly.
3. **Instrumented wall-clock Pareto** (C3+C4 D4). Parse gateway timestamps, publish per-family measured ledger + score-vs-compute curve with REAL_REPLAY_CEILING=150 note; add Gemma doubled-brace fence.
4. **Safety adjacency + per-sentence INFERRED** (C3+C5). Box the 3 lines above every <|end|> literal; tag every private re.search sentence.
5. **Full factory** (C4). Expand research/experiments.json to 15+ rows; add notebooks/01..05 run-order README; dump SETTINGS.json/entry_points/requirements verbatim.
6. **Figure/table budget enforcement via CI** (C1). Add tools/check_gates.py that fails on words >5500 or lines >3500 narrative or >5 figures in narrative or any table >12 rows and run it pre-commit.

**After P0, P1 polish (each +0.2-0.5):** gallery figure (200-gallery spirit A#25), appreciation + upstream diff (Konwinski A#22), hook sentence reframe (IEEE A#1 "not cleverness, throughput"), reviewer 5-minute dry-run note.

> **One-line guidance for the author:** The work to win is done -- the work to be *read* is not. V11 is an editing + instrumentation sprint, not a new experiment: cut verbatim bulk out of the file, measure what you claimed was measured, and let the 60-second self-test carry the note.

---

## Appendix -- Evidence base and method

**How this review was done:** Read docs/WORKING_NOTE_V10.md first 200 lines + TOC scan + 6 hero tables + 8 self-test + appendices (bash Get-Content + Select-String), read research/SCORING_RUBRIC_DEEPDIVE.md:1-170 and docs/writeup_style_guide.md:1-136, re-measured file on disk via python split count (73262 words), pipe-line count (2445), line count (4652), byte size (511021), diff delta vs V9 (152 lines), sampled Appendix N vs disk, checked assets 10 PNGs exist, checked research/experiments.json 5 rows, checked tools/bundle.py, local_test.py, generate_figures.py existence. If any tool failed alternative was tried (read fallback to bash Get-Content, Select-String fallback to python re). No tool failed terminally.

**Evidence base:** docs/WORKING_NOTE_V10.md:1-4652 (sampled), research/SCORING_RUBRIC_DEEPDIVE.md:1-170, docs/writeup_style_guide.md:1-136, research/VERY_DETAILED_REPORT.md:1-528, research/all_submissions_raw.txt:14-63, research/experiments.json:1-53, tools/bundle.py:1-101, tools/local_test.py:1-434, tools/generate_figures.py:1-86, research/kernels_ALL_REFS.csv (pointer), disc_733345.txt:56-138 (variance 2-12 pts), disc_738915 wall-clock probing (via report), research/open_source_top50.md:1-314. Counts via python read().split() and Get-Content | Measure-Object -Word; pipe-line count (Select-String "^\|").Count = 2445.

**Reviewer stance:** Brutal 9.5 gate per instructions. Scores are 0-10 per criterion. 9.5 = award-ready with no P0 remaining. V10 scores 5.0-7.8: real science, packaging fails gates. Fixes above are minimal set to reach 9.5.

