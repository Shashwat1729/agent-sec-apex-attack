# Search Algorithms — What the Literature Says About Attack Discovery

Source-verified summaries of the search paradigms the competition explicitly invites ("prompt search,
fuzzing, heuristic search, evolutionary algorithms, state-space exploration, trace-guided mutation,
novelty search, Go-Explore-style archive methods").

## Go-Explore (Ecoffet et al.)
- Core loop: maintain an archive of visited states → select an under-visited cell → restore to that
  state → branch (mutate) → if novel, add to archive. Return-then-explore solves hard exploration in
  sparse-reward spaces.
- **Host-adapted version: Bhatt et al., arXiv 2601.00042** "Go-Explore adapted for AI Red Team Testing"
  (30+ experimental runs on GPT-4o-mini). Load-bearing findings:
  1. **Random-seed variance dominates algorithmic parameters** — 8x outcome spread (0–16 findings
     across 5 seeds); single-seed comparisons unreliable; averaging ~3-4 seeds materially reduces
     variance.
  2. **Reward shaping consistently HARMS** — 94% exploration collapse when combined with full
     signatures (16→1 findings, 84→7 tool calls); 18 false positives with 0 verified attacks when used
     alone → rewards amplify noise, don't guide discovery.
  3. **Simple state signatures beat complex ones** — tools-only signatures discovered the most diverse
     attack types; full-intent signatures were not better.
  4. **Ensembles trade quantity for type diversity** — single enhanced agent: 5 attacks, all one type;
     ensemble: 2-3 attacks across 2+ types.
  5. All verified attacks needed causal chains: untrusted source content containing an injection →
     dangerous action. Guarded environments stopped shell chains entirely.
- Interpretation for this competition: the baseline `attacker_goexplore.py` in the SDK embodies this
  paper; the field's live validation-fill supersedes it because the **objective is replay throughput,
  not exploration breadth** — the paper's findings (rewards hurt, seed matters, simple signatures fine)
  all transfer to the "structure race" design: don't reward-shape, do average seeds, keep signatures
  cheap.

## MAP-Elites / Quality-Diversity (Mouret & Clune 2015)
- Archive = grid over a feature/behavior space; each cell keeps the highest-fitness solution found for
  that descriptor; iterate select-mutate-evaluate-insert.
- Output is a *portfolio* of diverse, high-quality solutions — exactly what a competition that scores
  `Σ severity + 2 × |unique cells|` rewards.

## Rainbow Teaming (Samvelyan et al., NeurIPS 2024 — includes host Manish Bhatt)
- arXiv 2402.16822 (the paper the host linked in the private-LB discussion, 714340, "Offline diversity
  algorithms e.g. https://arxiv.org/abs/2402.16822").
- Casts adversarial prompt generation as QD search: archive dimensions = attack style / risk category /
  prompt length; LLM-as-mutator; judge-LLM preference ranking; parent-child similarity filtering to
  preserve linguistic diversity.
- Results: hundreds of adversarial prompts per run, ASR > 90% across Llama 2/3; prompts transfer;
  SFT on them reduces later ASR to 0.3-0.7% (i.e., diversity data is also the best defense data).
- **Direct implication for us**: the score-cell diversity term is a QD objective. A MAP-Elites-style
  archive over (predicate × tool-seq × source × domain) is the principled way to cover cells — but in
  this budget regime, unique random domains already mint one new cell per candidate at zero search cost,
  so explicit QD adds little unless a new *predicate or tool sequence* dimension is reachable.

## IterInject loop (Chen et al., 2026) — see relevant_papers.md
- Optimizer + 4-level diagnostics + seed bank + failure-pattern synthesis. The state of the art for
  adaptive IPI; our live-fill is its competition-form.

## MCTS-based jailbreak search (context)
- PAIR (Chao et al.), Tree of Attacks (TAP), Crescendo (multi-turn escalation), GPTFuzzer, GCG /
  AutoDAN (white-box token optimization), ArtPrompt (ASCII art). These target *direct* jailbreaks of
  chat models rather than IPI of tool-using agents, and none of them survive contact with a **replay
  cost that is a model generation per hop** — which is why the field abandoned them for the throughput
  race.

## Synthesis: which paradigm fits this benchmark
- The scoring contract (findings from replay, budget = seconds) makes the binding constraint *latency
  per candidate on the slowest model*, not search quality. Go-Explore / QD / MCTS all consume budget on
  exploration that does not directly score.
- The winning field pattern is therefore a **degenerate Go-Explore**: archive = firing candidates, cell
  = unique domain, branch = one new message. The only search that pays is the *template/structure*
  race (12–19 structures calibrated live per model), which is a tiny MAP-Elites over template space.
- Unexplored search levers that could still matter (see synthesis/next_steps.md):
  - per-model template archives mined from *observable fixture content* (web_hop/email fixtures carry
    tool-call syntax worth borrowing),
  - multi-seed averaging for calibration decisions (per 2601.00042), and
  - keep-out lists so a slow model's full 9000s is spent on the proven-best template rather than
    re-probing variants.