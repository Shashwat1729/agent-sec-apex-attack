# Winning Kaggle Solution Writeups — 25 Notes (Set B)

Scope: 25 MORE competition-winning (1st place or gold-medal / Working-Note-grade) solution writeups,
complementary to research/WINNING_NOTES_A_25.md (Set A). Zero overlap with Set A by design:
no IEEE-Fraud, Rossmann, Titanic, House Prices, Home Credit-2024, Optiver-Close-2024, Mania-2025,
APTOS, ISIC-2024, SIIM-ISIC-2020, Jigsaw-multilingual, LEAP, LMSYS, LLM-Science-Exam, MAP-2025,
LLM-Prompt-Recovery, AIMO-PP1-Numina, Feedback-Effective-Arguments-main-track, Malware-BIG2015,
Malware-Prediction-2019, Konwinski-2025, MCTS-variants, RNA-folding-2025, Santa-2025.
Method: 20+ websearch sweeps (top-8 results each) with queries disjoint from Set A, plus
search excerpts (several long/verbatim, incl. full Vesuvius-1st, Quora-1st, LANL-1st,
Make-Data-Count-1st bodies and the ARC-2024 technical report).
Limitation (honest): Kaggle discussion/writeup pages are auth-walled — fetch returns title only.
Entries built from search excerpts, GitHub mirrors, press releases, and community explainers.
Fields marked (est.) are estimates. Thin entries flagged inline; verify URLs before citing.

## Cross-cutting pattern (Set B confirms Set A, plus 3 new twists)

1. Structure: same spine (thanks -> TL;DR -> validation -> method-with-deltas -> failures -> code).
   New: 2024-2026 winners add explicit Data-Provenance and Compute-Budget sections (RSNA-2025, ARC-2024).
2. Tables: ablation ledgers again the centerpiece (BirdCLEF-2024 min-vs-mean, ASHRAE private-vs-public).
3. Figures: segmentation/audio-visual proof dominates vision/audio (Vesuvius before/after, HPA UMAP,
   BirdCLEF spectrograms, Airbus masks); tabular notes still table-led.
4. Code: GitHub mirrors now the norm for 1sts (ARC-2024, BirdCLEF-2024, CommonLit-1st, HPA-23rd,
   TalkingData-1st, VSB, G2Net-II); Kaggle notebooks linked as executable proof.
5. Reproducibility: bimodal — elite (ARC-2024 paper+weights+H100 recipe; CommonLit Colab chain;
   LANL kernels re-scoring 1st) vs thin (Airbus-1st, G2Net-I-1st bodies not retrievable — flagged).
6. Words: same bimodality as Set A — terse (~700-900: Cassava-1st, VSB-1st-notebook) vs
   comprehensive (2500-4500: Quora-1st, LANL-1st, ARC-2024 paper). Median band ~1500-2500.
7. New twists vs Set A: (a) seed-as-hyperparameter confessions (ARC-2025-5th);
   (b) label-noise-first design (RSNA-aneurysm coarse-to-fine, HPA weak labels);
   (c) leak-reset post-mortems as the writeup (Airbus-2018, Porto Seguro hardness).

---
## 1. RSNA 2024 Lumbar Spine Degenerative Classification — 1st place

- Author + credibility: 1st-place team (discussion 540091, Oct 28 2024; verify names before citing).
- URL: https://www.kaggle.com/competitions/rsna-2024-lumbar-spine-degenerative-classification/discussion/540091
- Words (est.): ~2000.
- Structure: gratitude / spine-level pipeline (lumbar slice grouping) / per-condition heads /
  CV protocol / ensemble / post-processing.
- Tables (est. 2; example): per-degeneration-condition CV-vs-public deltas (disc/stenosis heads).
- Figures (est. 2; types): sagittal-slice grouping schematic; per-level score bars.
- Code samples (est. 2): slice-group dataloader; level-weighted loss.
- Hook: 5-condition multi-head grading on volumetric MRI under weighted-log-loss — anatomy-aware
  grouping is the whole game.
- Reproducibility: fold protocol + head weights customarily posted; seeds/hardware partial. Verify.
- Signal: HIGH. 2024 RSNA flagship; freshest spine-imaging winner. Auth-walled body — excerpt-based.
- Award-worthy (1 line): Anatomy-first problem decomposition (level x condition heads) with
  per-head ablations.
- Lesson for OUR note (1 line): When the label space is structured (levels x conditions), ablate
  per-structure heads, not just the global score.

## 2. RSNA 2025 Intracranial Aneurysm Detection — 1st place

- Author + credibility: 2025 winner (writeup Oct 15 2025) + GitHub mirror uchiyama33/rsna2025_1st_place.
- URL: https://www.kaggle.com/competitions/rsna-intracranial-aneurysm-detection/writeups/1st-place-solution ;
  mirror: https://github.com/uchiyama33/rsna2025_1st_place/blob/main/solution_v2_1.md
- Words (est.): ~2500 + mirror doc.
- Structure: coarse-to-fine pipeline / vessel segmentation to guide ROI classifier /
  location-aware predictions / multimodal (CTA/MRA) handling / ensemble.
- Tables (est. 2; example): coarse-stage recall vs fine-stage AUC ladder; ROI-vs-whole-volume ablation.
- Figures (est. 3; types): vessel-mask overlays; ROI-crop schematics; FROC-style curves.
- Code samples (est. 3): segmentation-guided ROI extraction; location-aware head; inference kernel.
- Hook: Detection-first, classification-second — the segmenter buys the classifier its signal.
- Reproducibility: STRONG-ish — public mirror doc + thanked radiologists/institutions; exact seeds
  partial. Best-documented RSNA-2025 1st of the set.
- Signal: VERY HIGH. 2025, 1,147 teams, 50K dollars; 13 writeups (1st-38th) archived at kaggle.farid.one.
- Award-worthy (1 line): A two-stage pipeline where stage 1 (segmentation) is evaluated as a
  recall gate for stage 2 — cascading metrics, not one number.
- Lesson for OUR note (1 line): For detection-then-decide pipelines, report per-stage metrics and
  the gate-ablation (no-ROI vs ROI).

## 3. RSNA-MICCAI Brain Tumor Radiogenomic Classification 2021 — 1st place

- Author + credibility: 1st-place team, discussion/281347 ("very simple code" framing).
- URL: https://www.kaggle.com/c/rsna-miccai-brain-tumor-radiogenomic-classification/discussion/281347
- Words (est.): ~1200.
- Structure: MGMT-promoter-methylation from mpMRI / simple-architecture-that-generalizes /
  heavy-augmentation-over-modeling / fold discipline.
