from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib
own=Path(__file__).resolve().parents[1];root=own.parents[1]
stem='B_irreducible_point_field_layers'
expected='964d658fac540f02d87163941e0076b7321c5e71513e467f46f80124c26be9ae'
h=lambda b:hashlib.sha256(b).hexdigest()
p=own/(stem+'_candidate.tex');raw=p.read_bytes();assert h(raw)==expected
rp=root/'outputs/root_B97_audit.json'
cp=own.parent/'monodromy/outputs/independent_B97_point_field_layers_audit.json'
r=json.loads(rp.read_text());c=json.loads(cp.read_text())
for a in (r,c):assert 'PASS' in a['status'] and a['candidate_sha256']==expected
rr=r['isolated_runs'][0];cr=c['isolated_run']
assert rr['author_bytes_unchanged'] and rr['all_mathematical_output_identical']
assert cr['author_before']==cr['author_after'] and all(cr['mathematical_fields_equal'].values())
prior=own/'notes'/f'{stem}.prepromotion.tex';can=own/f'{stem}.tex';rec=own/'outputs/B97_promotion.json'
assert not prior.exists() and not can.exists() and not rec.exists()
prior.write_bytes(raw)
new=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion audits passed.}',raw.decode())
new=new.replace(new.splitlines()[0],'% Proved after complete root and companion audits; exact candidate retained.',1)
para=r'''
\smallskip
\noindent\emph{Independent audits.}
The full root and monodromy companion proof and exact-code audits
passed at 05:32:32.208856 and 05:32:53.522155 UTC on
20 November 2026. Their unchanged isolated reruns took
\(%s\) and \(%s\) seconds,
respectively, with all mathematical outputs identical and the
author bytes preserved. Both rederived all actual point-field,
normality, coefficient-boundary, conductor and Lie-algebra steps.
The companion reread the retained original Colmez ramification
proofs on pp.~14--16; neither audit claims a new external opening.
All proof versions, programs, outputs, independent records and
the promotion diff are retained.
'''%(rr['runtime_seconds'],cr['independent_runtime_seconds'])
assert new.count(r'\end{remark}')==1
new=new.replace(r'\end{remark}',para+r'\end{remark}')
can.write_text(new)
labels=re.findall(r'\\label\{([^}]+)\}',new)
assert len(labels)==6 and labels==r['labels']==[x['label'] for x in c['assertions']]
now=datetime.now(timezone.utc).isoformat()
scope='For every p>=5 at e=p(p-1), a different-special-character irreducible-residual actual p^3 comparison must have traceful layers(3,4) or(4,4). All actual second-point degrees are p^2, third-point relative degrees p^2, and terminal conductors satisfy the proved bound. At p5/e20 only orders5^7 and5^8 remain under this result; no exact least-index closure is inferred here.'
pr={'status':'PROVED','promotion_utc':now,'canonical':str(can),'canonical_sha256':h(can.read_bytes()),
 'audited_candidate_sha256':expected,'preserved_candidate':str(prior),'labels':labels,'scope':scope,
 'root_audit':str(rp),'root_audit_utc':r['actual_utc'],'root_runtime_seconds':rr['runtime_seconds'],
 'companion_audit':str(cp),'companion_audit_utc':c['actual_utc'],'companion_runtime_seconds':cr['independent_runtime_seconds'],
 'author_runtime_seconds':1.2538034710014472,
 'canonical_change_scope':'Statuses, leading provenance comment and exact audit paragraph only. Audited mathematical proof unchanged.',
 'executed_failures':[],'source_scope':'Complete invoked proofs reread; companion retained original Colmez14–16 proofs read. No new external-source opening claimed.','shared_wiring':'Pending coordinated window; no shared file modified by this script.'}
rec.write_text(json.dumps(pr,indent=2)+'\n')
(own/'notes/B97_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),new.splitlines(True),fromfile=p.name,tofile=can.name)))
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',scope,stem+'.tex;outputs/B97_promotion.json','Complete root and monodromy companion proof/code audits; exact candidate and author outputs retained'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:f.write(f'\n## {now} — B97 promoted\n\n{scope}\n')
print(json.dumps(pr,indent=2))
