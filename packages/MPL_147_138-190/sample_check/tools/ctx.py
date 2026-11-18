# usage: python -I -B ctx.py <context_file> <scan_from>-<scan_to> <regex> [<regex> ...]
# Prints, for the given scan range of a context transcription, each match of each regex with a little context.
import re, sys

BS = chr(92)
f, rng = sys.argv[1], sys.argv[2]
a, b = [int(x) for x in rng.split('-')]
s = open(f, encoding='utf-8').read()
marks = [(m.start(), m.group(0)) for m in re.finditer(BS + BS + r'scanpage\{[^}]*\}|^%+ *=*.*?scan[ _]?\d+.*$', s, flags=re.M)]
# find page boundaries by any marker containing a number
pages = []
for pos, txt in marks:
    nums = re.findall(r'\d+', txt)
    if nums:
        pages.append((pos, int(nums[-1]), txt[:60]))
if not pages:
    print('no page markers found; first 300 chars:', s[:300])
    sys.exit()
sel = ''
for i, (pos, n, txt) in enumerate(pages):
    if a <= n <= b:
        end = pages[i + 1][0] if i + 1 < len(pages) else len(s)
        sel += '\n@@SCAN %d@@ ' % n + s[pos:end]
print('markers: %d; selected chars: %d; marker sample: %r' % (len(pages), len(sel), pages[0][2]))
for rx in sys.argv[3:]:
    ms = list(re.finditer(rx, sel, flags=re.I))
    print('--- %s: %d match(es)' % (rx, len(ms)))
    for m in ms[:3]:
        st = sel.rfind('@@SCAN', 0, m.start())
        scan = sel[st:st + 12]
        print('   [%s] ...%s...' % (scan, sel[max(m.start() - 110, 0):m.end() + 110].replace('\n', ' ')))
