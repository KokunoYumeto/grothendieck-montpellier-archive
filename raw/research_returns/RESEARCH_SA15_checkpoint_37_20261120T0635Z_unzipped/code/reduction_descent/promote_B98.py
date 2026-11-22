from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib
own=Path(__file__).resolve().parents[1];root=own.parents[1]
stem='B_first_wild_cyclotomic_different'
expected='0b8f978f9cfa246cfc0f6b1f2fb99212912cd4b4cfd1df86b0f04d7a8a868dc1'
h=lambda b:hashlib.sha256(b).hexdigest()
p=own/(stem+'_candidate.tex');raw=p.read_bytes();assert h(raw)==expected
rp=root/'outputs/root_B98_audit.json';cp=own.parent/'obstructions_crystals/B98_independent_audit.json'
r=json.loads(rp.read_text());c=json.loads(cp.read_text())
for a in (r,c):
 assert 'PASS' in a['status'] and a['candidate_sha256']==expected
 assert a['author_bytes_unchanged'] and a['all_mathematical_output_identical']
prior=own/'notes'/f'{stem}.prepromotion.tex';can=own/f'{stem}.tex';rec=own/'outputs/B98_promotion.json'
assert not prior.exists() and not can.exists() and not rec.exists()
prior.write_bytes(raw)
new=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; full independent root and companion audits passed.}',raw.decode())
new=new.replace(new.splitlines()[0],'% Proved after complete root and companion audits; exact candidate retained.',1)
para=r'''
\smallskip
\noindent\emph{Independent audits.}
The complete root and obstruction/crystal companion proof,
source and exact-code audits passed. Their unchanged isolated
reruns took \(%s\) and \(%s\) seconds,
respectively, with every mathematical output equal to the author
output and all author bytes preserved. Both checked the actual
Cohen/cyclotomic fields, the two different towers, the complete
terminal-character spanning and restriction, and the exact
height-two upper and lower bounds. Both reread the retained
original Colmez Propositions3.17--3.18 and Corollary3.19 with
their complete proofs on pp.~17--18. No new web opening or
image inspection is claimed. The exact candidates, field-scope
clarification, all executed code and outputs, audit records and
promotion diff are retained.
'''%(r['independent_runtime_seconds'],c['independent_runtime_seconds'])
assert new.count(r'\end{remark}')==1
new=new.replace(r'\end{remark}',para+r'\end{remark}')
can.write_text(new)
labels=re.findall(r'\\label\{([^}]+)\}',new)
assert len(labels)==4 and labels==r['labels']==c['labels']
now=datetime.now(timezone.utc).isoformat()
scope='Exact full B4 height-two least index nu_min(5,20,2)=2: actual125 determines all requested prime-to-five special characters, and actual25 can fail. For every p>=5 at e=p(p-1), the irreducible-residual whole height-two branch is recovered at actualp^3. No full first-wild equality for another prime, general ramification or higher height is inferred.'
pr={'status':'PROVED','promotion_utc':now,'canonical':str(can),'canonical_sha256':h(can.read_bytes()),
 'audited_candidate_sha256':expected,'preserved_candidate':str(prior),'labels':labels,'scope':scope,
 'root_audit':str(rp),'root_audit_utc':r['actual_utc'],'root_runtime_seconds':r['independent_runtime_seconds'],
 'companion_audit':str(cp),'companion_audit_utc':c['actual_utc'],'companion_runtime_seconds':c['independent_runtime_seconds'],
 'author_runtime_seconds':1.8577888349973364,
 'canonical_change_scope':'Statuses, leading provenance comment and exact audit paragraph only. Audited mathematical proof unchanged.',
 'executed_failures':[],'source_scope':'Author/root/companion freshly read complete retained original Colmez3.17–3.19 proofs, pp17–18. Complete invoked B86/B97/B76/B63 proofs checked. No new external opening, image inspection or priority claim.',
 'shared_wiring':'Pending coordinated window; no shared file modified by this script.'}
rec.write_text(json.dumps(pr,indent=2)+'\n')
(own/'notes/B98_promotion.diff').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),new.splitlines(True),fromfile=p.name,tofile=can.name)))
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',scope,stem+'.tex;outputs/B98_promotion.json','Complete root and companion proof/source/code audits; actual-field upper bound and retained explicit lower example independently verified'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:f.write(f'\n## {now} — B98 promoted\n\n{scope}\n')
print(json.dumps(pr,indent=2))
