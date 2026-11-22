"""Integrate three fully audited finite models; no main-gate movement."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,re
root=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
out=root/'code/output/integrate_post18_finite_models.json';assert not out.exists()
paths=['parts/C/post18_research/integration_manifest_C_finite_Hom.json','parts/D/post18_research/integration_manifest_twisted_depth_D.json']
cols=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
with (root/'parts/D/results_D.csv').open() as f:rows=list(csv.DictReader(f))
known={x['id'] for x in rows};added=[];new_events=[];files=[]
pattern=re.compile(r'\\begin\{(proposition|corollary|lemma|theorem)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
for path in paths:
 m=json.loads((root/path).read_text());assert set(m['audit_scope'])=={'root','B','C','D'}
 p=root/m['path'];source=p.read_text();assert hashlib.sha256(p.read_bytes()).hexdigest()==m['sha256']
 units=list(pattern.finditer(source));assert {u[3] for u in units}==set(m['labels'])
 assert all(u[2].startswith(('Proved:','Proved under')) for u in units)
 scope=m.get('scope_precision',m.get('scope',[]));scope=' '.join(scope) if isinstance(scope,list) else scope
 movement=m.get('movement_classification',m.get('movement','Auxiliary; no main-gate movement.'))
 for u in units:
  assert u[3] not in known,u[3]
  rows.append(dict(id=u[3],statement=u[2].split(':',1)[-1].strip(),status='Proved under stated hypotheses',where_proved=m['path']+': label '+u[3],depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}',source)))),manuscript_pages='29/061,066',notes=scope+' Four full actual-file/source audits. '+movement))
  known.add(u[3]);added.append(u[3])
  for actor,audit in m['audit_scope'].items():
   who='/root' if actor=='root' else '/root/part_'+actor.lower()
   new_events.append(dict(statement_id=u[3],date=m['recorded_utc'],who='GPT-6 Astra Pro; '+who+'; SA12 run1; effort setting not independently exposed',type='targeted proof check',outcome='PASS: '+str(audit)))
 p=root/'parts/D/paper_D.tex';s=p.read_text();line='\\input{'+m['path']+'}';assert line not in s;p.write_text(s+'\n'+line+'\n')
 b=m['bibliography'];b=dict(path=b,sha256=m['bibliography_sha256'],keys=m['bibliography_keys']) if isinstance(b,str) else b
 bp=root/b['path'];bs=bp.read_text();assert hashlib.sha256(bp.read_bytes()).hexdigest()==b['sha256'];assert 'Opened' in bs
 p=root/'parts/D/references_D.bib';s=p.read_text();old=set(re.findall(r'@\w+\{([^,]+),',s));assert not(set(b['keys'])&old);p.write_text(s+'\n'+bs)
 files.append({'path':m['path'],'sha256':m['sha256']})
assert len(added)==3
with (root/'parts/D/results_D.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
p=root/'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f:events=list(csv.DictReader(f,delimiter='\t'))
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events+new_events)
p=root/'parts/D/unresolved_D.tex';s=p.read_text();s+=r'''

\paragraph{Finite map models and twisted normal depth.}
Proposition~\ref{D:fixed-determinant-finite-Hom} constructs actual
polynomial models for maps, composition, equality and inverse witnesses
on a fixed Cohen--Macaulay curve, for all coefficient algebras. Its
constant-degree formulas and hereditary coordinate budget do not give
bounded equations for the required coflat object strata or arbitrary
prescribed surface arrows.
Lemma~\ref{D:twisted-connected-anchor-minimal-slopes} constructs a
mixed-band formal anchor and normalized twisted lattices when the
residual spectral torsor is connected. Its Euler quotient has precisely
the spectral rank, giving a slope window of width independent of the
period. Proposition~\ref{D:twisted-period-independent-normal-depth}
then gives fixed original-curve pole and map-lifting depths, including
actual Artinian families, and quadratic Hom cohomology. A finite
graded object/arrow atlas with uniformly bounded equation degrees is
still missing. These three inputs leave every strongest main gate
unchanged; no unbounded-period representation count follows from them.
''';p.write_text(s)
p=root/'code/assemble.py';s=p.read_text()
para=('Three further audited finite models are assembled after checkpoint18. Fixed-determinant curve presentations now have explicit all-coefficient finite Hom complexes with differential degree at most two, composition degree at most five, and exact boundary/inverse witnesses. A connected mixed-band spectral cover admits a formal anchor selecting twisted lattices with a period-independent slope-window width. Their maps have bounded original-curve poles and lift from a fixed thickening; actual Artinian families and a quadratic Hom-cohomology budget are included. Every actual file and its primary inputs passed four proof audits. These results do not supply the missing effective coflat or graded normal-direction atlas and do not prove a new representation count. They do not constitute formal-review movement.')
assert para not in s;s=s.replace("'','## Files and continuation','',",repr(para)+",\n'','## Files and continuation','',");p.write_text(s)
r=dict(utc=now,labels=added,added_rows=len(added),added_events=len(new_events),files=files,additional_independent_movement_events=0,requested_status_changes=[],archive_created=False)
out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
