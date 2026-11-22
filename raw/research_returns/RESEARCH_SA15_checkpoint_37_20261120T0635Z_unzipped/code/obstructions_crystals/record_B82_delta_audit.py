from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
source = root / 'agents/reduction_descent/B_first_wild_reducible_terminal_candidate.tex'
digest = hashlib.sha256(source.read_bytes()).hexdigest()
assert digest == '594f019abab5cd378c489671f7ff021c7e0e446ac53166f696dafa035f0f761b'
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'FULL PASS - exact proof delta checked', 'actual_utc': now,
    'candidate': str(source.relative_to(root)), 'candidate_sha256': digest,
    'prior_full_audit': 'agents/obstructions_crystals/B82_independent_audit.json',
    'prior_candidate_sha256': '1fc957292d7075037e58964a058c77ca52c2460b610bc222329ca8dc05afffb1',
    'diff_read': 'agents/reduction_descent/notes/B82_determinant_simplification.diff',
    'label': 'thm:B-RD82',
    'check': 'The only proof delta removes an unnecessary square-determinant case split and common twist. Both whole groups have the same cyclotomic determinant factor. Actual torsion comparison therefore identifies their finite mu_(p-1) characters, giving c1=c2 modulo p-1. The common high-line character gives B1=B2 modulo p-1. With B_i=p^2 k_i and p^2=1 modulo p-1, the interval 1<=k_i<=p-2 forces k1=k2; then the original high-line equality yields c1=c2 modulo N. This is valid without any square-class normalization.',
    'code_scope': 'Checker and author output are unchanged. The preceding isolated rerun remains the computational audit; no redundant rerun or new external-source read is claimed.'
}
path = own / 'B82_determinant_delta_audit.json'
with path.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    f.write('\t'.join([now, 'thm:B-RD82', 'independent_proof_delta_audit',
                       str(source.relative_to(root)), 'Exact saved diff read and determinant congruences rederived',
                       'PASS', str(path.relative_to(root))]) + '\n')
print(json.dumps({'status': record['status'], 'actual_utc': now,
                  'record': str(path.relative_to(root)), 'candidate_sha256': digest}))
