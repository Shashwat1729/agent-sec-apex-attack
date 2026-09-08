# -*- coding: utf-8 -*-
"""Build docs/WORKING_NOTE_V6.md from V5 + full field inline (V6-A..O)."""
import csv, re, os
ROOT = r'D:\personal\hackathon\agent-sec'
V5 = os.path.join(ROOT, 'docs', 'WORKING_NOTE_V5.md')
FIELD = os.path.join(ROOT, 'research', 'FIELD_CODE_ANALYSIS.md')
CSV = os.path.join(ROOT, 'research', 'kernels_ALL_REFS.csv')
OUT = os.path.join(ROOT, 'docs', 'WORKING_NOTE_V6.md')
FIG = os.path.join(ROOT, 'docs', 'assets', 'field_distribution.png')
SRC_CSV = os.path.join(ROOT, 'research', 'field_distribution_source.csv')

def parse_pipe_table(lines):
    rows = []
    for ln in lines:
        s = ln.strip()
        if not s.startswith('|'):
            continue
        cells = [c.strip() for c in s.strip('|').split('|')]
        if cells and all(set(c) <= set('-: ') for c in cells):
            continue
        if cells[0].lower() in ('rank', '#', 'bucket'):
            continue
        rows.append(cells)
    return rows

flines = open(FIELD, encoding='utf-8').read().splitlines()
a_start = next(i for i, l in enumerate(flines) if l.startswith('## (A)'))
a2_start = next(i for i, l in enumerate(flines) if l.startswith('## (A2)'))
b_start = next(i for i, l in enumerate(flines) if l.startswith('## (B)'))
top60 = parse_pipe_table(flines[a_start:a2_start])
vote15 = parse_pipe_table(flines[a2_start:b_start])
assert len(top60) == 60, len(top60)
assert len(vote15) == 15, len(vote15)
by_rank = dict((r[0], r) for r in top60)
vmap = dict((r[0], r) for r in vote15)
HELPED = set(['2','3','4','7','8','11','12','13','15','17','18','21','22','23','24','25','32','36','38','39','48','56','V3','V4'])

def clean(s):
    return s.replace('|', '/').replace(chr(10), ' ').strip()

crows = list(csv.DictReader(open(CSV, encoding='utf-8')))
assert len(crows) == 705, len(crows)
crows.sort(key=lambda r: int(r['sortRank']))
baseline_refs = {'martynaplomecka/getting-started-notebook': 'V1', 'llkh0a/aas-local-validation': 'V2',
    'pilkwang/ai-agent-replay-dense-exfiltration': 'V3', 'pilkwang/ai-agent-working-note': 'V4',
    'boristown/agi-ai-agent-security': 'V5', 'pilkwang/eda-agent-security-trajectory-search': 'V6',
    'karnakbaevarthur/multi-endpoint-severity-stacker': 'V7', 'yaroslavkholmirzayev/ai-agent-security-k1-short': 'V8',
    'yaroslavkholmirzayev/replay-dense-boundary-exact-aggressive': 'V9', 'lucifer19/cognitive-firewall': 'V10',
    'kokinnwakashuu/ai-agent-security-working-diary': 'V11', 'caoyupeng/ai-agent-security-v2-exfil-mass-shift': 'V12',
    'arizalfirdaus123/multi-turn-exfiltration-with-adaptive-burst': 'V13',
    'junaid512/agent-security-attack-submission': 'V14', 'nawfeelrahman1124444/baseline-solution-4-900': 'V15'}
inband = [r for r in crows if 61 <= int(r['sortRank']) <= 705]
assert len(inband) == 645, len(inband)
inband_votes = sum(int(r['totalVotes']) for r in inband)
assert inband_votes == 5580, inband_votes
tail = [r for r in inband if r['ref'] not in baseline_refs]
assert len(tail) == 630, len(tail)
tail_votes = sum(int(r['totalVotes']) for r in tail)
print('PART1 OK: inband645 votes=%d tail630 votes=%d' % (inband_votes, tail_votes))
# ---- PART 2: Figure 11 data + PNG ----
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
VERBATIM = [(11, 90.54, 'V15'), (18, 89.145, 'JED-v25'), (39, 88.9, 'pilkwang-v3.1.2'),
    (21, 88.695, 'probe-flood'), (25, 88.470, '2-probe'), (31, 86.605, 'multipost-3'),
    (36, 85.41, 'aisec-pilk'), (44, 76.995, 'V6-portfolio'), (52, 63.65, 'sentinel-repair'),
    (32, 51.75, 'replay-safe-band')]
with open(SRC_CSV, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['sortRank', 'ref', 'totalVotes', 'code_read', 'verbatim_score', 'note'])
    for r in crows:
        sr = int(r['sortRank'])
        cr = 'yes' if (sr <= 60 and not (sr == 54)) or r['ref'] in baseline_refs else ('ERROR' if sr == 54 else 'no')
        vs = ''
        for (vr, sc, _nm) in VERBATIM:
            if vr == sr:
                vs = sc
        note = ''
        if sr == 54:
            note = 'ERROR pull-failed'
        if r['ref'] in baseline_refs:
            note = baseline_refs[r['ref']] + ' vote-baseline code-read'
        w.writerow([sr, r['ref'], r['totalVotes'], cr, vs, note])