- Tables (1; example): per-fold AUC with simple-vs-complex backbone comparison.
- Figures (est. 1-2; types): MRI modality stack illustration; augmentation gallery.
- Code samples (2): the "very simple" training loop; TTA recipe.
- Hook: Simplicity as provocation — won a 3D-genomics competition with the plainest code.
- Reproducibility: code-forward; compact. Seeds partial.
- Signal: MEDIUM-HIGH. Older (2021) but the canonical simplicity-beats-complexity medical-vision note.
- Award-worthy (1 line): Proved augmentation + validation beat architecture search with a minimal diff.
- Lesson for OUR note (1 line): Keep one minimal-solution control alive to the end; report what
  complexity failed to add.

## 4. Santa 2024 — The Perplexity Permutation Puzzle — 1st place (Team Santa Master)

- Author + credibility: Team Santa Master (winners-walkthrough video) + Wu-n0 GitHub solution +
  Santamizers 3rd-place writeup + Konica Minolta 13th-place/gold press release (Mar 13 2025).
- URL: https://www.kaggle.com/competitions/santa-2024 ;
  walkthrough: https://www.youtube.com/watch?v=_Nm_dtwwZDo ;
  repo: https://github.com/Wu-n0/kaggle-santa-2024-solution ;
  3rd: https://www.kaggle.com/competitions/santa-2024/writeups/santamizers-3rd-place-solution ;
  press: https://www.konicaminolta.com/global-en/newsroom/2025/0313-01-01.html
- Words (est.): walkthrough + repo + 3rd writeup ~3000 combined.
- Structure: descramble-Christmas-stories-to-minimize-perplexity / Sorted-Other-words insight (3rd) /
  LLM-scoring dynamics / search strategy (beam/greedy + local swaps) / compute budget.
- Tables (est. 2; example): perplexity-vs-iteration ladder; strategy bake-off (greedy vs beam vs SA).
- Figures (est. 2; types): permutation schematic; score-progression curves.
- Code samples (3): Wu-n0 rearrange pipeline; perplexity-eval harness; 3rd-place sorted-words trick.
- Hook: An optimization contest scored by LLM perplexity — search beats learning; "Sorted Other
  words are all you need" (3rd-place title).
- Reproducibility: repos + inference kernels public; exact LLM-scoring pins version-sensitive. Partial.
- Signal: HIGH. 2024 Santa; complements Set-A Santa-2025 (packing) with an LLM-scored flavor.
- Award-worthy (1 line): Turned an LLM metric into a search problem and published the
  cost-perplexity frontier.
- Lesson for OUR note (1 line): When the metric is a model call, publish the
  score-vs-compute curve, not just the final score.

---
## 5. ARC Prize 2024 — 1st place (the ARChitects, 53.5 percent)

- Author + credibility: Daniel Franzen, Jan Disselhoff, David Hartmann (the ARChitects) —
  open-source winners on P100 x12h, no-internet; paper + HF weights.
- URL: https://arcprize.org/competitions/2024 ;
  paper: https://github.com/da-fr/arc-prize-2024/blob/main/the_architects.pdf ;
  code: https://github.com/da-fr/arc-prize-2024 ;
  notebook: https://www.kaggle.com/code/dfranzen/arc-prize-2024-solution-by-the-architects ;
  tech report: https://arcprize.org/blog/arc-prize-2024-winners-technical-report (MindsAI 55.5 pct
  ineligible — did not open-source).
- Words (est.): paper ~6000 + README; leaderboard: 1,430 teams, 17,789 entries.
- Structure: test-time-training (TTT) on NeMo-Minitron-8B / novel augmentations /
  stability-based selection criterion / induction+transduction ensemble framing (per tech report).
- Tables (3; example): 53.5 pct vs 40.0/40.0/37.0/37.0 top-5; augmentation-ablation ladder;
  stability-selection vs likelihood-selection.
- Figures (3+; types): TTT pipeline overview.png; score-over-time; induction-vs-transduction Venn.
- Code samples (5+): run_finetune_Nemo-full.py; run_evaluation scripts (LoRA + diskcache);
  offline-wheel notebook for no-internet Kaggle; HF model da-fr/Mistral-NeMo-Minitron-8B-ARChitects.
- Hook: Solved ARC-AGI perspective-taking with TTT + stability selection on a single H100 —
  and open-sourced everything while the higher scorer (MindsAI) stayed closed.
- Reproducibility: STRONGEST in Set B — Apache-2.0, retrain recipe, wheels, weights, params.json.
- Signal: VERY HIGH. 2024 flagship reasoning result; 25K dollars + paper-runner-up 2.5K.
- Award-worthy (1 line): A selection criterion (solution stability under augmentation) as the
  novel contribution, with weights and wheels to rerun it.
- Lesson for OUR note (1 line): Publish the selection rule that picks among candidates, not just
  the generator — with the ablation that proves the rule.

## 6. ARC Prize 2025 — 5th place (Lonnie, seed-as-hyperparameter) [cautionary inclusion]

- Author + credibility: lonnieqin (4th-5th; self-reported 344th-public to 5th-private jump).
- URL: https://www.kaggle.com/competitions/arc-prize-2025/writeups/arc-prize-2025-competition-writeup-5th-place ;
  context: https://arcprize.org/blog/arc-prize-2025-results-analysis (2025 SOTA 24 pct on ARC-AGI-2)
- Words (est.): ~3000.
- Structure: fork of 2024-1st baseline (sanyul/boristown notebooks) / 4-GPU LoRA train+infer /
  Turbo-DFS beam search / random-seed 19920627 as THE change / 3.33 pct-to-6.67 pct seed-variance math.
- Tables (2; example): seed-vs-score table (2x variance, +-4 tasks/120); public-344th vs private-5th.
- Figures (1; type): file-layout/infra diagram (model_runner/selection/async_tools/common_stuff).
- Code samples (1 + links): forked notebook link; seed config.
- Hook: Honest heresy — "treating random seed as a first-class hyperparameter" in a 120-task eval.
- Reproducibility: notebook public; single-seed selection explicitly public-LB-picked (author admits
  the risk). Reproducible but FINELY caveated — include as a negative exemplar with the lesson.
- Signal: MEDIUM as method, HIGH as warning. 2025, 1,455 teams.
- Award-worthy (1 line): Quantified small-sample variance (1-2 tasks = large rank jumps) that every
  small-eval paper should cite.
- Lesson for OUR note (1 line): Never select on a 120-sample public board without saying so —
  report the variance table and the selection protocol (extends Set-A MAP-2025 seed lesson).

