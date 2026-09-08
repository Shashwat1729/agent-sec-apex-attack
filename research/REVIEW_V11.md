# REVIEW V11 - Strict 9.5/10 Working Note Audit

**Date:** 2026-09-08 | **Doc:** `docs/WORKING_NOTE_V11.md` | **Auditor:** strict reviewer (brutal 9.5 gate)
**Doc stats (measured via tools/check_gates.py:88-116):** 2968 lines / 323520 bytes / 50604 words total / 4508 slice words / 335 pipe lines / 12 figs (5 narrative) / 23 fences / max rows 12 (narr 8) / 13/13 CI PASS
**Compared claim (header docs/WORKING_NOTE_V11.md:7):** "Sec 1-10 = 3100 words [MEASURED via split]" - **MISMATCH** (see C5)
**Read scope:** first 200 lines + TOC + §6 hero + §8 self-test + appendices A/K/N + filler F1-F30 + research/SCORING_RUBRIC_DEEPDIVE.md + tools/check_gates.py output + tools/local_test.py + research/experiments.json + research/seeded_triplet_measured.json + research/appendices/V11-A_CHRONO.md + research/appendices/V11-B_EXHAUST_CHUNKED.md
**Rubric:** 5 criteria per docs/writeup_style_guide.md:9 and research/SCORING_RUBRIC_DEEPDIVE.md:5 - weights ~ C1 30% gate / C2 25% / C3 20% / C4 15% / C5 10%+VETO. 9.5/10 = "winning threshold, publish without revision."

---

## Verdict - DOES NOT CLEAR 9.5

| Criterion | Score | 9.5 gate | Verdict |
|---|---|---|---|
| C1 Technical clarity & reproducibility | 6.5/10 | FAIL | PASS at gate, FAIL at density/honesty win level |
| C2 Methodological contribution | 8.0/10 | FAIL | Strong levers, weak transfer proof |
| C3 Security insight | 8.5/10 | FAIL | Best section, still INFERRED-dependent |
| C4 Usefulness to community | 7.0/10 | FAIL | Generous factory diluted by padding |
| C5 Responsible communication | 5.5/10 | VETO RISK | Safety exemplary, ledger honesty fails |

**One-line:** V11 mechanically passes all 13 CI gates (tools/check_gates.py:93-105 OVERALL PASS 13/13) but games the gate it claims to honor. The 30 verbatim filler supplements + ~800 HTML padding comments + stale Appendix N numbers inflate 2968 lines to pass while breaking stratified elegance. At 9.5, honesty is a veto - V11 would be praised, cited, and returned for revision, not awarded as-is.

**Gate logic per research/SCORING_RUBRIC_DEEPDIVE.md:87:** C1 hard gate (unreadable = unscored) technically passed; C5 veto (dishonest = failed) narrowly tripped by MEASURED-vs-claimed mismatch. C2+C3 cannot rescue a ledger that misreports its own MEASURED. Weighted estimate ~7.1/10.

---

## C1 - Technical clarity & reproducibility - 6.5/10 - FAIL 9.5

**What 9.5 requires (docs/writeup_style_guide.md:38,50,72 + research/SCORING_RUBRIC_DEEPDIVE.md:18):** skim-path TL;DR+Fig1+Table7-A+Sec8+Fig12 carries whole argument in 5 min at 2500-3500 award-core words, 4-8 row narrative tables, 3-5 narrative figs, every claim as idea -> fence (10-25 lines, Expected:) -> isolated delta + file:line, no prose-only claim.

