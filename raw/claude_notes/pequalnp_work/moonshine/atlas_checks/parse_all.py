"""Parse the three FIND dossiers and the three MAPS conference files into entries and maps.

Writes (next to this script, in the folder given as argv[2]):
  entries.json  : {id: {dossier, line_start, line_end, title, body}}
  maps.json     : [{mid, file, line_start, line_end, home, arrow_ids, all_ids, type, text}]
  stats.txt     : counts, type distribution, unparsed lines that look like maps
"""
import json, re, sys, os, collections

SRC = sys.argv[1]  # <local>/pequalnp_work/moonshine
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)

ID_RE = re.compile(r'\b(S6|AG|WEEK)-(\d{3})\b')

def read(name):
    with open(os.path.join(SRC, name), encoding='utf-8') as f:
        return f.read().split('\n')

entries = {}
def parse_find(name, head_re, dossier):
    lines = read(name)
    cur = None
    for i, ln in enumerate(lines, 1):
        m = head_re.match(ln)
        if m:
            if cur:
                cur['line_end'] = i - 1
            cur = {'id': m.group(1), 'dossier': dossier, 'line_start': i, 'line_end': None,
                   'title': m.group(2).strip(), 'body': []}
            entries[m.group(1)] = cur
            continue
        if cur is not None:
            if ln.startswith('## ') or ln.startswith('# '):
                cur['line_end'] = i - 1
                cur = None
                continue
            cur['body'].append(ln)
    if cur:
        cur['line_end'] = len(lines)

parse_find('FIND_s6.md', re.compile(r'^\*\*(S6-\d{3})\*\*\s*[·\-—]\s*(.*)$'), 'S6')
parse_find('FIND_ag.md', re.compile(r'^\*\*(AG-\d{3})\*\*\s*(?:\([^)]*\)\s*)?[—\-·]\s*(.*)$'), 'AG')
parse_find('FIND_week.md', re.compile(r'^### (WEEK-\d{3})\s*[—\-·]\s*(.*)$'), 'WEEK')
for e in entries.values():
    e['body'] = '\n'.join(e['body']).strip()

maps = []
def parse_maps(name, label_re, fileid, home_from):
    lines = read(name)
    cur = None
    section_home = None
    for i, ln in enumerate(lines, 1):
        hm = re.match(r'^#{2,3} ((?:S6|AG|WEEK)-\d{3})\b', ln)
        if hm:
            section_home = hm.group(1)
        m = label_re.match(ln)
        if m:
            if cur:
                cur['line_end'] = i - 1
                maps.append(cur)
            cur = {'mid': fileid + ':' + m.group(1), 'file': name, 'line_start': i, 'line_end': None,
                   'label': m.group(1), 'rest0': m.group(2), 'text': [m.group(2)], 'section_home': section_home}
            continue
        if cur is not None:
            if ln.strip() == '' or ln.startswith('#') or ln.startswith('- **') or ln.startswith('---') or ln.startswith('|'):
                cur['line_end'] = i - 1
                maps.append(cur)
                cur = None
                continue
            cur['text'].append(ln.strip())
    if cur:
        cur['line_end'] = len(lines)
        maps.append(cur)

parse_maps('MAPS_from_s6.md', re.compile(r'^- \*\*\[(\d{3}\.\d+)\]\*\*\s*(.*)$'), 'S6m', 'label')
parse_maps('MAPS_from_ag.md', re.compile(r'^- \*\*(M\d{3})\*\*\s*(.*)$'), 'AGm', 'section')
parse_maps('MAPS_from_week.md', re.compile(r'^- \*\*(M\d{3}\.\d+)\*\*\s*(.*)$'), 'WKm', 'label')

for mp in maps:
    text = ' '.join(mp['text'])
    mp['text'] = text
    r0 = mp['rest0']
    if mp['mid'].startswith('S6m'):
        mp['home'] = 'S6-' + mp['label'].split('.')[0]
        arrow = r0.split('·')[0]
        t = re.search(r'·\s*\*([^*]+)\*', r0)
        mp['type'] = t.group(1).strip() if t else ''
    elif mp['mid'].startswith('AGm'):
        mp['home'] = mp['section_home']
        t = re.match(r'\s*\[([^\]]+)\]\s*(.*)$', r0)
        if t:
            mp['type'] = t.group(1).strip()
            after = t.group(2)
        else:
            mp['type'] = ''
            after = r0
        # arrow part: up to first '.' followed by space or ':' (ids at the start)
        cut = re.split(r'(?<=[^0-9A-Z\-])[.:](?=\s)', after, maxsplit=1)
        arrow = cut[0]
    else:
        mp['home'] = 'WEEK-' + mp['label'][1:].split('.')[0]
        t = re.search(r'\[([^\]]+)\]', r0)
        mp['type'] = t.group(1).strip() if t else ''
        arrow = r0.split('[')[0]
    mp['arrow_ids'] = sorted(set(a + '-' + b for a, b in ID_RE.findall(arrow)))
    mp['all_ids'] = sorted(set(a + '-' + b for a, b in ID_RE.findall(text)))
    del mp['rest0']

with open(os.path.join(OUT, 'entries.json'), 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=0)
with open(os.path.join(OUT, 'maps.json'), 'w', encoding='utf-8') as f:
    json.dump(maps, f, ensure_ascii=False, indent=0)

st = []
st.append('entries: %d (S6 %d, AG %d, WEEK %d)' % (len(entries), sum(e['dossier']=='S6' for e in entries.values()),
          sum(e['dossier']=='AG' for e in entries.values()), sum(e['dossier']=='WEEK' for e in entries.values())))
c = collections.Counter(mp['mid'].split(':')[0] for mp in maps)
st.append('maps: %d %s' % (len(maps), dict(c)))
st.append('maps with no home: %d' % sum(1 for mp in maps if not mp['home']))
st.append('maps with empty arrow ids: %d' % sum(1 for mp in maps if not mp['arrow_ids']))
tc = collections.Counter()
for mp in maps:
    tc[(mp['mid'].split(':')[0], mp['type'][:40])] += 1
st.append('types:')
for k, v in sorted(tc.items(), key=lambda x: -x[1]):
    st.append('  %s\t%s\t%d' % (k[0], k[1], v))
# missing entries
for prefix, n in (('S6', 125), ('AG', 126), ('WEEK', 153)):
    miss = [prefix + '-%03d' % i for i in range(1, n + 1) if prefix + '-%03d' % i not in entries]
    st.append('missing %s: %s' % (prefix, miss))
# entries never reached by any map
reached = set()
for mp in maps:
    reached.update(mp['all_ids'])
    if mp['home']:
        reached.add(mp['home'])
st.append('entries in no map: %s' % sorted(set(entries) - reached))
with open(os.path.join(OUT, 'stats.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(st))
print('\n'.join(st[:6]))