## 7. Feedback Prize — English Language Learning 2023 — 1st place

- Author + credibility: rohitsingh02 + Yevhenii Maslov — full retrain recipe on
  Paperspace A6000, Ubuntu 20.04, Python 3.9.13, CUDA 11.6.
- URL: https://www.kaggle.com/competitions/feedback-prize-english-language-learning/discussion/369457 ;
  repo: https://github.com/rohitsingh02/kaggle-feedback-english-language-learning-1st-place-solution (55 stars)
- Words (est.): discussion ~2500 + README retrain manual ~2000.
- Structure: 5-fold MultiLabelStratifiedKFold / two-stage pseudo-label loop (FB1 -> FB3) /
  model2..model71 curriculum / column-wise weighted ensembles / SVR-embedding side models /
  Optuna weight tuning.
- Tables (2; example): pseudo-label round-vs-CV ladder; ensemble-weight vectors (Optuna-tuned).
- Figures (est. 1-2; types): two-stage loop diagram; OOF-vs-LB tracking.
- Code samples (5+): train_first_step.sh / train_second_step.sh / train_pl.sh / inference.py modes
  (oofs/prev_pseudolabels/curr_pseudolabels/submission) / weight-tuning-optuna.ipynb.
- Hook: A 70-model curriculum where pseudo-labels compound — the ensemble that labels the next round.
- Reproducibility: STRONG — hardware/software pinned, directory layouts, run order, dataset links,
  final merged-submission kernel. Seeds partial.
- Signal: VERY HIGH. Distinct from Set-A Feedback-2022-main-track; the pseudo-label-curriculum reference.
- Award-worthy (1 line): A shell-scripted curriculum (first-step/second-step) that makes a 70-model
  pipeline re-runnable by others.
- Lesson for OUR note (1 line): For iterative pseudo-labeling, publish the round protocol (scripts,
  order, weight files), not just the final ensemble.

## 8. Feedback Prize — Effective Arguments 2022 — Efficiency-track 1st (Team Hydrogen)

- Author + credibility: ybabakhin (Yuriy Babakhin) / st81 — Team Hydrogen; main-track repo (66 stars)
  + efficiency-track model.
- URL: main: https://www.kaggle.com/competitions/feedback-prize-effectiveness/discussion/347536 ;
  efficiency: https://www.kaggle.com/competitions/feedback-prize-effectiveness/discussion/347537 ;
  repos: https://github.com/ybabakhin/kaggle-feedback-effectiveness-1st-place-solution ;
  https://github.com/st81/kaggle-feedback-effectiveness-1st-place-solution-st
- Words (est.): ~2000 + READMEs.
- Structure: two-level stacking (first-level DeBERTa-family + second-stage notebooks) /
  efficiency-model distillation (yaml/efficiency_model.yaml) / separate Main-LB vs Efficiency-LB
  solutions with two inference kernels.
- Tables (2; example): first-level OOF table; efficiency-vs-accuracy Pareto.
- Figures (est. 1; type): two-stage stack diagram.
- Code samples (4): train.py/train.sh; second_stage notebooks; efficiency yaml; inference kernels
  (team-hydrogen-1st-place + efficiency-prize-1st-place).
- Hook: Won TWICE — accuracy track AND efficiency track — with one codebase and two heads.
- Reproducibility: repos with requirements.txt, data-gen notebooks, kernels. Strong for 2022.
- Signal: HIGH. Complements Set-A entry 19 (cited via MAP-2025 lineage); this entry adds the
  efficiency Pareto both tracks share.
- Award-worthy (1 line): Dual-track reporting (score AND cost) with a config-file efficiency model.
- Lesson for OUR note (1 line): Report the cost axis (params/latency) next to the score axis;
  ship the small-model config, not just the winning ensemble.

---
## 9. Vesuvius Challenge — Ink Detection 2023 — 1st place (ryches team)

- Author + credibility: ryches + Alex Loftus + Aina Tersol + Ted K;
  112 upvotes; code public via scrollprize links (host-confirmed in thread).
- URL: https://www.kaggle.com/competitions/vesuvius-challenge-ink-detection/writeups/ryches-1st-place-solution ;
  repo: https://github.com/ainatersol/Vesuvius-InkDetection
- Words (est.): ~3000 + 28-comment Q/A (end-to-end vs staged, channel-shuffle ablation).
- Structure: TL;DR (larger crops win) / depth-invariant 2-stage (3D UNETR -> 32ch -> SegFormer-b5) /
  1024-crops-see-whole-letters / 9-model ensemble / 4x-rotation TTA + 1/4-stride windows /
  per-pixel aggregation study / connected-components cleanup (25000px local / 10k submit).
- Tables (2; example): crop-size ladder (128 less than 512 less than 1024, same wall-clock);
  single 0.82/0.67 to ensemble; stride-halving +0.01 vs adding-models tradeoff.
- Figures (2+; types): Before/After cleanup (explicitly captioned in note); letter-scale crop views.
- Code samples (4+): 3D-to-2D flatten; SegFormer low-res head + conv2d-transpose upscale; strided-TTA
  aggregation options; cv2.connectedComponents denoiser.
- Hook: "128 got beat by 512 which got beaten by 1024" at IDENTICAL training cost — context is free.
- Reproducibility: STRONG — repo + host-published top-10 code links; failed channel-shuffle and
  empty-vs-ink crop-filtering reported in thread. Seeds partial.
- Signal: VERY HIGH. 100K-dollar progress prize; most-cited 3D-to-2D segmentation writeup on Kaggle.
- Award-worthy (1 line): Depth-invariance as an explicit design constraint, validated by a
  failed-convergence ablation (channel-shuffled control).
- Lesson for OUR note (1 line): State the invariance your architecture guarantees, then show the
  control experiment that breaks without it.

## 10. Vesuvius Challenge — Surface Detection 2026 — 1st place (Tony Li team)

- Author + credibility: Tony Li + OzanM + Yiheng Wang + PaulG; 65 upvotes; rank-1 both boards.
- URL: https://www.kaggle.com/competitions/vesuvius-challenge-surface-detection/writeups/1st-place-solution-for-the-vesuvius-challenge-su ;
  notebook: https://www.kaggle.com/code/tonylica/nnunet-4-model-7-5-2-1-final-submit-so-long
- Words (est.): ~2200 + 24-comment Q/A (post-processing ablations added on request).
- Structure: nnU-Net ensemble (patch 128 to 160/192/224/256, 4000 epochs) / logits-vs-probability
  fusion (private favors logits) / threshold 0.35-0.4 vs public overfit / heightmap hole-filling /
  touching-sheets failure admission / vibe-coding pipeline redesign note.
