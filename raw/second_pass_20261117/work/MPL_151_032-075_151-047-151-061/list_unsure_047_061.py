"""List every \\unsure{...} (balanced braces) in the corrected scans 047-061, as markdown lines."""
import io
import os

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
OUT = os.path.join(BASE, 'second_pass', 'out', 'MPL_151_032-075')
TAG = '\\unsure{'

for n in range(47, 62):
    t = io.open(os.path.join(OUT, 'MPL_151_032-075_151_scan%03d.tex' % n), encoding='utf-8').read()
    items, pos = [], 0
    while True:
        i = t.find(TAG, pos)
        if i < 0:
            break
        j, depth = i + len(TAG), 1
        while depth:
            depth += {'{': 1, '}': -1}.get(t[j], 0)
            j += 1
        line = t.count('\n', 0, i) + 1
        items.append('l.%d `%s`' % (line, t[i + len(TAG):j - 1].replace('\n', ' ')))
        pos = i + len(TAG)
    print('- %03d (%d): %s' % (n, len(items), '; '.join(items)))
