# Sweep 2 part 2: interlinking tables and the readable map of a topic (agent a6d42bf6, Claude Opus 5.5 at effort max, 18 Nov 2026)
# usage: python -I -B build3.py SA01   (reads cfg3_SA01.py; writes DEPENDS, CLAIM_LINKS, UNIT_LINKS, CORRECTIONS, WHAT_IS_WHERE.md; appends part-2 check events)
import csv, os, re, sys, collections, importlib.util
csv.field_size_limit(10**9)
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
DOC = 'C:/Users/user/Documents'
S2 = os.path.join(DOC, 'results_register', 'horizontal', 'sweep2')
topic = sys.argv[1]
spec = importlib.util.spec_from_file_location('cfg', os.path.join(HERE, f'cfg3_{topic}.py'))
cfg = importlib.util.module_from_spec(spec); spec.loader.exec_module(cfg)
OUT = os.path.join(S2, topic)
WHO3 = 'Claude Opus 5.5 at effort max, a6d42bf6fe2b0d8a8, horizontal sweep 2 part 2'

def rd(name):
    with open(os.path.join(OUT, name), encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))
def w(name, header, rows):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_MINIMAL); wr.writerow(header)
        for r in rows: wr.writerow(r)
def scans_of(s):
    out = set()
    for a, b in re.findall(r'(\d+)(?:\s*-\s*(\d+))?', s or ''):
        a = int(a); b = int(b) if b else a
        if b - a < 400: out |= set(range(a, b + 1))
    return out
def compact(nums):
    nums = sorted(nums); out = []; i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1: j += 1
        out.append(str(nums[i]) if i == j else f'{nums[i]}-{nums[j]}'); i = j + 1
    return ','.join(out)

P = rd('PLACEMENT.tsv'); O = rd('OBJECTS.tsv'); F = rd('FLAGS.tsv')
OBJ = {o['item']: o for o in O}
ordered = [it for _, its in cfg.ORDER for it in its]
miss = [i for i in OBJ if i not in ordered]; extra = [i for i in ordered if i not in OBJ]
dup = [i for i, c in collections.Counter(ordered).items() if c > 1]
if miss or extra or dup: raise SystemExit(f'ORDER mismatch: missing {miss} extra {extra} dup {dup}')
NONMATH = {i for i, o in OBJ.items() if re.search(r'documentary|apparatus', o['kind'] + ' ' + o['object'][:40], re.I)}
by_item = collections.defaultdict(list)
for r in P: by_item[r['item']].append(r)

# DEPENDS
D = []
for a, b, basis, where in cfg.DEPS:
    D.append([a, 'uses', b, basis, where])
    if re.match(r'SA\d\d-\d+$', b): D.append([b, 'used by', a, basis, where])
for a, b, basis, where in getattr(cfg, 'RELATED', []):
    D.append([a, 'related', b, basis, where])
    if re.match(r'SA\d\d-\d+$', b): D.append([b, 'related', a, basis, where])
D.sort(key=lambda r: (ordered.index(r[0]) if r[0] in ordered else 999, r[1], r[2]))
w('DEPENDS.tsv', ['item', 'relation', 'other', 'basis', 'where'], D)

# CLAIM_LINKS
w('CLAIM_LINKS.tsv', ['claim_id', 'his_claim', 'his_place', 'item', 'linked_to', 'relation', 'basis', 'where'], cfg.CLAIMS)

# CORRECTIONS
C = list(cfg.CORR) + (cfg.corr_auto(P) if hasattr(cfg, 'corr_auto') else [])
w('CORRECTIONS.tsv', ['id', 'item', 'where', 'kind', 'what', 'corrected', 'evidence', 'decided_by'], C)

# UNIT_LINKS
with open(os.path.join(DOC, 'grothendieck_archive_transcription_20261110', 'UNITS_DRAFT_20261118.tsv'), encoding='utf-8', newline='') as f:
    U = list(csv.DictReader(f, delimiter='\t'))
folder_items = collections.defaultdict(collections.Counter)
for r in P:
    m = re.match(r'work:([A-Z]+\d+-\d+(?:_\d+)?)#', r['entry_id'])
    if m: folder_items[m.group(1)][r['item']] += (100 if r['item'] not in NONMATH else 1)