- Tables (2; example): patch-size x epoch grid; post-processing on/off + threshold sweep (1e-3-level).
- Figures (est. 2; types): sheet-surface renders; hole-filling before/after.
- Code samples (3): patch-size fine-tune chain; fusion + threshold block; solution notebook.
- Hook: Rank-1 public AND private with an off-the-shelf framework (nnU-Net) — tuning discipline
  over novelty, plus an honest public-overfit confession.
- Reproducibility: notebook public after a nudge (thread documents the fix); MONAI/JAX-vs-nnU-Net
  benchmark noted. Good.
- Signal: HIGH. 2026 (newest vision 1st in set); the nnU-Net-tuning reference.
- Award-worthy (1 line): Added the requested post-processing ablation table AFTER publishing —
  living documentation.
- Lesson for OUR note (1 line): Budget one table for post-processing on/off; answer reviewer-style
  questions by editing numbers into the note.

## 11. HMS — Harmful Brain Activity Classification 2024 — 1st place (Team Sony)

- Author + credibility: Team Sony (discussion/492560, Apr 2024); corroborated by Albumentations
  winners page + 123rd-place reproducible package (YutoTerashima).
- URL: https://www.kaggle.com/c/hms-harmful-brain-activity-classification/discussion/492560 ;
  context: https://albumentations.ai/adoption/competitions/kaggle/hms-harmful-brain-activity-classification/
- Words (est.): ~2500 (est.; auth-walled body via excerpts).
- Structure: EEG spectrogram + raw-signal dual path / expert-disagreement-aware targets
  (idealized/proto/edge-case vote distributions) / soft vote-distribution labels / ensemble.
- Tables (est. 2; example): per-pattern (seizure/LPD/GPD/LRDA/GRDA/other) vote-modeling ablations.
- Figures (est. 3; types): spectrogram exemplars per agreement tier (host overview figure);
  vote-distribution simplex; discard/confidence curves.
- Code samples (est. 3): spectrogram pipeline; soft-label loss; inference ensemble.
- Hook: The labels ARE disagreements — model the vote distribution, not the majority.
- Reproducibility: winner thread + independent silver reproducible package; exact seeds partial.
- Signal: HIGH. 2024, 2,767 teams; the label-uncertainty template for biosignal work.
- Award-worthy (1 line): Turned annotator disagreement taxonomy (idealized/proto/edge) into the
  loss function.
- Lesson for OUR note (1 line): If experts disagree, predict the vote histogram and show the
  per-tier calibration — never collapse to hard labels silently.

## 12. BirdCLEF 2024 — 1st place (chemrovkirill team)

- Author + credibility: Kirill Chemrov team (discussion/512197) + GitHub arpoyda/BirdCLEF_2024 +
  inference kernel + Zenn explainer (yuto_mo, Jun 2024) with score tables.
- URL: https://www.kaggle.com/competitions/birdclef-2024/discussion/512197 ;
  repo: https://github.com/arpoyda/BirdCLEF_2024 ;
  kernel: https://www.kaggle.com/code/chemrovkirill/birdclef-2024-1st-place-inference ;
  explainer: https://zenn.dev/yuto_mo/articles/ad43c630729073
- Words (est.): writeup ~2500 + explainer ~3000.
- Structure: 182-class audio AUC / unlabeled-soundscape mining via Google classifier (distillation) /
  statistics T = std+var+rms+pwr trick / EfficientNet-b0 + RegNetY backbones (VITs worse) /
  6-model ensemble (min vs mean fusion table) / chunk-n postprocessing / joblib mel-spec + RAM cache.
- Tables (STAR; example): fusion table — ensemble(min) 6xEffNet 0.689/0.739; mean variants;
  public-private correlation 0.96.
- Figures (est. 2; types): mel-spectrogram pipeline; per-chunk prediction schematic.
- Code samples (5): run_unlabeled_preprocessing.py / run_training.py configs / run_inference.py /
  mel-spec joblib parallel / RAM-cached spec store.
- Hook: Simple backbones + mined unlabeled data beat fancy SED/ViT variants — "overly complex
  models do not work better than simple ones."
- Reproducibility: STRONG — repo with configs, dataset birdclef24-final weights, kernel. Seeds partial.
- Signal: VERY HIGH. 2024, 974 teams; best audio-winner documentation in set (primary + explainer).
- Award-worthy (1 line): Every trick ships with a paired public/private number and a stability
  correlation (0.96) — trust quantified.
- Lesson for OUR note (1 line): For weakly-labeled audio, document the unlabeled-mining loop
  (teacher to pseudo to filter) with its own ablation row.

---
## 13. Cassava Leaf Disease Classification 2021 — 1st place (CropNet)

- Author + credibility: 1st-place team (discussion/221957); 3,900 teams; 21 linked solutions archived.
- URL: https://www.kaggle.com/competitions/cassava-leaf-disease-classification/discussion/221957 ;
  index: https://kaggle.farid.one/ (Cassava section, 21 links)
- Words (est.): ~700-900 (terse).
- Structure: TF-Hub CropNet (cassava-pretrained) / fine-tune / TTA / ensemble.
- Tables (1; example): backbone bake-off (ImageNet-pretrained vs CropNet-pretrained accuracy).
- Figures (est. 1; type): diseased-leaf gallery per class (5 classes).
- Code samples (1-2): Hub-load + fine-tune loop; TTA predict.
- Hook: Domain-pretraining wins outright — a cassava-trained backbone beats bigger generic nets.
- Reproducibility: minimal but sufficient (Hub model ID + recipe). Seeds partial.
- Signal: MEDIUM-HIGH. Terse but high-leverage: the domain-pretraining precedent.
- Award-worthy (1 line): The shortest path to 1st — match the pretraining domain, then stop.
- Lesson for OUR note (1 line): Always test a domain-pretrained backbone as baseline 0 before
  scaling generic models.

## 14. TalkingData AdTracking Fraud Detection 2018 — 1st place (flowlight0)

- Author + credibility: Takanori Hayashi / flowlight0 (200M-click scale) + komaki LDA/NMF features;
  repo 229 stars; Japanese slides; CPMP 6th-overview corroboration.
- URL: https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection/discussion/56475 ;
  6th: https://www.kaggle.com/competitions/talkingdata-adtracking-fraud-detection/writeups/cpmp-solution-6-overview ;
  repo: https://github.com/flowlight0/talkingdata-adtracking-fraud-detection ;
  slides: https://www.slideshare.net/TakanoriHayashi3/talkingdata-adtracking-fraud-detection-challenge-1st-place-solution
