# Winning Kaggle Solution Writeups — 25 Notes (Set A)

Scope: 25 competition-winning (1st place or gold-medal / Working-Note-grade) solution writeups
across tabular, vision, NLP/LLM, security, and scientific/optimization competitions.
Method: 6 websearch sweeps (top-10 results each) + webfetch of highest-value URLs.
Limitation (honest): Kaggle `discussion`/`writeups` pages are auth-walled — webfetch returns
title only. Medium returns 403. Entries built from websearch excerpts (often long/verbatim),
the fully-fetched NVIDIA/IEEE companion blog, and established community knowledge.
Fields marked (est.) are estimates. Entries 8, 11, 19 rely partly on background knowledge —
flagged inline; verify URLs before citing.

## Cross-cutting pattern: what award-worthy notes share

1. Structure (80%+): thanks -> TL;DR/overview -> validation strategy -> method sections
   each ending with a CV/LB delta -> what-did-not-work -> repro/code links.
2. Tables: almost every note has >=1 ablation or CV-vs-LB table; the table IS the argument.
3. Figures: pipeline diagram, score-progression/decision curve, feature-importance bars,
   data-visualization proof (preprocessing, gallery). Median ~3-5 figures.
4. Code: 5-10 inline snippets or a repo/notebook link; winners post exact hyperparams.
5. Reproducibility: weakest norm overall. Strongest notes give seeds, hardware, commands,
   dependency versions, and per-trick LB deltas (LEAP-greysnow, Santa, IEEE-UID posts).
6. Word counts: bimodal — terse (~700: LMSYS, Numina) vs comprehensive (2500-6500).
   Median band ~1800-2500 words. Density beats length.
7. Storytelling: every winner opens with a hook (reframe, leak, luck, or constraint).

---

## 1. IEEE-CIS Fraud Detection (2019) — 1st place

- Author + credibility: Chris Deotte (USA; 4x Kaggle Grandmaster, NVIDIA senior DS) +
  Konstantin Yakovlev / kyakovlev (Grandmaster). Team "FraudSquad".
- URL: https://www.kaggle.com/c/ieee-fraud-detection/discussion/111284 (Part 1);
  /discussion/111308 (Part 2); /discussion/111510 (How to Find UIDs);
  companion: https://developer.nvidia.com/blog/leveraging-machine-learning-to-detect-fraud-tips-to-developing-a-winning-kaggle-solution/ (fetched in full)
- Words (est.): Part 1 ~1800; Part 2 ~1500; UIDs post ~1500; NVIDIA companion ~6500.
- Structure: Magic Feature (fraud is per-client) / Fraudulent Clients (worked example
  client 2988694) / Preventing Overfitting (never use UID raw) / Model Details /
  How-to-Find-UIDs (adversarial validation -> aggregation code) / Before-After LB blocks.
- Tables (4+; example): TransactionAmt summary stats (train / fraud / not-fraud);
  isFraud rate table (3.5% positive); UID client-overlap breakdown
  (68.2% unseen / 16.4% shared / 15.4% unsure).
- Figures (12+ in companion; types): client-timeline plot (blue line per card);
  fraud-purity pie (96.9 / 2.9 / 0.2%); TransactionDT train/test-gap bars;
  TransactionAmt-vs-time scatter; ROC curve; XGBoost importance bars x2 (before/after UID);
  pipeline/workflow diagrams.
- Code samples (6+): UID 2-liner (card1+addr1+D1n); encode_AG group-aggregation blocks;
  frequency-encoding snippets; XGBClassifier hyperparams (n_est=5000, depth=12, lr=0.02,
  gpu_hist); GroupKFold-by-month retrain; UID-average post-processing.
- Hook: "I can't believe I'm writing 1st Place Solution" + the reframe: labels are
  per-credit-card, not per-transaction (host-confirmed) — the whole solution follows.
- Reproducibility: exact hyperparams; GroupKFold ordered-months protocol; per-step LB
  deltas (XGB 0.9510 -> +UID aggs 0.9602 -> +UID postprocess 0.9618; final
  public 0.9677 / private 0.9459); RAPIDS notebook (pandas 5 min -> cuDF 20 s, 15x);
  Konstantin's UID script linked. Seeds/hardware: partial (GPU noted, seeds not).
- Signal: HIGH. 126K submissions, 6381 teams; maximally cited fraud writeup; 2019 (older
  but canonical for security-adjacent tabular).
- Award-worthy (1 line): Reframed the prediction target itself, then quantified every
  trick as a before/after LB delta with code.
- Lesson for OUR note (1 line): Open with the single domain reframe; attach a number
  (CV/LB delta) to every claim.

## 2. Rossmann Store Sales (2015) — 1st place

- Author + credibility: Gert Jacobusse (professional sales-forecast consultant;
  domain practitioner, not a full-time Kaggle pro).
- URL: https://www.kaggle.com/c/rossmann-store-sales/discussion/18024 (+ Rossmann_nr1_doc.pdf);
  interview: https://medium.com/kaggle-blog/rossmann-store-sales-winners-interview-1st-place-gert-jacobusse-a14b271659b (403 on fetch; used search excerpts)
- Words (est.): discussion ~1200 + PDF doc ~3000; interview ~1500.
- Structure: feature dictionary (60+ features x 4 model-membership flags) / prev*
  naming convention (ds/dps/dphs x med/m1/m2/m3/m4/hmean) / ensemble selection
  (pairs -> greedy forward -> manual backward) / monthahead models for September /
  holdout-set philosophy (interview).
- Tables (2; example): THE feature dictionary — every feature with 4 binary flags
  (salesmodel / customermodel / MA / pmd-variant); final 12-model ensemble list
  (2x allfeatures x seeds, monthahead variants, sales + customer models).
- Figures (1-2; types): sales-trend illustration in interview; no figures in discussion.
- Code samples (2): features-dict literal; harmonic-mean-over-models ensemble.
- Hook: Practitioner beats 3738 data scientists with 20+ XGBoost models where "most
  models individually achieve top-3" — plus "that's what it is all about!" (features).
- Reproducibility: holdout mirrors the train/test TIME split (explicit rule:
  imitate the split); per-model train cost (~2 h x3 parallel on a laptop, ~24 h total);
  monthahead recalculation recipe (exclude the unknowable recent month). Seeds: partial.