idx = collections.defaultdict(list)
for r in P:
    if r['item'] in NONMATH or r['entry_id'].startswith(('work:', 'codex:')): continue
    for c in re.split(r'[,; ]+', r['cote']):
        if c: idx[c].append((scans_of(r['scans']), r['item']))
UL = []
for u in U:
    rule = next((it for rx, it in getattr(cfg, 'UNIT_TITLE_RULES', []) if re.search(rx, u['folder'] + ' ' + u['title'], re.I)), None)
    if rule:
        UL.append([rule, u['unit'], u['cote'], u['folder'], u['scans'], u['title'], 'unit title rule']); continue
    us = scans_of(u['scans'])
    cand = collections.Counter(it for s, it in idx.get(u['cote'], []) if s & us)
    if u['folder'] in folder_items:
        it = folder_items[u['folder']].most_common(1)[0][0]
        UL.append([it, u['unit'], u['cote'], u['folder'], u['scans'], u['title'], 'folder placed in this topic']); continue
    if cand:
        it, n = cand.most_common(1)[0]
        UL.append([it, u['unit'], u['cote'], u['folder'], u['scans'], u['title'], f'scan overlap with {n} placed Pro entries'])
UL.sort(key=lambda r: (ordered.index(r[0]) if r[0] in ordered else 999, r[1]))
w('UNIT_LINKS.tsv', ['item', 'unit', 'cote', 'folder', 'scans', 'title', 'basis'], UL)

# CHECK_EVENTS
CE = rd('CHECK_EVENTS.tsv')
drop_who = {WHO3} | set(getattr(cfg, 'DROP_WHO', []))
keep = [[r['id'], r['date_utc'], r['who'], r['how'], r['result'], r['where']] for r in CE if r['who'] not in drop_who]
new = [[c[0], cfg.DATE, WHO3, c[1], c[2], c[3]] for c in cfg.CHECKS3] + (cfg.checks_auto(P) if hasattr(cfg, 'checks_auto') else [])
w('CHECK_EVENTS.tsv', ['id', 'date_utc', 'who', 'how', 'result', 'where'], keep + new)

# WHAT_IS_WHERE.md
deps = collections.defaultdict(lambda: collections.defaultdict(list))
for a, rel, b, basis, where in D: deps[a][rel].append(f'{b} ({basis})')
claims = collections.defaultdict(list)
for c in cfg.CLAIMS: claims[c[3]].append(c)
corrs = collections.defaultdict(list)
for c in C: corrs[c[1]].append(c)
units = collections.defaultdict(list)
for r in UL: units[r[0]].append(r[1])
flagrows = collections.defaultdict(list)
for fl in F:
    txt = ' '.join(fl.values())
    for it in OBJ:
        if re.search(re.escape(it) + r'(?!\d)', txt): flagrows[it].append(fl['kind'])
    ids = set(re.findall(r'[A-Za-z_]+[\w:.+-]*#\d+', fl.get('where', '')))
    for r in P:
        if r['entry_id'] in ids: flagrows[r['item']].append(fl['kind'])
def notes_file(eid):
    if eid.startswith('work:'):
        f = eid.split(':')[1].split('#')[0]; return f'codex_web_20261113/returns/{f}/out/{f}_mathnotes.md'
    if eid.startswith('codex:'):
        f = eid.split(':')[1].split('#')[0]; return f'codex_web_20261113/returns/{f}/out/{f}_notes.md'
    pkg = eid.split('#')[0].split(':')[0]
    if ':records:' in eid: return f'returns/{pkg}_unzipped/.../{eid.split(":records:")[1].split("#")[0]}.md'
    return f'inputs/{topic}/pro/{pkg}_notes.md'
