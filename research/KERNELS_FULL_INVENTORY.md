# KERNELS FULL INVENTORY - AI Agent Security Multi-Step Tool Attacks

Date: 2026-09-05. Total kernels listed: 705. Files: research/kernels_score_desc_p1..p8.json + kernels_vote_p1/p2.json + kernels_hot_p1/p2.json + kernels_ALL_REFS.csv (705 dedup refs).

## Method and score limitation (read first)

1. Fetched via kaggle kernels list --competition ai-agent-security-multi-step-tool-attacks --page-size 100 -p N --sort-by scoreDescending --format json, pages 1-8 (100+100+100+100+100+100+100+5 = 705). API caps effective page at 100 despite documented max 200, so page-size 200 calls also returned 100.
2. Also fetched --sort-by voteCount p1-p2 (200 refs) and --sort-by hotness p1-p2 (200 refs): deduplicated union added 0 new refs beyond the score sort, so 705 is the complete public set reachable by the API.
3. LIMITATION: kernels list does NOT return numeric scores. Rank order under scoreDescending is the server best-score order, but exact scores are not exposed. Numeric scores below are VERBATIM only where captured in prior research or notebook titles. All other rows carry INFERRED rank order only.
4. Score sources: research/open_source_top50.md, research/kaggle/public_notebooks.md, research/raw_discussions/code_tab.txt, notebooks/extracted (17 txt), research/VERY_DETAILED_REPORT V1-V4, research/INVENTORY_EVERY_SOLUTION.md, plus 2 websearch rounds 2026-09-05 (competition overview scoring formula, 1st-place CD-only writeup 44.5 to 46.5, faresrafat portfolio 76.995, relay-push100 v7 Devpost).
5. Title-embedded numbers (95.130, 66.015, 60.525, 60.435, 22.155) are author self-claims, NOT Kaggle-verified. Pre-refresh frozen scores (90.54 etc.) are not comparable to post-refresh (LB invalidated 2026-08-07 per disc 733058) or private-era Sept-2026 scores.

## Top 50 by scoreDescending (inferred rank + verbatim scores where known)

| rank | ref | title | votes | score note |
|---|---|---|---|---|
| 1 | konbu17/jed-attack-exp093 | JED Attack exp093 | 8 | INFERRED rank order only, no verbatim score |
| 2 | outliar/agi-exfil-160-gpt500-gem2000-sub | agi-exfil-160-gpt500-gem2000_sub | 1 | INFERRED rank order only, no verbatim score |
| 3 | sebastianmateus/replayforge-k8-correctness-router-0824 | ReplayForge K8 Correctness Router 0824 | 1 | INFERRED rank order only, no verbatim score |
| 4 | aleaiest/aisec-n38urllast | aisec-n38urllast | 1 | INFERRED rank order only, no verbatim score |
| 5 | xiangwaaaaa/notebook93b16cbbf4 | notebook93b16cbbf4 | 0 | INFERRED rank order only, no verbatim score |
| 6 | hiranorm/publiclb-95-130-privatelb-0-00-aas-mf-k8-ff-test | [publicLB:95.130,privateLB:0.00]aas-mf-k8-ff-test | 1 | INFERRED rank order only, no verbatim score |
| 7 | samwiz/aas-v15-gpu | AAS v15 GPU | 1 | INFERRED rank order only, no verbatim score |
| 8 | nkosindwandwe/jed-attack-multi-step | JED Attack Multi-Step | 0 | INFERRED rank order only, no verbatim score |
| 9 | merkiraz/v8-hybrid-frame-gpt-oss-biraz-daha-agresif-r | v8 hybrid + FRAME (gpt_oss) + biraz daha agresif R | 0 | INFERRED rank order only, no verbatim score |
| 10 | merkiraz/jed-v35-uniquecellmax-v1 | jed-v35-uniquecellmax-v1 | 0 | INFERRED rank order only, no verbatim score |
| 11 | foysalemonshanto/ai-agent-security-v15 | AI Agent Security V15 | 546 | 90.54 VERBATIM V15 3-probe family, pre-freeze frozen |
| 12 | eugeneyeung/ai-agent-security-fillmax-m34-f099 | AI Agent Security fillmax_m34_f099 | 4 | INFERRED rank order only, no verbatim score |
| 13 | sirikilohit/agent-sec-tool-atk-v170-winner | agent_sec_tool_atk_v170_winner | 0 | INFERRED rank order only, no verbatim score |
| 14 | aqibrazadev/maximum-throughput-attack-code | MAXIMUM THROUGHPUT Attack Code | 1 | INFERRED rank order only, no verbatim score |
| 15 | evgendvorkin/ai-agent | AI Agent | 371 | INFERRED rank order only, no verbatim score |
| 16 | malikhammadfarooq/jed-attack-v38-slowest-1-29 | Jed Attack V38: Slowest 1.29 | 0 | INFERRED rank order only, no verbatim score |
| 17 | foysalemonshanto/ai-agent-security-v12 | AI Agent Security V12 | 317 | INFERRED rank order only, no verbatim score |
| 18 | nctuan/jed-v25 | JED - v25 | 170 | 89.145 Gold VERBATIM code_tab |
| 19 | dimong4/ai-agent-security | AI Agent Security | 426 | INFERRED rank order only, no verbatim score |
| 20 | kaiwalyaatulraut/ai-agent-security-solution | AI Agent Security Solution | 122 | INFERRED rank order only, no verbatim score |
| 21 | adhirajjagtap/probe-and-flood-strategy | Probe-and-Flood Strategy | 116 | 88.695 peak VERBATIM V2 s4 row5 |
| 22 | danischaparov/ai-agent-security-v12 | AI Agent Security V12 | 1 | INFERRED rank order only, no verbatim score |
| 23 | farbricated/confused-deputy | Confused Deputy | 1 | INFERRED rank order only, no verbatim score |
| 24 | canqiang/aiagsec-ea-b-0721 | AIAgSec Ea B 0721 | 273 | INFERRED rank order only, no verbatim score |
| 25 | tetsutani/ai-agent-sec-adaptive-uniform-two-probe-recovery | AI Agent Sec Adaptive Uniform Two Probe Recovery | 217 | 88.470 VERBATIM 2-probe, same-bytes 88.515/89.055 |
| 26 | kaiwalyaatulraut/ai-agent-security-competition-solution | AI Agent Security Competition Solution | 135 | INFERRED rank order only, no verbatim score |
| 27 | anasriaz/ai-agent-security | AI Agent Security  | 108 | INFERRED rank order only, no verbatim score |
| 28 | rokaiyasomapti/ai-agent-sec-another-approach-resubmission | AI Agent Sec / Another Approach (Resubmission) | 142 | INFERRED rank order only, no verbatim score |
| 29 | haodou092/notebookcb9f3b04b6 | notebookcb9f3b04b6 | 106 | INFERRED rank order only, no verbatim score |
| 30 | maqsoudtawaliou/aas-attack-exp9 | AAS Attack Exp9 | 0 | INFERRED rank order only, no verbatim score |
| 31 | nctuan/jed-slow-multipost | JED - Slow multipost | 154 | 86.605 Bronze VERBATIM code_tab |
| 32 | haodou092/conservative-replay-safe-sizing | Conservative Replay-Safe Sizing | 124 | 51.25-52 band, V2 row16 |
| 33 | lopure/jed-multi-step-attack-relay-push100 | JED Multi Step Attack RELAY PUSH100 | 69 | INFERRED rank order only, no verbatim score |
| 34 | naveenvenubagadi/ai-agent-security-exfil-primary-v2 | AI Agent Security - Exfil Primary v2 | 0 | INFERRED rank order only, no verbatim score |
| 35 | yusuketogashi/ai-agent-sec-another-approach | AI Agent Sec / Another Approach 🧭 | 182 | INFERRED rank order only, no verbatim score |
| 36 | anvithpothula/aisec-pilk | AISec Pilk | 86 | 85.41 Bronze VERBATIM code_tab |
| 37 | caoyupeng/jed-multi-step-attack-2 | JED Multi Step Attack 2 | 33 | INFERRED rank order only, no verbatim score |
| 38 | diladiclekeke/working-note-ai-agent-security | Working Note AI Agent Security | 0 | INFERRED rank order only, no verbatim score |
| 39 | pilkwang/ai-agent-v3-1-2-single-post-exfiltration | AI Agent v3.1.2 - Single-Post Exfiltration | 189 | 88.9 VERBATIM fill-efficiency stack V2 row17 |
| 40 | mehdielm/jed-attack-budget-aware-portfolio-search | JED Attack - budget-aware portfolio search | 0 | INFERRED rank order only, no verbatim score |
| 41 | biohack44/jed-multi-step-attack-3753a0 | JED Multi Step Attack 3753a0 | 6 | INFERRED rank order only, no verbatim score |
| 42 | raunakdey07/ai-agent-security-adaptive-template-race | AI Agent Security — Adaptive Template Race | 1 | INFERRED rank order only, no verbatim score |
| 43 | godofthunder2407/ai-agent-sec | AI Agent Sec  | 3 | INFERRED rank order only, no verbatim score |
| 44 | faresrafat/notebook85c5782962 | notebook85c5782962 | 2 | 76.995 VERBATIM V6 faresrafat portfolio, pre-refresh stale (websearch-verified) |
| 45 | clemendes/borapracima-v1 | borapracima_v1 | 2 | INFERRED rank order only, no verbatim score |
| 46 | aratisantoshshinde/ai-agent-security-adaptive-tool-call-throughput-se | AI Agent Security Adaptive Tool-Call Throughput Se | 1 | INFERRED rank order only, no verbatim score |
| 47 | tiktoktrendz/jed-submission | JED 🐐 Submission  | 31 | INFERRED rank order only, no verbatim score |
| 48 | pengwang91/jed-fill-v26-replaysafe | jed-fill-v26-replaysafe | 24 | INFERRED rank order only, no verbatim score |
| 49 | caoyupeng/lb-66-015-from-kun-zhang | LB【66.015】from Kun Zhang | 51 | TITLE-CLAIMED 66.015 in title, self-reported |
| 50 | naveenvenubagadi/ai-attack-probe | ai-attack-probe | 0 | INFERRED rank order only, no verbatim score |

Ranks 26-30, 33-35, 37-38, 40-43, 45-48, 50 have no verbatim public score in prior research or websearch: 26 competition-solution THIN dump, 27 anasriaz, 28 resubmission 142 votes, 29 notebookcb9f3b04b6 106 votes, 30 exp9, 33 relay-push100 v7-linear-base family per Devpost, 34 exfil-primary-v2, 35 another-approach 182 votes, 37 multi-step-attack-2, 38 working-note, 40 budget-aware-portfolio, 41 3753a0, 42 adaptive-template-race, 43 ai-agent-sec, 45 borapracima, 46 throughput-se, 47 jed-submission 31 votes, 48 jed-fill-v26-replaysafe, 50 ai-attack-probe.
Rank 6 hiranorm title claims publicLB 95.130 privateLB 0.00 (self-claimed, not Kaggle-verified). Rank 23 farbricated/confused-deputy is CD family, private-relevant per 2026-09-02 1st-place writeup (CD only reliable route, 44.5 to 46.5 via GCG hop-2 EOG).

## Full table - all 705 kernels (sortRank = scoreDescending order)

Columns: sortRank | ref | title | author | lastRunTime | totalVotes | score note (VERBATIM/TITLE-CLAIMED/FAMILY or dash = inferred order only).

