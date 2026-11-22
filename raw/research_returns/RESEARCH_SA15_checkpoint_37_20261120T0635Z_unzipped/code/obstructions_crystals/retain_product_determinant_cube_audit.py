"""Full independent audit of the actual one-axis product cross determinant."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
author = root / 'agents/monodromy'
source = author / 'post_CP34_product_twisted_determinant_cube_candidate.tex'
program = author / 'code/verify_ss_product_one_axis_determinant_cube.py'
author_output = program.with_suffix('.output.json')
expected = {
    source: '0f67ca3f9ff32439e04dd2dfb319bb5e85ef21cb746eaf5fc7201b31b51f76b0',
    program: '0ccf9e7a71f04fbe8c28692e3187e26ebe9422c6d89770adf830907cb21dd65e',
    author_output: '03f9abaefe9790b9fa1b19ce6b1f742be1fa7a1906aa70490a4421419ae122bc',
}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for p, h in expected.items():
    assert sha(p) == h, str(p)
labels = re.findall(r'\\label\{([^}]+)\}', source.read_text())
assert len(labels) == 3
isolated = own / 'outputs/product_determinant_cube_independent_run'
isolated.mkdir(exist_ok=False)
copied = isolated / program.name
copied.write_bytes(program.read_bytes())
assert sha(copied) == expected[program]
run = subprocess.run([sys.executable, str(copied)], cwd=isolated,
                     capture_output=True, text=True)
(isolated / 'stdout.txt').write_text(run.stdout)
(isolated / 'stderr.txt').write_text(run.stderr)
preserved = {str(p.relative_to(root)): {'before': h, 'after': sha(p)}
             for p, h in expected.items()}
(isolated / 'author_hashes.json').write_text(json.dumps(preserved, indent=2) + '\n')
assert all(v['before'] == v['after'] for v in preserved.values())
assert run.returncode == 0, run.stderr
result = json.loads(copied.with_suffix('.output.json').read_text())
original = json.loads(author_output.read_text())
math_fields = lambda d: {k: v for k, v in d.items()
                        if k not in ('actual_utc', 'runtime_seconds')}
assert result['status'] == 'PASS' and math_fields(result) == math_fields(original)
now = datetime.now(timezone.utc).isoformat()
dependency = own / 'A4_ss_product_dual_Cartier.tex'
record = {
    'status': 'FULL-INDEPENDENT-PROOF-CODE-PASS',
    'actual_utc': now,
    'candidate': str(source.relative_to(root)),
    'candidate_sha256': expected[source],
    'labels': labels,
    'proof_read_scope': 'Entire final three-label proof and complete standalone exact checker read. Entire canonical supersingular-product dual-Cartier dependency freshly reread, including the actual relative-Cartier elliptic bases, rational product trivialization, p-basis calculation and tensor/Schur argument. No new external-source opening or numerical-to-uniform inference is claimed.',
    'dependency': str(dependency.relative_to(root)),
    'dependency_sha256': sha(dependency),
    'checks': [
        'The source spaces are H0(M_E P1) and H0(M_E P1^-1) with the exact degree3 bases in the canonical elliptic lemma. Relative Cartier targets the actual Frobenius-twisted line, and its coefficient matrices are precisely A0,R,A2. On the untwisted factor the B_j form all alternating forms on a three-space. Kunneth therefore gives the actual full nine-variable matrix sum t_ij A_i tensor B_j.',
        'With the stated definition g^t B_j g=sum_k S(g)_kj B_k, S is the pullback action and is conjugate, through the fixed volume-basis permutation, to det(g)g^-1. The original inverse-transpose sentence was a convention slip; the retained exact two-line delta now corrects it. The determinant character remains det(S)=det(g)^2.',
        'The full matrix covariance is C(T S^t)=(I tensor g^t) C(T)(I tensor g), so its determinant gains det(g)^6=det(S)^3. Every invertible S is reached on geometric points: choose delta^2=det(h) and g=delta h^-1 after the fixed volume identification. This uses existence of square roots over the algebraically closed field, not etaleness or separability of the exterior-square map.',
        'Right multiplication is transitive on invertible coefficient matrices T, hence detC(T)/det(T)^3 is constant there. The fixed permutation T with t10=t01=t22=1 has determinant1, and its exact Schur complement is [[0,1,a],[1,0,0],[a,0,1]], of determinant1 uniformly in the twist. Thus the constant is1, and density gives the universal full polynomial identity for every nontrivial P1.',
        'For rank2 T its column span in span(A0,R,A2) is two-dimensional. The determinant on that three-space is r^2t+rt^2+s^3, whose partial derivatives t^2,s^2,r^2 have no common projective zero. A smooth plane cubic contains no line, so this span contains an invertible U. The surjective right-coordinate action puts its columns into U,V,0. The resulting block matrix has exact kernel(0,U^-1 Vz,z) and a nonzero six-minor det(U)^2, hence rank exactly6.',
        'For rank1 T the matrix is a single tensor A tensor B with B a nonzero alternating three-by-three matrix of rank2, so its rank is at most6. Rank0 gives0, and rank3 gives9. Therefore rank8 never occurs. The ordinary determinant hypersurface of three-by-three matrices is reduced irreducible with dense rank2 orbit and nonzero adjugate there; detC=det(T)^3 gives multiplicity exactly3.',
        'The69-check program verifies universal elliptic/Schur and exterior-square identities, the symbolic kernel/minor, and a complete independent36-term cube reconstruction at the nontrivial point(a,b)=(0,0). The theorem uniformity comes from covariance and the universal unit proof, not that single specialization. The prior multivariate-gcd exception is explicitly retained and contributes no mathematical inference.',
        'The conclusion refutes automatic reduced corank-one behavior for a nonzero actual twisted product cross determinant. It does not identify a whole Frobenius-cycle operator, infer its stable rank or inertia, give a nonproduct factorization, or contradict previously proved full product monodromy.'
    ],
    'covariance_delta': 'agents/monodromy/notes/CP35_product_covariance_transpose_repair/exact.diff',
    'prior_candidate_sha256': 'e72b7b7f6083c1e5f0eb42683a7afcc6ed80c372010565eef15849e48ca7e812',
    'independent_program': str(copied.relative_to(root)),
    'independent_output': str(copied.with_suffix('.output.json').relative_to(root)),
    'independent_runtime_seconds': result['runtime_seconds'],
    'independent_result_utc': result['actual_utc'],
    'program_sha256': sha(copied),
    'all_mathematical_output_identical': True,
    'author_bytes_unchanged': True,
    'exact_checks': result['check_count'],
    'full_determinant_term_count': result['full_determinant_term_count'],
    'scope': 'Actual one-axis supersingular-product relative cross pencil only; uniform determinant cube and rank6 along its rank2 coefficient locus.'
}
audit = own / 'product_determinant_cube_independent_audit.json'
with audit.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([
            now, label, 'independent_full_proof_code_audit', str(source.relative_to(root)),
            'Complete actual relative-Cartier dependency, covariance and rank proof; literal unchanged69-check isolated run',
            'PASS', str(audit.relative_to(root)),
        ]) + '\n')
print(json.dumps({
    'status': record['status'], 'actual_utc': now,
    'record': str(audit.relative_to(root)), 'candidate_sha256': expected[source],
    'independent_runtime_seconds': result['runtime_seconds'],
    'checks': result['check_count'], 'author_unchanged': True,
}))
