"""Escape '|' inside \\unsure{...} in the table rows of the changes file (GFM tables split cells on '|'),
and repair the code spans of row 31."""
import os, re

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
P = os.path.join(BASE, 'second_pass', 'out', 'MPL_151_032-075', 'MPL_151_032-075_151-032-151-046_changes.md')

with open(P, encoding='utf-8') as f:
    lines = f.read().split('\n')

old31 = "| ```faisceautiser`` | ```\\unsure{faisceautisés|faisceautisées}`` |"
new31 = "| ``` ``faisceautiser ``` | ``` ``\\unsure{faisceautisés|faisceautisées} ``` |"
n31 = 0
out = []
for ln in lines:
    if old31 in ln:
        ln = ln.replace(old31, new31); n31 += 1
    if ln.startswith('| ') and not ln.startswith('|---'):
        ln = re.sub(r'\\unsure\{([^{}]*)\}', lambda m: '\\unsure{' + m.group(1).replace('|', '\\|') + '}', ln)
    out.append(ln)
assert n31 == 1, n31
with open(P, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
rows = [l for l in out if l.startswith('| ') and l[2:3].isdigit()]
bad = [l[:12] for l in rows if l.replace('\\|', '').count('|') != 8]
print('table rows', len(rows), 'rows with wrong cell count', bad)
