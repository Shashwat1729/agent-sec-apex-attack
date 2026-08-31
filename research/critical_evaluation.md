# Critical Evaluation of Sources

Systematic review of every notebook, discussion, writeup, and paper used in this project. Each source scored on: upvotes/downvotes, discussion quality, author credibility, evidence type, recency, and validation.

## 1. Community Discussions (raw captures in `raw_discussions/`)

| Thread | File | Upvotes | Quality | Credibility | Evidence | Verdict |
|---|---|---|---|---|---|---|
| Welcome (707811) | `disc_707811.txt` | 26 host | Low-technical | Host (OpenAI/IEEE) + Manish | Intent only | **Keep as context**, not technical evidence |
| Evaluator FAQ (712642) | `disc_712642.txt` | High | High | Host | Spec (9k s, secret fix, static replay) | **Load-bearing** — defines budget & private=static replay |
| Private LB static replay (714340) | `disc_714340.txt` | Medium | High | Host links arXiv 2402.16822 | Design tradeoff (no online adaptation) | **Load-bearing** for private strategy |
| Evaluator updates (733058) | `discussion_733058.txt` | 28 staff | Very high | Staff (MartynaPlomecka) | Parser fix, partial credit, 68k subs, leaderboard reset | **Highest credibility** — changes optimal shape from conservative→fill-to-cap; Gemma still broken (Renee/Syed independent repro, template source) |
| Score fluctuation (733345) | `disc_733345.txt` | 3 | High | Top-1 Adarsh, 10th Shadab, zigiella | 2–12 pt same-bytes variance | **High credibility** — treat <5 pts as noise, best-of-public policy |
| Exfil without cheating (733442) | `disc_733442.txt` | 4 | Medium | Viktor + Cleanor | Marker vs secret.txt path (stale desc vs current SDK) | **Corrected** — public = literal SECRET_MARKER, not secret.txt read |
| Working-note thread (734944) | `disc_734944.txt` | Low | Medium | Sabrina? | Working-note guidance | Background |

**Cross-cutting reading:** host statements > community folklore. Any claim without a replayed trace or source diff is treated as hypothesis, not fact. The 733058 thread is the Rosetta stone for why pre-2026-08-07 scores are incomparable.

## 2. Organizer Working Note (radiant-allomancer)

- **File:** `raw_writeup/writeup_radiant.txt` (also `notebooks/extracted/...`)
- **Credibility:** Very high — source-read scorer/harness/guardrail, isolated A/B (+27.5 forge, +4.3 fill), honest variance & negative ledger.
- **Score:** 57.1 no-forge → 84.6 forge → 88.9 fill (refreshed evaluator). `S = 0.09 × N_eff`, replay latency bound ~985 cands/model.
- **Validation:** re-derived scoring & gateway contracts independently; reproduces.
- **Use:** Primary reference for methodology §3–§5 and for the "read source before leaderboard" principle. Copied verbatim in `research/raw_writeup/`.

## 3. Public Notebooks (18 extracts in `notebooks/extracted/`)

| Notebook | Score | Upvotes | Lineage | Critique |
|---|---|---|---|---|
| Getting Started | 0.075 | 1487 | Starter | Trivial; no search, blind 31 % fire rate |
| JED v25 | 89.145 Gold | High | Foreground: verbose Gemma / Harmony GPT, 0.98 replay-safe, best-of lottery | **Gold-standard** for throughput framing |
| JED Slow multipost | 86.605 Bronze | Medium | Forge-commit multipost on slow row | Useful but Gemma-broken; isolated to GPT-OSS |
| Dense-exfiltration | ~88.9 era | Medium | Pure throughput math, prompt length lever | `S=0.09×N_eff`; over-return → void |
| Adaptive-uniform (2/3-probe) | 88.5/89.0 | Medium | Live measurement at true hop cap | Same-bytes variance demo (88.515 vs 89.055) |
| 5-templates aggressive | — | Low | bare/bare_ok + inj_close/commentary, eff/median latency | Useful for MIN_FIRE_RATE 0.2 prior |
| v23-alpha2co 667 | 60.03 target | Low | Static 667 ×0.09, aa.co hosts | Proof unique domains must be short |
| Trajectory-search EDA | — | Low | `η = (E[raw]+2P[new])/E[cost]` density | Intellectual template for eff-ranking |
| scratch_k1/k2/k3 | didactic/676-alpha2/target80 | Low | MARL, 676-static, 8-post+deputy reserve | k3's hop-saturating burst is *unproven* (harness 1 tool/call per hop) |