| sortRank | ref | title | author | lastRunTime | votes | score note |
|---|---|---|---|---|---|---|
| 1 | konbu17/jed-attack-exp093 | JED Attack exp093 | konbu17 | 2026-09-01T10:04:00.577000 | 8 | - |
| 2 | outliar/agi-exfil-160-gpt500-gem2000-sub | agi-exfil-160-gpt500-gem2000_sub | Mohammad Shadab Alam | 2026-08-28T09:30:23.303000 | 1 | - |
| 3 | sebastianmateus/replayforge-k8-correctness-router-0824 | ReplayForge K8 Correctness Router 0824 | Sebastian Mateus | 2026-08-24T12:01:18.267000 | 1 | - |
| 4 | aleaiest/aisec-n38urllast | aisec-n38urllast | Taewoong Kim | 2026-08-27T05:03:16.953000 | 1 | - |
| 5 | xiangwaaaaa/notebook93b16cbbf4 | notebook93b16cbbf4 | xiang W | 2026-08-31T00:16:59.620000 | 0 | - |
| 6 | hiranorm/publiclb-95-130-privatelb-0-00-aas-mf-k8-ff-test | [publicLB:95.130,privateLB:0.00]aas-mf-k8-ff-test | Hira Norm | 2026-08-20T08:54:20.353000 | 1 | TITLE-CLAIMED 95.130 pub 0.00 priv |
| 7 | samwiz/aas-v15-gpu | AAS v15 GPU | Sam-wiz | 2026-09-01T05:32:59.570000 | 1 | - |
| 8 | nkosindwandwe/jed-attack-multi-step | JED Attack Multi-Step | The light that shines | 2026-08-15T19:29:33.370000 | 0 | - |
| 9 | merkiraz/v8-hybrid-frame-gpt-oss-biraz-daha-agresif-r | v8 hybrid + FRAME (gpt_oss) + biraz daha agresif R | ömer kiraz | 2026-08-29T17:18:33.907000 | 0 | - |
| 10 | merkiraz/jed-v35-uniquecellmax-v1 | jed-v35-uniquecellmax-v1 | ömer kiraz | 2026-09-01T07:09:23.720000 | 0 | - |
| 11 | foysalemonshanto/ai-agent-security-v15 | AI Agent Security V15 | FOYSAL | 2026-08-04T17:40:16.763000 | 546 | 90.54 VERBATIM V15 |
| 12 | eugeneyeung/ai-agent-security-fillmax-m34-f099 | AI Agent Security fillmax_m34_f099 | EUGENEYEUNG | 2026-09-02T12:31:36.373000 | 4 | - |
| 13 | sirikilohit/agent-sec-tool-atk-v170-winner | agent_sec_tool_atk_v170_winner | rellik13 | 2026-08-30T16:21:31.337000 | 0 | - |
| 14 | aqibrazadev/maximum-throughput-attack-code | MAXIMUM THROUGHPUT Attack Code | Aqib Raza | 2026-09-01T20:39:57.237000 | 1 | - |
| 15 | evgendvorkin/ai-agent | AI Agent | Дворкин Евгений Владимирович | 2026-08-31T18:06:32.470000 | 371 | - |
| 16 | malikhammadfarooq/jed-attack-v38-slowest-1-29 | Jed Attack V38: Slowest 1.29 | Hammad Farooq | 2026-08-30T06:26:50.647000 | 0 | - |
| 17 | foysalemonshanto/ai-agent-security-v12 | AI Agent Security V12 | FOYSAL | 2026-07-25T04:07:34.263000 | 317 | - |
| 18 | nctuan/jed-v25 | JED - v25 | Nguyễn Công Tuấn | 2026-07-30T03:55:44.803000 | 170 | 89.145 Gold VERBATIM |
| 19 | dimong4/ai-agent-security | AI Agent Security | Dmitry Belan | 2026-08-16T14:45:13.587000 | 426 | - |
| 20 | kaiwalyaatulraut/ai-agent-security-solution | AI Agent Security Solution | KAIWALYA RAUT | 2026-07-23T15:37:26.337000 | 122 | - |
| 21 | adhirajjagtap/probe-and-flood-strategy | Probe-and-Flood Strategy | Adhiraj Jagtap | 2026-08-22T04:44:26.357000 | 116 | 88.695 peak VERBATIM |
| 22 | danischaparov/ai-agent-security-v12 | AI Agent Security V12 | karnezz | 2026-09-01T10:46:57.247000 | 1 | - |
| 23 | farbricated/confused-deputy | Confused Deputy | Farbricated | 2026-08-16T15:39:37.953000 | 1 | FAMILY CD private-relevant |
| 24 | canqiang/aiagsec-ea-b-0721 | AIAgSec Ea B 0721 | Xander | 2026-07-21T06:31:44.707000 | 273 | - |
| 25 | tetsutani/ai-agent-sec-adaptive-uniform-two-probe-recovery | AI Agent Sec Adaptive Uniform Two Probe Recovery | tetsu2131 | 2026-07-26T16:45:41.237000 | 217 | 88.470 VERBATIM |
| 26 | kaiwalyaatulraut/ai-agent-security-competition-solution | AI Agent Security Competition Solution | KAIWALYA RAUT | 2026-08-13T11:37:47.210000 | 135 | - |
| 27 | anasriaz/ai-agent-security | AI Agent Security  | Anas Riaz | 2026-08-29T19:06:44.697000 | 108 | - |
| 28 | rokaiyasomapti/ai-agent-sec-another-approach-resubmission | AI Agent Sec / Another Approach (Resubmission) | RS | 2026-07-18T00:45:20.977000 | 142 | - |
| 29 | haodou092/notebookcb9f3b04b6 | notebookcb9f3b04b6 | haodou092 | 2026-07-18T12:06:16.493000 | 106 | - |
| 30 | maqsoudtawaliou/aas-attack-exp9 | AAS Attack Exp9 | Maqsoud Tawaliou | 2026-08-16T05:48:42.573000 | 0 | - |
| 31 | nctuan/jed-slow-multipost | JED - Slow multipost | Nguyễn Công Tuấn | 2026-08-04T03:37:04.947000 | 154 | 86.605 Bronze VERBATIM |
| 32 | haodou092/conservative-replay-safe-sizing | Conservative Replay-Safe Sizing | haodou092 | 2026-07-20T01:52:09.413000 | 124 | 51.25-52 band V2row16 |
| 33 | lopure/jed-multi-step-attack-relay-push100 | JED Multi Step Attack RELAY PUSH100 | Who am I? | 2026-08-30T02:30:45.927000 | 69 | FAMILY v7-linear-base |
| 34 | naveenvenubagadi/ai-agent-security-exfil-primary-v2 | AI Agent Security - Exfil Primary v2 | Naveen Venu Bagadi | 2026-08-23T17:35:12.310000 | 0 | - |
| 35 | yusuketogashi/ai-agent-sec-another-approach | AI Agent Sec / Another Approach 🧭 | Yusuke Togashi | 2026-07-19T21:31:40.777000 | 182 | - |
| 36 | anvithpothula/aisec-pilk | AISec Pilk | Anvith Pothula | 2026-07-21T19:11:34.547000 | 86 | 85.41 Bronze VERBATIM |
| 37 | caoyupeng/jed-multi-step-attack-2 | JED Multi Step Attack 2 | SpeedSci | 2026-07-16T18:27:54.517000 | 33 | - |
| 38 | diladiclekeke/working-note-ai-agent-security | Working Note AI Agent Security | dila dicle kekec | 2026-08-31T21:38:34.357000 | 0 | - |
| 39 | pilkwang/ai-agent-v3-1-2-single-post-exfiltration | AI Agent v3.1.2 - Single-Post Exfiltration | Pilkwang Kim | 2026-07-24T06:05:01.873000 | 189 | 88.9 VERBATIM |
| 40 | mehdielm/jed-attack-budget-aware-portfolio-search | JED Attack - budget-aware portfolio search | Mehdi El Mouttaki | 2026-08-31T11:11:56.747000 | 0 | - |
| 41 | biohack44/jed-multi-step-attack-3753a0 | JED Multi Step Attack 3753a0 | Emre Cirak | 2026-07-16T09:24:52.993000 | 6 | - |
| 42 | raunakdey07/ai-agent-security-adaptive-template-race | AI Agent Security — Adaptive Template Race | Raunak Dey | 2026-09-01T17:33:28.870000 | 1 | - |
| 43 | godofthunder2407/ai-agent-sec | AI Agent Sec  | GodofThunder2407 | 2026-07-19T05:32:20.410000 | 3 | - |
| 44 | faresrafat/notebook85c5782962 | notebook85c5782962 | Fares Rafat | 2026-07-16T09:45:37.847000 | 2 | 76.995 VERBATIM V6 stale |
| 45 | clemendes/borapracima-v1 | borapracima_v1 | byCMF | 2026-07-18T01:21:44.620000 | 2 | - |
| 46 | aratisantoshshinde/ai-agent-security-adaptive-tool-call-throughput-se | AI Agent Security Adaptive Tool-Call Throughput Se | ARATI SHINDE | 2026-07-21T17:02:40.650000 | 1 | - |
| 47 | tiktoktrendz/jed-submission | JED 🐐 Submission  | patchmeifucan.ko | 2026-07-24T03:51:25.067000 | 31 | - |
| 48 | pengwang91/jed-fill-v26-replaysafe | jed-fill-v26-replaysafe | Peng Wang | 2026-07-13T02:08:05.020000 | 24 | - |
| 49 | caoyupeng/lb-66-015-from-kun-zhang | LB【66.015】from Kun Zhang | SpeedSci | 2026-07-12T04:37:53.243000 | 51 | TITLE-CLAIMED 66.015 |
| 50 | naveenvenubagadi/ai-attack-probe | ai-attack-probe | Naveen Venu Bagadi | 2026-08-26T16:26:12.343000 | 0 | - |
| 51 | lucifer19/shadow-cat-firewall | 🐈‍⬛⚡ Shadow Cat Firewall | Krizsó Gergely | 2026-07-18T07:51:20.777000 | 74 | - |
| 52 | lucifer19/jed-strategy-sentinel | ⚡🧿 JED Strategy Sentinel | Krizsó Gergely | 2026-07-16T06:29:57.487000 | 28 | - |
| 53 | llccqq624/shadow-cat-firewall | 🐈‍⬛⚡ Shadow Cat Firewall | Jiachen Li | 2026-07-12T14:15:52.263000 | 9 | - |
| 54 | quan0095/security-eval-edge-fill | Security Eval Edge Fill | Quan Vu | 2026-07-13T04:23:24.167000 | 5 | - |
| 55 | boristown/shadow-cat-firewall-darkagi-edited | 🐈‍⬛⚡ Shadow Cat Firewall - DarkAGI Edited | 暗黑AGI | 2026-07-13T00:35:35.423000 | 9 | - |
| 56 | canqiang/aiagsec-submission | AIAgSec Submission | Xander | 2026-07-17T12:53:15.090000 | 82 | - |
| 57 | devchandra/ai-agent-security-v83-assia-live-fill-m37 | AI Agent Security v83 Assia Live Fill M37 | Dr Chandrasen Pandey | 2026-07-11T12:42:08.393000 | 1 | - |
| 58 | yusuketogashi/lb60-525-july-safe-edge-prune-tail8-upgrade | LB60.525 July Safe Edge-Prune 🛡️ / Tail8 Upgrade | Yusuke Togashi | 2026-07-08T01:01:11.700000 | 138 | - |
| 59 | devchandra/ai-agent-security-v75-yusuke-lb60525-margin32 | AI Agent Security v75 Yusuke LB60525 margin32 | Dr Chandrasen Pandey | 2026-07-10T16:08:45.630000 | 3 | - |
| 60 | caoyupeng/v23-alpha2co-667-break60 | V23 Alpha2CO 667 Break60 | SpeedSci | 2026-06-22T02:49:18.317000 | 94 | - |
| 61 | devchandra/ai-agent-security-v70-yusuke-tail8-margin32 | AI Agent Security v70 Yusuke tail8 margin32 | Dr Chandrasen Pandey | 2026-07-07T03:03:22.513000 | 1 | - |
| 62 | yaroslavkholmirzayev/ai-agent-security-k1-short | AI Agent Security / k1-short | Yaroslav kholmirzayev | 2026-06-24T18:58:34.707000 | 111 | - |
| 63 | uctpexx123/aas-kun-lb66015-official-v1 | AAS Kun LB66015 Official V1 | uctpexx123 | 2026-07-20T03:17:18.670000 | 14 | - |
| 64 | rumblingb/ai-security-lb60120-yusuke-fork-20260706 | AI Security LB60120 Yusuke Fork 20260706 | rumbling_b | 2026-07-06T17:42:46.173000 | 7 | - |
| 65 | qyq1693/ai-agent-security-dense-v9 | ai-agent-security-dense-v9 | QYQ1693 | 2026-07-15T03:00:39.630000 | 4 | - |
| 66 | pilkwang/ai-agent-working-note |  AI Agent - 📘 Working Note | Pilkwang Kim | 2026-07-05T03:18:45.847000 | 159 | - |
| 67 | kokinnwakashuu/ai-agent-security-working-diary | AI Agent Security - Working Diary | kokinnwakashuu | 2026-06-25T09:36:58.600000 | 77 | - |
| 68 | boristown/agi-ai-agent-security | 【暗黑AGI】AI Agent Security | 暗黑AGI | 2026-06-21T08:24:20.167000 | 129 | - |
| 69 | caoyupeng/ai-agent-security-v22-urlcompact-642 | AI Agent Security - V22 URLCompact 642 | SpeedSci | 2026-06-21T07:19:21.427000 | 48 | - |
| 70 | verise6211/aas-pilk-gx2 | aas-pilk-gx2 | verise6211 | 2026-07-07T13:37:48.800000 | 8 | - |
| 71 | lucifer19/cognitive-firewall | 🧠🛡️ Cognitive Firewall | Krizsó Gergely | 2026-07-18T07:16:57.437000 | 90 | - |
| 72 | yaroslavkholmirzayev/replay-dense-boundary-exact-aggressive | Replay Dense Boundary Exact + Aggressive | Yaroslav kholmirzayev | 2026-06-22T11:08:20.077000 | 104 | - |
| 73 | verise6211/aas-pilk-gx1 | aas-pilk-gx1 | verise6211 | 2026-07-06T15:34:00.500000 | 4 | - |
| 74 | devchandra/ai-agent-security-v65b-yusuke-lb60-margin32 | AI Agent Security v65b Yusuke LB60 margin32 | Dr Chandrasen Pandey | 2026-07-06T01:16:26.667000 | 6 | - |
| 75 | rumblingb/ai-security-shadow-cat-stable-boost-20260708 | AI Security Shadow Cat Stable Boost 20260708 | rumbling_b | 2026-07-08T20:12:26.913000 | 1 | - |
| 76 | imbikramsaha/ai-agent-security-v10-score-56-87 | AI Agent Security - v10 / Score-56.87 | Bikram Saha | 2026-06-20T17:26:49.933000 | 13 | - |
| 77 | pilkwang/ai-agent-replay-dense-exfiltration | AI Agent: Replay-Dense Exfiltration | Pilkwang Kim | 2026-06-16T09:52:13.737000 | 231 | - |
| 78 | blacklions/ai-agent-replay-dense-exfiltration | AI Agent: Replay-Dense Exfiltration | 陈耀洋 | 2026-06-18T13:31:38.190000 | 25 | - |
| 79 | berkahkarya/ai-agent-security-attack-v52 | ai-agent-security-attack-v52 | Berkahkarya Dev | 2026-06-21T16:07:23.207000 | 1 | - |
| 80 | berkahkarya/ai-agent-security-attack-v53 | ai-agent-security-attack-v53 | Berkahkarya Dev | 2026-06-21T20:35:13.963000 | 1 | - |
| 81 | akshitasrivastava1/omega-attack-v8-2-static-no-probe | omega attack v8 2 static no probe | Akshita Srivastava | 2026-06-21T18:10:58.480000 | 3 | - |
| 82 | pengwang91/jed-fill-a2-mechanical | jed-fill-a2-mechanical | Peng Wang | 2026-07-06T02:23:23.947000 | 3 | - |
| 83 | devchandra/ai-agent-security-v64-yusuke-lb60-safe-exact | AI Agent Security v64 Yusuke LB60 safe exact | Dr Chandrasen Pandey | 2026-07-06T01:14:53.670000 | 1 | - |
| 84 | sumangnalla/project-agent-security | PROJECT AGENT SECURITY | NALLA SUMANG | 2026-07-17T00:22:32.147000 | 8 | - |
| 85 | pengwang91/jed-fill-mech-noval-m35 | jed-fill-mech-noval-m35 | Peng Wang | 2026-07-06T22:37:37.750000 | 1 | - |
| 86 | devchandra/ai-agent-security-v76b-shadowcat-stable-boost | AI Agent Security v76b Shadowcat stable boost | Dr Chandrasen Pandey | 2026-07-10T16:19:36.940000 | 2 | - |
| 87 | verise6211/aas-pilk-a3 | aas-pilk-a3 | verise6211 | 2026-07-06T00:10:23.923000 | 1 | - |
| 88 | pengwang91/jed-fill-post-terse | jed-fill-post-terse | Peng Wang | 2026-07-06T02:23:59.593000 | 2 | - |
| 89 | devchandra/ai-agent-security-v67b-pilkwang-jul5-56-6 | AI Agent Security v67b Pilkwang Jul5 56.6 | Dr Chandrasen Pandey | 2026-07-06T01:18:47.960000 | 6 | - |
| 90 | verise6211/aas-adaptive-e2e | aas-adaptive-e2e | verise6211 | 2026-07-10T07:09:20.927000 | 3 | - |
| 91 | pengwang91/jed-fill-a2-base | jed-fill-a2-base | Peng Wang | 2026-07-06T02:22:48.703000 | 2 | - |
| 92 | caoyupeng/fork-from-ai-agent-security | Fork from AI Agent Security | SpeedSci | 2026-06-18T03:43:55.387000 | 9 | - |
| 93 | hongdaekim/deep-battle-atk | deep_battle_atk | Hong Dae Kim | 2026-07-09T20:54:25.323000 | 1 | - |
| 94 | devchandra/ai-agent-security-v69b-yusuke-lb60435-tail8 | AI Agent Security v69b Yusuke LB60435 tail8 | Dr Chandrasen Pandey | 2026-07-07T03:00:36.880000 | 2 | - |
| 95 | alt0er/ai-agent-security-fresh | AI Agent Security Fresh | Pratik Acharya | 2026-07-17T02:37:51.947000 | 6 | - |
| 96 | rauffauzanrambe/security-agresive-multi-attack-with-agents-ai | Security Agresive Multi Attack with Agents AI | Ra'uf Fauzan Rambe | 2026-06-18T08:07:37.193000 | 6 | - |
| 97 | tkhanna96/h006-pilkwang-580 | H006 Pilkwang 580 | Tkhanna96 | 2026-06-23T07:17:14.343000 | 7 | - |
| 98 | paul720810/hermes-attack-v69-proven-code-20260721-052046 | Hermes Attack v69-proven-code-20260721-052046 | Paul720810 | 2026-07-21T05:20:49.097000 | 1 | - |
| 99 | paul720810/hermes-attack-v71-n1000-20260721-102018 | Hermes Attack v71-n1000-20260721-102018 | Paul720810 | 2026-07-21T10:20:21.030000 | 6 | - |
| 100 | malikhammadfarooq/multi-step-tool-attacks-replay-aware-exfil | Multi-Step Tool Attacks — Replay-Aware Exfil | Hammad Farooq | 2026-08-27T09:20:16.733000 | 0 | - |
| 101 | pengwang91/jed-fill-yusuke-m50 | jed-fill-yusuke-m50 | Peng Wang | 2026-07-06T02:21:37.913000 | 2 | - |
| 102 | caoyupeng/real-submission-fork-from-pilkwang-changed | [real submission]Fork from pilkwang-changed | SpeedSci | 2026-07-01T16:16:04.887000 | 10 | - |
| 103 | evilyevihut/ai-agent-security-fast-safe-560 | AI Agent Security Fast Safe 560 | Zhang.ZJ | 2026-06-20T16:16:54.597000 | 6 | - |
| 104 | paul720810/hermes-attack-v58-pure-n1000-std-20260719-002444 | Hermes Attack v58-pure-n1000-std-20260719-002444 | Paul720810 | 2026-07-19T00:24:48.733000 | 2 | - |
| 105 | paul720810/hermes-attack-v59-pure-n1100-std-20260719-002609 | Hermes Attack v59-pure-n1100-std-20260719-002609 | Paul720810 | 2026-07-19T00:26:13.347000 | 2 | - |
| 106 | pengwang91/jed-fill-yusuke-m44 | jed-fill-yusuke-m44 | Peng Wang | 2026-07-06T02:22:13.807000 | 2 | - |
| 107 | paul720810/hermes-attack-v70-n900-20260721-101920 | Hermes Attack v70-n900-20260721-101920 | Paul720810 | 2026-07-21T10:19:24.107000 | 4 | - |
| 108 | malikhammadfarooq/per-post-exfil-budget-sized | Per-Post EXFIL, Budget-Sized | Hammad Farooq | 2026-08-28T16:46:39.417000 | 0 | - |
| 109 | kashyapsinhgohil/multi-step-tool |  Multi-Step Tool | Kashyapsinh gohil | 2026-08-27T13:17:52.687000 | 0 | - |
| 110 | devchandra/ai-agent-security-v66b-yusuke-lb60-bare-m37 | AI Agent Security v66b Yusuke LB60 bare m37 | Dr Chandrasen Pandey | 2026-07-06T01:17:46.913000 | 5 | - |
| 111 | karnakbaevarthur/multi-endpoint-severity-stacker | Multi Endpoint Severity Stacker  | Karnakbayev Artur | 2026-06-16T05:28:20.557000 | 118 | - |
| 112 | verityix/ai-agent-security-attack-algorithm-hitherto | AI Agent Security — Attack Algorithm (Hitherto) | Verity IX | 2026-09-01T22:43:29.540000 | 30 | - |
| 113 | berkahkarya/ai-agent-security-v50-probe-verify-attack | AI Agent Security - v50 Probe-Verify Attack | Berkahkarya Dev | 2026-06-19T20:11:26.260000 | 3 | - |
| 114 | yaroslavkholmirzayev/ai-agent-security-achieve-and-validate | AI Agent Security / achieve and validate 🌀 | Yaroslav kholmirzayev | 2026-06-30T09:23:24.307000 | 29 | - |
| 115 | arizalfirdaus123/multi-turn-exfiltration-with-adaptive-burst | Multi-Turn Exfiltration with Adaptive Burst | Arizal Muluk | 2026-07-02T09:14:05.297000 | 62 | - |
| 116 | evilyevihut/ai-agent-security-fast-safe-520 | AI Agent Security Fast Safe 520 | Zhang.ZJ | 2026-06-19T08:32:42.957000 | 3 | - |
| 117 | xiaoz259/aas-final-submission-cd | AAS / Final Submission - CD | xz | 2026-09-01T09:42:11.557000 | 6 | - |
| 118 | paul720810/hermes-attack-v55-n1050-std-20260718-002905 | Hermes Attack v55-n1050-std-20260718-002905 | Paul720810 | 2026-07-18T00:29:10.627000 | 1 | - |
| 119 | geokocha/replay-dense-exfiltration-first-submission | Replay-Dense Exfiltration — First Submission | Yuanchen Huang | 2026-06-16T09:05:13.850000 | 6 | - |
| 120 | junaid512/anatomy-of-an-agentic-jailbreak | Anatomy of an Agentic Jailbreak  | Muhammad Junaid | 2026-06-23T10:55:48.543000 | 1 | - |
| 121 | paul720810/hermes-attack-v52-replicate-20260717-001828 | Hermes Attack v52-replicate-20260717-001828 | Paul720810 | 2026-07-17T00:18:32.473000 | 1 | - |
| 122 | rikitomo0526/ai-agent-security-attack-script-exp021 | AI Agent Security - Attack script exp021 | Rick | 2026-08-31T14:23:23.270000 | 4 | - |
| 123 | paul720810/hermes-attack-v38-pure-n950-20260713-200926 | Hermes Attack v38-pure-n950-20260713-200926 | Paul720810 | 2026-07-13T20:09:29.480000 | 1 | - |
| 124 | paul720810/hermes-attack-v49-pure-n950-m1p05-20260717-001515 | Hermes Attack v49-pure-n950-m1p05-20260717-001515 | Paul720810 | 2026-07-17T00:15:18.323000 | 1 | - |
| 125 | malikhammadfarooq/jed-x-adaptive-trace-guided-attack-search | JED-X: Adaptive Trace-Guided Attack Search | Hammad Farooq | 2026-08-25T10:29:38.847000 | 0 | - |
| 126 | paul720810/hermes-attack-v50-pure-n950-m1p15-20260717-001610 | Hermes Attack v50-pure-n950-m1p15-20260717-001610 | Paul720810 | 2026-07-17T00:16:15.720000 | 1 | - |
| 127 | isakatsuyoshi/jed-clean-email-rick-use-allcaps-n2000 | JED clean email Rick USE allcaps N2000 | ISAKA Tsuyoshi | 2026-08-30T12:47:19.800000 | 2 | - |
| 128 | jek1wantaufik/tool-attack-submission | Tool Attack Submission | Jeki Wan Taufik | 2026-06-15T18:48:13.547000 | 23 | - |
| 129 | pengwang91/jed-cleanimp445-marker | jed-cleanimp445-marker | Peng Wang | 2026-07-05T01:05:51.777000 | 2 | - |
| 130 | kleniopadilha/winnex-v61-attack | WINNEX V61 Attack | Klenio Padilha | 2026-07-13T14:50:11.160000 | 1 | - |
| 131 | paul720810/hermes-attack-v51-pure-n950-m1p2-20260717-001708 | Hermes Attack v51-pure-n950-m1p2-20260717-001708 | Paul720810 | 2026-07-17T00:17:13.390000 | 1 | - |
| 132 | paul720810/hermes-attack-v39-pure-n1000-tight-20260716-002217 | Hermes Attack v39-pure-n1000-tight-20260716-002217 | Paul720810 | 2026-07-16T00:22:21.930000 | 1 | - |
| 133 | pengwang91/jed-cleanimp430-marker | jed-cleanimp430-marker | Peng Wang | 2026-07-05T01:05:16.753000 | 2 | - |
| 134 | paul720810/hermes-attack-v53-n1200-framing-20260718-002659 | Hermes Attack v53-n1200-framing-20260718-002659 | Paul720810 | 2026-07-18T00:27:03.317000 | 1 | - |
| 135 | pengwang91/jed-cleanimp420-marker | jed-cleanimp420-marker | Peng Wang | 2026-07-03T00:49:25.227000 | 3 | - |
| 136 | junaid512/agent-security-attack-submission | Agent-Security Attack Submission | Muhammad Junaid | 2026-07-03T18:25:52.880000 | 62 | - |
| 137 | karnakbaevarthur/dynamic-replay-architecture | Dynamic Replay Architecture | Karnakbayev Artur | 2026-06-18T10:24:40.760000 | 35 | - |
| 138 | paul720810/hermes-attack-v72-m112-20260721-151926 | Hermes Attack v72-m112-20260721-151926 | Paul720810 | 2026-07-21T15:19:30.777000 | 2 | - |
| 139 | paul720810/hermes-attack-v57-n950-naked-url-20260718-003257 | Hermes Attack v57-n950-naked-url-20260718-003257 | Paul720810 | 2026-07-18T00:33:02.153000 | 1 | - |
| 140 | tkhanna96/gemma-k4-gpt-k1-nb | Gemma K4 GPT K1 NB | Tkhanna96 | 2026-06-15T20:53:13.027000 | 4 | - |
| 141 | imbikramsaha/ai-agent-public-score-34-540 | AI Agent / Public Score - 34.540 | Bikram Saha | 2026-06-19T07:15:35.487000 | 4 | - |
| 142 | yw8837/ai-agent-security-34-255-to-8-145-full-code | AI Agent Security: 34.255 to 8.145 / Full Code | yw8837 | 2026-09-02T01:54:07.787000 | 0 | - |
| 143 | verise6211/aas-pilk-a3-k2 | aas-pilk-a3-k2 | verise6211 | 2026-07-06T00:11:07.740000 | 1 | - |
| 144 | paul720810/hermes-openclaw-attack-e005-20260704-041518 | Hermes OpenClaw Attack E005-20260704-041518 | Paul720810 | 2026-07-04T04:15:22.277000 | 1 | - |
| 145 | pratyaymon/notebook289b303504 | notebook289b303504 | Pratyay Mondal | 2026-07-18T14:24:15.057000 | 1 | - |
| 146 | caoyupeng/ai-agent-security-v2-exfil-mass-shift | AI Agent Security - V2 Exfil Mass Shift | SpeedSci | 2026-06-13T16:01:18.113000 | 72 | - |
| 147 | paul720810/hermes-openclaw-attack-v20-20260707-041613 | Hermes OpenClaw Attack v20-20260707-041613 | Paul720810 | 2026-07-07T04:24:07.803000 | 1 | - |
| 148 | yaroslavkholmirzayev/ai-agent-security-v8-9-10-11 | AI Agent Security - V8-9-10-11 | Yaroslav kholmirzayev | 2026-06-13T16:31:44.520000 | 11 | - |
| 149 | tkhanna96/h006-s1-anchor-len60-n400 | H006 S1 Anchor Len60 N400 | Tkhanna96 | 2026-06-20T16:37:51.850000 | 4 | - |
| 150 | paul720810/hermes-openclaw-attack-e005-20260628-001654 | Hermes OpenClaw Attack E005-20260628-001654 | Paul720810 | 2026-06-28T00:16:57.580000 | 4 | - |
| 151 | paul720810/hermes-openclaw-attack-e005-20260630-161123 | Hermes OpenClaw Attack E005-20260630-161123 | Paul720810 | 2026-06-30T16:11:27.837000 | 3 | - |
| 152 | devchandra/ai-agent-security-v25-dual-350 | AI Agent Security V25 Dual 350 | Dr Chandrasen Pandey | 2026-06-19T05:11:16.107000 | 0 | - |
| 153 | paul720810/hermes-openclaw-attack-e005-20260627-060617 | Hermes OpenClaw Attack E005-20260627-060617 | Paul720810 | 2026-06-27T06:06:21.677000 | 4 | - |
| 154 | paul720810/hermes-openclaw-attack-e005-20260627-140935 | Hermes OpenClaw Attack E005-20260627-140935 | Paul720810 | 2026-06-27T14:09:39.207000 | 7 | - |
| 155 | paul720810/hermes-openclaw-attack-e005-20260627-101429 | Hermes OpenClaw Attack E005-20260627-101429 | Paul720810 | 2026-06-27T10:14:32.553000 | 1 | - |
| 156 | rageshthangaraj/defensive-red-teaming | Defensive red-teaming  | Ragesh Thangaraj | 2026-07-09T11:13:22.580000 | 3 | - |
| 157 | paul720810/hermes-openclaw-attack-v19-replica-20260707-122726 | Hermes OpenClaw Attack v19-replica-20260707-122726 | Paul720810 | 2026-07-07T12:27:30.230000 | 3 | - |
| 158 | akshitasrivastava1/omega-attack-v5-0-ai-agent-security | OMEGA ATTACK v5.0 - AI Agent Security | Akshita Srivastava | 2026-06-18T22:04:20.273000 | 3 | - |
| 159 | outliar/agi-deputy-nb1-v11b-gpt2000-gem2000-sub | agi-deputy-nb1-v11b-gpt2000-gem2000_sub | Mohammad Shadab Alam | 2026-08-27T13:27:46.890000 | 0 | - |
| 160 | mayuening/notebookde0d25bc7d | notebookde0d25bc7d | Ma Yuening | 2026-07-05T15:39:32.867000 | 4 | - |
| 161 | aleaiest/13th-aisec-cdrole-adaptive | 🥇 13th: aisec-cdrole-adaptive | Taewoong Kim | 2026-09-02T05:23:21.907000 | 0 | - |
| 162 | paul720810/hermes-openclaw-attack-e005-20260626-161244 | Hermes OpenClaw Attack E005-20260626-161244 | Paul720810 | 2026-06-26T16:12:49.710000 | 8 | - |
| 163 | adonisleu/jed-attack-submission | JED Attack Submission | ElijahMingLiu | 2026-07-04T05:59:03.727000 | 35 | - |
| 164 | verise6211/aas-pilk-a3-k4 | aas-pilk-a3-k4 | verise6211 | 2026-07-06T00:11:49.123000 | 1 | - |
| 165 | kojimar/ai-agent-security-attack-baseline | AI Agent Security Attack Baseline | islet | 2026-06-13T06:01:39.537000 | 26 | - |
| 166 | paul720810/hermes-attack-v34-dual-post-20260715-063801 | Hermes Attack v34-dual-post-20260715-063801 | Paul720810 | 2026-07-15T06:38:04.810000 | 2 | - |
| 167 | mdabdulalhasib/solution-using-very-deep-reaserch | Solution using very deep reaserch | Md Abdul Al Hasib | 2026-06-14T14:47:53.540000 | 9 | - |
| 168 | kashyapsinhgohil/27-3-eda-agent-security-trajectory-search | 27.3-EDA: Agent Security Trajectory Search | Kashyapsinh gohil | 2026-06-13T10:47:06.970000 | 6 | - |
| 169 | pilkwang/eda-agent-security-trajectory-search | EDA: Agent Security Trajectory Search | Pilkwang Kim | 2026-06-13T22:34:19.580000 | 125 | - |
| 170 | junaid512/ai-agent-security-dense-exfiltration-calibrate | AI Agent Security — Dense Exfiltration calibrate  | Muhammad Junaid | 2026-06-24T15:15:13.070000 | 6 | - |
| 171 | yaroslavkholmirzayev/ai-agent-security-trajectory-search | 👾AI Agent Security - Trajectory Search | Yaroslav kholmirzayev | 2026-06-13T08:29:31.747000 | 23 | - |
| 172 | anthonytherrien/agent-security-trajectory | Agent Security Trajectory | AnthonyTherrien | 2026-06-13T11:29:02.027000 | 21 | - |
| 173 | qyq1693/ai-agent-security-multiturn-v14 | ai-agent-security-multiturn-v14 | QYQ1693 | 2026-07-12T08:29:21.547000 | 3 | - |
| 174 | arnavkewalram/ais-attack-notebook | AIS Attack Notebook | Arnav Kewalram | 2026-06-24T11:11:29.803000 | 18 | - |
| 175 | kokinnwakashuu/ai-agent-security-v035-marker-stack | AI Agent Security v035 marker stack | kokinnwakashuu | 2026-07-01T16:15:42.467000 | 3 | - |
| 176 | maximbatykovich/ai-agent | AI Agent | Maxim Batykovich | 2026-06-15T18:47:19.370000 | 11 | - |
| 177 | eugeneyeung/ai-agent-security-private-pp-corp-wide | AI Agent Security Private PP Corp Wide | EUGENEYEUNG | 2026-09-02T12:31:39.857000 | 4 | - |
| 178 | cdeotte/final-cd5 | final-cd5 | Chris Deotte | 2026-09-01T11:22:00.160000 | 12 | - |
| 179 | kkrasikov/workingnote-66th-place-submission | [WorkingNote] 66th place submission | Kirill Krasikov | 2026-09-03T01:47:28.770000 | 2 | - |
| 180 | tatuhelander/jed-attack-forge33-email | JED Attack Forge33 Email | Tatu Helander | 2026-08-30T04:56:56.473000 | 0 | - |
| 181 | adhirajjagtap/omni-stack-multiplier-v25 | OMNI_STACK_MULTIPLIER_V25 | Adhiraj Jagtap | 2026-06-28T15:51:02.503000 | 18 | - |
| 182 | akshitasrivastava1/omega-attack-v9-0-secret-marker-n250 | omega attack v9 0 secret marker n250 | Akshita Srivastava | 2026-06-25T16:01:05.927000 | 7 | - |
| 183 | seungjunleeofficial/aas-v14-cd-only-kaggle-submit | aas_v14_cd_only_kaggle_submit | Seungjun Lee | 2026-08-31T08:23:03.777000 | 1 | - |
| 184 | caoyupeng/ai-agent-security-trajectory-search-plus-2 | AI Agent Security - Trajectory Search Plus-2 | SpeedSci | 2026-06-13T06:19:16.750000 | 8 | - |
| 185 | samwiz/aas-v8deputy-gpu | AAS v8deputy GPU | Sam-wiz | 2026-08-31T18:00:03.953000 | 1 | - |
| 186 | hiranorm/publiclb-21-465-privatelb-21-465-aas-email-hedge | [publicLB:21.465,privateLB:21.465]aas-email-hedge | Hira Norm | 2026-08-26T15:30:22.893000 | 0 | - |
| 187 | imbikramsaha/ai-agent-security-baseline-score-21-285 | AI Agent Security - Baseline / Score - 21.285 | Bikram Saha | 2026-06-15T18:09:29.880000 | 5 | - |
| 188 | ruhul20/red-team-ai-agent-security | Red-team AI Agent Security | Ruhul Amin | 2026-08-29T10:25:53.707000 | 5 | - |
| 189 | josephadamski91/conditional-draft-generation-control-v4 | Conditional Draft Generation Control V4 | Joseph Adamski | 2026-08-30T00:10:43.450000 | 2 | - |
| 190 | zhtngr/suffix-allow-guardrail-033-n700 | Suffix Allow Guardrail 033 n700 | kawasaki | 2026-06-30T00:11:39.417000 | 0 | - |
| 191 | anvithpothula/aisec-jedcd6 | aisec-jedcd6 | Anvith Pothula | 2026-08-31T01:57:22.693000 | 1 | - |
| 192 | ducnamphan/jed-v6-0-proven-format | JED v6.0 — Proven Format | Duc Nam Phan | 2026-07-07T07:02:41.840000 | 1 | - |
| 193 | sebastianmateus/champion-v8-1-cdframe-0811000200 | Champion V8 1 Cdframe 0811000200 | Sebastian Mateus | 2026-08-11T00:02:04.833000 | 0 | - |
| 194 | ducnamphan/jed-v13-0-fixed-n-250 | JED v13.0 Fixed N=250 | Duc Nam Phan | 2026-07-09T06:54:38.997000 | 1 | - |
| 195 | aleixlopez/v49-confused-deputy-hedge | v49_confused_deputy_hedge | Aleix López | 2026-08-30T18:34:13.233000 | 0 | - |
| 196 | wguesdon/ai-agent-security-attack-v19 | AI Agent Security - Attack v19 | Will | 2026-08-31T11:40:39.420000 | 0 | - |
| 197 | outliar/agi-deputy-nb2-v14-gpt2000-gem2000-sub | agi-deputy-nb2-v14-gpt2000-gem2000_sub | Mohammad Shadab Alam | 2026-08-27T13:27:25.930000 | 0 | - |
| 198 | akshitasrivastava1/omega-attack-v9-1-gemma-phrase-hunt | omega attack v9 1 gemma phrase hunt | Akshita Srivastava | 2026-06-26T15:14:46.660000 | 6 | - |
| 199 | maqsoudtawaliou/aas-attack-deputy-uncond-frac97 | AAS Attack Deputy Uncond Frac97 | Maqsoud Tawaliou | 2026-08-16T05:49:53.737000 | 0 | - |
| 200 | ducnamphan/jed-v19-0-pure-exfil | JED v19.0 Pure EXFIL | Duc Nam Phan | 2026-07-11T07:34:23.750000 | 2 | - |
| 201 | ducnamphan/jed-v7-0-shell-obfuscation | JED v7.0 Shell Obfuscation | Duc Nam Phan | 2026-07-08T01:57:14.070000 | 2 | - |
| 202 | qyq1693/ai-agent-security-marker-v13 | ai-agent-security-marker-v13 | QYQ1693 | 2026-07-08T11:16:33.520000 | 2 | - |
| 203 | ducnamphan/jed-attack-v0-60-adaptive | JED Attack v0.60 — Adaptive | Duc Nam Phan | 2026-07-05T06:18:25.157000 | 2 | - |
| 204 | ducnamphan/jed-v18-0-cd-exfil | JED v18.0 CD+EXFIL | Duc Nam Phan | 2026-07-10T19:03:42.823000 | 2 | - |
| 205 | ducnamphan/jed-attack-v0-50-fixed | JED Attack v0.50 — Fixed | Duc Nam Phan | 2026-07-04T19:15:51.240000 | 3 | - |
| 206 | funcnano/ai-agent-security-auto-attack | AI Agent Security Auto Attack | func-nano | 2026-06-27T04:40:47.463000 | 2 | - |
| 207 | ducnamphan/jed-v17-0-precision-uta | JED v17.0 Precision UTA | Duc Nam Phan | 2026-07-10T19:01:46.297000 | 1 | - |
| 208 | ducnamphan/jed-attack-v0-70-model-aware | JED Attack v0.70 — Model-Aware | Duc Nam Phan | 2026-07-05T06:23:24.630000 | 2 | - |
| 209 | tkhanna96/h006-pre-taint-exfil-probe-nb | H006 Pre-Taint EXFIL Probe NB | Tkhanna96 | 2026-06-13T18:41:51.517000 | 3 | - |
| 210 | chavarost/jed-attack-v8 | JED Attack v8 | Chavarost Choampangpacharapan | 2026-06-15T05:05:56.483000 | 3 | - |
| 211 | ducnamphan/jed-attack-v0-55-optimized | JED Attack v0.55 — Optimized | Duc Nam Phan | 2026-07-05T06:13:43.877000 | 2 | - |
| 212 | akshitasrivastava1/omega-attack-v7-multi-hop-exfil-ai-agent-security | omega attack v7 multi-hop exfil ai agent security | Akshita Srivastava | 2026-06-20T07:47:27.623000 | 1 | - |
| 213 | ducnamphan/jed-v21-0-best-combo | JED v21.0 Best Combo | Duc Nam Phan | 2026-07-11T09:33:12.783000 | 3 | - |
| 214 | nawfeelrahman1124444/multi-step-tool-attacks-16-980 | Multi-Step Tool Attacks - 16.980 🏅🔥 | (ノ◡ <) | 2026-06-11T20:13:04.487000 | 18 | - |
| 215 | adostie3/jed-attack-cd-v1 | JED Attack CD v1 | Adam Dostie | 2026-09-01T13:41:14.207000 | 0 | - |
| 216 | gdataranger/jed-attack-starter-v3-1-2-fixed | JED Attack — Starter (v3.1.2 Fixed) | Mark Susol | 2026-06-26T14:18:35.887000 | 53 | - |
| 217 | merkiraz/notebook5ed42e3e8f | notebook5ed42e3e8f | ömer kiraz | 2026-08-29T15:16:15.633000 | 0 | - |
| 218 | verise6211/aas-persona-1post | AAS Persona 1post | verise6211 | 2026-07-05T19:43:42.617000 | 2 | - |
| 219 | emanuellcs/aias-deterministic-bounded-search | AIAS - Deterministic Bounded Search | Emanuel Lázaro | 2026-06-13T11:13:54.807000 | 6 | - |
| 220 | saharmgh/notebook3 | notebook3 | Sahar Mgh | 2026-07-13T15:02:11.393000 | 1 | - |
| 221 | pengwang91/jed-fill-k2-exact2 | jed-fill-k2-exact2 | Peng Wang | 2026-07-06T22:39:46.987000 | 2 | - |
| 222 | devchandra/ai-agent-security-v71-peng-k2-exact2 | AI Agent Security v71 Peng K2 exact2 | Dr Chandrasen Pandey | 2026-07-07T03:01:55.117000 | 1 | - |
| 223 | karnakbaevarthur/verify-and-keep-deterministic-red-team-attack | Verify-and-Keep: Deterministic Red-Team Attack | Karnakbayev Artur | 2026-06-12T07:17:05.840000 | 56 | - |
| 224 | yaroslavkholmirzayev/ai-agent-security-first-submission | AI Agent Security - First Submission | Yaroslav kholmirzayev | 2026-06-12T18:32:46.337000 | 29 | - |
| 225 | gouthamkonduru/twoforfamily | TwoforFamily | Goutham Konduru | 2026-08-27T09:11:08.477000 | 3 | - |
| 226 | tkhanna96/h026-calibrate-then-generate-nb | H026 Calibrate Then Generate NB | Tkhanna96 | 2026-06-24T19:16:10.727000 | 6 | - |
| 227 | ducnamphan/jed-v5-5-budget-safe-n-275 | JED v5.5 — Budget Safe N~275 | Duc Nam Phan | 2026-07-06T08:09:59.497000 | 2 | - |
| 228 | pengwang91/jed-fill-k3-fasttriple | jed-fill-k3-fasttriple | Peng Wang | 2026-07-07T03:25:58.420000 | 1 | - |
| 229 | debugendless/jed-attack-mutation-baseline | 🔓 JED Attack: Mutation Baseline | Yamaguchi | 2026-06-12T14:55:02.160000 | 10 | - |
| 230 | wisdomdogah/jed-attack-submission | JED Attack Submission | Wisdom Dogah | 2026-06-20T07:12:55.837000 | 4 | - |
| 231 | pengwang91/jed-fill-k2-fastpair | jed-fill-k2-fastpair | Peng Wang | 2026-07-07T03:25:23.517000 | 1 | - |
| 232 | verise6211/aas-persona60 | AAS Persona60 | verise6211 | 2026-07-05T19:43:17.803000 | 2 | - |
| 233 | hasnain201/baseline-solution-4-900 | Baseline Solution - 4.900  | Hasnain khan | 2026-06-12T18:06:12.087000 | 3 | - |
| 234 | tkhanna96/h006-s4-maxn-cd | H006 S4 MaxN CD | Tkhanna96 | 2026-06-20T17:34:39.740000 | 1 | - |
| 235 | nawfeelrahman1124444/baseline-solution-4-900 | Baseline Solution - 4.900 🔥🫡 | (ノ◡ <) | 2026-06-11T19:12:50.857000 | 61 | - |
| 236 | tkhanna96/h006-s2-headline-len60-selfcap | H006 S2 Headline Len60 Selfcap | Tkhanna96 | 2026-06-20T17:34:14.917000 | 1 | - |
| 237 | tkhanna96/h006-s3-pilkwang-replica | H006 S3 Pilkwang Replica | Tkhanna96 | 2026-06-20T17:34:37.933000 | 1 | - |
| 238 | youssefyacoup/ai-agent | AI AGENT | Youssef Yacoup | 2026-08-22T16:36:34.533000 | 0 | - |
| 239 | tkhanna96/h006-s5-encoding-hedge | H006 S5 Encoding Hedge | Tkhanna96 | 2026-06-20T17:34:41.347000 | 1 | - |
| 240 | ferencjuhsz/ghostpost-verify-and-keep-agent-red-team | GHOSTPOST — verify-and-keep agent red-team | Catcatcher | 2026-06-12T12:35:37.317000 | 26 | - |
| 241 | monkeydz/aisec-attack-v2 | aisec-attack-v2 | Dengzhe Hou | 2026-06-16T08:44:53.030000 | 5 | - |
| 242 | chetansahney/openaisoln1 | OpenAISoln1 | Chetan Sahney | 2026-06-13T19:33:57.193000 | 1 | - |
| 243 | verise6211/aas-persona30 | AAS Persona30 | verise6211 | 2026-07-05T14:52:54.300000 | 3 | - |
| 244 | mdabdulalhasib/kronos-fixed-without-time-limit | KRONOS /  Fixed without time limit | Md Abdul Al Hasib | 2026-06-13T13:45:06.097000 | 2 | - |
| 245 | mccocoful/local-cpu-submission-for-hengck23 | local cpu + submission for hengck23 | cm391 | 2026-08-26T11:49:06.403000 | 53 | - |
| 246 | paul720810/hermes-openclaw-attack-e005-20260625-060859 | Hermes OpenClaw Attack E005-20260625-060859 | Paul720810 | 2026-06-25T06:11:08.493000 | 2 | - |
| 247 | paul720810/hermes-openclaw-attack-e005-20260704-061228 | Hermes OpenClaw Attack E005-20260704-061228 | Paul720810 | 2026-07-04T06:12:32.037000 | 1 | - |
| 248 | paul720810/hermes-openclaw-attack-v5-4-4-20260616-034038 | Hermes OpenClaw Attack v5.4.4-20260616-034038 | Paul720810 | 2026-06-16T03:40:41.340000 | 2 | - |
| 249 | paul720810/hermes-openclaw-attack-e005-20260620-154759 | Hermes OpenClaw Attack E005-20260620-154759 | Paul720810 | 2026-06-20T15:48:04.387000 | 2 | - |
| 250 | paul720810/hermes-openclaw-attack-v6-0-rollback | Hermes OpenClaw Attack v6.0 Rollback | Paul720810 | 2026-06-17T04:36:41.307000 | 1 | - |
| 251 | paul720810/hermes-openclaw-attack-v7-5-20260617-051723 | Hermes OpenClaw Attack v7.5-20260617-051723 | Paul720810 | 2026-06-17T05:17:26.457000 | 2 | - |
| 252 | ducnamphan/jed-v10-0-balanced-best | JED v10.0 Balanced Best | Duc Nam Phan | 2026-07-08T15:43:39.700000 | 2 | - |
| 253 | ducnamphan/jed-v11-0-cell-diversity | JED v11.0 Cell Diversity | Duc Nam Phan | 2026-07-08T15:47:22.957000 | 2 | - |
| 254 | paul720810/hermes-openclaw-attack-e005-20260622-004139 | Hermes OpenClaw Attack E005-20260622-004139 | Paul720810 | 2026-06-22T00:41:42.943000 | 3 | - |
| 255 | paul720810/hermes-openclaw-attack-e005-20260622-014255 | Hermes OpenClaw Attack E005-20260622-014255 | Paul720810 | 2026-06-22T01:42:59.907000 | 2 | - |
| 256 | paul720810/hermes-openclaw-attack-e005-20260622-025415 | Hermes OpenClaw Attack E005-20260622-025415 | Paul720810 | 2026-06-22T02:54:19.540000 | 2 | - |
| 257 | paul720810/hermes-openclaw-attack-e005-20260622-035525 | Hermes OpenClaw Attack E005-20260622-035525 | Paul720810 | 2026-06-22T03:55:28.923000 | 2 | - |
| 258 | nawfeelrahman1124444/getting-started-notebook-0-9 | Getting Started Notebook - 0.9 | (ノ◡ <) | 2026-06-21T16:53:58.270000 | 33 | - |
| 259 | anvithpothula/aisec-sevstack | AISec SevStack | Anvith Pothula | 2026-07-20T19:01:01.437000 | 6 | - |
| 260 | ayushkhaire/clean-getting-started-notebook | Clean Getting Started Notebook | Ayush Khaire | 2026-06-12T13:38:51.800000 | 12 | - |
| 261 | loveautomn/notebookbef7d3ffbd | notebookbef7d3ffbd | love automn | 2026-07-12T09:05:28.570000 | 0 | - |
| 262 | ayushanand01/jed-mab-attack | JED MAB Attack | Ayush Anand | 2026-09-01T17:11:43.153000 | 0 | - |
| 263 | dedquoc/data-clean-exploit | Data Clean & Exploit | De DQ | 2026-07-05T07:18:40.300000 | 1 | - |
| 264 | vineetvsalimath/ai-agent-secure | Ai-agent secure | Vineet v Salimath | 2026-06-18T15:15:54.167000 | 0 | - |
| 265 | martynaplomecka/getting-started-notebook | Getting Started Notebook | MartynaPlomecka | 2026-07-13T13:04:02.040000 | 1763 | - |
| 266 | harmeetkaur24/getting-started-notebook | Getting Started Notebook | Harmeet Kaur | 2026-07-09T07:56:43.350000 | 0 | - |
| 267 | sravanikamjula/ai-agent-security-multi-step-tool-attack-baseline | AI Agent Security–Multi-Step Tool Attack Baseline | sravani kamjula | 2026-07-21T21:24:01.860000 | 2 | - |
| 268 | adonisleu/jed-attack-control | JED Attack Control | ElijahMingLiu | 2026-06-29T09:56:12.337000 | 3 | - |
| 269 | avikdas567/state-space-search-for-multi-step-agent-attacks | State-Space Search for Multi-Step Agent Attacks | Avik Das | 2026-08-31T03:26:12.320000 | 23 | - |
| 270 | irongm/omega-attack-v8-7-multi-phrase-n250 | omega attack v8 7 multi phrase n250 | IRON GM | 2026-06-25T09:08:50.770000 | 0 | - |
| 271 | ducnamphan/jed-v8-0-max-combo | JED v8.0 Max Combo | Duc Nam Phan | 2026-07-08T01:58:36.593000 | 2 | - |
| 272 | carlysipahutar/jed-attack-multi-step-v1 | jed-attack-multi-step-v1 | carly sipahutar | 2026-06-14T18:08:01.843000 | 4 | - |
| 273 | vineetvsalimath/ai-agent-secure-3 | =Ai-agent secure 3 | Vineet v Salimath | 2026-06-20T03:28:26.817000 | 7 | - |
| 274 | paul720810/hermes-openclaw-attack-e005-20260624-020503 | Hermes OpenClaw Attack E005-20260624-020503 | Paul720810 | 2026-06-24T02:05:07.470000 | 1 | - |
| 275 | musnet/go-explore-red-team-multi-step-tool-attacks | 🥇 Go-Explore Red-Team — Multi-Step Tool Attacks | MohamedMustafa | 2026-06-13T04:52:01.927000 | 5 | - |
| 276 | carlysipahutar/jed-attack-v2 | jed-attack-v2 | carly sipahutar | 2026-06-14T18:30:01.183000 | 4 | - |
| 277 | paul720810/hermes-openclaw-attack-e005-20260624-123750 | Hermes OpenClaw Attack E005-20260624-123750 | Paul720810 | 2026-06-24T13:16:14.843000 | 0 | - |
| 278 | udaken10/hi-hihi-ho | hi_hihi_ho | really? | 2026-06-26T15:13:40.787000 | 5 | - |
| 279 | tkhanna96/h006-v2-geometry-nb | H006-v2 geometry NB | Tkhanna96 | 2026-06-13T21:01:48.323000 | 1 | - |
| 280 | tkhanna96/h006-v2-scale-2k-nb | H006-v2 SCALE 2k NB | Tkhanna96 | 2026-06-13T21:19:48.657000 | 1 | - |
| 281 | tkhanna96/h006-v3-optimize-nb | H006-v3 OPTIMIZE NB | Tkhanna96 | 2026-06-13T21:21:40.997000 | 1 | - |
| 282 | tkhanna96/h006-v2-h007-stack-nb | H006-v2 + H007 STACK NB | Tkhanna96 | 2026-06-13T21:20:04.130000 | 1 | - |
| 283 | tkhanna96/h006-simple-scale-900-nb | H006 Simple Scale 900 NB | Tkhanna96 | 2026-06-14T08:37:51.650000 | 1 | - |
| 284 | tkhanna96/h006-4post-400-nb | H006 4post 400 NB | Tkhanna96 | 2026-06-14T09:33:06.313000 | 1 | - |
| 285 | tkhanna96/h006-2turn-4post-400-nb | H006 2turn 4post 400 NB | Tkhanna96 | 2026-06-14T11:23:45.277000 | 1 | - |
| 286 | paul720810/hermes-openclaw-attack-v5-5 | Hermes OpenClaw Attack v5.5 | Paul720810 | 2026-06-14T16:50:38.977000 | 2 | - |
| 287 | paul720810/hermes-openclaw-attack-v5-4-4-20260615-045937 | Hermes OpenClaw Attack v5.4.4-20260615-045937 | Paul720810 | 2026-06-15T04:59:40.123000 | 2 | - |
| 288 | paul720810/hermes-openclaw-attack-v5-4-4-20260615-094527 | Hermes OpenClaw Attack v5.4.4-20260615-094527 | Paul720810 | 2026-06-15T09:45:31.247000 | 2 | - |
| 289 | paul720810/hermes-openclaw-attack-v5-4-4-20260615-111041 | Hermes OpenClaw Attack v5.4.4-20260615-111041 | Paul720810 | 2026-06-15T11:10:44.370000 | 2 | - |
| 290 | paul720810/hermes-openclaw-attack-v7-0 | Hermes OpenClaw Attack v7.0 | Paul720810 | 2026-06-17T13:51:31.037000 | 3 | - |
| 291 | paul720810/hermes-openclaw-attack-v7-5-20260618-012506 | Hermes OpenClaw Attack v7.5-20260618-012506 | Paul720810 | 2026-06-18T01:25:11.763000 | 1 | - |
| 292 | paul720810/hermes-openclaw-attack-v7-5-20260618-013134 | Hermes OpenClaw Attack v7.5-20260618-013134 | Paul720810 | 2026-06-18T01:31:38.543000 | 1 | - |
| 293 | paul720810/hermes-openclaw-attack-v7-5-20260618-075324 | Hermes OpenClaw Attack v7.5-20260618-075324 | Paul720810 | 2026-06-18T07:53:29.560000 | 0 | - |
| 294 | paul720810/hermes-openclaw-attack-v7-5-20260618-132354 | Hermes OpenClaw Attack v7.5-20260618-132354 | Paul720810 | 2026-06-18T13:23:58.547000 | 3 | - |
| 295 | paul720810/hermes-openclaw-attack-v8-0 | Hermes OpenClaw Attack v8.0 | Paul720810 | 2026-06-18T14:07:13.910000 | 0 | - |
| 296 | berkahkarya/ai-agent-security-attack-v36 | ai-agent-security-attack-v36 | Berkahkarya Dev | 2026-06-20T13:45:58.887000 | 1 | - |
| 297 | paul720810/hermes-openclaw-attack-v7-5-20260619-173824 | Hermes OpenClaw Attack v7.5-20260619-173824 | Paul720810 | 2026-06-19T17:38:27.660000 | 0 | - |
| 298 | paul720810/hermes-openclaw-attack-e002-20260619-174939 | Hermes OpenClaw Attack E002-20260619-174939 | Paul720810 | 2026-06-19T17:49:43.743000 | 1 | - |
| 299 | paul720810/hermes-openclaw-attack-e003-20260619-175322 | Hermes OpenClaw Attack E003-20260619-175322 | Paul720810 | 2026-06-19T17:53:26.620000 | 0 | - |
| 300 | paul720810/hermes-openclaw-attack-e004-20260620-021421 | Hermes OpenClaw Attack E004-20260620-021421 | Paul720810 | 2026-06-20T02:14:25.227000 | 0 | - |
| 301 | paul720810/hermes-openclaw-attack-e005-20260620-025043 | Hermes OpenClaw Attack E005-20260620-025043 | Paul720810 | 2026-06-20T02:50:46.707000 | 0 | - |
| 302 | max4kr/notebook22b0ab8b82 | notebook22b0ab8b82 | Максим Кравченко | 2026-06-22T09:20:40.730000 | 0 | - |
| 303 | geokocha/eda-agent-security-sdk-deep-dive | EDA Agent Security SDK Deep Dive | Yuanchen Huang | 2026-06-21T16:41:10.937000 | 7 | - |
| 304 | sgzk001/ai-agent-security-optimized-attack | ai-agent-security-optimized-attack | SGzK001 | 2026-06-26T06:02:19.530000 | 1 | - |
| 305 | seyominaoto/jed-attack-multi-strategy | jed attack multi strategy | Seyominaoto | 2026-06-23T07:08:28.707000 | 0 | - |
| 306 | paul720810/hermes-openclaw-attack-e005-20260622-121024 | Hermes OpenClaw Attack E005-20260622-121024 | Paul720810 | 2026-06-22T12:11:24.337000 | 1 | - |
| 307 | paul720810/hermes-openclaw-attack-e005-20260623-000650 | Hermes OpenClaw Attack E005-20260623-000650 | Paul720810 | 2026-06-23T00:06:56.197000 | 1 | - |
| 308 | paul720810/hermes-openclaw-attack-e005-20260623-000740 | Hermes OpenClaw Attack E005-20260623-000740 | Paul720810 | 2026-06-23T00:07:44.280000 | 1 | - |
| 309 | paul720810/hermes-openclaw-attack-e005-20260623-020427 | Hermes OpenClaw Attack E005-20260623-020427 | Paul720810 | 2026-06-23T02:04:30.940000 | 1 | - |
| 310 | paul720810/hermes-openclaw-attack-e005-20260623-040534 | Hermes OpenClaw Attack E005-20260623-040534 | Paul720810 | 2026-06-23T04:05:37.637000 | 1 | - |
| 311 | paul720810/hermes-openclaw-attack-e005-20260624-020556 | Hermes OpenClaw Attack E005-20260624-020556 | Paul720810 | 2026-06-24T02:06:00.377000 | 1 | - |
| 312 | alt0er/ai-agent-security-submission | AI Agent Security Submission | Pratik Acharya | 2026-06-25T00:26:10.873000 | 1 | - |
| 313 | paul720810/hermes-openclaw-attack-e005-20260630-141208 | Hermes OpenClaw Attack E005-20260630-141208 | Paul720810 | 2026-06-30T14:12:12.423000 | 1 | - |
| 314 | farmountain/harness-test-ai-sec-nb-sub01 | Harness Test Ai Sec Nb Sub01 | Liew Keong Han | 2026-07-01T01:35:46.727000 | 1 | - |
| 315 | paul720810/hermes-openclaw-attack-e005-20260702-041330 | Hermes OpenClaw Attack E005-20260702-041330 | Paul720810 | 2026-07-02T04:13:35.247000 | 2 | - |
| 316 | verise6211/aas-caoyupeng-repro | AAS Caoyupeng Repro | verise6211 | 2026-07-04T17:41:30.730000 | 1 | - |
| 317 | verise6211/aas-sentinel | AAS Sentinel | verise6211 | 2026-07-05T03:17:26.520000 | 0 | - |
| 318 | qyq1693/ai-agent-security-speed-v12 | ai-agent-security-speed-v12 | QYQ1693 | 2026-07-07T12:59:20.800000 | 0 | - |
| 319 | erkkj98/notebook1e97ff965b | notebook1e97ff965b | Alexander_Perez | 2026-07-15T11:27:18.067000 | 1 | - |
| 320 | paul720810/hermes-attack-v56-n950-ultrashort-20260718-003002 | Hermes Attack v56-n950-ultrashort-20260718-003002 | Paul720810 | 2026-07-18T00:30:07.380000 | 0 | - |
| 321 | narajan/best-public-score | Best Public score | Rajan Nagarajan | 2026-06-12T16:55:47.027000 | 5 | - |
| 322 | clawdyhuang/ai-agent-security-sov-v9 | ai-agent-security-sov-v9 | Clawdy Huang (Andy's AI) | 2026-06-12T07:55:50.257000 | 3 | - |
| 323 | clawdyhuang/ai-agent-security-sov-v10 | ai-agent-security-sov-v10 | Clawdy Huang (Andy's AI) | 2026-07-05T14:17:06.067000 | 0 | - |
| 324 | aminmahmoudalifayed/shadow-strike-advanced-multi-step-ai-agent-attack | Shadow Strike: Advanced Multi-Step AI Agent Attack | Dr/ameen Fayed | 2026-06-12T20:42:02.143000 | 5 | - |
| 325 | arnavkewalram/ai-agent-security-attack | AI Agent Security Attack | Arnav Kewalram | 2026-06-15T16:39:18.173000 | 3 | - |
| 326 | aadias777/ais-attack-notebook | AIS Attack Notebook | Aadi77 | 2026-06-13T02:00:41.900000 | 1 | - |
| 327 | yujiyyy/jed-benchmark-demystified | JED Benchmark Demystified | yuji y | 2026-06-13T02:32:48.663000 | 2 | - |
| 328 | mdabdulalhasib/apex-attack-engine-multi-step | APEX Attack Engine: Multi-Step | Md Abdul Al Hasib | 2026-06-13T04:37:22.090000 | 8 | - |
| 329 | rauffauzanrambe/agent-v20-security-for-the-openai | Agent V20 Security for the OpenAI | Ra'uf Fauzan Rambe | 2026-06-13T05:30:41.627000 | 8 | - |
| 330 | sohaibdevv/ai-agent-security | AI Agent Security | Sohaib Malik | 2026-06-13T06:01:35.907000 | 8 | - |
| 331 | chaitanyajamble/ai-agent-security-multi-step-tool-attack | AI Agent Security-Multi step tool attack | Chaitanya Jamble | 2026-06-13T09:33:12.673000 | 5 | - |
| 332 | roy210005/ai-agent-sec-v1 | AI agent sec- V1 | Sojib Chandra Roy | 2026-06-13T07:37:13.510000 | 2 | - |
| 333 | avikdas567/diversity-optimized-multi-step-agent-red-teaming | Diversity Optimized Multi-Step Agent Red Teaming | Avik Das | 2026-06-19T03:13:52.060000 | 20 | - |
| 334 | llkh0a/aas-local-validation | AAS / Local validation | Kh0a | 2026-08-24T01:51:34.697000 | 459 | - |
| 335 | chaitanyajamble/ai-agent-security-multi-step-tool-attacks | AI Agent Security _ Multi-Step-Tool-Attacks | Chaitanya Jamble | 2026-06-14T02:47:54.610000 | 1 | - |
| 336 | quynthnh/sdk-walkthrough-attack-strategy | SDK Walkthrough + Attack Strategy | Quyền Thịnh | 2026-06-13T14:50:38.350000 | 5 | - |
| 337 | beicicc/security-eval-public | Security Eval Public | Kun Zhang | 2026-06-13T15:08:00.590000 | 4 | - |
| 338 | paul720810/hermes-openclaw-attack-v4 | Hermes OpenClaw Attack v4 | Paul720810 | 2026-06-14T01:14:04.030000 | 3 | - |
| 339 | chaitanyajamble/ai-agent-security-multi-step-tool-attacks-3 | AI Agent Security - Multi step tool attacks-3 | Chaitanya Jamble | 2026-06-14T10:42:52.813000 | 2 | - |
| 340 | tuannm3812/ai-agent-security-01-eda | AI Agent Security 01 EDA | tuannm3812 | 2026-06-14T14:49:43.597000 | 5 | - |
| 341 | tkhanna96/h006-simple-scale-2000-nb | H006 Simple Scale 2000 NB | Tkhanna96 | 2026-06-14T08:58:17.353000 | 1 | - |
| 342 | tkhanna96/h006-4post-email-stack-nb | H006 4post Email Stack NB | Tkhanna96 | 2026-06-14T10:15:20.650000 | 1 | - |
| 343 | imbikramsaha/ai-agent-security-explained-eda-starter | AI Agent Security Explained EDA Starter  | Bikram Saha | 2026-06-14T13:11:19.297000 | 9 | - |
| 344 | tonylagumen/final-ai-agent-sec-ver19 | final_ai_agent_sec_ver19 | Tony Lagumen | 2026-06-15T13:45:13.517000 | 1 | - |
| 345 | pavloivanin/ai-agent-security-multi-step-attack-engine-eda | AI Agent Security: Multi-Step Attack Engine EDA | Pavlo Ivanin | 2026-06-14T14:33:24.743000 | 2 | - |
| 346 | tkhanna96/h006-persona-4post-900-nb | H006 Persona 4post 900 NB | Tkhanna96 | 2026-06-14T14:48:08.803000 | 2 | - |
| 347 | tkhanna96/h026-adaptive-verify-keep-nb | H026 Adaptive Verify-Keep NB | Tkhanna96 | 2026-06-14T15:31:08.450000 | 2 | - |
| 348 | nicolepatterson8910/attack-py | attack.py | Nicole Patterson | 2026-06-25T18:45:44.070000 | 0 | - |
| 349 | tkhanna96/h026-4post-direct-nb | H026 4post Direct NB | Tkhanna96 | 2026-06-14T16:27:19.393000 | 3 | - |
| 350 | tkhanna96/h006-simple-scale-600-nb | H006 Simple Scale 600 NB | Tkhanna96 | 2026-06-24T16:58:51.390000 | 4 | - |
| 351 | shamarjordan/albalgorithim | AlBalgorithim | Shamar Jordan | 2026-06-14T20:29:58.613000 | 3 | - |
| 352 | hichambedrani/ai-agent-security-eval-v13 | AI Agent Security Eval v13 | hicham bedrani | 2026-06-14T18:41:15.580000 | 2 | - |
| 353 | hichambedrani/ai-agent-security-v17 | AI Agent Security v17 | hicham bedrani | 2026-06-14T18:56:40.300000 | 4 | - |
| 354 | hichambedrani/ai-agent-security-v18 | AI Agent Security v18 | hicham bedrani | 2026-06-14T18:59:51.660000 | 3 | - |
| 355 | shamarjordan/notebook354da3e7b2 | notebook354da3e7b2 | Shamar Jordan | 2026-06-14T19:21:20.443000 | 2 | - |
| 356 | hichambedrani/ai-agent-security-min-v1 | AI Agent Security Min v1 | hicham bedrani | 2026-06-14T19:19:37.023000 | 4 | - |
| 357 | prtkpiyush/solutions-first-attempt | Solutions_first_attempt | PrtkPiyush | 2026-06-14T19:37:04.890000 | 6 | - |
| 358 | tkhanna96/h006-static-400-slot-10-nb | H006 Static 400 Slot 10 NB | Tkhanna96 | 2026-06-24T19:15:10.450000 | 2 | - |
| 359 | shamarjordan/notebook794e4c7509 | notebook794e4c7509 | Shamar Jordan | 2026-06-14T21:09:49.583000 | 1 | - |
| 360 | tarikumehdi/perfect-1000-score-attack | Perfect 1000 Score Attack | Tariku Mehdi | 2026-06-15T17:06:49.943000 | 2 | - |
| 361 | paul720810/hermes-openclaw-attack-v5-4-4-20260615-045242 | Hermes OpenClaw Attack v5.4.4-20260615-045242 | Paul720810 | 2026-06-15T04:52:45.823000 | 2 | - |
| 362 | paul720810/hermes-openclaw-attack-v5-4-4-20260615-050418 | Hermes OpenClaw Attack v5.4.4-20260615-050418 | Paul720810 | 2026-06-15T05:04:22.227000 | 2 | - |
| 363 | paul720810/hermes-openclaw-attack-v5-4-4-20260615-090607 | Hermes OpenClaw Attack v5.4.4-20260615-090607 | Paul720810 | 2026-06-15T09:06:10.667000 | 2 | - |
| 364 | paul720810/hermes-openclaw-attack-v5-4-4-20260615-093314 | Hermes OpenClaw Attack v5.4.4-20260615-093314 | Paul720810 | 2026-06-15T09:33:18.240000 | 2 | - |
| 365 | paul720810/hermes-openclaw-attack-v5-4-4-20260615-093845 | Hermes OpenClaw Attack v5.4.4-20260615-093845 | Paul720810 | 2026-06-15T09:38:47.793000 | 2 | - |
| 366 | mdabdulalhasib/hmmm-let-s-give-another-solution | Hmmm.... let's give another solution | Md Abdul Al Hasib | 2026-06-15T09:44:30.957000 | 6 | - |
| 367 | qinggedada/agent-security-v1 | Agent Security V1 | qinggedada | 2026-06-15T11:52:02.293000 | 2 | - |
| 368 | hasnain201/aas-local-validation | AAS  Local validation | Hasnain khan | 2026-06-15T14:01:19.490000 | 1 | - |
| 369 | dhanvinsureshareddy/multiguard-validation-1 | Multiguard Validation 1 | Dhanvin S | 2026-06-16T13:34:38.337000 | 6 | - |
| 370 | tkhanna96/k4-d1r1-routed-v4-nb | K4 D1R1 Routed v4 NB | Tkhanna96 | 2026-06-15T20:52:18.230000 | 2 | - |
| 371 | tkhanna96/k4-d1r1-routed-v2-nb | K4 D1R1 Routed v2 NB | Tkhanna96 | 2026-06-15T20:53:09.927000 | 2 | - |
| 372 | tkhanna96/k4-d1r1-routed-nb | K4 D1R1 Routed NB | Tkhanna96 | 2026-06-15T20:53:15.840000 | 2 | - |
| 373 | tkhanna96/k4-d1r1-routed-v3-nb | K4 D1R1 Routed v3 NB | Tkhanna96 | 2026-06-15T20:53:19.140000 | 3 | - |
| 374 | tkhanna96/h006-multimsg-200x3-nb | H006 multimsg 200x3 NB | Tkhanna96 | 2026-06-24T19:15:46.093000 | 2 | - |
| 375 | varunraosfanlkan/extraordinaries-agent-security |  extraordinaries-agent-security | Varun Rao | 2026-06-16T07:01:08.137000 | 6 | - |
| 376 | chaitanyajamble/ai-agent-security-1 | AI Agent Security-1 | Chaitanya Jamble | 2026-06-16T09:12:25.067000 | 4 | - |
| 377 | monkeydz/aisec-attack-v1 | aisec-attack-v1 | Dengzhe Hou | 2026-06-16T08:38:43.983000 | 4 | - |
| 378 | chaitanyajamble/ai-agent-security-msta-2 | AI Agent Security - MSTA/2 | Chaitanya Jamble | 2026-06-16T10:16:16.483000 | 3 | - |
| 379 | qinggedada/v6-read-multipost-static-attacks | V6 Read-Multipost Static Attacks | qinggedada | 2026-06-25T06:19:30.220000 | 4 | - |
| 380 | tkhanna96/k1-short-n1200 | k1-short-n1200 | Tkhanna96 | 2026-06-16T16:17:29.247000 | 1 | - |
| 381 | tkhanna96/mixed-k1-k4-n800 | mixed-k1-k4-n800 | Tkhanna96 | 2026-06-16T16:33:01.977000 | 1 | - |
| 382 | tkhanna96/two-msg-k1-n900 | two-msg-k1-n900 | Tkhanna96 | 2026-06-16T16:33:03.467000 | 1 | - |
| 383 | tkhanna96/k1-short-n1500 | k1-short-n1500 | Tkhanna96 | 2026-06-16T16:33:05.583000 | 1 | - |
| 384 | paul720810/hermes-openclaw-attack-v5-4-4-20260616-164412 | Hermes OpenClaw Attack v5.4.4-20260616-164412 | Paul720810 | 2026-06-16T16:44:15.913000 | 1 | - |
| 385 | paul720810/hermes-openclaw-attack-v5-4-4-20260616-191008 | Hermes OpenClaw Attack v5.4.4-20260616-191008 | Paul720810 | 2026-06-16T19:10:11.047000 | 1 | - |
| 386 | paul720810/hermes-openclaw-attack-v5-4-4-20260616-225601 | Hermes OpenClaw Attack v5.4.4-20260616-225601 | Paul720810 | 2026-06-16T22:56:04.277000 | 1 | - |
| 387 | paul720810/hermes-openclaw-attack-v5-4-4-20260617-003205 | Hermes OpenClaw Attack v5.4.4-20260617-003205 | Paul720810 | 2026-06-17T00:32:09.357000 | 1 | - |
| 388 | paul720810/hermes-openclaw-attack-v5-4-4-20260617-004304 | Hermes OpenClaw Attack v5.4.4-20260617-004304 | Paul720810 | 2026-06-17T00:43:08.373000 | 1 | - |
| 389 | paul720810/hermes-openclaw-attack-v5-4-4-20260617-004904 | Hermes OpenClaw Attack v5.4.4-20260617-004904 | Paul720810 | 2026-06-17T00:49:08.163000 | 1 | - |
| 390 | paul720810/hermes-openclaw-attack-v5-4-4-20260617-005744 | Hermes OpenClaw Attack v5.4.4-20260617-005744 | Paul720810 | 2026-06-17T00:57:47.007000 | 1 | - |
| 391 | paul720810/hermes-openclaw-attack-v7-4-20260617-013605 | Hermes OpenClaw Attack v7.4-20260617-013605 | Paul720810 | 2026-06-17T01:36:08.457000 | 1 | - |
| 392 | paul720810/hermes-openclaw-attack-v7-5-20260617-033553 | Hermes OpenClaw Attack v7.5-20260617-033553 | Paul720810 | 2026-06-17T03:35:55.913000 | 1 | - |
| 393 | tanetwonghong/dual-obfuscation | Dual-Obfuscation | Bangsaen AI | 2026-06-17T04:43:15.517000 | 1 | - |
| 394 | kuangyicheng/aas-original-attack | aas-original-attack | AbsoluterGeist | 2026-06-17T05:32:15.460000 | 1 | - |
| 395 | kuangyicheng/aas-dual-strategy-attack | aas-dual-strategy-attack | AbsoluterGeist | 2026-06-17T05:43:52.310000 | 1 | - |
| 396 | nakamurasyuta/jed-scoring-surface-analysis | JED Scoring Surface Analysis | Syuta | 2026-06-23T12:37:16.490000 | 16 | - |
| 397 | yashrajkeshari59194/notebook27af2aa2b5 | notebook27af2aa2b5 | Yash Raj Keshari | 2026-06-17T14:12:15.343000 | 1 | - |
| 398 | mdabdulalhasib/nexus-v1-ai-agent-attack | Nexus v1 ai agent attack | Md Abdul Al Hasib | 2026-06-18T10:45:16.843000 | 6 | - |
| 399 | felipe1983/aas-replay-dense-exfil-fork | aas replay dense exfil fork | Felipe KNBIS | 2026-06-18T13:24:02.377000 | 3 | - |
| 400 | paul720810/hermes-openclaw-attack-v7-5-20260618-133348 | Hermes OpenClaw Attack v7.5-20260618-133348 | Paul720810 | 2026-06-18T13:33:53.757000 | 3 | - |
| 401 | etnkaya/nwe-version-attack | nwe_version_attack | ÇETİN KAYA | 2026-06-18T15:11:16.460000 | 0 | - |
| 402 | paul720810/hermes-openclaw-attack-v7-5-20260618-142234 | Hermes OpenClaw Attack v7.5-20260618-142234 | Paul720810 | 2026-06-18T14:22:37.930000 | 0 | - |
| 403 | paul720810/hermes-openclaw-attack-v7-5-20260618-152315 | Hermes OpenClaw Attack v7.5-20260618-152315 | Paul720810 | 2026-06-18T15:23:20.773000 | 0 | - |
| 404 | paul720810/hermes-openclaw-attack-v7-5-20260618-162455 | Hermes OpenClaw Attack v7.5-20260618-162455 | Paul720810 | 2026-06-18T16:24:59.820000 | 1 | - |
| 405 | paul720810/hermes-openclaw-attack-v7-5-20260618-172614 | Hermes OpenClaw Attack v7.5-20260618-172614 | Paul720810 | 2026-06-18T17:26:19.047000 | 0 | - |
| 406 | paul720810/hermes-openclaw-attack-v7-5-20260618-182727 | Hermes OpenClaw Attack v7.5-20260618-182727 | Paul720810 | 2026-06-18T18:27:31.047000 | 0 | - |
| 407 | paul720810/hermes-openclaw-attack-v7-5-20260618-192836 | Hermes OpenClaw Attack v7.5-20260618-192836 | Paul720810 | 2026-06-18T19:28:40.847000 | 0 | - |
| 408 | paul720810/hermes-openclaw-attack-v7-5-20260618-202949 | Hermes OpenClaw Attack v7.5-20260618-202949 | Paul720810 | 2026-06-18T20:29:54.100000 | 1 | - |
| 409 | paul720810/hermes-openclaw-attack-v7-5-20260618-213136 | Hermes OpenClaw Attack v7.5-20260618-213136 | Paul720810 | 2026-06-18T21:31:40.010000 | 1 | - |
| 410 | paul720810/hermes-openclaw-attack-v9 | Hermes OpenClaw Attack v9 | Paul720810 | 2026-06-18T22:31:09.397000 | 1 | - |
| 411 | paul720810/hermes-openclaw-attack-v9-fix | Hermes OpenClaw Attack v9-fix | Paul720810 | 2026-06-19T04:10:30.650000 | 0 | - |
| 412 | vineetvsalimath/ai-agent-secure-2 | Ai-agent secure 2 | Vineet v Salimath | 2026-06-19T07:44:57.073000 | 0 | - |
| 413 | akshitasrivastava1/omega-attack-v6-0-ai-agent-security | OMEGA ATTACK v6.0 - AI Agent Security | Akshita Srivastava | 2026-06-19T07:44:18.210000 | 0 | - |
| 414 | shamseldeenismaiil/multi-step-tool-attack-engine | Multi-Step Tool Attack Engine | Shamseldeen ismaiil | 2026-06-20T01:31:56.590000 | 0 | - |
| 415 | hmnshudhmn24/ai-agent-security-multi-step-tool-attacks | AI Agent Security - Multi-Step Tool Attacks | Himanshu Dhiman | 2026-06-20T04:03:38.873000 | 1 | - |
| 416 | kokinnwakashuu/ai-agent-security-working-diary-v002 | AI Agent Security - Working Diary v002 | kokinnwakashuu | 2026-06-21T11:12:23.047000 | 8 | - |
| 417 | bang1850/attack-go-explore | attack go explore | ธนากร หาญวงค์ | 2026-06-21T09:10:48.620000 | 1 | - |
| 418 | paul720810/hermes-openclaw-attack-e005-20260620-175033 | Hermes OpenClaw Attack E005-20260620-175033 | Paul720810 | 2026-06-20T17:50:37.197000 | 0 | - |
| 419 | paul720810/hermes-openclaw-attack-e005-20260620-185147 | Hermes OpenClaw Attack E005-20260620-185147 | Paul720810 | 2026-06-20T18:51:50.543000 | 0 | - |
| 420 | paul720810/hermes-openclaw-attack-e005-20260620-195302 | Hermes OpenClaw Attack E005-20260620-195302 | Paul720810 | 2026-06-20T19:53:06.810000 | 0 | - |
| 421 | berkahkarya/ai-agent-security-attack-v54 | ai-agent-security-attack-v54 | Berkahkarya Dev | 2026-06-21T20:35:17.397000 | 0 | - |
| 422 | akshitasrivastava1/omega-attack-v8-single-call-saturation | omega attack v8 single call saturation | Akshita Srivastava | 2026-06-20T23:30:22.530000 | 0 | - |
| 423 | akshitasrivastava1/omega-attack-v8-1-safe-ceiling | omega attack v8 1 safe ceiling | Akshita Srivastava | 2026-06-21T00:00:32.560000 | 1 | - |
| 424 | tkhanna96/h006-win-len60-n490 | H006 Win Len60 N490 | Tkhanna96 | 2026-06-23T07:23:27.217000 | 1 | - |
| 425 | koushikkumardinda/ai-agent-security-replay-safe-exfiltration | 🛡️ AI Agent Security: Replay-Safe Exfiltration  | KOUSHIK KUMAR DINDA | 2026-08-25T03:24:00.537000 | 4 | - |
| 426 | ferozahmedds/securing-ai-agents-multi-step-attack-simulation | Securing AI Agents: Multi-Step Attack Simulation | Feroz Ahmed DS | 2026-06-21T06:04:27.633000 | 3 | - |
| 427 | kokinnwakashuu/ai-agent-security-v001-redteam-bank | AI Agent Security V001 Redteam Bank | kokinnwakashuu | 2026-06-27T00:05:56.337000 | 7 | - |
| 428 | iamsdt/taint-aware-quality-diversity-red-teaming | Taint-Aware Quality-Diversity Red-Teaming | Shudipto Trafder | 2026-06-21T15:22:54.343000 | 3 | - |
| 429 | geokocha/eda-multi-cell-bandit-attack | EDA Multi-Cell Bandit Attack | Yuanchen Huang | 2026-06-21T17:25:37.987000 | 4 | - |
| 430 | tkhanna96/h006-pilkwang-exact-77 | H006 Pilkwang Exact 77 | Tkhanna96 | 2026-06-23T10:25:48.533000 | 0 | - |
| 431 | tkhanna96/h006-multipost-k2-n300 | H006 Multipost K2 N300 | Tkhanna96 | 2026-06-21T17:44:27.647000 | 0 | - |
| 432 | rauffauzanrambe/chain-of-thought-security-mileware | Chain of Thought Security Mileware | Ra'uf Fauzan Rambe | 2026-06-22T04:42:42.473000 | 8 | - |
| 433 | souldrive/why-your-attack-completes-but-scores-blank | Why Your Attack Completes but Scores BLANK 🧱 | souldrive | 2026-09-02T12:01:10.777000 | 7 | - |
| 434 | paul720810/hermes-openclaw-attack-e005-20260622-121312 | Hermes OpenClaw Attack E005-20260622-121312 | Paul720810 | 2026-06-22T12:13:17.067000 | 3 | - |
| 435 | sgzk001/ai-agent-security-smoke-submit | ai-agent-security-smoke-submit | SGzK001 | 2026-06-22T15:18:23.820000 | 1 | - |
| 436 | paul720810/hermes-openclaw-attack-e005-20260622-181355 | Hermes OpenClaw Attack E005-20260622-181355 | Paul720810 | 2026-06-22T18:13:58.687000 | 1 | - |
| 437 | paul720810/hermes-openclaw-attack-e005-20260622-181838 | Hermes OpenClaw Attack E005-20260622-181838 | Paul720810 | 2026-06-22T18:18:43.980000 | 1 | - |
| 438 | akshitasrivastava1/omega-attack-v8-3-gemma-phrase-a | omega attack v8 3 gemma phrase a | Akshita Srivastava | 2026-06-22T22:39:59.277000 | 0 | - |
| 439 | paul720810/hermes-openclaw-attack-e005-20260623-020944 | Hermes OpenClaw Attack E005-20260623-020944 | Paul720810 | 2026-06-23T02:09:49.067000 | 1 | - |
| 440 | akshitasrivastava1/omega-attack-v8-4-n500-gemma-a | omega attack v8 4 n500 gemma a | Akshita Srivastava | 2026-06-23T06:27:21.860000 | 3 | - |
| 441 | ericyhs/ai-agent-security-attack-v0-4 | AI Agent Security Attack v0-4 | EricYHS | 2026-06-23T10:45:30.920000 | 3 | - |
| 442 | logiclab/test-deep | TEST：DEEP | LogicLab | 2026-06-26T01:04:28.800000 | 1 | - |
| 443 | akshitasrivastava1/omega-attack-v8-5-baseline-n500 | omega attack v8 5 baseline n500 | Akshita Srivastava | 2026-06-23T14:30:35.493000 | 1 | - |
| 444 | simplexcomplex/run-the-ai-agent-locally-without-a-gpu | Run the AI Agent Locally WITHOUT a GPU | Aryan Yadav | 2026-06-23T18:42:01.860000 | 8 | - |
| 445 | paul720810/hermes-openclaw-attack-e005-20260623-160546 | Hermes OpenClaw Attack E005-20260623-160546 | Paul720810 | 2026-06-23T16:05:50.180000 | 1 | - |
| 446 | paul720810/hermes-openclaw-attack-e005-20260623-160628 | Hermes OpenClaw Attack E005-20260623-160628 | Paul720810 | 2026-06-23T16:06:32.717000 | 1 | - |
| 447 | aristotelesborges84/notebook29ca6d58e7 | notebook29ca6d58e7 | Aristoteles Borges Oliveira | 2026-06-23T16:46:54.367000 | 1 | - |
| 448 | aristotelesborges84/notebooka2d33dc7a3 | notebooka2d33dc7a3 | Aristoteles Borges Oliveira | 2026-06-23T17:58:06.390000 | 1 | - |
| 449 | aristotelesborges84/notebookb5f47fc1d9 | notebookb5f47fc1d9 | Aristoteles Borges Oliveira | 2026-06-23T18:12:40.297000 | 1 | - |
| 450 | pengwang91/jed-attack-alpha2co-700 | JED Attack Alpha2co 700 | Peng Wang | 2026-06-23T21:05:43.377000 | 0 | - |
| 451 | pengwang91/jed-attack-alpha2co-680-gpu | JED Attack Alpha2co 680 GPU | Peng Wang | 2026-06-23T21:29:08.820000 | 1 | - |
| 452 | pengwang91/jed-attack-alpha2co-720-gpu | JED Attack Alpha2co 720 GPU | Peng Wang | 2026-06-23T21:29:10.367000 | 1 | - |
| 453 | pengwang91/jed-attack-alpha2co-760-t4b | JED Attack Alpha2co 760 T4b | Peng Wang | 2026-06-23T21:33:53.517000 | 1 | - |
| 454 | pengwang91/jed-attack-fastco-740-t4b | JED Attack Fastco 740 T4b | Peng Wang | 2026-06-23T21:33:54.967000 | 1 | - |
| 455 | pengwang91/jed-daily-20260624-620-proven-control | jed-daily-20260624-620-proven-control | Peng Wang | 2026-06-24T00:13:09.673000 | 1 | - |
| 456 | pengwang91/jed-daily-20260624-667-reference-control | jed-daily-20260624-667-reference-control | Peng Wang | 2026-06-24T00:16:59.283000 | 1 | - |
| 457 | pengwang91/jed-daily-20260624-720-ref-retry-t4 | jed-daily-20260624-720-ref-retry-t4 | Peng Wang | 2026-06-24T00:17:34.387000 | 1 | - |
| 458 | pengwang91/jed-daily-20260624-700-near-ref-wording | jed-daily-20260624-700-near-ref-wording | Peng Wang | 2026-06-24T00:18:09.557000 | 1 | - |
| 459 | pengwang91/jed-daily-20260624-400-multi2-exploration | jed-daily-20260624-400-multi2-exploration | Peng Wang | 2026-06-24T00:18:44.773000 | 1 | - |
| 460 | paul720810/hermes-openclaw-attack-e005-20260624-040715 | Hermes OpenClaw Attack E005-20260624-040715 | Paul720810 | 2026-06-24T04:07:18.423000 | 1 | - |
| 461 | paul720810/hermes-openclaw-attack-e005-20260624-060737 | Hermes OpenClaw Attack E005-20260624-060737 | Paul720810 | 2026-06-24T06:07:41.463000 | 0 | - |
| 462 | paul720810/hermes-openclaw-attack-e005-20260624-060827 | Hermes OpenClaw Attack E005-20260624-060827 | Paul720810 | 2026-06-24T06:08:31.613000 | 0 | - |
| 463 | bigbag1983/ai-agent-security-attack-v9 | AI Agent Security Attack v9 | PavelLiashkov | 2026-06-24T06:25:56.863000 | 0 | - |
| 464 | paul720810/hermes-openclaw-attack-e005-20260624-080921 | Hermes OpenClaw Attack E005-20260624-080921 | Paul720810 | 2026-06-24T08:09:24.687000 | 0 | - |
| 465 | teisnestech/notebookf94cc567e4 | notebookf94cc567e4 | Teisnes Tech | 2026-06-24T23:11:00.417000 | 0 | - |
| 466 | khj1222/aisec-exfil-fill-644 | aisec-exfil-fill-644 | khj1222 | 2026-06-24T11:49:23.963000 | 0 | - |
| 467 | khj1222/aisec-exfil-fill-648 | aisec-exfil-fill-648 | khj1222 | 2026-06-24T12:00:35.967000 | 0 | - |
| 468 | paul720810/hermes-openclaw-attack-e005-20260624-121821 | Hermes OpenClaw Attack E005-20260624-121821 | Paul720810 | 2026-06-24T12:18:25.497000 | 3 | - |
| 469 | junaid512/ai-agent | AI Agent | Muhammad Junaid | 2026-06-24T17:33:24.417000 | 0 | - |
| 470 | ckyasb/ai-agent-security-attack | ai-agent-security-attack | ckyasb | 2026-06-25T17:50:01.913000 | 1 | - |
| 471 | tensorliu/jed-attack-nb-v2 | JED Attack NB v2 | Chang Liu | 2026-06-24T14:33:20.210000 | 0 | - |
| 472 | tensorliu/jed-attack-nb-v3 | JED Attack NB v3 | Chang Liu | 2026-06-24T13:27:39.077000 | 0 | - |
| 473 | souldrive/the-replay-wall-and-the-guardrail-mirror | The Replay Wall and the Guardrail Mirror | souldrive | 2026-09-02T12:01:15.997000 | 4 | - |
| 474 | manderson240/agent-security-mcts-attack-20260624-1526 | Agent Security MCTS Attack 20260624-1526 | Mike Anderson | 2026-06-24T17:19:47.977000 | 1 | - |
| 475 | paul720810/hermes-openclaw-attack-e005-20260624-160707 | Hermes OpenClaw Attack E005-20260624-160707 | Paul720810 | 2026-06-24T16:07:11.997000 | 3 | - |
| 476 | paul720810/hermes-openclaw-attack-e005-20260624-160919 | Hermes OpenClaw Attack E005-20260624-160919 | Paul720810 | 2026-06-24T16:09:24.117000 | 1 | - |
| 477 | pengwang91/jed-daily-20260625-620-proven-control | jed-daily-20260625-620-proven-control | Peng Wang | 2026-06-25T03:26:43.873000 | 1 | - |
| 478 | djenkivanov/local-validation-guide | Local Validation Guide | Djenk Ivanov | 2026-06-24T22:10:33.250000 | 27 | - |
| 479 | irongm/omega-attack-v8-6-gemma-b-n450 | omega attack v8 6 gemma b n450 | IRON GM | 2026-06-24T21:28:50.393000 | 1 | - |
| 480 | maj0rt0m/private-eval-proxy | Private-Eval Proxy | MAJ0RT0M | 2026-06-26T00:09:20.527000 | 5 | - |
| 481 | qinggedada/v7-read-multipost-delete-hybrid | V7 Read-Multipost + Delete Hybrid | qinggedada | 2026-06-25T06:24:06.543000 | 5 | - |
| 482 | aman5153684/sentinel-alpha2co-700-break62 | sentinel-alpha2co-700-break62 | Aman Sharma | 2026-06-26T05:04:23.207000 | 6 | - |
| 483 | sud0su/ai-agent-security-v8-attack | ai-agent-security-v8-attack | sud0su | 2026-06-25T07:11:34.883000 | 4 | - |
| 484 | kiluazen/aas-clone-best | AAS Clone Best | kiluazen | 2026-06-25T10:10:37.460000 | 1 | - |
| 485 | qinggedada/v8-gold-targeted-multi-cell | V8 Gold-Targeted Multi-Cell | qinggedada | 2026-06-25T07:26:26.120000 | 2 | - |
| 486 | qinggedada/v9-4-cell-targeted-attack | V9 4-Cell Targeted Attack | qinggedada | 2026-06-25T07:27:05.637000 | 1 | - |
| 487 | paul720810/hermes-openclaw-attack-e005-20260625-080918 | Hermes OpenClaw Attack E005-20260625-080918 | Paul720810 | 2026-06-25T08:09:23.147000 | 1 | - |
| 488 | paul720810/hermes-openclaw-attack-e005-20260625-120737 | Hermes OpenClaw Attack E005-20260625-120737 | Paul720810 | 2026-06-25T12:07:41.380000 | 0 | - |
| 489 | jiamengzhangjemma/ai-agent-security-v80-dualpost-nb-20260625 | AI Agent Security V80 Dualpost NB 20260625 | Jemma | 2026-06-25T14:00:28.267000 | 0 | - |
| 490 | jiamengzhangjemma/ai-agent-security-v81-clean-attackpy-20260625 | AI Agent Security V81 Clean Attackpy 20260625 | Jemma | 2026-06-25T13:57:14.597000 | 0 | - |
| 491 | jiamengzhangjemma/ai-agent-security-v82-clean-attackpy-cpu-20260625 | AI Agent Security V82 Clean Attackpy CPU 20260625 | Jemma | 2026-06-26T14:14:15.923000 | 1 | - |
| 492 | paul720810/hermes-openclaw-attack-e005-20260625-140800 | Hermes OpenClaw Attack E005-20260625-140800 | Paul720810 | 2026-06-25T14:08:04.950000 | 0 | - |
| 493 | udaken10/les-s-read-the-sdk | Les's_read_the_SDK | really? | 2026-06-26T05:16:32.537000 | 2 | - |
| 494 | udaken10/advancedmultipredicateattack | AdvancedMultiPredicateAttack | really? | 2026-06-25T22:51:24.030000 | 1 | - |
| 495 | paul720810/hermes-openclaw-attack-e005-20260625-161241 | Hermes OpenClaw Attack E005-20260625-161241 | Paul720810 | 2026-06-25T16:12:44.770000 | 0 | - |
| 496 | ghazarosbarseghyan91/ai-agent-security-multi-step-tool-attacks-v21 | AI Agent Security Multi-Step Tool Attacks v21 | Ghazaros Barseghyan | 2026-06-29T11:47:10.327000 | 1 | - |
| 497 | paul720810/hermes-openclaw-attack-e005-20260625-180903 | Hermes OpenClaw Attack E005-20260625-180903 | Paul720810 | 2026-06-25T18:09:07.097000 | 3 | - |
| 498 | paul720810/hermes-openclaw-attack-e005-20260625-200702 | Hermes OpenClaw Attack E005-20260625-200702 | Paul720810 | 2026-06-25T20:07:05.450000 | 1 | - |
| 499 | paul720810/hermes-openclaw-attack-e005-20260625-200905 | Hermes OpenClaw Attack E005-20260625-200905 | Paul720810 | 2026-06-25T20:09:10.797000 | 1 | - |
| 500 | maj0rt0m/private-eval-proxy-gpu | Private-Eval Proxy (GPU) | MAJ0RT0M | 2026-06-26T00:10:56.557000 | 9 | - |
| 501 | paul720810/hermes-openclaw-attack-e005-20260625-221411 | Hermes OpenClaw Attack E005-20260625-221411 | Paul720810 | 2026-06-25T22:14:15.173000 | 1 | - |
| 502 | paul720810/hermes-openclaw-attack-e005-20260626-040151 | Hermes OpenClaw Attack E005-20260626-040151 | Paul720810 | 2026-06-26T04:01:53.870000 | 1 | - |
| 503 | kiranvitly/ai-agent-security-attack | AI Agent Security Attack | Kiran Vitly | 2026-07-03T14:37:09.727000 | 4 | - |
| 504 | paul720810/hermes-openclaw-attack-e005-20260626-080717 | Hermes OpenClaw Attack E005-20260626-080717 | Paul720810 | 2026-06-26T08:07:21.700000 | 0 | - |
| 505 | agentzz/ai-agent-security-working-note | ai agent security working note | ⸻AgentZZ ⸻ | 2026-06-26T08:56:19.890000 | 0 | - |
| 506 | chrisopherjoshy/ai-agent-security-attack | ai-agent-security-attack | Chriz | 2026-06-26T09:46:24.937000 | 0 | - |
| 507 | paul720810/hermes-openclaw-attack-e005-20260626-120947 | Hermes OpenClaw Attack E005-20260626-120947 | Paul720810 | 2026-06-26T12:09:52.710000 | 0 | - |
| 508 | akshitasrivastava1/omega-attack-v10-0-v82-secret-marker | omega attack v10 0 v82 secret marker | Akshita Srivastava | 2026-06-30T11:11:05.057000 | 1 | - |
| 509 | kokinnwakashuu/ai-agent-security-v038-pipeline-check | AI Agent Security v038 pipeline check | kokinnwakashuu | 2026-07-01T10:18:48.207000 | 10 | - |
| 510 | paul720810/hermes-openclaw-attack-e005-20260627-020837 | Hermes OpenClaw Attack E005-20260627-020837 | Paul720810 | 2026-06-27T02:08:42.517000 | 0 | - |
| 511 | qinggedada/agent-security-v7-llm-evolution-attacks | Agent Security V7 LLM Evolution Attacks | qinggedada | 2026-06-27T02:32:25.913000 | 0 | - |
| 512 | paul720810/hermes-openclaw-attack-e005-20260627-121730 | Hermes OpenClaw Attack E005-20260627-121730 | Paul720810 | 2026-06-27T12:17:35.127000 | 1 | - |
| 513 | kiranvitly/agent-attack-v13 | Agent Attack v13 | Kiran Vitly | 2026-06-27T14:42:46.670000 | 3 | - |
| 514 | paul720810/hermes-openclaw-attack-e005-20260627-180517 | Hermes OpenClaw Attack E005-20260627-180517 | Paul720810 | 2026-06-27T18:05:21.780000 | 0 | - |
| 515 | bigbag1983/ai-agent-security-attack-v12 | AI Agent Security Attack v12 | PavelLiashkov | 2026-06-28T03:20:52.543000 | 0 | - |
| 516 | emanuellcs/aias-agent | AIAS Agent | Emanuel Lázaro | 2026-06-28T22:29:59.207000 | 5 | - |
| 517 | paul720810/hermes-openclaw-attack-e005-20260628-001214 | Hermes OpenClaw Attack E005-20260628-001214 | Paul720810 | 2026-06-28T00:12:19.357000 | 1 | - |
| 518 | paul720810/hermes-openclaw-attack-e005-20260628-001401 | Hermes OpenClaw Attack E005-20260628-001401 | Paul720810 | 2026-06-28T00:14:07.163000 | 1 | - |
| 519 | paul720810/hermes-openclaw-attack-e005-20260628-021533 | Hermes OpenClaw Attack E005-20260628-021533 | Paul720810 | 2026-06-28T02:15:37.210000 | 1 | - |
| 520 | paul720810/hermes-openclaw-attack-e005-20260628-021718 | Hermes OpenClaw Attack E005-20260628-021718 | Paul720810 | 2026-06-28T02:17:22.450000 | 1 | - |
| 521 | paul720810/hermes-openclaw-attack-e005-20260628-021828 | Hermes OpenClaw Attack E005-20260628-021828 | Paul720810 | 2026-06-28T02:18:32.413000 | 1 | - |
| 522 | paul720810/hermes-openclaw-attack-e005-20260628-080608 | Hermes OpenClaw Attack E005-20260628-080608 | Paul720810 | 2026-06-28T08:06:11.553000 | 3 | - |
| 523 | jiamengzhangjemma/as-v80-template-20260628 | AS V80 Template 20260628 | Jemma | 2026-06-28T09:13:28.930000 | 3 | - |
| 524 | matthewblakeward/jed-red-team-winning-attack | JED Red-Team Winning Attack | Matthew Blake Ward | 2026-06-28T10:05:01.870000 | 4 | - |
| 525 | akshitasrivastava1/omega-attack-v10-1-n560-no-placeholder | omega attack v10 1 n560 no placeholder | Akshita Srivastava | 2026-06-28T13:58:32.067000 | 0 | - |
| 526 | akshitasrivastava1/omega-attack-v10-2-n420-peak-safe | omega attack v10 2 n420 peak safe | Akshita Srivastava | 2026-06-28T18:23:37.057000 | 0 | - |
| 527 | jiamengzhangjemma/as-adaptive-v2-20260628 | AS Adaptive V2 20260628 | Jemma | 2026-06-28T21:43:01.210000 | 1 | - |
| 528 | ghazarosbarseghyan91/agent-security-multi-step-attacks-v21 | Agent Security Multi Step Attacks v21 | Ghazaros Barseghyan | 2026-07-02T21:17:10.680000 | 2 | - |
| 529 | paul720810/hermes-openclaw-attack-e005-20260629-001115 | Hermes OpenClaw Attack E005-20260629-001115 | Paul720810 | 2026-06-29T00:11:21.067000 | 3 | - |
| 530 | paul720810/hermes-openclaw-attack-e005-20260629-040732 | Hermes OpenClaw Attack E005-20260629-040732 | Paul720810 | 2026-06-29T04:07:36.663000 | 0 | - |
| 531 | paul720810/hermes-openclaw-attack-e005-20260629-081200 | Hermes OpenClaw Attack E005-20260629-081200 | Paul720810 | 2026-06-29T08:12:03.657000 | 2 | - |
| 532 | paul720810/hermes-openclaw-attack-e005-20260629-081305 | Hermes OpenClaw Attack E005-20260629-081305 | Paul720810 | 2026-06-29T08:13:08.343000 | 2 | - |
| 533 | paul720810/hermes-openclaw-attack-e005-20260629-101001 | Hermes OpenClaw Attack E005-20260629-101001 | Paul720810 | 2026-06-29T10:10:05.957000 | 3 | - |
| 534 | hashimrazi/attack-template-validator | Attack Template Validator | 9Hash | 2026-06-29T10:40:58.627000 | 4 | - |
| 535 | lucifer19/v9-hop-saturation-overdrive | V9 — Hop Saturation Overdrive 🔥🚀 | Krizsó Gergely | 2026-06-29T15:12:35.100000 | 4 | - |
| 536 | jiamengzhangjemma/as-static-v3-safe-20260629 | AS Static V3 Safe 20260629 | Jemma | 2026-06-29T16:34:00.720000 | 0 | - |
| 537 | aristotelesborges84/notebookbf5cac589b | notebookbf5cac589b | Aristoteles Borges Oliveira | 2026-06-29T19:19:29 | 0 | - |
| 538 | aristotelesborges84/notebook4f47354ee4 | notebook4f47354ee4 | Aristoteles Borges Oliveira | 2026-06-29T20:17:09.397000 | 0 | - |
| 539 | paul720810/hermes-openclaw-attack-e005-20260630-000719 | Hermes OpenClaw Attack E005-20260630-000719 | Paul720810 | 2026-06-30T00:07:23.417000 | 0 | - |
| 540 | mtoshidesu/test-ai-security-urad-code | test-AI Security URAD Code | m-toshi desu | 2026-06-30T01:19:51.147000 | 0 | - |
| 541 | mtoshidesu/test-ai-agent-security-001 | test AI AGENT SECURITY 001  | m-toshi desu | 2026-06-30T05:15:29.570000 | 0 | - |
| 542 | mtoshidesu/test-ai-agent-0fa258 | test-AI Agent 0fa258 | m-toshi desu | 2026-06-30T05:30:51.957000 | 0 | - |
| 543 | mtoshidesu/test-jed-attack-improved-nb | test JED Attack Improved NB | m-toshi desu | 2026-06-30T05:42:46.180000 | 0 | - |
| 544 | mtoshidesu/notebook48684707e0 | notebook48684707e0 | m-toshi desu | 2026-06-30T05:45:49.637000 | 1 | - |
| 545 | jiamengzhangjemma/as-public-wall-n560-20260630 | AS Public Wall N560 20260630 | Jemma | 2026-06-30T07:30:59.973000 | 2 | - |
| 546 | paul720810/hermes-openclaw-attack-e005-20260630-081455 | Hermes OpenClaw Attack E005-20260630-081455 | Paul720810 | 2026-06-30T08:14:58.793000 | 2 | - |
| 547 | paul720810/hermes-openclaw-attack-e005-20260630-082149 | Hermes OpenClaw Attack E005-20260630-082149 | Paul720810 | 2026-06-30T08:21:53.677000 | 2 | - |
| 548 | sol12378/hosted-replay-economics-aas-working-note | Hosted Replay Economics - AAS Working Note | sol12378 | 2026-06-30T12:21:54.270000 | 2 | - |
| 549 | paul720810/hermes-openclaw-attack-e005-20260630-180356 | Hermes OpenClaw Attack E005-20260630-180356 | Paul720810 | 2026-06-30T18:03:59.530000 | 1 | - |
| 550 | busyaprime/ai-agent-security-getting-started | AI Agent Security: Getting Started | Busya PRIME | 2026-06-30T18:54:31.413000 | 1 | - |
| 551 | farmountain/harness-test-ai-agent-security-sub01 | Harness Test Ai Agent Security Sub01 | Liew Keong Han | 2026-07-01T00:24:28.327000 | 1 | - |
| 552 | paul720810/hermes-openclaw-attack-e005-20260701-021139 | Hermes OpenClaw Attack E005-20260701-021139 | Paul720810 | 2026-07-01T02:11:43.280000 | 1 | - |
| 553 | paul720810/hermes-openclaw-attack-e005-20260701-021235 | Hermes OpenClaw Attack E005-20260701-021235 | Paul720810 | 2026-07-01T02:12:38.313000 | 1 | - |
| 554 | paul720810/hermes-openclaw-attack-e005-20260701-021335 | Hermes OpenClaw Attack E005-20260701-021335 | Paul720810 | 2026-07-01T02:13:38.943000 | 1 | - |
| 555 | paul720810/hermes-openclaw-attack-e005-20260701-040507 | Hermes OpenClaw Attack E005-20260701-040507 | Paul720810 | 2026-07-01T04:05:10.593000 | 2 | - |
| 556 | paul720810/hermes-openclaw-attack-e005-20260701-040634 | Hermes OpenClaw Attack E005-20260701-040634 | Paul720810 | 2026-07-01T04:06:38.997000 | 2 | - |
| 557 | tamiltechno/mutation-attack | Mutation Attack | Chandru | 2026-07-01T08:47:35.980000 | 4 | - |
| 558 | paul720810/hermes-openclaw-attack-e005-20260701-081023 | Hermes OpenClaw Attack E005-20260701-081023 | Paul720810 | 2026-07-01T08:10:27.333000 | 1 | - |
| 559 | paul720810/hermes-openclaw-attack-e005-20260701-081213 | Hermes OpenClaw Attack E005-20260701-081213 | Paul720810 | 2026-07-01T08:12:17.023000 | 1 | - |
| 560 | rauffauzanrambe/ai-security-sot-of-multi-tools-safe-v9 | AI Security SoT of Multi Tools Safe V9 | Ra'uf Fauzan Rambe | 2026-07-01T10:02:17.190000 | 4 | - |
| 561 | georgymamarin/red-team-starter-what-fires-and-what-it-s-worth | Red-team starter: what fires, and what it's worth | Georgy Mamarin | 2026-08-19T10:41:42.900000 | 51 | - |
| 562 | paul720810/hermes-openclaw-attack-e005-20260702-000929 | Hermes OpenClaw Attack E005-20260702-000929 | Paul720810 | 2026-07-02T00:09:34.243000 | 1 | - |
| 563 | paul720810/hermes-openclaw-attack-e005-20260702-002343 | Hermes OpenClaw Attack E005-20260702-002343 | Paul720810 | 2026-07-02T00:23:49.847000 | 1 | - |
| 564 | paul720810/hermes-openclaw-attack-e005-20260702-002510 | Hermes OpenClaw Attack E005-20260702-002510 | Paul720810 | 2026-07-02T00:25:15.150000 | 2 | - |
| 565 | untouchableforest/fork-v22-urlcompact-642-orig-caoyupeng-57-78 | Fork: V22 URLCompact 642 (orig. caoyupeng, 57.78) | Maria Startseva | 2026-07-02T09:51:54.007000 | 2 | - |
| 566 | n0rollback/reading-the-ai-agent-security-leaderboard | Reading the AI Agent Security Leaderboard | n0Rollback 🇩🇿🇫🇷 | 2026-07-02T19:22:44.837000 | 1 | - |
| 567 | rumblingb/provenance-note-20260702 | Provenance Note 20260702 | rumbling_b | 2026-07-02T22:19:56.090000 | 0 | - |
| 568 | pengwang91/jed-cleanimp560-marker | jed-cleanimp560-marker | Peng Wang | 2026-07-03T00:50:00.467000 | 1 | - |
| 569 | pengwang91/jed-cleanimp610-marker | jed-cleanimp610-marker | Peng Wang | 2026-07-03T00:50:36.063000 | 1 | - |
| 570 | pengwang91/jed-cleanimp636-marker | jed-cleanimp636-marker | Peng Wang | 2026-07-03T00:51:11.183000 | 1 | - |
| 571 | pengwang91/jed-cleanimp667-marker | jed-cleanimp667-marker | Peng Wang | 2026-07-03T00:51:45.993000 | 1 | - |
| 572 | naka84/guardrails-s-flow-chart | Guardrails's Flow Chart | Nakanishi | 2026-07-04T05:51:02.023000 | 1 | - |
| 573 | paul720810/hermes-openclaw-attack-e005-20260703-021019 | Hermes OpenClaw Attack E005-20260703-021019 | Paul720810 | 2026-07-03T02:10:22.920000 | 1 | - |
| 574 | paul720810/hermes-openclaw-attack-e005-20260703-040359 | Hermes OpenClaw Attack E005-20260703-040359 | Paul720810 | 2026-07-03T04:04:03.343000 | 1 | - |
| 575 | paul720810/hermes-openclaw-attack-e005-20260703-101916 | Hermes OpenClaw Attack E005-20260703-101916 | Paul720810 | 2026-07-03T10:19:20.780000 | 0 | - |
| 576 | paul720810/hermes-openclaw-attack-e005-20260703-141248 | Hermes OpenClaw Attack E005-20260703-141248 | Paul720810 | 2026-07-03T14:12:51.843000 | 1 | - |
| 577 | paul720810/hermes-openclaw-attack-e005-20260703-181226 | Hermes OpenClaw Attack E005-20260703-181226 | Paul720810 | 2026-07-03T18:12:31.270000 | 1 | - |
| 578 | yuriymikityuk/jed-red-team-teardown | JED Red-Team Teardown | Yuriy Mikityuk | 2026-07-03T22:07:25.313000 | 2 | - |
| 579 | paul720810/hermes-openclaw-attack-e005-20260704-020719 | Hermes OpenClaw Attack E005-20260704-020719 | Paul720810 | 2026-07-04T02:07:24.867000 | 0 | - |
| 580 | pengwang91/jed-indirect-marker180 | jed-indirect-marker180 | Peng Wang | 2026-07-04T02:30:48.460000 | 0 | - |
| 581 | pengwang91/jed-indirect-marker240 | jed-indirect-marker240 | Peng Wang | 2026-07-04T02:31:24.307000 | 0 | - |
| 582 | pengwang91/jed-indirect-marker300 | jed-indirect-marker300 | Peng Wang | 2026-07-04T02:32:00.520000 | 0 | - |
| 583 | pengwang91/jed-indirect-marker360 | jed-indirect-marker360 | Peng Wang | 2026-07-04T02:32:36.687000 | 0 | - |
| 584 | drkongvis/agent-security-v1-baseline | agent-security-v1-baseline | Jet | 2026-07-04T07:12:18.150000 | 1 | - |
| 585 | paul720810/hermes-openclaw-attack-e005-20260704-081003 | Hermes OpenClaw Attack E005-20260704-081003 | Paul720810 | 2026-07-04T08:10:05.730000 | 1 | - |
| 586 | paul720810/hermes-openclaw-attack-e005-20260704-081127 | Hermes OpenClaw Attack E005-20260704-081127 | Paul720810 | 2026-07-04T08:11:31.140000 | 1 | - |
| 587 | gautampatil9898/state-space-agent-attack-search | state-space-agent-attack-search | gautam patil | 2026-07-04T13:56:45.883000 | 1 | - |
| 588 | pengwang91/jed-cleanimp480-marker | jed-cleanimp480-marker | Peng Wang | 2026-07-04T19:16:56.390000 | 0 | - |
| 589 | pengwang91/jed-cleanimp460-marker | jed-cleanimp460-marker | Peng Wang | 2026-07-05T01:06:27.773000 | 1 | - |
| 590 | pengwang91/jed-shortimp475-marker | jed-shortimp475-marker | Peng Wang | 2026-07-05T01:07:01.493000 | 1 | - |
| 591 | pengwang91/jed-shortimp500-marker | jed-shortimp500-marker | Peng Wang | 2026-07-05T01:07:36.590000 | 1 | - |
| 592 | verise6211/aas-persona | AAS Persona | verise6211 | 2026-07-05T03:20:49.367000 | 0 | - |
| 593 | paul720810/hermes-openclaw-attack-e005-20260705-040747 | Hermes OpenClaw Attack E005-20260705-040747 | Paul720810 | 2026-07-05T04:07:51.543000 | 0 | - |
| 594 | ducnamphan/jed-attack-v0-80-multi-call | JED Attack v0.80 — Multi-Call | Duc Nam Phan | 2026-07-05T06:25:32.887000 | 1 | - |
| 595 | ducnamphan/jed-attack-v0-90-all-in-multi-call | JED Attack v0.90 — All-In Multi-Call | Duc Nam Phan | 2026-07-05T06:27:38.353000 | 1 | - |
| 596 | ducnamphan/jed-attack-v0-95-ultimate | JED Attack v0.95 — Ultimate | Duc Nam Phan | 2026-07-05T06:28:51.940000 | 4 | - |
| 597 | ducnamphan/jed-attack-v1-0-high-call | JED Attack v1.0 — High-Call | Duc Nam Phan | 2026-07-05T08:22:37.847000 | 3 | - |
| 598 | qyq1693/ai-agent-security-multi-dense-attack-v8 | ai-agent-security-multi-dense-attack-v8 | QYQ1693 | 2026-07-06T11:11:21.067000 | 1 | - |
| 599 | konitac/aias-preliminary-submission-format-checker | AIAS - Preliminary Submission Format Checker | 🫠konita🫠 | 2026-07-05T13:43:47.727000 | 3 | - |
| 600 | ducnamphan/jed-attack-v2-0-8-call | JED Attack v2.0 — 8-Call | Duc Nam Phan | 2026-07-05T14:04:33.663000 | 1 | - |
| 601 | ducnamphan/jed-attack-v3-0-probe-validated | JED Attack v3.0 — Probe-Validated | Duc Nam Phan | 2026-07-05T15:30:17.717000 | 1 | - |
| 602 | busyaprime/what-fires-and-what-its-worth | What Fires And What Its Worth | Busya PRIME | 2026-07-05T15:41:57.170000 | 2 | - |
| 603 | ducnamphan/jed-attack-v5-0-mass-exfil | JED Attack v5.0 — Mass EXFIL | Duc Nam Phan | 2026-07-05T15:44:09.097000 | 1 | - |
| 604 | ducnamphan/jed-v5-5-production-final | JED v5.5 — Production Final | Duc Nam Phan | 2026-07-05T17:14:39.260000 | 1 | - |
| 605 | busyaprime/two-flow-properties-behind-four-attack-predicates | Two flow properties behind four attack predicates | Busya PRIME | 2026-07-05T19:35:40.027000 | 2 | - |
| 606 | devchandra/ai-agent-security-v68b-bikram-v10-56-87 | AI Agent Security v68b Bikram v10 56.87 | Dr Chandrasen Pandey | 2026-07-06T01:19:48.690000 | 1 | - |
| 607 | paul720810/auto-build-20260706-040938 | auto-build 20260706-040938 | Paul720810 | 2026-07-06T04:09:42.390000 | 1 | - |
| 608 | paul720810/hermes-openclaw-attack-e005-20260706-053700 | Hermes OpenClaw Attack E005-20260706-053700 | Paul720810 | 2026-07-06T05:37:04.807000 | 1 | - |
| 609 | paul720810/hermes-openclaw-attack-e005-20260706-053718 | Hermes OpenClaw Attack E005-20260706-053718 | Paul720810 | 2026-07-06T05:37:22.807000 | 1 | - |
| 610 | paul720810/hermes-openclaw-attack-e005-20260706-053756 | Hermes OpenClaw Attack E005-20260706-053756 | Paul720810 | 2026-07-06T05:37:59.857000 | 1 | - |
| 611 | paul720810/hermes-openclaw-attack-e005-20260706-053818 | Hermes OpenClaw Attack E005-20260706-053818 | Paul720810 | 2026-07-06T05:38:23.307000 | 1 | - |
| 612 | paul720810/hermes-openclaw-attack-e005-20260706-053858 | Hermes OpenClaw Attack E005-20260706-053858 | Paul720810 | 2026-07-06T05:39:01.820000 | 1 | - |
| 613 | paul720810/hermes-openclaw-attack-e005-20260706-053900 | Hermes OpenClaw Attack E005-20260706-053900 | Paul720810 | 2026-07-06T05:39:04.013000 | 1 | - |
| 614 | paul720810/hermes-openclaw-attack-e005-20260706-053932 | Hermes OpenClaw Attack E005-20260706-053932 | Paul720810 | 2026-07-06T05:39:35.193000 | 1 | - |
| 615 | paul720810/hermes-openclaw-attack-e005-20260706-053933 | Hermes OpenClaw Attack E005-20260706-053933 | Paul720810 | 2026-07-06T05:39:37.570000 | 1 | - |
| 616 | paul720810/hermes-openclaw-attack-e005-20260706-053954 | Hermes OpenClaw Attack E005-20260706-053954 | Paul720810 | 2026-07-06T05:39:58.010000 | 1 | - |
| 617 | paul720810/hermes-openclaw-attack-e005-20260706-054013 | Hermes OpenClaw Attack E005-20260706-054013 | Paul720810 | 2026-07-06T05:40:17.733000 | 1 | - |
| 618 | paul720810/hermes-openclaw-attack-e005-20260706-054029 | Hermes OpenClaw Attack E005-20260706-054029 | Paul720810 | 2026-07-06T05:40:33.037000 | 1 | - |
| 619 | jayanthpattela/attacking | Attacking | Jayanth Pattela | 2026-07-06T09:45:03.490000 | 0 | - |
| 620 | paul720810/hermes-openclaw-attack-e005-20260706-081625 | Hermes OpenClaw Attack E005-20260706-081625 | Paul720810 | 2026-07-06T08:16:29.560000 | 2 | - |
| 621 | paul720810/hermes-openclaw-attack-e005-20260706-081850 | Hermes OpenClaw Attack E005-20260706-081850 | Paul720810 | 2026-07-06T08:18:54.240000 | 1 | - |
| 622 | paul720810/hermes-openclaw-attack-e005-20260706-082026 | Hermes OpenClaw Attack E005-20260706-082026 | Paul720810 | 2026-07-06T08:20:31.283000 | 1 | - |
| 623 | gautampatil9898/state-space-agent-attack-search-1 | state-space-agent-attack-search-1 | gautam patil | 2026-07-06T11:03:13.680000 | 0 | - |
| 624 | ghazarosbarseghyan91/jed-attack-map-elites-archive | JED Attack — MAP-Elites Archive | Ghazaros Barseghyan | 2026-07-06T13:02:38.297000 | 0 | - |
| 625 | pengwang91/jed-fill-mech-v2-control | jed-fill-mech-v2-control | Peng Wang | 2026-07-06T22:37:03.783000 | 0 | - |
| 626 | pengwang91/jed-fill-noreason-short | jed-fill-noreason-short | Peng Wang | 2026-07-06T22:38:40.663000 | 0 | - |
| 627 | pengwang91/jed-fill-post-noreason | jed-fill-post-noreason | Peng Wang | 2026-07-06T22:39:13.740000 | 1 | - |
| 628 | khj1222/ai-agent-security-working-note | AI Agent Security Working Note | khj1222 | 2026-09-03T11:10:10.690000 | 0 | - |
| 629 | devchandra/ai-agent-security-v72-peng-mech-noval-m35 | AI Agent Security v72 Peng mech noval m35 | Dr Chandrasen Pandey | 2026-07-07T03:05:12.197000 | 0 | - |
| 630 | qyq1693/ai-agent-security-dense-v10 | ai-agent-security-dense-v10 | QYQ1693 | 2026-07-07T06:09:59.487000 | 0 | - |
| 631 | uditjain13/the-0-byte-submission-bug-guardrail-anatomy | The 0-Byte Submission Bug + Guardrail Anatomy | Udit Jain | 2026-07-07T09:21:09.053000 | 3 | - |
| 632 | qyq1693/ai-agent-security-speed-v11 | ai-agent-security-speed-v11 | QYQ1693 | 2026-07-07T10:02:54.627000 | 0 | - |
| 633 | paul720810/hermes-v19-replica-best-33-660 | Hermes V19 Replica Best 33.660 | Paul720810 | 2026-07-07T12:25:34.417000 | 2 | - |
| 634 | ducnamphan/jed-v9-0-multi-tool | JED v9.0 Multi-Tool | Duc Nam Phan | 2026-07-08T02:03:22.900000 | 1 | - |
| 635 | ducnamphan/jed-v12-0-uta-amplifier | JED v12.0 UTA Amplifier | Duc Nam Phan | 2026-07-08T15:50:54.507000 | 1 | - |
| 636 | ducnamphan/jed-v13-0-compact-n-250 | JED v13.0 Compact N=250 | Duc Nam Phan | 2026-07-08T15:53:52.760000 | 1 | - |
| 637 | rumblingb/ai-security-lb60525-yusuke-fork-20260708 | AI Security LB60525 Yusuke Fork 20260708 | rumbling_b | 2026-07-08T16:01:22.523000 | 1 | - |
| 638 | rumblingb/ai-agent-security-working-note-rumblingb | Ai Agent Security Working Note Rumblingb | rumbling_b | 2026-07-09T04:09:37.257000 | 0 | - |
| 639 | harmeetkaur24/attack-notebook | Attack_Notebook | Harmeet Kaur | 2026-07-09T07:30:09.497000 | 0 | - |
| 640 | ducnamphan/jed-v14-0-task-blended | JED v14.0 Task-Blended | Duc Nam Phan | 2026-07-09T17:23:48.440000 | 0 | - |
| 641 | ducnamphan/jed-v15-0-5-paper-integration | JED v15.0 5-Paper Integration | Duc Nam Phan | 2026-07-09T17:27:09.867000 | 0 | - |
| 642 | ducnamphan/jed-v16-0-calibrated-n-300 | JED v16.0 Calibrated N=300 | Duc Nam Phan | 2026-07-10T15:30:46.143000 | 1 | - |
| 643 | devchandra/ai-agent-security-v74-yusuke-lb60525-exact | AI Agent Security v74 Yusuke LB60525 exact | Dr Chandrasen Pandey | 2026-07-10T16:07:51.933000 | 1 | - |
| 644 | devchandra/ai-agent-security-v77-shadowcat-stable-margin32 | AI Agent Security v77 Shadowcat stable margin32 | Dr Chandrasen Pandey | 2026-07-10T16:21:07.647000 | 1 | - |
| 645 | ducnamphan/jed-v20-0-gpu-n-500 | JED v20.0 GPU N=500 | Duc Nam Phan | 2026-07-11T07:36:05.517000 | 1 | - |
| 646 | funnyai1234/notebook082499274c | notebook082499274c | QweekOS | 2026-07-12T06:59:13.133000 | 0 | - |
| 647 | kyleslight/ai-agent-security-public-anchor-v1 | AI Agent Security Public Anchor v1 | Kyles Light | 2026-07-12T17:24:05.107000 | 1 | - |
| 648 | commencethescourge/ai-agent-security-baseline-submission | AI Agent Security Baseline Submission | commencethescourge | 2026-07-11T18:51:12.163000 | 0 | - |
| 649 | yuriymikityuk/the-taint-window-trap-jed-sdk-predicate-stacking | The Taint-Window Trap: JED SDK Predicate Stacking | Yuriy Mikityuk | 2026-07-11T23:25:13.377000 | 1 | - |
| 650 | loveautomn/getting-started-notebook-b8f749 | Getting Started Notebook b8f749 | love automn | 2026-07-12T09:49:30.087000 | 1 | - |
| 651 | yuriymikityuk/read-the-source-not-the-leaderboard | Read the source, not the leaderboard | Yuriy Mikityuk | 2026-07-12T16:30:33.413000 | 1 | - |
| 652 | paul720810/hermes-attack-v34-pure-n1050-tight-20260712-200748 | Hermes Attack v34-pure-n1050-tight-20260712-200748 | Paul720810 | 2026-07-12T20:07:52.043000 | 0 | - |
| 653 | andrewmedran0/ai-agent-security-submit | AI Agent Security Submit | Andy | 2026-07-13T02:00:35.057000 | 1 | - |
| 654 | paul720810/hermes-attack-test-comp | Hermes Attack Test Comp | Paul720810 | 2026-07-13T15:16:45.780000 | 0 | - |
| 655 | paul720810/hermes-attack-test-big-code | Hermes Attack Test Big Code | Paul720810 | 2026-07-13T15:17:03.697000 | 0 | - |
| 656 | paul720810/hermes-attack-v36-pure-n1050-tight-fixed | Hermes Attack v36-pure-n1050-tight-fixed | Paul720810 | 2026-07-13T15:17:20.817000 | 0 | - |
| 657 | paul720810/hermes-attack-v36-n1050-tight-20260713-151754 | Hermes Attack v36-n1050-tight-20260713-151754 | Paul720810 | 2026-07-13T15:18:00.110000 | 0 | - |
| 658 | paul720810/hermes-attack-v36-n1050-tight-20260713-151832 | Hermes Attack v36-n1050-tight-20260713-151832 | Paul720810 | 2026-07-13T15:18:35.170000 | 0 | - |
| 659 | paul720810/hermes-attack-v37-n950-reg-20260713-152254 | Hermes Attack v37-n950-reg-20260713-152254 | Paul720810 | 2026-07-13T15:22:58.937000 | 0 | - |
| 660 | shayml/ai-agent-security-latest-best-v2 | AI Agent Security Latest Best V2 | ShayML | 2026-07-14T02:40:01.243000 | 0 | - |
| 661 | shayml/ai-agent-security-latest-best-v3 | AI Agent Security Latest Best V3 | ShayML | 2026-07-14T02:59:34.170000 | 0 | - |
| 662 | kleniopadilha/winnex-v62-attack | WINNEX V62 Attack | Klenio Padilha | 2026-07-14T06:41:36.967000 | 0 | - |
| 663 | kleniopadilha/winnex-v63-attack | WINNEX V63 Attack | Klenio Padilha | 2026-07-14T11:54:51.453000 | 0 | - |
| 664 | kleniopadilha/winnex-v64-attack | WINNEX V64 Attack | Klenio Padilha | 2026-07-14T12:08:11.737000 | 0 | - |
| 665 | kleniopadilha/winnex-v65-attack | WINNEX V65 Attack | Klenio Padilha | 2026-07-14T19:57:08.547000 | 0 | - |
| 666 | paul720810/hermes-attack-v34-dual-post-20260715-063727 | Hermes Attack v34-dual-post-20260715-063727 | Paul720810 | 2026-07-15T06:37:31.573000 | 1 | - |
| 667 | weizhouliu/jed-attack-v2 | jed-attack-v2 | weizhou liu | 2026-07-15T16:15:46.433000 | 0 | - |
| 668 | coolin666/getting-started-notebook | Getting Started Notebook | coolin666 | 2026-07-16T08:23:26.597000 | 2 | - |
| 669 | coolin666/getting-started-notebook-4c3e91 | Getting Started Notebook 4c3e91 | coolin666 | 2026-07-15T16:57:04.837000 | 0 | - |
| 670 | coolin666/getting-started-notebook-2 | Getting Started Notebook 2 | coolin666 | 2026-07-15T16:56:59.210000 | 0 | - |
| 671 | paul720810/hermes-attack-v48-pure-n950-m1p0-20260717-001415 | Hermes Attack v48-pure-n950-m1p0-20260717-001415 | Paul720810 | 2026-07-17T00:14:20.367000 | 0 | - |
| 672 | paul720810/hermes-attack-v54-n950-framing-20260718-002808 | Hermes Attack v54-n950-framing-20260718-002808 | Paul720810 | 2026-07-18T00:28:11.130000 | 0 | - |
| 673 | paul720810/hermes-attack-v60-pure-n1050-m125-20260719-052338 | Hermes Attack v60-pure-n1050-m125-20260719-052338 | Paul720810 | 2026-07-19T05:23:41.477000 | 0 | - |
| 674 | paul720810/hermes-attack-v61-pure-n1050-m115-20260719-052445 | Hermes Attack v61-pure-n1050-m115-20260719-052445 | Paul720810 | 2026-07-19T05:24:47.870000 | 0 | - |
| 675 | paul720810/hermes-attack-v62-replicate-20260719-052601 | Hermes Attack v62-replicate-20260719-052601 | Paul720810 | 2026-07-19T05:26:05.847000 | 0 | - |
| 676 | paul720810/hermes-attack-v64-n1000-s46-m1-2-20260720-004121 | Hermes Attack v64-n1000-S46-M1.2-20260720-004121 | Paul720810 | 2026-07-20T00:41:25.387000 | 0 | - |
| 677 | paul720810/hermes-attack-v65-n1000-s45-m1-25-20260720-004434 | Hermes Attack v65-n1000-S45-M1.25-20260720-004434 | Paul720810 | 2026-07-20T00:44:36.990000 | 0 | - |
| 678 | paul720810/hermes-attack-v66-n1025-s45-m1-2-20260720-004615 | Hermes Attack v66-n1025-S45-M1.2-20260720-004615 | Paul720810 | 2026-07-20T00:46:19.040000 | 0 | - |
| 679 | paul720810/hermes-attack-v67-n975-s45-m1-2-20260720-004714 | Hermes Attack v67-n975-S45-M1.2-20260720-004714 | Paul720810 | 2026-07-20T00:47:18.413000 | 0 | - |
| 680 | dakbsabsa/ai-agent-security-multi-step-tool-attacks | ai-agent-security-multi-step-tool-attacks | I PUTU KRISNA PRAMANA YUDA | 2026-07-20T11:30:56.300000 | 9 | - |
| 681 | ojanapalash/notebook6d94950baf | notebook6d94950baf | OjanaPalash MD. KAMAL UDDIN | 2026-07-20T19:46:52.387000 | 2 | - |
| 682 | paul720810/hermes-attack-v68-tight-20260721-003427 | Hermes Attack v68-tight-20260721-003427 | Paul720810 | 2026-07-21T00:34:32.267000 | 1 | - |
| 683 | prvsiyan/ai-agent-security-defense-in-depth-audit | AI Agent Security / Defense-in-Depth Audit | prvsiyan | 2026-07-21T14:12:19.767000 | 13 | - |
| 684 | enriro0/replay-throughput-and-guardrail-reachability-jed | Replay-Throughput and Guardrail Reachability (JED) | Enrique Rodríguez | 2026-09-04T14:01:01.673000 | 1 | - |
| 685 | seb001010/51-silver-working-note-the-gate-reads-payloads | #51 Silver / Working Note: the gate reads payloads | Sebastian Martin | 2026-09-04T13:20:00.107000 | 1 | - |
| 686 | coolin666/jed-attack-v12 | JED Attack v12 | coolin666 | 2026-08-13T14:11:10.673000 | 44 | - |
| 687 | souldrive/drop-them-a-line-quietly-deletes-a-file | Drop them a line quietly deletes a file | souldrive | 2026-09-02T12:02:35.160000 | 3 | - |
| 688 | addonyas/adiya | adiya | Adiya Orazbek | 2026-08-21T18:36:53.600000 | 3 | - |
| 689 | antoniorotundo2/a-throughput-floor-plus-a-genuine-multi-step-searc | A throughput floor plus a genuine multi-step searc | Antonio Rotundo | 2026-09-04T18:38:30.493000 | 12 | - |
| 690 | ashraf1232/isolating-the-taint-boundary-working-note | Isolating the Taint Boundary -- Working Note | Ashraf 1232 | 2026-09-03T08:10:56.730000 | 0 | - |
| 691 | anvithpothula/aisec-jedcdprobe | aisec-jedcdprobe | Anvith Pothula | 2026-08-29T00:22:31.860000 | 1 | - |
| 692 | sirikilohit/submission-v170-dual-harmony | submission_v170_dual_harmony | rellik13 | 2026-09-01T21:18:58.913000 | 0 | - |
| 693 | zashraf1337hs/msta-working-note | MSTA Working Note | zashraf1337-hs | 2026-09-02T00:27:05.643000 | 0 | - |
| 694 | municef1/105-silver-private-lb-22-155-confused-deputy | #105 Silver: Private LB 22.155 Confused Deputy | 안녕하세요이세입니다잘부탁드립니다 | 2026-09-02T11:11:39.087000 | 4 | TITLE-CLAIMED priv 22.155 Silver105 private-era |
| 695 | gerwynng/ai-agent-security-final-leaderboard-shake | AI Agent Security: Final Leaderboard Shake | Gerwyn | 2026-09-02T07:55:04.873000 | 2 | - |
| 696 | backtracking/jed-silver-public-v43 | jed-silver-public-v43 | Le Trong Hieu | 2026-09-02T04:16:09.030000 | 0 | - |
| 697 | backtracking/jed-silver-private-hedge-v37 | jed-silver-private-hedge-v37 | Le Trong Hieu | 2026-09-02T04:16:11.120000 | 0 | - |
| 698 | backtracking/jed-silver-solution-writeup | jed-silver-solution-writeup | Le Trong Hieu | 2026-09-02T04:26:07.683000 | 0 | - |
| 699 | takamichitoda/the-hedge-that-survived-clean-confused-deputy | The hedge that survived: clean CONFUSED_DEPUTY | Takamichi Toda | 2026-09-02T06:32:28.767000 | 0 | REPORTED 24.36 per INVENTORY |
| 700 | ahmedmobasher86/working-note-guardrail-predicate-asymmetry | Working Note: Guardrail-Predicate Asymmetry | Ahmed Mobasher | 2026-09-02T06:40:02.843000 | 0 | - |
| 701 | merkiraz/jed-v84-deputymax-attack | JED-v84-DeputyMax-attack | ömer kiraz | 2026-09-02T08:44:55.360000 | 0 | - |
| 702 | takamichitoda/the-objective-is-raw-per-second | The objective is raw per second | Takamichi Toda | 2026-09-02T11:54:16.543000 | 5 | - |
| 703 | kkrasikov/workingnote-66th-place-method-harness | [WorkingNote] 66th place - Method & Harness | Kirill Krasikov | 2026-09-03T01:49:33.110000 | 1 | - |
| 704 | abukayyisahbasyid/ai-agent-security-working-note | AI Agent Security - Working Note | Abu Kayyisah Basyid | 2026-09-02T12:55:54.330000 | 2 | - |
| 705 | thwaitsusa2/jed-working-note-verifier | JED Working Note verifier | thwaitsusa2 | 2026-09-02T19:41:34.517000 | 1 | - |

End of table. 705 rows. voteCount/hotness sorts added 0 refs beyond score sort. Scores numeric only where marked VERBATIM/TITLE-CLAIMED, else inferred order.
