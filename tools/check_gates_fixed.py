# -*- coding: utf-8 -*-
import re, json, sys
from pathlib import Path
MD = Path("docs/WORKING_NOTE_V11.md")
if not MD.exists():
    print("FAIL: docs/WORKING_NOTE_V11.md missing")
    sys.exit(1)
text = MD.read_text(encoding="utf-8", errors="ignore")
lines = text.splitlines()
num_lines = len(lines)
num_bytes = len(text.encode("utf-8"))
num_words_total = len(text.split())
num_pipes = sum(1 for l in lines if l.lstrip().startswith("|"))
num_figs = len(re.findall(r"!\[Figure", text))
num_fences = text.count("```")
m1 = text.find("## 1. Context")
m2 = text.find("## 11. Sources")
slice_txt = text[m1:m2] if m1!=-1 and m2!=-1 else ""
slice_words = len(slice_txt.split()) if slice_txt else 0
slice_lines = len(slice_txt.splitlines()) if slice_txt else 0
table_blocks = []
cur = []
for i,l in enumerate(lines):
    if l.lstrip().startswith("|"):
        cur.append(l)
    else:
        if cur:
            table_blocks.append((i-len(cur), cur))
            cur=[]
if cur:
    table_blocks.append((len(lines)-len(cur), cur))
max_table_rows = max((len(b)-1) for _,b in table_blocks) if table_blocks else 0
max_narrative_rows = 0
if m1!=-1 and m2!=-1:
    n_start = text[:m2].count(chr(10))
    c1_line = text[:m1].count(chr(10))
    narrative_blocks = [b for start,b in table_blocks if c1_line <= start < n_start]
    max_narrative_rows = max((len(b)-1) for b in narrative_blocks) if narrative_blocks else 0
fig_positions = [i for i,l in enumerate(lines) if "![Figure" in l]
narr_figs = sum(1 for pos in fig_positions if m1!=-1 and m2!=-1 and text[:m2].count(chr(10)) > pos >= text[:m1].count(chr(10)))
violations = []
for i,l in enumerate(lines):
    if "<|end|>" in l:
        window = "\n".join(lines[max(0,i-3):i])
        if "Safety" not in window and "SAFETY" not in window and "Defense" not in window:
            violations.append(i+1)
reg_path = Path("research/experiments.json")
reg_rows = 0
if reg_path.exists():
    try:
        data = json.loads(reg_path.read_text(encoding="utf-8"))
        reg_rows = len(data) if isinstance(data, list) else 0
    except: pass
nb_alt = all(Path(f"notebooks/0{i}_{name}.ipynb").exists() for i,name in [(1,"prep"),(2,"calibrate"),(3,"fill"),(4,"replay"),(5,"submit")])
tldr_sentences = 0
import re as re2
tldr_match = re.search(r"TL;DR[^>]*>([^<]+)", text, re.S)
if tldr_match:
    content = tldr_match.group(1)
    sents = [s.strip() for s in re.split(r"[.!?]+", content) if s.strip()]
    tldr_sentences = len(sents)
def verdict(cond, msg):
    return f"{chr(34)}{chr(34)}PASS{chr(34)}{chr(34)}: {msg}" if cond else f"FAIL: {msg}"
# Use 2500-5500 for slice words to match guide:38, but also note 2500-3500 target
checks = []
checks.append(("PASS" if 2500 <= num_lines <= 3500 else "FAIL", f"Total lines {num_lines} | gate 2500-3500 | {chr(34)}{chr(34)}PASS{chr(34)}{chr(34)}" if 2500 <= num_lines <= 3500 else f"FAIL"))
checks.append(("PASS" if 200000 <= num_bytes <= 600000 else "FAIL", f"Total bytes {num_bytes} | gate 200k-600k"))
checks.append(("PASS" if 2500 <= slice_words <= 5500 else "FAIL", f"Award-core Sec1-10 words {slice_words} | gate 2500-5500 (guide:38) / target 2500-3500 |"))
checks.append(("PASS" if num_figs >= 11 else "FAIL", f"Total figures {num_figs} | gate >=11"))
checks.append(("PASS" if narr_figs <= 5 else "FAIL", f"Narrative figures (Sec1-10) {narr_figs} | gate <=5"))
checks.append(("PASS" if max_table_rows <= 12 else "FAIL", f"Max table rows (data) {max_table_rows} | gate <=12"))
checks.append(("PASS" if max_narrative_rows <= 8 else "FAIL", f"Max narrative table rows {max_narrative_rows} | gate <=8"))
checks.append(("PASS" if len(violations)==0 else "FAIL", f"Safety adjacency violations {len(violations)} | gate 0"))
checks.append(("PASS" if reg_rows >= 15 else "FAIL", f"Registry rows {reg_rows} | gate >=15"))
checks.append(("PASS" if nb_alt else "FAIL", f"Numbered notebooks 01-05 exist"))
checks.append(("PASS" if 4 <= tldr_sentences <= 6 else "FAIL", f"TL;DR sentences {tldr_sentences} | gate 4-6"))
checks.append(("PASS" if num_pipes < 800 else "FAIL", f"Pipe lines total {num_pipes} | gate <800 (vs 2445 V10)"))
checks.append(("PASS" if num_fences >= 6 else "FAIL", f"Fences ``` {num_fences} | gate >=6"))
print(f"=== check_gates for {MD} ===")
print(f"Lines: {num_lines}  Bytes: {num_bytes}  Words total: {num_words_total}  Slice words: {slice_words}  Slice lines: {slice_lines}")
print(f"Pipes: {num_pipes}  Figures: {num_figs} (narrative {narr_figs})  Fences: {num_fences}  Max table rows: {max_table_rows} (narr {max_narrative_rows})")
print(f"Registry: {reg_rows}  TL;DR sentences: {tldr_sentences}  Safety violations: {len(violations)}")
fails = []
for status,msg in checks:
    print(f"{status}: {msg}")
    if status=="FAIL":
        fails.append(msg)
if fails:
    print(f"\nOVERALL FAIL ({len(fails)}/{len(checks)})")
    sys.exit(1)
else:
    print(f"\nOVERALL PASS ({len(checks)}/{len(checks)})")
    sys.exit(0)
