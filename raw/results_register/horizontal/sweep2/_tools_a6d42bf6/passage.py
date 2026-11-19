# Show transcription text around a pattern on one scan page (agent a6d42bf6, horizontal sweep 2)
# usage: python -I -B passage.py <tex path> <scan> <regex|-> [width]   ('-' prints the whole scan segment, cut to width)
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
path, scan, pat = sys.argv[1], int(sys.argv[2]), sys.argv[3]
w = int(sys.argv[4]) if len(sys.argv) > 4 else 300
t = open(path, encoding='utf-8', errors='replace').read()
parts = re.split(r'\\scanpage\{0*(\d+)\}', t)
seg = {}
for i in range(1, len(parts) - 1, 2):
    seg.setdefault(int(parts[i]), '')
    seg[int(parts[i])] += parts[i + 1]
s = seg.get(scan, '')
if not s:
    print('no scan', scan, 'have', sorted(seg)[:5], '...', sorted(seg)[-3:]); sys.exit()
flat = re.sub(r'\s+', ' ', s)
if pat == '-':
    print(f'[{scan}] {flat[:w]}')
else:
    n = 0
    for m in re.finditer(pat, flat):
        a = max(0, m.start() - w // 3)
        print(f'[{scan}] ...{flat[a:m.start() + w]}...')
        n += 1
        if n >= 2: break
    if not n: print(f'[{scan}] no match for {pat}')
