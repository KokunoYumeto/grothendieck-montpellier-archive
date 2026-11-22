# Appends check events to INTAKE_RESEARCH_SA05_20261121_full_CHECK_EVENTS.tsv from a batch file.
# Batch file lines: id || type || outcome   (lines starting with # are skipped)
# Usage: python -I -B add_events.py batchNN.txt
import os, sys, datetime
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(os.path.dirname(here), 'INTAKE_RESEARCH_SA05_20261121_full_CHECK_EVENTS.tsv')
WHO = 'Claude Opus 5.5 at effort max, agent a7b7747fd6dd29f87, full intake of the RESEARCH_SA05 final (GPT-6 Astra, ChatGPT Pro mode, 19 Nov 2026)'
TYPES = {'targeted proof check', 'independent re-proof', 'computation or formal certificate', 'used and rechecked in this run',
         'carried as background without fault found', 'refuted, with the refined statement'}
ids = [l.strip() for l in open(os.path.join(here, 'ids.txt'), encoding='utf-8') if l.strip()]
new = not os.path.exists(out)
seen = set()
if not new:
    for l in open(out, encoding='utf-8').read().splitlines()[1:]:
        if l.strip():
            seen.add(l.split('\t')[1])
n0 = 0 if new else sum(1 for _ in open(out, encoding='utf-8')) - 1
rows = []
for l in open(sys.argv[1], encoding='utf-8'):
    l = l.strip()
    if not l or l.startswith('#'):
        continue
    p = [x.strip() for x in l.split(' || ')]
    assert len(p) == 3, l[:80]
    sid, typ, outc = p
    assert sid in ids, 'unknown id ' + sid
    assert any(typ.startswith(t) for t in TYPES), 'bad type ' + typ
    rows.append((sid, typ, outc.replace('\t', ' ')))
date = datetime.datetime.utcnow().strftime('%Y-%m-%d')
with open(out, 'a', encoding='utf-8', newline='\n') as f:
    if new:
        f.write('id\tstatement_id\tdate_utc\twho\ttype\toutcome\n')
    for k, (sid, typ, outc) in enumerate(rows, n0 + 1):
        f.write('\t'.join(['SA05F-E%03d' % k, sid, date, WHO, typ, outc]) + '\n')
done = seen | {r[0] for r in rows}
print('appended', len(rows), '; ids covered', len(done), 'of', len(ids), '; next uncovered:', [i for i in ids if i not in done][:5])
