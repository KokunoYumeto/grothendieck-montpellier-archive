from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib
own=Path(__file__).resolve().parents[1];root=own.parents[1]
stem='B_remaining_tracefree_rows';expected='7967d6fbaffaef6eb32fa250ae9e24d403fd0424ff013bdfd79fbca9e1461a86'
h=lambda b:hashlib.sha256(b).hexdigest()
p=own/(stem+'_candidate.tex');raw=p.read_bytes();assert h(raw)==expected
rp=root/'outputs/root_B95_audit.json';cp=own.parent/'obstructions_crystals/B95_independent_audit.json'
r=json.loads(rp.read_text());c=json.loads(cp.read_text())
for a in [r,c]:
 assert 'PASS' in a['status'] and a['candidate_sha256']==expected
 assert a['author_bytes_unchanged'] and a['all_mathematical_output_identical']
prior=own/'notes'/f'{stem}.prepromotion.tex';can=own/f'{stem}.tex';rec=own/'outputs/B95_promotion.json'
assert not prior.exists() and not can.exists() and not rec.exists();prior.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion audits passed.}',raw.decode())
s=s.replace(s.splitlines()[0],'% Proved after complete root and companion audits; exact candidate retained.',1)
para='''
\\smallskip
\\noindent\\emph{Independent audits.}
The complete root and companion four-assertion proof and exact-code
audits passed. Their literal author-output-preserving reruns took
\\(%s\\) and \\(%s\\) seconds, respectively.
Both rederived the critical coefficient argument, its vanishing
boundary, the actual field filtrations and restrictions, and all
eight symbolic strict gaps. The exact filtration-wording correction
was read in both audits. The complete invoked B94 proof and its
relevant canonical dependencies were reread; no additional external
source opening is claimed. All proof versions, the exact correction,
programs, outputs, independent records and promotion diff are retained.
'''%(r['independent_runtime_seconds'],c['independent_runtime_seconds'])
assert s.count(r'\end{remark}')==1;s=s.replace(r'\end{remark}',para+r'\end{remark}');can.write_text(s)
labels=re.findall(r'\\label\{([^}]+)\}',s);assert len(labels)==4 and labels==r['labels']==c['labels']
now=datetime.now(timezone.utc).isoformat()
scope='All residual-wild layer(3,4) comparisons at p5,e20 are excluded. A surviving residual-wild comparison must have the full actual Iwahori image of order5^9 and layer(4,4). That branch and irreducible residual orders5^5..5^8 remain open; no realization or unrestricted least-index equality is inferred.'
pr={'status':'PROVED','promotion_utc':now,'canonical':str(can),'canonical_sha256':h(can.read_bytes()),'audited_candidate_sha256':expected,'preserved_candidate':str(prior),'labels':labels,'scope':scope,'root_audit':str(rp),'root_audit_utc':r['actual_utc'],'root_runtime_seconds':r['independent_runtime_seconds'],'companion_audit':str(cp),'companion_audit_utc':c['actual_utc'],'companion_runtime_seconds':c['independent_runtime_seconds'],'author_runtime_seconds':0.062296249001519755,'canonical_change_scope':'Statuses, leading provenance comment and exact audit paragraph only; audited mathematical proof unchanged.','wording_delta':'notes/B95_filtration_wording_repair/record.json','executed_failures':[],'source_scope':'Complete retained internal proofs read; no new external source opening claimed.'}
rec.write_text(json.dumps(pr,indent=2)+'\n')
(own/'notes/B95_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),s.splitlines(True),fromfile=p.name,tofile=can.name)))
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',scope,stem+'.tex;outputs/B95_promotion.json','Complete root and companion proof/code audits; exact author bytes and all prior proof versions retained'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:f.write(f'\n## {now} — B95 promoted\n\n{scope}\n')
hist=own/'notes/CP35_before_B95_wiring';hist.mkdir()
con=root/'code/consolidate.py';cfg=root/'notes/checkpoint35_promoted_inputs.json';oc=con.read_text();oj=cfg.read_text()
(hist/'consolidate.py').write_text(oc);(hist/cfg.name).write_text(oj)
anchor="'B_both_large_tracefree_rows.tex']";assert oc.count(anchor)==1 and stem+'.tex' not in oc
nc=oc.replace(anchor,"'B_both_large_tracefree_rows.tex',\n                    '"+stem+".tex']")
items=json.loads(oj);path='agents/reduction_descent/'+stem+'.tex';assert path not in items;items.append(path);nj=json.dumps(items,indent=2)+'\n'
compile(nc,str(con),'exec');con.write_text(nc);cfg.write_text(nj)
(hist/'consolidate.diff').write_text(''.join(difflib.unified_diff(oc.splitlines(True),nc.splitlines(True),fromfile='before/consolidate.py',tofile='after/consolidate.py')))
(hist/'config.diff').write_text(''.join(difflib.unified_diff(oj.splitlines(True),nj.splitlines(True),fromfile='before/'+cfg.name,tofile='after/'+cfg.name)))
w={'status':'WIRED_CP35','actual_utc':datetime.now(timezone.utc).isoformat(),'canonical':path,'canonical_sha256':h(can.read_bytes()),'consolidate_before_sha256':h(oc.encode()),'consolidate_after_sha256':h(con.read_bytes()),'config_before_sha256':h(oj.encode()),'config_after_sha256':h(cfg.read_bytes()),'prior_directory':str(hist),'scope':'Single B95 include after B94 and single CP35 required-input addition; current one-axis and OC entries preserved. No updater/report/build mutation.'}
(own/'outputs/B95_CP35_wiring.json').write_text(json.dumps(w,indent=2)+'\n')
print(json.dumps({'promotion':pr,'wiring':w},indent=2))
