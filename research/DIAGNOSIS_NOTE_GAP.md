# DIAGNOSIS: Why research/ Has All Notebooks Data but docs/WORKING_NOTE_V5.md Does Not

**Date:** 2026-09-06
**Scope:** D:/personal/hackathon/agent-sec — research/ vs docs/WORKING_NOTE_V5.md (V5: The Full Field - 705 Notebooks)
**Sources read:** research/VERY_DETAILED_REPORT_V5.md (headers), docs/WORKING_NOTE_V5.md (headers), research/FIELD_CODE_ANALYSIS.md (full 139 lines), docs/writeup_style_guide.md (full 136 lines)
**Verdict:** Gap is intentional condensation under judging gates, not data loss. All 705 refs are accounted for; 74 code-read live verbatim in research/, only top-20 HELPED + banded pointers survive into the Note.

---

## 1. TL;DR

- research/ holds everything: 4477-line V5 report (537036 bytes, 74535 words), FIELD_CODE_ANALYSIS.md 139 lines with 75 technique rows (60 top60 + 15 vote15, incl 1 ERROR), kernels_ALL_REFS.csv 706 lines (header + 705 refs), field_code/top60 (60 pulls) + vote15 pulls (~2.02 MB across 74 notebooks).
- WORKING_NOTE_V5.md (3120 lines via Count, 42921 words, 294584 bytes) condenses to Section 23 (23.1 top-20 HELPED split 10+10, 23.2 family tally, 23.3 three tail examples + title-only family list, 23.4 combined-810 synthesis) + Appendices V5-A..V5-O (banded pointers, mini-tables, fetch method, pull manifest in 12-row chunks).
- Seven gates force the cut: (1) length gate, (2) table-row cap, (3) missing scores for 630, (4) HURT=0 focus, (5) readability tradeoff, (6) appendix pointer, (7) figure budget. Each is documented below with file:line evidence.

---

## 2. Root causes (all 7 required)

### RC1 — Length gate (style guide 2.5-5.5k words; >6k loses reviewers)
- Guide: docs/writeup_style_guide.md:38 — Length: winners cluster 2500-5500 words. WORKING_NOTE.md is 570 lines ~3800 words — in range. >6k loses reviewers; <1.5k fails A4-A6.
- Note already violates it: WORKING_NOTE_V5.md = 3120 lines (.Count), 42921 words (Measure-Object), 294584 bytes. Report V5 = 4477 lines, 74535 words, 537036 bytes. Both are ~8-13x over the award window.
- Consequence: V5 header docs/WORKING_NOTE_V5.md:32-35 explicitly states base 22 sections byte-identical, only Section 23 + V5-A..V5-L added. Full 74-row technique tables deliberately left at research/VERY_DETAILED_REPORT_V5.md:3290-3428 per docs/WORKING_NOTE_V5.md:18 and docs/WORKING_NOTE_V5.md:2515-2518. Verbatim repetition of 74 rows (~90 lines in FIELD_CODE_ANALYSIS.md:11-94) would add ~8-10k words and guarantee reviewer skim-penalty.
- Evidence: guide checklist docs/writeup_style_guide.md:134 — Word/lint: 2.5k-5.5k words. Note is 42921 words = 7.8x cap.

### RC2 — Table-row cap (4-8 rows; >10 rows move out)
- Guide: docs/writeup_style_guide.md:50 — 4-8 rows; >10 rows move to docs/experiments.md and link. Also docs/writeup_style_guide.md:44-46 — Use only for ledgers, ablations, bucket defs, knob refs, reachability. Never for prose.
- Note obeys it: Section 23 splits top-20 HELPED into two 10-row tables (Table 23-A part 1 of 2 VERBATIM-score forge/probe lineage + part 2 of 2 sizing/guardrail/deputy, docs/WORKING_NOTE_V5.md:2515-2550). Family tally Table 23-B has 6 rows (docs/WORKING_NOTE_V5.md:2551+). Tail Table 23-C has 3 rows (docs/WORKING_NOTE_V5.md:2568+). Combined Table 23-D has 5 rows (docs/WORKING_NOTE_V5.md:2582+). Appendices chunk everything else at 8-12 rows: V5-C1 8 rows, V5-C2 7 rows, V5-H1..H6 12 rows each, V5-K 12 rows, V5-K1/K2 9 rows, V5-K3 8 rows (docs/WORKING_NOTE_V5.md:2785-3036).
- Full 74 cannot fit: FIELD_CODE_ANALYSIS.md (A) 60 rows + (A2) 15 rows = 75 technique rows. Report V5 holds them verbatim; Note points instead (see RC6).
- Evidence: Note carries 968 pipe-table lines total but no single table exceeds 12 rows by design; grep Table V5-H1..H7 / V5-K1..K3 captions all state (caption above, N rows).

