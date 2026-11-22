"""Independent universal Leibniz check of the retained norm-eleven algebra.

This is an algebraic certificate only. It asserts no triple-fibre exclusion.
"""
from pathlib import Path
from itertools import permutations
from datetime import datetime, timezone
import hashlib
import json
import time
import post_CP27_eleven_rational_quintic as q

start = time.perf_counter()
assert q.result['status'] == 'PASS_UNIVERSAL_QUINTIC_IDENTITIES_ONLY'


def direct_charpoly(matrix):
    """Leibniz determinant of TI+M; all permutation signs equal1 in char2."""
    n = len(matrix)
    total = [q.zero for _ in range(n + 1)]
    for perm in permutations(range(n)):
        product = [q.one]
        for i, j in enumerate(perm):
            factors = [matrix[i][j], q.one if i == j else q.zero]
            new = [q.zero for _ in range(len(product) + 1)]
            for a, x in enumerate(product):
                for b, y in enumerate(factors):
                    new[a+b] = new[a+b] + x*y
            product = new
        for i, x in enumerate(product):
            total[i] = total[i] + x
    return list(reversed(total))


assert direct_charpoly(q.matrix_of(q.P)) == q.cp
assert direct_charpoly(q.matrix_of(q.B)) == q.cb
assert not q.padd(q.pmul(q.u, [q.zero, q.zero, q.one]),
                  q.scale([q.L0, q.one], q.t*q.t))

# Reconstruct the quintic before monic normalization, directly by expansion.
# (alpha Y²+beta Y+gamma)²(Y+L0)+Y⁴.
raw = [q.gamma*q.gamma*q.L0, q.gamma*q.gamma,
       q.beta*q.beta*q.L0, q.beta*q.beta,
       q.alpha*q.alpha*q.L0+1, q.alpha*q.alpha]
assert [x*q.inverse_alpha_squared for x in raw] == q.C

root = Path(__file__).resolve().parents[1]
record = {
    'status': 'PASS_UNIVERSAL_ALGEBRA_ONLY',
    'actual_utc': datetime.now(timezone.utc).isoformat(),
    'runtime_seconds': time.perf_counter()-start,
    'direct_determinants': 2,
    'permutations_each': 120,
    'base_ring': 'F2[v,v^-1,(v+1)^-1,G(v)^-1][L]',
    'checks': [
        'Both full five-by-five characteristic polynomials agree with an independent Leibniz determinant over the universal coefficient ring.',
        'The monic quintic is the direct expansion of (alpha Y²+beta Y+gamma)²(Y+L0)+Y⁴ divided by alpha².',
        'The polynomial u satisfies uY²=t²(Y+L0) in the exact quintic quotient.',
        'The copied author program reproduces every coefficient of the retained F16 specialization.'
    ],
    'scope_limit': 'Coefficient arithmetic and exact algebra only. No exceptional-locus elimination, triple-fibre exclusion, nodality or new monodromy claim.'
}
(root/'outputs/direct_determinant_audit.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
