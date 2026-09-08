# INVENTORY OF EVERY SOLUTION -- AI Agent Security (foundation for V4 weighting)

Date: 2026-09-05. Workspace: D:/personal/hackathon/agent-sec
Goal: list EVERY solution available, not just top results, so V4 can weight what helped vs did not.
Method: live `kaggle competitions submissions` pull (page-size 200), directory scans, first-line reads,
grep cross-checks against VERY_DETAILED_REPORT_V3.md. Code-read vs assumed is flagged per row.

Key discrepancies vs task brief: (1) notebooks/extracted holds 17 .txt, not 18. (2) Total submissions
is 105, not 90-120. (3) research/all_submissions_raw.txt = 63 lines = 11 header + 50 newest data rows.
(4) research/open_source_top50.md (314 lines) covers only 5 repos with raw reads; Seyamalam / PoojanTa /
tuannm3812 / will-rice are websearch-only per V2 s6.6 and V3 s6.7/s13.

## (A) OURS -- every submission (105 rows, oldest first)

Source: research/all_submissions_FULL.txt (107 lines, 138033 bytes, saved 2026-09-05 via
`kaggle competitions submissions -c ai-agent-security-multi-step-tool-attacks --page-size 200`).
Stats: 105 total = 97 COMPLETE + 8 ERROR. Public range 47.975-92.540. Dates 2026-08-04 to 2026-09-01.
V3 Table A audited only the newest 50 (IN-V3); the older 55 (v2-v70 era) were OMITTED-from-V3 as full
rows (partially summarized via docs/experiments.md ledger: v8/v9/v10-13/v14/v19-22/v27-34/v45/v50/v51/v62-67).

