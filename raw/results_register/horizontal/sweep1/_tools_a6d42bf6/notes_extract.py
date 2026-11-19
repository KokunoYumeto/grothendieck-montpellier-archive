"""Horizontal sweep 1 (agent a6d42bf6, Claude Opus 5.5 at effort max): map NOTES_INDEX rows and Work math-notes units
to their text. Read-only on the inputs. Usage: notes_extract.py SA01 dump|json [opening_chars]"""
import csv, sys, os, re, json
sys.stdout.reconfigure(encoding='utf-8')
csv.field_size_limit(10**9)
H = 'C:/Users/user/Documents/results_register/horizontal/inputs'
DOC = 'C:/Users/user/Documents/'
HEAD = re.compile(r'^(#{1,6})\s+(.*)$')

def blocks(path):
    """list of (level, heading, start_line, text) for every markdown heading of a file"""
    if not os.path.exists(path): return []
    L = open(path, encoding='utf-8').read().split('\n')
    hs = [(i, len(m.group(1)), m.group(2).strip()) for i, l in enumerate(L) for m in [HEAD.match(l)] if m]
    out = []
    for j, (i, lev, h) in enumerate(hs):
        k = len(L)
        for i2, lev2, h2 in hs[j + 1:]:
            if lev2 <= lev: k = i2; break
        nxt = hs[j + 1][0] if j + 1 < len(hs) else len(L)
        out.append((lev, h, i + 1, '\n'.join(L[i + 1:k]), '\n'.join(L[i + 1:nxt])))
    return out

def norm(s): return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()

def entries(topic):
    rows = list(csv.DictReader(open(f'{H}/{topic}/NOTES_INDEX.tsv', encoding='utf-8'), delimiter='\t'))
    cache = {}; used = {}
    res = []
    for r in rows:
        pkg = r['package']
        if pkg not in cache:
            files = []
            for sub, suf in (('pro', '_notes.md'), ('pro', '_doubts.md'), ('codex', '_notes.md')):
                p = f'{H}/{topic}/{sub}/{pkg}{suf}'
                if os.path.exists(p):
                    for b in blocks(p): files.append((p, b))
            cache[pkg] = files; used[pkg] = set()
        target = norm(r['heading']); hit = None
        for idx, (p, b) in enumerate(cache[pkg]):
            if idx in used[pkg]: continue
            if norm(b[1]) == target or (target and norm(b[1]).startswith(target[:60])):
                hit = (idx, p, b); break
        kind = r['kind'].split('. **')[0].strip() if r['kind'] else ''
        if hit:
            used[pkg].add(hit[0]); p, b = hit[1], hit[2]
            res.append(dict(id=r['entry_id'], pkg=pkg, cotes=r['cotes'], heading=r['heading'], kind=kind, scans=r['scans_cited'],
                            file=os.path.relpath(p, H).replace(chr(92), '/'), line=b[2], text=b[3], own=b[4]))
        else:
            res.append(dict(id=r['entry_id'], pkg=pkg, cotes=r['cotes'], heading=r['heading'], kind=kind, scans=r['scans_cited'],
                            file='', line=0, text='', own=''))
    return res

def work_units(topic):
    rows = [x for x in csv.DictReader(open(f'{H}/WORK_MATHNOTES_BY_TOPIC.tsv', encoding='utf-8'), delimiter='\t') if x['topic'] == topic]
    res = []
    for x in rows:
        p = DOC + x['path']
        bs = [b for b in blocks(p) if b[0] == 2]
        title = ''
        if os.path.exists(p):
            first = open(p, encoding='utf-8').readline().strip('# \n')
            title = first
        for n, b in enumerate(bs, 1):
            res.append(dict(id=f"work:{x['folder']}#{n}", folder=x['folder'], cote=x['cote'], heading=b[1], title=title,
                            file=x['path'], line=b[2], text=b[3]))
    return res

if __name__ == '__main__':
    topic, mode = sys.argv[1], sys.argv[2]
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 90
    E = entries(topic); W = work_units(topic)
    if mode == 'dump':
        for e in E:
            op = re.sub(r'\s+', ' ', re.sub(r'\*\*|`', '', e['own']))[:n]
            print(f"{e['id'].split('#')[0][-12:]}#{e['id'].split('#')[1]}|{e['kind'][:28]}|{e['scans'][:18]}|{e['heading'][:110]}|{len(e['text'])}|{op}")
        print('UNMATCHED', sum(1 for e in E if not e['file']), 'of', len(E), '; work units', len(W))
    elif mode == 'work':
        for w in W:
            op = re.sub(r'\s+', ' ', re.sub(r'\*\*|`', '', w['text']))[:n]
            print(f"{w['id']}|{w['heading'][:40]}|{len(w['text'])}|{op}")