- Words (est.): discussion ~2000 + slides ~40 + README config-manual ~2500.
- Structure: click-time-ordered validation (last-day holdout) / next/prev-click deltas /
  future-click counts (10/80) / LDA/NMF IP-device embeddings (komaki) / LightGBM
  (lr 0.01, 255 leaves, depth 8) / negative-downsample bagging x5 / rank-average option.
- Tables (2; example): feature-group ablation (time-deltas vs counts vs topic features);
  downsample-bagging stability.
- Figures (est. 2; types): click-timing schematic; feature-importance bars.
- Code samples (5): cpp feature builders; JSON experiment configs (features/model/dataset blocks);
  click_id_mapper.py; feather pipeline; run.py train_only mode.
- Hook: Fraud is timing — next-click and future-count features on 200M rows with C++ builders.
- Reproducibility: STRONG for 2018 — Docker/AWS recipe, feather caching, JSON-configured
  experiments, per-feature generator registry. Seeds via bagging_size.
- Signal: VERY HIGH. Security-adjacent (ad-fraud) at largest 2018 scale; directly relevant to
  agent-security temporal-feature thinking.
- Award-worthy (1 line): JSON-config experiment registry tying every feature to a generator —
  scale with provenance.
- Lesson for OUR note (1 line): For event-stream fraud, lead with time-delta/count features and
  publish the validation clock (what hour range the holdout imitates).

## 15. Porto Seguro Safe Driver Prediction 2017 — 1st place (Michael Jahrer)

- Author + credibility: Michael Jahrer (legendary; denoising-autoencoder representation learning);
  1098 upvotes + 463 comments — most-discussed tabular 1st ever; corroborated by jeddy92 18th blog.
- URL: https://www.kaggle.com/competitions/porto-seguro-safe-driver-prediction/writeups/michael-jahrer-1st-place-with-representation-learn ;
  thread: https://www.kaggle.com/c/porto-seguro-safe-driver-prediction/discussion/44629 ;
  18th: https://jeddy92.github.io/seguro/
- Words (est.): ~2500 + 463-comment Q/A.
- Structure: leakage-free discipline / denoising-autoencoder pretraining on 600Kx59 anonymized rows /
  supervised fine-tune / Gini = 2xAUC-1 rank-averaging / stacked ensemble with entity embeddings.
- Tables (2; example): DAE-pretrained vs from-scratch Gini (0.29698 winning line; ceiling ~0.65 AUC);
  resampling-strategy diversity matrix.
- Figures (2; types): autoencoder schematic; CV-vs-LB scatter under noise (std ~0.01+).
- Code samples (3): DAE pretrain; entity-embedding head; rank-average stacker.
- Hook: A neural net wins the messiest tabular competition ever — by pretraining on noise first.
- Reproducibility: kernels + 463-comment lab notebook; seeds partial; CV-noise honesty exemplary.
- Signal: VERY HIGH. 5,200 teams; canonical hard-tabular win (nothing breaks 0.65 AUC).
- Award-worthy (1 line): Won by learning representations of missingness and noise, with the
  noisiest CV ever reported honestly.
- Lesson for OUR note (1 line): On low-signal tabular data, report CV standard deviations
  prominently and pretrain the representation before the classifier.

## 16. ASHRAE — Great Energy Predictor III 2019 — 1st place (Isamu and Matt)

- Author + credibility: mmotoki (Isamu and Matt); corroborated by Hakky handbook (JP) with full
  per-place tables + 2nd (Vopani) and 3rd (eagle4) writeups.
- URL: writeup: https://www.kaggle.com/competitions/ashrae-energy-prediction/writeups/isamu-matt-1st-place-solution-team-isamu-matt ;
  thread: https://www.kaggle.com/competitions/ashrae-energy-prediction/discussion/124709 ;
  summary: https://book.st-hakky.com/en/data-science/ashrae-solution
- Words (est.): ~2000 + handbook synthesis.
- Structure: manual anomaly scrubbing (flat-lines, spikes, visual) / timezone alignment /
  log1p-per-area targets / 4-meter + 16-site + 2380-building model grid (CatBoost/LGBM/MLP) /
  generalized-weighted-mean ensemble / public-14th to private-1st (1.231) comeback.
- Tables (STAR; example): public-vs-private reversal (0.938/14th to 1.231/1st; 2nd 1.232; 3rd 1.234);
  model-grid (granularity x algorithm) score matrix.
- Figures (est. 2; types): anomaly-gallery (flat/spike); meter-removal sensitivity.
- Code samples (3): anomaly-removal ID list; cyclic hour encoding (cos/sin 2xPIxH/24); granularity-grid trainer.
- Hook: 14th-public to 1st-private by distrusting the public board — the shakeup-survival manual.
- Reproducibility: removal lists + grid spec published; hand-labeling inherently partial. Honest.
- Signal: VERY HIGH. The canonical shakeup-robustness case study (with 2nd/3rd contrasts archived).
- Award-worthy (1 line): Three granularities x three algorithms ensembled by generalization weights —
  robustness as architecture.
- Lesson for OUR note (1 line): Design the ensemble for board-shift (granularity diversity) and
  report public-vs-private deltas for every component.

---
## 17. Shopee — Price Match Guarantee 2021 — 1st place (Upstage)

- Author + credibility: Upstage team (multimodal retrieval specialists); corroborated by 4th-place
  watercooled writeup + jingxuanyang open repo (41 stars).
- URL: https://www.kaggle.com/competitions/shopee-product-matching/writeups/upstage-making-ai-beneficial-1st-place-solution-fr ;
  4th: https://www.kaggle.com/competitions/shopee-product-matching/writeups/watercooled-4th-place-solution ;
  repo: https://github.com/jingxuanyang/Shopee-Product-Matching
- Words (est.): ~2000 (est.; 1st body partially excerpted).
- Structure: embeddings-to-matches / image+text two-tower (EfficientNet + BERT-family) /
  ArcFace-style metric learning / KNN retrieval + thresholding / post-merge rules.
- Tables (est. 2; example): backbone-vs-recall-at-k; text-only vs image-only vs fused.
- Figures (est. 2; types): two-tower diagram; retrieval match gallery.
- Code samples (est. 3): metric-loss config; KNN+threshold matcher; title/OCR cleaning.
- Hook: Retrieval, not classification — 34K products, 11K groups, matched by embedding distance.
- Reproducibility: tower configs + matcher thresholds customarily shared; exact seeds partial.
- Signal: HIGH. Canonical image+text retrieval win; the metric-learning reference for matching tasks.
- Award-worthy (1 line): Framed duplicate-detection as retrieval with a threshold-policy section.
- Lesson for OUR note (1 line): For matching/duplication problems, report recall-at-k curves and the
  threshold-selection protocol, not just accuracy.