L = [f'# {cfg.TITLE}: what is where', '', f'{WHO3}, {cfg.DATE}.', '']
L += [cfg.INTRO.strip(), '']
L += ['How to read an entry:', '- **Where:** cote and scans, the notes it is in (package or folder), and the notes files. Scans are the PDF pages of the cote in `grothendieck_archive_montpellier`.',
      '- **Depends:** what the item uses and what uses it, with the basis: his page, our note, or a proof (ours).',
      '- **Claims:** his claims on the item, linked to what proves, refutes or refines them (CLAIM_LINKS.tsv).',
      '- **Units:** the companion units that discuss it (UNIT_LINKS.tsv).',
      '- **Flags, corrections:** from FLAGS.tsv and CORRECTIONS.tsv.', '']
for sec, its in cfg.ORDER:
    L += [f'## {sec}', '']
    for it in its:
        o = OBJ[it]; rows = by_item[it]
        cs = collections.defaultdict(set)
        for r in rows:
            c = '+'.join(x for x in re.split(r'[,; ]+', r['cote']) if x)
            if c: cs[c] |= scans_of(r['scans'])
        where = '; '.join(('cotes ' if '+' in c else 'cote ') + c + (f', scans {compact(s)}' if s else '') for c, s in sorted(cs.items(), key=lambda x: (int(re.match(r'\d+', x[0]).group()), x[0])))
        srcs = collections.Counter(re.sub(r'#\d+$', '', r['entry_id']) for r in rows)
        files = sorted({notes_file(r['entry_id']) for r in rows})
        tag = re.findall(r'= (H0\w\w)', o.get('cross_topic', ''))
        L.append(f'### {it}: {o["object"]}' + (f' (= {", ".join(dict.fromkeys(tag))})' if tag else ''))
        L.append('')
        L.append(f'- **Status on his pages:** {o["status_on_pages"] or "not checked"}. **Kind:** {o["kind"]}.')
        L.append(f'- **Where:** {where or "no scans recorded"}.')
        L.append(f'- **Notes ({len(rows)} {"entry" if len(rows) == 1 else "entries"}):** ' +'; '.join(f'{s} ({n})' for s, n in srcs.most_common(8)) + (' ...' if len(srcs) > 8 else '') + '.')
        L.append('- **Notes files:** ' + '; '.join(f'`{x}`' for x in files[:6]) + (' ...' if len(files) > 6 else '') + '.')
        d = deps.get(it, {})
        if d:
            L.append('- **Depends:** ' + '; '.join(f'{rel}: ' + ', '.join(v) for rel, v in d.items()) + '.')
        if claims.get(it):
            L.append('- **Claims:**')
            for c in claims[it]:
                L.append(f'  - {c[0]} ({c[2]}): "{c[1][:140]}". **{c[5]}**: {c[4][:260]}.')
        if corrs.get(it):
            L.append('- **Corrections:** ' + '; '.join(f'{c[2]}: {c[4][:80]} -> {c[5][:80]}' for c in corrs[it]) + '.')
        if units.get(it):
            L.append(f'- **Units ({len(units[it])}):** ' + ', '.join(units[it][:8]) + (' ...' if len(units[it]) > 8 else '') + '.')
        fl = collections.Counter(flagrows.get(it, []))
        if fl or o.get('flags'):
            L.append('- **Flags:** ' + '; '.join([f'{k} ({n})' for k, n in fl.items()] + ([o['flags']] if o.get('flags') else [])) + '.')
        if o.get('cross_topic'):
            L.append(f'- **Other topics:** {o["cross_topic"]}.')
        L.append('')
L += ['## Counts', '', f'- Items: {len(OBJ)}; placed entries: {len(P)}.', f'- DEPENDS rows: {len(D)}; CLAIM_LINKS: {len(cfg.CLAIMS)}; UNIT_LINKS: {len(UL)}; CORRECTIONS: {len(C)}; part-2 check events: {len(new)}.', '']
open(os.path.join(OUT, 'WHAT_IS_WHERE.md'), 'w', encoding='utf-8').write('\n'.join(L))
print(topic, 'items', len(OBJ), 'DEPENDS', len(D), 'CLAIMS', len(cfg.CLAIMS), 'UNITS', len(UL), 'CORR', len(C), 'checks3', len(new), 'units by basis', dict(collections.Counter(r[6].split(' with ')[0] for r in UL)))
