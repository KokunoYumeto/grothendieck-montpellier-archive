from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

own = Path(__file__).resolve().parents[1]
source = own / 'B_first_level_mixed_boundary_candidate.tex'
prior = own / 'notes/B_first_level_mixed_boundary.before_certificate.tex'
assert not prior.exists()
prior.write_bytes(source.read_bytes())
result = json.loads((own / 'code/verify_first_level_mixed_boundary.output.json').read_text())
old = '''An exact finite supplement is being prepared separately; the
all-prime conclusions above are not inferred from numerical tests.'''
new = r'''The retained exact supplement
\path{code/reduction_descent/verify_first_level_mixed_boundary.py}
reconstructs both actual high-quotient Newton polygons from the
universal vertices and counts quotient roots using the product map.
Across twelve primes from \(5\) through \(43\), it checks
\(24\) double-quotient root records, \(264\) corresponding
distinct-eigenvalue records, \(545{,}376\) first-level prime breaks,
and \(1{,}074{,}792\) tame mixed point-field inequalities.
It also checks the entire stated small common-norm case split,
the boundary strict-break contradiction at every tested prime,
and all remaining tame quotient-divisibility branches.
For \(p=5,e=48\), the actual second parameters are \(125\) and
\(63\); the prime model requires lower break \(1062\), whereas
the divisible model requires it to be strictly less than \(690\).
The author run passed in \(0.5185015480092261\) seconds at
22:14:11 UTC. The complete program, output, and pre-certificate
proof are retained. No executed numerical check failed.
These finite checks supplement the all-prime proof and do not
provide a formal-group existence test.'''
text = source.read_text()
assert old in text
source.write_text(text.replace(old, new))
now = datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
labels = re.findall(r'\\label\{([^}]+)\}', source.read_text())
record = {
 'status':'CANDIDATE_COMPLETE_PROOF_AND_EXACT_SUPPLEMENT',
 'actual_utc':now, 'candidate':source.name,
 'candidate_sha256':sha(source), 'pre_certificate_sha256':sha(prior),
 'labels':labels,
 'claim':'Exact full B4 nu_min(p,2(p^2-1),2)=2 for p>=5; first-level mixed inequality and marked actual second-quotient proof. p5/e48 included; e52 and p-divisible absolute indices unclaimed.',
 'program':'code/verify_first_level_mixed_boundary.py',
 'program_sha256':sha(own/'code/verify_first_level_mixed_boundary.py'),
 'output':'code/verify_first_level_mixed_boundary.output.json',
 'output_sha256':sha(own/'code/verify_first_level_mixed_boundary.output.json'),
 'author_runtime_seconds':result['elapsed_seconds'],
 'author_actual_utc':result['actual_utc'], 'counts':result['counts'],
 'independent_audits':'Requested; no promotion from this record.',
 'executed_failures':[]
}
(own/'outputs/B72_candidate_record.json').write_text(json.dumps(record,indent=2)+'\n')
notes = '''# B72 source and proof check record

The new lemma is an immediate application of the complete elementary lower-break
proof in B60 (lem:B-RD60-break), reread in full. It retains both the exact
prime-valuation equality and the strict divisible-valuation inequality.

The actual quotient/Newton/decent statements are exactly the fully audited B69
quotient proof and B71 marked-low proof, both reread in full. The new second
quotient retains only p-torsion. No p^2 comparison is silently used afterward.
Finite special-character and full-monodromy reductions reuse B69/B70/B71 and
the actual B63 lower example. No new external theorem or fresh primary web
retrieval is claimed in this extension; the original Hopkins--Gross and Tate
source bridges remain those recorded for these dependencies.

No equality of integral good models over ramified quotients is asserted.
No scalar complement is selected: the boundary marked quotients have distinct
residual eigenvalues. Scalar small-pair cases remain covered only by B71's
separate actual point-field argument.

The first exact program run passed. The exact pre-certificate proof, complete
executed source, output and stdout are retained. Universal proof, not a finite
row test, supplies the all-prime assertion. Candidate pending independent audits.
'''
(own/'notes/POST_CP26_B72_SOURCE_CHECKS.md').write_text(notes)
with (own/'CHECK_EVENTS.tsv').open('a') as stream:
 for label in labels:
  stream.write('\t'.join([now,label,'CANDIDATE_COMPLETE_PROOF','First-level mixed lower break and actual double quotient exclude e=2N remaining pair; exact full B4 index2 candidate.','B_first_level_mixed_boundary_candidate.tex;outputs/B72_candidate_record.json','Complete self-proof review and exact supplement PASS; independent audits requested'])+'\n')
print(json.dumps({'status':record['status'],'actual_utc':now,'candidate_sha256':record['candidate_sha256'],'labels':labels,'runtime':result['elapsed_seconds']}))
