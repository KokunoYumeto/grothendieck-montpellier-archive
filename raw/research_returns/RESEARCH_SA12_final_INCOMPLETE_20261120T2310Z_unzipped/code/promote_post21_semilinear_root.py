"""Status-only promotion after four exact-candidate mathematical audits."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
p=root/'parts/D/post21_research/D_tame_projective_semilinear_crowns_root.tex'
candidate='f5f0b3e917d1325eef5023f38e22950cb29eea58d38896f935528603ada93a5f'
assert hashlib.sha256(p.read_bytes()).hexdigest()==candidate
records={
 'root':'parts/D/post21_research/audit_root_projective_semilinear_author.json',
 'B':'parts/B/post21_research/audit_root_tame_projective_semilinear_crowns_B.json',
 'C':'parts/C/post21_research/audit_root_projective_semilinear_crowns_C.json'}
candidates=[]
for q in (root/'parts/D/post21_research').glob('audit*.json'):
 a=json.loads(q.read_text())
 if a.get('sha256')==candidate and a.get('actor',a.get('auditor'))=='D':candidates.append(q)
assert len(candidates)==1,[str(q) for q in candidates]
records['D']=str(candidates[0].relative_to(root))
audits={}
for actor,name in records.items():
 a=json.loads((root/name).read_text());assert a['sha256']==candidate
 assert a.get('outcome',a.get('verdict'))=='PASS'
 audits[actor]=dict(record=name,verdict='PASS',audit_scope=a.get('audit_scope',a.get('scope',a.get('checks'))),audited_sha256=candidate)
snapshot=p.with_name(p.stem+'_audited.source.txt');assert not snapshot.exists();snapshot.write_bytes(p.read_bytes())
s=p.read_text();assert s.count('[Candidate:')==2
p.write_text(s.replace('[Candidate:','[Proved:'))
now=datetime.now(timezone.utc).isoformat()
manifest=dict(path=str(p.relative_to(root)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
 recorded_utc=now,promoted_at_utc=now,status='Proved; four exact-candidate audits complete',
 labels=['D:tame-projective-semilinear-count','D:tame-projective-automorphism-crowns'],
 audited_candidate_sha256=candidate,candidate_snapshot=str(snapshot.relative_to(root)),
 promotion_changes='Exactly two Candidate-to-Proved statement-heading replacements; all other bytes unchanged.',
 bibliography=None,reused_bibliography_keys=['LucchiniMarionTracey2020D'],audits=audits,
 audit_scope='Four actual-file mathematical checks with exact fresh versus reused source scope in the records.',
 scope_precision='Complete excellent normal local one-smooth-exceptional-curve setting. The subgroup cover and fixed field character are radially tame; the projective representation itself need not be tame. Field-image order, geometric Brauer period and scalar order are unrestricted. Crown hypotheses retain faithful projective embedding, standard field-semilinear preimage, bounded graph quotient and order comparison.',
 movement_classification='Together with the three coherent-gerbe/sector/skew dependencies, one strict post-review14 crown-gate reduction from bounded to unrestricted field-image order; not five separate movements.',
 literature_search_record='parts/D/post21_research/projective_semilinear_search_root.json')
out=root/'parts/D/post21_research/integration_manifest_root_projective_semilinear_crowns.json'
assert not out.exists();out.write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'utc':now,'manifest':str(out.relative_to(root)),'sha256':manifest['sha256']},indent=2))