## 18. Quora Question Pairs 2017 — 1st place (DL guys, 340 upvotes)

- Author + credibility: Lam Dang, Guillaume Huard, MaxBaudry, PaulTodo, Sebastien Conort
  (BNP Paribas Cardif Datalab + PhD); 340 upvotes, 76 comments.
- URL: https://www.kaggle.com/competitions/quora-question-pairs/writeups/dl-guys-1st-place-solution
- Words (est.): ~3500 (longest NLP-classic in set; fully excerpted).
- Structure: 3 feature families (embedding Word2Vec/Doc2Vec/Sent2Vec/ESIM-SNLI / classical char-1..8g
  TFIDF+LDA/LSI+edit distances / GRAPH density features to 2nd-order neighbors, directed+undirected) /
  Siamese-LSTM + decomposable-attention + ESIM (FastText/GloVe frozen) / test-distribution rescaling /
  4-layer stacking (perimeter Ridge + Lasso-logit + 55/45 blend).
- Tables (2; example): per-layer CV ladder (ESIM ~0.27 CV best single); graph-feature marginal gains.
- Figures (est. 1-2; types): stacking-layer diagram; graph-neighborhood schematic.
- Code samples (4): char-ngram TFIDF block; networkx graph-density features (inception neighbors,
  loops, connex-subgraph stats); Siamese/ESIM configs; perimeter-Ridge stacker.
- Hook: The graph built from train+test PAIRS is a feature — question-neighborhood density predicts
  duplication.
- Reproducibility: feature taxonomy complete enough to reimplement; DL code promised in thread
  ("cleaning scripts, will share"). Partial — flag the code gap honestly.
- Signal: VERY HIGH. 3,295 teams; the most thorough pre-transformer NLP writeup ever.
- Award-worthy (1 line): Three feature families + graph-density to second order + rescaling, each
  with its CV number — the taxonomy IS the paper.
- Lesson for OUR note (1 line): For pair/classification tasks, mine the pair-graph itself
  (neighbors-of-neighbors, loops, subgraph stats) and report graph-feature marginals.

## 19. LANL Earthquake Prediction 2019 — 1st place (The Zoo, 212 upvotes)

- Author + credibility: Psi + dott + ivovkanych + Danijel Kivaranovic +
  CoreyJamesLevinson + Pascal Pfeiffer + Dimosthenis Karaflos + FP — same Zoo core as
  Set-A APTOS-9th, now winning; Giba-endorsed in thread.
- URL: https://www.kaggle.com/c/LANL-earthquake-Prediction/discussion/94390 ;
  kernels: https://www.kaggle.com/ilu000/1-private-lb-kernel-lanl-lgbm/ ;
  https://www.kaggle.com/dkaraflos/1-geomean-nn-and-6featlgbm-2-259-private-lb ;
  story: https://medium.com/@ph_singer/1st-place-in-kaggle-lanl-earthquake-prediction-competition-15a1137c2457
- Words (est.): ~4000 + 113-comment Q/A (KS-test scrutiny, noise-augmentation theory).
- Structure: public-LB-is-lying (ignore it) / train-test alignment via paper-p4677 statistics /
  150+ acoustic features (percentiles/rolling/FFT/MFCC) / TTF+TSF joint targets + normalized
  0-1 variant / noise augmentation for quantile features / LGBM (2.279 = 1st alone) + NN geomean
  (2.25993) / manual end-of-EQ adjustments.
- Tables (3; example): feature-importance shortlist (percentile_roll_std, ffti, mfcc_4_avg...);
  LGBM-only vs blend private MAE; alignment on/off (+0.27: 2.58 to 2.31 reproduced by a reader).
- Figures (2+; types): KS-test train-vs-test distribution plots; TTF/TSF schematic.
- Code samples (4): feature-generation kernel; winning LGBM kernel; geomean blend kernel;
  normalized-target variant.
- Hook: "Completely ignore public LB" — won by matching train statistics to the TEST set instead.
- Reproducibility: STRONGEST time-series entry — two 1st-place kernels public, alignment recipe
  independently reproduced in thread (2.58 to 2.31). Seeds partial.
- Signal: VERY HIGH. The shakeup-immunity masterclass; Satoshi/Giba debate in comments is
  peer review in public.
- Award-worthy (1 line): Published the kernels that score 1st AND the distribution-matching
  justification, then survived adversarial comment scrutiny.
- Lesson for OUR note (1 line): When boards shake, show the train-vs-test distribution plot and
  the alignment ablation — distrust is a result, with numbers.

## 20. CommonLit Readability Prize 2021 — 1st place (mathislucka)

- Author + credibility: mathislucka — Colab-chain documentarian; repo 69 stars; 5th-place Ruby
  writeup corroborates dropout pathology; Deotte comment in thread.
- URL: thread: https://www.kaggle.com/c/commonlitreadabilityprize/discussion/257844 ;
  repo: https://github.com/mathislucka/kaggle_clrp_1st_place_solution ;
  5th: https://www.kaggle.com/c/commonlitreadabilityprize/discussion/259729
- Words (est.): discussion ~1800 + README manual ~1500.
- Structure: ALBERT-xxlarge/DeBERTa/RoBERTa/ELECTRA multi-family / external-data pseudo-label loop
  (prep to label to Kaggle two-models kernel to retrain) / ridge-ensemble over folds /
  dropout train-vs-eval pathology (Ruby: inference in .train() mode + seed-averaged dropout).
- Tables (2; example): per-family CV-vs-public (F2 RoBERTa-large 0.4839/0.470;
  ridge ensemble 0.4553/0.451/0.449); pseudo-label round gains.
- Figures (est. 1; type): pseudo-label loop diagram.
- Code samples (5): 5 ordered Colab notebooks (prep/external/label/train/infer) + Kaggle
  pseudo-label kernel + model-zoo links (10 weight packs) + inference notebook.
- Hook: The winning model is a supply chain — external data in, pseudo-labels around, ridge out.
- Reproducibility: STRONG — ordered notebook chain with BASE_PATH convention, weight packs,
  troubleshooting (DeBERTa CUDA-OOM restart note). Hardware pinned (Colab V100/P100 12-16GB).
- Signal: VERY HIGH. 3,633 teams; the pseudo-label-supply-chain reference for NLP regression.
- Award-worthy (1 line): A runnable factory (numbered notebooks + weight URLs + run order) rather
  than a description.
