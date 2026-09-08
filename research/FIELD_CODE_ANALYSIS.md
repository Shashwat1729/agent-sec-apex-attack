# FIELD CODE ANALYSIS - 705-notebook sweep (2026-09-05)

Sources: research/kernels_ALL_REFS.csv (705 refs), research/KERNELS_FULL_INVENTORY.md (scoreDescending rank order).
Pulls: kaggle kernels pull into research/field_code/top60/<sanitized>/ and research/field_code/vote15/<sanitized>/.

Context: Optimal = OptimalGuardrail (public, destination-only, checks http.post url first-arg, taint-window 5).
Our v64 = Apex v64-exact (92.540 public best, 9-structure EXFIL pool + forge5 + single_exfil_deputy hedge).
Verdict scale: HELPED = technique or evidence supports a v64 component; NEUTRAL = untested, stale, opaque, or baseline;
HURT = ledger-confirmed regression if adopted. ERROR = pull failed (private or deleted).

## (A) Technique table - TOP 60 by scoreDescending (ranks 1-60)

| rank | ref | votes | bytes | family | payload | guard | verdict | why |
|---|---|---|---|---|---|---|---|---|
| 1 | konbu17/jed-attack-exp093 | 8 | 11499 | multi-post | literal | ALLOW | NEUTRAL | Serial K-hop EXFIL per http.post; Sept private-era, unverifiable delta vs v64 |
| 2 | outliar/agi-exfil-160-gpt500-gem2000-sub | 1 | 61866 | single-post | literal | ALLOW | HELPED | Truncated args-prefill exemplar (B7, 128.770 baseline); prefill technique relevant to fill-era v64 |
| 3 | sebastianmateus/replayforge-k8-correctness-router-0824 | 1 | 43469 | forge | literal | ALLOW | HELPED | ReplayForge K-endpoint forge + correctness router; same forge lineage as v64 forge5 pool |
| 4 | aleaiest/aisec-n38urllast | 1 | 7497 | single-post | literal | ALLOW | HELPED | Gemma URL-last two-form router; URL-routing evidence supports v64 clean-URL design |
| 5 | xiangwaaaaa/notebook93b16cbbf4 | 0 | 22395 | other-resubmit | literal-inline | ALLOW | NEUTRAL | Byte-identical best-of resubmission (v679 of v664); variance lottery, no technique delta |
| 6 | hiranorm/publiclb-95-130-privatelb-0-00-aas-mf-k8-ff-test | 1 | 42532 | multi-post | literal | ALLOW | NEUTRAL | Title-claimed 95.130 pub / 0.00 priv; cautionary public-only max-fill exemplar v64 rejected |
| 7 | samwiz/aas-v15-gpu | 1 | 10681 | forge | literal | ALLOW | HELPED | PAYLOAD literal + single-post frame + K-hop chains + probe winners; frame evidence for v64 pool |
| 8 | nkosindwandwe/jed-attack-multi-step | 0 | 22183 | multi-post | literal | ALLOW | HELPED | Self-validating attack.py (keep only firing candidates); gating matches v64 calibration |
| 9 | merkiraz/v8-hybrid-frame-gpt-oss-biraz-daha-agresif-r | 0 | 22118 | forge | literal | ALLOW | NEUTRAL | FRAME + gpt_oss hybrid; late-Aug private-era variant, no transferable delta |
| 10 | merkiraz/jed-v35-uniquecellmax-v1 | 0 | 13946 | other-probe | literal | ALLOW | NEUTRAL | Unique-cell-max probe variant; late private-era, no delta |
| 11 | foysalemonshanto/ai-agent-security-v15 | 546 | 29973 | forge | literal | ALLOW | HELPED | 90.54 VERBATIM 3-probe family; probe-era ancestor of v64 calibration |
| 12 | eugeneyeung/ai-agent-security-fillmax-m34-f099 | 4 | 28435 | single-post | literal | ALLOW | HELPED | Fillmax sizing family; fill-budget evidence used by v64 FILL work |
| 13 | sirikilohit/agent-sec-tool-atk-v170-winner | 0 | 8590 | other-suppressor | literal | ALLOW | HELPED | GPT-OSS analysis-bypass + Gemma strict-single-post; bypass framing + single-post discipline |
| 14 | aqibrazadev/maximum-throughput-attack-code | 1 | 37756 | multi-post | literal | ALLOW | NEUTRAL | Single+dual flood multi-predicate coverage; throughput flood untested vs v64 |
| 15 | evgendvorkin/ai-agent | 371 | 11802 | CD | benign-email+fs.write | ALLOW | HELPED | PHOENIX private-only CD + DESTRUCTIVE_WRITE combo, no EXFIL; private-CD direction supports v64 deputy hedge |
| 16 | malikhammadfarooq/jed-attack-v38-slowest-1-29 | 0 | 29488 | multi-post | literal | ALLOW | NEUTRAL | Budget-sized slowest-latency branch; latency corner, no v64 delta |
| 17 | foysalemonshanto/ai-agent-security-v12 | 317 | 30065 | forge | literal | ALLOW | HELPED | Same 3-probe family as v15; probe-era ancestor |
| 18 | nctuan/jed-v25 | 170 | 28920 | forge | literal | ALLOW | HELPED | 89.145 Gold VERBATIM; FRAME + replay-safe 0.98 adopted into v64-era thinking |
| 19 | dimong4/ai-agent-security | 426 | 10140 | single-post | literal | ALLOW | NEUTRAL | High-vote baseline, no verbatim score delta |
| 20 | kaiwalyaatulraut/ai-agent-security-solution | 122 | 21076 | other-blob | encoded-blob | ALLOW* | NEUTRAL | Opaque b64 attack.py (single-post 3-probe race inside); inner unverified |
| 21 | adhirajjagtap/probe-and-flood-strategy | 116 | 10146 | single-post | literal | ALLOW | HELPED | 88.695 peak VERBATIM; probe-then-flood calibration pattern |
| 22 | danischaparov/ai-agent-security-v12 | 1 | 9468 | CD | benign-email | ALLOW | HELPED | Benign email.send deputy-only templates; private-bet evidence for v64 deputy hedge |
| 23 | farbricated/confused-deputy | 1 | 12938 | CD | literal | ALLOW | HELPED | CD family, private-relevant per 1st-place writeup; supports v64 hedge |
| 24 | canqiang/aiagsec-ea-b-0721 | 273 | 29235 | single-post | literal | ALLOW | HELPED | K=1 + guardrail-first-arg analysis; guardrail modeling supports v64 clean-URL design |
| 25 | tetsutani/ai-agent-sec-adaptive-uniform-two-probe-recovery | 217 | 18218 | single-post | literal | ALLOW | HELPED | 88.470 VERBATIM 2-probe recovery; probe-recovery fed v64 calibration |
| 26 | kaiwalyaatulraut/ai-agent-security-competition-solution | 135 | 30198 | other-blob | encoded-blob | ALLOW* | NEUTRAL | Opaque b64 attack.py; THIN dump, inner unverified |
| 27 | anasriaz/ai-agent-security | 108 | 12577 | multi-post | literal | ALLOW | NEUTRAL | Forge + deputy + secretread hybrid; no verbatim peak |
| 28 | rokaiyasomapti/ai-agent-sec-another-approach-resubmission | 142 | 22186 | other-blob | encoded-blob | ALLOW* | NEUTRAL | Opaque b64 blob resubmission; inner unverified |
| 29 | haodou092/notebookcb9f3b04b6 | 106 | 13410 | single-post | literal | ALLOW | NEUTRAL | Domain-diversity on v7 algo; diversity bonus minor |
| 30 | maqsoudtawaliou/aas-attack-exp9 | 0 | 10963 | forge | literal | ALLOW | NEUTRAL | Forge + suppressor exp9; no verbatim peak |
| 31 | nctuan/jed-slow-multipost | 154 | 28546 | multi-post | literal | ALLOW | NEUTRAL | 86.605 Bronze multipost=3; multipost branch not adopted by v64 |
| 32 | haodou092/conservative-replay-safe-sizing | 124 | 12414 | single-post | literal | ALLOW | HELPED | Replay-safe sizing band evidence (51-52); sizing fed v64 |
| 33 | lopure/jed-multi-step-attack-relay-push100 | 69 | 20057 | multi-post | literal-inline | ALLOW | NEUTRAL | Relay v7-linear-base family per Devpost; different lineage from v64 |
| 34 | naveenvenubagadi/ai-agent-security-exfil-primary-v2 | 0 | 15062 | CD | encoded-blob | ALLOW* | NEUTRAL | V8 deputy-prefill single-send inside b64; opaque |
| 35 | yusuketogashi/ai-agent-sec-another-approach | 182 | 23273 | other-blob | encoded-blob | ALLOW* | NEUTRAL | Opaque b64 blob; early approach note, inner unverified |
| 36 | anvithpothula/aisec-pilk | 86 | 15866 | single-post | literal | ALLOW | HELPED | 85.41 Bronze single-message raw-weighted fill; fill sizing evidence |
| 37 | caoyupeng/jed-multi-step-attack-2 | 33 | 21540 | other-blob | encoded-blob | ALLOW* | NEUTRAL | Opaque b64 blob; inner unverified |
| 38 | diladiclekeke/working-note-ai-agent-security | 0 | 24518 | other-analysis | literal | ALLOW | HELPED | Working note: live validation-fill EXFIL adopted + CD tail; analysis supports v64 combo |
| 39 | pilkwang/ai-agent-v3-1-2-single-post-exfiltration | 189 | 29101 | single-post | literal | ALLOW | HELPED | 88.9 VERBATIM full fill-efficiency stack; v64 fill-stack ancestor |
| 40 | mehdielm/jed-attack-budget-aware-portfolio-search | 0 | 48322 | other-search | literal | ALLOW | NEUTRAL | Budget-aware portfolio search harness; Sept search tooling, no delta |
| 41 | biohack44/jed-multi-step-attack-3753a0 | 6 | 21468 | other-blob | encoded-blob | ALLOW* | NEUTRAL | Opaque b64 blob; inner unverified |
| 42 | raunakdey07/ai-agent-security-adaptive-template-race | 1 | 12863 | other-race | literal | ALLOW | NEUTRAL | Template-race harness; methodology note, no delta |
| 43 | godofthunder2407/ai-agent-sec | 3 | 22186 | other-blob | encoded-blob | ALLOW* | NEUTRAL | Opaque b64 blob; inner unverified |
| 44 | faresrafat/notebook85c5782962 | 2 | 24394 | other-portfolio | literal | ALLOW | NEUTRAL | 76.995 VERBATIM V6 portfolio; pre-refresh stale |
| 45 | clemendes/borapracima-v1 | 2 | 14424 | other | literal | ALLOW | NEUTRAL | Probe + deputy + calib hybrid; no verbatim peak |
| 46 | aratisantoshshinde/ai-agent-security-adaptive-tool-call-throughput-se | 1 | 35476 | other-blob | encoded-blob | ALLOW* | NEUTRAL | Hybrid single/dual density gate inside b64; opaque |
| 47 | tiktoktrendz/jed-submission | 31 | 73225 | multi-post | literal | ALLOW | NEUTRAL | Throughput JED submission; scale branch untested vs v64 |
| 48 | pengwang91/jed-fill-v26-replaysafe | 24 | 21313 | single-post | literal | ALLOW | HELPED | Fill K-chain live-gated selection with marker assert; fill sizing fed v64 |
| 49 | caoyupeng/lb-66-015-from-kun-zhang | 51 | 6790 | other-fill | literal-inline | ALLOW | NEUTRAL | Kun Zhang fork, title-claimed 66.015; stale July fill |
| 50 | naveenvenubagadi/ai-attack-probe | 0 | 6411 | CD | encoded-blob | ALLOW* | NEUTRAL | Deputy addr-compress blind probe inside b64; opaque |
| 51 | lucifer19/shadow-cat-firewall | 74 | 15701 | other-fallback | literal+packed | ALLOW | NEUTRAL | AnchorLock v28 safe-alternative fallback fork; defensive flavor |
| 52 | lucifer19/jed-strategy-sentinel | 28 | 14798 | single-post | literal | ALLOW | NEUTRAL | 63.650 anchor-repair fork; repair-only, no new technique |
| 53 | llccqq624/shadow-cat-firewall | 9 | 8551 | other-fork | literal | ALLOW | NEUTRAL | Shadow Cat format-safe fork; no delta |
| 54 | quan0095/security-eval-edge-fill | 5 | 0 | ERROR | pull-failed | n/a | ERROR | 400 Bad Request on pull (private or deleted); metadata only |
| 55 | boristown/shadow-cat-firewall-darkagi-edited | 9 | 78540 | other-fork | literal | ALLOW | NEUTRAL | Dual-GPU visual teaching edition; teaching fork, no attack delta |
| 56 | canqiang/aiagsec-submission | 82 | 21005 | single-post | literal | ALLOW | HELPED | K=1 + first-arg guardrail analysis; same guardrail-modeling family as rank 24 |
| 57 | devchandra/ai-agent-security-v83-assia-live-fill-m37 | 1 | 5156 | other-sweep | literal | ALLOW | NEUTRAL | July fill sweep stub; superseded |
| 58 | yusuketogashi/lb60-525-july-safe-edge-prune-tail8-upgrade | 138 | 45381 | other-sweep | literal | ALLOW | NEUTRAL | Tail8/margin sweep; v64 superseded margin work |
| 59 | devchandra/ai-agent-security-v75-yusuke-lb60525-margin32 | 3 | 45381 | other-sweep | literal | ALLOW | NEUTRAL | Byte-identical twin of rank 58 sweep (same 45381 bytes); duplicate, superseded |
| 60 | caoyupeng/v23-alpha2co-667-break60 | 94 | 9223 | other-ablation | wrong-payload | ALLOW | NEUTRAL | PAYLOAD=TOKEN=admin123 ablation (667 x 0.09 math); marker later reverted upstream |

