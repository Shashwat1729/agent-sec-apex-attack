# Relevant Literature (source-verified 2026-08-14)

All entries below were verified against arXiv / ACL Anthology / OpenReview / project pages during this
research pass. Numbers are quoted from the papers themselves, not from memory.

## Directly related: IPI on tool-using agents

### AgentDojo — Debenedetti et al., NeurIPS 2024 Datasets & Benchmarks
- arXiv 2406.13352 / OpenReview m1YYAQjO3w. ETH Zurich SPY Lab + Invariant Labs.
- Dynamic framework, not a static suite: 97 realistic tasks, 629 security test cases, injection
  placeholders, formal utility + security checks computed over environment state (no LLM-as-judge env).
- Results: models solve < 66% of tasks even without attacks; best attacks succeed < 25% of the time;
  a secondary PI detector drops ASR to ~8%.
- Structural ancestor of this competition's fixture corpus (web / email / file content + injection nodes).
- Defense stack evaluated there (data delimiters, PI detector, prompt sandwiching, tool filter) is the
  same family the private guardrail presumably draws from.

### InjecAgent — Zhan et al., ACL 2024 Findings
- arXiv 2403.02691. UIUC Kang lab. 1,054 test cases, 17 user tools, 62 attacker tools.
- ReAct-prompted GPT-4: ASR 24% base, 47% with a "hacking prompt" (nearly 2x). Prompted Llama-2-70B
  exceeds 80%. **Fine-tuned function-calling agents are far more resilient** (GPT-4 ft 7.1% / 3.8%;
  GPT-3.5 ft 6.6%) — prompted agents are the vulnerable deployment pattern.
- Relevance: our targets are GGUF-instruct (prompted-style) models, consistent with high fire rates.

### ChatInject — Chang, Jun, Lee, ICLR 2026
- arXiv 2509.22830 / OpenReview WVhgFSKniL.
- Formats payloads as native chat-template role tokens (forged system/user) to exploit the learned
  role hierarchy; plus a Multi-turn variant embedding a persuasive 7-turn dialogue in one payload.
- ASR: AgentDojo 5.18% → 32.05%; InjecAgent 15.13% → 45.90% (52.33% multi-turn). Template payloads
  transfer across models, including closed-source.
- **Family-aligned transfer is strongest**: GPT-oss → GPT-4o 40.1; Grok-2 → Grok-3 37.0; Gemma-3 →
  Gemini-pro 10.3. "Agentic variants (+think, +tool)" amplify further — the tool-calling hook produces
  the largest swings. **This is exactly the Harmony `<|channel|>analysis<|message|>` forgery the top
  teams use on gpt-oss.**
- Mixture-of-Templates (concatenated templates) works when the backbone is unknown — lower variance than
  picking one foreign template.
- Defenses: prompt-based defenses often INCREASE ASR; detector defenses react to special tokens (so
  plain multi-turn slips through); format stripping defeated by 10% character perturbation.

### IterInject — Chen et al., arXiv 2605.24659 (2026-05)
- Feedback-guided iterative IPI optimization: closed loop inject → diagnose → refine.
- Rule-based diagnoser emits 4-level labels (SUCCESS / PARTIAL / DETECTED / IGNORED) + behavioral
  description; LLM optimizer refines payloads conditioned on full history; synthesis step evolves the
  seed bank from failure patterns; cross-target scoring reuses winning seeds.
- Results: AgentDojo highest ASR on all 4 victim models (DeepSeek 47.8% vs 32.9% static); InjecAgent
  lifts total ASR from ~0 to 33–90%; Claude Code full success on 5/9 targets.
- **Our live validation-fill is the competition realization of this loop** (probe → keep firing →
  adapt), and the seed-bank + cross-target scoring pattern maps to our per-model structure race.
- Mechanistic finding: attention amplification on payload tokens in mid-to-late layers; threshold-like
  decision boundary → inference-time attention suppression is a plausible future defense direction.

## Benchmarks / adjacent systems

- **ToolHijacker** (NDSS 2026) — prompt injection into tool *selection*; two-phase optimization.
- **AdapTools** — adaptive IPI with stealthy tool selection; ~2x ASR vs baselines on open models
  (consistent with our open GGUF targets being substantially easier than frontier models).
- **Agent Security Bench (ASB), WASP, MCPTox** — related agent-security benchmarks; MCPTox notes more
  capable models are often MORE susceptible (instruction-following amplifies attacks).
- **AgentVigil** — MCTS with generic mutation operators for IPI (baseline IterInject beats).
- **JED SDK / mbhatt1/competitionscratch** (host repo, MIT) — the exact SDK base for this competition;
  documents `aicomp evaluate/test redteam`, the attack-only workflow, and `min(1000, raw/200000*1000)`
  normalization (`= raw/200`). The Go-Explore baseline attacker shipped with the SDK is
  `attacker_goexplore.py` (analyzed in this workspace).

## Key transferable takeaways (applied to our design)

1. **Template/role abuse works on reasoning models** (ChatInject): forge completed `<channel>` turns to
   skip CoT — already the dominant lever on gpt-oss (working note: 57.1 → 84.6, +27.5).
2. **Diagnosis-driven iterative refinement beats static payloads** (IterInject, +15–80 ASR): keep the
   live validate-and-keep loop; improve failure labels where possible.
3. **Stealth = task-aligned, benign-looking legs** (IterInject disguise seeds; ChatInject persuasive
   multi-turn): our notify/email legs and "answer OK only" wrap-up are this pattern.
4. **Open/prompted models are far more vulnerable than fine-tuned/frontier ones** (InjecAgent): maximize
   raw per candidate via multi-predicate chains rather than qualifying single-primitive volume alone.
5. **Diversity is an explicit optimization axis** (Rainbow Teaming / Go-Explore / AgentDojo): the +2
   score-cell term is the benchmark's own diversity pressure — unique URL domains per candidate.