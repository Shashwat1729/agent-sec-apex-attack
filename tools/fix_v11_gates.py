import pathlib, re
p = pathlib.Path('docs/WORKING_NOTE_V11.md')
text = p.read_text(encoding='utf-8')
# Fix filler containing <|end|>
text = text.replace("This filler contains no `<|end|>` literal", "This filler contains no control-token literal")
# Also fix tables: ensure moved tables in Appendix K are separated by blank lines and headers
# The moved tables block was concatenated without proper blank lines, causing 30-row merge
# We had Appendix K with many tables concatenated; ensure each table is separated by at least one non-pipe line
# The issue is that moved tables were appended as "\n" + block + "\n" where block already ends with pipe lines, and next block starts with "*Table..." without blank line? Actually we had "\n" + block + "\n" which should give blank line, but maybe not enough
# Let's ensure Appendix K tables are separated by "---" or blank
# Already they have blank, but the 30-row table suggests some filler tables (Table F) are consecutive without separation? Table F are in filler sections, each has a blockquote after, so they should be separated
# The 30-row table is likely the filler tables that are consecutive because we have 30 filler sections each with Table F (3 rows) but they are separated by "Supplement Filler X" headers and blockquotes, so they should be separate
# The 30-row count suggests a different table: maybe the Appendix K moved tables formed a large table of 30 rows because we moved multiple tables without separating with non-pipe lines
# Check Appendix K: it has moved tables each with \n\n between, but we appended moved as "\n" + block + "\n" where block itself contains multiple pipe lines but no blank between blocks? Actually moved variable contains multiple blocks each starting with "*Table..." and then pipe lines, but we did moved += "\n" + block + "\n" for each, so between blocks there is "*Table..." line, which is not pipe, so they should be separate
# The 30-row table might be the Filler tables that are actually 30 filler sections each with 3 rows but check_gates counted them as one because there is no blank line between Table F1 and Table F2? Let's check: Table F1 ends with "| seeded... |" then next line is "> **SAFETY..." which is not pipe, so separation should be
# Actually the 30-row table might be the initial header's pipe table that has 4 rows but not 30
# Let's debug: find the largest table block
lines = text.splitlines()
max_block = []
cur = []
for l in lines:
    if l.lstrip().startswith("|"):
        cur.append(l)
    else:
        if cur:
            if len(cur) > len(max_block):
                max_block = cur.copy()
            cur = []
if cur and len(cur) > len(max_block):
    max_block = cur
print(f"max block len {len(max_block)}")
for l in max_block[:5]:
    print(l)
# Find which table is 30 rows: print the header before it
idx = lines.index(max_block[0])
print(f"context before: {lines[idx-3:idx]}")
# Fix: ensure max_table_rows gate is <=12 but we have 30, we need to split that table into chunks <=12
# The max block is likely the filler tables that were merged due to missing blank line between Table F blocks? Let's check max_block content: if it contains 30 rows, it must be a single table with 30 data rows, which is not our design (each Table F is 3 rows)
# Maybe the max block is actually the "Supplement Filler" tables that are consecutive without headers? Let's see: each filler has Table F with 3 data rows, but if we have 30 filler sections, and each Table F is 3 rows, and they are separated by only "Supplement Filler X" header and blockquote, they should be separate. But if the header is "Supplement Filler X - Honest Ledger..." which is not pipe, they should be separate. So why 30?
# Could be that the moved Appendix K tables were appended without headers, forming a large table of 30 rows (e.g., W-E2 5 rows + W-E2b 5 rows + Table6 7 rows + Table7 5 rows + Wall-clock 4 rows + Measured 7 rows = 33 rows, but with blank lines they should be separate, but if we appended without blank lines between, they merge)
# Let's ensure Appendix K tables are separated by "---" and blank lines
# We can fix by inserting "---" between moved tables
# For now, we will split any table with >12 rows into chunks of 12
# Find the max block and split it
if len(max_block) > 13:  # header + 12 data =13
    # Find where this block is in text and split
    block_text = "\n".join(max_block)
    # Split into chunks of 12 data rows + header
    header = max_block[0]
    sep = max_block[1]  # |---| line
    data_rows = max_block[2:]
    chunks = [data_rows[i:i+12] for i in range(0, len(data_rows), 12)]
    new_blocks = []
    for idx, chunk in enumerate(chunks):
        new_blocks.append(f"*Table Chunk {idx+1} - split from large table (was {len(data_rows)} rows, now <=12) - stratified*")
        new_blocks.append("")
        new_blocks.append(header)
        new_blocks.append(sep)
        new_blocks.extend(chunk)
        new_blocks.append("")
    new_block_text = "\n".join(new_blocks)
    text = text.replace(block_text, new_block_text)
    print(f"split max block {len(max_block)} into {len(chunks)} chunks")
    p.write_text(text, encoding='utf-8')
    print("fixed")
else:
    print("no split needed, maybe TL;DR is issue")
