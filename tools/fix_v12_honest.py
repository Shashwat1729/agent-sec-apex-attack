import pathlib, re, subprocess, sys
p = pathlib.Path('docs/WORKING_NOTE_V12.md')
t = p.read_text(encoding='utf-8')
# Honest numbers from check_gates for V11 (2968 lines etc.) - we will update Appendix N to match actual
# The Appendix N previously claimed 2850/3100 etc., we update to 2968/4508 etc.
replacements = [
    (r'Total lines.*?2850', 'Total lines 2968'),
    (r'Total bytes.*?320000', 'Total bytes 323520'),
    (r'Award-core words.*?3100', 'Award-core Sec1-10 words 4508'),
    (r'Total figures.*?11', 'Total figures 12'),
    (r'Pipe lines.*?450', 'Pipe lines 335'),
]
for pat, repl in replacements:
    t = re.sub(pat, repl, t)
# Ensure hero Table 6-A is first in Section 6 - if not, we note but not fix automatically
# Just ensure safety box is line-adjacent - already is
p.write_text(t, encoding='utf-8')
print('fixed Appendix N honest numbers')
# verify
print('lines', len(t.splitlines()))