## (A2) Baseline table - TOP 15 by votes NOT in top 60

| # | ref | rank | votes | bytes | family | payload | guard | verdict | why |
|---|---|---|---|---|---|---|---|---|---|
| V1 | martynaplomecka/getting-started-notebook | 265 | 1763 | 7239 | other-starter | secret.txt-read | ALLOW | NEUTRAL | Official starter (read secret.txt demo); baseline coverage only |
| V2 | llkh0a/aas-local-validation | 334 | 459 | 19951 | other-harness | none | ALLOW | NEUTRAL | Local GPT-OSS/Gemma validation harness; runs attack.py, no attack of its own |
| V3 | pilkwang/ai-agent-replay-dense-exfiltration | 77 | 231 | 106695 | single-post | literal | ALLOW | HELPED | Replay-dense template ancestor; density thinking fed v64 replay-safe sizing |
| V4 | pilkwang/ai-agent-working-note | 66 | 159 | 8115 | other-suppressor | literal | ALLOW | HELPED | Reasoning-suppression probe on 52.87 base; suppression evidence |
| V5 | boristown/agi-ai-agent-security | 68 | 129 | 18745 | other-ablation | wrong-payload | ALLOW | NEUTRAL | TOKEN=admin123 direct-post repair; payload ablation, no lift |
| V6 | pilkwang/eda-agent-security-trajectory-search | 169 | 125 | 189495 | other-EDA | literal-rotation | ALLOW | NEUTRAL | Early trajectory-search baseline (55 cells); predates v64 methods |
| V7 | karnakbaevarthur/multi-endpoint-severity-stacker | 111 | 118 | 70436 | single-post | literal | ALLOW | NEUTRAL | Static single-post N=900; sizing consistent with v64, no measured delta |
| V8 | yaroslavkholmirzayev/ai-agent-security-k1-short | 62 | 111 | 2880 | other-minimal | wrong-payload | ALLOW | NEUTRAL | Minimal static replay, TOKEN payload; ablation stub |
| V9 | yaroslavkholmirzayev/replay-dense-boundary-exact-aggressive | 72 | 104 | 8045 | other-rotation | literal-rotation | ALLOW | NEUTRAL | Multi-payload rotation (TOKEN + marker); rotation ablation, no lift |
| V10 | lucifer19/cognitive-firewall | 71 | 90 | 26455 | multi-post | encoded-blob | ALLOW* | NEUTRAL | Shadow Cat Relay EdgeFill v27 inside b64; opaque |
| V11 | kokinnwakashuu/ai-agent-security-working-diary | 67 | 77 | 7467 | other-diary | unverified | ALLOW* | NEUTRAL | Working diary, static replay notes; no literal marker found in code |
| V12 | caoyupeng/ai-agent-security-v2-exfil-mass-shift | 146 | 72 | 34775 | other-rotation | literal-included | ALLOW | NEUTRAL | SCORING_PAYLOADS multi-payload rotation from 27.23 EDA base; ablation |
| V13 | arizalfirdaus123/multi-turn-exfiltration-with-adaptive-burst | 115 | 62 | 18599 | multi-post | literal | ALLOW | NEUTRAL | Multi-turn EXFIL + CD fusion; fusion untested vs v64 |
| V14 | junaid512/agent-security-attack-submission | 136 | 62 | 93623 | single-post | literal | ALLOW | NEUTRAL | Timeout-safe static dense single-post; sizing overlaps v64, no delta |
| V15 | nawfeelrahman1124444/baseline-solution-4-900 | 235 | 61 | 23668 | other-baseline | destructive-demo | ALLOW | NEUTRAL | Baseline demos incl destructive fs.write prompts; coverage only |