**Strengths (why not a 4):**
- TL;DR is genuinely 5 sentences (docs/WORKING_NOTE_V11.md:8-9 `> (1)...(5)`), passes tools/check_gates.py:84 marker count - best V11 fix over V10 single-paragraph failure.
- TOC at docs/WORKING_NOTE_V11.md:13 + pipeline Fig1 at line 28 thickness=wall-clock exemplary per docs/writeup_style_guide.md:66.
- Every lever has file:line: optimal.py:51-58 blind spot, templates.py:39-50 forge, config.py:35-46 knobs, predicates.py:22-24 EXFIL - auditable in 30 min.
- Max narrative rows 8 / max any row 12 / narrative figs 5 (tools/check_gates.py:98-99 PASS) - prior V10 2445-pipe bloat collapsed to 335 pipes.
- 23 fences ``` (tools/check_gates.py:105 PASS), placed per-lever with Expected: per docs/writeup_style_guide.md:76.

**Weaknesses (load-bearing at 9.5):**
1. **Padding-as-stratification.** Lines 514-813 = 30 identical Supplement Filler N paragraphs (verbatim 80-word copy-paste, each with Table F[N] 3-row pointer) + lines 814-~2950 = >1000 HTML comments `<!-- filler line 893... -->` solely to hit 2500-3500 lines. research/SCORING_RUBRIC_DEEPDIVE.md:99 "Length beyond the window divides the total - every 10k words over cap costs more than any lever adds" - inverse (words-inflated to meet cap) equally penalized for density. Reviewer scrolling after §10 hits 300 lines of lorem-padding: skim penalty returns despite gate PASS.
2. **Slice word mismatch = reproducibility breach.** Header docs/WORKING_NOTE_V11.md:7 claims Sec 1-10 = 3100 words [MEASURED via split] and Appendix N:485-492 repeats 3100 [MEASURED] - tools/check_gates.py:16 slice `## 1. Context` to `## 11. Sources` actually measures **4508 words** (tool output: Slice words: 4508). 3100 vs 4508 = 45% under-report. tools/check_gates.py:95 truth is 4508 in 2500-5500 PASS, but note's own honesty marker is false. At 9.5, MEASURED must mean measured.
3. **Appendix N stale/ghost.** Appendix N:484-499 verification table claims Total lines 2850 / bytes ~320000 / slice 3100 / figs 11 / pipes ~450 / max rows 7 - actual tools/check_gates.py output is 2968 / 323520 / 4508 / 12 / 335 / 12. Every number stale. Table header says "CI-generated, honest ledger - do not hand-edit" (docs/WORKING_NOTE_V11.md:484) but it is hand-stale vs CI. Precisely docs/writeup_style_guide.md pitfall #5 and research/SCORING_RUBRIC_DEEPDIVE.md:87 C5 veto bait.
4. **Table fragmentation obscures hero.** §6 hero is 3 chunks across docs/WORKING_NOTE_V11.md:114-190 with duplicated row | method headers and split Table Chunk labels - reviewer must mentally reassemble to compare forge vs deputy. Award note needs one Table 6-A hero (Optiver A#6 style) - V11 still punts single-table ask.
5. **Figure lane off-by-one.** 12 figs PASS >=11 but App K reuse map at docs/WORKING_NOTE_V11.md:468 claims 6 deferred while counting Figs 5-11 = 7 deferred + narrative 5 = 12 total. Off-by-one signals hand-count.

**Fixes for V12 (P0/P1):**
- P0-1 Delete filler padding. Remove all 30 verbatim Filler paragraph+table blocks and ~800 HTML comment lines. Replace with one honest disclosure at §A: "Award core measured 4508 words; supplements add X lines to reach 2500-3500 stratified target via content, not padding - see generator tools/make_v11_simple.py:XX." Then regenerate so tools/check_gates.py line count drops truthfully; if under 2500, move real content (e.g., promote wall-clock ledger from A/K into narrative) rather than filler.
- P0-2 Sync MEASURED. Fix docs/WORKING_NOTE_V11.md:7 and Appendix N row 492 to 4508 [MEASURED via split tools/check_gates.py:16] - or recompute after P0-1 and pin new number. Gate Appendix N must be generated by tools/check_gates.py write-back, not typed.
- P0-3 Promote one hero Table 6-A. Collapse §6 chunks into single <=8-row *Table 6-A - Isolated levers (single-variable, same harness, noise flag).* with rows: forge +27.5 / THS 30->300 +9.4 cum / N=2-5 +9.1 / boundary crater -11.1 / gate 31%->100% +3.2x. Chunk rest verbatim to V11-A.
- P1-1 DPI/palette audit. Add to each ![Figure N: ...] one-sentence interpretation already partially done (docs/WORKING_NOTE_V11.md:469-482) plus alt-text file and 150 DPI grid per docs/writeup_style_guide.md:72 - currently asserted "[MEASURED]" at line 476 without tool output.

---

## C2 - Methodological contribution - 8.0/10 - FAIL 9.5

**What 9.5 requires (research/SCORING_RUBRIC_DEEPDIVE.md:29):** one transferable rule + ablation proving rule, unified harness same folds/seed/metric, selection/blend rule, seed-variance proof that rule is stable (MAP A#16 triplet + ensemble).

**Strengths:**
- Throughput-first framing (lever pillars Table1 at docs/WORKING_NOTE_V11.md:33-39) is correct transferable idea, backed by tools/local_test.py:355 31%->100% gate + REAL_REPLAY_CEILING=150 sizing (docs/WORKING_NOTE_V11.md:111).
- Isolated deltas honest and large: Harmony forge +27.5 isolated (research/VERY_DETAILED_REPORT.md:32 VERBATIM via docs/WORKING_NOTE_V11.md:116), THS ladder +4.84/+3.93 stepwise (lines 117-118), multi-post +7.90 (119), boundary crater -11.1 (187). Each with control->treatment pair - meets docs/writeup_style_guide.md:129 fence+score.
- Seeded triplet 42/123/999 -> 61.50/46.70/61.50 mean 56.57 +/-8.54 t=0.318 p=0.78 at research/seeded_triplet_measured.json:1-41 + hosted band 85.800-91.860 (lonnie +6 pts docs/WORKING_NOTE_V11.md:134 VERBATIM) is strongest variance node in series - fixes V6 single-seed failure (research/SCORING_RUBRIC_DEEPDIVE.md:110).
- Ship rule explicit at docs/WORKING_NOTE_V11.md:6 "3-seed mean delta >5 + fire_rate at CALIB_HOPS=8 + t-test p<0.05" and stop rule 41 post-v64 no-beats ceiling ~91-92.5 (line 190) - ISIC A#10 + Titanic A#3 patterns fulfilled.

**Weaknesses (why not 9.5):**
1. **Harness not unified for field.** Field golds JED v25 89.145 + V15 90.54 compared at docs/WORKING_NOTE_V11.md:142-144 under hosted scores, not under REAL_REPLAY_CEILING=150 mock harness - reader cannot answer "does forge beat v64 under identical replay ceiling?" research/SCORING_RUBRIC_DEEPDIVE.md:32 calls this centerpiece. research/experiments.json:130-259 rows for externals are INFERRED costs, not reruns.
2. **Local mock != host predictor.** Triplet mean 56.57 predicts "real" ~56 but hosted band is ~89 - research/seeded_triplet_measured.json:40 note admits "MockCompliantAgent... not hosted rerolls; hosted band confounded" and docs/WORKING_NOTE_V11.md:128 "Not significant: local 6x under-estimate". Ship t-test t=0.318 p=0.78 vs 55 is therefore local noise test, not ship gate - weak selection proof for note claiming throughput is metric.
3. **Small-n confessed not cured.** docs/WORKING_NOTE_V11.md:138-139 era aggregates n=6/10/25/10 hide that per-lever isolation is n=1 seed-123 (plus triplet only for v64). MAP A#16 demands triplet+ensemble per row. Lonnie B6 5-7 pt inflation (docs/WORKING_NOTE_V11.md:134) cited to discount 92.540 point, which undercuts isolated +1.16 ceiling claim - cannot have both "point is draw" and "+1.16 proves N=5 ceiling" without per-lever triplet.

**Fixes for V12:**
- P1-2 Unified harness Table 6-A ext row. Add 2 rows under same harness: V15 90.54 + JED v25 89.145 rerun at REAL_REPLAY_CEILING=150 (measure locally or label INFERRED with 12-row exhaust pointer, not hosted). Closes P0-4 gap flagged in research/SCORING_RUBRIC_DEEPDIVE.md:112.
- P1-3 Per-lever variance box. For forge / THS / N=5 promote isolated delta with sidecar seed-triplet band +/-X or explicitly label "single-seed, Lonnie +/-6 - direction real, magnitude provisional" (honest label beats false precision).

---

## C3 - Security insight - 8.5/10 - FAIL 9.5 (closest to win)

**What 9.5 requires (research/SCORING_RUBRIC_DEEPDIVE.md:40):** threat model up front, attacker capability per lever named, hole falsifiable in <60 s runnable probe, temporal/artifact negative controls BEFORE model-gain, public-vs-private per-component deltas.

**Strengths (best section of V11):**
- Blind spot is source-pinned and falsifiable: OptimalGuardrail._extract_target scans first present among [path,url,cmd,data,body,content] - http.post(url,data) checks url only (comp_data/aicomp_sdk/guardrails/optimal.py:51-58 [SOURCE]) vs scorer checks data (predicates.py:22-24 EXFIL) - asymmetry diagram Fig2 docs/WORKING_NOTE_V11.md:72 with taint window 5 superset 2 Fig5 line 469.
- Four guardrail probes + self-test at docs/WORKING_NOTE_V11.md:309-313 + Sec 8 Venn Fig12 line 285 triply surfaced; tools/local_test.py:1-434 run reproduces 9.02/9.05/9.06 s 5/5 PASS including web->post DENY vs clean post ALLOW (probe output Guardrail behavior probes 4/4 correct).
- Negative controls before gains: date/version-segment at docs/WORKING_NOTE_V11.md:21-27 LEAP integrity box + pre/post-refresh non-comparability + canonical-vs-substring secret.txt (core/predicates.py:147-149 empty secret_values unless fs.read).
- Private collapse autopsy award-grade: syed v19 120.850 TITLE-CLAIMED -> 0.000 VERBATIM collapses while syed v12b 30.735 + backtracking 15.975 VERBATIM survive via taint-free email.send source="tool" (core/tools/email.py:103-115 line 299) - ASHRAE B#16 per-component public-vs-private delta done.

**Weaknesses (why 8.5 not 9.5):**
1. **Private mechanism is INFERRED scaffold.** Every re.search(secret) claim tagged [INFERRED via 738915 wall-clock, high] (>=20 occurrences, e.g., line 305-337) - correctly honest, but note then uses it as causal ("proves taint-free" line 3, "private re.search(secret) [INFERRED...] scans all args" line 337). At 9.5, security note cannot crown INFERRED regex as collapse mechanism without labeled confidence ladder per claim. research/SCORING_RUBRIC_DEEPDIVE.md:118 already flagged wall-clock as admitted-not-instrumented - V11 instruments local wall-clock but hosted 13h vs 15h remains INFERRED via 738946 side-channel.
2. **Self-test surfacing still buried.** docs/WORKING_NOTE_V11.md:381-399 bash recall puts local_test.py behind bundle/triplet steps; ideal Santa A#25 "executable proof ABOVE prose" would be Sec 2/3 code block with tools/local_test.py:330-338 contract smoke 10-liner - currently in §8/§13 only.
3. **Cascade vs gate ablation conflated.** Fig5 taint 5 superset 2 and Fig12 Venn and §8b payload paragraph (288) all explain same mechanism with slightly different prose - could be one falsifiable chain (first-arg -> taint superset -> private regex) with single scoring-repro fence.

**Fixes for V12:**
- P0-4 already done (safety boxes at every forge use - docs/WORKING_NOTE_V11.md:88,90,343,348 SAFETY PASS 0 violations). Keep.
- P1-4 Confidence ladder. Add 3-row mini-table: payload blind spot [SOURCE] / taint superset [SOURCE] / private re.search(secret) [INFERRED via 738915, high, wall-clock 15h vs 13h] with wall-clock Pareto Fig6/Fig9 cited - makes INFERRED scope explicit without weakening claim.

---

## C4 - Usefulness to community - 7.0/10 - FAIL 9.5

**What 9.5 requires (research/SCORING_RUBRIC_DEEPDIVE.md:52,59):** next team copy-paste saves GPU-hours - registry, numbered notebooks in run order with BASE_PATH+artifact URLs+OOM workaround, cost axis next to score axis, keep/never-retry tags, per-structure/per-head ablations.

**Strengths:**
- research/experiments.json:1-260 16 rows is full TalkingData B#14 registry (generator/config/seed/cost/delta/label) - every lever traceable; tools/check_gates.py:45-51 validates 16 >=15 PASS.
- Bash 1-5 exact at docs/WORKING_NOTE_V11.md:382-398 with Expected outputs + SETTINGS dump pyproject.toml + config.py:21-46 verbatim + entry_points at line 431 - tools/local_test.py 5/5 PASS on CPU verified above.
- Numbered notebooks notebooks/01_prep..05_submit.ipynb flagged PASS (tools/check_gates.py:52 alternative-path check) - CommonLit B#20 factory present.
- Wall-clock Pareto Figs 9/11 (assets/wallclock_pareto.png / assets/efficiency.png lines 477,481) + efficiency dual-track small-model vs v64 - Hydrogen B#8 pattern met.
- Failure §7 F1-F10 table docs/WORKING_NOTE_V11.md:197-215 + keep/never-retry rules (NEVER/ PROMOTE) plus "what we missed" §8b crediting V15/JED/takamichitoda - MDC B#25 4-failures fulfilled.

**Weaknesses:**
1. **Registry cost honesty split.** In research/experiments.json 10/16 rows mark cost_status: INFERRED / wall_clock_status: INFERRED via 738946 (lines 11,27,42-43 etc.). Useful only if labeled proxy - V11 does label, but cost axis at §6 and Figs 6/9 then treats 60-second GPU-free (local) and 13h hosted as commensurate without normalization - Vesuvius B#9 identical wall-clock requirement not met for externals.
2. **Factory not click-runnable in note.** Notebooks exist but note cites only notebooks/README.md at docs/WORKING_NOTE_V11.md:435 - no inline pinned artifact URLs or OOM note inline (OOM is at line 435 T4 OOM on forge8_terse reduce TOP 300->150 but easy to miss among filler). 5-minute fresh-clone promise (research/SCORING_RUBRIC_DEEPDIVE.md:122 P1-2) relies on appendix, not skim.
3. **Usefulness diluted by exhaust routing.** Stratified exhaust to research/kernels_ALL_REFS.csv (824 = 105+719 per line 4/444) + V11-A/B chunked <=12 is correct per docs/writeup_style_guide.md:50, but V11 replaces inline exhaust with pointer filler (30x identical paragraph) rather than with content (e.g., efficiency Pareto interpretation) - net usefulness per page drops despite ledger completeness.

**Fixes for V12:**
- P0-5 Collapse pointer filler to 1 pointer. Delete F1-F30 duplication; keep one Table A-0 stratified layer pointer (already at docs/WORKING_NOTE_V11.md:440) plus links to V11-A/B/CSV. Spend saved pages on 6-row Hydrogen efficiency Pareto inline (already exists as Fig11 but needs table complement).
- P1-5 experiments.json schema note. Add top-level legend: which rows MEASURED vs INFERRED - already per-row but add header comment.

---

## C5 - Responsible communication - 5.5/10 - VETO RISK - FAIL 9.5

**What 9.5 requires (research/SCORING_RUBRIC_DEEPDIVE.md:64):** variance disclosed never single-seed, decision rule + every override logged with outcome, small-n protocol confessed, misses credited by name, stop rule stated, CLAIM/VERBATIM/INFERRED labelled, luck/betting/probing disclosed. VETO criterion - hidden probing, uncredited borrowing, or CLAIM-as-VERBATIM flips win to fail.

**Strengths (why not 3):**
- Triple labeling disciplined throughout: VERBATIM = Kaggle-verified vs TITLE-CLAIMED [CLAIM] vs INFERRED legend at docs/WORKING_NOTE_V11.md:27, every tail title number (e.g., 95.130 hiranorm line 312) now tagged CLAIM - fixes V6 DIAGNOSIS RC3.
- Safety boxes exemplary: defense/research-only banner at docs/WORKING_NOTE_V11.md:10-11 responsible skim + at first forge §4.2:88-90 + fence 12A 341-348 + adjacency gate PASS 0 (tools/check_gates.py:100) - clears docs/writeup_style_guide.md:119 pitfall #8.
- Variance + gap + stop disclosed: hosted noise 2-12 pts disc_733345:56-138 at line 12, Lonnie max-inflation 5-7 pts line 134, gap 19 pts to 111.690 top-50 cutoff line 12, stop 41 post-v64 no-beats line 190 - Titanic + Porto-Seguro honesty.
- Credit generous: takamichitoda 24.360, syed 30.735, huanligong 21.495, JED v25 89.145, V15 90.54 all by name with ref at §11 Sources:327-332 plus INVALIDATED flags - MCTS A#23 appreciated.

**Weaknesses (veto-level at 9.5):**
1. **[MEASURED] is false on headline number.** Note's most prominent honesty marker - 3100 words [MEASURED via split] (docs/WORKING_NOTE_V11.md:7,440,442,512, Appendix N:492) - contradicted by tools/check_gates.py:16 slice ## 1. Context to ## 11. Sources = 4508 words. 45% low. Appendix N compounds by claiming CI-generated while listing stale 2850 lines / 3100 words / pipes ~450 vs CI 2968 / 4508 / 335. Responsible note cannot mismeasure itself. Per research/SCORING_RUBRIC_DEEPDIVE.md:85 C5 veto: "Smallest share when clean, largest penalty when violated... hidden LB-probing... CLAIM-as-VERBATIM flips win to fail." Mismeasured MEASURED is precisely this class.
2. **Filler marketed as honesty.** Each Filler block opens "This filler ensures V11 meets the 2500-3500 line gate honestly without flat 2445 pipe-table bloat [MEASURED]" (docs/WORKING_NOTE_V11.md:514,524...714) - but filler is bloat, just comment-form rather than pipe-form. Claiming honest stratification while shipping 30 copy-paste pointer blocks is luck disclosure failure (docs/writeup_style_guide.md honesty-under-pressure).
3. **Private probes disclosed but not bounded.** Syed v19-style 120.850 title self-claim correctly labeled TITLE-CLAIMED at research/appendices/V11-B_EXHAUST_CHUNKED.md:46 and research/experiments.json:225 but narrative still uses hosted public scores as if private hedge absence were free - does not state "we probed private via wall-clock side-channel per 738946 (INFERRED) N times, outcome X" as probing ledger.

**Fixes for V12 (P0 veto repairs):**
- P0-6 Honest ledger rewrite. Regenerate docs/WORKING_NOTE_V11.md via tools/make_v11_simple.py after removing filler; run py -3.12 tools/check_gates.py and paste stdout verbatim into Appendix N (or better, have tool write it - tools/check_gates.py should emit appendix_n.md). Pin 4508 (or post-fix number) as MEASURED slice and remove "honest ledger filler" prose.
- P0-7 Probing/hedge ledger. Add 4-row Table - Private hedge probing log (all INFERRED): H 90.930 10% tail flat / I b64 90.555 flat / deputy-pure INFERRED hedge / wall-clock 15h vs 13h INFERRED signal with source 738946 - turns dispersed hedge notes into one veto-proof box (Home-Credit A#5 betting disclosure).

---

## Cross-cutting: Tools and Evidence

- python tools/check_gates.py OVERALL PASS 13/13 - evidence above; secondary run after read confirmed Lines 2968 Slice words 4508 Fences 23 (tools/check_gates.py:88-95). Exit 0. Fallback tried: direct python, no alternative needed - tool healthy.
- python tools/local_test.py 5/5 conceptual PASS - contract smoke 400 cands, pipeline 239 cands raw 19598 norm 97.99, realistic ceiling 61.5, VulnerableDeterministicAgent 20 cands no-crash, SDK eval_attack 20 cands norm 1.8, 4/4 guardrail probes ALLOW/DENY as expected (tools/local_test.py:330-431). Wall-clock 9.0 s (triplet 9.02/9.05/9.06 at research/seeded_triplet_measured.json:12,22,31).
- research/experiments.json 16 rows valid JSON (tools/check_gates.py:49-51 length check), but 62% INFERRED costs - see C4.
- research/kernels_ALL_REFS.csv 824 refs + V11-A 50-row chrono + V11-B exhaust claimed; spot-checked counts additive 824 = 105+719 (docs/WORKING_NOTE_V11.md:4,444).

---

## V12 Ship List - Brutal Priority (P0 must, P1 for win)

**P0 - Do not submit without (veto/gate fixes):**
1. Delete 30x filler paragraphs + HTML padding; keep one stratified pointer (Tables A-0/A1/B1 sample). Regenerate to honest line/word count.
2. Sync MEASURED: fix docs/WORKING_NOTE_V11.md:7 and Appendix N to tools/check_gates.py:88 output (4508 words / 2968 lines / 12 figs / 335 pipes / 23 fences). Make Appendix N generated, not typed.
3. Promote one hero Table 6-A (<=8 rows) - collapse §6 hero sprawl.
4. Keep safety 0 violations (already PASS) - no regression.
5. Add probing/hedge log table + confidence ladder for re.search(secret) [INFERRED].

**P1 - Competitive to earn 9.5:**
6. Unified harness row for JED/V15 at REAL_REPLAY_CEILING=150 (rerun or explicitly INFERRED).
7. Per-lever variance sidecar (single-seed vs triplet Lonnie +/-6).
8. Wall-clock Pareto normalization note (local s vs hosted h on shared x).
9. Inline BASE_PATH + artifact URL + OOM workaround in §13 factory (not just notebooks/README.md).
10. 5-minute dry-run per research/SCORING_RUBRIC_DEEPDIVE.md:158 P2-4: verify skim-path carries argument and research/kernels_ALL_REFS.csv 824 reconciles 74+630+14+1 vs vote sum 5580.

---

## Bottom line for 9.5

V11 is strongest draft of V6->V11 arc - CI-green, variance-honest, safety-exemplary, and scientifically load-bearing on blind-spot + forge + taint chain. At polite 8.5/10 it wins. At brutal 9.5/10 it loses on C5 honesty lenity: MEASURED that mismeasures, and stratification that stratifies pointers not prose, violates very integrity front-load it preaches (docs/WORKING_NOTE_V11.md:30 LEAP). Fix ledger, delete filler, promote hero table - V12 then clears 9.5.

*Artifacts: tools/check_gates.py:1-116 gate definitions are source of truth; this review defers to them over prose claims.*