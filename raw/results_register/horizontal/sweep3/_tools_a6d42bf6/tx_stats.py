# Transcription statistics per cote part (agent a6d42bf6, horizontal sweep 3): folders, scans, unsure marks, illegible marks, doubt rows, audits
# usage: python -I -B tx_stats.py <returns dir> <glob prefix> [...]
import os, re, glob, sys, collections
sys.stdout.reconfigure(encoding='utf-8')
R = sys.argv[1]
rows = []
for pref in sys.argv[2:]:
    for d in sorted(glob.glob(os.path.join(R, pref + '*'))):
        name = os.path.basename(d)
        tp = os.path.join(d, 'out', name + '_transcription.tex')
        if not os.path.exists(tp): continue
        t = open(tp, encoding='utf-8', errors='replace').read()
        sc = [int(x) for x in re.findall(r'scanpage\{0*(\d+)\}', t)]
        un = t.count(chr(92) + 'unsure{'); ill = len(re.findall('illegible', t))
        dp = os.path.join(d, 'out', name + '_doubts.md')
        db = len(re.findall(r'(?m)^\|\s*[^-\s|]', open(dp, encoding='utf-8').read())) if os.path.exists(dp) else 0
        au = os.path.exists(os.path.join(d, 'out', name + '_audit.md'))
        rows.append((name, sc, un, ill, db, au))
part = collections.OrderedDict()
for name, sc, un, ill, db, au in rows:
    k = re.match(r'[A-Z](\d+(?:-\d+)?)', name).group(1) if name.startswith('J') else name
    p = part.setdefault(k, dict(folders=0, scans=0, un=0, ill=0, db=0, au=0, lo=9999, hi=0))
    p['folders'] += 1; p['scans'] += len(sc); p['un'] += un; p['ill'] += ill; p['db'] += db; p['au'] += au
    if sc: p['lo'] = min(p['lo'], min(sc)); p['hi'] = max(p['hi'], max(sc))
for k, p in part.items():
    print(f"{k}\tfolders {p['folders']}\tscans {p['scans']} ({p['lo']}-{p['hi']})\tunsure {p['un']} ({p['un']/max(1,p['scans']):.1f}/scan)\tillegible {p['ill']}\tdoubt rows {p['db']}\taudits {p['au']}")