## (B) Family tally (top 75)

Buckets collapsed to single-post / forge / multi-post / other. Suppressor-only, CD-only, opaque blobs, starters,
harness, diary, resubmits, sweeps, payload-ablations, forks, and races all count as other.

| bucket | count | members |
|---|---|---|
| single-post | 17 | ranks 2,4,12,19,21,24,25,29,32,36,39,48,52,56 + V3,V7,V14 |
| forge | 7 | ranks 3,7,9,11,17,18,30 |
| multi-post | 11 | ranks 1,6,8,14,16,27,31,33,47 + V10,V13 |
| other | 39 | CD-only (15,22,23,34,50), suppressor (13,V4), opaque blobs (20,26,28,35,37,41,43,46), resubmits, sweeps, ablations, forks, starter, harness, diary, baselines |
| ERROR | 1 | rank 54 quan0095 (400 Bad Request, private or deleted) |

Verdict totals: HELPED 24 (22 top60 + V3,V4), NEUTRAL 50, HURT 0, ERROR 1.
HURT is 0 because no pulled field notebook matches a ledger-confirmed regression; our HURT cases
(encoded-marker hedge I_b64/N_b64, forge7/forge8 additions v72/v73) came from our own ablations, not from field code.
Payload split across 74 code-read: literal SECRET_MARKER 54, opaque b64 attack.py 11 (9 + CD 34,50),
benign-email CD-only 2 (15,22), wrong-payload TOKEN=admin123 3 (60,V5,V8), secret.txt starter 1,
destructive-demo 1 (V15), no-payload harness 1 (V2), unverified diary 1 (V11).
Guardrail under Optimal: ALLOW 62, ALLOW* 12 (inner blob unverified, presumed EXFIL), ERROR n/a 1.
Optimal never DENYs a clean-URL post in this set; every attack uses clean urls and passed the url check.