### RC3 — Missing scores for 630 (metadata-only tail has no Kaggle-verified delta)
- Field: research/FIELD_CODE_ANALYSIS.md:120-133 — 74 code-read (59 top60 + 15 vote15) + 1 ERROR (rank 54) + 630 metadata-only = 705 total. Band stats: 645 rows at rank 61-705 hold 5580 total votes; the 15 highest-voted in-band rows are exactly V1-V15, so unpulled 630-row tail is long-tail low-vote material.
- Why unscoreable: docs/WORKING_NOTE_V5.md:2568-2580 (23.3) + Appendix V5-E/V5-K — full ref/title/author/votes/lastRunTime for all 630 in research/kernels_ALL_REFS.csv sortRank 61-705; nothing below is code-read. Title-embedded numbers (95.130, 66.015, 60.525, 60.435, 22.155) are author self-claims, NOT Kaggle-verified; pre-refresh frozen scores (freeze 2026-08-07 per disc 733058) not comparable to post-refresh or private-era September scores (research/KERNELS_FULL_INVENTORY.md:9-11).
- Consequence: Note gives tail only Table V5-B band summary (100-rank bands) + 3 bad/stale teachers (rank 61 July sweep stub, rank 275 Go-Explore once-in-705, rank 54 ERROR 400) + title-only family list (Hermes/OpenClaw, ducnamphan JED v0-v21, tkhanna96 H006, pengwang91 K-series, verise6211 persona/pilk, musnet Go-Explore, cdeotte final-cd5 rank 178, aleaiest cdrole-adaptive rank 161, xiaoz259 CD final rank 117). No per-row technique verdict possible without code.
- Evidence: 630 rows have votes but 0 bytes pulled, 0 VERBATIM scores, 0 guard/payload labels vs 74 code-read with bytes/payload/guard/verdict per row.

### RC4 — HURT=0 focus (field contributes no ledger-HURT; all 38 HURT are ours)
- Field: research/FIELD_CODE_ANALYSIS.md:109-111 — Verdict totals: HELPED 24 (22 top60 + V3,V4), NEUTRAL 50, HURT 0, ERROR 1. HURT is 0 because no pulled field notebook matches a ledger-confirmed regression; our HURT cases (encoded-marker hedge I_b64/N_b64, forge7/forge8 v72/v73) came from our own ablations, not field code.
- Note scope line docs/WORKING_NOTE_V5.md:8 — 810 weighted (ours 105 + field 705: 74 code-read + 630 metadata-only + 1 ERROR = 49 helped / 38 hurt / 722 neutral / 1 error). Field verdicts HELPED 24 / NEUTRAL 680 (50 code + 630 tail) / HURT 0 / ERROR 1; ours 25/38/42/0.
- Consequence: Section 23.4 top-15 hurt across BOTH are all ours (D1 v10 lean -30 through D15 v31 trust-skip; docs/WORKING_NOTE_V5.md:2582+ synthesis paragraph). Field cautionary mirrors (rank 6 public-only max-fill 95.130 pub / 0.00 priv, wrong-payload TOKEN 3-ways rank 60/V5/V8, 11 opaque blobs ALLOW-star) stay NEUTRAL by definition, not ledger-HURT. A reader expecting bad-notebook autopsies finds only 3 stale-tail teachers.
- Evidence: payload split FIELD_CODE_ANALYSIS.md:112-116 — literal 54, opaque b64 11, benign-email CD-only 2, wrong-payload TOKEN 3, starter 1, destructive-demo 1, harness 1, diary 1; guard ALLOW 62, ALLOW-star 12, ERROR 1. Optimal never DENYs clean-URL post in this set — no negative-transfer example to promote.