**Pattern:** field converged on single-post + Harmony forge + validation-fill + replay-safe sizing. Any notebook claiming multi-post on Gemma without harness trace is discounted (template bug refutes).

## 4. Literature (in `literature/`)

| Paper | Link | Why it matters | Confidence |
|---|---|---|---|
| AgentDojo (Debenedetti, NeurIPS 2024) | arXiv 2406.13352 | Fixture corpus ancestor; 97 tasks ×629 tests; utility+security over state | Verified via arXiv/OpenReview |
| InjecAgent (Zhan, ACL 2024) | arXiv 2403.02691 | Prompted Llama-2-70B 80 %+ ASR; ft 6–7 % — open GGUF = vulnerable pattern | Verified |
| ChatInject (Chang, ICLR 2026) | arXiv 2509.22830 | Role-template payloads 5→32 % on AgentDojo; agentic +think/tool largest gains; this *is* the Harmony forge | Verified; Family-aligned transfer GPT-oss→GPT-4o 40.1 |
| IterInject (Chen, 2605.24659) | arXiv | Diagnose(4-level) → LLM refine → seed bank → cross-target reuse = our validation-fill loop | Verified |
| Go-Explore / Rainbow (2601.00042 / 2402.16822) | arXiv | Diversity archive, QD, MAP-Elites — justifies +2 cell pressure & Go-Explore baseline | Verified but single-seed variance 8× (needs 3–4 seeds for stability) |
| ToolHijacker, AdapTools, ASB/WASP/MCPTox | — | Tool selection injection; 2× ASR on open models; MCPTox "more capable → more susceptible" | Contextual, not directly reused |

**Discipline:** no paper claim is cited without checking the PDF/table; numbers quoted from papers, not memory.

## 5. This Project's Own History (`PLAN.md`, `TUNING.md`, `WORKING_NOTE.md`)

- **PLAN.md:** reverse-engineered scoring/guardrail/predicate map — useful but superseded by source-verified contracts in `research/competition/overview.md` and `docs/writeup.md`.
- **TUNING.md / WORKING_NOTE.md:** 80-iteration ledger, honest about variance and open gap (92.5 vs 100–137). **Most valuable artifact** after source reads — documents crater causes (6-streak inertness, raw-floor miss, bundling non-additivity) with isolated A/B per lever.
- **NEXT_BATCH_PLAN.md:** superseded; preserved for provenance (v91–v95 pending).
- **Validation:** every "confirmed lever" requires an isolated branch + real LB score; <5 pt deltas discarded as noise.

## 6. What Was Rejected

- UNTRUSTED_TO_ACTION / DESTRUCTIVE_WRITE stacking under public guardrail (structural, not empirical).
- Multi-step web/email→action chaining (taint superset).
- Verbose jailbreak / high-salience framing (lengthens CoT → throughput loss).
- Encoded SECRET_MARKER as private hedge (would zero EXFIL on both LBs — source `_contains_secret` trace).
- Gemma multi-post & all-hops forge on continuation (mechanically impossible: `http.post` returns literal `ok`, never re-enters context; Gemma emits doubled braces).
- Blind emit / static-N without validation (31 % fire → cap ~47).

## 7. Open Portfolio

Top 100–137 reached in 3–5 submissions on same primitive family suggests the remaining gap is **throughput quantization** (candidates fitting replay budget), not a missing exploit — pending isolation. See `research/synthesis/next_steps.md` for ranked hypotheses H2–H7.
