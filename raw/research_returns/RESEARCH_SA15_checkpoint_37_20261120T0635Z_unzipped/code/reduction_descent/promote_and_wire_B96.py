from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib
own=Path(__file__).resolve().parents[1];root=own.parents[1]
stem='B_full_Iwahori_selected_point'
expected='a56221d040b93f4550b5dcd1cd78fe0ad8dcd833aba3020ed04299da5157778e'
h=lambda b:hashlib.sha256(b).hexdigest()
p=own/(stem+'_candidate.tex');raw=p.read_bytes();assert h(raw)==expected
rp=root/'outputs/root_B96_audit.json';cp=own.parent/'obstructions_crystals/B96_independent_audit.json'
r=json.loads(rp.read_text());c=json.loads(cp.read_text())
for a in (r,c):
 assert 'PASS' in a['status'] and a['candidate_sha256']==expected
 assert a['author_bytes_unchanged'] and a['all_mathematical_output_identical']
prior=own/'notes'/f'{stem}.prepromotion.tex';can=own/f'{stem}.tex';rec=own/'outputs/B96_promotion.json'
assert not prior.exists() and not can.exists() and not rec.exists()
prior.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion audits passed.}',raw.decode())
s=s.replace(s.splitlines()[0],'% Proved after complete root and companion audits; exact candidate retained.',1)
before='If proved, this removes the remaining residual-wild branch rather\n'
assert s.count(before)==1
s=s.replace(before,'This removes the remaining residual-wild branch rather\n')
para=r'''
\smallskip
\noindent\emph{Independent audits.}
The complete root and companion six-assertion proof and exact-code
audits passed. Their unchanged isolated reruns took
\(%s\) and \(%s\) seconds, respectively,
preserving the author source and output. Both rederived the selected
quotient-point stabilizers and normality, the exact opposite-field
characters and Herbrand restriction, and every coefficient boundary
of the final gap argument. The total-ramification scope repair was
read explicitly. The complete invoked internal proofs were reread;
the companion additionally reread the retained original Colmez
3.7--3.13 proofs. Neither audit claims a new external-source opening.
Exact candidate versions, the scope repair, all executed code and
outputs, independent audit records and the promotion diff are retained.
'''%(r['independent_runtime_seconds'],c['independent_runtime_seconds'])
assert s.count(r'\end{remark}')==1
s=s.replace(r'\end{remark}',para+r'\end{remark}')
can.write_text(s)
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert len(labels)==6 and labels==r['labels']==c['labels']
now=datetime.now(timezone.utc).isoformat()
scope='All nontrivial residual-wild actual125 comparisons of whole potentially supersingular height-two groups with different finite special characters at p5,e20 are excluded. The irreducible-residual image orders5^5..5^8 and the unrestricted least-index alternative{2,3} remain open. No comparison realization is inferred.'
pr={'status':'PROVED','promotion_utc':now,'canonical':str(can),'canonical_sha256':h(can.read_bytes()),'audited_candidate_sha256':expected,'preserved_candidate':str(prior),'labels':labels,'scope':scope,'root_audit':str(rp),'root_audit_utc':r['actual_utc'],'root_runtime_seconds':r['independent_runtime_seconds'],'companion_audit':str(cp),'companion_audit_utc':c['actual_utc'],'companion_runtime_seconds':c['independent_runtime_seconds'],'author_runtime_seconds':11.402156060998095,'canonical_change_scope':'Statuses, leading provenance comment, proved-scope wording and exact audit paragraph only. The audited mathematical proof is unchanged.','scope_delta':'notes/B96_total_ramification_scope_repair/record.json','executed_failures':[],'source_scope':'Complete retained internal proofs read; companion reread retained original Colmez3.7--3.13. No new external source opening claimed.'}
rec.write_text(json.dumps(pr,indent=2)+'\n')
(own/'notes/B96_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),s.splitlines(True),fromfile=p.name,tofile=can.name)))
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',scope,stem+'.tex;outputs/B96_promotion.json','Complete root and companion proof/code audits; exact author bytes and all prior proof versions retained'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:f.write(f'\n## {now} — B96 promoted\n\n{scope}\n')
hist=own/'notes/CP36_before_B96_wiring';hist.mkdir()
con=root/'code/consolidate.py';cfg=root/'notes/checkpoint36_promoted_inputs.json'
oc=con.read_text();oj=cfg.read_text()
(hist/'consolidate.py').write_text(oc);(hist/cfg.name).write_text(oj)
anchor="'B_remaining_tracefree_rows.tex']"
assert oc.count(anchor)==1 and stem+'.tex' not in oc
nc=oc.replace(anchor,"'B_remaining_tracefree_rows.tex',\n                    '"+stem+".tex']")
items=json.loads(oj);path='agents/reduction_descent/'+stem+'.tex'
assert path not in items;items.append(path);nj=json.dumps(items,indent=2)+'\n'
compile(nc,str(con),'exec');con.write_text(nc);cfg.write_text(nj)
(hist/'consolidate.diff').write_text(''.join(difflib.unified_diff(oc.splitlines(True),nc.splitlines(True),fromfile='before/consolidate.py',tofile='after/consolidate.py')))
(hist/'config.diff').write_text(''.join(difflib.unified_diff(oj.splitlines(True),nj.splitlines(True),fromfile='before/'+cfg.name,tofile='after/'+cfg.name)))
w={'status':'WIRED_CP36','actual_utc':datetime.now(timezone.utc).isoformat(),'canonical':path,'canonical_sha256':h(can.read_bytes()),'consolidate_before_sha256':h(oc.encode()),'consolidate_after_sha256':h(con.read_bytes()),'config_before_sha256':h(oj.encode()),'config_after_sha256':h(cfg.read_bytes()),'prior_directory':str(hist),'scope':'Single B96 include after B95 and single CP36 required-input addition. Current primitive, product and earlier promoted inputs preserved. No updater/report/build mutation.'}
(own/'outputs/B96_CP36_wiring.json').write_text(json.dumps(w,indent=2)+'\n')
print(json.dumps({'promotion':pr,'wiring':w},indent=2))
