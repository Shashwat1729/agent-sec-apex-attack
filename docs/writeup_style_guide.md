# Kaggle Winning Writeup Style Guide — for WORKING_NOTE.md

*For D:\personal\hackathon\agent-sec — distilled from 9 winning writeups + official guidelines to earn Working Note awards (clarity, usefulness, reproducibility).*

## Sources (critical evaluation)

| Source | Cred / recency | What it contributed |
|---|---|---|
| **Kaggle Winning Model Documentation Guidelines** | **Canonical** — normative for prize-eligible ranks. Defines A1–A9 + B1–B8. | Required skeleton: 4–6-sentence Summary (A3), Features, Methods, Findings, Simple baseline, Execution time, References + bundle (README, requirements, SETTINGS.json, entry_points). |
| **IEEE Fraud 1st — Deotte/Konstantin (disc. 111284/111308)** | ~500+ votes, 6,381 teams, 2019. Grandmaster, still the narrative archetype. | Story spine: EDA → "not time — clients" → UID `card1+addr1+D1` → 6-line `groupby` code → time-consistency feature filter → GroupKFold → ensemble/post-process. Pie + timeline plots inline. |
| **Benetech 2nd — hallstatt** | Recent (2023), Matcha backbone. | Figure-first pipeline, 700k synthetic-plot table, hyperparams + `A.Compose` code block. |
| **WiDS 2026 2nd — btt_mapping** | Very recent (2026-05), hybrid 0.97272. | 3-stage survival pipeline, Nelder-Mead blend weights, Platt/isotonic calibration, cells 15/19/20/21 reproducibility. |
| **IEEE 5th/13th/15th/40th + Rossmann 1st (Gert)** | 4–40th illustrate variance; Rossmann 3,738 teams | Honest ensembles, "what didn''t work," adversarial AUC 0.999, holdout must mimic time split. |
| **Gabruseva "Writing papers after Kaggle" (2020)** + **NVIDIA IEEE blog (2021)** + **ML Journey (2025-11)** | Meta-guides; lower weight (not winners) | Tech-report upgrade: ablation with fixed seeds, dataset graphs, training curves; visual hierarchy, TOC, explain-why comments. |

**Pattern:** winners *narrate one insight per section*, then *prove* with table + plot + runnable fence. Low-award notes list actions.

---

## 1. Structure template (12 sections — merges A1–A9 with Agent-Sec needs)

```
0. Title block — authors, competition link, best single (v64 92.540), code link
1. TL;DR box (4–6 sentences, A3) — what, why, score, repo link
2. Context — threat model + fixtures + task envelope
3. Overview — 4-row pillar table (what/why)
4. Data & environment — fixtures, budgets, hardware
5. Methodology — one subsection per lever (idea → fence → isolated Δ)
6. Validation — local harness + what it cannot check + private hedge
7. Experiments — climb + craters + marginal tables + ablation plot
8. What didn''t work — families with isolated A/B
9. Insights & defenses — for builders + benchmark designers + self-test
10. Responsible & limitations — variance, infra, gap to 100+
11. Sources — papers, SDK/gateway pin, discussions, notebooks
12. Appendices — A runnable samples  B checklist & exact bash
```

Length: winners cluster 2,500–5,500 words. WORKING_NOTE.md is 570 lines ≈3,800 words — in range. >6k loses reviewers; <1.5k fails A4–A6. Headings: `#` once, `##` for 12 sections, `###` for levers, `####` only for probes. Never skip a level.

---

## 2. Formatting checklist

### Tables — when/how

**Use only for:** ledgers, ablations, bucket defs, knob refs, reachability. Never for prose.

- One header row, no merged cells (Kaggle breaks them).
- Deltas as `+x.xx isolated` with control (`v8→v22`); flag noise (`<5 pts noise` [733345]).
- 4–8 rows; >10 rows move to `docs/experiments.md` and link.
- Caption *above* table: `*Table 1 — Isolated levers (real public).*`

```markdown
*Table 1 — Climb 60.7→92.54 (isolated branches).*

| Phase | Lever | Evidence | Δ |
|---|---|---|---|
| Forge | Harmony token injection | v8 78.5 → v22 82.5 | **+27.5** |
| v51→v64 | Multi-post N=5 (`forge5`) | 91.38 → 92.54 | +1.16 |
```

### Plots/graphs — types, placement, captions