### RC5 — Readability tradeoff (narrate one insight per section, not list 75)
- Guide: docs/writeup_style_guide.md:17 — Pattern: winners narrate one insight per section, then prove with table + plot + runnable fence. Low-award notes list actions. Pitfall docs/writeup_style_guide.md:111 — Listing, not narrating — 20 subs without isolated delta. Winners show 4-6 levers.
- Note obeys it: V5 delta paragraph docs/WORKING_NOTE_V5.md:18 — No field notebook contradicts v64 pool; 24 support it. 23.2 collapses 74 rows to 6 buckets (single-post 17, forge 7, multi-post 11, other 39, CD-hedge 5, wrong-payload 3) each with one proves-lesson + VERBATIM-score proof (e.g. single-post holds 6 of 9 VERBATIM 85-89; forge holds top two 90.54/89.145; multi-post cautionary rank 6 0.00-private).
- Consequence: remaining 4 HELPED outside top-20 collapsed to one sentence (rank 38 working-note, rank 56 guardrail-modeling twin, V3 replay-dense ancestor, V4 suppression probe); other 50 NEUTRAL collapsed to parenthetical (opaque b64 unverified, stale sweeps, resubmits, forks, harness, starter, diary) + 1 ERROR. Full per-row why-column lives only in FIELD_CODE_ANALYSIS.md:11-94.
- Evidence: Note Section 23.1 condensed-table pointer sentence explicitly says full technique rows live verbatim in report V5 + FIELD_CODE_ANALYSIS lines (docs/WORKING_NOTE_V5.md:2515-2518).

### RC6 — Appendix pointer (full data exists, linked not repeated)
- Note: docs/WORKING_NOTE_V5.md:11 — Full 105-row matrix lives in research/VERY_DETAILED_REPORT_V4.md:2622-2730 (Tables W-A..W-D) and is condensed — not repeated — in Section 22.1. Same pattern for field: docs/WORKING_NOTE_V5.md:18 — Full 74-row technique tables live in research/VERY_DETAILED_REPORT_V5.md:3290-3428.
- V5 appendices are pointers, not reprints: V5-A all-74 detailed index, V5-B tail band summary, V5-C V1-V15 mini-tables (8+7), V5-D cross-ref index, V5-E fetch method, V5-F designer guidance, V5-G reproduce fences, V5-H pull manifest rows 1-75 in 12-row chunks, V5-K 630-tail pointer by 25-rank bands (12+9+9+8 rows), V5-M figure reuse map, V5-N scoring-math example, V5-O next-read queue, V5 verification table (docs/WORKING_NOTE_V5.md:2614-3118).
- Evidence: grep V5-A..V5-O in Note returns ~40 hits; Appendix M/N/P/Q (V4-era 105-ledger, cross-ref, Q reprints capped at 8 lines each, R transcripts) already occupy docs/WORKING_NOTE_V5.md:1920-2506 before Section 23 even starts.

