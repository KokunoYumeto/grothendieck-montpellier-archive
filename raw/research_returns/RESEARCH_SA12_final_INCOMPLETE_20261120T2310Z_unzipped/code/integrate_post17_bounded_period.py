"""Assemble the fully audited bounded-geometric-period closure of one reduction."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
m = json.loads((root / 'parts/D/post17_research/integration_manifest_bounded_Brauer_period_D.json').read_text())
assert set(m['audit_scope']) == {'root', 'B', 'C', 'D'}
source_path = root / m['path']
assert hashlib.sha256(source_path.read_bytes()).hexdigest() == m['sha256']
source = source_path.read_text()
pattern = re.compile(r'\\begin\{(proposition|corollary|lemma|example|theorem)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
units = list(pattern.finditer(source))
assert {u[3] for u in units} == set(m['labels'])
assert all(u[2].startswith('Proved:') for u in units)
columns = ['id', 'statement', 'status', 'where_proved', 'depends_on', 'manuscript_pages', 'notes']
p = root / 'parts/D/results_D.csv'
with p.open() as f:
    rows = list(csv.DictReader(f))
known = {r['id'] for r in rows}
added = []
for u in units:
    if u[3] in known:
        continue
    rows.append(dict(id=u[3], statement=u[2].split(':', 1)[1].strip(), status='Proved',
        where_proved=m['path'] + ': label ' + u[3],
        depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}', source)))),
        manuscript_pages='29/061,066',
        notes=m['scope_precision'] + ' Four complete actual-file audits with precise source provenance. '
              + m['movement_classification']))
    added.append(u[3])
with p.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=columns)
    w.writeheader(); w.writerows(rows)
p = root / 'parts/D/paper_D.tex'
s = p.read_text()
line = '\\input{' + m['path'] + '}'
if line not in s:
    p.write_text(s + '\n' + line + '\n')
p = root / 'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f:
    events = list(csv.DictReader(f, delimiter='\t'))
new_events = []
for e in m['events']:
    if e['label'] not in added:
        continue
    actor = '/root' if e['actor'] == 'root' else '/root/part_' + e['actor'].lower()
    new_events.append(dict(statement_id=e['label'], date=e['recorded_utc'],
        who='GPT-6 Astra Pro; ' + actor + '; SA12 run1; effort setting not independently exposed',
        type='targeted proof check', outcome='PASS: ' + e['scope']))
events.extend(new_events)
with p.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['statement_id','date','who','type','outcome'], delimiter='\t')
    w.writeheader(); w.writerows(events)
p = root / 'parts/D/unresolved_D.tex'
s = p.read_text()
s = s.replace('only representations with nonzero geometric Brauer class remain in that\npart of the global normal surface problem.',
    'the bounded-geometric-period closure below further restricts this\npart of the global normal surface problem to unbounded geometric period.')
marker = '% Post-checkpoint17 bounded geometric Brauer period'
if marker not in s:
    s += '\n\n' + marker + r'''
\paragraph{Every fixed geometric period bound.}
Theorem~\ref{D:bounded-geometric-Brauer-period} proves the same
$q^{C_Br^2}$ count when the geometric Brauer class has order at most
a fixed integer $B$, on the stated normal proper surfaces and
complete local surfaces. The finite set of realized classes is killed
on one fixed normal cover obtained from witness representations.
Restriction to that cover and a coset-representative fibre bound
reduce the assertion to the Brauer-zero theorem. Scalar-centre order
is still unrestricted. The constant and the chosen cover may depend
on $B$; no bound uniform in $B$ is proved.
Corollary~\ref{D:bounded-Brauer-period-selected-simple-product}
gives the corresponding selected-kernel product consequence.
This is a finite-cover closure of the same single main reduction,
not another movement event. The projective route still requires
unbounded geometric Brauer period, and the remaining alternating,
cross-characteristic and general-crown gates are unchanged.
'''
p.write_text(s)
p = root / 'code/assemble.py'
s = p.read_text()
paragraph = ('The bounded-geometric-Brauer-period closure is now assembled. For each fixed B, '
    'all realized projective classes of geometric period at most B are killed by one fixed '
    'normal cover, and restriction plus an ambient extension-fibre bound gives q^(C_B r^2) '
    'classes. This holds in the stated normal proper surface and complete normal local '
    'surface scopes; scalar order is unrestricted. The constant may depend on B. Its '
    'selected-simple-product consequence is included. These are closures of the single '
    'reduction counted at review11, and create no additional movement event.')
if paragraph not in s:
    s = s.replace("'','## Files and continuation','',", repr(paragraph) + ",\n'','## Files and continuation','',")
p.write_text(s)
record = dict(utc=now, labels=m['labels'], added_rows=len(added), added_events=len(new_events),
    files=[dict(path=m['path'], sha256=m['sha256'])],
    additional_independent_movement_events=0, requested_status_changes=[], archive_created=False)
(root / 'code/output/integrate_post17_bounded_period.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