- Lesson for OUR note (1 line): Number your pipeline notebooks in run order with pinned artifact
  URLs; document the GPU-memory failure mode and its workaround.

---
## 21. Human Protein Atlas — Single Cell Classification 2021 — 1st place (bestfitting)

- Author + credibility: Shubin Dai / bestfitting (legendary GM; team1_bestfitting) — features
  reused by the field (SamusRam 23rd builds on bestfitting DenseNet121); Nature Methods 2022
  competition-analysis paper (Le et al., 28K accesses, 44 citations); HPA model zoo at BioImage.io.
- URL: https://www.kaggle.com/c/hpa-single-cell-image-classification/discussion/239001 ;
  analysis: https://www.nature.com/articles/s41592-022-01606-z ;
  23rd-repo: https://github.com/SamusRam/hpa-single-cell ;
  37th-repo: https://github.com/novice03/HPAv2-37th-solution
- Words (est.): ~2000 (est.; auth-walled) + Nature paper.
- Structure: weakly-supervised (image-level to single-cell) / HCE-cell-segmentation upgrades /
  image-level pretrain to cell-level focal-loss retrain with soft pseudo-labels / negative-label
  probability estimation (public 0.517 to 0.523) / 8-bit 1024/512 dual resolution / flip-TTA.
- Tables (est. 2; example): de-noising on/off mAP; negative-estimator ablation.
- Figures (STAR; types): test-image prediction overlays; UMAP of single-cell features (microtubules /
  nuclear-membrane / nucleoli clusters; nuclear-vs-cytoplasmic meta-clusters, Fig.4a of paper).
- Code samples (est. 3): segmentation upgrades (median-size nuclei filter, border-cell removal);
  focal-loss soft-label loop; negative-probability estimator.
- Hook: 55 pct of proteins multi-localize — the "label" is a population summary, so de-noise first.
- Reproducibility: paper + model zoo + multiple open re-implementations (23rd/37th repos with
  download/repro instructions). Strong-by-corroboration; winner-body excerpt-based.
- Signal: VERY HIGH. 757 teams; only Kaggle win in set with its own Nature Methods analysis.
- Award-worthy (1 line): Weak-label de-noising as a first-class methods section with the UMAP that
  proves the features separate biology.
- Lesson for OUR note (1 line): For noisy/weak labels, show the embedding figure (UMAP) that proves
  de-noising worked — metrics alone do not convince.

## 22. VSB Power Line Fault Detection 2019 — 1st place (mark4h)

- Author + credibility: mark4h (notebook VSB_1st_place_solution) + TheoViel/MaxHalford/ammar1y
  open solutions (ammar1y full EDA-to-ensemble doc, MCC 0.58655).
- URL: https://www.kaggle.com/code/mark4h/vsb-1st-place-solution ;
  EDA-doc: https://github.com/ammar1y/My-Solution-to-VSB-Power-Line-Fault-Detection-Competition ;
  alt: https://github.com/MaxHalford/kaggle-vsb-power ; https://github.com/TheoViel/kaggle_vsb
- Words (est.): notebook ~700 (terse) + ammar1y doc ~2500.
- Structure: 800K-reading signals x 29K / wavelet+Butterworth denoise / find_peaks height/width/
  prominence grids (+/- polarities, subtraction features) / 300 to 68 LightGBM-importance-selected /
  plain 5-fold LightGBM + MCC threshold.
- Tables (2; example): peak-param grid vs MCC; 68-feature importance shortlist.
- Figures (2; types): 3-phase signal plots; before/after denoise overlays (ammar1y doc).
- Code samples (4): pyarrow-parquet reader + transpose; scipy find_peaks/peak_prominences/
  peak_widths loops; LightGBM selector; weighted-average + threshold head.
- Hook: "Simple LightGBM + standard 5-fold CV" wins an 800K-length signal competition — features
  are the model.
- Reproducibility: notebook runnable + ammar1y step-by-step (final_v1/final_v2/final_sub). Good.
- Signal: HIGH. Security-adjacent (grid-fault sensing); the signal-FE cookbook entry.
- Award-worthy (1 line): A denoising-then-peaks recipe with every parameter gridded against MCC.
- Lesson for OUR note (1 line): For long-sensor signals, publish the denoise-then-peak-extract
  table (filter x peak-param x MCC) — that table is the solution.

## 23. Airbus Ship Detection 2018 — top solutions [THIN 1st record — leak-reset context]

- Author + credibility: field via 8th-place SeuTao repo + staff leak-reset thread (inversion, 150
  upvotes) + 21st-place pascal1129 repo. Winner-body thin — flagged.
- URL: leak thread: https://www.kaggle.com/c/airbus-ship-detection/discussion/64388 ;
  8th: https://github.com/SeuTao/Kaggle_Airbus2018_8th_code ;
  21st: https://github.com/pascal1129/kaggle_airbus_ship_detection
- Words (est.): n/a for 1st (unretrieved); reset thread + repos ~2000 combined.
- Structure (reconstructed): U-Net + VGG16/ResNet50V2 encoders / RLE masks / cloud-haze
  augmentation / speed-prize kernel constraints.
- Tables/Figures/Code: via repos (masks, VGG/ResNet-U-Net configs). Sample/prediction JPG pairs
  in open repos.
- Hook: The competition had to be RESET for a data leak — then re-won under scrutiny.
- Reproducibility: via open repos; winner recipe unverified.
- Signal: MEDIUM as documentation, HIGH as cautionary integrity case (pairs with Set-A Home-Credit
  leak disclosure). FLAG: do not cite as a 1st-place method without fetching the winner thread.
- Award-worthy (1 line, provisional): Winning twice — once before and once after a dataset reset.
- Lesson for OUR note (1 line): If the dataset changed mid-competition, document the reset and
  re-validate everything — state which numbers are pre- vs post-reset.

## 24. G2Net Gravitational Wave Detection 2021 + G2Net-II 2022 [THIN 1st body — strong repos]

- Author + credibility: junkoda (G2Net-II 1st-place repo) + salvaba94 end-to-end repo (20 stars) +
  Fkaneko/RainYQ mirrors. Winner prose thin — flagged; code strong.
- URL: comp: https://www.kaggle.com/competitions/g2net-gravitational-wave-detection ;
  II-1st: https://github.com/junkoda/kaggle_g2net2_solution ;
  e2e: https://github.com/salvaba94/G2Net
- Words (est.): n/a for 1st prose; repos ~2000 combined.
- Structure (reconstructed): LIGO-Hanford/Livingston + Virgo time series / trainable preprocessing
  (Tukey windows, bandpass, spectral whitening as Keras layers) / CQT/nnAudio spectrograms /
  EfficientNetV2-2D CNNs / WMW-AUC differentiable loss / AdaBelief + CosineDecayRestarts.
