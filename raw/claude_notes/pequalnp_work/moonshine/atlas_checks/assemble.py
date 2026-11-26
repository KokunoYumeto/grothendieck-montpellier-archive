"""Assemble MOONSHINE_ATLAS.md from the parts and appendices; escape '|' inside code spans of table rows."""
import re, sys, os
D = sys.argv[1]
OUT = sys.argv[2]
parts = ['part0.md', 'part1a.md', 'part1b.md', 'part1c.md', 'part2.md', 'part3.md', 'part4.md', 'part5.md']
apps = ['appA.md', 'appB.md', 'appC.md', 'appD.md']
BT = chr(96)
PIPE = re.compile(r'(?<!\\)\|')

def fix(line):
    if not line.lstrip().startswith('|'):
        return line
    segs = line.split(BT)
    for i in range(1, len(segs), 2):
        segs[i] = PIPE.sub(lambda m: '\\|', segs[i])
    return BT.join(segs)

out = []
for p in parts:
    s = open(os.path.join(D, p), encoding='utf-8').read()
    out.append('\n'.join(fix(l) for l in s.split('\n')))
out.append('\n---\n')
for p in apps:
    s = open(os.path.join(D, p), encoding='utf-8').read()
    out.append('\n'.join(fix(l) for l in s.split('\n')) + '\n')
txt = '\n'.join(out)
# checks: odd backticks in table rows; column-count consistency per table
problems = []
lines = txt.split('\n')
cur = None
for i, l in enumerate(lines, 1):
    if l.lstrip().startswith('|'):
        if l.count(BT) % 2:
            problems.append('odd backticks L%d: %s' % (i, l[:100]))
        segs = l.split(BT)
        n = sum(len(PIPE.findall(segs[j])) for j in range(0, len(segs), 2))
        if cur is None:
            cur = n
        elif n != cur:
            problems.append('column count %d vs %d at L%d: %s' % (n, cur, i, l[:100]))
    else:
        cur = None
open(OUT, 'w', encoding='utf-8').write(txt)
print('chars', len(txt), 'lines', len(lines))
print('\n'.join(problems[:40]))
print('problems', len(problems))