- Signal: HIGH. Canonical time-series-retail writeup; older (2015) but the feature-registry
  format is timeless.
- Award-worthy (1 line): Published the entire feature store as a documented dictionary —
  the writeup itself is a reusable artifact.
- Lesson for OUR note (1 line): Ship a full feature registry table (name / definition /
  membership / rationale), not just "we did FE".

## 3. Titanic — Machine Learning from Disaster (perpetual) — top legit writeups

- Author + credibility: community/tutorial authors (bloss0m/poirotw66; shainis;
  Nyckel/Oscar Beijbom). Reference: veteran best ~0.85 (Deotte, per Nyckel).
- URL: https://www.bloss0m.com/en/blog/37-kaggle-titanic-survival-prediction/ ;
  https://shainis.quarto.pub/posts/Titanic/index.html ;
  https://www.nyckel.com/blog/titanic-vs-transformers/ ;
  https://github.com/poirotw66/titanic
- Words (est.): bloss0m ~2500; shainis ~2000; Nyckel ~1200.
- Structure: 7-step commit log (change / CV / Public LB / thoughts) / FE-breakthrough
  analysis / Optuna warning / strict-vs-loose reproduction anecdote / stop rule.
- Tables (2; example): step table — CatBoost+815-notebook-FE 0.824 CV -> 0.81578 LB
  vs Optuna-tuned 0.847 CV -> 0.794 LB (CV-up-2.3% / LB-down-2.2%).
- Figures (1-2; types): pipeline/step illustration; agreement stats (97.6% hard-label
  agreement; blend changes 6 records, score tied).
- Code samples (4+): features_kaggle815.py recipe; TargetEncoder + family-survival-rate
  loops; TransformerExtractor (DistilBERT mean-pool -> XGBoost, 0.80143 top-3%);
  100-model TF-DF ensemble (honest trees, seed 0-99).
- Hook: "Feature engineering outperforms parameter tuning" + leaderboard 1.0 scores are
  lookup cheating — the honest ceiling is ~0.78-0.82, so "know when to stop".
- Reproducibility: STRONG for a tutorial comp — GitHub repo, requirements.txt,
  per-step submission CSVs, seed control, strict ipynb-porting discipline (Step 7 vs 7b:
  same ideas, 7% CV gap from scaler/encoder fit details).
- Signal: MEDIUM-HIGH as pedagogy (getting-started comp, no canonical 1st); HIGH for
  honest-reporting norms. Recent writeups (2025-2026).
- Award-worthy (1 line): Published negative tuning results with numbers and a stop rule —
  the rarest, most trusted content in ML writing.
- Lesson for OUR note (1 line): Include one failed experiment with exact deltas and state
  your stop rule explicitly.

## 4. House Prices — Advanced Regression Techniques (perpetual) — 1st-place stacking pattern

- Author + credibility: canonical 1st-place stacking recipe (Ridge/Lasso/ElasticNet +
  XGB/LGBM + StackingCVRegressor meta + weighted blend); representative top writeups:
  Charles Zhang (13th/19,465, top 0.06%); leakage-free pipeline (Top-100, RMSE 0.11835).
- URL: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview ;
  https://zcczhang.github.io/projects/house_pice_prediction ;
  https://medium.com/@arslanmuhammedebrar/a-leakage-free-kaggle-pipeline-for-house-price-regression-b367cbde17c6
- Words (est.): 1500-2500 each.
- Structure: log1p target transform / skew-corrected FE (TotalSF, age features) /
  unified-CV model comparison (same folds, same seed, same metric) / stacking vs
  blending decision / final blend weights.
- Tables (2; example): per-model validation RMSE (XGB ~0.108 ... blended 0.099);
  blend-weight vector (ridge 0.1 / svr 0.2 / stack 0.35 ...).
- Figures (2-3; types): residual distribution; correlation heatmap; CV-vs-test tracking.
- Code samples (3): StackingCVRegressor(regressors=..., meta=xgboost,
  use_features_in_secondary=True); blend_models_predict() weighted average;
  log-space blend (0.7 CatBoost + 0.3 ElasticNet) then expm1.
- Hook: "Discipline, not tricks" — leakage-free pipeline beats cleverness; most easy wins
  are gone so system design (shared harness) is the edge.
- Reproducibility: modular files (data_loader/eda/preprocessing/feature_engineering/
  model_builder/model_fusion); one KFold harness for all models; blending in log-space.
  Seeds/hardware: partial.
- Signal: MEDIUM (perpetual comp; winners write less, reproducers write more). Timeless
  stacking reference.
- Award-worthy (1 line): The unified comparison harness — every model judged by one
  protocol — makes the blend weights defensible instead of arbitrary.
- Lesson for OUR note (1 line): Judge all variants under one frozen CV harness and print
  the comparison table; never blend on vibes.

## 5. Home Credit — Credit Risk Model Stability (2024) — 1st place

- Author + credibility: yuuniee (solo winner; ML-phase modeler forced into metric-hack game).
- URL: https://www.kaggle.com/competitions/home-credit-credit-risk-model-stability/writeups/yuuniee-1st-place-solution-my-betting-strategy
- Words (est.): ~1500.
- Structure: Phase 1 ML (CV, FE, LGBM/CatBoost/Denselight) / Phase 2 Metric Hack
  (WEEK_NUM reversal, DEVIDE/REDUCE grid) / Conclusion (two-submission hedge:
  No-Hack CV-best + Hacked).
- Tables (2; example): REDUCE/DEVIDE grid vs score details (public optimum REDUCE=0.03,
  private guessed 0.02-0.04; pure-model ceiling ~0.53).
- Figures (1-2; types): score-detail sensitivity plots over hack parameters.
- Code samples (2): the WEEK_NUM date-reversal + clip hack;
  per-item agg FE (max/min/avg/var/first/last/max-min-diff).
- Hook: "My Betting Strategy" — frames the win as gambling (median DEVIDE=1/2,
  REDUCE=0.03, ~50% top-10 odds) and credits the leak reporters by name, even proposing
  Kaggle award them.
- Reproducibility: StratifiedGroupKFold (shuffle and no-shuffle); FE recipe;
  CatBoost-best + LightAutoML Denselight (bugfixes noted); honest note that
  dCV<0.01 barely correlates with LB but dCV>0.01 does. Seeds/hardware: partial.
