"""Horizontal sweep 1, agent a6d42bf6 (Claude Opus 5.5 at effort max): build PLACEMENT, OBJECTS, FLAGS and CHECK_EVENTS
for one topic from its config cfg_<topic>.py. Read-only on the inputs; writes only sweep1/<topic>/.
Usage: python -I -B build_topic.py SA01"""
import csv, os, re, sys, importlib.util, collections
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from notes_extract import entries, work_units, blocks, H
WHO = 'Claude Opus 5.5 at effort max, a6d42bf6fe2b0d8a8, horizontal sweep 1'
topic = sys.argv[1]
spec = importlib.util.spec_from_file_location('cfg', os.path.join(HERE, f'cfg_{topic}.py'))
cfg = importlib.util.module_from_spec(spec); spec.loader.exec_module(cfg)
OUT = os.path.join(os.path.dirname(HERE), topic); os.makedirs(OUT, exist_ok=True)
E = entries(topic); W = work_units(topic)
ITEMS = {i[0]: dict(zip(['item', 'object', 'kind', 'statement', 'status'], i)) for i in cfg.ITEMS}

def clean_heading(h):
    h = re.sub(r'^[A-Z]{1,3}[0-9]{1,3}[a-z]?(\.\d+)?\s*[—–-]\s*', '', h)
    h = re.sub(r'^[A-Z]\.\s+', '', h)
    return h.strip()

def item_for(pkg, n, heading):
    for (p, lo, hi, it) in cfg.RANGES:
        if (p == pkg or (p != '*' and pkg.startswith(p))) and lo <= n <= hi: return it
    for rx, it in cfg.HEADING_RULES:
        if re.search(rx, heading, re.I): return it
    return cfg.DEFAULT_ITEM.get(pkg, cfg.DEFAULT_ITEM.get('*'))

# codex stage-A notes units with content
CX = []
cdir = os.path.join(H, topic, 'codex')
if os.path.isdir(cdir):
    for f in sorted(os.listdir(cdir)):
        if not f.endswith('_notes.md'): continue
        folder = f[:-9]
        bs = [b for b in blocks(os.path.join(cdir, f)) if b[0] == 2]
        for k, b in enumerate(bs, 1):
            txt = re.sub(r'\s+', ' ', b[3]).strip()
            if txt.lower() in ('none', 'none.', ''): continue
            CX.append(dict(id=f'codex:{folder}#{k}', folder=folder, heading=b[1], text=txt, file=f'{topic}/codex/{f}', line=b[2]))

P = []
used_items = collections.defaultdict(list)
for e in E:
    n = int(e['id'].split('#')[1]); it = item_for(e['pkg'], n, e['heading'])
    ov = cfg.OVERRIDE.get(e['id'], {})
    it = ov.get('item', it)
    obj = ov.get('object') or (ITEMS[it]['object'] + ': ' + clean_heading(e['heading']))[:170]
    his = ov.get('his_term', cfg.HIS.get(it, ''))
    basis = ov.get('basis', 'index-row'); fid = ov.get('fidelity', 'not checked')
    flag = ov.get('flag', ''); note = ov.get('note', '')
    if not note and e['kind']: note = 'kind in the notes: ' + e['kind']
    kind = e['kind'] or ('documentary/apparatus' if it in cfg.APPARATUS else 'note')
    P.append([e['id'], topic, e['cotes'], e['scans'], kind[:80], obj, his, it, basis, fid, flag, note])
    used_items[it].append(e['id'])
AUTO_OBJ = {}
for w in W:
    if w['folder'] not in AUTO_OBJ and w['heading'].lower().startswith('what the pages do'):
        t = re.sub(r'\s+', ' ', re.sub(r'\*\*|`|\[[A-Z0-9, ]+\]', '', w['text'])).strip()
        AUTO_OBJ[w['folder']] = (t.split('. ')[0] + (' ...' if '. ' in t else ''))[:110]
