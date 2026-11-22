"""Assemble four audited statements first saved separately in checkpoint17."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re
root=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
dm=json.loads((root/'parts/D/post17_research/integration_manifest_local_Brauer_transfer_D.json').read_text())
bm=json.loads((root/'parts/B/post17_research/integration_manifest_B_post17.json').read_text())
assert set(dm['audit_scope'])=={'root','B','C','D'}
assert {a['auditor'] for a in bm['independent_sparse_DVR_audits']}=={'root','C','D'}
bf=bm['files'][0];files=[{'path':dm['path'],'sha256':dm['sha256']},bf]
pattern=re.compile(r'\\begin\{(proposition|corollary|lemma|example|theorem)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
cols=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
with (root/'parts/D/results_D.csv').open() as f:rows=list(csv.DictReader(f))
known={r['id'] for r in rows};added=[];labels=[]
for info in files:
 p=root/info['path'];source=p.read_text();assert hashlib.sha256(p.read_bytes()).hexdigest()==info['sha256']
 for m in pattern.finditer(source):
  assert m[2].startswith('Proved:');labels.append(m[3])
  if m[3] in known:continue
  note=('All-dimension local closure of the one Brauer-zero reduction. Only Brauer vanishing after the fixed detecting surface pullbacks is assumed; no H2 injection or full-group generation.' if m[3] in dm['labels'] else 'Auxiliary all-ring sparse DVR presentation with finite unpointed Isom witnesses. Fixed residue polynomial; global coefficient poles and constrained surface-extension locus remain uncontrolled.')
  rows.append(dict(id=m[3],statement=m[2].split(':',1)[1].strip(),status='Proved',where_proved=info['path']+': label '+m[3],depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}',source)))),manuscript_pages='29/061,066',notes=note+' Four complete actual-file audits with exact primary-source scope. First archived as separate source in checkpoint17. Not another independent movement event.'))
  known.add(m[3]);added.append(m[3])
 p=root/'parts/D/paper_D.tex';s=p.read_text();line='\\input{'+info['path']+'}'
 if line not in s:p.write_text(s+'\n'+line+'\n')
assert len(labels)==4
with (root/'parts/D/results_D.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
p=root/'parts/D/references_D.bib';s=p.read_text();key='StacksSparseDVRB'
if key not in re.findall(r'@\w+\{([^,]+),',s):p.write_text(s+'\n'+(root/bm['bibliography']).read_text())
p=root/'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f:events=list(csv.DictReader(f,delimiter='\t'))
for e in dm['events']:
 if e['label'] not in added:continue
 actor='/root' if e['actor']=='root' else '/root/part_'+e['actor'].lower()
 events.append(dict(statement_id=e['label'],date=e['recorded_utc'],who='GPT-6 Astra Pro; '+actor+'; SA12 run1; effort setting not independently exposed',type='targeted proof check',outcome='PASS: '+e['scope']))
audits=[{'auditor':'B','scope':bf['scope']}]+bm['independent_sparse_DVR_audits']
for label in bf['labels']:
 if label not in added:continue
 for e in audits:
  actor='/root' if e['auditor']=='root' else '/root/part_'+e['auditor'].lower()
  events.append(dict(statement_id=label,date=bm['promoted_utc'],who='GPT-6 Astra Pro; '+actor+'; SA12 run1; effort setting not independently exposed',type='targeted proof check',outcome='PASS: '+e['scope']+' Consolidated at later assembly; original author/auditor records preserved.'))
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
p=root/'parts/D/unresolved_D.tex';s=p.read_text()
s=s.replace('It leaves nonzero\ngeometric Brauer classes, higher-dimensional local extensions outside\nits hypotheses, and full generation unresolved.', 'Its all-dimension fixed-surface closure is\nCorollary~\\ref{D:local-Brauer-zero-surface-transfer}. It leaves\nnonzero geometric Brauer classes after the fixed surface pullbacks,\nlocal settings outside the stated hypotheses, and full generation unresolved.')
marker='% Post-checkpoint17 sparse DVR and local transfer closure'
if marker not in s:s+='\n\n'+marker+r'''
\paragraph{The local dimensional closure and sparse extension charts.}
Corollary~\ref{D:local-Brauer-zero-surface-transfer} gives the
surface-detected Brauer-zero count on complete excellent normal
equicharacteristic punctures in every dimension. This is a closure
of the earlier count, not a new independent reduction.
Proposition~\ref{D:sparse-DVR-linear-atlas} gives two-generator
finite flat charts and exact finite unpointed Isom witnesses over
arbitrary coefficient rings, including imperfect residue fields.
The normalized different condition gives linear coordinate counts
and polynomial equation degrees in
Corollary~\ref{D:sparse-DVR-normalized-different-complexity}.
The residue polynomial is fixed. Its global poles and those of the
other coefficients remain uncontrolled, as does the degree of the
constrained surface-extension locus. No full cover count follows.
'''
p.write_text(s)
p=root/'code/assemble.py';s=p.read_text();para='Four statements first saved as separate audited source in checkpoint17 are now assembled: the all-dimensional complete-local surface-detected Brauer-zero closure, and three auxiliary sparse-DVR presentation results. The latter allow imperfect primitive residue extensions and prove all-ring flatness and finite unpointed Isom existence with O(n) coordinates and polynomial equation degree under a fixed normalized different bound. Fixed residue polynomials, global coefficient poles and the constrained extension locus remain outside these estimates. This assembly creates no additional independent movement event.'
if para not in s:s=s.replace("'','## Files and continuation','',",repr(para)+",\n'','## Files and continuation','',")
p.write_text(s)
record={'utc':now,'labels':labels,'added_rows':len(added),'files':files,'additional_independent_movement_events':0,'requested_status_changes':[],'archive_created':False}
(root/'code/output/integrate_post17.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
