"""Retain the independent B82 audit without changing any author artifact."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
OWN = ROOT / 'agents/obstructions_crystals'
AUTHOR = ROOT / 'agents/reduction_descent'
candidate = AUTHOR / 'B_first_wild_reducible_terminal_candidate.tex'
program = AUTHOR / 'code/verify_first_wild_reducible_terminal.py'
author_output = program.with_suffix('.output.json')
expected = {
    candidate: '1fc957292d7075037e58964a058c77ca52c2460b610bc222329ca8dc05afffb1',
    program: 'fa0816d90ad10cd616219c9ee4f7df12bca8d2e66bbfc33301f701c4e9974889',
    author_output: '029967729cb587c6a5ba8ed7738b74f7289b7687e93833baa721687c2e7409e2',
}
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
for path, digest in expected.items():
    assert sha(path) == digest, str(path)
copied = OWN / 'code/B82_independent_check.py'
assert not copied.exists()
copied.write_bytes(program.read_bytes())
run = subprocess.run([sys.executable, str(copied)], cwd=ROOT,
                     capture_output=True, text=True)
copied.with_suffix('.stdout.txt').write_text(run.stdout)
copied.with_suffix('.stderr.txt').write_text(run.stderr)
preserved = {str(path.relative_to(ROOT)): {'before': digest, 'after': sha(path)}
             for path, digest in expected.items()}
hash_path = OWN / 'outputs/B82_author_hashes_preserved.json'
hash_path.write_text(json.dumps(preserved, indent=2) + '\n')
assert all(row['before'] == row['after'] for row in preserved.values())
assert run.returncode == 0, run.stderr
result = json.loads(copied.with_suffix('.output.json').read_text())
assert result['status'] == 'PASS'
assert result['counts'] == json.loads(author_output.read_text())['counts']
now = datetime.now(timezone.utc).isoformat()
labels = ['lem:B-RD82-Newton', 'lem:B-RD82-terminal',
          'prop:B-RD82-recovery', 'thm:B-RD82', 'rem:B-RD82-scope']
record = {
    'status': 'FULL PASS', 'actual_utc': now,
    'candidate': str(candidate.relative_to(ROOT)),
    'candidate_sha256': expected[candidate], 'labels': labels,
    'proof_read_scope': 'Entire final five-label B82 proof and entire standalone checker read. Fresh internal reads: B49 universal coefficient bounds and tame inertia; B60 complete fixed-coefficient lower-break proof and Newton/high-line argument; the relevant B69 Newton, residual-field and actual line-character proof; B67 exact Honda framing/tame averaging; B76 determinant detection; B77 complete square-determinant proof and its actual-target scope; B50 common finite twisting/normalization.',
    'checks': [
        'Re-derived the actual two-slope Newton vertices at e=p(p-1), the integer B, high/low valuations s-B and B/p, and the two successive low-target inverse polygons giving B/p^5. No prime-to-p-index theorem is imported beyond its explicitly rederived coefficient argument.',
        'The high line is inertia-stable and has a tame F_p-valued character killed by the degree-N good field. Its leading character is zeta^(c-B), since s=pN. Over L the determinant and high-line action are trivial, so residual wild image is either trivial or unipotent of order p.',
        'When the full division degree is p^4 and B=pb with p not dividing b, every outside-high primitive point has prime-to-p integral valuation b. The fixed-coefficient lower-break equality prevents a nonzero terminal matrix from killing an outside vector and forces all outside images to have the same high/low status.',
        'Varying (x,1) forces every terminal matrix to be upper triangular and every zero-lower-diagonal element to lie in F_p E12. The actual identity (1+pA+p^2B)^p=1+p^2A modulo p^3 and the exact order filtration 4=epsilon+r1+t force t=2, supplying both E12 and a matrix with nonzero lower diagonal. No orbit-rank shortcut is used.',
        'A common outside-both primitive vector gives p|B2. The actual E12 break p^4(s-pb1)-b1 excludes distinct high lines by a uniformly negative displacement inequality. With aligned lines the low-invertible element gives b2>=b1 and E12 gives b1>=b2. Equal actual high-line characters then recover c modulo N.',
        'For nontrivial residual wild inertia, one slope would imply a fixed injective leading-coordinate map and hence trivial residual wild action, so both polygons are unequal and their unique wild fixed lines align. Integrality and r<=4 reduce to either the preceding prime-b case or B_i=p^2 k_i with 1<=k_i<=p-2. The actual p^3 determinant comparison and common finite twist give k1=k2 from their congruence modulo p-1.',
        'The upper exponent r<=9 is one residual unipotent dimension plus two at-most-four-dimensional congruence kernels. The theorem only forces r>=5 for nontrivial residual wild comparisons with different special characters. It does not remove the residual-tame exchanged-high-line sector, larger images, or the unrestricted index interval {2,3}.'
    ],
    'primary_source_scope': 'No fresh external original-source read is claimed. The complete internal dependency proofs listed above were freshly reread; previously audited Hopkins-Gross, Tate, Bondarko and fixed-coefficient source bridges are used only in their established scope. The new terminal-matrix and two-break arguments were rederived directly.',
    'independent_program': str(copied.relative_to(ROOT)),
    'independent_output': str(copied.with_suffix('.output.json').relative_to(ROOT)),
    'independent_runtime_seconds': result['runtime_seconds'],
    'counts': result['counts'], 'author_bytes_unchanged': True,
    'hash_record': str(hash_path.relative_to(ROOT)),
    'finite_scope': result['scope'],
    'checkpoint_scope': 'Post-CP29 candidate audit only. No frozen canonical paper input was modified.'
}
audit = OWN / 'B82_independent_audit.json'
with audit.open('x') as stream:
    json.dump(record, stream, indent=2)
    stream.write('\n')
with (OWN / 'CHECK_EVENTS.tsv').open('a') as stream:
    for label in labels:
        stream.write('\t'.join([now, label, 'independent_full_proof_code_audit',
                                str(candidate.relative_to(ROOT)),
                                'Entire proof and invoked internal dependencies rederived; literal isolated checker rerun with author hashes preserved',
                                'PASS', str(audit.relative_to(ROOT))]) + '\n')
print(json.dumps({'audit': str(audit.relative_to(ROOT)), 'actual_utc': now,
                  'status': 'FULL PASS',
                  'runtime_seconds': result['runtime_seconds'], 'labels': labels}))
