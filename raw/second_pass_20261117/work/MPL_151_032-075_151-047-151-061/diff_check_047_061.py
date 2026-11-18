"""Word-level diff of the corrected scans 047-061 against the first pass, and doubt-mark counts."""
import difflib
import io
import os
import re

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
FIRST = os.path.join(BASE, 'returns', 'MPL_151_032-075_unzipped', 'pages')
OUT = os.path.join(BASE, 'second_pass', 'out', 'MPL_151_032-075')

tot_first = tot_out = 0
for n in range(47, 62):
    name = 'MPL_151_032-075_151_scan%03d.tex' % n
    a = io.open(os.path.join(FIRST, name), encoding='utf-8').read()
    b = io.open(os.path.join(OUT, name), encoding='utf-8').read()
    ua, ub = a.count('\\unsure{'), b.count('\\unsure{')
    tot_first += ua
    tot_out += ub
    ta, tb = re.findall(r'\S+', a), re.findall(r'\S+', b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    print('=== scan %03d  unsure first=%d out=%d' % (n, ua, ub))
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal':
            print('  %s: %r -> %r' % (op, ' '.join(ta[i1:i2])[:200], ' '.join(tb[j1:j2])[:200]))
print('TOTAL unsure macros: first pass %d, corrected %d' % (tot_first, tot_out))
