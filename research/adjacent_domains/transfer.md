# Adjacent-Domain Transfer

## Fuzzing
The competition is budgeted trace-fuzzing: mutate candidate message chains, replay each, keep only
those that survive replay and fire predicates. Classic fuzzing lessons transfer: input-length control
(shorter prompts = faster replay = more candidates — the field's #1 lever), targeted seed corpora
(here: one verified primitive + structure variants), and coverage guidance (here: the +2 score-cell
term replaces coverage as the diversity signal).

## Quality-Diversity / MAP-Elites
Rainbow Teaming (arXiv 2402.16822, host co-author) framed adversarial-prompt generation as QD search
over an archive grid (attack style × risk category × length) with an LLM mutator + judge ranking.
Transfers here as the *template/structure race*: a tiny archive over
(template × payload × ending), ranked by `(raw × fire_rate) / replay_cost`. Explicit QD over tool
sequences is unnecessary because unique random domains already mint one new cell per candidate at zero
search cost — unless a new *predicate or tool-sequence* dimension becomes reachable (H5/H2).

## Evolutionary search / novelty search
Go-Explore (host paper 2601.00042): archive-and-restore exploration; findings transfer as cautions —
(a) reward shaping hurts (don't give intermediate bonuses; validate-and-keep instead), (b) seed
variance dominates (average several probes before trusting a calibration), (c) simple state signatures
win (our score-cell key is already minimal), (d) ensembles diversify (per-model structure race is an
ensemble over templates).

## Adversarial ML / jailbreak search
PAIR, TAP, Crescendo, GPTFuzzer target direct chat-model jailbreaks and assume cheap scoring per
candidate; here each candidate costs a full replay (model generation per hop), which is why those
methods don't transfer — the memory-jailbreak parallel is limited to the *one-shot* primitives
(GA/token-level mutation is prohibitively expensive at ~20 s/candidate on gpt-oss).

## Security operations / provenance analysis
Read the guardrail as a taint-tracking dataflow policy: sinks = {fs.delete, fs.write, shell.run,
http.post, email.send}, sources = web/email, window = 5 events. Predicate windows (2 events) must be
kept inside the *search*, not the guardrail — the winning primitive is a sink whose payload is never a
sensitive *keyword* (so the arg check passes) yet is a recognized *secret* (so the scorer fires). This
destination-vs-payload blind spot is the benchmark's single most important design fact, and the working
note's proposed fix (content policy on every outbound argument / data-flow checks) is the likely shape
of the private guardrail — hence the deputy + encoded-payload hedges.

## Reinforcement learning
The environment resembles a one-step contextual bandit with a hard wall-clock budget: the "policy" is
the candidate generator, the "reward" is fire-rate × raw, and the horizon is seconds, not episodes.
The field's validation-fill is exactly an on-policy REINFORCE-style loop (keep what fired, discard the
rest) — already optimal for the constraint. The only RL lesson still untapped is exploration under
non-stationarity (evaluator/parser/artifact churn → re-calibrate per run, seeded variance → best-of-N
submissions).