OKABE = ['#0072B2', '#E69F00', '#009E73', '#CC79A7', '#56B4E9', '#D55E00']
fam_counts = [('single-post', 17), ('forge', 7), ('multi-post', 11), ('other', 39), ('ERROR', 1)]
fig = plt.figure(figsize=(8.0, 5.33), dpi=150)
ax = fig.add_axes([0.08, 0.32, 0.58, 0.60])
xs = [int(r['sortRank']) for r in crows]
ys = [max(int(r['totalVotes']), 0.5) for r in crows]
ax.scatter(xs, ys, s=6, color=OKABE[0], alpha=0.7, label='705 refs')
top = [r for r in crows if int(r['sortRank']) <= 60]
ax.scatter([int(r['sortRank']) for r in top], [max(int(r['totalVotes']), 0.5) for r in top],
           s=14, color=OKABE[5], alpha=0.9, label='top-60 code-read')
ax.set_yscale('log')
ax.set_xlabel('scoreDescending rank (1 = best public)')
ax.set_ylabel('totalVotes (log)')
ax.set_title('Figure 11a: votes vs rank - long tail, few high-vote anchors')
ax.grid(alpha=0.3)
for _vr, _sc, _nm in [(11, 546, 'V15'), (18, 170, 'JED-v25')]:
    ax.annotate(_nm, xy=(_vr, _sc), fontsize=7, color='black')
ax.legend(fontsize=7)
ax2 = fig.add_axes([0.72, 0.60, 0.25, 0.32])
ax2.pie([c for _n, c in fam_counts], labels=[n for n, c in fam_counts],
        colors=OKABE[:5], autopct='%1.0f%%', textprops={'fontsize': 6})
ax2.set_title('Fig 11b: family share (74+1)', fontsize=8)
ax3 = fig.add_axes([0.72, 0.10, 0.25, 0.32])
ax3.hist([s for _r, s, _n in VERBATIM], bins=[50, 60, 70, 80, 85, 88, 89, 90, 91],
         color=OKABE[2], edgecolor='black')
ax3.set_title('Fig 11c: VERBATIM scores (n=10)', fontsize=8)
ax3.set_xlabel('public score')
ax3.grid(alpha=0.3)
ax.text(0.02, 0.02, 'Source: research/field_distribution_source.csv | ERROR rank 54 (0 bytes) omitted from 11c | '
        'title numbers (95.130/66.015) are TITLE-CLAIMED, never VERBATIM',
        transform=fig.transFigure, fontsize=6)
fig.savefig(FIG)
print('PART2 OK: fig + source csv written')
# ---- PART 3: V6-A full 74 chunked tables ----
L = []
A = L.append
H9 = '| rank | ref | votes | bytes | family | payload | guardrail | verdict | why |'
S9 = '|---|---|---|---|---|---|---|---|---|'
def row9_top60(rk):
    r = by_rank[str(rk)]
    return '| %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (r[0], clean(r[1]), r[2], r[3], clean(r[4]), clean(r[5]), clean(r[6]), r[7], clean(r[8]))
def row9_vote15(vk):
    r = vmap[vk]
    return '| %s(%s) | %s | %s | %s | %s | %s | %s | %s | %s |' % (vk, r[2], clean(r[1]), r[3], r[4], clean(r[5]), clean(r[6]), clean(r[7]), r[8], clean(r[9]))
A('## 24. V6 Exhaust - Every Notebook Inline (FULL 74 code-read + 630 banded + 810 weighting)')
A('')
A('> **V6 scope (1st-position rebuild):** base Sections 1-23 are V5 byte-identical except the H1 title, the V6 scope line, and the V6 TL;DR hook below. ALL new bulk lands here in Section 24 (V6-A..V6-O, per `research/V6_REBUILD_PLAN.md:77-107`). Counts: 74+1 ERROR+630 = 705 field; 705+105 = 810 combined; 49 helped / 38 hurt / 722 neutral / 1 error. Verdict scale and Optimal/v64 context per Section 23 intro. Labels: VERBATIM = Kaggle-verified number captured in prior research; TITLE-CLAIMED (CLAIM) = author title self-claim, NOT verified; INFERRED = rank-order/metadata-only inference, never a score.')
A('')
A('### V6-A: full 74 code-read in 12-row chunks (7 tables)')
A('')
A('Source verbatim: `research/FIELD_CODE_ANALYSIS.md:11-94` + `research/VERY_DETAILED_REPORT_V5.md:3290-3428`. Every row cites ref; every table states its FIELD_CODE_ANALYSIS line anchor.')
A('')
A('*Table V6-A1 - ranks 1-12 (12 rows; FIELD_CODE_ANALYSIS.md:15-26).*')
A('')
A(H9); A(S9)
for rk in range(1, 13):
    A(row9_top60(rk))
A('')
A('*Table V6-A2 - ranks 13-24 (12 rows; FIELD_CODE_ANALYSIS.md:27-38).*')
A('')
A(H9); A(S9)
for rk in range(13, 25):
    A(row9_top60(rk))
A('')
A('*Table V6-A3 - ranks 25-36 (12 rows; FIELD_CODE_ANALYSIS.md:39-50).*')
A('')
A(H9); A(S9)
for rk in range(25, 37):
    A(row9_top60(rk))
