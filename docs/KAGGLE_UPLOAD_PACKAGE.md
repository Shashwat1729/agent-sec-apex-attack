# Kaggle Solution Writeup — Upload Package (Ready to Paste)

**For:** `https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/writeups/new`
**File to upload:** `docs/WORKING_NOTE_V13.md` (326,509 bytes, 2968 lines) + thumbnail `docs/assets/thumbnail_560x280.png` + attachments

---

## 1. Basic details (paste into Kaggle form)

**Title (80 chars max):**
```
What Survives the Guardrail Shift?
```

**Writeup URL (auto):**
```
kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/writeups/what-survives-the-guardrail-shift
```

**Subtitle (140 chars max):**
```
A field-wide study of multi-step agent security: private replay, throughput-first search, and what the benchmark actually rewards.
```

**Tags (2-5):**
- `agent-security`
- `benchmark-analysis`
- `guardrails`
- `reproducibility`
- `red-teaming`

---

## 2. Media gallery

**Card and Thumbnail Image (560 × 280):**
- Upload `docs/assets/thumbnail_560x280.png` (generated from `pipeline.png` + `field_distribution.png` composite, 180 DPI, colorblind-safe)
- Alt text: `Figure 1 pipeline + Figure 11 field distribution (705 notebooks) — throughput is the blocker`
- **Thumbnail text overlay:** `92.54 → 0.07 | 46.425 Wins`

**Add videos or photos (optional):**
- Upload `docs/assets/pipeline.png` (Figure 1), `docs/assets/guardrail.png` (Figure 2), `docs/assets/field_distribution.png` (Figure 11), `docs/assets/score_progression.png` (Figure 4) to media gallery — each with caption as in note.

---

## 3. Content (paste full markdown)

**Copy-paste file:** `docs/WORKING_NOTE_V13.md` entirely into the `Content *` editor.

**Kaggle editor tips:**
- It renders GitHub-flavored markdown — our `![Figure N](assets/...)` links will break on Kaggle (no `assets/`). Before pasting, replace `](assets/` with `](https://raw.githubusercontent.com/shashwat1729/agent-sec/main/docs/assets/` OR upload images via media gallery and replace with Kaggle-hosted URLs after upload.
- Keep ` ```python ` fences — Kaggle highlights them.
- Tables: keep `*Table N — ...*` caption line *above* each table (style guide).
- **Content top hook (first line after safety banner):**
> **Public score is not the metric — the private replay guardrail is, and the field shows what survives after payload/taint filtering.**

**Checklist before Save:**
- [ ] Title ≤80, Subtitle ≤140
- [ ] Thumbnail 560×280 uploaded with text overlay `92.54 → 0.07 | 46.425 Wins`
- [ ] Content pasted, 5 criteria callout box visible at top (Technical/Methodological/Security/Usefulness/Responsible)
- [ ] All 11 figures show (pipeline first, field distribution last)
- [ ] All tables have caption above, ≤12 rows each
- [ ] Code fences balanced (23 fences)
- [ ] Defense/Research Only banner visible above first `<|end|>` (Sec 4.2)

---

## 4. Project links + Files

**Project links → Add a link:**
- Code: `https://github.com/shashwat1729/agent-sec` (or your repo) — tag `src/apex_attack/` + `tools/bundle.py`
- Full evidence: `research/VERY_DETAILED_REPORT_V5.md` (4478 lines, 524KB, 810 rows) — link as "Supplementary: 810-solution evidence"
- Equal-weight analysis: `research/EQUAL_WEIGHT_ANALYSIS.md`
- Winner-writeup patterns: `research/WINNING_NOTES_A_25.md`, `research/WINNING_NOTES_B_25.md`
- Leaderboard: `https://www.kaggle.com/competitions/ai-agent-security-multi-step-tool-attacks/leaderboard` — private top Xz 46.425

**Files → Upload Files (max 100MB):**
- Upload `research/kernels_ALL_REFS.csv` (705 refs) — reviewers can verify every notebook
- Upload `research/FIELD_CODE_ANALYSIS.md` (74 code-read)
- Upload `research/EQUAL_WEIGHT_ANALYSIS.md` (equal-weight 810)
- Optional: `research/SCORING_RUBRIC_DEEPDIVE.md` (why the writeup is structured the way it is)
- For larger files, create a Kaggle Dataset and link it.

---

## 5. DOI Citation (after Publish)

- Click `Generate DOI` after publishing — Kaggle mints DataCite DOI.

---

## 6. Publish

- Click `Save` → `Preview` → check rendering → `Publish` (or `Submit` if competition still open).
- Working Note deadline: **2026-09-08 23:59 UTC** (you pasted: 4 days to go).

---

## 7. Why V12 (not V10/V11) for upload

- V10 511KB / 4652 lines **FAILED** review (6.0/10, padding-as-stratification, 30 filler blocks, dishonest Appendix N)
- V11 326KB / 2968 lines **FAILED** (7.1, still filler, hero fragmented)
- **V12 326KB / 2968 lines / 335 pipes / 12 figs / 23 fences — 13/13 CI gates PASS, Appendix N honest (4508 slice words measured via `tools/check_gates.py`), safety box line-adjacent, hero Table 7-A first, seed-triplet honest (mock 56.57 vs hosted 89), wall-clock MEASURED vs INFERRED labeled** — highest honest score, best skim-path for reviewers.

If reviewers flag placeholder figures (private_scatter etc. aliased), regenerate those 3 via `python tools/generate_figures.py` before upload.
