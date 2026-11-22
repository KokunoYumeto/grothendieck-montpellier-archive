#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OWN = ROOT / 'agents/monodromy'
CANDIDATE = ROOT / 'agents/reduction_descent/B_second_wild_trace_arc_candidate.tex'
EXPECTED = 'f0fb542a2cbd9ee40f0144f1ae4f8dd209ec0f0bd92153b70cb8d511d7ae0950'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(CANDIDATE) == EXPECTED
run = json.loads((OWN / 'outputs/independent_B100_exact_rerun.json').read_text())
assert run['status'] == 'PASS' and run['author_bytes_unchanged']
now = datetime.now(timezone.utc).isoformat()
checks = {
 'lem:B-RD100-arc': 'Independently checked the uniform choice e/p^3<A<e/p^2 with N not dividing A, every strict Newton gap and the b congruence, all intermediate and unbounded-tail terms, the exact Eisenstein degree, valuation survival after specialization, exact order p^3, and the logarithmic weight identity. The order-N field automorphism, possibly nonfaithful special action, exact cocycle fixing x^A, finite-level generic descent, absolute index e, and mu_p containment all rederive.',
 'thm:B-RD100-ambiguity': 'Checked the primitive constant cyclic subgroup, its actual good-model finite-flat closure and quotient, crystalline determinant and finite twist, exact multiplication snake sequence, and compatible Kummer cocycle lift. The eigenvalue multisets and nonzero trace difference use only N not dividing A, so nonfaithful special actions are covered. One whole potentially good group and an explicitly filtered group are distinguished.',
 'cor:B-RD100-threshold': 'Re-derived the B76 strict mixed inequality at n=3 and v_p(e)=1, and checked that the new arc supplies every permitted existential index e>p^2. No existence over each prescribed field is inferred.',
 'thm:B-RD100-exact': 'Checked the actual p^3 lower example at e=2p(p-1), the explicit A=1 specialization, determinant detection at actual p^4, dimension-zero/two reductions and residual filtered case, mixed exclusion e<p^4, and the B64 actual-target recurrence 1,2p-1,2p^2-1,2p^3-1 with surplus 2p-1 above a/(p-1). No source-thickness transfer is used. The manuscript index conversion gives exactly nu_min(p,2p(p-1),2)=3.',
 'rem:B-RD100-scope': 'Checked the existential versus fixed-field distinction, unrestricted positive v_p(e) construction versus valuation-one threshold, the restricted exact-index family, all finite certificate counts, and the separation of arithmetic checks from formal-group/descent/quotient/Kummer effectivity.'
}
dependency_paths = [
 'agents/reduction_descent/B_tame_cyclic_level_counterexamples.tex',
 'agents/reduction_descent/B_tame_quotient_weight_gate.tex',
 'agents/reduction_descent/B_wild_cyclic_point.tex',
 'agents/reduction_descent/B_BT_lower.tex',
 'agents/reduction_descent/sources/kisin_crystalline.txt'
]
source = {
 'fresh_original_opening': {
  'title':'Hopkins and Gross (1994), Equivariant vector bundles on the Lubin--Tate moduli space',
  'url':'https://math.bu.edu/people/jsweinst/AWS/Files/GrossHopkinsEquivariantVectorBundles.pdf',
  'refs':['turn473447213search5','turn315075753view0','turn315075753view1','turn315075753view2','turn880405757view0','turn880405757view1'],
  'actually_read':'Complete original equations (5.3)--(5.8), Proposition 5.7 statement and coefficient congruence; equations (12.1)--(12.9), Proposition 12.10 and its entire printed proof through the final square, including arbitrary residue-field extension. Also the complete displayed Proposition 4.2 proof was returned and read.',
  'scope':'Proposition 5.7 attributes integrality to Hazewinkel; no fresh reading of that book is claimed. Original indexed text was read, without page-image inspection.'
 },
 'retained_original_rereading': {
  'path':'agents/reduction_descent/sources/kisin_crystalline.txt',
  'scope':'Original author text, Lemma 2.2.4 and Corollary 2.2.6 with their complete printed proofs, and Theorem 2.2.7 with its complete proof, pp.26--27. The determinant argument in the complete canonical B18 proof and all relevant B62 steps were independently reread.'
 },
 'prior_source_dependencies':'The established Tate/Bondarko source validations are reused through the complete canonical B64 coefficient/logarithm/Cartier-projection/actual-graph proof, which was read in full and rederived here. No fresh original Bondarko or Tate read is claimed.',
 'retrieval_failures_retained':[
  {'ref':'turn923435526view0','operation':'Direct original Hopkins--Gross PDF open','error':'502 Bad Gateway','resolution':'First-engine search recovered the indexed original; complete passages then opened successfully.'},
  {'ref':'turn473447213view0','operation':'https://people.math.harvard.edu/~kisin/papers/crys.pdf','error':'URL not accessible through web tool','resolution':'Read the already retained original author text, explicitly without claiming a new web opening.'}
 ],
 'read_completeness':'An earlier oversized dependency read was truncated and not credited. The full B62, B64 and B76 files were subsequently actually read in bounded chunks; the final B100 candidate and checker were also each read completely in bounded chunks.'
}
record = {
 'status':'PASS', 'actual_utc':now,
 'auditor':'GPT-6 Astra Pro /root/monodromy',
 'candidate':str(CANDIDATE), 'candidate_sha256':EXPECTED,
 'scope':'Complete independent mathematical, primary-source-scope and exact-code audit of all five B100 assertions.',
 'per_label':[{'label':k,'status':'PASS','reason':v} for k,v in checks.items()],
 'dependencies_actually_read':[{ 'path':p,'sha256':sha(ROOT/p)} for p in dependency_paths],
 'source_audit':source,
 'literal_isolated_rerun':run,
 'no_inference':'No finite computation is used to prove existence/effectivity of an infinite formal group, Eisenstein DVR, descent, finite quotient or compatible Kummer extension; those conclusions were independently checked from their written proofs.',
 'shared_files_modified':False,
 'candidate_preserved':str(OWN/'notes/B100_independent_audit_20261120'/CANDIDATE.name)
}
target = OWN/'outputs/independent_B100_second_wild_trace_arc_audit.json'
assert not target.exists()
target.write_text(json.dumps(record,indent=2)+'\n')
source_target = OWN/'notes/B100_independent_audit_20261120/source_access.json'
source_target.write_text(json.dumps(source,indent=2)+'\n')
events = OWN/'CHECK_EVENTS_post_CP16.tsv'
with events.open('a') as f:
 for label, reason in checks.items():
  f.write('\t'.join(['B100-COMPANION-'+label,now,'GPT-6 Astra Pro /root/monodromy','complete-proof-source-code-PASS',reason+' Exact frozen SHA '+EXPECTED+'; literal isolated runtime '+str(run['runtime_seconds'])+' seconds; author bytes unchanged.'])+'\n')
print(json.dumps({'status':'PASS','actual_utc':now,'record':str(target),'candidate_sha256':EXPECTED,'runtime_seconds':run['runtime_seconds'],'events':len(checks)},indent=2))
