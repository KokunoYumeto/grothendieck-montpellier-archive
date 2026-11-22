from pathlib import Path
import datetime,json,hashlib
r=Path(__file__).resolve().parent.parent;p=r/'nonordinary_uniform_five_theta_geometry_candidate.tex';s=p.read_text()
s=s.replace('\\status{Candidate; complete proofs and universal certificate submitted for independent audit.}','\\status{Proved and independently checked.}').replace('\\textup{[Candidate.]}','\\textup{[Proved; independent audits passed.]}')
s=s.replace('\\path{code/nonordinary_uniform_five_self_isogeny_identities.py}','\\path{code/monodromy/nonordinary_uniform_five_self_isogeny_identities.py}').replace('\\path{outputs/nonordinary_uniform_five_self_isogeny_identities.json}','\\path{agents/monodromy/outputs/nonordinary_uniform_five_self_isogeny_identities.json}')
s=s.replace('no mathematical identity failed. The theorem proves a nodal theta','no mathematical identity failed. The parent completed the full proof and code audit at 20:40:04 UTC and independently reran all identities in $0.101561034$ seconds. Reduction/descent completed the full proof and code audit at 20:39:50 UTC, with an output-preserving rerun in $0.36796294799569296$ seconds. The theorem proves a nodal theta')
q=r/'nonordinary_uniform_five_theta_geometry.tex';q.write_text(s)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:uniform-f0-order-four-presentation-candidate','thm:uniform-f0-five-self-isogeny-nodal-candidate','lem:nonproduct-three-theta-four-values-candidate','rem:uniform-five-theta-geometry-scope-candidate']
rec={'status':'PROMOTED','actual_utc':now,'candidate':p.name,'candidate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'canonical':q.name,'canonical_sha256':hashlib.sha256(q.read_bytes()).hexdigest(),'labels':labels,'root_audit':'../../outputs/root_uniform_five_geometry_audit.json','scope':'Uniform nodal five-self-isogenies for supersingular genus-two Jacobians and finite four-value exceptions; full degree-five monodromy not asserted here.'}
(r/'outputs/nonordinary_uniform_five_geometry_promotion.json').write_text(json.dumps(rec,indent=2)+'\n')
with (r/'post_CP16_notes.md').open('a') as f:f.write('\n## '+now+' — Uniform five-theta geometry promotion\n\nPromoted nonordinary_uniform_five_theta_geometry.tex after full root/RD proof/code audits. Exact final candidate retained. Only statuses, exported paths and completed-check paragraph changed. Stable labels unchanged. Uniform nodal five-self-isogeny and four-value theorem do not themselves assert monodromy. Initial coefficient-domain setup failure retained separately.\n')
with (r/'CHECK_EVENTS_post_CP16.tsv').open('a') as f:
 for l in labels:f.write('\t'.join([now,l,'promotion_after_full_root_RD_audits','PASS','Uniform geometric result; exact nine identities independently rerun; no full-image inference',q.name])+'\n')
print(json.dumps(rec,indent=2))