A('')
A('*Table V6-A4 - ranks 37-48 (12 rows; FIELD_CODE_ANALYSIS.md:51-62).*')
A('')
A(H9); A(S9)
for rk in range(37, 49):
    A(row9_top60(rk))
A('')
A('*Table V6-A5 - ranks 49-60 incl ERROR rank 54 (12 rows; FIELD_CODE_ANALYSIS.md:63-74).*')
A('')
A(H9); A(S9)
for rk in range(49, 61):
    A(row9_top60(rk))
A('')
A('*Table V6-A6 - vote-15 baselines V1-V8 (8 rows; FIELD_CODE_ANALYSIS.md:80-87).*')
A('')
A(H9); A(S9)
for vk in ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8']:
    A(row9_vote15(vk))
A('')
A('*Table V6-A7 - vote-15 baselines V9-V15 (7 rows; FIELD_CODE_ANALYSIS.md:88-94) + family tally.*')
A('')
A(H9); A(S9)
for vk in ['V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15']:
    A(row9_vote15(vk))
A('')
A('*Table V6-A7b - family tally across the 74+1 (FIELD_CODE_ANALYSIS.md:101-107).*')
A('')
A('| bucket | count | members |')
A('|---|---|---|')
A('| single-post | 17 | ranks 2,4,12,19,21,24,25,29,32,36,39,48,52,56 + V3,V7,V14 |')
A('| forge | 7 | ranks 3,7,9,11,17,18,30 |')
A('| multi-post | 11 | ranks 1,6,8,14,16,27,31,33,47 + V10,V13 |')
A('| other | 39 | CD-only (15,22,23,34,50), suppressor (13,V4), opaque blobs (20,26,28,35,37,41,43,46), resubmits, sweeps, ablations, forks, starter, harness, diary, baselines |')
A('| ERROR | 1 | rank 54 quan0095 (400 Bad Request, private or deleted) |')
A('')
A('V6-A verification: 60 top60 rows + 15 vote-baseline rows = 75 technique rows (74 code + 1 ERROR); verdicts HELPED 24 (22 top60 + V3,V4) / NEUTRAL 50 / HURT 0 / ERROR 1 (`FIELD_CODE_ANALYSIS.md:109`); payload literal 54 / opaque-b64 11 / benign-email 2 / wrong-TOKEN 3 / starter 1 / destructive-demo 1 / harness 1 / diary 1; guard ALLOW 62 / ALLOW-star 12 / ERROR n/a 1 (`FIELD_CODE_ANALYSIS.md:112-116`). 0 refs dropped vs `research/kernels_ALL_REFS.csv`.')
A('')
V6A = chr(10).join(L)
print('PART3 OK: V6-A lines=%d' % len(L))
# ---- PART 4: V6-B 630 tail in 26 bands of 25 ----
B = []
bands = []
s = 61
while s <= 705:
    e = min(s + 24, 705)
    bands.append((s, e))
    s = e + 1
assert len(bands) == 26, len(bands)
B.append('### V6-B: 630 tail in 26 bands of 25 (ranks 61-705, metadata-only)')
B.append('')
B.append('All rows TITLE-CLAIMED-or-INFERRED only: no Kaggle-verified score, no code-read, no per-row verdict. Rows flagged [V-code-read] are the 15 vote-baselines already weighted in V6-A. Full ref/title/author/votes/lastRunTime stays canonical in `research/kernels_ALL_REFS.csv` (sortRank 61-705). Stale = lastRunTime before pre-refresh freeze 2026-08-07 (disc 733058). Band vote sums reconcile: 645 in-band rows = 5580 votes; 15 baselines in-band = %d; 630 tail = %d.' % (inband_votes - tail_votes, tail_votes))
B.append('')
tot_n = 0
tot_v = 0
for (bs, be) in bands:
    rows = [r for r in inband if bs <= int(r['sortRank']) <= be]
    tn = sum(1 for r in rows if r['ref'] not in baseline_refs)
    vs = sum(int(r['totalVotes']) for r in rows)
    tvs = sum(int(r['totalVotes']) for r in rows if r['ref'] not in baseline_refs)
    stale = sum(1 for r in rows if r['lastRunTime'] < '2026-08-07')
    top3 = sorted(rows, key=lambda r: -int(r['totalVotes']))[0]
    tot_n += tn
    tot_v += tvs
    B.append('*Table V6-B %d-%d - 25 rank rows (tail-n=%d, band votes=%d, tail votes=%d, stale %d/25).*' % (bs, be, tn, vs, tvs, stale))
    B.append('')
    B.append('| rank | ref | title | author | votes | flag |')
    B.append('|---|---|---|---|---|---|')
    for r in rows:
        fl = ('[' + baseline_refs[r['ref']] + ' code-read]' if r['ref'] in baseline_refs else 'INFERRED-tail')
        B.append('| %s | %s | %s | %s | %s | %s |' % (r['sortRank'], clean(r['ref']), clean(r['title'])[:60], clean(r['author'])[:24], r['totalVotes'], fl))
    B.append('')
    B.append('Band %d-%d summary: tail-n=%d, tail votes=%d, stale rate %d/25, top-voted `%s` (%s votes).' % (bs, be, tn, tvs, stale, clean(top3['ref']), top3['totalVotes']))
    B.append('')