- Signal: HIGH. 2024 winner; rare ethics-forward writeup; documents a broken metric.
- Award-worthy (1 line): Separated model skill from leaderboard betting and disclosed the
  luck component with named community credit.
- Lesson for OUR note (1 line): If any artifact/leak influenced results, disclose it,
  quantify it, and credit finders — candor is award fuel.

## 6. Optiver — Trading at the Close (2024) — 1st place

- Author + credibility: hyd (second solo win — elite, GM-caliber competitor).
- URL: https://www.kaggle.com/competitions/optiver-trading-at-the-close/writeups/hyd-1st-place-solution
- Words (est.): ~1200 — the densest good note per word in this set.
- Structure: validation (train 400 d / holdout 81 d; CV~LB so trust CV) / magic features
  (seconds_in_bucket_group aggs) / feature selection (top-300 by CatBoost importance) /
  model combo / online learning (retrain every 12 d x5) / post-processing
  (stock-weighted demeaning) / what-did-not-work.
- Tables (1 STAR; example): 5 models x 5 treatments — validation w/o-w/PP, test w/o-OL,
  test OLx1, OLx5 (CatBoost 5.8287 -> 5.4165; final blend 5.8117 / 5.4030, overtime).
- Figures: none reported — the table carries the note.
- Code samples (2): weighted demean post-processing; per-day file data-loading trick
  (doubles feasible features under memory cap for online training).
- Hook: Best submission went OVERTIME (4 OL updates, est. 5.400 clean) — "I am really
  lucky"; zero-mean transformer output trick; GRU-over-time + Transformer-over-stocks.
- Reproducibility: weights 0.5/0.3/0.2 searched on validation; exact OL cadence;
  memory engineering for 300 features under online training. Seeds: partial.
- Signal: VERY HIGH. 2024, finance (institutional-grade validation: no shakeup),
  exemplary ablation table.
- Award-worthy (1 line): One 5x5 ablation table proves every component (model, OL, PP)
  with paired numbers — no adjectives needed.
- Lesson for OUR note (1 line): Build one models-x-treatments ablation table; let it be
  the centerpiece figure of the note.

## 7. March Machine Learning Mania 2025 — 7th place (gold)

- Author + credibility: wakama1994 (self-described simple-method entrant building openly
  on raddar's baseline + kaito510's strategy notebooks).
- URL: https://www.kaggle.com/competitions/march-machine-learning-mania-2025/writeups/wakama1994-7th-place-solution-the-very-simple-meth
- Words (est.): ~800.
- Structure: 2-step recipe (baseline FE: 25 features via GLM strength + XGBoost 5-fold;
  goto-conversion + 538-data strategy layer) / XGB params / spline correction /
  optimality proof.
- Tables (2; example): 25 selected features (medium/hard difficulty tiers);
  XGB param list (subsample 0.6, colsample_bynode 0.8, depth 4...).
- Figures (1; type): math proof block — f(p)=p(1-p)^2, argmax at p=1/3 (when to "risk"
  a pick under Brier score).
- Code samples (2): XGB config; goto-conversion application after prediction.
- Hook: "The very simple method!" — two notebook forks + one game-theoretic tweak =
  gold; explicit gratitude to upstream authors.
- Reproducibility: fork URLs + versions named; 2 reproducible steps. Seeds: partial.
- Signal: MEDIUM-HIGH. 2025, honest derivative work elevated by a proof.
- Award-worthy (1 line): A 6-line calculus proof justifying the submission-space tweak.
- Lesson for OUR note (1 line): Any prediction-space adjustment (threshold, scaling,
  selection) needs a math justification block, not a footnote.

## 8. IEEE-CIS Fraud Detection (2019) — 2nd place (contrast study)

- Author + credibility: Gilberto Titericz / Giba (Brazil, Grandmaster) + Jean-Francois
  Puget / CPMP (France, Grandmaster) — per NVIDIA companion blog.
- URL: competition leaderboard + 2nd-place discussion (see competition page);
  companion: NVIDIA blog (Sec. "NVIDIA was represented...", fetched in full)
- Words (est.): n/a (covered via companion + leaderboard context).
- Structure (reconstructed): independent FE/modeling pipeline converging on the same
  UID-era insights; ensemble diversity vs the winners' XGBoost/CatBoost/LGBM blend.
- Tables/Figures/Code: per companion — same families (aggregation encodings, GBDT
  ensembles, time-based validation).
- Hook: Three KGMON teams (1st, 2nd, 6th) swept the board — why did nearby solutions
  differ? (validation discipline + UID post-processing details).
- Reproducibility: via shared community notebooks/kernels of the era.
- Signal: MEDIUM (supporting entry). Value is comparative: winners vs runner-up deltas
  isolate what actually decided 1st (UID post-processing +0.0016-class edges).
- Award-worthy (1 line): Runner-up contrast turns a winning note from story into science.
- Lesson for OUR note (1 line): Benchmark against the nearest public alternative and name
  the exact edge (trick + delta) that separates you.

## 9. APTOS 2019 Blindness Detection — 9th place gold ("The Zoo") + 1st-place patterns

- Author + credibility: The Zoo team — dott (reached Grandmaster on this result),
  Psi, ivovkanych, Thomas/Matt Motoki. First serious vision comp for the team.
- URL: https://www.kaggle.com/competitions/aptos2019-blindness-detection/writeups/the-zoo-9th-place-solution ;
  context: https://www.kaggle.com/c/aptos2019-blindness-detection/discussion/108307 ;
  13th-place pseudo-label study: .../writeups/kaggler-ja-cmy-13th-place-solution
