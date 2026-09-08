# Scoring Rubric Deep-Dive: What Actually Wins Working Notes

Date: 2026-09-06

Sources: research/WINNING_NOTES_A_25.md (Set A, 25 notes), research/WINNING_NOTES_B_25.md (Set B, 25 notes), docs/WORKING_NOTE_V6.md headers (Secs 1-24 + V6-A..V6-O scope), research/V6_REBUILD_PLAN.md (10 lessons x 5 criteria matrix, Sec 2), docs/writeup_style_guide.md (12-section template + 10-point checklist + 8 pitfalls).

Host rubric (NOT rank alone): (C1) Technical clarity and reproducibility; (C2) Methodological contribution; (C3) Security insight; (C4) Usefulness to benchmark community; (C5) Responsible communication. Leaderboard performance is supporting evidence only.

Thesis in one line: C1/C5 are table stakes (pass/fail gates - miss one checkbox and you are out); C3+C4 are the differentiators (mechanism + reusable factory is what separates 1st-note from 2nd-note when both have ablations); C2 breaks ties among mechanism-grade notes.

---

## 0. Method note: awards vs LB rank (why 50 winners, not 50 first-places)

Set A+B deliberately include non-1sts that won the documentation game. The award-vs-rank split is the single most important inference for V7:

| Non-1st exemplar | Rank | Why it is award-grade (scoring signal) |
|---|---|---|
| APTOS Zoo (A#9) | 9th gold | Why-we-are-not-1st loss autopsy with quantified pseudo-label gap (private 0.922 to 0.931 from 13th-place study). Judges reward self-critique over victory laps. |
| Jigsaw Seed-42 (A#12) | 13th gold | Seed-vs-score variance table as THE result. Methodology sections outlive results - cited 3 years later by MAP-2025. |
| MCTS goldenlock rival (A#23 ctx) | missed trick | Winner credits rival flip-augmentation he missed (0.01 better hybrid exists). Generosity reads as science. |
| ARC-2025 Lonnie (B#6) | 5th (344th public to 5th private) | Cautionary inclusion: seed-as-hyperparameter confession + variance math (+-4 tasks/120). Honest heresy beats hidden selection. |
| Malware-2019 7-liner (A#21) | leak post, not a model | Perfect negative control (7 lines, 0.681 private, no training). Proved the board measured sampling lag, not skill. Controls are contributions. |
| Home-Credit yuuniee (A#5) | 1st but ethics-forward | Betting Strategy frame + named leak-reporter credit + luck disclosure. Candor is award fuel. |
| Vesuvius-Surface (B#10) | 1st with overfit confession | Rank-1 both boards yet confesses public-overfit threshold + adds requested post-processing ablation AFTER publishing. Living documentation. |
| ISIC-2024 (A#10) | 1st with rule violation | States p<0.05 ship rule AND logs violating it (lowered to 0.2 under pressure, leaned on LB). Overrides logged beats rules stated. |

Inference for V7: do NOT chase we-are-rank-N prose. Chase the 8 behaviors above: autopsy, variance table, rival credit, negative control, luck disclosure, overfit confession, override log, living-doc update. Every one maps to C5 + C4 - the two criteria most 1st-place-only notes under-invest.

---

## 1. Per-criterion: what judges actually reward (inferred from 50 winners)

### C1 - Technical clarity and reproducibility (can I rerun it in 5 minutes?)

What wins: file:line on every claim + seeds/hardware/requirements/commands + runnable fences with Expected comments + one insight per section (story spine EDA to code to validation).

| Signal | Winner pattern (Sets A+B unanimous) | V6 status | V7 gap |
|---|---|---|---|
| file:line anchors | IEEE-1st UID 2-liner + GroupKFold protocol (A#1); TalkingData JSON experiment registry tying every feature to a generator (B#14); ARC-2024 run_finetune script + params.json (B#5) | STRONG - V6 Sec 2 pillar table + Sec 4 levers carry templates.py:39-50, optimal.py:51-58, config.py:35-43 | Keep. Add upstream-vs-fork diff table (Konwinski A#22 pattern) in Sec 11 |
| seeds/hardware/requirements/commands | Feedback-ELL 1st pins A6000/Ubuntu20.04/py3.9.13/CUDA11.6 + train_first_step.sh run order (B#7); CommonLit 5 numbered Colabs + weight-pack URLs + OOM workaround (B#20); MAP-2025 exact base-model IDs + quant alpha + A100/RTX/T4 split (A#16) | MEDIUM - V6 has bash 1-6 + SETTINGS.json + GGUF c099eb4 pin; seed-triplet promised in rebuild plan L6 but headline v64 92.540 still ships mostly single-run | V7 MUST: seed-triplet + ensemble column on headline; decision rule + override log (ISIC pattern); OOM/timeout failure modes documented |
| runnable fences + Expected | Style-guide IEEE-1st 10-line guardrail self-test (clean ALLOW vs web-tainted DENY); Santa-2025 notebook-first ordering, runnable code ABOVE prose (A#25); Vesuvius channel-shuffle failed-convergence control (B#9) | STRONG - V6 Sec 7.0 B64 self-probe + Sec 5 four guardrail probes + local_test.py 5-check harness | V7 MUST: 10-line GPU-free self-test as Figure-2 companion in Sec 5 (falsifiable in under 60 s); wrong-payload TOKEN 3-way ablation as negative control |
| story spine, one insight per section | IEEE labels-are-per-card reframe to UID to filter to GroupKFold (A#1); Quora 3 feature families each with CV number (B#18); LANL public-LB-is-lying to alignment to 150+ features (B#19) | STRONG - V6 Sec 4 levers follow idea to fence to isolated delta | Enforce ban: no prose-only claim survives; every lever gets control-to-treatment isolated delta (rebuild L3) |
| figure-first legibility | Santa-2025 200-solution gallery legible in 10 s (A#25); RSNA-Aneurysm coarse-to-fine recall-gate schematic (B#2); ARC-2024 TTT overview.png (B#5); HPA UMAP Fig.4a proves de-noising (B#21) | STRONG - V6 Fig 1 pipeline + Fig 2 guardrail trace + Fig 3 ablation bar + Fig 4 progression + Fig 11 field distribution | Freeze at 11 (10+1 grandfathered+mapped). No new figure without deleting one (rebuild L8). |

C1 scoring rule of thumb: the reviewer tries the 5-minute verify path (TL;DR + Fig 1/2 + hero Table 7-A + self-test). If it runs, C1 passes regardless of prose length. If it does not, no word count saves it.

### C2 - Methodological contribution (what is transferable beyond this LB?)

What wins: novel search framing + ablation with isolated single-variable deltas + rejected alternatives with numbers (not vibes).

| Signal | Winner pattern | V6 status | V7 gap |
|---|---|---|---|
| novel framing, one transferable idea | LMSYS Distill-is-all-you-need 70B-to-9B logits under inference constraints in 700 words (A#14); ARC-2024 stability-based SELECTION criterion as the contribution, not the generator (B#5); MAP-2025 trust-LOSS-over-MAP@3 validation methodology (A#16); Numina eval-harness-as-deliverable (A#18) | STRONG - V6 throughput-first search (forge + halving + validate-then-keep) beats prompt art, forge +27.5 isolated | Sharpen to one sentence up front (LMSYS density): public scoring is a throughput game on one primitive won by X, reaching Y. Cut everything else from TL;DR. |
| hero ablation table, methods x treatments, paired deltas | Optiver-hyd 5x5 (model x OL x PP, CatBoost 5.8287 to 5.4165, blend 5.8117/5.4030), zero adjectives needed (A#6); IEEE per-trick ladder 0.9510 to 0.9602 to 0.9618 (A#1); MDC stage ladder 0.362/0.350 to 0.754/0.664 to 0.890/0.797 (B#25); BirdCLEF min-vs-mean fusion + 0.96 pub-priv correlation (B#12) | STRONG - V6 Table 7-A climb 60.7 to 92.54 (8 rows max, isolated branches) + V6-D 6x4 family matrix | V7 MUST: Table 7-A is the centerpiece figure of the note (rebuild D1). Every other ledger chunked to 12-row appendices. Noise floor (under 5 pts, field 2-12 [733345]) labeled per cell. |
| rejected alternatives, why not X | MAP aux-SFT marginal kept as negative (A#16); Vesuvius synthetic Derm-T2IM helps-single-hurts-ensemble, dropped (A#10); MDC 4 named failures with reasons (B#25); RSNA-Brain very-simple-code minimal control kept to end (B#3) | STRONG - V6 Sec 7.0 ten families F1-F10 + Table 6b H1-H10 ledger + Sec 4.3 why-we-rejected-evolutionary/MCTS/Go-Explore with budget math | Add minimal-solution control alive to end (RSNA-Brain pattern): plain single-post without forge/halving, and what complexity added. |
| unified harness, blend weights defensible | House-Prices one KFold harness for all models (A#4); ISIC 5-fold x10-seed t-test ship rule (A#10); Porto-Seguro DAE-pretrain vs from-scratch Gini with CV-std prominent (B#15) | MEDIUM - V6 race ranks by eff = mean_raw/mean_cost at CALIB_HOPS=8 (true replay cost) + head-start floor; seed handling still single-run | V7 MUST: frozen CV harness statement (same folds/seed/metric for all variants) + seed-triplet table; never blend or select on vibes or single-seed. |
| selection-rule ablation | ARC-2024 stability-vs-likelihood selection ablation (B#5); MDC tool-assignment matrix (which subtask ML wins vs LLM wins) + failures justifying split (B#25) | WEAK - V6 eff ranking starves deputy (16 over 4) admitted post-hoc (F8); the selector itself never ablated | V7 MUST: ablate the selector (eff vs raw vs survivability-weighted) on a held-out replay split; report which rule picks the private winner. |

C2 scoring rule of thumb: one 4-8-row table with isolated deltas + one rejected-alternative row beats ten pages of architecture prose. Listing 20 submissions without deltas = style-guide pitfall 1, scores near 0 on C2.

### C3 - Security insight (what hole, what mechanism, what defense?)

What wins: named mechanism (blind spot / taint / template / bug) + measurement (guard on/off, payload swap) + defenses (builder + designer) + self-test (falsifiable in under 60 s).

| Signal | Winner pattern (security-adjacent subset) | V6 status | V7 gap |
|---|---|---|---|
| mechanism named precisely | IEEE UID reframe labels-are-per-client (A#1); Malware-BIG feature-family taxonomy + XGBoost-as-judge loop (A#20); Prompt-Recovery adversarial-attack frame (A#17, thin but directional); G2Net trainable-whitening-as-layers (B#24) | STRONG - V6 outbound-payload blind spot (first-present-arg check optimal.py:51-58) + taint-window-5 superset predicate-2 + private re.search(secret) collapse | Keep mechanism name in title + TL;DR sentence 1. Name the attacker capability each lever tests (rebuild L3). |
| measurement, guard/payload ablations | Malware-Prediction 7-liner AvSigVersion segment-vs-label-rate table (A#21); Vesuvius depth-invariance + channel-shuffled failed control (B#9); HPA weak-label de-noising on/off mAP + UMAP proof (B#21); LANL alignment on/off +0.27 reproduced by a reader (B#19) | STRONG - V6 data-vs-url trace + web-to-post DENY vs clean ALLOW + B64 literal-vs-encoded trap + TOKEN wrong-payload rows | V7 MUST: guard on/off + payload-swap rows IN Table 7-A (not just appendices): clean-post ALLOW / web-tainted DENY / encoded-marker 0-raw / TOKEN wrong-payload. The hole quantified in the hero table. |
| stage-gate / cascading metrics | RSNA-Aneurysm stage-1 segmentation evaluated as recall gate for stage-2 classifier (B#2); Vesuvius 3D-UNETR to 32ch to SegFormer 2-stage with per-stage numbers (B#9) | WEAK - V6 race-to-fill pipeline reports end-to-end only; no per-gate recall (race crown rate, fill keep rate, replay survival rate) | V7 MUST: per-stage metrics + gate-ablation (no-race vs race; no-validate vs validate-then-keep). Cascading numbers beat one headline (Set-B lesson 1). |
| defenses, two audiences | Home-Credit metric-hack disclosure + award-the-leak-reporters proposal (A#5); LEAP I-win-anyway no-spacetime ablation (A#13) | STRONG - V6 Sec 8 defenses (data-flow/provenance on every sink; strip control tokens; re.search parity) | Split defenses builder-vs-designer (V6 Sec 9 pattern): builder checklist (fire_rate, cost_replay, hedge 70 percent) + designer guidance (provenance replay, wall-clock parity, private-wheel disclosure). |
| self-test + visual proof | Style-guide 10-line guardrail test; HPA UMAP Fig.4a, metrics alone do not convince (B#21); Santa gallery (A#25); BirdCLEF spectrograms (B#12) | STRONG - V6 Fig 2 + B64 probe + local_test.py 5/5 | V7 MUST: self-test ABOVE prose (Santa notebook-first ordering) + taint-window visualization (taint-5 vs predicate-2 Venn). Reviewer falsifies central claim without GPU. |

C3 scoring rule of thumb: the note that names the narrowest falsifiable mechanism (first-present-arg stops at url, data never inspected) + ships the 10-line test beats the note with three vaguer insights. Specificity is the score.

### C4 - Usefulness to benchmark community (what can I steal on Monday?)

What wins: checklist + pinning guidance + sizing rules + hedge testing + factory (numbered notebooks, registries, weight URLs).

| Signal | Winner pattern | V6 status | V7 gap |
|---|---|---|---|
| checklist with thresholds | V6 Sec 9 Red-Team checklist (fire_rate, cost_replay, 15h vs 13h, 70 percent hedge rule) matches winner shape (Rossmann feature-registry A#2, MDC tool-assignment matrix B#25) | STRONG | Keep + add sizing rule (see below) as checklist row 1. |
| pinning guidance, every external artifact | LLM-Science RAG playbook pins dumps/embedders/chunk-counts (A#15); ARC-2024 wheels+weights+params.json Apache-2.0 (B#5); TalkingData Docker/AWS + feather + JSON configs (B#14) | MEDIUM - V6 pins GGUF/date/gateway/SDK; field tail pins partial (metadata-only 630) | V7 MUST: pin table (artifact / version / hash-or-date / where-used): SDK pin, gateway date, GGUF c099eb4, fixture hashes, top-3 field notebook refs+versions. |
| sizing rules, score-vs-compute frontier | Santa-2024 perplexity-vs-compute curve (B#4); Vesuvius 1024-beats-512-at-IDENTICAL-wall-clock, context is free (B#9); Hydrogen efficiency-track Pareto + efficiency_model.yaml (B#8); ASHRAE granularity-diversity ensemble for board-shift (B#16) | MEDIUM - V6 has REAL_REPLAY_CEILING=150 (6x anti-inflation) + N=4/5/6 boundary bar + 8750-vs-9000 budget math | V7 MUST: wall-clock frontier figure/table: N=4/5/6 x FILL_FRAC x TOP vs public + wall-clock; TOP300 ceiling + TOP450/TOP600 craters as more-is-not-better proof; per-lever wall-clock ledger. |
| hedge testing, public-vs-private per component | ASHRAE public-14th-to-private-1st with per-component pub-priv deltas (B#16); LANL ignore-public-LB + alignment ablation (B#19); aleaiest pure-deputy 29.73-to-29.67 vs pure-EXFIL 100.665-to-0.000 selected-pair trap (V6 Sec 6.4) | STRONG - V6 Sec 6.3/6.4 pub-vs-priv tables + hedge pool-neutral verdict | V7 MUST: hedge-fraction sweep (10 percent vs 70 percent vs pure-deputy) with BOTH pub and priv numbers. Even if post-hoc, label INFERRED honestly (ISIC pattern). |
| factory, not story | CommonLit numbered notebooks + BASE_PATH + weight URLs (B#20); Feedback-ELL shell-scripted curriculum (B#7); BirdCLEF run_unlabeled_preprocessing/train/inference.py configs (B#12) | MEDIUM - V6 tools/bundle.py, local_test.py, make_notebook.py + pull manifests; run-order numbering partial | V7 MUST: numbered pipeline (1 fetch to 2 race to 3 fill to 4 bundle to 5 local_test to 6 submit) with exact bash verbatim + RAM/timeout notes. |

C4 scoring rule of thumb: the most-copied section wins C4. Checklists, registries, sizing rules, and hedge tables get forked; adjectives do not. Write the section you wish you had found on day 1.

### C5 - Responsible communication (do no harm, disclose everything)

What wins: benchmark-only scope + no real-system instructions + private-wheel honesty (INFERRED/CLAIM/VERBATIM labels) + variance honesty + failure/miss credit.

| Signal | Winner pattern | V6 status | V7 gap |
|---|---|---|---|
| benchmark-only scope + no real-system instructions | Defense/Research-Only banner (targets the Kaggle sandbox and vendored SDK guardrail, nothing production) matches security-note norm (Prompt-Recovery attack-story framing done responsibly, A#17) | STRONG | Keep banner ABOVE title block (first screen). Repeat scope in Sec 8 defenses (control-token patterns documented so builders can detect them). |
| private-wheel honesty | ISIC ship-rule-violation log (A#10); Lonnie single-seed public-picked confession (B#6); MDC labeling critique F1-should-be-macro (B#25); Vesuvius template-version caveat (B#10) | STRONG - V6 CLAIM/VERBATIM/INFERRED labels + private-claims-INFERRED + 630-tail CLAIM-only rule | V7 MUST: never promote a TITLE-CLAIMED tail score to VERBATIM; every tail number carries CLAIM + selection-protocol note (Lonnie warning). ERROR row retained (0 dropped). |
| variance honesty | Jigsaw seed table (A#12); MAP 3-seed ensemble columns (A#16); Porto-Seguro CV-std prominent on 0.65 ceiling (B#15); final-batch 85.80-91.86 = 6.06-pt same-bytes band (V6 Sec 6.5) | MEDIUM - V6 noise rule stated (under 5 pts noise [733345]) but headline lacks triplet | V7 MUST: headline = point + triplet + ensemble + noise note, every time. 120-sample-class selections state protocol + variance table. |
| failures + stop rule | Titanic Optuna-tuned 0.847 CV to 0.794 LB + stop rule (A#3); MCTS Trust-CV-vs-Trust-LB + failures + missed avenues (A#23); Quora DL-code-promised gap flagged honestly (B#18) | STRONG - V6 F1-F10 + H1-H10 + craters v72/v74/v91 with isolated deltas + never-retry rules | Add explicit stop-rule sentence per family (Titanic pattern): we stopped X when Y; the rule is Z. |
| miss-credit + appreciation | MCTS goldenlock credit (A#23); Santa-2024 + MDC named-credit appreciation sections (B#4, B#25); Home-Credit leak-reporter credit (A#5) | STRONG - V6 miss-credit to forge 90.54 V15 and JED-v25 89.145 + V6-E 50 NEUTRAL one-line lessons | Keep named-credit section. Add what-winners-did-that-we-skipped quantified from others (APTOS-Zoo pattern): deputy-primary + two-msg form with external numbers. |
| silent-control-token flag | Style-guide pitfall 8: not flagging control-token injection troubles safety reviewers | MEDIUM - V6 flags forge as control-token injection (ChatInject 2509.22830) + strip-control-tokens in Sec 8 | V7 MUST: flag in TL;DR-adjacent scope box, not buried in Sec 4.2. Safety reviewers skim; silence reads as concealment. |

C5 scoring rule of thumb: responsible notes are not penalized for low rank - they are rewarded for making rank INTERPRETABLE (variance, wheel-hidden, selection protocol, luck). One integrity flag can sink all five criteria (LEAP no-leaky inverse).

---

## 2. Scoring failure modes (what loses points — inferred negatives from 50 winners + style guide)

Every winner in Sets A+B avoids these; every thin/low-award note commits >=1. Map each to the criterion it kills and the V6 header it would violate (`docs/WORKING_NOTE_V6.md:1-35` + `docs/writeup_style_guide.md:110-120` 8 pitfalls + `research/V6_REBUILD_PLAN.md:56-72` 10x5 matrix).

| # | Failure mode | What it looks like | Criteria hit | Winner contrast (what award notes do instead) | V6/V7 guard |
|---|---|---|---|---|---|
| F1 | **Listing without isolated deltas** (style-guide pitfall #1) | 20 submissions enumerated as story beats; no control->treatment paired number. "We tried X, then Y" with only final score. | **C1 FAIL, C2 0** | Optiver-hyd A#6: every method section ends with CV/LB delta; IEEE A#1 per-trick ladder; MDC B#25 stage ladder. One 4-8-row hero Table 7-A with `control -> treatment = +x.xx isolated` (rebuild L1). | Build gate: no prose-only claim survives (`V6_REBUILD_PLAN.md:24`). V6 Sec 7 isolated branches only; `docs/WORKING_NOTE_V6.md:227` `<5 pts noise` rule. |
| F2 | **Untruncated mock scores** (pitfall #2) | Local replay of 2000 cands in-process reported as "score 120+" without truncation; mock underestimates replay latency ~6x (`V6:217`, `tools/local_test.py:64`). | C1, C4 | LEAP greysnow A#13: 100+ copy-run notebooks at true replay cost; TalkingData A#14 true-cost sizing (10/80 future counts). V6 fixes: `REAL_REPLAY_CEILING=150` (`V6:212`), probe1/bill8, `REPLAY_SAFE_FRAC=0.97`. | V7: label proxy vs replay-verified; never report untruncated mock as headline. |
| F3 | **Encoded marker (literal vs decode trap)** | `base64(SECRET_MARKER)` / hex / URL-encode without prior `fs.read(secret.txt)` -> `secret_values=[]` -> `_contains_secret` literal check fails -> 0 raw both LBs (`V6:399`, `predicates.py:144`). | C3, C4 | Malware-BIG A#20: canonical-vs-substring mismatch named explicitly (`secret.txt` basename vs `secret|password|...` substring). V6 drops encoding (Table 6 row 5: lit True / encoded False). | V7: B64 self-probe in Table 7-A as negative control (rebuild D3). |
| F4 | **Moonshot bundles** (pitfall #6) | 3 ideas changed together; crater hides which lever hurt (V6 v94: v91 -9.46 + v92 -11.3 bundled -> 91.91 flat, confounded). | C2, C5 | MCTS A#23: per-trick CV/LB delta ledger; Santa-2025 A#25: one idea 90 days. V6 `V6:261` 20 single-variable tests; bundled confounds labeled. | V7: one variable per submission; bundled combos only after singles. |
| F5 | **Missing `what-did-not-work` / stop rule** (pitfall #7, guide A6) | No failures section; or failures without numbers/diagnosis. Reads as victory lap, not science. | **C2, C5** | Titanic A#3: Optuna 0.847 CV -> 0.794 LB + stop rule; MDC B#25: 4 named failures with reasons; ISIC A#10: violated ship rule logged. | V6 Sec 7.0 F1-F10 + H1-H10 (`V6:372-426`), Table 6b + crater deep dives; rebuild L5 requires >=3 families with diagnosis + credit. |
| F6 | **Silent control tokens** (pitfall #8) | Harmony `<|end|><|start|>assistant<|channel|>...` used but not flagged as control-token injection; safety reviewers read as concealment. | **C5 FAIL** (can sink all criteria) | LEAP "no-leaky" A#13 front-loads integrity; LMSYS "no-leak" A#14. ChatInject `arXiv:2509.22830` disclosed in V6 Sec 8 + banner. | V7: flag in TL;DR-adjacent scope box, not buried Sec 4.2 (rebuild C5 table). |
| F7 | **TITLE-CLAIMED scores as VERBATIM** | Tail notebook title says 88.5; body unreachable (auth-walled); cited as 88.5 verbatim without `CLAIM` label. 630 tail V6 is metadata-only. | **C5**, C1 | Airbus-2018 B#23 flagged thin; G2Net B#24 code-strong/prose-thin flagged. V6 labels: CLAIM vs VERBATIM vs INFERRED (`V6:20`, `V6:32`). | V7: 630 labeled CLAIM + selection-protocol note (Lonnie B#6 warning); ERROR retained, 0 dropped (`V6_REBUILD_PLAN.md:108`). |
| F8 | **Variance hidden (single-seed headline)** | Headline 92.540 single run; field band 2-12 pts [733345] not disclosed; small-n (120-task) selection with no variance math (Lonnie B#6). | C1, C5 | Jigsaw A#12 seed table; MAP-2025 A#16 8-model x 3-seed ensemble columns; Porto-Seguro B#15 CV-std prominent. | V7: headline = point + seed-triplet + ensemble + noise note (rebuild L6); 120-sample selections publish variance table. |
| F9 | **Missing per-stage / per-head metrics** | Pipeline reported only end-to-end; no gate recall, no per-family beam metrics (Rossmann A#2 feature-registry, RSNA-Aneurysm B#2 recall-gate). | C2, C4 | RSNA-Aneurysm B#2 coarse-to-fine recall gate; Vesuvius B#9 stage1->stage2; BirdCLEF B#12 per-chunk. | V7: per-stage recall/keep/survival rates; gate-ablation rows (rebuild C3/C4). |
| F10 | **Tables >12 rows inline / figures >8 / prose >6k** | 74-row dump inline, gallery unchunked, >6k words losing reviewers (Gabruseva A#25 guide:72). Bimodal winners are 1800-2500 or terse 700. | C1 | Rossmann dictionary structured 60+ x 4-flag table (A#2) but FINDABLE; guide `V6_REBUILD_PLAN.md:48` >10 rows -> `docs/experiments.md`. V6 chunks to 12-row appendices. | V7: narrative 2500-5500 words; appendices chunked 12 rows (rebuild L9); Fig 11 only new figure (L8). |
| F11 | **Stale / fork-baseline claimed as novelty** | Fork of Santa-2024 public notebook with no diff table; Kaggle `sorted-other-words` renamed. | C2, C5 | Konwinski A#22 fork-diff table (upstream vs changed why + validity rate); Santa-2024 B#4 fork URLs + versions named. | V7: upstream-vs-fork diff Table 11-A (rebuild Sec 11); stale-sweep 8 rows flagged. |
| F12 | **Private-wheel hand-waving** | Private scores quoted as if read from wheel; gateway never shipped private wheel (`V6:534-535`). | C5 | ISIC honest deviation; Home-Credit betting disclosure A#5. V6 INFERRED labels. | V7: private transfer always INFERRED; wall-clock side-channel disclosed as side-channel, not score. |
| F13 | **Wall-clock / sizing omitted** | Score without cost axis; no budget math (8750 vs 9000), no TOP ladder. | C4 | Santa-2024 perplexity-vs-compute; Vesuvius context-is-free at identical wall-clock; Hydrogen B#8 Pareto. | V7: wall-clock frontier figure + N=4/5/6 x FILL x TOP matrix (rebuild D4). |
| F14 | **No decision rule / override unlogged** | Ship rule stated but override hidden (vs ISIC A#10 honest log). | C5 | ISIC 5-fold x10-seed t-test + log lowering 0.05->0.2; MAP trust-LOSS rule. | V7: threshold + every override outcome in Sec 6. |
| F15 | **Visual proof missing where metrics do not convince** | Weak-label de-noising claimed without UMAP; segmentation without before/after. | C3, C4 | HPA UMAP Fig.4a B#21; Vesuvius before/after cleanup caption B#9; BirdCLEF spectrograms. | V7: taint-window Venn + gallery/progression figures with caption+interpretation+alt (rebuild L4/L8). |

Summary: the 15th failure (F15) is the tie-breaker most teams skip — when labels are noisy or guardrails are hidden, a figure that proves separation beats a table that asserts it.

---

## 3. Weighting hypothesis — which criteria separate 1st-note from 2nd-note

### 3.1 Table-stakes vs differentiators (inferred from 50 winners + host rubric weight)

Host says: 5 criteria co-equal; LB rank is supporting evidence only (`docs/WORKING_NOTE_V6.md:54` rubric block). In practice 50 winners reveal a **tiered scoring** mental model:

| Tier | Criteria | Role | Evidence from 50 | V6 header evidence |
|---|---|---|---|---|
| **Gate** | **C1 Technical clarity + reproducibility** | **Pass/fail.** Most 1sts (LMSYS 700 words A#14, Cassava 700 B#13, VSB notebook 700 B#22) still pass C1 with just config + repo link. Missing file:line / seeds / commands is an auto-fail regardless of insight. | Cross-cutting A#5: reproducibility is weakest norm overall — which is why doing it wins; but not doing it is not partially penalized, it is failed. Guide checklist 10-point gate `writeup_style_guide.md:125-134`. | V6 Sec 5 + Sec 13: 5-check harness, bash 1-6, GGUF `c099eb4` pin, 10-line self-test. |
| **Gate** | **C5 Responsible communication** | **Pass/fail with veto.** One integrity flag (LEAP suspicion A#13, Airbus reset B#23, Malware-BIG 0.681 leak A#21) can sink all five. Integrity front-loading is negatively weighted: absence hurts more than presence helps (rebuild L2). | LEAP "no-leaky" in title; Malware 7-liner as negative control; Lonnie B#6 confession rewarded, hidden selection punished. | V6 Sec 10 scope box + CLAIM/VERBATIM/INFERRED + private INFERRED + ERROR retained + variance honesty. |
| **Differentiator** | **C3 Security insight** | **Rank-ordered.** The narrowest falsifiable mechanism wins. First-present-arg at `optimal.py:51-58` + taint-5 superset-2 + private `re.search` collapse is narrower than 3 vague insights. | Malware BIG A#20 feature-family taxonomy + judge loop; Vesuvius depth-invariance + failed shuffle control B#9; Prompt-Recovery attack framing A#17 as genre signal. | V6 Sec 4.1-4.2 + Fig 2 + Sec 8 defenses + self-test. |
| **Differentiator** | **C4 Usefulness to benchmark community** | **Rank-ordered, most-copied wins.** Checklists, registries, sizing rules, hedge tables get forked; adjectives do not. | Rossmann feature registry 60+ x 4 flags A#2; ARC wheels+weights B#5; CommonLit numbered notebooks B#20; MDC tool-assignment matrix B#25; Santa-2024 compute frontier B#4. | V6 Sec 9 checklist + V6-D 6x4 family matrix + V6-E 50 one-line lessons + V6-A/B stratified field. |
| **Tie-breaker** | **C2 Methodological contribution** | **Breaks ties among mechanism-grade notes.** Novel search framing + hero ablation with isolated deltas + rejected alternatives. When C3+C4 both strong, the note with the cleaner harness/ablation wins. | Optiver 5x5 without adjectives A#6; MAP validation methodology A#16; House-Prices unified harness A#4; Quora 3-family taxonomy B#18. | V6 Table 7-A climb + Table W-E1 era aggregates + F1-F10 + H1-H10. |

**Hypothesis in one sentence:** **C1 and C5 are necessary, not sufficient (table stakes — you cannot win without them, but they do not make you win); C3 (mechanism specificity) + C4 (reusable factory) rank the top 10; C2 (ablation discipline) breaks ties within the top 3.**

Why this weighting fits the 50:

* **C1 table-stakes proof:** terse winners (LMSYS 700, Numina 600, Cassava 900) still won with minimal prose because they shipped the one runnable recipe; comprehensive winners (IEEE companion 6500, Quora 3500, LEAP 3500) won with the same recipe plus tables. Length did not rank. Missing `seed/hardware/requirements/commands` is the only C1 failure that recurs in thin-note post-mortems (B#23, B#24 flagged).
* **C5 veto proof:** ISIC A#10 violated its own p<0.05 rule yet was rewarded because it logged the violation; Lonnie B#6 picked a seed on 120 tasks and told the truth — also rewarded as cautionary inclusion. The inverse (hidden selection, TITLE-score as VERBATIM) is the fastest way to lose judges even at rank 1.
* **C3+C4 differentiator proof:** ARC-2024 B#5 (53.5% + stability criterion + Apache-2.0 factory) beat MindsAI 55.5% which stayed closed — higher LB lost to higher usefulness. Porto-Seguro 0.65 ceiling A#15 won with the noisiest CV ever because the DAE representation insight + CV-std disclosure were more useful than the 0.29698 delta. HPA B#21 won with a Nature Methods paper + UMAP proof, not just mAP.
* **C2 tie-breaker proof:** Optiver A#6 vs IEEE A#1 — both have mechanism + factory, but the note whose ablation table is cleaner (paired deltas, noise floor labeled) is the one reviewers cite.

### 3.2 Score simulation (illustrative, not host weights)

If judges score 0-5 per criterion (25 max), inferred bands for a 4,200-team competition like Agent-Sec:

| Profile | C1 | C2 | C3 | C4 | C5 | Total | Award likelihood |
|---|---|---|---|---|---|---|---|
| Unranked but perfect factory + honest (CommonLit B#20) | 5 | 4 | 2 | 5 | 5 | 21 | **Honorable/working-note** (rank irrelevant — CLP 1st was 1st, but Vesuvius B#9 pattern shows non-1sts get notes) |
| Rank 1, terse, no failures, hidden variance | 3 | 3 | 4 | 2 | 2 | 14 | **Not awarded** (C5 veto, C4 weak) |
| Rank 6 multi-post 95.130-pub -> 0.00-priv (hiranorm) | 2 | 2 | 1 | 1 | 1 | 7 | Negative exemplar — proves leak, not insight |
| **Our V6** (92.540 pub / 0.07 priv, full-field 810, honest gap) | 5 | 4 | 5 | 5 | 5 | **24** | **1st-note contender** if C3 specificity + C4 factory hold |
| Pure-deputy private winner 46.425 (Xz) with no note | 1 | 2 | 3 | 1 | 2 | 9 | Prize winner, not note winner — inverse relationship is the point |

Lesson: **chasing LB rank without the factory is negatively correlated with note score.** The note that wins documents *why* rank collapses (gap autopsy), not that rank is high.

### 3.3 What this means for V7 vs V6

V6 already passes gates (C1 5/5, C5 5/5 per build gates `V6_REBUILD_PLAN.md:108`). The remaining points are in **C3 specificity (make mechanism falsifiable in <60 s) and C4 reusability (make the factory forkable in 5 min) and C2 tie-breaker (make Table 7-A the cleanest table the judge sees all cycle).** That is why Section 4 below front-loads self-test, pinning, frontier figure, and hero-table polish — not more narrative words.

---

## 4. Fifteen concrete scoring-maximizing actions for V7 (build-ready)

Each action names the exact file:line anchor, the criterion it scores, and the winner it copies. All 15 are single-variable, verifiable, and map to the 10x5 matrix in `research/V6_REBUILD_PLAN.md:60-71`.

| # | Action (what to ship, where, how) | Criteria | Winner copied | File:line / figure anchor |
|---|---|---|---|---|
| 1 | **Integrity front-loading box on page 1** — freeze date 2026-08-07 [733058], pre-refresh vs post-refresh vs private-era comparability rule, no-leak ablation list, CLAIM/VERBATIM/INFERRED legend in 6 lines before method. Title-claim numbers never VERBATIM. Private-transfer always INFERRED. | **C5 (P)**, C1 | LEAP greysnow A#13 no-leaky first; Airbus reset B#23 | `docs/WORKING_NOTE_V6.md:20` scope scope; `V6_REBUILD_PLAN.md:20` L2 action |
| 2 | **Ablation hero Table 7-A as centerpiece (4-8 rows, isolated deltas, noise floor per cell)** — v2 60.69 -> forge +27.5 -> v22 validate-then-keep +4.84 -> v34 SH/head-start +3.93 -> v51 multi-post N=2-4 +7.90 -> v64 N=5 +1.16 = 92.540; craters v72 -11.1 / v74 -10.3 / v91 -9.46 as companion rows. Every cell: `control -> treatment = +x.xx isolated`, flag `<5 noise`. | **C2 (P)**, C1 | Optiver 5x5 A#6; IEEE per-trick ladder A#1; MDC stage ladder B#25 | `V6:248-258` Table 3; `V6_REBUILD_PLAN.md:16` L1 |
| 3 | **10-line GPU-free guardrail self-test with Expected comments (falsifiable in <60 s)** — `Guardrail().decide(http.post url=... data=SECRET_MARKER) -> ALLOW` clean vs `recent_sources=[web] -> DENY`; canonical `secret.txt` True / `dir/secret.txt` False; literal True / b64 False. Ship ABOVE prose (Santa notebook-first A#25). | **C3 (P)**, C1, C5 | IEEE 10-line guide + style-guide fence; Vesuvius failed-shuffle control B#9 | `V6:483-502` self-test; `V6:389-398` B64 probe; `docs/writeup_style_guide.md:93-101` |
| 4 | **Variance seed-triplet + ensemble column on headline, every time** — v64 92.540 ships as `92.540 (triplet mean +- std, n=3, ensemble=..., <5 noise [733345])`; final-batch 85.80-91.86=6.06-pt band shown; 120-task selections publish variance math (Lonnie B#6: +-4 tasks/120). | **C5 (P)**, C1 | Jigsaw Seed-42 A#12; MAP 3-seed A#16; ISIC 5x10-seed t-test A#10 | `V6_REBUILD_PLAN.md:35` L6; `V6:340` variance envelope |
| 5 | **Wall-clock frontier figure (NEW Fig 11 companion, or add as Table 7-B)** — N=4/5/6 x FILL_FRAC x TOP300/450/600 vs public + wall-clock; TOP300 ceiling + TOP450/TOP600 craters as more-is-not-better proof (Santa-2024 perplexity-vs-compute B#4; Vesuvius 1024 at identical wall-clock B#9). | **C4 (P)**, C2 | Santa-2024 B#4; Vesuvius B#9; Hydrogen Pareto B#8 | `V6:474-479` Sec 9; `comp_data/kaggle_evaluation/.../jed_attack_gateway.py:62-63` 8750; `src/apex_attack/config.py:27-46` |
| 6 | **Guard on/off + payload-swap rows IN Table 7-A (not just appendix)** — clean-post ALLOW / web-tainted DENY / encoded-marker 0-raw / TOKEN wrong-payload as the narrowest mechanism proof (payload blind spot `optimal.py:51-58` stops at url). | **C3 (P)** | Malware 7-liner segment table A#21; Vesuvius depth-invariance B#9 | `comp_data/aicomp_sdk/guardrails/optimal.py:51-58`; `V6:143-149` |
| 7 | **Per-stage cascading metrics + gate-ablation** — race crown rate, fill keep rate (31%->100%), replay survival rate, per-stage deltas; no-race vs race, no-validate vs validate-then-keep (RSNA-Aneurysm recall-gate B#2; Vogel UMAP-gate). | C3, **C4** | RSNA-Aneurysm B#2; Vesuvius B#9; CommonLit loop B#20 | `V6:183-197` Sec 4.3-4.4; `src/apex_attack/search/race.py`; `search/fill.py` |
| 8 | **Pinning table (artifact / version / hash-or-date / where-used)** — SDK pin, gateway 2026-08-14, GGUF `c099eb4` 2026-07-17, fixture hashes, top-3 field notebook refs+versions (LLM-Science RAG pins A#15; ARC wheels+weights B#5; TalkingData JSON registry B#14). | **C4 (P)**, C1 | LLM-Science A#15; ARC-2024 B#5; TalkingData B#14 | `V6:548-566` Sources; `pyproject.toml:6`; `tools/local_test.py:28` |
| 9 | **Upstream-vs-fork diff table in Sec 11 (Konwinski pattern)** — base Agentless/Getting-Started 0.075 vs fork: what changed, why, validity-rate evidence (adaptation for 32B local models). 1 table, 6 rows max. | C1, C2 | Konwinski A#22 | `V6_REBUILD_PLAN.md:93` Sec 11 |
| 10 | **Minimal-solution control alive to end** — single-post without forge/halving as baseline 0; report what complexity added (RSNA-Brain "very simple code" B#3; Santa GA-vs-relaxation hierarchy). | C2 | RSNA-Brain B#3; Santa-2025 A#25 | `V6:400-413` family table |
| 11 | **Selector ablation (eff vs raw vs survivability-weighted)** — on held-out replay split, which ranking rule (eff=mean_raw/mean_cost vs max-raw vs hedge-aware) picks the private survivor. V6 starves deputy (16>4) — show it. | C2, C3, C4 | ARC stability-vs-likelihood B#5; MDC tool-assignment B#25 | `src/apex_attack/search/race.py`; `config.py:40-42` `ROLLING_TOP_RAW_FRAC` |
| 12 | **Hedge-fraction sweep with BOTH pub+priv numbers (label post-hoc INFERRED honestly)** — 10% vs 70% vs pure-deputy; aleaiest 29.73->29.67 vs 100.665->0.00 trap + takamichitoda 24.36 + hiranorm 0.00 controls (ASHRAE pub-priv per component B#16; LANL ignore-LB B#19). | **C4 (P)**, C5 | ASHRAE B#16; LANL B#19 | `V6:294-315` Table 5 + Sec 6.4 |
| 13 | **Failure close with rival credit + stop rule per family** — forge7/8 -11/-10, encoding 0-raw, TOKEN, rotation; each with isolated delta + diagnosis + `NEVER ...` / `PROMOTE ...` rule + credited notebook (forge 90.54 V15, JED-v25 89.145) (MCTS failures+missed+credit A#23; MDC 4-failures B#25; Titanic stop rule A#3). | **C5 (P)**, C2 | MCTS A#23; APTOS Zoo A#9; MDC B#25; Titanic A#3 | `V6:372-426` F1-F10/H1-H10 |
| 14 | **Figure reuse map + word budget discipline (11 figures max, 2500-5500 words narrative)** — Fig1 pipeline + Fig2 guardrail trace + Fig3 ablation bar + Fig4 progression + Fig11 distribution; every caption has one-sentence interpretation + alt text; deferred heatmaps stated explicitly (reviewer-respect signal). | C1, C5 | Santa gallery A#25 (visual proof); Gabruseva >8 bloat | `V6:75-77` Fig1/2 + `V6_REBUILD_PLAN.md:44` L8 |
| 15 | **Factory > story (numbered pipeline, exact bash 1-6, manifest, 30-s verify)** — `1 fetch -> 2 race -> 3 fill -> 4 bundle -> 5 local_test.py 5/5 PASS -> 6 submit`; `settings.json` + `entry_points` + `requirements` pinned; RAM/timeout notes (CommonLit Colab chain B#20; Feedback-ELL shell curriculum B#7; BirdCLEF configs B#12). | **C4 (P)**, C1 | CommonLit B#20; Feedback-ELL B#7; BirdCLEF B#12 | `V6:747-791` Sec 13; `tools/bundle.py:1-101`; `tools/local_test.py:1-434` |

**Why 15?** 1-3 are gate passes (integrity, hero table, self-test) — miss one and you are out regardless of insight. 4-8 are differentiator core (variance, frontier, mechanism rows, gates, pins) — they rank you. 9-12 are usefulness depth (diff table, minimal control, selector ablation, hedge sweep) — they make you forkable. 13-15 are responsible close + reviewer respect (failures+credit, figure/word discipline, factory) - they make you citable. Every action cites a winner that already won with it, so none is speculative.

---

## Appendix: 10x5 coverage check (rebuild plan Sec 2)

Primary (P) + supporting (s) per `research/V6_REBUILD_PLAN.md:60-71`. Counts after 15 actions:

| Lesson | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|
| L1 one ablation table | **P(2)** | s | s(6) | s | s(2) |
| L2 integrity front-load | s(1) | s | **P(1,6)** | s | **P(1,4,7,12)** |
| L3 story spine | **P(2)** | s(10) | s(6) | s(7) | s(3) |
| L4 pipeline figure first | **P(14)** | s | **P(3,6,7)** | s | s |
| L5 failure closing | s | **P(13)** | s | **P(13)** | **P(13)** |
| L6 variance disclosure | s(4) | **P(4)** | s | s | **P(4)** |
| L7 reproducibility factory | s(8,15) | s(15) | s | **P(8,12,15)** | s |
| L8 figure budget | **P(14)** | s | s | s | s |
| L9 chunked tables | **P(2)** | s | s | **P(15)** | s |
| L10 hook+TL;DR | **P** | s | s | s | s |

Coverage: every criterion has >=3 primaries after actions (C1: L1/L3/L4/L8/L9; C2: L5/L6; C3: L2/L4; C4: L5/L7/L9; C5: L2/L5/L6). No criterion carried by a single lesson — the `V6_REBUILD_PLAN.md:73` coverage invariant holds and is strengthened by actions 4,6,11.

*End — research/SCORING_RUBRIC_DEEP.md — 50 winners distilled to 5 criteria + 15 failures + hypothesis + 15 actions.*
