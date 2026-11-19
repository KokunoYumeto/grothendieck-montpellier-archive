# Sweep-2 placement of the gap entries into sweep2/SA<nn>/ (agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026)
# usage: python -I -B build2.py SA01   (reads cfg2_SA01.py; idempotent: replaces only the rows it owns)
import csv, os, re, sys, collections, importlib.util
csv.field_size_limit(10**9)
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from gap_tools import gap, S2
topic = sys.argv[1]
spec = importlib.util.spec_from_file_location('cfg', os.path.join(HERE, f'cfg2_{topic}.py'))
cfg = importlib.util.module_from_spec(spec); spec.loader.exec_module(cfg)
OUT = os.path.join(S2, topic)
WHO = 'Claude Opus 5.5 at effort max, a6d42bf6fe2b0d8a8, horizontal sweep 2'

def rd(name):
    with open(os.path.join(OUT, name), encoding='utf-8', newline='') as f:
        rows = list(csv.reader(f, delimiter='\t'))
    return rows[0], rows[1:]

def w(name, header, rows):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_MINIMAL); wr.writerow(header)
        for r in rows: wr.writerow(r)

G = cfg.prepare(gap(topic)) if hasattr(cfg, 'prepare') else gap(topic)
gset = {g['entry_id'] for g in G}
hP, P = rd('PLACEMENT.tsv')
P = [r for r in P if r[0] not in gset]
NEW = {i[0]: dict(zip(['item', 'object', 'kind', 'statement', 'status'], i)) for i in cfg.ITEMS2}
hO, O = rd('OBJECTS.tsv')
O = [r for r in O if r[0] not in NEW]
OLD = {r[0]: r for r in O}
newrows = []
for g in G:
    d = cfg.place(g)
    d.update(cfg.OVERRIDE.get(g['entry_id'], {}))
    it = d['item']
    if it not in NEW and it not in OLD: raise SystemExit(f"unknown item {it} for {g['entry_id']}")
    row = [g['entry_id'], topic, d.get('cote', ''), d.get('scans', g['scans']), d.get('kind', g['cls'])[:80], d.get('object', '')[:200],
           d.get('his_term', ''), it, d.get('basis', 'index-row'), d.get('fidelity', 'not checked'), d.get('flag', ''), d.get('note', '')[:300]]
    newrows.append(row)
P = P + newrows
w('PLACEMENT.tsv', hP, P)
ents = collections.defaultdict(list); cs = collections.defaultdict(set)
for r in P:
    ents[r[7]].append(r[0])
    if r[2] or r[3]: cs[r[7]].add(f"{r[2]}:{r[3]}" if r[3] else r[2])
def addto(old, extra):
    if not extra: return old
    parts = [p for p in extra.split('; ') if p and p not in old]
    return (old + '; ' + '; '.join(parts)) if old and parts else (old or '; '.join(parts))
outO = []
for r in O:
    it = r[0]; e = ents.get(it, [])
    r = list(r) + [''] * (9 - len(r))
    if e: r[4] = f"{len(e)}: " + ', '.join(e[:12]) + (' ...' if len(e) > 12 else '')
    r[5] = '; '.join(sorted(cs[it]))[:200] if cs[it] else r[5]
    r[7] = addto(r[7], cfg.CROSS2.get(it, '')); r[8] = addto(r[8], cfg.ITEM_FLAGS2.get(it, ''))
    if it in getattr(cfg, 'OBJ_UPDATE', {}): r[1] = cfg.OBJ_UPDATE[it]
    outO.append(r)
unused = []
for it in sorted(NEW, key=lambda x: int(x.split('-')[1])):
    e = ents.get(it, [])
    if not e: unused.append(it); continue
    d = NEW[it]
    outO.append([it, d['object'], d['kind'], d['statement'], f"{len(e)}: " + ', '.join(e[:12]) + (' ...' if len(e) > 12 else ''),
                 '; '.join(sorted(cs[it]))[:200], d['status'], cfg.CROSS2.get(it, ''), cfg.ITEM_FLAGS2.get(it, '')])
w('OBJECTS.tsv', hO, outO)
hF, F = rd('FLAGS.tsv')
F = [r for r in F if not (len(r) > 3 and r[3].endswith('(sweep 2)'))] + [[k, wh, wt, ev + ' (sweep 2)'] for k, wh, wt, ev in cfg.FLAGS2]
w('FLAGS.tsv', hF, F)
hC, C = rd('CHECK_EVENTS.tsv')
C = [r for r in C if len(r) < 3 or r[2] != WHO] + [[c[0], cfg.DATE, WHO, c[1], c[2], c[3]] for c in cfg.CHECKS2]
w('CHECK_EVENTS.tsv', hC, C)
if getattr(cfg, 'NOTES2', ''):
    p = os.path.join(OUT, 'TOPIC_NOTES.md'); s = open(p, encoding='utf-8').read()
    i = s.find('\n## Sweep 2')
    if i >= 0: s = s[:i]
    open(p, 'w', encoding='utf-8').write(s.rstrip('\n') + '\n\n' + cfg.NOTES2.strip('\n') + '\n')
bas = collections.Counter(r[8] for r in newrows); fid = collections.Counter(r[9] for r in newrows if r[8] == 'passage-read')
it_new = collections.Counter(r[7] for r in newrows)
print(topic, 'gap rows', len(newrows), 'of', len(G), '| basis', dict(bas), '| fidelity', dict(fid), '| row flags', sum(1 for r in newrows if r[10]),
      '| FLAGS2', len(cfg.FLAGS2), '| checks2', len(cfg.CHECKS2), '| new items', len(NEW) - len(unused), 'unused', unused)
print('items used by gap rows:', sorted(it_new.items(), key=lambda x: (x[0].split('-')[0], int(x[0].split('-')[1]))))
