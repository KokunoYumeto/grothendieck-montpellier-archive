# Row-by-row verdict table for the intake of RESEARCH_SA08_C3_D031 (checkpoint 08), from the sorted register.
# Claude Opus 5.5 at effort max, agent a34c04448e8299803, 20 Nov 2026. Prints Markdown; the intake appends it.
import csv, sys
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')
T = 'C:/Users/user/Documents/field_experts/intake_20261120/SORTED/RESEARCH_SA08_C3_D031.tsv'
rows = list(csv.DictReader(open(T, encoding='utf-8', newline=''), delimiter='\t'))
V = {
    'B-001': 'confirmed: targeted proof check of the proof in full, and the statement checked against the source '
             '(arXiv:2511.22614v4, Section 2.1, Prop. 3.10 and its proof)',
    'B-006': 'reach of D-031 confirmed against the source (Thm 3.15 assumes a quasi-isomorphism; its visible proof '
             'does not use Prop. 3.10); the comparison proof itself not read in full',
    'B-008': 'reach of D-031 confirmed as for B-006; the proof itself not read in full',
}
cell = lambda s: ' '.join((s or '').replace('|', '/').split())
out = ['| id | run status | statement | proof at | the run\'s check events | intake verdict |',
       '|---|---|---|---|---|---|']
cnt = Counter()
for r in rows:
    v = V.get(r['row_id'], 'not read in full: statement level, with the run\'s own check events')
    cnt['read in full' if r['row_id'] == 'B-001' else ('partly checked' if r['row_id'] in V else 'statement level')] += 1
    out.append('| %s | %s | %s | %s | %s | %s |' % (r['row_id'], cell(r['run_status']), cell(r['statement'])[:240],
               cell(r['proof_at']).split(' ')[0], cell(r['check_events'])[:80], v))
print('\n'.join(out))
print()
print('Counts:', dict(cnt), '; run status:', dict(Counter(cell(r['run_status']).split(' ')[0] for r in rows)))