| Place | Type | Why winners use it | Caption |
|---|---|---|---|
| §2 | Pipeline diagram (sandbox→guardrail→scoring) | Every 1st-place opens with it; reviewers skim first | `Figure 1: Pipeline — … Thickness=wall-clock.` |
| §3/5 | Guardrail trace (first-arg vs payload) | Makes blind-spot falsifiable | `Figure 2: Guardrail — `data` never inspected.` |
| §7 | Score progression v2→v64 (line + crater labels) | Shows levers + craters; IEEE 1st uses 3 such | `Figure 4: Progression — <5 pts noise.` |
| §7 | Ablation bar N=4/5/6 | Proves ceiling | `Figure 3: Ablation — N=5 boundary.` |
| §4 | Fixture/class histogram | One plot per "aha" (Rossmann/IEEE) | Include n= and zero-spike note |

Image rules: PNG ≤1200px, DPI ≥150, colorblind-safe (no red/green alone), grid `alpha=0.3`. Each `![Figure N: …](assets/…)` on its own line + one-sentence interpretation after ("Notice …"). Alt text restates insight, not filename. Keep 3–5 figures; >8 is paper bloat (Gabruseva).

### Other formatting

- **Code fences:** 10–25 lines, runnable Python, `# Expected:` comment. Explain *why* not *what* (ML Journey excellent vs mediocre example). Required for guardrail test, `rescore()`, `fill_should_keep()`.
- **Math:** inline `$S = \text{raw}/200$`; display block for `E[\text{raw}]`.
- **Bullets vs prose:** bullets for pillars/knobs/checklists; prose for failure diagnosis.
- **Links:** pin gateway date + IDs `[733058](url)`, not bare URLs.
- **TOC:** auto-TOC after TL;DR (you exceed 1000 lines).

---

## 3. Example snippets (copy-paste)

**Figure + interpretation:**
```markdown
![Figure 2: Guardrail — clean `http.post` ALLOW vs `web→post` DENY.](assets/guardrail.png)

*Figure 2 — taint window (5) ⊃ predicate window (2) → UNTRUSTED unreachable; same check misses `data`.*
```

**Guardrail self-test (IEEE 1st pattern — 10 lines, no GPU):**
```markdown
```python
from aicomp_sdk.guardrails.optimal import Guardrail
g = Guardrail()
assert g.decide("http.post", {"url": "http://ab.co", "data": "SECRET_MARKER"}, {"recent_sources": []}).action == "ALLOW"
assert g.decide("http.post", {"url": "http://ab.co", "data": "SECRET_MARKER"}, {"recent_sources": ["web"]}).action == "DENY"
```
```

**Variance honesty (15th-place style):**
```markdown
> Single-run deltas <5 pts are noise (field 2–12 pts, [733345](…)). All below are isolated single-variable branches.
```

---

## 4. Common pitfalls (reviewer penalties)

1. **Listing, not narrating** — 20 subs without isolated Δ. Winners show 4–6 levers.
2. **Untruncated mock scores** — replaying 2000 cands in-process inflates ~6×. Truncate `REAL_REPLAY_CEILING=150` and label proxy.
3. **Encoding the marker** — `base64(SECRET_MARKER)` scores 0; decode only for `fs.read` values.
4. **Random split on temporal data** — must use time-based GroupKFold (Rossmann/NVIDIA).
5. **Tables without Δ, plots without captions** — #1 reproducibility feedback.
6. **Moonshot bundles** — 3 ideas together hide signal; submit halves alongside combo.
7. **Missing "what didn''t work"** — A6 requires it; omit = "not insightful."
8. **Silent control tokens** — not flagging `<|end|>` injection troubles safety reviewers.

---

## 5. 10-point quality checklist (gate before submit)

- [ ] **Heads:** `#` once, `##` ×12, hierarchy intact; TOC anchors work.
- [ ] **TL;DR 4–6 sentences** with score + code link (A3) at top.
- [ ] **Pillar table (§2) + isolated-Δ table (§7)** with caption above, Δ col, noise note.
- [ ] **3–5 figures** each `Figure N: …` caption, colorblind palette, interpretation sentence.
- [ ] **Every claim has fence + score** (or `PENDING` range) — no prose-only claims.
- [ ] **Validation §:** 5 local checks + 3 things local cannot check + private hedge.
- [ ] **Failures §:** ≥3 families with real Δ and diagnosis.
- [ ] **Reproducibility §:** hardware, pinned GGUF/date, requirements, SETTINGS.json, entry_points, exact bash 1→6.
- [ ] **Sources §:** SDK pin + gateway date + ≥4 discussions + ≥3 papers with links.
- [ ] **Word/lint:** 2.5k–5.5k words, no bare URLs, no red/green plots, `local_test.py` 5/5 PASS linked.

*Any unchecked box → not award-ready.*
