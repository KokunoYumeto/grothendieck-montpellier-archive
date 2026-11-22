"""Full B85 proof audit with a literal, author-output-preserving rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
author = root / 'agents/reduction_descent'
source = author / 'B_first_wild_diagonal_projection_candidate.tex'
program = author / 'code/verify_first_wild_diagonal_projection.py'
author_output = program.with_suffix('.output.json')
expected = {
    source: '7ae032b8394c8209094c53cdbf26d13d23868fd3c39ab026841527f9dd65cb18',
    program: '6e7307002a4682c7121a7aec0a6ae02d3273c1cd57114ad07e3989e1e73bcbb5',
    author_output: '819668814d2535b0150387737240e4067517e78610c9cf5735776f0af5e656fc',
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

for path, digest in expected.items():
    assert sha(path) == digest, str(path)
copied = own / 'code/B85_independent_check.py'
assert not copied.exists()
copied.write_bytes(program.read_bytes())
run = subprocess.run([sys.executable, str(copied)], cwd=root,
                     capture_output=True, text=True)
copied.with_suffix('.stdout.txt').write_text(run.stdout)
copied.with_suffix('.stderr.txt').write_text(run.stderr)
hashes = {str(path.relative_to(root)): {'before': digest, 'after': sha(path)}
          for path, digest in expected.items()}
hash_path = own / 'outputs/B85_author_hashes_preserved.json'
hash_path.write_text(json.dumps(hashes, indent=2) + '\n')
assert all(row['before'] == row['after'] for row in hashes.values())
assert run.returncode == 0, run.stderr
result = json.loads(copied.with_suffix('.output.json').read_text())
assert result['status'] == 'PASS'
assert result['counts'] == json.loads(author_output.read_text())['counts']
now = datetime.now(timezone.utc).isoformat()
labels = ['lem:B-RD85-diagonal', 'cor:B-RD85-tame', 'rem:B-RD85-scope']
record = {
    'status': 'FULL PASS', 'actual_utc': now,
    'candidate': str(source.relative_to(root)),
    'candidate_sha256': expected[source], 'labels': labels,
    'proof_read_scope': 'Entire final B85 candidate and standalone checker read. The whole canonical B83 proof and whole B69 proof were freshly reread, and the complete B60 elementary lower-break lemma and proof were freshly reread. The actual B84 corollary was rechecked against its preceding complete independent audit. All invoked steps were independently rederived at the present wild absolute index.',
    'checks': [
        'The two actual high lines are inertia-stable. The B83 finite-flat quotient construction and lattice T+Zp(e_i/p) identify the nontrivial residual quotient actions with the two off-diagonal projections of the same W1, without using p=1 modulo4.',
        'If the 11 projection vanishes, W1 e1 is exactly Fp e2 because its 21 projection is nonzero. The actual action on a primitive p2 point above e1 consequently has orbit p. Rational first-level torsion makes its point field Galois, and the actual torsion isomorphism identifies the point stabilizers and hence the same degree-p field and translation group for both models. No full division-field size is substituted for this point-field calculation.',
        'For B=p2*k with k in1..p-2, the high inverse constant valuation is p*(N-p*k). The degree-p coefficient lies strictly above the degree-q chord precisely because p*(p+1)*k>N; the linear and intermediate coefficients obey the established universal bounds independently of p-divisibility of the absolute index. Thus every high inverse has valuation (N-p*k)/p. Low inverse valuation is k/p. Multiplication by the ramification degree p gives positive prime-to-p integral valuations N-p*k and k.',
        'The same nonidentity automorphism translates by e2, low in the first model and high in the second. Formal addition changes the coordinate by that translation times an integral unit. Its two displacement valuations are q*k1 and q*(N-p*k2). The B60 prime-valuation equality therefore gives the two displayed exact lower breaks, not an upper-numbering shortcut.',
        'Equality of these lower breaks would force p*(p+1)*k1+(p3+1)*k2=p4-1. The maximum allowed left side at k1=k2=p-2 is smaller by (p+1)*(p2+1)>0. Exchanging models and basis directions proves the second diagonal projection nonzero as well.',
        'Only the corollary invokes p=1 modulo4 and the nonsquare determinant. B83 spectral projectors supply both off-diagonal matrix units and the diagonal projector. A nonzero diagonal projection supplies a third independent W1 direction; actual p-th powers inject W1 into W2. The exact actual group order p^(dimW1+dimW2) yields at least p6. The p5 pattern is the already-proved B84 necessary pattern, with no construction or unrestricted recovery conclusion.'
    ],
    'primary_source_scope': 'No new external original-source read is claimed. The complete invoked internal coefficient/Newton, actual quotient/lattice, and fixed-coefficient lower-break proofs were reread in the scopes above; no new literature theorem is imported.',
    'independent_program': str(copied.relative_to(root)),
    'independent_output': str(copied.with_suffix('.output.json').relative_to(root)),
    'independent_runtime_seconds': result['runtime_seconds'],
    'counts': result['counts'], 'finite_scope': result['scope'],
    'author_bytes_unchanged': True, 'hash_record': str(hash_path.relative_to(root)),
    'scope': 'Both diagonal projections are nonzero in the stated exchanged-high-line configuration for all p>=5. The p6 wild-image lower bound is confined to the tame reducible residual sector at p=1 modulo4. It does not extend that lower bound across all residual types or decide the unrestricted first-wild least index.'
}
audit = own / 'B85_independent_audit.json'
with audit.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'independent_full_proof_code_audit',
                           str(source.relative_to(root)),
                           'Full actual degree-p point-field and both exact-break arguments rederived; literal isolated certificate',
                           'PASS', str(audit.relative_to(root))]) + '\n')
print(json.dumps({'status': record['status'], 'actual_utc': now,
                  'record': str(audit.relative_to(root)),
                  'runtime_seconds': result['runtime_seconds'], 'labels': labels}))
