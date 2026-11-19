# Gap entries of a topic with their text (agent a6d42bf6, Claude Opus 5.5 at effort max, horizontal sweep 2, 18 Nov 2026)
# usage: python -I -B gap_tools.py SA01 dump [nchars] [id-substring]
import csv, os, re, sys, collections
csv.field_size_limit(10**9)
DOC = 'C:/Users/user/Documents'
S2 = os.path.join(DOC, 'results_register', 'horizontal', 'sweep2')

def units_by_file():
    d = collections.defaultdict(set)
    with open(os.path.join(S2, 'inputs', 'UNITS.tsv'), encoding='utf-8', newline='') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            try: d[r['source_file']].add(int(r['line']))
            except Exception: pass
    return {k: sorted(v) for k, v in d.items()}

def gap(topic):
    with open(os.path.join(S2, 'inputs', topic, 'GAP_INDEX.tsv'), encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    U = units_by_file(); cache = {}
    for r in rows:
        sf = r['source_file']
        if sf not in cache:
            cache[sf] = open(os.path.join(DOC, sf), encoding='utf-8', errors='replace').read().split('\n')
        L = cache[sf]; ln = int(r['line'])
        nxt = [x for x in U.get(sf, []) if x > ln]
        end = nxt[0] - 1 if nxt else len(L)
        seg = L[ln - 1:end]
        r['text'] = '\n'.join(seg)
        r['body'] = '\n'.join(seg[1:]) if seg and seg[0].lstrip().startswith('#') else '\n'.join(seg)
        m = re.match(r'(?:work|codex):([A-Z]+\d+(?:-\d+)*)', r['entry_id'])
        r['folder'] = m.group(1) if m else ''
    return rows

def flat(s):
    return re.sub(r'\s+', ' ', re.sub(r'\*\*|`', '', s)).strip()

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    topic, mode = sys.argv[1], sys.argv[2]
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    sub = sys.argv[4] if len(sys.argv) > 4 else ''
    G = gap(topic)
    if mode == 'dump':
        for g in G:
            if sub and sub not in g['entry_id']: continue
            print(f"{g['entry_id']}|{g['words']}w|s:{g['scans'][:20]}|{g['heading'][:90]}|{flat(g['body'])[:n]}")
    elif mode == 'count':
        print(len(G), collections.Counter(g['cls'] for g in G))
