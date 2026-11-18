"""Print register rows of scope s6 in full or truncated: show.py N TAG [TAG...]  (read-only)."""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract import load
rows, cp, flags, edges, led = load()
R = {r['tag']: r for r in rows}
n = int(sys.argv[1])
for t in sys.argv[2:]:
    if ':' not in t: t = 'S6_06_BLIND:' + t
    r = R.get(t)
    if r is None:
        rid = t.split(':')[1]
        if t.startswith('S6_06_BLIND') and rid in cp:
            c = cp[rid]; print(t, '(cp35 only)', c['status'], '::', re.sub(r'\s+', ' ', c['statement'])[:n]); print(); continue
        print(t, 'MISSING'); continue
    s = re.sub(r'\s+', ' ', r['statement'])
    print(t, r['status'], '::', s[:n])
    print('   WP:', r['where_proved'][:100], '| DEP:', re.sub(r'\s+', ' ', r['depends_on'])[:160], '| NOTES:', re.sub(r'\s+', ' ', r['notes'])[:300])
    print()
