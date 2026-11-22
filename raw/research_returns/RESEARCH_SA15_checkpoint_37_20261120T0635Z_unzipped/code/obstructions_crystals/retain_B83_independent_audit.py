"""Retain the complete B83 companion audit and an unchanged isolated run."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
author = root / 'agents/reduction_descent'
source = author / 'B_first_wild_swapped_quotients_candidate.tex'
program = author / 'code/verify_first_wild_swapped_quotients.py'
author_output = program.with_suffix('.output.json')
expected = {
    source: '453ca8011e454fcb1360ccf27195d7b8a5db633d6383cd3048a9bae8d9b83d40',
    program: '8e4e4decea77980e34a32f2d83d37e1c24aa2a49b2faa55faf47fd1fb7276fc4',
    author_output: 'e78f7e183fd17bbdafdfff9ecfbb0533c0df7ee670325bd6d58539e6ab45b4aa'
}
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
for path, digest in expected.items():
    assert sha(path) == digest, str(path)
copied = own / 'code/B83_independent_check.py'
assert not copied.exists()
copied.write_bytes(program.read_bytes())
run = subprocess.run([sys.executable, str(copied)], cwd=root,
                     capture_output=True, text=True)
copied.with_suffix('.stdout.txt').write_text(run.stdout)
copied.with_suffix('.stderr.txt').write_text(run.stderr)
hashes = {str(path.relative_to(root)): {'before': digest, 'after': sha(path)}
          for path, digest in expected.items()}
hash_path = own / 'outputs/B83_author_hashes_preserved.json'
hash_path.write_text(json.dumps(hashes, indent=2)+'\n')
assert all(row['before'] == row['after'] for row in hashes.values())
assert run.returncode == 0, run.stderr
result = json.loads(copied.with_suffix('.output.json').read_text())
assert result['status'] == 'PASS'
assert result['counts'] == json.loads(author_output.read_text())['counts']
now = datetime.now(timezone.utc).isoformat()
labels = ['lem:B-RD83-tame', 'lem:B-RD83-quotients', 'prop:B-RD83-Lie',
          'cor:B-RD83', 'rem:B-RD83-scope']
record = {
    'status': 'FULL PASS', 'actual_utc': now,
    'candidate': str(source.relative_to(root)), 'candidate_sha256': expected[source],
    'labels': labels,
    'proof_read_scope': 'Entire final B83 source and entire standalone checker read. Freshly reread the full B69 actual quotient, inherited-character and generic-descent proof, its common-point-field argument and leading-coordinate scalar/irreducible dichotomy; the complete canonical B81 proof and scope were read for the final assembly. B82 was independently rederived in full immediately before this audit, including its direct determinant delta. B60 lower-break and B49 coefficient proofs, B76 determinant detection and B77 square exclusion were freshly read in that preceding audit.',
    'checks': [
        'With rational first-level torsion, a primitive lift above an outside-both residual vector has a common Galois point field of degree at most q; its prime b/q denominator forces degree exactly q and every translation. A translation outside both high lines therefore has the same exact lower break N*b_i, giving b1=b2. The argument uses no prime-to-p assumption on the absolute index.',
        'For B_i=p^2*k_i with 1<=k_i<=p-2, every B_i>e. The actual Weierstrass quotient product gives high parameter s-B_i=p(N-p*k_i) and low parameter B_i/p=p*k_i. Each quotient has a two-slope polygon and both divided parameters are prime to p; N-p*k_i>=2p-1>k_j.',
        'Both stable lines are actual inertia-stable subgroup schemes of the common first-level representation. Their schematic closures and finite-flat quotients exist over the good field; the inherited generic semilinear cocycles descend the generic quotients. The exact subquotient {P in M[p^3]:p^2 P in J}/J identifies the quotient p^2 representations, with no lost torsion level or integral descent claim.',
        'Each quotient residual representation is a subquotient of the original p-group over L. If tame it is trivial, contradicting the common-point-field equality for unequal prime b-parameters. Its actual old first-level image gives an invariant line, so the residual wild action is nontrivial unipotent.',
        'The actual quotient Tate lattice is T+Z_p(e1/p), not the opposite lattice. Its matrix is [[rho11,p*rho12],[rho21/p,rho22]], so quotient wild action detects A21 of the original W1. The other quotient detects A12 of the same W1. The given actual finite-level comparison suffices to identify these coefficients; no full Tate-module isomorphism is assumed.',
        'For p=1 mod4 and nonsquare finite determinant, the residual diagonal ratio alpha/beta is nonsquare and cannot equal either 1 or -1. Thus the three adjoint weights 1,rho,rho^-1 are distinct. Polynomial spectral projectors on the invariant W1 isolate both matrix units E12 and E21 from its two nonzero projections.',
        'Actual pth powers place W1 in W2, and actual commutators place [E12,E21]=diag(1,-1) in W2 independently of lift coefficients. Hence dim W1>=2 and dim W2>=3, giving the actual group order bound p^5.',
        'The final assembly treats irreducible residual inertia by B81, nontrivial residual wild inertia by B82, and tame reducible inertia by the one-slope scalar-determinant exclusion, the prime-b point-field denominator, common-high determinant congruences, or the exchanged-high quotient argument. The p=3 mod4 order-two weight case is explicitly excluded from the new theorem. No larger-image exclusion, example, or exact first-wild index follows.'
    ],
    'primary_source_scope': 'No new external original-source read claimed. All new statements are direct point-field, lattice, finite-flat quotient and matrix arguments, with the internal source bridges and proved dependencies scoped as above.',
    'independent_program': str(copied.relative_to(root)),
    'independent_output': str(copied.with_suffix('.output.json').relative_to(root)),
    'independent_runtime_seconds': result['runtime_seconds'],
    'counts': result['counts'], 'author_bytes_unchanged': True,
    'hash_record': str(hash_path.relative_to(root)), 'finite_scope': result['scope']
}
audit = own / 'B83_independent_audit.json'
with audit.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'independent_full_proof_code_audit',
                           str(source.relative_to(root)),
                           'Complete proof and exact dependency steps rederived; unchanged isolated certificate and author hashes',
                           'PASS', str(audit.relative_to(root))])+'\n')
print(json.dumps({'status':record['status'], 'actual_utc':now,
                  'record':str(audit.relative_to(root)),
                  'runtime_seconds':result['runtime_seconds'], 'labels':labels}))
