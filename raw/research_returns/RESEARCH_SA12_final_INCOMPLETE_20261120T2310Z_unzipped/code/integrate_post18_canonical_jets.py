"""Integrate the two fully audited pointwise canonical-module jet results."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
relative = 'parts/B/post17_research/D_canonical_module_two_level_jets_B.tex'
source_path = root / relative
digest = hashlib.sha256(source_path.read_bytes()).hexdigest()
assert digest == 'b702dcf49019bbbd340b0a37c9fb5d13269d0d2178661e328589cbf473e4bf5b'
source = source_path.read_text()
manifest = json.loads((root/'parts/B/post17_research/integration_manifest_B_post17.json').read_text())
entry = next(x for x in manifest['files'] if x['path'] == relative)
assert entry['sha256'] == digest and entry['status'] == 'Proved'
audits = {x['auditor']: x for x in manifest['canonical_jets_audits']}
assert set(audits) == {'root','B','C','D'}
for actor, path in [
    ('C','parts/C/post17_research/audit_B_two_level_module_jets_C.json'),
    ('D','parts/D/post17_research/audit_canonical_module_two_level_jets_D.json')]:
    record = json.loads((root/path).read_text())
    assert digest in json.dumps(record), (actor, 'final-file confirmation required')

pattern = re.compile(r'\\begin\{(lemma|proposition)\}\[Proved: ([^\]]+)\]\s*\\label\{([^}]+)\}')
units = list(pattern.finditer(source))
assert len(units) == 2 and {x[3] for x in units} == set(entry['labels'])
columns = ['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
p = root/'parts/D/results_D.csv'
with p.open() as f: rows = list(csv.DictReader(f))
known = {x['id'] for x in rows}
added = []
events = []
for u in units:
    if u[3] in known: continue
    rows.append(dict(id=u[3],statement=u[2],status='Proved',where_proved=relative+': label '+u[3],
        depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}',source)))),
        manuscript_pages='29/061,066',notes='Exact pointwise recovery for actual reflexive modules on finite punctured surface covers. Uniform level and O(nr) cohomology. No arbitrary-family effectiveness or base change of images. All four full actual-file and exact primary-source audits; final-byte confirmations retained. Auxiliary, no main-gate movement.'))
    added.append(u[3])
    for actor, audit in audits.items():
        who = '/root' if actor == 'root' else '/root/part_'+actor.lower()
        scope = audit['scope']
        if actor in ('C','D'):
            scope += ' Historical prepromotion hash and subsequent fresh complete final-file confirmation are both retained; only one leading comment and two status headings changed.'
        if actor == 'root':
            scope += ' Root freshly reread all final-file proof bytes at13:41UTC after checkpoint18.'
        events.append(dict(statement_id=u[3],date=now,
            who='GPT-6 Astra Pro; '+who+'; SA12 run1; effort setting not independently exposed',
            type='targeted proof check',outcome='PASS; event consolidation time, actual audit scopes retained: '+scope))
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=columns);w.writeheader();w.writerows(rows)
p=root/'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f: old_events=list(csv.DictReader(f,delimiter='\t'))
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    w.writeheader();w.writerows(old_events+events)
p=root/'parts/D/paper_D.tex';s=p.read_text();line='\\input{'+relative+'}'
if line not in s:p.write_text(s+'\n'+line+'\n')
bib=(root/'parts/B/post17_research/references_canonical_jets_B.bib').read_text()
assert 'Opened:' in bib
p=root/'parts/D/references_D.bib';s=p.read_text()
if '@misc{StacksCanonicalJetsB,' not in s:p.write_text(s+'\n'+bib)
p=root/'parts/D/unresolved_D.tex';s=p.read_text();marker='% Post-checkpoint18 exact canonical module jets'
if marker not in s:
    s+='\n\n'+marker+r'''
\paragraph{Actual module jets from two proper thickenings.}
Lemma~\ref{D:canonical-pullback-uniform-jet-loss} and
Proposition~\ref{D:canonical-module-two-level-recovery}
recover the fixed jets of every actual reflexive module from the
image of sections on two consecutive parameter-ideal thickenings.
The fixed level is independent of cover degree and module rank,
and both section and cohomology dimensions are $O(nr)$.
These thickenings can have embedded zero-dimensional structure.
No base-change property of the section images or realization
of an arbitrary chart family is inferred. Effective object and
arrow diagrams with the required equation-degree budget remain
the missing counting input. These two results are auxiliary.
'''
p.write_text(s)
p=root/'code/assemble.py';s=p.read_text()
old='Two additional fully audited auxiliary statements are preserved separately from certified build113 in checkpoint18:'
new='Two additional fully audited auxiliary statements, preserved separately from certified build113 in checkpoint18, are now assembled in the continuing manuscript:'
assert old in s;s=s.replace(old,new,1);p.write_text(s)
record=dict(utc=now,labels=entry['labels'],added_rows=len(added),added_events=len(events),
    path=relative,sha256=digest,final_mathematical_bytes_identical_to_independent_audits=True,
    exact_status_only_hash_transition=dict(before='8b67958fe3cacb2087ea1f24d38d44354cab152030a459be138fee10319a8b85',after=digest),
    additional_main_movement_events=0,archive_created=False)
(root/'code/output/integrate_post18_canonical_jets.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