for w in W:
    it = cfg.WORK_ITEM.get(w['folder'], cfg.DEFAULT_ITEM.get('work'))
    if w['folder'] not in cfg.WORK_OBJECT and w['folder'] in AUTO_OBJ:
        cfg.WORK_OBJECT[w['folder']] = ITEMS[cfg.WORK_ITEM.get(w['folder'], cfg.DEFAULT_ITEM.get('work'))]['object'].split(':')[0][:60] + ' - ' + w['folder'] + ': ' + AUTO_OBJ[w['folder']]
    ov = cfg.OVERRIDE.get(w['id'], {})
    it = ov.get('item', it)
    fo = cfg.WORK_OBJECT.get(w['folder'], ITEMS[it]['object'])
    obj = ov.get('object') or f"{fo} ({w['heading'].lower()})"
    scans = cfg.WORK_SCANS.get(w['folder'], '')
    P.append([w['id'], topic, w['cote'], scans, 'Work math-notes unit: ' + w['heading'], obj[:170], ov.get('his_term', cfg.HIS.get(it, '')),
              it, ov.get('basis', 'index-row'), ov.get('fidelity', 'not checked'), ov.get('flag', ''), ov.get('note', 'unit of ' + w['file'].split('/')[-1])])
    used_items[it].append(w['id'])
for c in CX:
    it = cfg.WORK_ITEM.get(c['folder'], cfg.CODEX_ITEM.get(c['folder'], cfg.DEFAULT_ITEM.get('codex', cfg.DEFAULT_ITEM.get('work'))))
    ov = cfg.OVERRIDE.get(c['id'], {})
    it = ov.get('item', it)
    fo = cfg.WORK_OBJECT.get(c['folder'], ITEMS[it]['object'])
    P.append([c['id'], topic, cfg.CODEX_COTE.get(c['folder'], cfg.CODEX_COTE.get(c['folder'][:3], '')), cfg.WORK_SCANS.get(c['folder'], ''), 'Codex stage-A notes unit: ' + c['heading'],
              f"{fo} ({c['heading'].lower()})"[:170], cfg.HIS.get(it, ''), it, ov.get('basis', 'index-row'), ov.get('fidelity', 'not checked'),
              ov.get('flag', ''), ov.get('note', c['text'][:160])])
    used_items[it].append(c['id'])

def w(name, header, rows):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_MINIMAL); wr.writerow(header)
        for r in rows: wr.writerow(r)
w('PLACEMENT.tsv', ['entry_id', 'topic', 'cote', 'scans', 'kind', 'object', 'his_term', 'item', 'basis', 'fidelity', 'flag', 'note'], P)
cotescans = collections.defaultdict(set)
for r in P:
    if r[2] or r[3]: cotescans[r[7]].add(f"{r[2]}:{r[3]}" if r[3] else r[2])
O = []
for it, d in ITEMS.items():
    ents = used_items.get(it, [])
    if not ents: continue
    O.append([it, d['object'], d['kind'], d['statement'], f"{len(ents)}: " + ', '.join(ents[:12]) + (' ...' if len(ents) > 12 else ''),
              '; '.join(sorted(cotescans[it]))[:200], d['status'], cfg.CROSS.get(it, ''), cfg.ITEM_FLAGS.get(it, '')])
w('OBJECTS.tsv', ['item', 'object', 'kind', 'statement', 'entries', 'cotes_scans', 'status_on_pages', 'cross_topic', 'flags'], O)
w('FLAGS.tsv', ['kind', 'where', 'what', 'evidence'], cfg.FLAGS)
w('CHECK_EVENTS.tsv', ['id', 'date_utc', 'who', 'how', 'result', 'where'], [[c[0], cfg.DATE, WHO, c[1], c[2], c[3]] for c in cfg.CHECKS])
bas = collections.Counter(r[8] for r in P); fid = collections.Counter(r[9] for r in P if r[8] == 'passage-read')
unused = [it for it in ITEMS if it not in used_items]
print(topic, 'rows', len(P), '(index', len(E), 'work', len(W), 'codex', len(CX), ') items', len(O), 'basis', dict(bas), 'fidelity', dict(fid),
      'flags', len(cfg.FLAGS), 'checks', len(cfg.CHECKS), 'unused items', unused)
miss = [e['id'] for e in E if not e['file']]
if miss: print('unmatched entries', miss[:10])
