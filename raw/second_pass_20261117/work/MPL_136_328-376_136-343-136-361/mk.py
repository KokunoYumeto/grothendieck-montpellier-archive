import sys, re, collections
# usage: mk.py LOG.md out_changes.md block_name
log, out, block = sys.argv[1], sys.argv[2], sys.argv[3]
rows, unres, notes, nochange = [], [], [], []
for line in open(log, encoding='utf-8'):
    line = line.rstrip('\n')
    if not re.match(r'^\d{3} \|', line):
        continue
    f = [x.strip() for x in line.split(' | ')]
    scan, place = f[0], f[1]
    if place.startswith('unresolved'):
        txt = f[2] if f[2] != '-' else ''
        ev = f[4] if len(f) > 4 and f[4] not in ('-', 'not settled', 'not decided', 'not settled on enlargement') else ''
        unres.append((scan, '; '.join(x for x in (txt, ev) if x)))
    elif place.startswith('note') or place.startswith('(no change)') or place.startswith('(page)'):
        notes.append((scan, ' — '.join(x for x in f[1:] if x and x != '-')))
    else:
        rows.append(f)
conf = collections.Counter()
def esc(s):
    return s.replace('|', '\\|')
with open(out, 'w', encoding='utf-8', newline='\n') as o:
    o.write('# Changes, block ' + block + '\n\n')
    o.write('Second pass by Claude Opus 5.5 at effort max (agent aa2156d1c23970b0d), 19 Nov 2026, against the scan images '
            '(both halves of every scan read; enlarged crops where a reading was in doubt, kept in '
            '`second_pass/work/' + block + '/`). The first pass is GPT-6 Astra (ChatGPT Pro mode), run MPL_136_328-376, '
            'checkpoint 02. Further witnesses named where they agree: Codex Work K136-01..03 (GPT-6.2 Astra at Max), '
            'and the sweep-3 reading `results_register/horizontal/sweep3/SA08/readings/136_282-376.md`.\n\n')
    o.write('| scan | place | first-pass reading | corrected reading | evidence (what the image shows) | confidence |\n')
    o.write('|---|---|---|---|---|---|\n')
    for f in rows:
        c = f[5] if len(f) > 5 else ''
        for part in c.split(';'):
            part = part.strip()
            if part in ('high', 'medium', 'low'):
                conf[part] += 1
        o.write('| ' + ' | '.join(esc(x) for x in f[:6]) + ' |\n')
    o.write('\n## Places still unresolved\n\n')
    for s, t in unres:
        o.write('- ' + s + ': ' + t + '\n')
    if notes:
        o.write('\n## Scans checked without change, and readings confirmed\n\n')
        for s, t in notes:
            o.write('- ' + s + ': ' + t + '\n')
print('rows', len(rows), 'conf', dict(conf), 'unresolved', len(unres), 'notes', len(notes))