### RC7 — Figure budget (3-5 figures; >8 is paper bloat; V5 reuses 10, adds 0)
- Guide: docs/writeup_style_guide.md:72-73 — Keep 3-5 figures; >8 is paper bloat (Gabruseva). Image rules PNG <=1200px, DPI >=150, colorblind-safe, grid alpha=0.3. Each Figure N caption + one-sentence interpretation. Checklist docs/writeup_style_guide.md:128 — 3-5 figures each Figure N caption.
- Note: 10 figures already (pipeline, guardrail, ablation, score_progression, taint_window, wallclock, private_scatter, per_structure_bar, per_day_timeline, + Figure 10 reuse of score_progression for HELPED/HURT; docs/WORKING_NOTE_V5.md:75-200 + Appendix V5-M docs/WORKING_NOTE_V5.md:3042+). Section 23 intro states Figures in this section are the 10 existing base figures reused, not duplicated (docs/WORKING_NOTE_V5.md:2507-2514). Appendix V5-M Figure reuse map lists 10 existing, no duplicates.
- Consequence: no distribution figure (votes vs rank, family share, VERBATIM-score histogram), no family matrix heatmap, no tail-coverage map — all deferred to V6. Field evidence therefore reads as tables-only.
- Evidence: Select-String Figure N in Note = 40 hits (captions + interpretations + reuse map); !Figure image embeds = 10 (all assets/*.png from base sections).

---

## 3. Evidence (counts)

| Item | Count | Source |
|---|---|---|
| Report V5 lines / words / bytes | 4477 / 74535 / 537036 | .Count + Measure-Object Word/Character; Get-Item Length |
| Note V5 lines (.Count) / words / bytes | 3120 / 42921 / 294584 | .Count + Measure-Object; Get-Item Length |
| Field analysis lines / words / bytes | 139 / 2624 / 17155 | FIELD_CODE_ANALYSIS.md full read |
| kernels_ALL_REFS rows | 706 (header + 705 refs) | kernels_ALL_REFS.csv .Count |
| Field pulls attempted / succeeded / failed | 75 / 74 / 1 (rank 54 quan0095 400) | FIELD_CODE_ANALYSIS.md:137 |
| Technique rows written | 75 (60 + 15 incl 1 ERROR) | FIELD_CODE_ANALYSIS.md:138 |
| Metadata-only rows | 630 (ranks 61-705 minus 15 baselines) | FIELD_CODE_ANALYSIS.md:138; Note Sec 23.3 |
| Field coverage | 705/705 accounted, 0 dropped | FIELD_CODE_ANALYSIS.md:139 |
| Code bytes across 74 | ~2.02 MB (largest V6 EDA 189495, V3 replay-dense 106695) | FIELD_CODE_ANALYSIS.md:121; Note 23.1 |
| Field verdicts | HELPED 24 (22 top60 + V3,V4) / NEUTRAL 50 / HURT 0 / ERROR 1 | FIELD_CODE_ANALYSIS.md:109 |
| Combined 810 | 49 helped / 38 hurt / 722 neutral / 1 error | Note docs/WORKING_NOTE_V5.md:8; Sec 23.4 Table 23-D |
| Ours 105 | 25 / 38 / 42 / 0; 97 COMPLETE + 8 ERROR; refs 55250029-55946443 | Note Sec 23.4 Table 23-D |
| Payload split (74) | literal 54, opaque b64 11, benign-email CD-only 2, wrong-payload TOKEN 3, starter 1, destructive-demo 1, harness 1, diary 1 | FIELD_CODE_ANALYSIS.md:112-114 |
| Guard split (74+1) | ALLOW 62, ALLOW-star 12 (blob inner unverified), ERROR n/a 1 | FIELD_CODE_ANALYSIS.md:115-116 |
| Family buckets (74+1) | single-post 17, forge 7, multi-post 11, other 39, ERROR 1 | FIELD_CODE_ANALYSIS.md:101-107; Note Table 23-B |
| Note pipe-table lines | 968 | Select-String ^\\| count |
| Note figures (embeds) / Figure-N mentions | 10 embeds / 40 mentions | Select-String ^!\\[Figure + Figure \\d |
| Style caps | 2500-5500 words; tables 4-8 rows (>10 move out); figures 3-5 (>8 bloat) | writeup_style_guide.md:38,50,72 |
| Full-data pointers | 105-row Tables W-A..W-D report V4:2622-2730; 74-row report V5:3290-3428; FIELD_CODE_ANALYSIS:11-94 | Note docs/WORKING_NOTE_V5.md:11,18 |

Key file:line anchors: Note scope docs/WORKING_NOTE_V5.md:8; V5 delta docs/WORKING_NOTE_V5.md:18; length/table/figure caps writeup_style_guide.md:38,50,72; field verdicts FIELD_CODE_ANALYSIS.md:109-116; coverage FIELD_CODE_ANALYSIS.md:137-139; Sec 23 condensed pointer docs/WORKING_NOTE_V5.md:2515-2518; family/Figure-reuse/verification docs/WORKING_NOTE_V5.md:2551-2580,3042-3118.

---

## 4. V6 fix plan for 1st-position target (stratified appendix, no base-section churn)

Goal: keep base 23 sections byte-identical (award readability), add one stratified V6 appendix block that a judge can verify in 5 minutes and an auditor can exhaust in 30. All counts below are build-time PASS/FAIL checkable.

### V6-A — Stratified appendix with full 74 (not top-20 only)
- Reprint all 74 code-read rows stratified by bucket (single-post 17, forge 7, multi-post 11, other 39) + 1 ERROR, 12 rows per table max (reuse V5-H chunk pattern). Each row: rank/ref/votes/bytes/family/payload/guard/verdict + FIELD_CODE_ANALYSIS line pointer. Source verbatim: FIELD_CODE_ANALYSIS.md:11-94 + report V5:3290-3428. This closes RC2/RC6 without touching Section 23 narrative.
- Acceptance: 74 + 1 ERROR rows present, 0 refs dropped vs kernels_ALL_REFS.csv; every row carries file:line.

### V6-B — 630 banded (25-rank bands with vote sums + stale flags)
- Extend V5-K pattern: 630 rows in 25-rank bands (61-85 … 686-705, ~26 bands, 8-9 rows per table), each band: rank-range, n, vote-sum, top-title example, stale flag (pre-refresh 2026-08-07 / July fill-era / September private-era). Full ref/title/author/votes/lastRunTime stays in kernels_ALL_REFS.csv sortRank 61-705; appendix carries band aggregates + 3-row teacher per 100-rank block (keep current 61/275/54 teachers, add one CD-final per block: rank 117 xiaoz259, 161 aleaiest, 178 cdeotte). This closes RC3 honestly: banded metadata, no fake per-row verdicts.
- Acceptance: band n sums to 630; vote sums reconcile to 5580 tail total (FIELD_CODE_ANALYSIS.md:127-128); title-claim numbers labeled CLAIM not VERBATIM.

### V6-C — Distribution figure (new Figure 11, first new figure since base 10)
- One PNG assets/field_distribution.png (<=1200px, 150+ DPI, colorblind-safe, grid alpha 0.3): (a) votes vs scoreDescending rank (log-y, annotate V1-V15 + rank 54 ERROR), (b) inset family share pie (17/7/11/39/1), (c) inset VERBATIM-score histogram (85-91 band, 9 scores). Caption + one-sentence interpretation per guide. Reuse map becomes V6-M (11 figures, still no duplicates). This closes RC7 within budget (11 total, justified as field-coverage proof).
- Acceptance: Figure 11 caption + interpretation present; alt text restates insight; data table behind plot committed as research/field_distribution_source.csv.

### V6-D — Family matrix (technique x evidence, 1st-place transfer read)
- One 6x4 matrix (rows: single-post/forge/multi-post/other/CD-hedge/wrong-payload; cols: n HELPED/NEUTRAL VERBATIM-peak / v64-lever fed / private-transfer INFERRED). Cells cite rank refs (e.g. forge 90.54 V15 + 89.145 JED-v25; single-post 88.9/88.695/88.470; multi-post caution rank 6 0.00-private; CD-hedge ranks 15/22/23 INFERRED; wrong-payload TOKEN 3-ways ablation). Explicitly states field HURT=0 with reason (ledger definition, FIELD_CODE_ANALYSIS.md:110-111) and lists field cautionary NEUTRAL mirrors that function as do-not-adopt.
- Acceptance: every cell has ref + FIELD_CODE_ANALYSIS line; private claims labeled INFERRED; HURT=0 rationale quoted.

### V6-E — 50-note lessons (every NEUTRAL earns one line)
- The 50 code-read NEUTRAL rows each get one lesson line grouped by failure mode: opaque-blob 11 (ALLOW-star unverified — never adopt without literal check), stale sweep/resubmit/twin 8 (variance lottery — harvest via byte-identical re-rolls only), fork/baseline/starter/harness/diary 14 (coverage only — cite, do not weight), rotation/ablation 6 (TOKEN/rotation no-lift — literal-sentinel discipline), multi-post unadopted 10 (replay-budget cost > return — cautionary), CD-opaque 1+? (private direction but unverified inner). Each line: ref + why-still-NEUTRAL + keep/never-retry tag extending V4 Sec 22.5 / V5-F Table V5-F.
- Acceptance: 50 lines, refs unique, 0 overlap with 24 HELPED; keep/never-retry tags reconcile to Sec 23.4 rule.

### V6 build gates (before calling V6 award-ready)
- [ ] Heads: base ## unchanged; V6-A..E appendices only; TOC anchors work.
- [ ] Counts: 74+1 ERROR + 630 = 705; 705+105 = 810; 49/38/722/1 reconciled; verification table updated.
- [ ] Style: no table >12 rows; Figure 11 single new PNG within palette/DPI/grid rules; words appended only in appendices (base narrative untouched).
- [ ] Honesty: 630 rows labeled metadata-only INFERRED order; title numbers labeled CLAIM; private transfer labeled INFERRED; ERROR row retained not dropped.
- [ ] Repro: pull manifest + fetch commands (V5-G/V5-H pattern) extended to V6; assets/field_distribution.png reproducible from research/field_distribution_source.csv via committed script.

---

## 5. What to tell reviewers (one paragraph)

V5 did not lose notebooks — it stratified them: 74 code-read with bytes/payload/guard/verdict live in research/FIELD_CODE_ANALYSIS.md + report V5:3290-3428, 630 metadata-only with votes/titles in kernels_ALL_REFS.csv, and the Note carries only the award-readable cut (top-20 HELPED, 6-row family tally, 3-row tail teachers, 5-row 810 synthesis) because length (42.9k vs 2.5-5.5k), table-row (4-8, >10 move out), and figure (3-5, >8 bloat) gates require it, field HURT is definitionally 0, and tail scores are unverifiable self-claims. V6 keeps the narrative and adds the auditable stratified appendix (full 74 chunked + 630 banded + Figure 11 distribution + family matrix + 50 one-line NEUTRAL lessons) so 1st-position judges get both skim-path and exhaust-path.

*End — research/DIAGNOSIS_NOTE_GAP.md*