| ref | date (UTC) | status | public | private | description (trunc 110) | V3? |
|---|---|---|---|---|---|---|
| 55250029 | 2026-08-04 21:10 | ERROR | 60.69000 | 1.39500 | Apex v2 (T4): self-adaptive structure race + validation-fill, EXFIL+CONFUSED stacking, replay-safe sizing | OMITTED-from-V3 |
| 55263596 | 2026-08-05 08:01 | ERROR | 75.53500 | 0.91500 | Apex v5: replay-exact calibration race (11 structures), EXFIL+CONFUSED multipost stacking, adaptive margin, re | OMITTED-from-V3 |
| 55265346 | 2026-08-05 09:15 | ERROR | 75.44500 | 0.63000 | Apex v6: 16-structure race (forge-N 2..8, Do-N-times K=2-4, reply-OK wrap-up suppression, EXFIL+CONFUSED), rep | OMITTED-from-V3 |
| 55266167 | 2026-08-05 09:48 | ERROR | 77.22000 | 0.61500 | Apex v7: 18-structure race + forge_ok wrap-up suppression + fill-time fail-out adaptivity; replay-exact calibr | OMITTED-from-V3 |
| 55268417 | 2026-08-05 11:29 | COMPLETE | 74.52000 | 0.58500 | Apex v8: 19-structure race + confirmation-stage calibration + fill drift re-check (adaptive K) + single_short; | OMITTED-from-V3 |
| 55269205 | 2026-08-05 12:01 | COMPLETE | 78.64000 | 0.58500 | Apex v9: confirm-calib blend fix, fill-phase wall reserve, recheck cap, injective label gen, warmup-continue | OMITTED-from-V3 |
| 55300466 | 2026-08-06 14:17 | ERROR | 48.78000 | 1.25500 | Apex v10: lean 7-structure race (single/single_short/forge/forge2/post2/post2_deputy/deputy), removed confirma | OMITTED-from-V3 |
| 55300533 | 2026-08-06 14:20 | ERROR | 53.76500 | 1.58500 | Apex v11 [A/B experiment vs v10]: identical 7-structure pool, REPLAY_BUDGET_S 16000->20000 (per-pass cap ~7200 | OMITTED-from-V3 |
| 55300754 | 2026-08-06 14:30 | ERROR | 53.22000 | 1.75000 | Apex v12 [A/B experiment vs v10]: lean 5-structure pool (single/single_short/forge/post2/deputy, dropped post2 | OMITTED-from-V3 |
| 55305928 | 2026-08-06 19:38 | ERROR | 47.97500 | 1.12500 | Apex v13: re-verified against the live SDK (server-updated 2026-08-05, one day after our original pull) -- gua | OMITTED-from-V3 |
| 55319349 | 2026-08-07 07:54 | COMPLETE | 76.54000 | 0.58500 | Apex v14: REVERT to the proven v9 baseline (confirmation round + drift re-check + 19-structure pool restored,  | OMITTED-from-V3 |
| 55330302 | 2026-08-07 17:28 | COMPLETE | 74.89500 | 0.52500 | Apex v15 [isolated experiment vs v14]: adds ONE new structure, forge7_deputy (7 forged http.post calls + 1 dep | OMITTED-from-V3 |
| 55331076 | 2026-08-07 18:07 | COMPLETE | 76.88500 | 0.52500 | Apex v16 [isolated experiment vs v15]: sorts the returned candidate list by descending calibrated raw value be | OMITTED-from-V3 |
| 55331168 | 2026-08-07 18:12 | COMPLETE | 77.64500 | 0.27000 | Apex v19: raise TOP_HEAD_START 6->30 (bias fill cycle toward eff-optimal top structure), on top of v16's sort- | OMITTED-from-V3 |
| 55331373 | 2026-08-07 18:22 | COMPLETE | 72.72000 | 0.48000 | Apex v17: add forge5_deputy (isolated vs v16, not stacked with v19's TOP_HEAD_START change) | OMITTED-from-V3 |
| 55342869 | 2026-08-08 06:09 | COMPLETE | 77.44500 | 0.24000 | Apex v20: multi-turn crescendo_forge3 (Crescendo-style escalation + chat-template injection, 3 chained 8-hop t | OMITTED-from-V3 |
| 55343171 | 2026-08-08 06:26 | COMPLETE | 79.75500 | 0.28500 | Apex v21: remove forge7_deputy from the v19 baseline (TOP_HEAD_START=30 kept, no crescendo) -- isolates whethe | OMITTED-from-V3 |
| 55343334 | 2026-08-08 06:35 | COMPLETE | 82.48500 | 0.15000 | Apex v22: raise TOP_HEAD_START further, 30->80, on the v19 baseline (forge7_deputy kept) -- tests whether the  | OMITTED-from-V3 |
| 55343457 | 2026-08-08 06:42 | COMPLETE | 75.85000 | 0.22500 | Apex v23: crescendo_forge6 (6 turns, up to 48 posts/candidate) replacing v20's crescendo_forge3, on the v19 ba | OMITTED-from-V3 |
| 55343706 | 2026-08-08 06:58 | COMPLETE | 75.67000 | 0.22500 | Apex v24: turnstile16 (16 plain single-post turns, no chat-template injection, no escalation) on the v19 basel | OMITTED-from-V3 |
| 55364447 | 2026-08-09 01:42 | COMPLETE | 82.10500 | 0.15000 | Apex v25: combine confirmed wins from v21 (-forge7_deputy) + v22 (TOP_HEAD_START=80) as new baseline | OMITTED-from-V3 |
| 55364472 | 2026-08-09 01:43 | COMPLETE | 84.68500 | 0.04500 | Apex v26: push TOP_HEAD_START further, 80 -> 200, on the v25 baseline | OMITTED-from-V3 |
| 55364500 | 2026-08-09 01:45 | COMPLETE | 84.25500 | 0.16500 | Apex v27: trim 8 low-value structures from the v25 pool | OMITTED-from-V3 |
| 55364530 | 2026-08-09 01:47 | COMPLETE | 83.30500 | 0.15000 | Apex v28: cut calibration rep counts, not hop count, on the v25 baseline | OMITTED-from-V3 |
| 55364560 | 2026-08-09 01:48 | COMPLETE | 83.04000 | 0.16500 | Apex v29: successive-halving structure selection (new technique) on v25 | OMITTED-from-V3 |
| 55461090 | 2026-08-12 14:43 | COMPLETE | 85.62000 | 0.09000 | Apex v30: remove gRPC-biased replay_cap early-break from the fill loop (pushed CPU-only due to weekly GPU quot | OMITTED-from-V3 |
| 55461116 | 2026-08-12 14:44 | COMPLETE | 82.38000 | 0.12000 | Apex v31: skip per-candidate probe for a trusted TOP structure once fire_rate>=0.95 (isolated from v30) | OMITTED-from-V3 |
| 55461142 | 2026-08-12 14:45 | COMPLETE | 83.11500 | 0.00000 | Apex v32: combine v30 (replay_cap removal) + v31 (trust-skip probe) | OMITTED-from-V3 |
| 55461164 | 2026-08-12 14:46 | COMPLETE | 86.96500 | 0.03000 | Apex v33: push TOP_HEAD_START further, 80 -> 300 (isolated from v30/v31) | OMITTED-from-V3 |
| 55461185 | 2026-08-12 14:47 | COMPLETE | 87.07500 | 0.00000 | Apex v34: everything combined -- v32 (v30+v31) + v33's TOP_HEAD_START push to 300 | OMITTED-from-V3 |
| 55476757 | 2026-08-13 07:08 | COMPLETE | 84.05500 | 0.00000 | Apex v35: prompt-space diversification -- 4 forge8-wrapper text variants (final channel, system role, fake too | OMITTED-from-V3 |
| 55476776 | 2026-08-13 07:09 | COMPLETE | 85.34000 | 0.00000 | Apex v36: clean 2-turn overhead-amortization retest (forge8_x2, no escalation framing) | OMITTED-from-V3 |
| 55476784 | 2026-08-13 07:10 | COMPLETE | 86.71000 | 0.00000 | Apex v37: aggressive minimal-calibration throughput bet (pool 19->11, SH_FINALISTS 4->2, CONFIRM_REPS 3->1) | OMITTED-from-V3 |
| 55476799 | 2026-08-13 07:11 | COMPLETE | 87.15000 | 0.00000 | Apex v38: v35 + v36 combined (forge8-wrapper diversification + forge8_x2 amortization test) | OMITTED-from-V3 |
| 55476811 | 2026-08-13 07:12 | COMPLETE | 88.14000 | 0.00000 | Apex v39: v35+v36+v37 combined moonshot (branched from v34) | OMITTED-from-V3 |
| 55493515 | 2026-08-14 00:03 | COMPLETE | 83.07000 | 0.07500 | Apex v45: structural pivot -- remove forge2-forge8 multi-hop family (external evidence: wash-to-negative) | OMITTED-from-V3 |
| 55493546 | 2026-08-14 00:04 | COMPLETE | 77.49000 | 0.03000 | Apex v46: v45 + TOP_HEAD_START 300->600 | OMITTED-from-V3 |
| 55493583 | 2026-08-14 00:05 | COMPLETE | 85.61000 | 0.07500 | Apex v47: v45 + calibration-overhead cut (SH_FINALISTS 4->3, CONFIRM_REPS 2->1) | OMITTED-from-V3 |
| 55493616 | 2026-08-14 00:06 | COMPLETE | 84.65000 | 0.03000 | Apex v48: v45 + v46 (THS=600) + v47 (calibration cut) combined moonshot | OMITTED-from-V3 |
| 55493647 | 2026-08-14 00:07 | COMPLETE | 88.52500 | 0.07500 | Apex v49: hedge -- v40 unmodified (pre-pivot baseline) | OMITTED-from-V3 |
| 55515927 | 2026-08-15 00:03 | COMPLETE | 83.49000 | 0.12000 | Apex v50: v45 + reintroduce forge2 in isolation | OMITTED-from-V3 |
| 55515953 | 2026-08-15 00:04 | COMPLETE | 90.95000 | 0.10500 | Apex v51: v45 + reintroduce forge2/3/4 together | OMITTED-from-V3 |
| 55515980 | 2026-08-15 00:05 | COMPLETE | 86.63500 | 0.00000 | Apex v56: replace v53 with forge2_lean/forge3_lean/forge4_lean on the v39 full pool | OMITTED-from-V3 |
| 55516004 | 2026-08-15 00:05 | COMPLETE | 88.32500 | 0.00000 | Apex v55: v52's fill-lever test rebased onto v39 full pool | OMITTED-from-V3 |
| 55516024 | 2026-08-15 00:06 | COMPLETE | 90.44500 | 0.00000 | Apex v54: hedge, byte-identical to v39 | OMITTED-from-V3 |
| 55538630 | 2026-08-16 00:02 | COMPLETE | 91.38000 | 0.10500 | Apex v51: v45 + reintroduce forge2/3/4 together | OMITTED-from-V3 |
| 55538665 | 2026-08-16 00:03 | COMPLETE | 91.16500 | 0.06000 | Apex v62: TOP_HEAD_START 300->450 on top of v51's pool | OMITTED-from-V3 |
| 55538698 | 2026-08-16 00:04 | COMPLETE | 92.06500 | 0.10500 | Apex v63: fill-lever push (FILL_FRAC/MARGIN_S) on top of v51's pool | OMITTED-from-V3 |
| 55538736 | 2026-08-16 00:05 | COMPLETE | 92.54000 | 0.10500 | Apex v64: forge5 reintroduced on top of v51's pool | OMITTED-from-V3 |
| 55538768 | 2026-08-16 00:06 | COMPLETE | 90.70500 | 0.06000 | Apex v65: moonshot -- THS push + fill-lever combined on v51's pool | OMITTED-from-V3 |
| 55566031 | 2026-08-17 00:03 | COMPLETE | 92.12000 | 0.10500 | Apex v66: reintroduce forge6 on top of v64's pool, continuing the boundary search | OMITTED-from-V3 |
| 55566054 | 2026-08-17 00:04 | COMPLETE | 88.85500 | 0.10500 | Apex v67: terseness swap using v41's purpose-built terse template (H3) | OMITTED-from-V3 |
| 55566075 | 2026-08-17 00:04 | COMPLETE | 90.90000 | 0.10500 | Apex v68: push calibration confidence further (SH_FINALISTS 4->6, CONFIRM_REPS 2->3) on v64's pool | OMITTED-from-V3 |
| 55566105 | 2026-08-17 00:05 | COMPLETE | 91.32500 | 0.10500 | Apex v69: fill-lever push (FILL_FRAC 0.985, MARGIN_S 35.0) re-applied on v64's pool | OMITTED-from-V3 |
| 55566137 | 2026-08-17 00:06 | COMPLETE | 90.03000 | 0.09000 | Apex v70: moonshot -- v67's terse forge2-5 combined with v66's forge6 addition | OMITTED-from-V3 |
| 55616874 | 2026-08-19 06:42 | COMPLETE | 89.88500 | 0.10500 | Apex v71: resubmit v64's exact winning pool (92.540 real best) as a clean anchor, reverting v66/v67's confirme | IN-V3 |
| 55616884 | 2026-08-19 06:43 | COMPLETE | 81.41500 | 0.07500 | Apex v72: add forge7 to v64's pool, one more rung of the boundary-extension search past forge5/forge6 | IN-V3 |
| 55616902 | 2026-08-19 06:44 | COMPLETE | 88.37000 | 0.09000 | Apex v73: add forge8 to v64's pool, max hop count -- targets the cheap-cost/high-raw combo from 2026-08-08's r | IN-V3 |
| 55616927 | 2026-08-19 06:45 | COMPLETE | 82.24000 | 0.04500 | Apex v74: cut calibration overhead on v64's pool (SH_FINALISTS 4->2, CONFIRM_REPS 2->1), the historically-posi | IN-V3 |
| 55616942 | 2026-08-19 06:46 | COMPLETE | 90.82500 | 0.03000 | Apex v75: moonshot -- v73's forge8 addition + v74's calibration-overhead cut combined on v64's pool | IN-V3 |
| 55633976 | 2026-08-20 00:05 | COMPLETE | 90.93500 | 0.21000 | Apex v76: TOP_HEAD_START 300->150 on v64's exact pool -- untested direction, pool/calibration-neutral single-l | IN-V3 |
| 55634002 | 2026-08-20 00:06 | COMPLETE | 92.16000 | 0.10500 | Apex v77: FILL_FRAC 0.97->0.99, MARGIN_S 47->40 on v64's exact pool -- fill-budget squeeze, pool/calibration-n | IN-V3 |
| 55634044 | 2026-08-20 00:07 | COMPLETE | 91.24000 | 0.10500 | Apex v78 (revised): clean control resubmit of v64's exact 92.540 pool -- replaces the original forge6/7/8 pool | IN-V3 |
| 55634068 | 2026-08-20 00:08 | COMPLETE | 89.53500 | 0.10500 | Apex v79: REPLAY_SAFE_FRAC 0.97->0.99, ENV_OVERHEAD_S 0.25->0.15 on v64's exact pool -- replay-budget squeeze, | IN-V3 |
| 55634077 | 2026-08-20 00:09 | COMPLETE | 88.55000 | 0.21000 | Apex v80 (revised): v76+v77+v79's three pool/calibration-neutral budget levers combined -- replaces the origin | IN-V3 |
| 55656362 | 2026-08-21 00:06 | COMPLETE | 90.64000 | 0.09000 | Apex v81: forge6+forge7+forge8 all together, protected by both new fixes (rolling-window fire-rate + raw-floor | IN-V3 |
| 55656403 | 2026-08-21 00:07 | COMPLETE | 87.34500 | 0.07500 | Apex v82: forge6 reintroduced alone, protected by both new fixes -- v66 landed flat/-0.42 unprotected, retests | IN-V3 |
| 55656439 | 2026-08-21 00:07 | COMPLETE | 91.53000 | 0.09000 | Apex v83: forge7 reintroduced alone, protected by both new fixes -- v72 landed 81.415/-11.1 unprotected, the s | IN-V3 |
| 55656459 | 2026-08-21 00:08 | COMPLETE | 91.62500 | 0.09000 | Apex v84: forge8 reintroduced alone, protected by both new fixes -- v73 landed 88.370/-4.2 unprotected | IN-V3 |
| 55656479 | 2026-08-21 00:09 | COMPLETE | 91.33000 | 0.10500 | Apex v85: both new fixes present (rolling-window fire-rate + raw-floor), NO new structure -- clean control thi | IN-V3 |
| 55679339 | 2026-08-22 00:06 | COMPLETE | 89.03000 | 0.10500 | Apex v86: both fixes + v74's calibration cut (SH_FINALISTS 4->2, CONFIRM_REPS 2->1) re-tested now that v85's r | IN-V3 |
| 55679367 | 2026-08-22 00:07 | COMPLETE | 91.05500 | 0.10500 | Apex v87: both fixes + v77's fill-budget squeeze (FILL_FRAC 0.99, MARGIN_S 40) re-tested -- no new structure,  | IN-V3 |
| 55679392 | 2026-08-22 00:08 | COMPLETE | 89.38000 | 0.10500 | Apex v88: both fixes + v86's calibration cut AND v87's fill-squeeze combined -- tests whether two mechanistica | IN-V3 |
| 55679410 | 2026-08-22 00:09 | COMPLETE | 90.59000 | 0.15000 | Apex v89: forge8 + both fixes + new NEW_STRUCTURE_HEAD_START_FRAC mechanism, tempers guaranteed head-start to  | IN-V3 |
| 55679437 | 2026-08-22 00:10 | COMPLETE | 89.25500 | 0.09000 | Apex v90: forge8 + both fixes (v84's config) + v87's fill-squeeze stacked on top -- highest-ceiling bet in thi | IN-V3 |
| 55706928 | 2026-08-23 05:22 | COMPLETE | 83.08000 | 0.04500 | Apex v91: TOP_HEAD_START 300->450, first-ever test above 300 in this project's history. Isolated on v85's clea | IN-V3 |
| 55706965 | 2026-08-23 05:24 | COMPLETE | 81.21500 | 0.07500 | Apex v92: calibration confidence raised (SH_FINALISTS 4->6, CONFIRM_REPS 2->3, back to v25's original), opposi | IN-V3 |
| 55706981 | 2026-08-23 05:25 | COMPLETE | 91.14500 | 0.10500 | Apex v93: byte-identical resubmit of v85 (91.330 real). Best-of-public re-roll #1 -- community-confirmed same- | IN-V3 |
| 55707000 | 2026-08-23 05:26 | COMPLETE | 91.91000 | 0.06000 | Apex v94: v91+v92 combined (TOP_HEAD_START=450 AND SH_FINALISTS=6/CONFIRM_REPS=3), no new structure. Submitted | IN-V3 |
| 55707018 | 2026-08-23 05:27 | COMPLETE | 91.84500 | 0.09000 | Apex v95: byte-identical resubmit of v84 (91.625 real, forge8+both fixes). Best-of-public re-roll #2, structur | IN-V3 |
| 55738263 | 2026-08-24 09:01 | COMPLETE | 91.51500 | 0.10500 | Apex A_v64_exact: SH4 CR2 TOP300 9structs proven 92.54 baseline | IN-V3 |
| 55738308 | 2026-08-24 09:03 | COMPLETE | 91.11000 | 0.10500 | Apex B_fill_squeeze: v64 + FILL 0.99 MARGIN 35 H7 pool-neutral | IN-V3 |
| 55739253 | 2026-08-24 09:50 | COMPLETE | 89.65500 | 0.10500 | Apex C_terse_swap: v64 with terse forge2-5 H3 isolated | IN-V3 |
| 55739268 | 2026-08-24 09:51 | COMPLETE | 87.34000 | 0.03000 | Apex D_conservative: SH6 CR3 TOP450 on v64 pool | IN-V3 |
| 55739293 | 2026-08-24 09:52 | COMPLETE | 88.76500 | 0.10500 | Apex E_resubmit_A: byte-identical v64-exact variance lottery | IN-V3 |
| 55838986 | 2026-08-28 08:16 | COMPLETE | 91.26500 | 0.10500 | F_forge8_terse: 8-post terse lottery for 110 tail (isolated vs v64) | IN-V3 |
| 55839013 | 2026-08-28 08:17 | COMPLETE | 85.95500 | 0.01500 | G_aggressive: TOP600 FILL0.99 REPLAY0.99 +4-6 pts no DENY risk | IN-V3 |
| 55839061 | 2026-08-28 08:19 | COMPLETE | 90.93000 | 0.10500 | H_exfil_deputy: single EXFIL+CONFUSED 22raw private hedge | IN-V3 |
| 55839083 | 2026-08-28 08:20 | COMPLETE | 90.55500 | 0.10500 | I_b64: encoded hedge B64(SECRET_MARKER) private scan bypass | IN-V3 |
| 55839113 | 2026-08-28 08:21 | COMPLETE | 91.60500 | 0.10500 | J_resubmit: byte-identical v64 exact variance lottery tail 102 | IN-V3 |
| 55865007 | 2026-08-29 10:36 | COMPLETE | 87.48500 | 0.03000 | K_plain_aggressive: plain suppressor + TOP600 FILL0.99 souldrive insight | IN-V3 |
| 55865018 | 2026-08-29 10:36 | COMPLETE | 90.23500 | 0.04500 | L_forge5_suppressor: forge5 suppressor + aggressive TOP600 | IN-V3 |
| 55865028 | 2026-08-29 10:37 | COMPLETE | 89.91000 | 0.10500 | M_forge8_plain: forge8 plain 8-post 130 raw single-msg | IN-V3 |
| 55865039 | 2026-08-29 10:38 | COMPLETE | 89.98000 | 0.04500 | N_b64_aggressive: B64 hedge aggressive TOP600 private scan bypass | IN-V3 |
| 55865057 | 2026-08-29 10:39 | COMPLETE | 91.60500 | 0.10500 | O_combined_aggressive: EXFIL+CONFUSED aggressive private hedge | IN-V3 |
| 55920936 | 2026-08-31 17:25 | COMPLETE | 86.71500 | 0.09000 | v96: add sync_task structure (no Harmony forge, plain 'Sync task:...No commentary. Execute immediately.' frami | IN-V3 |
| 55920951 | 2026-08-31 17:26 | COMPLETE | 89.25000 | 0.10500 | v97: byte-identical resubmit of v64-exact (91.515 on its last re-roll as 'A', best-ever single sample was 92.5 | IN-V3 |
| 55920966 | 2026-08-31 17:28 | COMPLETE | 90.49000 | 0.06000 | v98: byte-identical resubmit of v94 config (TOP_HEAD_START=450, SH_FINALISTS=6, CONFIRM_REPS=3 -- real 91.910, | IN-V3 |
| 55920990 | 2026-08-31 17:29 | COMPLETE | 84.34000 | 0.03000 | v99: sync_task structure + single_exfil_deputy swap (two independently-safe pool additions combined). Predicte | IN-V3 |
| 55921010 | 2026-08-31 17:30 | COMPLETE | 90.06500 | 0.10500 | v100: second byte-identical resubmit of v64-exact today (variance harvest, 2nd roll). | IN-V3 |
| 55946383 | 2026-09-01 19:10 | COMPLETE | 83.19500 | 0.03000 | v66-exact test2 | IN-V3 |
| 55946386 | 2026-09-01 19:11 | COMPLETE | 85.80000 | 0.04500 | v64-exact byte-identical resubmit (best-ever real 92.540) - final day anchor/variance | IN-V3 |
| 55946391 | 2026-09-01 19:11 | COMPLETE | 90.52000 | 0.04500 | v77-exact byte-identical resubmit (2nd-best real 92.160) | IN-V3 |
| 55946430 | 2026-09-01 19:14 | COMPLETE | 89.34500 | 0.04500 | v64 pool + single_exfil_deputy hedge (STRUCTURES_WITH_HEDGE): EXFIL+CONFUSED combined in one hop, confirmed po | IN-V3 |
| 55946443 | 2026-09-01 19:16 | COMPLETE | 91.86000 | 0.04500 | v64-exact byte-identical resubmit, 4th variance roll today - final day, maximize shot at beating 92.540 | IN-V3 |
## (B) PUBLIC NOTEBOOKS -- every file in notebooks/extracted/ (17 files, 641237 bytes)

notebooks/ also holds the 17 original .ipynb files (same basenames). research/notebook_markdown_dump.txt
(26878 bytes, 496 lines) contains only 14 FILE entries -- 3 extracted files were never dumped.
V3 s4 main table deep-dives 5 notebooks, but V15/3-probe, JED-slow-multipost and Probe-and-Flood have NO
extracted .txt file (they live only as V2-row citations). Status: SUMMARIZED = covered in V2/V3 with
mechanism + score; PARTIAL/THIN = dump entry only (3-9 lines) or file-list mention; MISSED = no dump, no cite.

| # | filename | bytes | first-5-lines technique hint | dump coverage | V3 status |
|---|---|---|---|---|---|
| 1 | ai-agent-replay-dense-exfiltration.txt | 97171 | CELL0 md: Replay-Dense Exfiltration Final Push, throughput math | dump:2-311 FULL | SUMMARIZED (V2/V3 s4 row 4, 40.5/36.0) |
| 2 | ai-agent-sec-adaptive-uniform-two-probe-recovery.txt | 15789 | CELL0 md: Adaptive Uniform Two-Probe Recovery, Purpose | dump:312-361 | SUMMARIZED (V2 row 9, 88.470; V3 s18) |
| 3 | ai-agent-security-apex-attack.txt | 39480 | CELL0 md: Apex Attack, mean(gpt_oss,gemma) raw/200 (own pipeline?) | NOT in dump | MISSED (no dump entry, no V3 cite) |
| 4 | ai-agent-security-competition-solution.txt | 27892 | CELL0 code: sys.path/glob kaggle_evaluation harness bootstrap | dump:362-364 (3 lines) | THIN |
| 5 | ai-agent-security-v12.txt | 27874 | CELL0 md: Write attack.py TEMPLATE/N_CANDIDATES/MSGS_PER_CANDIDATE | dump:365-373 (9 lines) | PARTIAL (V2 row 15, ~51-60 infra) |
| 6 | ai-agent-security.txt | 12909 | CELL0 code: writefile attack.py, time import | dump:374-376 (3 lines) | THIN |
| 7 | ai-agent-v3-1-2-single-post-exfiltration.txt | 27828 | CELL0 md: Single-post exfiltration, 18-raw fill-efficiency stack | dump:377-384 | SUMMARIZED (V2 row 17, 88.9) |
| 8 | aiagsec-ea-b-0721.txt | 28701 | CELL0 md: Submission notebook, gateway rerun, inference server | dump:385-407 | PARTIAL (V3 s18 file list) |
| 9 | conservative-replay-safe-sizing.txt | 11949 | CELL0 md: v20 Combined Parameter Optimisation, probe overhead | dump:408-424 | SUMMARIZED (V2 row 16, 51.25-52) |
| 10 | eda-agent-security-trajectory-search.txt | 173315 | CELL0 md: EDA Trajectory Search, replayable chains, density score | NOT in dump | PARTIAL (V2 row 10 cites concept eta=E[raw]+2P/E[cost]; full 173KB text never dumped) |
| 11 | getting-started-notebook.txt | 4751 | CELL0 md: JED Starter Notebook, trick tool agent | NOT in dump | SUMMARIZED (V2 row 8, 0.075 baseline via code_tab) |
| 12 | jed-attack-5-templates-aggressive-replay-0-99.txt | 9860 | CELL0-1 code: TEMPLATES harness, eff=median/fire_rate | dump:425-427 (3 lines) | SUMMARIZED (V2 row 6, V3 s18.6, 88.5-89) |
| 13 | jed-multi-step-attack-relay-push100.txt | 21018 | CELL0 code: base64 harness, candidate glob | dump:428-430 (3 lines) | THIN (V3 s18 file list only) |
| 14 | jed-v25.txt | 28224 | CELL0 md: JED v25 FRAME_TEMPLATE REPLAY_SAFE 0.98, Gold 89.145 | dump:431-438 | SUMMARIZED (V2 row 2) |
| 15 | lb60-525-july-safe-edge-prune-tail8-upgrade.txt | 40949 | CELL0 md: Experiment 007 Tail6+margin42 | dump:439-624 FULL (185 lines) | SUMMARIZED (V2 row 14, 60.125) |
| 16 | multi-endpoint-severity-stacker.txt | 67613 | CELL0 md: Single-post N=900, +50% candidates, timeout risk | dump:625-670 (45 lines) | SUMMARIZED (V2 row 18, target 54) |
| 17 | v23-alpha2co-667-break60.txt | 5914 | CELL0 md: V23 Alpha2CO 667 Break60, 667*0.09=60.03, aa.co hosts | dump:671-708 to EOF | SUMMARIZED (V2 row 7, V3 s18.7) |

Tallies for V4 weighting: SUMMARIZED 10 (1,2,7,9,11,12,14,15,16,17), PARTIAL 3 (5,8,10),
THIN 3 (4,6,13), MISSED 1 (3: apex-attack 39KB). Priority re-reads: #3 (own 39KB never dumped),
#10 (173KB EDA full text), #13 (relay-push100 21KB, 3-line dump only).

## (C) GITHUB REPOS -- 5 code-read + 4 websearch-only (9 rows)

open_source_top50.md:1-314 raw-fetched README + attack.py + notebooks.md for 5 repos, ran local
Guardrail.decide / eval_predicates probes (src-verified vs comp_data/aicomp_sdk). V2 s6.6 + V3 s6.7/s13
admit Seyamalam/PoojanTa/tuannm3812/will-rice were never raw-pulled. No repo ships a committed
private-survivable pipeline; that family lives in post-deadline notebooks (takamichitoda 24.36).

| # | repo | URL | claimed score | stars/commits | code actually read? | verdict |
|---|---|---|---|---|---|---|
| 1 | Jun-Morita/kaggle-ai-agent-security | https://github.com/Jun-Morita/kaggle-ai-agent-security | 89.685 post-refresh (91.89 pre) | 4 stars, 71 commits | YES (README + notebooks.md 69k tokens, SUBMISSIONS ledger) | VALIDATED, most trustworthy |
| 2 | vijayDL/kaggle-ai_agent_security | https://github.com/vijayDL/kaggle-ai_agent_security | 91.3 single-post transplant | 0 stars, 53 commits | YES (attack.py, v16_v15port, redteam harness) | PARTIALLY VALIDATED (91.3 is competitor lineage) |
| 3 | hamidhosen42/AI-Agent-Security-Multi-Step-Tool-Attacks | https://github.com/hamidhosen42/AI-Agent-Security-Multi-Step-Tool-Attacks | 100.62 paper math | 1 star, 2 commits, stale 2026-06-23 | YES (v8.ipynb attack_code) | INVALIDATED (fs.delete DENY + TOKEN no-read = 0) |
| 4 | faresrafat3/ai-agent-security-portfolio | https://github.com/faresrafat3/ai-agent-security-portfolio | 76.995 kernel 335686112 | 0 stars, 4 commits, stale 2026-07-18 | YES (attack.py v8.1) | HISTORICALLY VALIDATED, CURRENTLY STALE |
| 5 | dogahwisdom/ai-agent-security-attack | https://github.com/dogahwisdom/ai-agent-security-attack | none claimed | 1 star, 7 commits | YES (dispatcher, MultiStepExplorer) | RESEARCH-ONLY, anti-throughput |
| 6 | will-rice (exact slug unverified) | github.com/will-rice (INFERRED -- never raw-pulled) | private 29.520 rank 15 (team Will Rice 16555376) | unknown | NO (websearch only) | BRIDGE/MEDIUM (rank link only) |
| 7 | Seyamalam | no repo found | notebook-family? | -- | NO (not found) | INFERRED 0 if EXFIL-only / LOW |
| 8 | PoojanTa | no repo found | notebook-family? | -- | NO (not found) | INFERRED 0 if EXFIL-only / LOW |
| 9 | tuannm3812 | sparse, backlinks only | JED lineage? | few | NO (websearch only) | INFERRED / LOW |

## (D) DISCUSSIONS / THREADS -- all 12 files in research/raw_discussions/

Upvotes from V3 s7 + code_tab scrape. Credibility: host/staff posts load-bearing; community variance
reports high; working-note/scratch files background. rules_page/scratch have no upvotes (N/A).

| # | file | bytes | thread | author | upvotes | credibility | status in V3 |
|---|---|---|---|---|---|---|---|
| 1 | disc_707811.txt | 4392 | 707811 Welcome | host Owen Vallis / Manish Bhatt | 26 | low-technical | cited s7 |
| 2 | disc_712642.txt | 19131 | 712642 Evaluator update + FAQ | host Owen Vallis | 17 | HIGHEST load-bearing | cited s7 |
| 3 | disc_714340.txt | 5849 | 714340 Private LB static replay | host Manish Bhatt | 2 | load-bearing | cited s7 |
| 4 | discussion_733058.txt | 22563 | 733058 Evaluator updates + LB refresh | staff MartynaPlomecka | 28 | HIGHEST | cited s7 |
| 5 | disc_733345.txt | 3512 | 733345 Score fluctuation | community (Adarsh, Shadab, zigiella) | 3 | high | cited s7 |
| 6 | disc_733442.txt | 3005 | 733442 Exfil without cheating | community Cleanor Labs | 4 | medium | cited s7 |
| 7 | disc_734944.txt | 1601 | 734944 Working note (radiant-allomancer) | community | N/A (scrape) | medium-background | cited V2 s6, V3 s7 ref |
| 8 | code_tab.txt | 4064 | Code-tab leaderboard snapshot (not a thread) | N/A | per-notebook (JED v25 132 Gold, slow 61 Bronze, Pilk 46 Bronze, GettingStarted 1487) | high-evidence | cited s4/s5 |
| 9 | rules_page.txt | 37860 | Rules page scrape | N/A | N/A | context | background |
| 10 | scratch_k1_source.txt | 86564 | MARL/multi-agent framing source (didactic) | N/A | N/A | background | cited s4 family 7 |
| 11 | scratch_k2_source.txt | 1954 | v96-serveronly-alpha2co-bare676 static TOKEN 676-alpha2 | N/A | N/A | background | cited s4 family 7 |
| 12 | scratch_k3_source.txt | 45010 | hop-saturating 8-post burst + deputy reserve (target80) | N/A | N/A | background | cited s4 family 7 |

## APPENDIX -- every other local file (for completeness)

research/: adjacent_domains/transfer.md 3261; competition/overview.md 5899 (task interface + limits);
critical_evaluation.md 7148; existing_solution/field_landscape.md 4469; kaggle/public_notebooks.md 5585
(Code-tab snapshot + 7 families + 4 strategy signals); literature/relevant_papers.md 5672 +
search_algorithms.md 5298 (8 papers); synthesis/next_steps.md 8592 (H1-H7); techniques/attack_primitives.md
4833; variants_top50_proposal.md 29093; notebook_markdown_dump.txt 26878; raw_writeup 19678 (no ext);
README.md 1459; final_leaderboard.txt 2650 (20 rows + next-page token,iefrozen board);
final_private_top80.txt 2186 (20 rows: Xz 46.425 down to untitled 29.055 + token, rows 21-80 uncaptured);
VERY_DETAILED_REPORT.md 60248 (V1 528 lines); VERY_DETAILED_REPORT_V2.md 175799 (V2 1281 lines);
VERY_DETAILED_REPORT_V3.md 272327 (V3 s1-521+ read-capped).
docs/: experiments.md 11612 (full v8-O + v96-100 + v105-109 + post-deadline mechanism);
WORKING_NOTE.md 76876; WORKING_NOTE_V2.md 97867; WORKING_NOTE_V3.md 144585; writeup.md 845;
writeup_style_guide.md 8124; assets/ 6 PNGs (ablation, guardrail, pipeline, score_progression,
taint_window, wallclock).
submission/: attack.py + notebook.ipynb + kernel-metadata.json + 15 variant dirs x (attack.py +
notebook.ipynb): variants/ A_v64_exact B_fill_squeeze C_terse_swap D_conservative E_resubmit_A (2026-08-24);
variants_top50/ F_forge8_terse G_aggressive H_exfil_deputy I_b64 J_resubmit (2026-08-28);
variants_next5/ K_plain_aggressive L_forge5_suppressor M_forge8_plain N_b64_aggressive O_combined_aggressive
(2026-08-29).
archive/: NEXT_BATCH_PLAN.md 11350, PLAN.md 13132, README.md 626, TUNING.md 7183, WORKING_NOTE.md 47206
(superseded 2026-08-24 snapshot), writeup_draft_superseded_2026-08-24.md 24077.