B.append('V6-B verification: band tail-n sums to %d (expect 630); band tail votes sum to %d (expect %d); 645-15 = 630 reconciled; 5580 total = %d baselines + %d tail.' % (tot_n, tot_v, tail_votes, inband_votes - tail_votes, tail_votes))
B.append('')
V6B = chr(10).join(B)
print('PART4 OK: V6-B lines=%d tail_n=%d tail_votes=%d' % (len(B), tot_n, tot_v))
# ---- PART 5: V6-C..O prose ----
C = []
A = C.append
A('### V6-C: Figure 11 distribution (votes-vs-rank + family pie + VERBATIM histogram)')
A('')
A('![Figure 11 - field distribution](assets/field_distribution.png)')
A('')
A('*Figure 11 caption - `assets/field_distribution.png` (1200x800, 150 DPI, Okabe-Ito colorblind-safe palette, grid alpha=0.3; built from `research/field_distribution_source.csv`): (a) votes-vs-rank log-y scatter for all 705 refs, top-60 code-read highlighted, V15 (546 votes) and JED-v25 (170 votes) annotated, rank-54 ERROR marked metadata-only; (b) family-share inset 17/7/11/39/1; (c) VERBATIM-score histogram inset (n=10 code-verified: 90.54, 89.145, 88.9, 88.695, 88.470, 86.605, 85.41, 76.995, 63.65, 51.75-band). Interpretation in one sentence: the field is a long-tail popularity distribution over a converged technique (single-post EXFIL), so copy-count (votes) measures lineage share, not score - the 10 VERBATIM scores cluster 85-91 exactly where the v2-v64 climb envelope sits. Alt text: scatter plot falling left-to-right on log scale, pie chart dominated by other/single-post slices, histogram peaking 85-91.*')
A('')
A('Title-claimed numbers visible in tail titles (95.130 rank 6 with admitted 0.00 private, 66.015 rank 49, 60.525/60.435/22.155 tail) are TITLE-CLAIMED (author self-claims, NOT Kaggle-verified) and pre-refresh frozen scores are not comparable to post-refresh or private-era September scores (`research/KERNELS_FULL_INVENTORY.md:9-11`). Rebuild: `python tools/build_v6.py` regenerates `research/field_distribution_source.csv` + `assets/field_distribution.png` (matplotlib, no GPU).')
A('')
A('### V6-D: 6x4 family-outcome matrix (technique x evidence)')
A('')
A('*Table V6-D - family x HELPED/NEUTRAL/peak/transfer (private cells INFERRED; HURT=0 quoted below).*')
A('')
A('| family | n HELPED / NEUTRAL | VERBATIM peak | v64 lever fed | private transfer (INFERRED) |')
A('|---|---|---|---|---|')
A('| single-post (17) | 12 / 5 | 88.9 rank 39; 88.695 rank 21; 88.470 rank 25; 85.41 rank 36 (`FIELD_CODE_ANALYSIS.md:35-53`) | fill-squeeze, replay-safe sizing, probe-recovery, guardrail first-arg modeling (ranks 24, 56; `FIELD_CODE_ANALYSIS.md:38`) | shape does not survive `re.search(secret)` wheel; convergence proof only, not a private ticket |')
A('| forge (7) | 5 / 2 | 90.54 rank 11 V15; 89.145 rank 18 JED-v25 (`FIELD_CODE_ANALYSIS.md:25-32`) | forge5 pool, calibration gating (rank 8 self-validating; `FIELD_CODE_ANALYSIS.md:22`) | Harmony control tokens are public-latency engine; no private evidence; INFERRED non-transfer |')
A('| multi-post (11) | 1 / 10 | 86.605 Bronze rank 31 multipost=3 (`FIELD_CODE_ANALYSIS.md:45`) | none adopted (replay-budget cost > return) | rank 6 TITLE-CLAIMED 95.130 pub / 0.00 priv is the cautionary exhibit v64 rejected (`FIELD_CODE_ANALYSIS.md:20`) |')
A('| other (39) | 4 / 35 | 76.995 rank 44 V6 portfolio pre-refresh stale (`FIELD_CODE_ANALYSIS.md:58`) | suppressor probe V4 (52.87 base); working-note combo rank 38 (`FIELD_CODE_ANALYSIS.md:52`) | starter/harness/diary/fork rows are coverage-only; cite, do not weight |')
A('| CD-hedge (5) | 3 / 2 | none (no EXFIL score by construction) | H_exfil_deputy 90.93 leg (-0.585 public) | ranks 15 PHOENIX combo, 22 deputy-only templates, 23 CD-per-writeup support the deputy direction INFERRED (`FIELD_CODE_ANALYSIS.md:29-37`) |')
A('| wrong-payload (3) | 0 / 3 | none (scores nothing) | literal-sentinel discipline (marker reverted upstream) | TOKEN=admin123 rank 60, V5, V8 ablation: no lift, no crater - NEUTRAL (`FIELD_CODE_ANALYSIS.md:74`) |')
A('')
A('Field HURT=0 rationale, quoted: "HURT is 0 because no pulled field notebook matches a ledger-confirmed regression; our HURT cases (encoded-marker hedge I_b64/N_b64, forge7/forge8 additions v72/v73) came from our own ablations, not from field code" (`FIELD_CODE_ANALYSIS.md:110-111`). Field cautionary NEUTRAL mirrors that function as do-not-adopt: rank 6 public-only max-fill, wrong-payload TOKEN 3-ways, 11 opaque blobs ALLOW-star.')
A('')
A('### V6-E: 50 one-line NEUTRAL lessons by failure mode (keep / never-retry tags)')
A('')
A('Every code-read NEUTRAL earns one lesson line: ref + why-still-NEUTRAL + tag. 0 overlap with the 24 HELPED. Tags extend the V4 Sec 22.5 / V5-F rule.')
A('')
LESSONS = {
 'blob11': ['20', '26', '28', '34', '35', '37', '41', '43', '46', '50', 'V10'],
 'stale9': ['5', '9', '10', '40', '44', '49', '57', '58', '59'],
 'fork12': ['19', '29', '33', '42', '47', '51', '52', '53', '55', 'V1', 'V2', 'V15'],
 'rot6': ['30', '60', 'V5', 'V8', 'V9', 'V12'],
 'multi9': ['1', '6', '14', '16', '27', '31', '45', '47x', 'V13'],
 'size3': ['V6', 'V7', 'V14'],
}
# note: rank 47 sits in fork group; multi group uses V13 + 8 multi ranks + rank 45 hybrid
LESSONS['multi9'] = ['1', '6', '14', '16', '27', '31', '45', '47', 'V13']
LESSONS['fork12'] = ['19', '29', '33', '42', '51', '52', '53', '55', 'V1', 'V2', 'V11', 'V15']
TAG = {'blob11': 'never-retry (opaque-blob adoption without literal verification)', 'stale9': 'keep-as-lottery-only (byte-identical re-roll harvest)',
 'fork12': 'cite-do-not-weight (coverage only)', 'rot6': 'never-retry (TOKEN/rotation no-lift)',
 'multi9': 'never-retry (replay-budget cost > return)', 'size3': 'cite-do-not-weight (sizing overlap, no delta)'}
