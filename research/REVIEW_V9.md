# REVIEW V9 - Strict 9.5/10 Gate (5 Working Note Criteria)

**Date:** 2026-09-08
**Scope:** docs/WORKING_NOTE_V9.md (3670 lines / 71059 words / 484316 chars, measured Measure-Object) vs research/SCORING_RUBRIC_DEEPDIVE.md + docs/writeup_style_guide.md:9,38,50,72,124
**V9 claim:** 824 weighted (105 own + 719 field: 74 code-read + 630 metadata-only + 14 deadline-day + 1 ERROR), V8 frozen verbatim at docs/WORKING_NOTE_V8.md plus Sec 24/25 + Sec 6/8 expansions (docs/WORKING_NOTE_V9.md:6,19-21)
**Gate:** 9.5/10 per criterion is production. No criterion reaches it. Overall: FAIL on C1 gate, PASS-content / FAIL-packaging elsewhere - not WIN.

| Criterion | Score 0-10 | Verdict vs 9.5 |
}|--------------------------|--------------|-------------------|
| C1 Technical clarity & reproducibility | **6.2** | FAIL - gate violation |
| C2 Methodological contribution | **7.4** | FAIL |
| C3 Security insight | **8.4** | FAIL (strongest, still short) |
| C4 Usefulness | **6.8** | FAIL |
| C5 Responsible communication | **7.6** | FAIL |
| **Mean** | **7.28** | **Not award-ready** |

> Rubric weights (SCORING_RUBRIC_DEEPDIVE.md:78-86): C1 ~30% gate, C2 ~25%, C3 ~20% domain multiplier, C4 ~15% tie-break, C5 ~10% + VETO. C1 unreadable = unscored; C5 dishonest = veto. V9 is honest but unreadable at 71k words.

---

## C1 - Technical Clarity and Reproducibility - 6.2/10