## (C) Coverage note

74 code-read (59 top60 + 15 vote15) + 1 ERROR (rank 54) + 630 metadata-only = 705 total field.
Code bytes: about 2.02 MB across 74 notebooks (largest: V6 EDA 189495, V3 replay-dense 106695).

### Ranks 61-705: metadata only (630 rows after removing the 15 vote-baselines pulled above)

Reason per row: low rank, likely stale pre-refresh or no-signal. Full ref/title/author/votes/lastRunTime
for all 630 rows is in research/kernels_ALL_REFS.csv (sortRank 61-705); nothing below is code-read.
Band stats: 645 rows at rank 61-705 hold 5580 total votes; the 15 highest-voted in-band rows are exactly
the V1-V15 baselines pulled above, so the unpulled 630-row tail is long-tail low-vote material.
Notable in-band families visible from titles only (not code-verified): Hermes/OpenClaw chains (paul720810),
Hermes-attack N-series sizing sweeps, ducnamphan JED v0-v21 series, tkhanna96 H006 geometry/scale series,
pengwang91 jed-fill K-series, verise6211 persona/pilk series, Go-Explore red-team (musnet, rank 275),
cdeotte final-cd5 (rank 178), aleaiest 13th-place cdrole-adaptive (rank 161), xiaoz259 CD final (rank 117).
Go-Explore appears once in the whole 705 (no code-read; title-only signal, likely stale).

### Counts summary

- Pulls attempted: 75 (60 top60 + 15 vote15). Succeeded: 74. Failed: 1 (quan0095, 400, private or deleted).
- Technique rows written: 75 (60 + 15, incl 1 ERROR row). Metadata-only rows: 630 (by reference in CSV).
- Field coverage: 705 / 705 refs accounted for. No ref was dropped.
