# Kaggle Public Notebooks & Discussion Notes

## Code tab snapshot (2026-08-13; scores are pre-/mid-refresh)
- Getting Started Notebook — 0.075, 1487 upvotes, 12 comments
- **JED - v25 — 89.145** (Gold; verbose gemma / harmony gpt; replay-safe 0.98; "best-of PUBLIC lottery"
  engine, fire-rate-bound ~84±5, re-roll and keep the high roll)
- **JED - Slow multipost — 86.605** (Bronze; slow-row multipost)
- **AISec Pilk — 85.41** (Bronze)
- Hermes Attack v71-n1000-20260721-102018 — 51.525
- Defense-in-Depth Audit, FirstScoreAfteraMonth — 9

## What the extracted notebooks show (methodology lineage)
1. **Dense-exfiltration line** (replay-dense): pure throughput math. `S = 0.09 × N_eff`, N_eff capped
   by replay budget not return count; over-return → timeout → row void. Prompt length is the principal
   cost driver (400→260 chars lifted the ceiling 400→450). Fixed-N profiles (`return_target = min = N`)
   eliminate over-return risk.
2. **Adaptive-uniform line** (two/three-probe recovery): live measurement at the true hop cap, only
   measured-success rows returned, replay ledger bounded independently of the generation deadline.
   Best hosted 88.515 / 89.055 with the SAME attack bytes — sub-point differences include execution
   variance.
3. **JED v25 / SPLIT engine**: latency-classified split (verbose template for gemma, FRAME_TEMPLATE
   Harmony forge for gpt-oss), replay-safe sizing, PROBE_HOPS=1 + REPLAY_COST_COEF scaling, hop-1
   throughput lever, slow-multipost forge variant.
4. **5-templates aggressive replay** (jed-attack-5-templates): plain/bare/bare_ok + 2 injection forms
   (`inj_close`, `inj_commentary`); effective-cost selection = median latency / (fires/sample);
   MIN_FIRE_RATE = 0.2.
5. **Static emit line** (v23-alpha2co-667): NO search, NO gateway, NO llama_cpp — pure static 667
   candidates × 0.09 = 60.03 target; aa.co 2-letter hosts to avoid replay cost. V22 (642) scored 57.78.
6. **Trajectory-search EDA**: frames the problem as search over replayable traces with a density
   scheduling score `η(u) = (E[raw] + 2·P[new cell]) / E[cost]`; the intellectual template for the
   eff-ranking the shipped attack uses.
7. **scratch_k1/k2/k3**: MARL/multi-agent framing (k1, didactic), static `TOKEN=admin123` 676-alpha2
   (k2), and hop-saturating 8-post burst + deputy reserve (k3, target80 mode).

## Discussion threads (host + community signal)
- **707811 welcome**: Owen Vallis (OpenAI) + Manish Bhatt (host); goal "creative and generalizable"
   attacks; community notes the SEQUENCE is the attack, not a single call.
- **712642 evaluator update FAQ** (host): 9,000 s per phase, 15 h global, secret-scoring fix (reversible
   encodings now credited), replay is authoritative, attack.py runs once per model, private = static
   replay of your candidates. Community: old scores not rescored; submission slots wasted by broken
   harness (Raymond Brunell); requests for private-guardrail glimpse denied.
- **714340 private-LB static replay**: host explains tradeoff; **links arXiv 2402.16822 (Rainbow
   Teaming) as the diversity-algorithm reference**; community infers private guardrails may be
   slower than public (7.5 h ≈ 3×2.5 h → private replay of gpt-oss likely timed out).
- **733058 evaluator updates (staff)**: tool-call parser normalization (Gemma `{}`-wrapped calls),
   partial scores preserved on replay timeout, ~68,000 submissions, leaderboard invalidation + 2
   reruns/team by Aug 7 9am PT, and a warning against harness-specific tricks that won't transfer.
   Follow-ups: Gemma still emits doubled-brace tool calls on hop ≥ 2 (Renee, Syed Asad Ali — hooked
   generation, chat-template branch analysis); GGUF chat-template revision drift (Alex Sap);
   submission format errors for previously-working notebooks; historical-score provenance questions
   (Suzanne Crippin).
- **733345 score fluctuation**: 2–12 point swings for the same notebook (xz, Shadab Alam 10th place);
   top-1 (Adarsh) "sometimes wonder if I'm moving in the right direction"; zigiella: candidate sets
   differ run-to-run because attack.py is stochastic and wall-clock-sensitive — scorer deterministic,
   generator not. Implication: treat single-run deltas < ~5 as noise; keep best-of-PUBLIC strategy.
- **733442 exfiltration without cheating**: community confirms public scoring = literal SECRET_MARKER
   in a clean post; the secret.txt-read path is blocked by design and not the intended route; private
   board is the blind-transfer game where "stricter" actually matters.
- **734944 working note** (radiant-allomancer): payload blind spot + reasoning-channel injection; full
   analysis captured in this workspace (see writeup_radiant.txt summary in existing_solution/).

## Signals that should shape strategy
1. **Variance is real**: same-bytes reruns swing ±5 (88.515 vs 89.055 vs 84±5 band); 2–12 pt same-
   notebook fluctuation. → submit the same config multiple times, keep best; don't chase <5 pt deltas.
2. **Evaluator keeps moving**: parser fix, partial credit, leaderboard resets, artifact drift. → the
   only durable edges are primitive-level (payload blind spot, reasoning-channel forge) and
   budget-level (validation-fill, replay-safe sizing).
3. **Gemma multi-post is structurally broken** (doubled braces) → gemma row is single-post volume +
   deputy hedge only; multipost belongs on gpt-oss where the forge commits it.
4. **Private = blind transfer** → diversify predicates (deputy) and payload encodings; assume the
   private guardrail content-scans SECRET_MARKER.