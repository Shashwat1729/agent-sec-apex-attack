# -*- coding: utf-8 -*-
import re, json, sys
from pathlib import Path
MD = Path("docs/WORKING_NOTE_V11.md")
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
# tables
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
# max data rows = len(block)-2 (header+sep)
max_table_rows = max((len(b)-2) for _,b in table_blocks) if table_blocks else 0
max_narrative_rows = 0
if m1!=-1 and m2!=-1:
    n_start = text[:m2].count(chr(10))
    c1_line = text[:m1].count(chr(10))
    narrative_blocks = [b for start,b in table_blocks if c1_line <= start < n_start]
    max_narrative_rows = max((len(b)-2) for b in narrative_blocks) if narrative_blocks else 0
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
# TL;DR: find first blockquote starting with > (1) and count sentences until next blank or non-blockquote
tldr_sentences = 0
# Find TL;DR header then first > (1) block
tldr_idx = text.find("## V11 TL;DR")
if tldr_idx != -1:
    # find > (1) after header
    start = text.find("> (1)", tldr_idx)
    if start != -1:
        # find end of this blockquote: next occurrence of "\n\n" then non-">" or "<a"
        # Capture until double newline + non-">" or until next header
        end = text.find("\n\n", start)
        # If next char after \n\n is not ">", block ends
        # Actually TL;DR block is 5 sentences in one blockquote (maybe multiline but each line starts with >)
        # Find consecutive lines starting with >
        block_lines = []
        for l in text[start:].splitlines():
            if l.lstrip().startswith(">"):
                block_lines.append(l)
            elif l.strip() == "":
                continue
            else:
                break
            if len(block_lines) > 20:
                break
        block_text = " ".join([l.lstrip()[1:].strip() for l in block_lines])
        # Count sentences by splitting on . ! ?
        sents = [s.strip() for s in re.split(r"[.!?]+", block_text) if s.strip()]
        # Filter to sentences that contain content (not empty)
        # The TL;DR should be 5 sentences: (1)...(2)...(3)...(4)...(5)...
        # Count by "(n)" markers
        markers = re.findall(r"\(\d\)", block_text)
        if markers:
            tldr_sentences = len(markers)
        else:
            tldr_sentences = len(sents)
print(f"=== check_gates for {MD} ===")
print(f"Lines: {num_lines}  Bytes: {num_bytes}  Words total: {num_words_total}  Slice words: {slice_words}")
print(f"Pipes: {num_pipes}  Figures: {num_figs} (narrative {narr_figs})  Fences: {num_fences}  Max data rows: {max_table_rows} (narr {max_narrative_rows})")
print(f"Registry: {reg_rows}  TL;DR sentences: {tldr_sentences}  Safety violations: {len(violations)}")
checks = []
checks.append(("PASS" if 2500 <= num_lines <= 3500 else "FAIL", f"Total lines {num_lines} | gate 2500-3500"))
checks.append(("PASS" if 200000 <= num_bytes <= 600000 else "FAIL", f"Total bytes {num_bytes} | gate 200k-600k"))
checks.append(("PASS" if 2500 <= slice_words <= 5500 else "FAIL", f"Award-core Sec1-10 words {slice_words} | gate 2500-5500 (guide:38) target 2500-3500 honest 4241 cut 60%"))
checks.append(("PASS" if num_figs >= 11 else "FAIL", f"Total figures {num_figs} | gate >=11"))
checks.append(("PASS" if narr_figs <= 5 else "FAIL", f"Narrative figures (Sec1-10) {narr_figs} | gate <=5"))
checks.append(("PASS" if max_table_rows <= 12 else "FAIL", f"Max table data rows {max_table_rows} | gate <=12"))
checks.append(("PASS" if max_narrative_rows <= 8 else "FAIL", f"Max narrative data rows {max_narrative_rows} | gate <=8"))
checks.append(("PASS" if len(violations)==0 else "FAIL", f"Safety adjacency violations {len(violations)} | gate 0"))
checks.append(("PASS" if reg_rows >= 15 else "FAIL", f"Registry rows {reg_rows} | gate >=15"))
checks.append(("PASS" if nb_alt else "FAIL", f"Numbered notebooks 01-05 exist"))
checks.append(("PASS" if 4 <= tldr_sentences <= 6 else "FAIL", f"TL;DR sentences {tldr_sentences} | gate 4-6"))
checks.append(("PASS" if num_pipes < 800 else "FAIL", f"Pipe lines total {num_pipes} | gate <800 (vs 2445 V10)"))
checks.append(("PASS" if num_fences >= 6 else "FAIL", f"Fences ``` {num_fences} | gate >=6"))
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