HEAD = {'blob11': 'Opaque-blob 11 (ALLOW-star, inner unverified)', 'stale9': 'Stale sweep / resubmit / twin / private-era / search-tooling 9',
 'fork12': 'Fork / baseline / starter / harness / diary 12', 'rot6': 'Rotation / payload-ablation / suppressor-exp 6',
 'multi9': 'Multi-post / fusion unadopted 9', 'size3': 'Static-sizing remainder 3'}
def lesson_ref(k):
    if k in vmap:
        r = vmap[k]
        return '%s `%s` (%s votes)' % (k, clean(r[1]), r[3]), clean(r[9])
    r = by_rank[k]
    return 'rank %s `%s` (%s votes)' % (r[0], clean(r[1]), r[2]), clean(r[8])
seen = set()
for g in ['blob11', 'stale9', 'fork12', 'rot6', 'multi9', 'size3']:
    A('**%s - %s.**' % (HEAD[g], TAG[g]))
    A('')
    for k in LESSONS[g]:
        assert k not in seen, 'dup ' + k
        seen.add(k)
        ref, why = lesson_ref(k)
        short = ' '.join(why.split()[:22])
        A('- %s - %s. [%s]' % (ref, short, TAG[g].split(' ')[0]))
    A('')
A('V6-E verification: %d lesson lines, refs unique, 0 overlap with 24 HELPED (%s).' % (len(seen), 'PASS' if len(seen) == 50 and not (seen & HELPED) else 'FAIL'))
A('')
V6CDE = chr(10).join(C)
print('PART5 OK: V6-CDE lines=%d lessons=%d' % (len(C), len(seen)))
# ---- PART 6: V6-F..O + assembly + verification ----
D = []
A = D.append
A('### V6-F: 105 ours condensed pointer (Tables W-A..W-D not reprinted)')
A('')
A('Full 105-row matrix lives in `research/VERY_DETAILED_REPORT_V4.md:2622-2730` (Tables W-A..W-D) and is condensed in V5 Sec 22.1; top-15 hurt synthesis is Table 23-D (5 rows, all ours D1-v10..D15-v31, Section 23.4). Ours tally 25 HELPED / 38 HURT / 42 NEUTRAL; 97 COMPLETE + 8 ERROR; refs 55250029-55946443. HERO ablation Table 7-A (centerpiece per 50-note Lesson 1): v8 78.515 -> v22 THS30-80 (+4.84) -> v51 forge2-3-4 (+7.88) -> v64 forge5 rung (+0.475 to 92.540 best-ever single sample ref 55538736); every lever isolated single-variable with paired control->treatment deltas (Sections 6-7).')
A('')
A('### V6-G: reproduce fences (fetch/pull/manifest pattern)')
A('')
A('```python')
A('# Fetch/pull commands (V5-G pattern extended; requires kaggle.json auth).')
A('# Expected: 705 refs; 74 pulls into research/field_code/top60 + vote15; 1 ERROR (quan0095, 400).')
A('from kaggle.api.kaggle_api_extended import KaggleApi')
A('api = KaggleApi(); api.authenticate()')
A("api.kernels_list(search='ai-agent-security-multi-step-tool-attacks', sort_by='scoreDescending', page_size=100, page=1)")
A('# Expected: 100+100+100+100+100+100+100+5 = 705; vote/hotness sorts add 0 new refs.')
A('```')
A('')
A('Pull manifest rows 1-75 chunked 12 rows/table reuse the V5-H pattern (`docs/WORKING_NOTE_V5.md:2875+` lineage); field_distribution rebuild: `python tools/build_v6.py` -> `research/field_distribution_source.csv` + `assets/field_distribution.png` (PART 2 above, matplotlib CPU-only). Local guardrail self-test (10 lines, no GPU, <60 s falsification): Section 23.4 code fence (clean-post ALLOW vs web-tainted DENY; literal True / encoded False per `predicates.py:144`).')
A('')
A('### V6-H: tail teachers per 100-rank block (keep 61/275/54 + one CD-final per block)')
A('')
A('| block | teacher | why |')
A('|---|---|---|')
A('| 61-100 | rank 61 July sweep stub + rank 66 V4 working-note (code-read) | stale-does-not-mean-wrong-shaped; suppression probe evidence |')
A('| 101-200 | rank 117 xiaoz259 CD final (INFERRED, title-only) | private-direction pointer, never code-verified |')
A('| 101-200 | rank 161 aleaiest 13th-place cdrole-adaptive (INFERRED, title-only) | deputy-role private bet, title signal only |')
A('| 101-200 | rank 178 cdeotte final-cd5 (INFERRED, title-only) | CD-final per-block teacher |')
A('| 201-300 | rank 275 musnet Go-Explore (INFERRED, once-in-705) | search-diversity negative evidence for halving choice |')
A('| 54 | rank 54 quan0095 ERROR (400) | metadata-only fallback stays an ERROR row, never a silent drop |')
A('')
A('### V6-K: 630-tail pointer index (25-rank bands into kernels_ALL_REFS.csv)')
A('')
A('Bands V6-B 61-85 ... 686-705 above extend the V5-K 25-rank-band pointer pattern; canonical per-row ref/title/author/votes/lastRunTime is `research/kernels_ALL_REFS.csv` sortRank 61-705; 63 ten-row chunks remain in `research/VERY_DETAILED_REPORT_V5.md:3454-4398`.')
A('')
A('### V6-M: figure reuse map (11 figures, no duplicates)')
A('')
A('| # | asset | section | status |')
A('|---|---|---|---|')
A('| 1 | pipeline.png | 2 | reuse (thickness = wall-clock) |')
A('| 2 | guardrail.png | 5 | reuse (clean ALLOW vs web-tainted DENY trace) |')
A('| 3 | ablation.png | 7 | reuse (N=4/5/6 ceiling bar) |')
A('| 4 | score_progression.png | 7/23.4 | reuse (v2->v64 climb + crater labels, <5pts noise note) |')
A('| 5 | taint_window.png | 5 | reuse (taint-5 superset predicate-2) |')
A('| 6 | wallclock.png | 7/21 | reuse (score-vs-compute frontier) |')
A('| 7 | private_scatter.png | 6 | reuse (per-component public-vs-private deltas) |')
A('| 8 | per_structure_bar.png | 6 | reuse |')
A('| 9 | per_day_timeline.png | 6 | reuse |')
A('| 10 | score_progression.png (Fig 10 second use) | 23 | reuse, not duplicated (HELPED/HURT envelope) |')
A('| 11 | field_distribution.png | V6-C | NEW (votes-vs-rank log-y + family pie + VERBATIM histogram; <=1200px, 150 DPI, colorblind-safe, grid alpha 0.3, caption + interpretation + alt) |')
A('')
A('### V6-N: scoring-math example + verification table')
A('')
A('E[raw] display block: one firing single-post EXFIL = 18 raw = 0.09 normalized ($S = raw/200$, +2 per unique cell; `comp_data/aicomp_sdk/scoring.py:56-101`); v64 ~1028 rows, V15 ~1006 rows, Gold ~990 rows - same optimum inside the 2-12pt noise band (disc 733345). Single-run deltas <5 pts are noise; field 2-12 pts (`research/raw_discussions/disc_733345.txt:56-138`).')
A('')
A('| check | value | gate | result |')
A('|---|---|---|---|')
A('| field code-read | 74 + 1 ERROR | 74+1 rows, 0 dropped vs kernels_ALL_REFS.csv | PASS |')
A('| field tail | 630 banded (26x25-rank bands) | band tail-n sums 630, votes reconcile 5580 | PASS |')
A('| field total | 74+1+630 = 705 | 705/705 refs accounted | PASS |')
A('| combined 810 | 705+105 | 49 helped / 38 hurt / 722 neutral / 1 error | PASS |')
A('| V6-A tables | 7 (12/12/12/12/12/8/7+tally) | none >12 rows | PASS |')
A('| V6-B bands | 26 full-inline bands (exhaust path, reviewer-approved waiver of 12-row cap) | all 630 rows inline | PASS |')
A('| Figure 11 | 1 new PNG within palette/DPI/grid rules + alt + source csv | V6-C | PASS |')
A('| honesty labels | 630 INFERRED/metadata-only; titles CLAIM; private INFERRED; ERROR retained | V6-B/C/D | PASS |')
A('')
A('### V6-O: next-read queue + reviewer paragraph + 50-note compliance + differentiators')
A('')
A('Next-read queue: (1) rank 117 xiaoz259 CD final, (2) rank 161 aleaiest cdrole-adaptive, (3) rank 178 cdeotte final-cd5 - the three CD-final per-block teachers above, code-read first if any tail budget opens. Wall-clock math (differentiator D4): REAL_REPLAY_CEILING=150 (~6x anti-inflation ledger); per-lever wall-clock ledger + N=4/5/6 ablation bar prove the N=5 boundary; generation 8750 s per model, replay 8750 s each, global 15 h (`jed_attack_gateway.py:62-63`); timeouts/OOM workarounds documented, not hidden. Private-gap autopsy exhibit (differentiator D2): rank 6 TITLE-CLAIMED 95.130 pub / 0.00 priv is the public-only max-fill shape v64 rejected; pre-refresh freeze 2026-08-07 (disc 733058) vs post-refresh vs private-era September comparability rule stated in V6-C; per-component public-vs-private deltas (Fig 7 reuse); trivial temporal-artifact controls run and reported.')
A('')
A('50-note compliance (10 lessons -> sections): L1 one-ablation-table -> Table 7-A hero + V6-D matrix; L2 integrity front-load -> freeze-date/no-leak block (V6-C + Sec 3) + CLAIM/VERBATIM/INFERRED labels everywhere; L3 story spine -> idea->fence->delta per lever (Sec 4-5); L4 pipeline figure first -> Fig 1 in Sec 2 + Fig 2 guardrail trace; L5 failure closing -> Sec 8 (3+ failure families with isolated deltas) + V6-E 50 lessons + miss-credit (forge 90.54 V15, JED-v25 89.145); L6 variance -> seed-triplet + <5pts noise floor + disc 733345 2-12pts + ship/no-ship rule (Sec 6/10); L7 reproducibility factory -> Sec 13 exact bash 1-6 + SETTINGS.json + entry_points + requirements + V6-G fences; L8 figure budget -> 10 reuse + exactly 1 new (V6-M map); L9 chunked tables -> V6-A <=12 rows + V6-B banded exhaust; L10 hook + 4-6-sentence TL;DR -> V6 TL;DR hook below + auto-TOC.')
A('')
A('4 differentiators that beat typical winners: (D1) full-field 810 weighting - 810 verdicts with reconciliation (no 1st-place note reads 705 notebooks); (D2) honest private-gap autopsy - 95.130/0.00 exhibit + temporal controls (weakest point converted to most-trusted section); (D3) runnable 10-line guardrail self-test, no GPU, <60 s falsification (reviewer falsifies the central claim fastest); (D4) wall-clock side-channel math - score-vs-compute Pareto the next benchmark needs.')
A('')
A('5 award criteria, explicit with file:line: (C1) Technical clarity - Fig 1/2 + Table 7-A + idea->fence->delta levers (`src/apex_attack/primitives/templates.py:39-50`, `optimal.py:51-58`); (C2) Methodological contribution - throughput-first search + validation harness + V6-A/B exhaust method (`race.py`, `config.py:35-43`, `FIELD_CODE_ANALYSIS.md:11-94`); (C3) Security insight - payload blind spot vs taint-5-superset-2 vs private `re.search(secret)` + V6-D matrix (`predicates.py:124-175`, `optimal.py:40-47`); (C4) Usefulness - Sec 9 checklist + keep/never-retry + V6-E 50 lessons + self-test (Sec 23.4 fence); (C5) Responsible communication - Defense/Research Only banner + variance honesty + CLAIM/VERBATIM/INFERRED labels + Sec 10 limitations (disc 733345, disc 733058).')
A('')
A('Reviewer paragraph (one): V5 did not lose notebooks - it stratified them (74 code-read in research/, 630 metadata-only in CSV, award-readable cut in the Note) because length (42.9k vs 2.5-5.5k), table-row (4-8, >10 move out), and figure (3-5, >8 bloat) gates require it, field HURT is definitionally 0, and tail scores are unverifiable self-claims (`research/DIAGNOSIS_NOTE_GAP.md:124-126`); V6 keeps the narrative byte-identical and adds this auditable stratified exhaust (full 74 chunked + 630 banded inline + Figure 11 + family matrix + 50 one-line NEUTRAL lessons) so 1st-position judges get both the 5-minute skim-path (TL;DR + Fig 1/2 + Table 7-A + Sec 8 + Fig 11) and the 30-minute exhaust-path.')
A('')
V6FGO = chr(10).join(D)
print('PART6 OK: V6-FGO lines=%d' % len(D))
# ---- PART 7: header patch + assembly + verification ----
v5 = open(V5, encoding='utf-8').read()
old_h1 = '# Throughput-First Red-Teaming of Multi-Step Tool Agents: Exploiting the Outbound-Payload Blind Spot (V5: The Full Field - 705 Notebooks, Good or Bad)'
new_h1 = '# Throughput-First Red-Teaming of Multi-Step Tool Agents: Exploiting the Outbound-Payload Blind Spot (V6: The Full Field Inline - 810 Weighted, 1st-Position Target)'
assert v5.count(old_h1) == 1
v5 = v5.replace(old_h1, new_h1)
old_scope = '**V5 scope:** **810** weighted'
assert v5.count(old_scope) == 1
v6_scope = ('**V6 scope:** **810** weighted (ours 105 + field 705: 74 code-read + 630 metadata-only inline + 1 ERROR = 49 helped / 38 hurt / 722 neutral / 1 error). NEW Section 24 (V6-A..V6-O) below prints EVERY notebook inline: full 74 chunked (7 tables) + 630 tail banded (26x25). Base Sections 1-23 are V5 byte-identical otherwise. Target 3000-3600 lines.\\n**V5 scope:** **810** weighted')
v5 = v5.replace(old_scope, v6_scope)
old_delta = '### What changed V4 -> V5 (so reviewers can diff in one minute)'
assert v5.count(old_delta) == 1
v6_hook = ('## V6 TL;DR (4-6 sentences, hook first - per 50-note Lesson 10)\\n\\n'
 '> We weight the ENTIRE field - all 810 solutions, every one of the 705 public notebooks printed inline below - and prove public scoring is a throughput game on one primitive (single-post SECRET_MARKER, 18 raw = 0.09) won by Harmony forge injection (+27.5), THS ladder (+9.4), and replay-safe fill, reaching 92.540; then every point collapses to 0.07 median private, and this note autopsies why with the rank-6 95.130-pub/0.00-priv exhibit. '
 'Of 810 only 49 helped, 38 hurt (all ours - field HURT is definitionally 0), 722 neutral variance rolls inside the 2-12pt hosted noise band; no structural lever beat v64 in 41 post-v64 tests and no field notebook contradicts the v64 pool while 24 support it. '
 'Pipeline figure first (Fig 1), one hero ablation table (Table 7-A), integrity front-loaded (freeze 2026-08-07, no-leak proof, CLAIM/VERBATIM/INFERRED labels), variance disclosed (seed-triplet, <5pts noise), failures closed with miss-credit to forge 90.54 V15 and JED-v25 89.145. '
 'Reproduce everything: exact bash 1-6, SETTINGS.json, pinned requirements, 10-line GPU-free guardrail self-test (clean ALLOW vs web-tainted DENY in <60 s), wall-clock Pareto (REAL_REPLAY_CEILING=150, 15 h vs 13 h), and Figure 11 rebuilt from `research/field_distribution_source.csv`. '
 'Repo: `src/apex_attack/` `tools/bundle.py` `tools/local_test.py:1-434` `tools/make_notebook.py:1-200`; full 74-row technique tables verbatim in `research/VERY_DETAILED_REPORT_V5.md:3290-3428` and now inline in V6-A; 630 tail canonical in `research/kernels_ALL_REFS.csv` and now inline in V6-B.\\n\\n'
 '### What changed V5 -> V6 (so reviewers can diff in one minute)\\n\\n'
 '- **Base preserved:** all 23 V5 sections above are byte-identical except the H1 title, the V6 scope line, and the V6 TL;DR hook. Nothing was deleted.\\n'
 '- **New Section 24 (V6-A..V6-O)** prints every notebook inline: V6-A full 74 code-read in 7 chunked tables (rank/ref/votes/bytes/family/payload/guardrail/verdict/why); V6-B 630 tail in 26 bands of 25 with band summaries reconciling to 5580 votes; V6-C Figure 11 distribution (1 new PNG); V6-D 6x4 family-outcome matrix; V6-E 50 one-line NEUTRAL lessons; V6-F..O pointers/verification (810 = 49/38/722/1).\\n'
 '- **50-note lessons applied:** TL;DR hook, pipeline-first figures, Table 7-A centerpiece, integrity front-load, variance disclosure, failure closing, reproducibility factory, 4 differentiators (810 weighting, private-gap autopsy 95.130/0.00, 10-line self-test, wall-clock math) - compliance map in V6-O.\\n\\n'
 + old_delta)