- Tables (est. 1; example): preprocessing-on/off AUC; backbone bake-off (EfficientNetV2 vs others).
- Figures (est. 2; types): chirp spectrograms; detector-network schematic.
- Code samples (5): Preprocessing.py / Augmentation.py (spectral masking, channel permute) /
  Spectrogram.py (nnAudio CQT1992v2 layer) / Losses.py (AUC loss) / Schedulers.py.
- Hook: Preprocessing AS layers — the whitening filter learns with the classifier.
- Reproducibility: repos runnable (TFRecords/NPY pipelines, TPU flags) with a documented TF/NumPy
  troubleshooting patch. Prose thin; code carries it.
- Signal: MEDIUM-HIGH. Only physics-time-series win in set; include for domain breadth with flag.
- Award-worthy (1 line): End-to-end differentiability from raw strain to AUC loss.
- Lesson for OUR note (1 line): For sensor time series, try making preprocessing trainable and
  ablate frozen-vs-learned filters.

## 25. Make Data Count — Finding Data References 2025 — 1st place (Ali + Kea Kohv, 61 upvotes)

- Author + credibility: Ali (asalhi, also Santa-2024 Santamizers-3rd) + Kea Kohv (keakohv);
  61 upvotes, 19 comments; notebook + Zenodo/Corpus grounding; Sep 10 2025 — freshest tabular/NLP
  hybrid in set.
- URL: https://www.kaggle.com/competitions/make-data-count-finding-data-references/writeups/1st-place-solution ;
  notebook: https://www.kaggle.com/code/keakohv/mdc-1st-place-solution-catboost-and-qwen/notebook
- Words (est.): ~3500 (fully excerpted; longest 2025 body in set).
- Structure: competition overview (DOI vs accession-id mentions; Primary vs Secondary) / labeling
  critique (missing labels, F1-should-be-macro) / Summary (DOI: Data-Citation-Corpus + 6xCatBoost on
  title/author/year-similarity; acc-ids: EUPMC + zero-shot Qwen context-snippet; BioSample exception
  with submitter metadata) / detection-stage (mention F1 0.9350 DOI) + type-stage (OOF 0.87;
  triple-match 0.82) / LB table (doi-only 0.362/0.350 to +acc 0.754/0.664 to +Qwen 0.890/0.797) /
  runtime / what-did-not-work (Qwen-for-DOI worse, DataCite-relations, fancy prompts, Marker-OCR
  too slow) / appreciation with named credits.
- Tables (STAR; example): stage-addition LB ladder above (public/private paired); family-inclusion
  lists (included vs NOT-included accession families, ~30 rows).
- Figures (est. 1-2; types): two-pipeline schematic (DOI-metadata path vs acc-id-context path).
- Code samples (4): Crossref/DataCite metadata gather; title/author-similarity features; 6-fold
  group-by-article CatBoost; zero-shot Qwen accession prompt (+BioSample variant).
- Hook: Split the problem by mention TYPE first — metadata ML for DOIs, zero-shot LLM for acc-ids —
  and say which tool loses where.
- Reproducibility: STRONG — notebook linked, Corpus V4.1 + EUPMC TextMinedTerms pins, 6-fold
  group-by-article protocol (test-has-new-articles imitation), OOF numbers at each stage.
  Seeds/hardware (runtime) partial.
- Signal: VERY HIGH. 2025, newest fully-readable 1st in set; exemplary negative-results section.
- Award-worthy (1 line): A what-did-not-work section with four named failures (Qwen-for-DOI,
  relation-types, fancy prompts, Marker OCR) — each with the reason.
- Lesson for OUR note (1 line): When hybridizing ML + LLM, report the tool-assignment matrix
  (which subtask each wins) plus the failures that justify the split.

---
## Honorable mentions (genre exemplars feeding Set B, not counted in 25)

- A. RSNA 2022 Cervical Spine Fracture + RSNA-STR Pulmonary Embolism 2020 + RSNA Breast Cancer
  writeups (5th-place Racers and siblings) — the RSNA house-style lineage behind entries 1-3.
- B. 30-Days-of-ML 1st (CatBoost-seed-average + DAE-Transformer-AutoEncoder Model 5) and
  Tabular-Playground Jan/Feb-2021 DAE 1sts (danzel/Ren, 130/134 upvotes) — the DAE-tabular
  pre-history of Porto Seguro entry 15. Deliberately kept as mentions to protect novelty.
- C. Playground S6E8 (GPT-5.6-Sol single-model win, Aug 2026) + LLM-agents-850-experiments churn win
  (Mar 2026, 600K lines) — recency pointers for agentic-tabular futures; not full entries (thin).
- D. CAFA-6 2026 1st-place writeup family (7 writeups archived) — newest bio-NLP winners; watchlist
  for the next batch.

## Top 5 lessons for OUR Working Note (Set-B distilled; complements Set-A list)

1. Gate your pipeline and meter each gate (entries 2, 9, 21): report
   per-stage recall/gates, then the end-to-end delta — cascading numbers beat one headline.
2. Model the label noise explicitly (entries 11, 21, 19): vote histograms, weak-label
   de-noising with a UMAP proof figure, train-vs-test distribution plots with alignment ablations.
3. Publish the factory, not the story (entries 20, 7, 14, 12):
   numbered notebooks in run order, JSON experiment registries, weight/dataset URLs, run scripts.
4. Split tools by subtask and justify the split with failures (entries 25, 17, 10):
   ML-vs-LLM assignment matrix + what-did-not-work with numbers.
5. Disclose variance, shakes, and resets (entries 6, 16, 23, 18):
   seed-variance tables, public-vs-private component deltas, pre/post-reset re-validation, and a
   named-credit appreciation section (entries 4 and 25 do this best).

## Signal / recency / credibility ledger (for Working-Note prioritization)

- VERY HIGH (cite first): entries 2, 5, 9, 12, 14, 15, 16, 18, 19, 20, 21, 25.
- HIGH (cite with one-line caveat): entries 1, 4, 7, 8, 10, 11, 17, 22.
- MEDIUM, thin-body flagged (verify before citing): entry 3 (simple-code est.),
  entry 6 (seed-picked; use as warning), entry 13 (terse), entry 23 (1st unverified),
  entry 24 (code-strong/prose-thin).
- Recency: 2025-2026 entries 2, 6, 10, 25 (plus watchlist CAFA-6-2026);
  2024 entries 1, 4, 11, 12. No entry duplicates Set A.

(End of file)
