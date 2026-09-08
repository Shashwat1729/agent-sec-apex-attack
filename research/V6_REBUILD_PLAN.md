# V6 Rebuild Plan — 1st-Position Target (50 Winning-Writeup Lessons Synthesized)

**Date:** 2026-09-06
**Goal:** Rebuild docs/WORKING_NOTE_V5.md (3120 lines, 42921 words — 7.8x over award window) into V6 that wins 1st position: award-readable skim path (2500-5500 words base) + auditable exhaust path (FULL 74 code-read + 630 banded + 105 ours = 810 weighted).
**Sources synthesized:** research/WINNING_NOTES_A_25.md (Set A, 25 notes), research/WINNING_NOTES_B_25.md (Set B, 25 notes), research/DIAGNOSIS_NOTE_GAP.md (7 root causes + V6-A..E fix plan), docs/writeup_style_guide.md (12-section template + 10-point checklist).
**Non-negotiable constraint:** base 23 sections stay byte-identical in narrative; ALL new bulk goes to stratified appendices (chunked <=12-row tables, 1 new figure). Reviewer skim-penalty is the #1 enemy (guide: >6k words loses reviewers).

---

## 1. 50-Note Patterns — 10 Lessons for V6

Distilled from 50 notes (Set A #1-25 + Set B #1-25). Each lesson states the pattern, the exemplar notes, and the concrete V6 action.

### Lesson 1 — One ablation table is the centerpiece (the table IS the argument)
- **Pattern (Sets A+B unanimous):** ~80%+ of award notes carry >=1 ablation or CV-vs-LB table; every method section ends with a paired before/after delta. Optiver-Close-2024 hyd (A#6): one 5-models-x-5-treatments table (CatBoost 5.8287 -> 5.4165, final blend 5.8117/5.4030) proves model + online-learning + post-processing with zero adjectives. IEEE-Fraud 1st (A#1): per-trick LB ladder (XGB 0.9510 -> +UID aggs 0.9602 -> +postprocess 0.9618). BirdCLEF-2024 (B#12): min-vs-mean fusion table + 0.96 public-private correlation. MDC-2025 (B#25): stage-addition ladder (doi-only 0.362/0.350 -> +acc 0.754/0.664 -> +Qwen 0.890/0.797).
- **V6 action:** Keep ONE hero ablation table in Section 7 (ours: v2->v64 climb, isolated single-variable branches, <=8 rows) + ONE field family-matrix in V6-D (6x4, technique x evidence). Every other ledger is chunked to appendices. No prose-only claim survives — each lever gets `control -> treatment = +x.xx isolated`.

### Lesson 2 — Integrity front-loading (provenance before method)
- **Pattern:** LEAP-ClimSim 1st greysnow (A#13, "no-leaky" in title): leak-inoculation section FIRST (100+ copy-run notebooks, full pipeline HF->TFRecords->train->infer), then architecture; won under suspicion spotlight by pre-answering it. LMSYS 1st (A#14): "no-leak" framing in leakage-plagued comp. Malware-Prediction-2019 7-liner (A#21): temporal-artifact negative control as the whole post. Home-Credit-2024 yuuniee (A#5): separated model skill from metric-hack betting, credited leak reporters by name. Airbus-2018 reset (B#23): dataset changed mid-comp -> re-validate everything, label pre- vs post-reset.
- **V6 action:** Section 2/4 opens with provenance block: freeze date (2026-08-07 disc 733058), pre-refresh vs post-refresh vs private-era score comparability rule, no-leak ablation (what we checked), luck/betting disclosure. Title-claim numbers from 630 tail labeled CLAIM, never VERBATIM. Private-transfer labeled INFERRED.

### Lesson 3 — Story spine: EDA -> insight -> code -> validation (one insight per section)
- **Pattern:** Style guide + IEEE-Fraud archetype (guide:11): EDA -> "not time, clients" reframe -> UID `card1+addr1+D1` 6-line groupby -> time-consistency filter -> GroupKFold -> ensemble/post-process. Quora 1st (B#18): 3 feature families -> Siamese/ESIM -> rescaling -> 4-layer stack, each family with its CV number. Vesuvius-Ink 1st (B#9): TL;DR ("larger crops win") -> depth-invariance constraint -> 1024-crop ladder at identical cost. LANL 1st (B#19): "public LB is lying" -> train-test alignment via paper-p4677 stats -> 150+ features -> LGBM+NN geomean.
- **V6 action:** Each lever subsection follows `idea (1 sentence) -> fence (runnable code/test) -> isolated delta (paired numbers)`. Low-award listing ("20 subs without delta") is banned by checklist. V6 keeps 4-6 levers in narrative (forge token, multi-post N=5, guardrail/sentinel, CD-hedge, wall-clock), rest to appendices.

### Lesson 4 — Pipeline figure first (reviewers skim figures before prose)
- **Pattern:** Benetech 2nd hallstatt, RSNA-Aneurysm-2025 (B#2, coarse-to-fine recall gate), ARC-2024 (B#5, TTT pipeline overview.png), HPA-2021 (B#21, UMAP proof), Santa-2025 gallery (A#25, 200-solution exhibition = legible in 10 s). Guide:92-94: Figure 1 pipeline in Section 2, guardrail trace in Section 3/5, progression line + ablation bar in Section 7.
- **V6 action:** Figure order fixed: Fig 1 pipeline (sandbox->guardrail->scoring, thickness=wall-clock) in Section 2; Fig 2 guardrail trace (clean `http.post` ALLOW vs `web->post` DENY, taint-5 superset predicate-2) in Section 5; Figs 3-4 ablation bar (N=4/5/6 ceiling) + score-progression line (v2->v64 with crater labels, <5pts noise note) in Section 7. ONE new figure in V6 (Fig 11 field distribution, Sec 3.3 below). Total 11 embeds: justified as 10 base + 1 field-coverage proof; reuse map V6-M lists all with no duplicates.

### Lesson 5 — Failure closing (what-did-not-work + what-we-missed + credit)
- **Pattern:** MCTS-variants 1st James Day (A#23): dedicated "Trust CV vs Trust LB" + "failures" + "missed avenues (flip augmentation, credit goldenlock)" — reads as science, not victory lap. APTOS Zoo 9th (A#9): "why we are not 1st / what winners did that we skipped" with quantified pseudo-label gap (0.922->0.931). MDC-2025 (B#25): 4 named failures (Qwen-for-DOI worse, DataCite-relations, fancy prompts, Marker-OCR too slow) each with reason. Titanic honest-reporting (A#3): Optuna-tuned 0.847 CV -> 0.794 LB negative with stop rule.
- **V6 action:** Section 8 keeps >=3 failure families with real isolated deltas + diagnosis (encoded-marker hedge, forge7/8 v72/v73 regressions, TOKEN/rotation no-lift). Section 8b "What we missed / field did better" credits rival notebooks by ref (forge 90.54 V15, JED-v25 89.145). V6-E gives all 50 code-read NEUTRAL rows one lesson line each with keep/never-retry tags. Named-credit appreciation section (B#4 Santa-2024 + B#25 MDC pattern).

### Lesson 6 — Variance disclosure (never a single-seed headline)
- **Pattern:** Jigsaw-multilingual Seed-42 (A#12): seed-vs-score table, same config -> medal-or-not swings. MAP-2025 1st (A#16): 8-model comparison with single-seed loss/MAP@3 triplets + 3-seed ensemble columns; "trust LOSS over MAP@3"; multi-seed >> multi-fold. ISIC-2024 (A#10): 5-fold x10-seed t-test p<0.05 ship rule + honest log of violating it (lowered to 0.2 under pressure). ARC-2025-5th Lonnie (B#6, cautionary): seed-as-hyperparameter confession, 344th-public->5th-private, +-4 tasks/120 variance math. Porto-Seguro 1st (B#15): CV std ~0.01+ reported prominently on 0.65-AUC-ceiling data.
- **V6 action:** Headline v64 92.540 always ships with seed-triplet + ensemble column + noise floor note (`Single-run deltas <5 pts are noise; field 2-12 pts [733345]`). 120-sample-class selections state the selection protocol + variance table (Lonnie warning). Decision rule (ship threshold) stated in Section 6 with every override logged with outcome (ISIC pattern).

### Lesson 7 — Reproducibility: factory, not story (seeds/hardware/requirements/commands)
- **Pattern:** Strongest: ARC-2024 (B#5, Apache-2.0 + retrain recipe + wheels + weights + params.json), CommonLit 1st (B#20, 5 numbered Colab notebooks in run order + weight packs + OOM workaround), TalkingData 1st (B#14, Docker/AWS + feather cache + JSON experiment registry), Feedback-ELL 1st (B#7, train_first_step.sh/train_second_step.sh/train_pl.sh + pinned A6000/Ubuntu20.04/py3.9.13/CUDA11.6), Santa-2025 (A#25, notebook-first inverted pedagogy + 200-gallery). Weakest norm overall (A cross-cutting #5) — which is why doing it wins.
- **V6 action:** Appendix B checklist + exact bash 1->6 (guide:133); SETTINGS.json + entry_points + requirements pinned; gateway date + SDK pin + model IDs; per-trick LB deltas (Santa/LEAP pattern); Figure 11 reproducible from committed research/field_distribution_source.csv via committed script (DIAGNOSIS V6-C acceptance). Numbered pipeline notebooks in run order with BASE_PATH convention (CommonLit pattern).

### Lesson 8 — 3-5 figures max in narrative (each with caption + one-sentence interpretation)
- **Pattern:** Median 3-5 figures across 50 notes (A cross-cutting #3, B cross-cutting #3). Terse winners ship 0-2 (LMSYS 0, Optiver-Close 0 — table carries it) and still win; bloat (>8) is paper-penalty per Gabruseva (guide:72). Vision/audio notes spend budget on visual proof (Vesuvius before/after cleanup captioned, HPA UMAP Fig.4a, BirdCLEF spectrograms, Airbus masks); tabular notes stay table-led.
- **V6 action:** Narrative keeps base 10 (already over guide cap — grandfathered with reuse map); V6 adds exactly 1 (Fig 11 distribution: votes-vs-rank log-y + family-pie inset + VERBATIM-histogram inset, PNG <=1200px, DPI>=150, colorblind-safe, grid alpha=0.3, caption + interpretation + alt text). No further new figures without deleting one. Deferred figures (family heatmap, tail-coverage map) stay deferred — stated explicitly so reviewers see budget discipline.

### Lesson 9 — Tables 4-8 rows with isolated deltas (chunk the rest, never print 74 rows inline)
- **Pattern:** Rossmann 1st (A#2): full feature dictionary as THE artifact (60+ features x 4 membership flags) — but structured, not dumped. LLM-Science 7th (A#15): 11-row ensemble-weight vector. House-Prices (A#4): unified-CV harness table (same folds/seed/metric) makes blend weights defensible. Guide:50: 4-8 rows; >10 rows move to docs/experiments.md and link. V5 obeys: 23-A split 10+10, 23-B 6 rows, 23-C 3 rows, 23-D 5 rows, appendices 8-12 rows (DIAGNOSIS RC2).
- **V6 action:** No table >12 rows anywhere (build gate). Full 74 reprinted stratified by bucket (single-post 17 / forge 7 / multi-post 11 / other 39) in 12-row chunks reusing V5-H pattern (V6-A). 630 tail as ~26 band tables of 8-9 rows (25-rank bands, V6-B). 105 ours stay condensed in Sec 22.1 via Tables W-A..W-D pointers (report V4:2622-2730), top-15 hurt synthesis in 23-D. Every row carries rank/ref/votes/bytes/family/payload/guard/verdict + file:line pointer.

### Lesson 10 — Hook + TL;DR 4-6 sentences (1800-2500 word median band, density beats length)
- **Pattern:** Word counts bimodal: terse (~600-900: LMSYS A#14, Numina AIMO A#18, Cassava B#13, VSB-notebook B#22) vs comprehensive (2500-6500: IEEE companion, Quora 3500, LANL 4000, LEAP 3500+, ARC paper 6000). Median band 1500-2500 (B) / 1800-2500 (A). Every winner opens with a hook: reframe (IEEE "labels are per-card"), provocation (RSNA-Brain "very simple code", Malware-BIG "NO to overfitting"), luck confession (Optiver overtime, ISIC sliding 23rd-down), gambling frame (Home-Credit "Betting Strategy"), heresy (Lonnie seed-as-hyperparam). Guide A3: 4-6-sentence Summary with what/why/score/repo link.
- **V6 action:** Title block (authors, competition link, best single v64 92.540, code link) + TL;DR box 4-6 sentences + auto-TOC after TL;DR. Base narrative budgeted to 2500-5500 words; V5's 42921 words are 7.8x cap — V6 does NOT add narrative words, only appendix rows. Hook: full-field 810 weighting + honest private-gap autopsy (differentiators Sec 4) in sentence 1-2 of TL;DR.

---

## 2. Mapping: 10 Lessons x 5 Award Criteria

The 5 award criteria: **(C1) Technical clarity, (C2) Methodological contribution, (C3) Security insight, (C4) Usefulness, (C5) Responsible communication.** Primary (P) + supporting (s) marks per lesson.

| Lesson | C1 Technical clarity | C2 Methodological contribution | C3 Security insight | C4 Usefulness | C5 Responsible communication |
|---|---|---|---|---|---|
| L1 one ablation table | **P:** paired deltas replace adjectives; isolated single-variable branches | s: unified harness makes blend/choice defensible (House #4) | s: guard on/off + payload-swap rows quantify the hole | s: reader can copy the one table as their own test plan | s: noise floor (<5pts) labeled per cell |
| L2 integrity front-loading | s: provenance block is skimmable in 30 s | s: no-leak ablation is a method (LEAP) | **P:** threat model = artifact/temporal-leak adversary; negative controls | s: others reuse the provenance checklist | **P:** CLAIM vs VERBATIM vs INFERRED labels; luck/betting disclosed |
| L3 story spine | **P:** one insight per section, EDA->code->validation | s: pipeline-per-lever generalizes (Quora families, Vesuvius invariance) | s: each lever names the attacker capability it tests | s: idea->fence->delta is copy-paste runnable | s: fences make claims falsifiable |
| L4 pipeline figure first | **P:** Fig 1 + Fig 2 make system legible in 10 s | s: stage-gate metrics (recall gate, B#2) are a contribution | **P:** guardrail-trace figure makes blind spot falsifiable | s: diagrams beat 1000 words for re-implementers | s: colorblind-safe captioned figures, alt text |
| L5 failure closing | s: diagnosis prose > action lists | **P:** negative results are the rarest trusted content (Titanic Optuna, MDC 4-failures) | s: wrong-payload TOKEN + opaque-blob rows are do-not-adopt intel | **P:** keep/never-retry tags save readers GPU-hours | **P:** miss-credit to rivals, stop rules stated |
| L6 variance disclosure | s: seed triplets + ensemble columns | **P:** validation methodology as deliverable (MAP, Numina harness) | s: prevents security overclaim from a lucky seed | s: ship/no-ship rule (t-test) is directly reusable | **P:** overrides logged; small-n selection protocol confessed (Lonnie) |
| L7 reproducibility factory | s: exact bash 1->6 + pinned env | s: JSON registry / numbered notebooks are infra contributions | s: runnable guardrail self-test (10 lines, no GPU) | **P:** factory > story (CommonLit chain, ARC wheels+weights) | s: OOM/failure modes documented, not hidden |
| L8 figure budget | **P:** 3-5 (here 10+1 grandfathered+mapped) keeps skim-path alive | s: UMAP/spectrogram-style proof figures where metrics do not convince | s: taint-window + wall-clock visuals carry the security claim | s: gallery/progression figures are the 10-second pitch | s: budget discipline itself signals reviewer-respect |
| L9 chunked tables | **P:** 4-8-row narrative tables; 12-row appendix chunks | s: feature/artifact registry as reusable artifact (Rossmann) | s: payload x guard matrix exposes the hole taxonomy | **P:** full 74 + 630 banded + 105 pointers = exhaust-path for auditors | s: 0 refs dropped; ERROR row retained |
| L10 hook + TL;DR | **P:** 4-6-sentence TL;DR + TOC = 5-minute verify path | s: one transferable idea up front (LMSYS "Distill is all you need") | s: hook names the attacker/defender reframe | s: density beats length (1800-2500 band) | s: scores + code links in first screen |

**Coverage check:** every criterion has >=3 primary lessons (C1: L1,L3,L4,L8,L9,L10; C2: L5,L6; C3: L2,L4; C4: L5,L7,L9; C5: L2,L5,L6). No criterion is carried by a single lesson.

---

## 3. Concrete V6 Structure (Sections 1-24: placement, tables/figures, word budget)

**Budget rule:** Sections 1-12 (narrative) = 2500-5500 words TOTAL (award window). Sections 13-24 (appendices) = unbounded rows but <=12 rows/table, words only in captions + one-line interpretations. Base Sections 1-12 byte-identical to V5 except TL;DR hook refresh + Figure 11 pointer; all bulk lands in 13-24.

| Sec | Title | What goes where | Tables / Figures | Word budget |
|---|---|---|---|---|
| 1 | Title block | Authors, competition link, best single (v64 92.540), code link, 810-scope line (ours 105 + field 705 = 49 helped / 38 hurt / 722 neutral / 1 error) | none | 60-100 |
| 2 | TL;DR box (A3, 4-6 sentences) | Hook (full-field 810 + private-gap autopsy) -> what/why/score/repo; auto-TOC after | none | 120-180 |
| 3 | Context: threat model + fixtures + task envelope | Fixtures, budgets, attacker capabilities; integrity front-load (freeze 2026-08-07 [733058], pre/post-refresh rule) | Fig 1 pipeline (reuse); Table 3-A 4-row pillar (what/why) | 250-400 |
| 4 | Data & environment | Fixture/class histogram (n= + zero-spike note); hardware, GGUF/date pins, requirements, SETTINGS.json, entry_points | fixture histogram (reuse) | 200-350 |
| 5 | Methodology levers (1 subsection per lever, idea->fence->delta) | Forge token injection; multi-post N=5; guardrail/sentinel discipline; CD-hedge; wall-clock side-channel | Fig 2 guardrail trace (reuse); runnable fences 10-25 lines w/ `# Expected:` | 600-900 |
| 6 | Validation harness + private hedge | Local harness (5 checks) + 3 things local cannot check + private hedge; GroupKFold/time-split rule (Rossmann/NVIDIA); seed-triplet protocol (MAP/Jigsaw) | Table 6-A harness (<=8 rows) | 300-450 |
| 7 | Experiments: climb + craters + ablation | HERO Table 7-A: isolated climb 60.7->92.54 (v8->v22 +27.5 forge; v51->v64 +1.16 multi-post; <=8 rows); marginal tables; noise note | Fig 3 ablation bar N=4/5/6; Fig 4 progression v2->v64 + crater labels (reuse) | 400-600 |
| 8 | What did not work + what we missed | >=3 failure families w/ real deltas + diagnosis (encoded-marker hedge, forge7/8, TOKEN/rotation); miss-credit w/ numbers | Table 8-A failures (<=8 rows) | 300-450 |
| 9 | Insights & defenses | For builders + benchmark designers + self-test recipe (IEEE 10-line guardrail self-test, no GPU) | code fence: guardrail self-test | 250-400 |
| 10 | Responsible & limitations | Variance (seed triplets, <5pts noise), infra limits, gap-to-100+ autopsy, CLAIM/VERBATIM/INFERRED labeling | none (prose + variance quote block) | 200-350 |
| 11 | Sources | SDK pin + gateway date + >=4 discussions + >=3 papers w/ links; upstream-vs-fork diff table (Konwinski A#22 pattern) | Table 11-A upstream diff (<=8 rows) | 100-200 |
| 12 | Repro checklist & exact bash | 10-point gate (guide:122-134); bash 1->6; local_test.py 5/5 PASS link | checklist (bullets, not table) | 100-200 |
| 13 | V6-A: full 74 stratified (code-read) | 74 rows by bucket (single-post 17 / forge 7 / multi-post 11 / other 39) + 1 ERROR; cols: rank/ref/votes/bytes/family/payload/guard/verdict + file:line; verbatim from FIELD_CODE_ANALYSIS.md:11-94 + report V5:3290-3428 | ~7 tables x <=12 rows (reuse V5-H chunk pattern) | captions + 1-line interp only |
| 14 | V6-B: 630 banded (metadata-only) | ~26 bands of 25 ranks (61-85 ... 686-705), 8-9 rows each; cols: rank-range/n/vote-sum/top-title/stale-flag; full refs in kernels_ALL_REFS.csv sortRank 61-705; vote sums reconcile to 5580 tail total | ~26 tables x 8-9 rows (extend V5-K pattern) | captions only; CLAIM labels |
| 15 | V6-C: Figure 11 distribution | assets/field_distribution.png: (a) votes-vs-rank log-y (annotate V1-V15 + rank-54 ERROR), (b) family-share inset (17/7/11/39/1), (c) VERBATIM-histogram inset (85-91, 9 scores); source research/field_distribution_source.csv + script | Fig 11 (1 new PNG) | caption + 1-sentence interp + alt |
| 16 | V6-D: family matrix (technique x evidence) | 6 rows (single-post/forge/multi-post/other/CD-hedge/wrong-payload) x 4 cols (n HELPED+NEUTRAL / VERBATIM-peak / v64-lever fed / private-transfer INFERRED); cells cite rank refs + line anchors; HURT=0 rationale quoted (FIELD_CODE_ANALYSIS.md:110-111) | Table 16-A 6x4 (6 rows) | caption + per-cell refs |
| 17 | V6-E: 50 NEUTRAL one-line lessons | 50 lines grouped by failure mode: opaque-blob 11 / stale-sweep 8 / fork-baseline 14 / rotation-ablation 6 / multi-post-unadopted 10 / CD-opaque 1; format: ref + why-NEUTRAL + keep/never-retry | bullets grouped (no mega-table) | 50 lines, ~30 words each |
| 18 | V6-F: 105 ours condensed pointer | Tables W-A..W-D live in report V4:2622-2730 (condensed Sec 22.1, not reprinted); top-15 hurt synthesis Table 23-D (5 rows, all ours D1-v10..D15-v31) | pointer + Table 23-D (5 rows reuse) | caption only |
| 19 | V6-G: reproduce fences | Fetch/pull commands (V5-G/V5-H pattern extended); pull manifest rows 1-75 in 12-row chunks; field_distribution build script | manifest tables x <=12 rows | commands verbatim |
| 20 | V6-H: tail teachers per 100-rank block | Keep 61/275/54 teachers; add one CD-final per block (rank 117 xiaoz259, 161 aleaiest, 178 cdeotte) | Table 20-A teachers (<=8 rows) | caption + 1 line each |
| 21 | V6-K: 630-tail pointer index | 25-rank-band pointer (12+9+9+8 pattern) into kernels_ALL_REFS.csv | pointer tables | captions |
| 22 | V6-M: figure reuse map (11 figures) | 10 base + Fig 11; no duplicates; palette/DPI/grid compliance note | map table (11 rows -> split 6+5) | map only |
| 23 | V6-N: scoring-math example + verification table | E[raw] display block; S=raw/200 inline; counts reconciliation (74+1+630=705; 705+105=810; 49/38/722/1); 0-dropped check vs kernels_ALL_REFS.csv | Table 23-A verification (<=8 rows) | math + table |
| 24 | V6-O: next-read queue + reviewer paragraph | Next-read queue; one-paragraph reviewer summary (DIAGNOSIS Sec 5: stratified not lost — skim-path + exhaust-path) | none | 120-180 |

**Build gates (PASS/FAIL before calling V6 award-ready):** (i) heads `#`x1 `##`x24 hierarchy intact, TOC anchors work; (ii) counts 74+1+630=705, 705+105=810, 49/38/722/1 reconciled; (iii) no table >12 rows, narrative tables 4-8 where guide requires; (iv) Figure 11 single new PNG within palette/DPI/grid rules, alt text present; (v) 630 labeled metadata-only/INFERRED, title numbers CLAIM, private transfer INFERRED, ERROR retained; (vi) guide 10-point checklist all checked incl. local_test.py 5/5 PASS.

---

## 4. 1st-Position Differentiators (4 things that beat typical winners)

Typical winners do L1-L10 well. V6 wins by doing 4 things typical winners do NOT:

### D1 — Full-field 810 weighting (nobody else scores the whole field)
- Typical winner: ablates their own 5-10 variants (Optiver-hyd 5x5, MAP 8-model). V6: 810 weighted verdicts (ours 105 code-verified 25/38/42/0 + field 705: 74 code-read 24/50/0/1 + 630 banded metadata) with reconciliation table. The family matrix (V6-D) shows WHERE each v64 lever came from (forge peak V15 90.54 + JED-v25 89.145; single-post 6-of-9 VERBATIM 85-89; multi-post caution rank-6 0.00-private) — provenance no 1st-place note publishes because no 1st-place team reads 705 notebooks.
- Beating move: judge can verify top-20 in 5 minutes (Sec 23.1 split 10+10) and auditor can exhaust all 810 in 30 minutes (V6-A+B). Two-path readability is itself the contribution.

### D2 — Honest private-gap autopsy (temporal-artifact controls + public-vs-private per component)
- Typical winner: reports public LB as final (ASHRAE-14th->1st shakeup survivors excepted). V6: pre-refresh frozen (2026-08-07) vs post-refresh vs private-era September comparability rule stated up front; per-component public-vs-private deltas (ASHRAE B#16 pattern); trivial temporal-artifact controls run and reported (Malware-2019 7-liner A#21 pattern: version/date-segment baselines before model claims); rank-6 public-only max-fill 95.130-pub/0.00-priv as the cautionary exhibit; Vesuvius-Surface public-overfit confession (B#10) as house norm.
- Beating move: private-gap section converts our weakest point (refresh-shift) into the most-trusted section — exactly the ISIC ship-rule-violation + Home-Credit betting-disclosure effect that judges reward with Working Notes.

### D3 — Runnable guardrail self-test (10 lines, no GPU, copy-paste falsifiable)
- Typical winner: describes the guardrail/pipeline in prose + config dump. V6: ships the IEEE-1st-style 10-line self-test (guide:93-101: clean-post ALLOW vs web-tainted DENY) PLUS the taint-window visualization (Fig 2: taint-5 superset predicate-2 -> UNTRUSTED unreachable; same check misses `data`) PLUS the wrong-payload TOKEN 3-way ablation (rank 60/V5/V8) as the negative control. Follows Santa-2025 notebook-first ordering (A#25): runnable code ABOVE prose.
- Beating move: reviewer falsifies our central security claim in <60 seconds without a GPU. No competing note offers a faster falsification loop.

### D4 — Wall-clock side-channel math (score-vs-compute frontier, not just final score)
- Typical winner: reports final score + hardware footnote. V6: publishes the cost axis next to the score axis (Feedback-Efficiency Hydrogen B#8 pattern: dual-track score AND cost; Santa-2024 B#4 pattern: perplexity-vs-compute curve; Vesuvius crop-ladder "1024 beats 512 at IDENTICAL wall-clock" B#9 pattern): replay-ceiling truncation (REAL_REPLAY_CEILING=150, ~6x anti-inflation), per-lever wall-clock ledger, N=4/5/6 ablation bar proving the N=5 boundary, layer-wise/offload-style inference recipe where applicable (MAP-2025 32B-on-T4 spirit).
- Beating move: turns infrastructure honesty (timeouts, OOM workarounds, Colab V100/P100 notes per CommonLit B#20) into a methodological contribution — the efficiency Pareto that benchmark designers actually need for the next competition.

---

## 5. Execution order (build sequence)

1. Freeze base Sections 1-12 (byte-identical export from V5) + refresh TL;DR hook only.
2. Build V6-A (74 chunked) -> verify 74+1 rows, 0 dropped vs kernels_ALL_REFS.csv, every row file:line.
3. Build V6-B (630 banded ~26 tables) -> verify band n sums 630, votes reconcile 5580.
4. Generate Fig 11 + research/field_distribution_source.csv + script -> verify PNG spec + caption/interp/alt.
5. Build V6-D matrix + V6-E 50 lines (refs unique, 0 overlap w/ 24 HELPED) + V6-F..O pointers.
6. Run build gates (Sec 3 bottom) + guide 10-point checklist; fix until all PASS.
7. Reviewer dry-run: 5-minute skim (TL;DR + Fig 1/2 + Table 7-A + Sec 8 + Fig 11) must carry the whole argument.

*End — research/V6_REBUILD_PLAN.md*