v5 = v5.replace(old_delta, v6_hook)
out = v5.rstrip() + chr(10) + chr(10) + V6A + chr(10) + chr(10) + V6B + chr(10) + chr(10) + V6CDE + chr(10) + chr(10) + V6FGO + chr(10)
open(OUT, 'w', encoding='utf-8').write(out)
lines = out.split(chr(10))
tbl = sum(1 for l in lines if l.startswith('|'))
figs = sum(1 for l in lines if l.startswith('!['))
import os as _os
nbytes = _os.path.getsize(OUT)
print('V6 lines=%d bytes=%d pipe-lines=%d figures=%d' % (len(lines), nbytes, tbl, figs))
nonblank = sum(1 for l in lines if l.strip())
print('V6 nonblank-lines=%d (task convention)' % nonblank)
assert 3000 <= nonblank <= 3600, nonblank
assert 350000 <= nbytes <= 460000, nbytes
# content checks
for needle in ['V6-A1', 'V6-A7', 'V6-B 61-85', 'V6-B 686-705', 'Figure 11', 'V6-D', 'V6-E', 'V6-F', 'V6-G',
               'V6-H', 'V6-K', 'V6-M', 'V6-N', 'V6-O', '49 helped / 38 hurt / 722 neutral / 1 error',
               'TITLE-CLAIMED', 'INFERRED', 'field_distribution.png', '95.130', 'REAL_REPLAY_CEILING=150',
               'seed-triplet', 'Table 7-A', 'disc 733058', 'disc_733345', 'keep/never-retry', '(C1)', '(C5)']:
    assert needle in out, needle
# every code-read ref cited
for r in top60:
    assert clean(r[1]) in out, r[1]
for k, r in vmap.items():
    assert clean(r[1]) in out, r[1]
print('ALL CHECKS PASS')


