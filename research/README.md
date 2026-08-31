# Research Index

Competition analysis for **AI Agent Security - Multi-Step Tool Attacks**
(research-only; no changes to `submission/attack.py`).

## Contents
- `competition/overview.md` — benchmark, scoring formulas, guardrails, runtime contract, measured frontier
- `existing_solution/field_landscape.md` — field consensus, the 47→90 mechanism, negative results ledger
- `kaggle/public_notebooks.md` — notebook lineage, code-tab snapshot, discussion-thread signals
- `literature/relevant_papers.md` — source-verified papers (AgentDojo, InjecAgent, ChatInject, IterInject, ...)
- `literature/search_algorithms.md` — Go-Explore 2601.00042, MAP-Elites, Rainbow Teaming 2402.16822
- `techniques/attack_primitives.md` — confirmed primitives and the structure race
- `adjacent_domains/transfer.md` — fuzzing / QD / adversarial-ML lenses
- `synthesis/next_steps.md` — ranked unexplored hypotheses (H1–H7), dead ends, private-LB strategy

## Raw evidence (this workspace)
- `notebook_markdown_dump.txt` — extracted public notebook markdown cells
- `../notebooks/extracted/*.txt` — 18 full public notebook extracts
- `../disc_*.txt`, `../discussion_733058.txt`, `../rules_page.txt`, `../code_tab.txt` — browser-captured pages
- `../writeup_radiant.txt` — organizer working note (57.1 → 84.6 → 88.9 with full negative-results ledger)
- `../PLAN.md`, `../TUNING.md` — our own reverse-engineering and tuning history (v34 = 87.075 best)