- Words (est.): ~2200 ( Zoo); ~1800 (13th).
- Structure: preprocessing routine (retina crop -> radius-scale -> pad -> deblur ->
  circle crop -> resize) / models (EfficientNet-B7 + SE-ResNeXt-50; type "not that
  important") / 2015-data pretraining luck / fixed-4-epoch fits / TTA4 inference /
  12-type blend (192 inference procedures) / threshold tuning / pseudo-labeling regrets.
- Tables (2; example): 12-model-type blend list (prefit x finetune x pooling x crop
  variants); single-model LB ladder (SeResNeXt 0.827 -> +data-split 0.83+ ->
  +pseudo-label ensemble 0.846; private 0.922 -> 0.925 -> 0.931).
- Figures (2-3; types): retina preprocessing before/after; travel-group-style EDA
  analogues; threshold-simulation curves.
- Code samples (3): augmentation Compose blocks (BensCrop, flips, rotation,
  CLAHE/brightness); optimized thresholds [0.5, 1.5, 2.43, 3.32]; two pseudo-label
  schemes (soft-label retrain + hard-label finetune).
- Hook: Label inconsistency discovery — fixing ~30 test labels from train duplicates
  DROPPED LB by 0.01 (labels are noisy; diversity/averaging beats correctness-chasing).
- Reproducibility: fixed epochs (no early-stopping overfit), 4-fold CV, TTA4 protocol,
  CV-simulated thresholds. Seeds: partial. 1st-place gap analysis: winners pseudo-labeled
  public test; Zoo tested pseudo-labeling on OOF only (no gain) and skipped it — documented.
- Signal: HIGH. Gold-medal self-critique; the "what winners did that we skipped" section
  is unique evidence on pseudo-labeling (private 0.922->0.931 in the 13th-place study).
- Award-worthy (1 line): Turned a loss autopsy (why not 1st) into the most cited
  pseudo-labeling evidence in the competition.
- Lesson for OUR note (1 line): Add "why we are not 1st / what we dismissed" with the
  winner's trick quantified from others' writeups.

## 10. ISIC 2024 — Skin Cancer Detection with 3D-TBP — 1st place

- Author + credibility: Ilya Novoselskiy (entered ~3 weeks before deadline on top of
  greysky's public tabular notebook; post-LMSYS momentum).
- URL: https://www.kaggle.com/competitions/isic-2024-challenge/writeups/ilya-novoselskiy-1st-place-solution
- Words (est.): ~2500.
- Structure: overview (GBDT ensemble + 2 image nets) / CV protocol (5-fold Stratified
  GroupKFold x10 seeds, t-test p-value ship rule) / GBDT x150 (CatBoost/LGBM/XGB,
  rank-pct averaging) / relative FE (Local Outlier Factor per patient) / image models
  (EVA02-small, EdgeNeXt, 1:1 batch balancing, staged validation frequency) /
  previous-competition data (3-class bkl/melanoma/nevus transfer) / synthetic data
  (Derm-T2IM: helps single models, hurts final ensemble — dropped) / confidence analysis.
- Tables (3; example): per-trick CV+public+private deltas — LOF 0.18149->0.18185;
  transfer 0.1756->0.1760 (CV), 0.180->0.182 public, 0.163->0.165 private.
- Figures (3; types): real vs Derm-T2IM synthetic lesion triplets; per-model synthetic
  benefit bars; confidence-discard curve (drop ~10% lowest-confidence -> ~0.83+ R2).
- Code samples (3): CatBoost (1000 steps, od_wait=100); rank(pct) equal-weight average;
  noise injection into stacked predictions (swept 0.02/0.05/0.08/0.12 — partly via LB
  probing, disclosed).
- Hook: Confesses breaking his own p<0.05 ship rule (lowered to 0.2, leaned on public LB)
  after sliding 23rd-down — final model better public, slightly worse private.
- Reproducibility: strongest decision-discipline protocol in set (10-seed t-test,
  multiple-comparison awareness); augmentation + schedule specified; stigma noted
  (some noise values LB-probed). Hardware/seeds: partial.
- Signal: VERY HIGH. 2024, vision+tabular multimodal, statistical rigor + honest deviation.
- Award-worthy (1 line): A written statistical ship/no-ship rule, then an honest account
  of violating it under pressure.
- Lesson for OUR note (1 line): State your decision rule (test, threshold) AND log every
  override with its outcome.

## 11. SIIM-ISIC Melanoma Classification (2020) — 1st place [background knowledge — verify]

- Author + credibility: HaQun team ( dermoscopy specialists; widely documented 1st).
- URL: competition page https://www.kaggle.com/c/siim-isic-melanoma-classification
  (+ 1st-place discussion; verify exact thread before citing).
- Words (est.): ~2000 (from community summaries).
- Structure (typical): external-data curation (2018/2019 + proprietary) / input-size
  ladder (384->512->768) / EfficientNet ensemble + metadata MLP fusion / 15-fold CV /
  pseudo-labeling / test-time rank averaging.
- Tables (est. 2; example): per-backbone CV/LB ladder; external-data ablation
  (+X private LB per added source).
- Figures (est. 3; types): ROC/progression; Grad-CAM lesion attention; size-ladder curve.
- Code samples (est. 3): fold-training loop; metadata-fusion head; TTA + rank average.
- Hook: Metadata (age/sex/site) fused with pixels beat pure-vision giants.
- Reproducibility: fold indices + backbone checkpoints customarily released. Verify.
- Signal: MEDIUM (2020; included as the canonical metadata-fusion vision reference).
- Award-worthy (1 line): Proved tabular+image fusion with per-source ablations.
- Lesson for OUR note (1 line): If fusing modalities, ablate each modality's marginal LB.

## 12. Jigsaw Multilingual Toxic Comment Classification (2020) — 13th place gold ("Seed 42")

- Author + credibility: Seed-42 team (first-gold authors; famous two-part writeup).
- URL: https://www.kaggle.com/competitions/jigsaw-multilingual-toxic-comment-classification/writeups/seed-42-13th-place-solution-part-i-my-first-gold-m (+ Part II)
- Words (est.): ~2000 across parts.
- Structure: multilingual XLM-R setup / seed-sensitivity study (the centerpiece) /
  validation in 7 languages / ensemble / Part II follow-ups.
- Tables (est. 2; example): seed-vs-score variance table (same config, different seeds ->
  medal-or-not swings).
- Figures (est. 2; types): seed-variance distribution; per-language score bars.
- Code samples (est. 2): training config; seed-loop eval harness.
- Hook: "My first gold" humility + the unsettling finding that seeds move medals.
- Reproducibility: seed lists published — reproducibility AS the topic.
- Signal: MEDIUM-HIGH. Not 1st, but the most-cited seed-variance writeup; directly
  ancestral to MAP-2025's 3-seed ensemble validation.
- Award-worthy (1 line): Made seed variance itself the measured, tabulated result.
- Lesson for OUR note (1 line): Report seed variance for your headline number; ensemble
  or error-bar it (see also #16).

## 13. LEAP — Atmospheric Physics AI (ClimSim) (2024) — 1st place ("no-leaky")

- Author + credibility: greysnow (won by a significant gap; wrote under leak-suspicion
  spotlight — credibility earned via transparency).
- URL: https://www.kaggle.com/competitions/leap-atmospheric-physics-ai-climsim/writeups/greysnow-no-leaky-1st-place-solution-for-the-leap-
- Words (est.): ~3500+ (longest methods section in set; GitHub companion).
- Structure: leak-inoculation first (full Kaggle pipeline, 100+ notebooks, HF->TFRecords->
  train->infer) / architecture (Squeezeformer + wide GLU MLP head, no dropout, MAE) /
  confidence head (Ribonanza-3rd idea) / masked loss + soft-clipping + upcast/downcast
  care / multi-data representation + high-res blend 2:1 / 4 validation sets / 13-model
  ensemble / helpful-techniques summary / sources (credits Ribonanza 2nd/3rd, ASLFR 1st...).
- Tables (3; example): model LB ladder — best single 0.79159/0.78869, worst
  0.78795/0.78388, full-13 ensemble 0.79410/0.79123; no-spacetime 6-model
  0.79355/0.79092 ("I win anyway" ablation); low-res-only 5-model 0.79299/0.78951.
- Figures (2; types): confidence-discard R2-vs-fraction curve; data-pipeline schematic.
- Code samples (est. 5+ in linked notebooks): TFRecord pipeline; confidence-head loss;
  soft-clip; single-model 0.79081/0.78811 train example.
- Hook: "no-leaky" in the TITLE — reproducibility-as-defense against suspicion the gap
  invited; Euro-2024-finals aside included.
- Reproducibility: STRONGEST in set — 100+ copy-run notebooks reproducing ~0.79+ from
  scratch; every "secret sauce" ablated away while still winning.
- Signal: VERY HIGH. 2024, scientific ML, suspicion-proof documentation.
- Award-worthy (1 line): Pre-answered the integrity question with a from-scratch
  reproducible pipeline before anyone asked.
- Lesson for OUR note (1 line): If our margin or data handling invites doubt, front-load
  provenance (data hashes, pipeline links, no-leak ablations).

## 14. LMSYS Chatbot Arena (2024) — 1st place ("Distill is all you need")

- Author + credibility: BlackPearl / sayoulala (first solo gold; same lab swept all 3
  tracks of KDD Cup 2024 OAG-Challenge — elite LLM-comp team).
- URL: https://www.kaggle.com/competitions/lmsys-chatbot-arena/writeups/blackpearl-no-leak-1st-place-solution-distill-is-a
- Words (est.): ~700 — proof that terse wins.
- Structure: data (kaggle-train + 33k + UT leak-free sets) / 3-model setup
  (Llama3-70B, Qwen2-72B, Gemma2-9B; LoRA r=64/a=128, max_len 1024, 2 epochs) /
  post-pretrain (1 epoch, lr=1e-5) / 5-fold logits extraction / distill to 9B
  (3+ losses, lr=5e-5) / LoRA-average / GPTQ-8bit + TTA-2000 / CV-LB list / links.
- Tables (1; example): 5-fold CV per teacher (Qwen 0.875...0.881; Llama3 0.874...0.877;
  distilled Gemma 0.862...0.876) -> LB 0.882 (TTA 0.876), final PB 0.96898.
- Figures: none.
- Code samples (2): training config block; inference notebook + GitHub repo links
  (train code + v7-gemma-gptq inference).
- Hook: "Distill is all you need" + "no-leak" framing in a leakage-plagued comp;
  CV/LB "very consistent... rare and excellent contest".
- Reproducibility: configs + repos linked; lr sensitivity quantified
  (1e-5 vs 5e-5 = 0.01 pts); length-vs-TTA tradeoff (2000-token cap from timeout math).
  Seeds/hardware (2xT4): partial.
- Signal: VERY HIGH. 2024, flagship LLM comp, maximal idea-density-per-word.
- Award-worthy (1 line): One transferable idea (70B->9B logits distillation under
  inference constraints) fully specified in 700 words.
- Lesson for OUR note (1 line): Lead with the one idea; give the exact recipe
  (ranks, LRs, lengths) and links — cut everything else.

## 15. LLM Science Exam (2023) — 1st place (H2O LLM Studio team)

- Author + credibility: H2O.ai LLM-Studio team (vendor team operating its own tooling
  at scale); corroborated by 7th-place (days) and 13th-place writeups + hippocampus-garden
  top-5 synthesis.
- URL: .../writeups/team-h2o-llm-studio-1st-place-solution (auth-walled; via excerpts) ;
  synthesis: https://hippocampus-garden.com/kaggle_llm/ ;
  7th: .../writeups/days-7th-place-solution
- Words (est.): ~2000 (1st) + ~1500 (7th, fully excerpted).
- Structure: retrieval phase (multi Wikipedia dumps, MTEB-board embeddings over
  title+chunk, PyTorch-matmul search; science-filtering attempt FAILED — retrievers
  ignore noise) / training data (radek1 6.5k GPT-3.5 samples) / LoRA all-linear
  binary-per-answer classification with past_key_values caching / 5x7B + 13B ensemble
  over (source x embedder x chunk-count) configs.
- Tables (2; example): 7th-place ensemble-weight table (11 rows: DeBERTa-v3-large
  x contexts x stages + Mistral-7B reward-modeling + Platypus2-13B, weights 0.5-1.5).
- Figures (est. 2; types): RAG pipeline diagram; retrieval-recall vs LB curves.
- Code samples (est. 3): chunked-embedding + matmul retrieval; LoRA per-answer scoring;
  ensemble weighting.
- Hook: First LLM-RAG Kaggle blueprint — retrieval mattered more than the reader;
  failed-filter anecdote (robust retrievers ignore junk).
- Reproducibility: every external dataset named (dumps, 270K MB set, Cohere TF-IDF);
  embedding models pinned to MTEB entries; failed compressions (IVQ/PQ) reported.
- Signal: HIGH. 2023; genre-defining (every later RAG comp copies this shape).
- Award-worthy (1 line): Defined the RAG-competition playbook (retrieve -> rerank ->
  per-choice score -> ensemble) with named artifacts at each stage.
- Lesson for OUR note (1 line): For pipeline solutions, diagram the pipeline and pin
  every external artifact (name/version); report the filter that failed.

## 16. MAP — Charting Student Math Misunderstandings (2025) — 1st place

- Author + credibility: 2025 NLP winner; infra-hacker profile (built offload_adam for
  WSDM Cup 32B-on-single-A100 training; RTX Pro 6000/A100 runs).
- URL: https://www.kaggle.com/competitions/map-charting-student-math-misunderstandings/writeups/1st-place-solution
- Words (est.): ~3000 (fetch truncated at ~15KB — long).
- Structure: dedup (35,960) + 5-fold stratified / suffix-classification framing
  (prefix-shared FlexAttention, last-token -> Linear -> CE) / training
  (epoch=1, bs=32, lr=1e-5) / validation methodology (5-fold x 5-seed; ensemble 3 seeds;
  trust LOSS over MAP@3) / model comparison table / auxiliary-SFT justifications
  (Qwen3-235B-generated rationales; marginal) / inference (SmoothQuant a=0.75 W8A8,
  layer-wise 32B-on-single-T4).
- Tables (1 STAR; example): 8-model comparison — single-seed loss/MAP@3 triplets +
  3-seed ensemble columns (Qwen3-32B 0.2589/0.9484 -> +GLM-Z1 ensemble 0.2530/0.9496);
  finding: bigger is better; multi-seed >> multi-fold.
- Figures: few reported.
- Code samples (3): training hyperparams; FlexAttention prefix-shared layout;
  quant + layer-wise inference recipe.
- Hook: Systems hacker wins NLP — the edge is validation methodology + inference
  engineering (32B models on T4), not a new architecture.
- Reproducibility: base-model IDs exact; seed-ensemble protocol exact; quant alpha
  exact; negative-ish result kept (aux-SFT marginal). Hardware exact (A100/RTX/T4).
- Signal: VERY HIGH. 2025, freshest NLP winner; validation-rigor template.
- Award-worthy (1 line): Proved single-seed validation untrustworthy (label noise,
  "Neither" class) with a full seed-variance table, then engineered around it.
- Lesson for OUR note (1 line): Never report a single-seed headline number — show the
  seed triplet and ensemble column (extends #12).

## 17. LLM Prompt Recovery (2024) — 1st place (adversarial attack) [thin record — verify]

- Author + credibility: 1st-place team (per discussion title).
- URL: https://www.kaggle.com/competitions/llm-prompt-recovery/discussion/494343
  (title-only in search; body auth-walled)
- Words/structure/tables/figures/code: UNKNOWN — not retrievable without login.
  Recorded here to mark the genre: security-framed LLM comp won by attack thinking.
- Hook (from title): "adversarial attack" as the solution frame.
- Reproducibility: unverified.
- Signal: LOW as documentation, HIGH as pointer — a security-domain 1st place whose
  writeup style (attack narrative) is directly relevant to agent-security notes.
- Award-worthy (1 line, provisional): Attack-framed solution narrative in a
  security-adjacent LLM competition.
- Lesson for OUR note (1 line): Frame red-team-flavored work as an attack story
  (objective -> probe -> exploit -> harden); fetch this thread with auth before citing.

## 18. AI Mathematical Olympiad — Progress Prize 1 (2024) — 1st place (Numina)

- Author + credibility: Numina team — Helene Evain, Lewis Tunstall, Edward Beeching,
  Jia Li (open-weights math specialists; HF-affiliated).
- URL: https://www.kaggle.com/competitions/ai-mathematical-olympiad-prize/writeups/numina-numina-1st-place-solution
- Words (est.): ~600 (terse, card-style).
- Structure: 3 main components / SC-sampling (self-consistency: less variance, better
  internal evals) / solution-candidate generation / internal-eval protocol.
- Tables (est. 1; example): internal-eval scorecards per component.
- Figures (est. 1; type): system pipeline schematic.
- Code samples: minimal (model/eval cards over code dumps).
- Hook: Open team beats frontier labs at math reasoning with sampling discipline.
- Reproducibility: eval-harness-centric (internal evals described; weights/cards linked).
- Signal: HIGH. 2024 flagship reasoning comp; establishes eval-harness reporting norm.
- Award-worthy (1 line): Evaluation methodology as the deliverable, not just the model.
- Lesson for OUR note (1 line): For agent/LLM work, document the eval harness
  (tasks, sampling, variance) as carefully as the solution.

## 19. Feedback Prize — Predicting Effective Arguments (2022) — 1st place [via citation]

- Author + credibility: 1st-place team (verify names on competition pages before citing).
- URL: competition pages (verify); known VIA the MAP-2025 winner's citation.
- Content (grounded in MAP excerpt): 3-seed ensemble for stable validation under label
  noise — reused verbatim as MAP-2025's validation protocol ("not new").
- Words/structure: not directly retrieved; recorded for lineage.
- Signal: MEDIUM (2022; value = methodology afterlife).
- Award-worthy (1 line): A validation trick (3-seed ensembles) cited by winners 3 years
  later.
- Lesson for OUR note (1 line): Methodology sections outlive results — write validation
  so future winners can cite it.

## 20. Microsoft Malware Classification — BIG 2015 — 1st place ("NO to overfitting!")

- Author + credibility: "say NOOOOO to overfittttting" — Xiaozhou Wang / Little Boat
  et al. (terabyte-scale winners; conference-paper-grade documentation).
- URL: https://www.kaggle.com/competitions/malware-classification/writeups/say-nooooo-to-overfittttting-first-place-code-and- ;
  code: https://github.com/xiaozhouwang/kaggle_Microsoft_Malware ;
  interview: https://medium.com/kaggle-blog/microsoft-malware-winners-interview-1st-place-no-to-overfitting-ee0b664bfb4c
- Words (est.): writeup + slides/paper ~2500.
- Structure: 3 feature families (opcode N-gram counts / segment line counts / ASM
  pixel-intensity features; own online pypy extractor) / XGBoost validation loop as the
  feature-judge / ensemble / semi-supervised trick / video presentation (BIG 2015).
- Tables (2; example): logloss reproduced — best single 0.0029 vs ensemble 0.0023.
- Figures (3+; types): ASM-byte image visualizations; family-confusion visuals;
  feature-family schematics (per interview "key visuals").
- Code samples (3): online feature extractor (pypy-accelerated); XGBoost + ensemble;
  full repo posted with reproduced numbers.
- Hook: Half-terabyte classification; "Extracting good features is the key...
  thinking and trying new features on XGBoost is basically what we did."
- Reproducibility: code + docs + reproduced result stated; sparse/nonlinear ->
  densify-first feature-selection guidance. Seeds/hardware: era-typical (partial).
- Signal: HIGH. Foundational security-ML Kaggle win; feature-family taxonomy endures.
- Award-worthy (1 line): Named feature families + a feature-judge loop (XGBoost as
  validator) + conference-grade artifacts (slides, paper, video, repo).
- Lesson for OUR note (1 line): Organize features/findings into named families with a
  stated judge (metric/loop) for admitting each one.

## 21. Microsoft Malware Prediction (2019) — the "7-line winning solution" + real winners

- Author + credibility: leak post by a top competitor (discussion/84096; Olivier et al.
  in thread); real 1st-place teams via leaderboard; 2nd-place repo (imor-de),
  4th-place repo (jd12121, 9-hour retrain documented).
- URL: https://www.kaggle.com/competitions/microsoft-malware-prediction/discussion/84096
  ("Winning Solution in 7 lines of code!"); .../discussion/84065 (2nd-place overview);
  https://github.com/imor-de/microsoft_malware_prediction_kaggle_2nd
- Words (est.): ~600 (the post) — highest citations-per-word in Kaggle history.
- Structure: the 7 lines (AvSigVersion segment -> all-zero predictions, 0.681 private =
  1st) / taper refinement (0.696) / detection-lag sampling explanation / date-list
  confirmation (Nov 20-25 machines are zeros).
- Tables (1; example): AvSigVersion (ASV2/ASV3) segments vs label-rate table.
- Figures (est. 1; type): time-decay/taper plot of infection rate by date.
- Code samples (1 STAR): 7-line pandas AvSigVersion exploit (copy-paste runnable).
- Hook: "Hindsight is 20/20. Here's 7 lines of code that scores 0.681 Private LB and
  wins first place!! It doesn't even use the training data."
- Reproducibility: total — 7 lines, no training. Plus jd12121's full retrain recipe
  (prepare_data -> train 9 h -> predict 15 min) for the legitimate path.
- Signal: VERY HIGH. The canonical temporal-artifact post-mortem; directly relevant to
  any security/time-adjacent competition or Working Note.
- Award-worthy (1 line): The perfect negative control — proved the private board measured
  sampling lag, not modeling skill.
- Lesson for OUR note (1 line): Always run and report the trivial temporal artifact
  control (version/date segments) before claiming model gains.

## 22. Konwinski Prize (2025) — 1st place (Agentless adaptation)

- Author + credibility: Eduardo Rocha de Andrade (late joiner ~1 month; systems
  adapter, not from-scratch builder).
- URL: https://www.kaggle.com/competitions/konwinski-prize/writeups/eduardo-rocha-de-andrade-1st-place-solution-write-
- Words (est.): ~1800.
- Structure: why Agentless-1.5 as base / context + reproduction-test mods for weak
  32B local models / repair-patch generation (4 samples/location: greedy + temperature;
  SEARCH/REPLACE scheme >> raw diffs for validity) / validation funnel (git-apply
  dry-run -> F2P fix check -> P2P regression compare) / private-LB postscript
  (9 correct / 2 wrong / 109 skipped; frontier-model outlook).
- Tables (2; example): patch-validation funnel counts; F2P/P2P pass matrix.
- Figures (est. 1; type): agent pipeline (localize -> reproduce -> repair -> validate).
- Code samples (2): the repair prompt (quoted); SEARCH/REPLACE output scheme.
- Hook: "Joining late, adapt open-source instead of coding from scratch" + memorization
  insight (huge models import correctly from memory; 32B models need generated tests).
- Reproducibility: upstream base pinned (Agentless 1.5) + enumerated diffs; sampling
  spec exact (8 candidates/location); runtime optimization for local models noted.
- Signal: HIGH. 2025, agentic/SWE — closest genre analog to agent-security work.
- Award-worthy (1 line): Transparent fork-diff methodology: what upstream did, what
  changed, why, with validity-rate evidence.
- Lesson for OUR note (1 line): For agent work, publish the upstream-vs-fork diff table
  and the validation funnel (candidate -> valid -> fixes -> no-regressions).

## 23. UM — Game-Playing Strength of MCTS Variants (2024) — 1st place

- Author + credibility: James Day (solo; measurement-hacker profile).
- URL: https://www.kaggle.com/competitions/um-game-playing-strength-of-mcts-variants/writeups/james-day-1st-place-solution
- Words (est.): ~3000.
- Structure: starting-position evals (+0.045 CV / +0.012 LB; 15 s search ~= 1 h of
  matches, ~250x) / search-speed metrics (+0.005 CV) / extra data with per-model-type
  weights (+0.004 CV) / augmentation (+0.002) / feature selection / isotonic-regression
  postprocess (+0.002, beats scale-and-clip) / TabM (Yandex deep tabular, competitive
  with LGBM) / hyperparameter tuning / ensembling / Trust-CV-vs-Trust-LB / failures /
  missed avenues (flip augmentation — "0.01 better hybrid exists?!").
- Tables (est. 3; example): per-trick CV/LB delta ledger (every section ends with
  paired numbers); extra-data weight table per model type.
- Figures (2; types): tree-search config comparison visualization (UCB1/Tuned x
  random/NST playouts); stacked-ensemble (CatBoost/LGBM/TabM/isotonic) diagram.
- Code samples (3): UCB1Tuned-0.6-Random200 config + Ludii dependency pin (with
  suspected player-VERSION discrepancy disclosed); isotonic postprocess; ensemble weights.
- Hook: "Trust CV beat Trust LB on BOTH boards — I did not expect that" + crediting
  rivals' trick he missed (flip/inversion augmentation per goldenlock).
- Reproducibility: dependency version caveat stated; per-trick deltas; weights tuned to
  CV not LB (explicit). Seeds: partial.
- Signal: VERY HIGH. 2024, decision-theory content no other note has.
- Award-worthy (1 line): A dedicated "Trust CV vs Trust LB" strategy section plus
  "things I missed" generosity — the note reads as science, not victory lap.
- Lesson for OUR note (1 line): Add two closing sections — "What failed" and "What we
  missed / others did better" — with numbers and credit.

## 24. Stanford RNA 3D Folding (2025) — 1st place (hybrid TBM + DRfold2)

- Author + credibility: g john rao / jaejohn (first gold, first win; fast.ai + Radek-book
  + Khan Academy + HF-courses background — community-trained).
- URL: https://www.kaggle.com/competitions/stanford-rna-3d-folding/writeups/1st-place-solution ;
  notebooks: .../code/jaejohn/sub-2-hybrid-single-model, ...-folds-tbm-only
- Words (est.): ~2500 + active Q/A thread (parser details, dinucleotide ablations).
- Structure: competition strategy (TBM-from-day-1 from CASP literature + host talk) /
  metric analysis (TM-score: length-normalized, local-error-robust -> prioritize global
  fold) / data strategy (93-variant modified-base mapping, disorder-aware extraction:
  +36 sequences, +0.02-0.03) / TBM 5-step + adaptive refinement / DRfold2 enhancements
  (float64, torch.cdist, spline-cache, PyTorch LBFGS, Boltz-1) / hybrid + graceful
  fallback / ablations (TBM-only 0.59298 vs hybrid; DRfold2-disabled rescore 0.58487).
- Tables (2; example): TBM-only vs hybrid vs disabled-component rescores; template-
  library size sensitivity notes.
- Figures (est. 2; types): 5-step TBM pipeline; confidence-based routing schematic.
- Code samples (3): BioPython DisorderedAtom hasattr parser; comprehensive nucleotide
  mapping; notebook links as executable proof.
- Hook: 90 days refining ONE idea from literature; authors' own caveats quoted
  (p.8 lines 305-317: 5th-ranked model beats top-ranked -> fix ranking, not the net).
- Reproducibility: notebooks linked; template-library version caveat; dinucleotide-16
  vs 10 ablation answered in thread (0.5895 vs 0.59298). Seeds: partial.
- Signal: VERY HIGH. 2025, scientific-ML, literature-grounded, metric-first reasoning.
- Award-worthy (1 line): Metric-properties -> strategy derivation, then literature
  page-and-line citations for every enhancement.
- Lesson for OUR note (1 line): Open with metric analysis that DERIVES the strategy;
  cite external literature precisely (page/line) for each design choice.

## 25. Santa 2025 — Christmas Tree Packing (2025) — 1st place (GA + GPU relaxation)

- Author + credibility: jeroencottaar (Kaggle rank #2 at win time — elite optimizer).
- URL: https://www.kaggle.com/competitions/santa-2025/writeups/1st-place-genetic-algorithm-and-gpu-relaxation ;
  notebooks: .../code/jeroencottaar/santa-2025-1st-place-solution (read FIRST) +
  .../santa-2025-1st-place-first-share (all-200-solutions gallery)
- Words (est.): ~2000 + 2 notebooks.
- Structure: "read the notebook first" inverted pedagogy / GA core (hierarchical
  interaction layers; diversity-vs-domination mechanisms) / GPU relaxation (heavily
  optimized local minima; far more accepted moves) / symmetry + tessellated seeds
  (180-degree constraint for even counts; optimize-the-edge) / gallery notebook.
- Tables (est. 1; example): move-acceptance / relaxation convergence stats.
- Figures (STAR; types): packing visualizations; full 200-solution gallery (proof by
  exhibition); symmetry-constraint schematics.
- Code samples: 2 notebooks as the code (demo-first, share-second).
- Hook: GA wins at the top level + symmetry insight that deletes degrees of freedom;
  NeurIPS-corridor praise quoted in thread.
- Reproducibility: executable notebooks first, prose second — strongest
  show-don't-tell in the set. Seeds/hardware: in notebooks (verify).
- Signal: VERY HIGH. 2026-dated (Santa 2025, newest in set); visualization-as-proof.
- Award-worthy (1 line): The 200-solution gallery figure makes the win legible in
  10 seconds; the notebook-first ordering respects the reader.
- Lesson for OUR note (1 line): For optimization/agent-trace work, ship a gallery
  figure (all solutions/traces at a glance) and link runnable code ABOVE the prose.

---

## Honorable mentions (Working-Note genre exemplars, not counted in 25)

- A. ARC Prize 2025 — 2nd place, "The ARChitects' Solution" — SOLUTION CARDS format
  (per-approach card: performance, hyperparams, insights/tradeoffs) + expected-vs-real
  score honesty (16.53 expected, 19.17 real). Best card-template model for OUR note.
- B. NeurIPS Ariel Data Challenge 2025 — 7th gold, HorikitaSaku + takaito — bug-fix
  diary (orbital-period dataset update), team-merge narrative, "anxiety causes mistakes"
  confessional; first-to-publish solution. Best process-diary model.
- C. Optiver 2023 top-5% peer-reviewed writeup (Cohen et al., ESANN 2024,
  doi:10.14428/esann/2024.ES2024-159) — the formal "Working Note" genre exemplar:
  related-work comparison (SVR vs LGBM vs NN-ensemble), ablation study, revealed-target
  feature engineering. Closest template to an academic working note.
- D. Santa 2025 thread praise + MCTS goldenlock writeup — cited-with-credit pattern.

## Top 5 lessons for OUR Working Note (distilled)

1. One ablation table (methods x treatments, paired CV/LB deltas) is the centerpiece —
   copy Optiver-hyd #6 and IEEE #1: every trick gets a before/after number.
2. Publish the full feature/artifact registry as a table (Rossmann #2, LLM-Science #15);
   pin every external dataset, model ID, and version.
3. State the decision rule (validation protocol, ship threshold, seed handling) and log
   overrides (ISIC #10, MCTS #23, Titanic #3); report seed variance, never single-seed
   headlines (Jigsaw #12, MAP #16).
4. Front-load integrity: provenance, no-leak ablations, temporal-artifact controls,
   luck disclosure (LEAP #13, Malware-2019 #21, Home Credit #5).
5. Close with failures + missed avenues + credit to rivals (MCTS #23, APTOS #9,
  Santa-gallery #25 as the visual proof); keep prose dense — 1800-2500 words with
  code/notebook links beats 6000 words of adjectives.
