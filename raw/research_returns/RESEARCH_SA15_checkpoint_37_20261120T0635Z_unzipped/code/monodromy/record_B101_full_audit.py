#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
OWN = ROOT/'agents/monodromy'
CANDIDATE = ROOT/'agents/reduction_descent/B_uniform_wild_trace_arcs_candidate.tex'
EXPECTED = '7b3d5176da21e3d81c76e9fea88742dd9459f08112afbd3925d1d71ea688b7c2'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(CANDIDATE) == EXPECTED
run = json.loads((OWN/'outputs/independent_B101_exact_rerun.json').read_text())
assert run['status'] == 'PASS' and run['author_bytes_unchanged']
now = datetime.now(timezone.utc).isoformat()
checks = {
 'lem:B-RD101-arc':'Independently rederived the full interval choice for A, including avoidance of N dividing A, h=n-1-v>=1, b integrality and both exact strict gaps. Checked h uniquely minimal q-steps followed by v uniquely minimal p-steps, every intermediate coefficient and infinite tail, the v=0 case, closed iterate orders J_r, terminal Eisenstein degree eN, all p-coefficient cutoffs, exact order p^n, logarithmic equivariance, the order-N field action and semilinear cocycle fixing x^A, and mu_p containment. No numerical polygon is used as an existence argument.',
 'prop:B-RD101-ambiguity':'Checked the actual finite-flat closure and quotient of the primitive constant cyclic line, the rank-one crystalline determinant, exact multiplication snake sequence, finite twist, and complete compatible Kummer-cocycle lift from canonical B62. The trace difference is nonzero exactly using N not dividing A, including nonfaithful special actions. The two allowed monodromy classes and the manuscript-index conversion are exact.',
 'cor:B-RD101-threshold':'Checked necessity from the complete B76 strict mixed bound and sufficiency from the new constructed field and point. Scope is existential across fields, p-1 divides e, and n>=v_p(e)+2; no claim below that level is inferred.',
 'thm:B-RD101-exact':'Independently checked every v>=0: lower level n=v+2 has h=1,A=1 and b=(p-1)(p^2-2). For recovery at nprime=v+3, determinant detection and the full dimension exhaustion hold, the mixed branch is impossible, and the B64 recurrence on the actual target is q_j=2p^j-1 through j=v+2. The required surplus is exactly 2p^v-1>0, including v=0. This proves precisely nu_min(p,2p^v(p-1),2)=v+2.',
 'rem:B-RD101-scope':'The proof is independent of an unpromoted B100 assertion. Checked every finite-range and count statement against the exact unchanged output and code; finite v<=8/h<=6 data do not establish the infinite theorem. The restrictions on e, height, mu_p, perfect residue and the two comparison classes are preserved.'
}
b100 = json.loads((OWN/'outputs/independent_B100_second_wild_trace_arc_audit.json').read_text())
dependencies = b100['dependencies_actually_read']
for item in dependencies:
 assert sha(ROOT/item['path']) == item['sha256'], 'Dependency changed after its complete read'
record = {
 'status':'PASS','actual_utc':now,'auditor':'GPT-6 Astra Pro /root/monodromy',
 'candidate':str(CANDIDATE),'candidate_sha256':EXPECTED,
 'scope':'Complete independent proof and literal unchanged exact-code audit of all five assertions, with the precise original-source and full-dependency reads from the immediately preceding B100 audit reused.',
 'per_label':[{'label':k,'status':'PASS','reason':v} for k,v in checks.items()],
 'read_completeness':'The entire 337-line final candidate and entire 213-line checker were actually read in bounded complete chunks, without truncation credit. All mathematical output fields were compared exactly; the complete executed output and stdout are retained in the isolated environment.',
 'dependencies_actually_read':dependencies,
 'source_scope':{
  'reused_current_original_read_record':str(OWN/'notes/B100_independent_audit_20261120/source_access.json'),
  'precise_scope':'The original Hopkins--Gross indexed PDF was freshly opened during this same audit session: complete equations 5.3--5.8, Proposition 5.7 and coefficient congruence, 12.1--12.10 with the entire printed proof and arbitrary residue-field extension. The retained original Kisin 2.2.4/2.2.6/2.2.7 full proofs and the complete canonical B62, B64, B76 and B18 proofs were actually read. These same already-opened passages are reused for B101; no additional source opening, fresh Hazewinkel reading, page-image inspection, or new Bondarko/Tate original read is claimed.',
  'refs':b100['source_audit']['fresh_original_opening']['refs'],
  'retrieval_failures':b100['source_audit']['retrieval_failures_retained']
 },
 'literal_isolated_rerun':run,
 'no_inference':'The infinite formal-group, exact DVR, descent, finite quotient and Kummer effectivity steps were independently checked from the written proofs and are not inferred from the bounded arithmetic checks.',
 'canonical_or_shared_edits':False,
 'checkpoint_scope':'Candidate remains outside CP37; no promotion is inferred from this audit.'
}
target=OWN/'outputs/independent_B101_uniform_wild_trace_arcs_audit.json'
assert not target.exists()
target.write_text(json.dumps(record,indent=2)+'\n')
with (OWN/'CHECK_EVENTS_post_CP16.tsv').open('a') as f:
 for label,reason in checks.items():
  f.write('\t'.join(['B101-COMPANION-'+label,now,'GPT-6 Astra Pro /root/monodromy','complete-proof-source-scope-code-PASS',reason+' Frozen SHA '+EXPECTED+'; unchanged isolated runtime '+str(run['runtime_seconds'])+' seconds.'])+'\n')
print(json.dumps({'status':'PASS','actual_utc':now,'record':str(target),'candidate_sha256':EXPECTED,'runtime_seconds':run['runtime_seconds'],'events':len(checks)},indent=2))
