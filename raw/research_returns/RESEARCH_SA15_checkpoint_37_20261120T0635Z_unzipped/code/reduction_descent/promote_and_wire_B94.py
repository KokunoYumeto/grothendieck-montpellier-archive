from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib
own=Path(__file__).resolve().parents[1];root=own.parents[1]
stem='B_both_large_tracefree_rows';expected='756e9cfc2b38369c603ff21f98dac6210bfc5f2d8bc1c3804f1b273eee2bc44f'
h=lambda b:hashlib.sha256(b).hexdigest()
candidate=own/(stem+'_candidate.tex');raw=candidate.read_bytes();assert h(raw)==expected
ra_path=root/'outputs/root_B94_audit.json';ca_path=own.parent/'obstructions_crystals/B94_independent_audit.json'
ra=json.loads(ra_path.read_text());ca=json.loads(ca_path.read_text())
for j in [ra,ca]:
 assert 'PASS' in j['status'] and j['candidate_sha256']==expected
 assert j['author_bytes_unchanged'] and j['all_mathematical_output_identical']
pre=own/'notes'/f'{stem}.prepromotion.tex';can=own/f'{stem}.tex';rec=own/'outputs/B94_promotion.json'
assert not pre.exists() and not can.exists() and not rec.exists()
pre.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion audits passed.}',raw.decode())
s=s.replace(s.splitlines()[0],'% Proved after complete root and companion audits; exact candidate retained.',1)
para='''
\\smallskip
\\noindent\\emph{Independent audits.}
The complete root and companion seven-assertion proof and exact-code
audits passed. Their literal author-output-preserving reruns took
\\(%s\\) and \\(%s\\) seconds, respectively.
Both independently rederived the actual matrix groups, strict
normality and commutator ordering, common diagonal restrictions,
point-field stabilizers and terminal conductor comparisons, after
rereading the complete invoked internal proofs. The companion also
reread the full retained original Colmez 3.7--3.13 proofs; neither
this author nor the root claims a new external source opening here.
The exact audit scopes, unchanged candidate, typography-only delta,
all programs and outputs, initial census failure and correction,
and promotion diff remain retained.
'''%(ra['independent_runtime_seconds'],ca['independent_runtime_seconds'])
assert s.count(r'\end{remark}')==1;s=s.replace(r'\end{remark}',para+r'\end{remark}')
can.write_text(s);labels=re.findall(r'\\label\{([^}]+)\}',s);assert len(labels)==7 and labels==ra['labels']==ca['labels']
now=datetime.now(timezone.utc).isoformat()
scope='Six of ten both-large residual-wild parameter pairs are excluded in layer shape(3,4). Remaining(3,4) pairs are(7,15),(9,13),(9,17),(11,15); every(4,4) pair and irreducible residual case remain open. No realization or unrestricted least-index equality is inferred.'
promotion={'status':'PROVED','promotion_utc':now,'canonical':str(can),'canonical_sha256':h(can.read_bytes()),'audited_candidate_sha256':expected,'preserved_candidate':str(pre),'labels':labels,'scope':scope,'root_audit':str(ra_path),'root_audit_utc':ra['actual_utc'],'root_runtime_seconds':ra['independent_runtime_seconds'],'companion_audit':str(ca_path),'companion_audit_utc':ca['actual_utc'],'companion_runtime_seconds':ca['independent_runtime_seconds'],'author_runtime_seconds':ra['author_runtime_seconds'],'canonical_change_scope':'Statuses, leading provenance comment and exact independent-audit paragraph only; audited mathematical proof unchanged.','retained_failure':'notes/B94_initial_pair_enumeration_failure','typography_delta':'notes/B94_quad_typography_repair/record.json','source_scope':'Exact source scopes in the two audits; no new author/root external source opening claimed. Companion freshly reread retained Colmez original full3.7–3.13 proofs.'}
rec.write_text(json.dumps(promotion,indent=2)+'\n')
(own/'notes/B94_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),s.splitlines(True),fromfile=candidate.name,tofile=can.name)))
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',scope,stem+'.tex;outputs/B94_promotion.json','Complete root and companion proof/code audits; exact author bytes and initial failed census retained'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:f.write(f'\n## {now} — B94 promoted\n\n{scope}\n')
# Narrow authorized shared insertion, using fresh bytes and preserving both inputs.
hist=own/'notes/CP35_before_B94_wiring';hist.mkdir()
con=root/'code/consolidate.py';cfg=root/'notes/checkpoint35_promoted_inputs.json'
oldcon=con.read_text();oldcfg=cfg.read_text()
(hist/'consolidate.py').write_text(oldcon);(hist/cfg.name).write_text(oldcfg)
anchor="'B_residual_wild_last_crossing.tex']"
assert oldcon.count(anchor)==1 and stem+'.tex' not in oldcon
newcon=oldcon.replace(anchor,"'B_residual_wild_last_crossing.tex',\n                    '"+stem+".tex']")
items=json.loads(oldcfg);assert isinstance(items,list)
path='agents/reduction_descent/'+stem+'.tex';assert path not in items;items.append(path)
newcfg=json.dumps(items,indent=2)+'\n'
compile(newcon,str(con),'exec')
con.write_text(newcon);cfg.write_text(newcfg)
(hist/'consolidate.diff').write_text(''.join(difflib.unified_diff(oldcon.splitlines(True),newcon.splitlines(True),fromfile='before/consolidate.py',tofile='after/consolidate.py')))
(hist/'config.diff').write_text(''.join(difflib.unified_diff(oldcfg.splitlines(True),newcfg.splitlines(True),fromfile='before/'+cfg.name,tofile='after/'+cfg.name)))
wire={'status':'WIRED_CP35','actual_utc':datetime.now(timezone.utc).isoformat(),'canonical':path,'canonical_sha256':h(can.read_bytes()),'consolidate_before_sha256':h(oldcon.encode()),'consolidate_after_sha256':h(con.read_bytes()),'config_before_sha256':h(oldcfg.encode()),'config_after_sha256':h(cfg.read_bytes()),'prior_directory':str(hist),'scope':'Single canonical include immediately after B93 and single CP35 required-input addition; existing OC entries retained. No build or updater/report changes.'}
(own/'outputs/B94_CP35_wiring.json').write_text(json.dumps(wire,indent=2)+'\n')
print(json.dumps({'promotion':promotion,'wiring':wire},indent=2))
