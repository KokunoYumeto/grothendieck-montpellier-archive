"""Integrate eight audited inputs without counting them as main-gate movement."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
manifest_paths = [
    'parts/C/post18_research/integration_manifest_C_reduction_cycles.json',
    'parts/D/post18_research/integration_manifest_Cartier_parameters_root.json',
    'parts/D/post18_research/integration_manifest_residual_Frobenius_D.json',
    'parts/B/post18_research/integration_manifest_B_post18.json',
]
manifests = [json.loads((root/p).read_text()) for p in manifest_paths]
for i,m in enumerate(manifests):
    if 'files' not in m: continue
    assert len(m['files']) == 1
    f = m['files'][0]
    assert f['status'] == 'Proved'
    b = dict(f['bibliography'])
    b['sha256'] = hashlib.sha256((root/b['path']).read_bytes()).hexdigest()
    manifests[i] = dict(path=f['path'],sha256=f['sha256'],labels=f['labels'],
        recorded_utc=f['promoted_utc'],bibliography=b,
        audit_scope={a['auditor']:a['scope'] for a in f['audits']},
        scope_precision=f['audit_scope'],movement_classification='Auxiliary qualified family realization; no main-gate movement.')
pattern = re.compile(r'\\begin\{(proposition|corollary|lemma|theorem)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
columns = ['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
p = root/'parts/D/results_D.csv'
with p.open() as f: rows = list(csv.DictReader(f))
known = {r['id'] for r in rows}
added = []; labels = []; files = []; new_events = []
for m in manifests:
    assert set(m['audit_scope']) == {'root','B','C','D'}
    p = root/m['path']; source = p.read_text()
    assert hashlib.sha256(p.read_bytes()).hexdigest() == m['sha256']
    units = list(pattern.finditer(source))
    assert {u[3] for u in units} == set(m['labels'])
    assert all(u[2].startswith(('Proved:', 'Known correspondence:','Known:','Proved under')) for u in units)
    files.append(dict(path=m['path'],sha256=m['sha256']))
    for u in units:
        labels.append(u[3])
        if u[3] in known: continue
        scope = m['scope_precision']
        if isinstance(scope,list): scope = ' '.join(scope)
        status = 'Known' if u[2].startswith('Known') else 'Proved under stated hypotheses'
        rows.append(dict(id=u[3],statement=u[2].split(':',1)[1].strip(),status=status,
            where_proved=m['path']+': label '+u[3],
            depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}',source)))),
            manuscript_pages='29/061,066',notes=scope+' Four complete actual-file/source audits. '+
            m.get('movement_classification',m.get('movement','Auxiliary; no main movement.'))))
        added.append(u[3]);known.add(u[3])
        for actor,audit in m['audit_scope'].items():
            who='/root' if actor=='root' else '/root/part_'+actor.lower()
            new_events.append(dict(statement_id=u[3],date=m['recorded_utc'],
                who='GPT-6 Astra Pro; '+who+'; SA12 run1; effort setting not independently exposed',
                type='targeted proof check',outcome='PASS: '+audit))
    p=root/'parts/D/paper_D.tex';s=p.read_text();line='\\input{'+m['path']+'}'
    if line not in s:p.write_text(s+'\n'+line+'\n')
    b=m['bibliography']
    if isinstance(b,str):b=dict(path=b,sha256=m['bibliography_sha256'],keys=m['bibliography_keys'])
    bp=root/b['path'];bs=bp.read_text()
    assert hashlib.sha256(bp.read_bytes()).hexdigest()==b['sha256']
    assert 'Opened' in bs
    p=root/'parts/D/references_D.bib';s=p.read_text()
    old=set(re.findall(r'@\w+\{([^,]+),',s))
    assert not(set(b['keys'])&old) or set(b['keys'])<=old
    if not set(b['keys'])<=old:p.write_text(s+'\n'+bs)
    if 'certificate' in m and isinstance(m['certificate'],dict) and added:
        cert=m['certificate']
        if 'D:residual-twisted-Frobenius-transport' in added:
            for actor,key in [('D','author_seconds'),('root','root_seconds'),('B','B_seconds'),('C','C_seconds')]:
                who='/root' if actor=='root' else '/root/part_'+actor.lower()
                new_events.append(dict(statement_id='D:residual-twisted-Frobenius-transport',date=m['recorded_utc'],
                    who='GPT-6 Astra Pro; '+who+'; SA12 run1; effort setting not independently exposed',
                    type='computation or formal certificate',
                    outcome='PASS: independent actual execution of '+cert['source']+'; '+str(cert['assertions'])+
                        ' assertions; '+str(cert[key])+' seconds. '+cert['scope']))
assert len(labels)==8
with (root/'parts/D/results_D.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=columns);w.writeheader();w.writerows(rows)
p=root/'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f:events=list(csv.DictReader(f,delimiter='\t'))
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    w.writeheader();w.writerows(events+new_events)

p=root/'parts/D/unresolved_D.tex';s=p.read_text();marker='% Post-checkpoint18 geometric realization inputs'
if marker not in s:
    s+='\n\n'+marker+r'''
\paragraph{Known reduction cycles and the qualified relative realization.}
Proposition~\ref{D:energy-controlled-reduction-cycle} shows that
the established degree-linear energy cycles already satisfy the
Kahn--Gavran hypotheses. The exact known pointwise correspondence
is recorded in Theorem~\ref{D:reduction-cycle-full-module-correspondence},
with the actual first-step marking action and characteristic-free
proof scope checked. It gives no prescribed-arrow lifting.
Theorem~\ref{D:Artinian-full-neighbourhood-realization} supplies
actual Artinian module families when an explicit second-neighbourhood
bundle, cohomological freeness and base change, and a split injective
boundary are retained. Corollary~\ref{D:Artinian-canonical-two-level-jets}
recovers their module jets and proves base change of that recovered
quotient, without asserting base change of the raw section image.
Effective equations for the required strata and compatible arrows,
with the desired variable and degree bounds, remain unresolved.

\paragraph{Exact one-curve depth and the residual twisted category.}
Proposition~\ref{D:single-curve-Cartier-parameter-ideal} chooses
one separating parameter pair inside the fixed defect ideal whose
pullback is a fixed multiple of the sole exceptional curve.
Corollary~\ref{D:single-curve-Cartier-module-jet-recovery} therefore
identifies the actual recovery thickenings on every etale-resolution
cover with fixed Cartier multiples, independently of cover degree.
Propositions~\ref{D:residual-twisted-spectral-category} and
\ref{D:residual-twisted-Frobenius-transport} describe the residual
twisted category at composite scalar order and its precise
Frobenius transport, retaining the possibly nonidentity final
torsor automorphism. Neither these curve statements nor the
Cartier-depth bridge provides the missing global normal-direction
Frobenius atlas. No unbounded-period count or main-gate reduction
is inferred from these eight inputs.
'''
p.write_text(s)
p=root/'code/assemble.py';s=p.read_text()
paragraph=('Eight additional audited inputs are assembled after checkpoint18. '
 'The existing linear-energy cycles are reduction cycles; the known Kahn--Gavran '
 'correspondence has a complete scope and marking-action verification. Qualified '
 'Artinian second-neighbourhood data realize actual flat MCM families and their '
 'recovered module-jet quotient commutes with coefficient base change. In the '
 'one-curve case, a fixed separating pencil identifies every recovery thickening '
 'on an etale-resolution cover with a fixed Cartier multiple. The composite-order '
 'residual twisted category has exact Frobenius transport, including a possibly '
 'nonidentity final torsor translation. All four proof/source audits passed; four '
 'independent executions of the24066-assertion finite label/carry certificate passed. '
 'Its arithmetic scope excludes gerbe geometry. Cohomology-stratum equation bounds, '
 'specified arrows, normal-direction realization and the required representation '
 'count remain open. These results do not change a requested row or the strongest '
 'main gate, and are not formal-review movement.')
if paragraph not in s:s=s.replace("'','## Files and continuation','',",repr(paragraph)+",\n'','## Files and continuation','',")
p.write_text(s)
record=dict(utc=now,labels=labels,added_rows=len(added),added_events=len(new_events),files=files,
    additional_independent_movement_events=0,requested_status_changes=[],archive_created=False)
(root/'code/output/integrate_post18_geometric_inputs.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
