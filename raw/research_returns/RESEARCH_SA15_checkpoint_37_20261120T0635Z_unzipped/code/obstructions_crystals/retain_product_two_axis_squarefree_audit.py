"""Independent full audit of the actual two-axis Cartier determinant."""
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
source = author / 'post_CP35_product_two_axis_squarefree_candidate.tex'
program = author / 'code/verify_ss_product_two_axis_squarefree.py'
author_output = program.with_suffix('.output.json')
expected = {
    source: 'e5f2460eb4a5ed0e644963a1ebda95dc8c6eb6b02b535f68292e10bdfe479930',
    program: '2a7cf8bd3ae58083671b42dd85f01d1423703f18f10ee71183d84aeeb66699b6',
    author_output: 'cd2f66b0baea14c56607073fc7a1c145cfa3e0a8c881a3d84fd55d0ce506dc80',
}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
for p, h in expected.items():
    assert sha(p) == h, str(p)
labels = re.findall(r'\\label\{([^}]+)\}', source.read_text())
assert len(labels) == 4
isolated = own / 'outputs/product_two_axis_squarefree_independent_run'
isolated.mkdir(exist_ok=False)
copied = isolated / program.name
copied.write_bytes(program.read_bytes())
assert sha(copied) == expected[program]
run = subprocess.run([sys.executable, str(copied)], cwd=isolated,
                     capture_output=True, text=True)
(isolated / 'stdout.txt').write_text(run.stdout)
(isolated / 'stderr.txt').write_text(run.stderr)
hashes = {str(p.relative_to(root)): {'before': h, 'after': sha(p)}
          for p, h in expected.items()}
(isolated / 'author_hashes.json').write_text(json.dumps(hashes, indent=2) + '\n')
assert all(v['before'] == v['after'] for v in hashes.values())
assert run.returncode == 0, run.stderr
result = json.loads(copied.with_suffix('.output.json').read_text())
original = json.loads(author_output.read_text())
math_fields = lambda d: {k: v for k, v in d.items()
                       if k not in ('actual_utc', 'runtime_seconds')}
assert result['status'] == 'PASS'
assert math_fields(result) == math_fields(original)
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'FULL PASS',
    'actual_utc': now,
    'candidate': str(source.relative_to(root)),
    'candidate_sha256': expected[source],
    'labels': labels,
    'proof_read_scope': (
        'Entire final four-label candidate, complete universal pure-binary checker and complete '
        'author JSON read. The actual elliptic relative-Cartier table and product tensor proof '
        'in A4_ss_product_dual_Cartier.tex were freshly reread. Each homogeneous and geometric '
        'deduction was independently rederived. The checker is copied literally, not modified.'),
    'checks': [
        'A nontrivial Picard point on the supersingular elliptic curve is finite and satisfies b^2+b=a^3. The displayed three matrices are exactly the coefficient matrices of the already proved relative-Cartier cross table. Kunneth and relative Cartier therefore give the actual9-by9 product matrix sum Xij Ai tensor Aj, not an arbitrary pencil model.',
        'The coefficient ring used by the checker is free over F2[a,c,t] with basis1,b,d,bd, because both elliptic equations are monic in their separate quadratic variables. The XOR sets and multiplication correctly reduce b^2 to b+a^3 and d^2 to d+c^3. No sample specialization or determinant package is used.',
        'The subset-permutation dynamic program computes all determinant terms with their correct characteristic-two signs. The three reconstructed determinants are the original line, the negated first elliptic point on that line, and the original point on the changed line. Their full reduced polynomial identities agree exactly.',
        'The fixed-line determinant is homogeneous degree9. Its U=1 identity homogenizes to u^2 T^9+v^2 T^8 U+w^2(T^7 U^2+T^6 U^3)+T U^8+U^9. The relations give u=b+d+ac+a+1, v=c(a+1), w=ac+a+c and u+v=b+d+a+c+1.',
        'Direct homogeneous differentiation gives the stated two squares. Their roots differ by Delta*T^4. If Delta is nonzero, a common projective zero would force T=0 and then U=0. This includes infinity and the case u=0, when infinity may be a simple root. The code checks F_T on U=1 and F_U through F+t*F_T, using the odd-degree Euler identity.',
        'Replacing b by b+1 preserves the elliptic equation and changes A0 to A0+A2. On the original functional matrix this is exactly addition of row0 to row2, an invertible linear change. It changes Delta by1. Thus one of the two fixed lines has a squarefree restriction for every actual nontrivial pair, without replacing the original pencil or imposing any torsion-order condition.',
        'A repeated homogeneous irreducible factor of the full determinant restricts nontrivially to any line with nonzero determinant restriction. Its restriction is homogeneous of its original positive degree and has a projective root over the algebraically closed field; that root would be repeated. This proves full geometric squarefreeness from the binary certificate.',
        'At a generic point of each reduced determinant component, some first derivative is nonzero. Matrix corank at least2 would kill every cofactor, and hence every determinant derivative. Therefore the generic cross rank is8 on every component. This statement concerns a single cross block, not a Frobenius-cycle composition.',
        'In the stated actual family, local trivializations lift the two functional directions and their independence persists after shrinking. The common-zero locus of the two homogeneous derivatives is closed in a proper relative projective line. Its image is closed and misses the product point, providing an open containing that point on which each binary restriction, and therefore each full determinant, is geometrically reduced. No global reachability of a specified nonproduct surface or torsion section is asserted.'
    ],
    'source_scope': {
        'fresh_internal_dependency': 'agents/obstructions_crystals/A4_ss_product_dual_Cartier.tex',
        'new_external_source_openings': [],
        'no_inflation': 'No new numerical sampling, external-source opening or PDF-image inspection claimed. The exact universal binary determinant reconstruction is the independent run below.'
    },
    'independent_program': str(copied.relative_to(root)),
    'independent_output': str(copied.with_suffix('.output.json').relative_to(root)),
    'independent_runtime_seconds': result['runtime_seconds'],
    'independent_result_utc': result['actual_utc'],
    'program_sha256': sha(copied),
    'all_mathematical_output_identical': True,
    'author_bytes_unchanged': True,
    'universal_reduced_term_count': result['universal_reduced_term_count'],
    'identities': result['identities'],
    'scope': 'Every two-axis nontrivial twist on the actual supersingular elliptic product has a geometrically squarefree cross determinant and generic corank1 on every component. Local family openness only; no cycle stable-rank, full inertia, nonproduct uniformity or global monodromy inference.'
}
audit = own / 'product_two_axis_squarefree_independent_audit.json'
with audit.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([
            now, label, 'independent_full_proof_code_audit', str(source.relative_to(root)),
            'Actual relative-Cartier tensor dependency; universal binary determinant; homogeneous squarefreeness and deformation scope; unchanged isolated run',
            'PASS', str(audit.relative_to(root)),
        ]) + '\n')
print(json.dumps({
    'status': 'FULL PASS', 'actual_utc': now, 'record': str(audit.relative_to(root)),
    'candidate_sha256': expected[source], 'labels': labels,
    'independent_runtime_seconds': result['runtime_seconds'],
    'all_mathematical_output_identical': True, 'author_bytes_unchanged': True,
    'universal_reduced_term_count': result['universal_reduced_term_count'],
}))