**Looks for (SCORING_RUBRIC_DEEPDIVE.md:16):** TL;DR 4-6 sentences WHAT/WHY/SCORE/REPO (guide:22-36); pipeline Figure FIRST with caption+interpretation (guide:66,72); every claim idea -> fence (10-25 lines, # Expected:) -> isolated delta +x.xx with file:line (guide:76,129); exact params/seeds/hardware/commands/versions; no prose-only claim.

### Strengths (with file:line)
- **File:line discipline survives:** Every claim anchored - src/apex_attack/primitives/templates.py:39-50 forge (docs/WORKING_NOTE_V9.md:194), comp_data/aicomp_sdk/guardrails/optimal.py:51-58 first-present-arg (docs/WORKING_NOTE_V9.md:118-122,178), src/apex_attack/search/race.py eff definition (docs/WORKING_NOTE_V9.md:209-216), src/apex_attack/search/fill.py + src/apex_attack/config.py:35-43 probe1/bill8 (docs/WORKING_NOTE_V9.md:227-235), research/all_submissions_raw.txt:14-63 ledger.
- **Pillar + hero table exist:** Sec 2 pillar Table 1 (docs/WORKING_NOTE_V9.md:120-126) and Sec 6 hero Table 7-A (docs/WORKING_NOTE_V9.md:270-280) follow Optiver A6 5x5 style - 6 rows, control->treatment, isolated deltas + noise flags.
- **Guardrail self-test surfaced:** 10-line runnable fence + Expected + 60s falsification rule (docs/WORKING_NOTE_V9.md:582-608, 1937-1946). Santa A25 notebook-first + D3 differentiator.
- **Repro fences:** Sec 12A-D 10-25 line fences with # Expected: (docs/WORKING_NOTE_V9.md:753-886), Sec 13 bash 1-5 exact commands with Expected (docs/WORKING_NOTE_V9.md:908-932), hardware T4 + GGUF c099eb4 pinned (docs/WORKING_NOTE_V9.md:135-138,1308-1320). Passes tools/local_test.py:321-431 5/5.

### Weaknesses (load-bearing, each blocks 9.5)
1. **Length gate blown 11x.** Award window 2500-5500 WORDS (writeup_style_guide.md:38, SCORING_RUBRIC_DEEPDIVE.md:99-101). V9 is 71059 words / 3670 lines (docs/WORKING_NOTE_V9.md:21 gate 3800-4500 lines PASS but words ~13x). Mental model: Length beyond window divides total - every 10k over cap costs more than any lever adds (SCORING_RUBRIC_DEEPDIVE.md:96). Skim-penalty FAIL (C1 ~30% gate SCORING_RUBRIC_DEEPDIVE.md:78).
2. **Figure bloat.** Winners cap 3-5 figures (writeup_style_guide.md, SCORING_RUBRIC_DEEPDIVE.md:100). V9 ships 10 figures + Fig 12 Venn survival (docs/WORKING_NOTE_V9.md:638-641) + ablation variants; Table V5-M lists 10 reused (docs/WORKING_NOTE_V9.md:2031-2047).
3. **Table budget violated in narrative.** Guide: narrative 4-8 rows, appendix <=12 (guide:50). Hero 7-A 6 rows PASS, but Sec 5/6/7 tables (W-E1, W-E2, 6.x) plus Sec 8 Table 8b, plus Sec 24 Table 11 (14 rows at docs/WORKING_NOTE_V9.md:2117-2135) sit inline in narrative - breaks 12-row skim gate.
4. **Dual-TOC / duplicated intro.** V9 TL;DR (docs/WORKING_NOTE_V9.md:10-13) plus V9 how this note meets 5 criteria box (docs/WORKING_NOTE_V9.md:14) plus inherited V8 TL;DR Box (docs/WORKING_NOTE_V9.md:38-50) stacked in first screen - reviewer cannot tell which is the 5-sentence hook.
5. **No JSON registry / numbered notebooks.** Repro is commands not factory (see C4).

### Fixes for V10 (must, with acceptance)
- **F1 - Cut narrative to 2500-5500 words (hard gate).** Freeze Sec 1-10 narrative to <=5500 words via CI Measure-Object -Word. Move Sec 18-26 exhausts (W-A..W-D, V6-A/B, V5 maps) to appendices already chunked <=12 rows. Accept: CI word-check PASS, narrative no table >8 rows, appendix no table >12 rows.
- **F2 - One TL;DR, 5 sentences, then auto-TOC.** Rewrite docs/WORKING_NOTE_V9.md:10-14 to exactly 5 sentences: hook (824 weighted, 91-92.5 band, 0.07 collapse) + What/Why + 92.540 VERBATIM + 30.735 private proof + repo+60s self-test link. Delete duplicated V8 TL;DR from first screen. Accept: 5-sentence linter PASS, guide:38 PASS.
- **F3 - Cap skim figures to 5.** Narrative keeps Fig1 pipeline, Fig2 guardrail, Fig4 progression, Fig7 scatter, Fig12 Venn. Move other 6 to appendix with reuse map at docs/WORKING_NOTE_V9.md:2031-2047. Accept: grep ![Figure narrative ==5, each caption on own line + interpretation after.
- **F4 - Chunk Table 11.** Split 14-row Table 11 into 11a (1-7) + 11b (8-14) each <=12 rows. Accept: row-count linter PASS.
- **F5 - Variance callout under Table 7-A.** Promote seed-band box (docs/WORKING_NOTE_V9.md:332-334) to fenced box directly under 7-A with band mean ~89.6 +-2.6, <5 pts noise rule disc_733345.txt:56-138. Accept: reviewer sees band without scrolling.

---

## C2 - Methodological Contribution - 7.4/10

**Looks for (SCORING_RUBRIC_DEEPDIVE.md:28):** One transferable method as rule + ablation. Unified harness -> comparison table -> selection/blend rule -> seed-variance proof. Optiver 5x5, MAP triplet, ARC selection, Vesuvius invariance.

### Strengths
- **Throughput-first as method, not prompts.** Three levers (blind-spot primitive + Harmony forge +27.5 + halving race eff=mean_raw/mean_cost + validate-then-keep 31%->~100%) isolated with single-variable A/B and file:line (docs/WORKING_NOTE_V9.md:176-235 levers, Table 3 climb docs/WORKING_NOTE_V9.md:320-328 deltas +4.84/+3.93/+7.90/+1.16, Fig 3 ablation docs/WORKING_NOTE_V9.md:223-225).
- **Hero Table 7-A is right artifact.** Models x treatments matrix with paired deltas + noise flag (docs/WORKING_NOTE_V9.md:270-280) - zero prose-only claims. Complements era Table W-E1 (docs/WORKING_NOTE_V9.md:304-313) and 20-test ceiling sweep (docs/WORKING_NOTE_V9.md:348-357) proving ceiling ~91-92.5.
- **Ship log + stop rule exist.** docs/WORKING_NOTE_V9.md:335-347 ship rule (ship iff 3-seed mean delta >5 + fire_rate at CALIB_HOPS=8, overrides #1 THS ladder #2 deputy <10%) plus stop rule after 41 post-v64 no-beats (docs/WORKING_NOTE_V9.md:48,346). Titanium A3 + ISIC A10.
- **Rejected alternatives with cost model.** One probe = one inference = mean_cost seconds from fill budget (docs/WORKING_NOTE_V9.md:220-221,1369-1371); 100 probes = 8-26pct budget -> anti-throughput. Go-Explore dogahwisdom cited.
- **V9 external validation added.** Table 7-B deadline-day (docs/WORKING_NOTE_V9.md:284-294): syed v19 120.850->0.000 collapse vs v12b 30.735 survival, takamichitoda 136.250 formal row=43.75*r/el, tkd hedge 24.360. Formalizes eff as cost-first.

### Weaknesses (why not 9.5)
1. **Still single-seed headline.** SCORING_RUBRIC_DEEPDIVE.md:110 requires v64 92.540 [seed123 + 2 rerolls + ensemble mean +- std]. V9 reports band 85.800-91.860 via hosted rerolls (docs/WORKING_NOTE_V9.md:398-415, 6.06 pts) but these are HOSTED RESUBMITS confounded by wall-clock, not seeded reruns. Jigsaw A12/MAP A16 needs same-harness reseeds with std. Lonnie B6 max-of-105 inflation noted (docs/WORKING_NOTE_V9.md:332) not quantified.
2. **No unified-CV harness table.** Field VERBATIM (90.54 V15, 89.145 JED-v25, 88.9 pilkwang) not under same harness - incomparable eras flagged only in footnotes (docs/WORKING_NOTE_V9.md:296-297), not in harness table at REAL_REPLAY_CEILING=150.
3. **Table 7-B mixes eras.** Takamichitoda 136.250 September private-era envelope vs 92.540 August - needs ERA column.
4. **No private-aware ranking.** eff = mean_raw/mean_cost with 16 vs 4 guarantees EXFIL wins fill (docs/WORKING_NOTE_V9.md:261,538-541). No eff_private = p_survive*mean_raw/mean_cost row.

### Fixes for V10
- **F6 - Seed triplet + ensemble column.** Add Table 7-A1 next to 7-A: seed123 92.540 VERBATIM | reroll1 85.800 | reroll2 91.860 | mean 89.73 +-2.6 | noise floor 5 pts (disc_733345.txt:56-138). Run 2 local seeds via same harness (MockCompliantAgent) to fill cells even with mock gap. Tag HOSTED band vs SEEDED triplet separately. Accept: no single-seed headline remains.
- **F7 - Harness table (<=8 rows).** Table 6-A harness rows=v64/JED-v25/V15/pilkwang/deputy-only, cols=same folds/seed/metric (REAL_REPLAY_CEILING=150), score, delta, noise flag. All via tools/local_test.py proxy with 6x under-estimate note already at docs/WORKING_NOTE_V9.md:248-254. Accept: every comparison under same ceiling.
- **F8 - Private-aware flip proof.** Add ranking flip: p_survive from wall-clock 15h vs 13h (research/VERY_DETAILED_REPORT.md:423-428 Discussion 738946) or proxy-cascade strict rate (kkrasikov). Show eff crowns forge5 vs eff_private crowns deputy. Accept: ranking flip table present.
- **F9 - t-test ship rule stated.** In Sec 6 header add: Ship iff 3-seed mean delta >5 AND fire_rate at CALIB_HOPS=8, t-test p<0.05 ISIC style. Log 3rd override if violated. Accept: rule + p explicit, Lonnie B6 quantified.

---

## C3 - Security Insight - 8.4/10 (strongest, still <9.5)

**Looks for (SCORING_RUBRIC_DEEPDIVE.md:40):** Threat model + attacker capability per lever + hole falsifiable <60s + temporal/artifact controls BEFORE model gains + public-vs-private per-component deltas.

### Strengths
- **Mechanism chain best-in-class.** OptimalGuardrail._extract_target first-present-arg blind spot (optimal.py:51-58 -> docs/WORKING_NOTE_V9.md:118,178,562,2119), taint-5 superset predicate-2 (optimal.py:44-47 vs predicates.py:234 -> docs/WORKING_NOTE_V9.md:564-565 + Fig5 docs/WORKING_NOTE_V9.md:527-529), canonical secret.txt vs substring (predicates.py:181-196 vs optimal.py:22-30 -> docs/WORKING_NOTE_V9.md:566), Harmony ChatInject arXiv:2509.22830 (docs/WORKING_NOTE_V9.md:191-194,569), Gemma doubled-brace GGUF c099eb4 cap (docs/WORKING_NOTE_V9.md:570).
- **Falsifiable <60s.** Self-test fence (docs/WORKING_NOTE_V9.md:582-608) + Expected + falsification rule (docs/WORKING_NOTE_V9.md:607 if assertion 1 flips to DENY, claim dead). D3 differentiator SCORING_RUBRIC_DEEPDIVE.md:95 - fastest falsification loop.
- **Private autopsy per-component with honest labels.** Sec 8a Table docs/WORKING_NOTE_V9.md:609-617 (public VERBATIM vs private VERBATIM vs INFERRED transfer) + Sec 6.6 private-first view Spearman ~0.02 (docs/WORKING_NOTE_V9.md:419-432) + rank-6 95.130->0.00 title-claim flagged TITLE-CLAIMED. ASHRAE B16 per-component.
- **Wall-clock side-channel articulated.** Fig6 15h vs 13h DENY-skips-hop1 ~1.5s/cand (docs/WORKING_NOTE_V9.md:531-533,540-542), checklist pins it (docs/WORKING_NOTE_V9.md:655-660), future work quantifies 7200s delta (docs/WORKING_NOTE_V9.md:1275-1277).
- **V9 three proofs + matrix + Venn are real accretion.** 8a-extra proofs (docs/WORKING_NOTE_V9.md:620-627): takamichitoda 24.360 rank 76 + abukayyisah matrix predicate x guardrail (docs/WORKING_NOTE_V9.md:624-625) + syed v12b 30.735 vs v19 120.850 inversion plain beats fixture 3.435 provenance not recipient. Survival matrix Table 8b (docs/WORKING_NOTE_V9.md:628-635) + Fig12 Venn (docs/WORKING_NOTE_V9.md:638-641) make CD-only decidable without private - novel.

### Weaknesses (why 8.4 not 9.5)
1. **Wall-clock Pareto still INFERRED, never measured.** Table docs/WORKING_NOTE_V9.md:537-556 labels every cost cell INFERRED or MEASURED with STATUS honest - good honesty but cost axis is INFERRED arithmetic pending Santa-2024 curve. SCORING_RUBRIC_DEEPDIVE.md:117 requires retrospective gateway-timestamp ledger. P0-3 gate SCORING_RUBRIC_DEEPDIVE.md:138 wants curve, not admission.
2. **Private regex confidence hedge remains blanket.** Every private transfer INFERRED (docs/WORKING_NOTE_V9.md:562,674-678 confidence high but not 100%, research/VERY_DETAILED_REPORT.md:441-443). Needs per-claim tag SOURCE: vs INFERRED via 738915 wall-clock, not banner.
3. **Artifact-control table missing trivial baselines.** Malware A21 7-liner expects 4-row trivial controls printed BEFORE levers: date-segment split at freeze 2026-08-07 / version-segment GGUF c099eb4 same-bytes 2-12pts / title-claim control / private-transfer control. Sec1 integrity box docs/WORKING_NOTE_V9.md:90-100 states freeze but not as executed control rows with deltas.
4. **H10 untested still cited as lessons.** H10 wall-clock + B64 never instrumented (docs/WORKING_NOTE_V9.md:460) and syouyatobita synthetic surfaces honestly private_guardrail_observed=false (docs/WORKING_NOTE_V9.md:2130) - honest but not measured.

### Fixes for V10
- **F10 - Publish wall-clock Pareto (measure, not infer).** Parse kaggle kernels status gateway timestamps per research/all_submissions_raw.txt:14-63 + local probe1 vs bill8 ledger; emit per-family wall-clock ledger + score-vs-compute truncation curve at REAL_REPLAY_CEILING=150 + N=4/5/6 cost bars (Vesuvius B9). Label each cell MEASURED vs INFERRED. Downgrade current Pareto to provisional if timestamps unavailable. Accept: cost axis next to score axis, 15h-vs-13h explained with numbers.
- **F11 - Artifact-control table (Malware 7-liner).** Add 4-row Table 1b before Sec4: date trivial, version GGUF band, title-claim control, private-transfer control. Each expectation vs result + file:line. Accept: control rows precede any model-gain delta, lesson SCORING_RUBRIC_DEEPDIVE.md:45 satisfied.
- **F12 - Per-claim confidence tags.** Replace single banner with inline [SOURCE: predicates.py:144] vs [INFERRED via 738915 wall-clock, high] vs [INFERRED via synthetic proxy, low] on each sentence in 8a-extra and Table 8b Survives-private col. Accept: no ambiguous INFERRED paragraph.

---

## C4 - Usefulness to Benchmark Community - 6.8/10

**Looks for (SCORING_RUBRIC_DEEPDIVE.md:52):** Copy-paste to save GPU-hours: registry + numbered notebooks in run order + BASE_PATH + artifact URLs + OOM workarounds + cost axis + keep/never-retry tags + per-structure ablations.

### Strengths
- **Checklist generous and actionable.** Sec9 Table8 Red-Team Checklist (docs/WORKING_NOTE_V9.md:650-667): Measure fire_rate/cost_replay/wall-clock, Pin GGUF c099eb4 + budget 8750 vs 9000, Size REPLAY_SAFE_FRAC=0.97/MARGIN_S=47, Test deputy-hedge/decode-path - each with metric/threshold + source config.py:21-46 / local_test.py:594-623 / jed_attack_gateway.py:62-63.
- **Factory exists (not just story).** Sec13 exact bash 1-5 (docs/WORKING_NOTE_V9.md:908-932): bundle.py -> local_test 5/5 -> generate_figures -> make_notebook -> kaggle push/status/submit with Expected + pinned GGUF/seed/hardware (docs/WORKING_NOTE_V9.md:892-902). CommonLit B20 chain partially satisfied.
- **Keep/never-retry priced across 810.** Sec22.5 rule + Table23-D synthesis (docs/WORKING_NOTE_V9.md:1521-1555 keep: forge+THS300+confirm-calib+replay-cap+fill-squeeze+both-fixes; never: lean, THS>300, SH6/CR3, unprotected forge7/8, terse, trust-skip, TOP600, sync_task) plus V4 10 HELPED vs 10 HURT mapping (research/VERY_DETAILED_REPORT_V4.md:2785-2809). MDC B25 4-failures.
- **Exhaust not sample.** Sec23 74+1+630=705, 705+105=810, reconciliation 49/38/722/1, vote sums 5580, pointers research/VERY_DETAILED_REPORT_V5.md:3454-4478, research/kernels_ALL_REFS.csv sortRank 61-705. DIAGNOSIS RC6 satisfied - rare.

### Weaknesses (why not 9.5)
1. **No TalkingData JSON registry.** B14 expects experiments.json rows: generator/config/seed/cost/delta (SCORING_RUBRIC_DEEPDIVE.md:124). Repro is commands, not registry. SETTINGS.json/entry_points/requirements promised (writeup_style_guide.md:132) but Sec13 shows dependencies=[] vendored with no dumped SETTINGS content (docs/WORKING_NOTE_V9.md:895-900). Fresh clone cannot verify CONFIG without opening source.
2. **No numbered notebooks 01..05 in run order with BASE_PATH + URLs + OOM note.** CommonLit B20 asks notebooks/01_prep..05_infer with BASE_PATH + artifact URLs + CUDA-OOM restart. V9 has tools/bundle.py, tools/make_notebook.py:177-183 T4, tools/local_test.py harness but not as numbered notebooks.
3. **Cost axis partial (see C3).** No Hydrogen B8 efficiency-vs-accuracy table (small-model vs winning ensemble). Sec7 Pareto Table docs/WORKING_NOTE_V9.md:535-556 INFERRED pending.
4. **Field tail metadata-only - honest but low-transfer.** Sec23.3 630 tail (docs/WORKING_NOTE_V9.md:1904-1907) defended via 3 duplication signals docs/WORKING_NOTE_V9.md:2023-2024 (byte-identical twins, title-template repetition, author-series sweeps) - solid rationale but ranks 61-705 TITLE-CLAIMED/INFERRED only (docs/WORKING_NOTE_V9.md:1908-1916).
5. **Per-structure/per-head ablations thin.** Race mentions SH_FINALISTS=4, CONFIRM_REPS=2, ROLLING_WINDOW=20/0.6 (docs/WORKING_NOTE_V9.md:214-216,231-234) with crater proofs v72/v74/v92, but no per-structure eff bar with latency vs raw scatter (Fig3 N=4/5/6 exists but not score-vs-compute).

### Fixes for V10
- **F13 - experiments.json registry.** Ship research/experiments.json (one row per lever: generator file:line / config seed / wall-clock / cost_replay / delta) plus notebooks/01_prep..05_infer stubs in run order with BASE_PATH repo_root + comp_data/ pin + GGUF c099eb4 URL + OOM/slow-arm workaround (CommonLit B20). Accept: fresh clone runs bash 1-6 to 5/5 PASS without asking author, TalkingData B14 PASS.
- **F14 - Dump SETTINGS.json + entry_points + requirements verbatim.** In Sec13 or App.G dump pyproject.toml:6, src/apex_attack/config.py:21-46 defaults, tools/bundle.py:1-101 contract. Accept: writeup_style_guide.md:132 A3/B1 PASS.
- **F15 - Efficiency Pareto (Hydrogen dual-track).** 6-row table rows=forge5/v64/deputy-hedge/small-model/keep-all-no-gate, cols=public band, private observed, wall-clock MEASURED per Gateway stamps, params, score/cost ratio. Accept: small-model config shipped, not just winning ensemble, guide pitfall #2 addressed.
- **F16 - Decode sample for opaque blobs.** Add 2-line comment per opaque blob family why b64 considered ALLOW* research/VERY_DETAILED_REPORT_V5.md:3290-3428 has anchors - surface 1 example per family in narrative.

---

## C5 - Responsible Communication - 7.6/10 (honest voice, unfinished guardrails)

**Looks for (SCORING_RUBRIC_DEEPDIVE.md:63):** Honesty under pressure: variance disclosed (never single-seed), decision rule + every override logged, small-n selection risk confessed, misses credited by name, stop rule, luck/betting disclosed, CLAIM vs VERBATIM vs INFERRED where exactness varies. 10% share when clean, VETO when violated. ISIC A10, MCTS A23, Titanic A3, Porto/ASHRAE.

### Strengths
- **Two-banner defense framing.** Top Defense/Research Only benchmark scope (docs/WORKING_NOTE_V9.md:3,27-28), safety box before forge (docs/WORKING_NOTE_V9.md:186-188), Sec8 defense bullets strip-tokens/data-only/isolate reasoning (docs/WORKING_NOTE_V9.md:576-579), Sec10 Responsible scope + disclosure (docs/WORKING_NOTE_V9.md:670-686). Pitfall #8 addressed, not silent.
- **Variance honesty throughout.** Seed-band header docs/WORKING_NOTE_V9.md:332-334 band 85.800-91.860, <5 pts noise per disc_733345, gap ~19 pts 111.690 vs 92.540 rank 278/4216 (docs/WORKING_NOTE_V9.md:353-354,682), craters labeled -11.1/-10.3/-9.46 (docs/WORKING_NOTE_V9.md:510-514).
- **Honest labels hierarchy enforced.** VERBATIM = Kaggle-verified pulls or code-read, TITLE-CLAIMED [CLAIM]=title self-claim, INFERRED=rank-order/metadata or black-box probing legend (docs/WORKING_NOTE_V9.md:100,1932,1973). Every section tags status: Table7-B private wheel INFERRED, Table8a band INFERRED, Table11 VERBATIM vs TITLE-CLAIMED flagged (docs/WORKING_NOTE_V9.md:2117 header).
- **Misses credited by name with numbers.** Sec8b What we missed / field did better (docs/WORKING_NOTE_V9.md:644-648) credits V15 90.54, JED-v25 89.145 Gold, takamichitoda 24.36, aleaiest 29.67, xiaoz259 CD-final - MCTS A23. Asks prize via portfolio not prompt (docs/WORKING_NOTE_V9.md:12).
- **Decision/override + stop rule logged.** Ship log Table docs/WORKING_NOTE_V9.md:335-347 (rule ship iff 3-seed mean delta >5 AND fire_rate at CALIB_HOPS=8, overrides #1 THS ladder #2 deputy <10%) + stop rule docs/WORKING_NOTE_V9.md:346,1334-1336 no lever beat v64 in 41 tests, ceiling declared (Titanic A3). Infra failures candid: cron pushes failed twice, require kernels status (docs/WORKING_NOTE_V9.md:683), 710234-not-reverified hygiene (docs/WORKING_NOTE_V9.md:685-686), incident background agent (docs/WORKING_NOTE_V9.md:356).
- **V9 audit honest about new evidence.** Table11 synthesis Honesty note (portfolio, not prompt) docs/WORKING_NOTE_V9.md:2229 states synthetic proxies not recovered private, private_guardrail_observed=false, bytes large because base64 zip (docs/WORKING_NOTE_V9.md:2134-2136), Sec25 thesis guardrail shift as portfolio with host-disclosed static replay (disc 714340).

### Weaknesses (why not 9.5)
1. **Safety box not line-adjacent to first token literal.** writeup_style_guide.md:pitfall #8 expects defense at first <|end|> mention. V9 box at Sec4.2 docs/WORKING_NOTE_V9.md:186-188 but forge fence at docs/WORKING_NOTE_V9.md:194-200 - order correct yet rubric wants fenced box immediately adjacent to token literal with strip-tokens + Sec8 pointer, not two paragraphs before.
2. **Small-n selection incompletely confessed.** Lonnie B6 heresy (selecting on 120-sample / 2-12 noise, seed 19920627 SCORING_RUBRIC_DEEPDIVE.md:65) addressed qualitatively docs/WORKING_NOTE_V9.md:332 v64 is max-of-105 on 2-12pt band so point carries expected max-inflation but not as E[max inflation]=sigma*PhiInv(1-1/n) estimate.
3. **Tail numbers still surface without inline CLAIM tag in a few sentences.** e.g., Best public band about 91-92.5 (v64 peak 92.540 VERBATIM) docs/WORKING_NOTE_V9.md:7 tagged, but body Top score 147.530 docs/WORKING_NOTE_V9.md:353 relies on source table tag not inline. Strict RC3 needs every occurrence tagged.
4. **Responsible box not in TL;DR skim.** SCORING_RUBRIC_DEEPDIVE.md:130 fix: 5-line Responsible box under TL;DR surfacing variance + gap + private INFERRED + wall-clock INFERRED. Current responsible lives in Sec10 docs/WORKING_NOTE_V9.md:670-686 - not in 5-minute skim.

### Fixes for V10
- **F17 - Move safety box line-adjacent to first <|end|> fence.** Fence at docs/WORKING_NOTE_V9.md:194 should be immediately preceded by fenced Safety box copy of Sec4.2 banner verbatim. Accept: safety reviewer never encounters control token without banner + defense first, guide pitfall #8 PASS.
- **F18 - Lonnie max-inflation estimate.** Add: E[max inflation | n=105, sigma~2.6, band 2-12] approx 5-7 pts -> band is finding, point is draw. Cite research/all_submissions_raw.txt:14-18 band + disc_733345.txt:56-138. Accept: Lonnie B6 heresy explicitly quantified.
- **F19 - Inline CLAIM sweep.** Lint TOKEN / 95.130 / 66.015 / 147.530 - append [TITLE-CLAIMED] or [VERBATIM] on every inline occurrence, not just table headers. Grep audit grep -n "95.130|66.015|147.53" docs/WORKING_NOTE_V9.md. Accept: RC3 linter 0 untagged.
- **F20 - TL;DR responsible 5-line box.** Under TL;DR add box: variance 2-12 pts / <5 noise, gap 19 pts to 111.690, private INFERRED wall-clock, mock 6x gap, stop rule 41 tests. Accept: 5-minute skim (TL;DR+Fig1/Table7-A+Sec8+Fig12) carries responsible, V6_REBUILD_PLAN.md:142 dry-run PASS.

---

## V9_delta assessment (V8 -> V9)

V9 preserves V8 verbatim (docs/WORKING_NOTE_V9.md:24 docs/WORKING_NOTE_V8.md 3567 lines sha ac2c0a5225b0) and adds exactly four lessons V8 lacked:
- Table 7-B + Sec8a-extra three proofs + Fig12 Venn survival (docs/WORKING_NOTE_V9.md:620-641) - fixes P0-3 private confidence gap.
- Table 11 deadline-day 14 (docs/WORKING_NOTE_V9.md:2117-2149) + Table11b taint-free proof (docs/WORKING_NOTE_V9.md:2138-2148) - fixes hedging-starved diagnosis with 14 measured controls.
- Sec25 portfolio framing (docs/WORKING_NOTE_V9.md:2154-2228) + kkrasikov cascade + syouyatobita 2x8 study - fixes validation-harness gap (measure before submission, not after).
- Sec6 external validation rows (docs/WORKING_NOTE_V9.md:281-294 Table7-B, docs/WORKING_NOTE_V9.md:282 V9 external validation box) - proves 92.540 single-surface optimum, 30.735 hedge optimum.
All honest: private_guardrail_observed=false, synthetic proxies disclosed, bytes/hashes verifiable (research/NEW_WORKING_NOTES_ANALYSIS.md:10-29). Net: V9 raises C3 ~7.5->8.4 and C2/C5 measurably, but does not change word-count gate or registry factory - so 9.5 still blocked by C1/C4.

---

## Verdict for V10 submission readiness

**Do not submit V9 as Working Note award entry.** Content is prize-level security analysis marooned in 71k-word appendix-as-note. Reviewer never reaches Sec8 insights - failure is packaging, not science.

**V10 checklist (ordered by unblock power):**
1. F1+F2+F3+F4 length/figure/TLDR/table gates - else FAIL regardless of insight.
2. F10+F11 wall-clock Pareto + artifact-control table - else C3 stays <9.5.
3. F6+F7+F8+F9 seed triplet + harness + private-aware ranking + t-test - else C2 stays <9.5.
4. F13+F14+F15 registry + SETTINGS dump + efficiency Pareto - else C4 stays <9.5.
5. F17+F18+F19+F20 safety adjacency + inflation + CLAIM sweep + TLDR responsible - else C5 veto risk.

When all 20 fixes (F1-F20) pass linters, simulated scores are C1 9.6 / C2 9.5 / C3 9.7 / C4 9.5 / C5 9.6 - then WIN. Before that, PASS at best.

---

## Evidence anchors (so edits are traceable)

- 5 criteria: research/SCORING_RUBRIC_DEEPDIVE.md:14-71 + docs/writeup_style_guide.md:9
- Gates: writeup_style_guide.md:38 2500-5500 WORDS, :50 4-8 rows narrative / 12 rows appendix, :72-73 3-5 figures, :111 pitfalls, :124-135 10-point checklist
- V9 gates + TLDR: docs/WORKING_NOTE_V9.md:16 contents, :21 3800-4500 lines gate, :10-14 TLDR + criteria box, :32-36 frozen V8 meta, :90-100 integrity box
- Pipeline/guards/fill: optimal.py:51-58 blind spot, optimal.py:44-47 taint window, predicates.py:144 literal, templates.py:39-50 forge, config.py:21-46 knobs, labels.py:47-48 unique domains
- Ledger math: scoring.py:56-101 S=raw/200, W {1:1,2:2,3:4,4:8,5:16}, core/cells.py:58-211, +2 per unique domain
- Variance/refresh/GGUF: disc_733345.txt:56-138 2-12pts, research/VERY_DETAILED_REPORT.md:62-63 GGUF c099eb4, discussion_733058.txt:58-78 freeze 2026-08-07
- Ship/stop/cost: config.py:35-43 CALIB_HOPS=8 SH_FINALISTS=4 CONFIRM_REPS=2, docs/experiments.md:65 top-50 111.690, research/all_submissions_raw.txt:14-63 63 rows
- Private/wall-clock: discussion 738915 re.search(secret), 738946 15h vs 13h, tools/local_test.py:64-83 6x mock gap, research/final_private_top80.txt:7 Xz 46.425
- Field 705/824: research/KERNELS_FULL_INVENTORY.md:5-11 705 via scoreDescending, research/kernels_ALL_REFS.csv 705 refs, research/FIELD_CODE_ANALYSIS.md:11-94,109 74 code-read verdicts, research/VERY_DETAILED_REPORT_V5.md:3454-4478 tail chunks
- V9 adds: research/new_working_notes/syed3000-v12b-our-best-private-build/*.ipynb 30.735, syed3000-v19 120.850->0.000, takamichitoda hedge 24.360, takamichitoda objective 136.250, huanligong 21.495, backtracking 15.975, kkrasikov 7475 bytes, syouyatobita 8 surfaces

*End - research/REVIEW_V9.md*
