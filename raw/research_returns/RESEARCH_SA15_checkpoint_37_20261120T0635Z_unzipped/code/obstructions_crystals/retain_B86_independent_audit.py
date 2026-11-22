"""Full B86 proof/source audit and literal unchanged certificate rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
author = root / 'agents/reduction_descent'
source = author / 'B_first_wild_cyclotomic_quotient_candidate.tex'
program = author / 'code/verify_first_wild_cyclotomic_quotient.py'
author_output = program.with_suffix('.output.json')
expected = {
    source: 'ad8b70dc7b353f54ac8833794a2f962d916ec6f663f31f616fef85ddb33ddee6',
    program: 'f8084e1c2e0780e20fe9939857c38c6aceb5560d8188be038f009673f50854c2',
    author_output: '8d4f374be4b8ed343cb5af51eec58014bf61226bbe820d7ef704390df50e2e92',
}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

for path, digest in expected.items():
    assert sha(path) == digest, str(path)
copied = own / 'code/B86_independent_check.py'
assert not copied.exists()
copied.write_bytes(program.read_bytes())
run = subprocess.run([sys.executable, str(copied)], cwd=root,
                     capture_output=True, text=True)
copied.with_suffix('.stdout.txt').write_text(run.stdout)
copied.with_suffix('.stderr.txt').write_text(run.stderr)
hashes = {str(path.relative_to(root)): {'before': digest, 'after': sha(path)}
          for path, digest in expected.items()}
hash_path = own / 'outputs/B86_author_hashes_preserved.json'
hash_path.write_text(json.dumps(hashes, indent=2)+'\n')
assert all(row['before'] == row['after'] for row in hashes.values())
assert run.returncode == 0, run.stderr
result = json.loads(copied.with_suffix('.output.json').read_text())
assert result['status'] == 'PASS'
assert result['counts'] == json.loads(author_output.read_text())['counts']
now = datetime.now(timezone.utc).isoformat()
labels = ['lem:B-RD86-cyclotomic', 'prop:B-RD86-traceless',
          'cor:B-RD86-tame', 'rem:B-RD86-scope']
record = {
    'status': 'FULL PASS', 'actual_utc': now,
    'candidate': str(source.relative_to(root)),
    'candidate_sha256': expected[source], 'labels': labels,
    'proof_read_scope': 'Entire final four-label B86 proof and standalone checker read. B85 was completely independently audited immediately before this audit, including fresh full B83/B69 reads and the entire B60 lower-break proof. The determinant bridge is used in its previously audited whole-height-two good-reduction scope; the new cyclotomic calculation and quotient field were fully rederived here.',
    'checks': [
        'Since mu_p is contained in K, adjoining mu_p2 has degree dividing p; containment in the tame degree-N extension forces containment in K. Cohen structure supplies an embedded complete unramified DVR with the same perfect residue field. Eisenstein Phi_p2(1+T) and the exact absolute index make zeta_p2-1 a uniformizer of K. Completeness and fixed residue representatives prove O_K=Lambda[zeta_p2] and K=Frac(Lambda)(zeta_p2), with no uniqueness assumption on the coefficient ring.',
        'The next cyclotomic extension has degree p and uniformizer zeta_p3-1. Its nonidentity displacement has valuation p2, hence break N. The tame degree-N base change is disjoint; an N-th root of that uniformizer exists in the composite because its residue field is algebraically closed and N is invertible. The wild automorphism has residue-one uniformizer ratio, so the N-th-power identity multiplies the break by N, giving exactly N2 over L.',
        'Traceless W1 makes the actual determinant trivial modulo p2, so mu_p2 is in L. The cyclotomic calculation proves that the determinant modulo p3 is nevertheless nonzero of order p. Traceless W2 kills only its terminal restriction, allowing it to descend to a nonzero additive functional ell on W1. Actual tame-conjugation invariance kills both nontrivial off-diagonal weights, while ell(H) is nonzero. No false inference from terminal trace zero to total determinant zero is used.',
        'For a primitive second-level point over e1, W1=sl2 acts by its full first column. The actual common point field E/L is Galois of degree q, with quotient sl2/<E12>. Its full stabilizer contains the terminal layer and projects to <E12>; both are killed by the determinant. Thus the actual cyclotomic field C=L(mu_p3) is a subfield of this same point field, not merely an abstract quotient representation.',
        'A class aH+cE21 has nontrivial cyclotomic image exactly when a is nonzero. In the second model its translation is then low. The actual coordinate and displacement valuations on E are p*k2 and p3*k2. The universal lower-break inequality, which requires no prime valuation, bounds every lift in that coset by p*N*k2<N2.',
        'Colmez Proposition3.7 gives the exact average of i=b+1 over the p lifts to a quotient element; both extensions here are totally ramified. Applying the strict bound to every lift yields a quotient break smaller than N2, contradicting the independently computed cyclotomic break. No replacement of lower numbering by upper numbering is made.',
        'B85 gives both matrix dimensions at least three and actual p-th powers give W1 contained in W2. A total at most six would make them equal three-spaces. B83 supplies E12,E21 and their commutator H, forcing both spaces to be sl2, now excluded. This yields p7 only in the stated tame reducible sector; the other residual sectors and the remaining p7/p8 possibilities stay open.'
    ],
    'primary_sources': [
        {'title': 'Stacks Project, Theorem10.160.8, Tag032A',
         'url': 'https://stacks.math.columbia.edu/tag/032A',
         'web_ref': 'turn538475100view0',
         'actual_read_scope': 'Full theorem and entire coefficient-ring existence proof freshly opened and read, including its mixed-characteristic inverse-limit construction.'},
        {'title': 'Pierre Colmez, Corps locaux, notes du cours de M2',
         'url': 'https://webusers.imj-prg.fr/~pierre.colmez/CL.pdf',
         'web_refs': ['turn538475100view1', 'turn629449226view0', 'turn629449226view1'],
         'retained_original_text': 'agents/reduction_descent/sources/colmez_corps_locaux.txt',
         'retained_text_sha256': sha(author/'sources/colmez_corps_locaux.txt'),
         'actual_read_scope': 'Original PDF freshly opened; introductory complete-discrete-field scope read. Proposition2.12 and its full Hensel/uniformizer proof on p11, and Section3.1 definitions plus Proposition3.7 with its complete two-divisibility norm-polynomial proof on pp14-15, freshly read from the retained original text. No finite-residue hypothesis is present. No new image-view claim.'}
    ],
    'independent_program': str(copied.relative_to(root)),
    'independent_output': str(copied.with_suffix('.output.json').relative_to(root)),
    'independent_runtime_seconds': result['runtime_seconds'],
    'counts': result['counts'], 'finite_scope': result['scope'],
    'author_bytes_unchanged': True, 'hash_record': str(hash_path.relative_to(root)),
    'scope': 'The actual traceless three-plus-three layer case is excluded using a cyclotomic subfield and quotient ramification. For p=1 modulo4 the different-character tame reducible first-wild sector must have order at least p7. The remaining two image dimensions and the full least-index question are not decided.'
}
audit = own / 'B86_independent_audit.json'
with audit.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'independent_full_proof_source_code_audit',
                           str(source.relative_to(root)),
                           'Complete cyclotomic coefficient-field and actual point-field quotient proof; full primary passages; literal isolated certificate',
                           'PASS', str(audit.relative_to(root))])+'\n')
print(json.dumps({'status': record['status'], 'actual_utc': now,
                  'record': str(audit.relative_to(root)),
                  'runtime_seconds': result['runtime_seconds'], 'labels': labels}))
