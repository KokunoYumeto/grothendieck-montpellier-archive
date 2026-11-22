#!/usr/bin/env python3
"""Exact local trace-zero factorization and graph pairing in characteristic two.

This supplements the global acyclicity/Serre-duality proof. It does not
establish any lower bound for the actual variation-image dimension.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
import sympy as S

start = time.perf_counter()
u, h, w, b, c, d, x, y, z, t = S.symbols('u h w b c d x y z t')
variables = (u, h, w, b, c, d, x, y, z, t)

def zero_char_two(expr):
    numerator, denominator = S.fraction(S.cancel(expr))
    assert denominator != 0
    return S.Poly(S.expand(numerator), *variables, modulus=2).is_zero

J = S.Matrix([[0, 1], [1, 0]])
a = S.Matrix([[1, u*h*h], [0, w]])
f = S.diag(u*w, 1)
pairing_G = u*J
inverse_pairing_G = J/u
identities = 0
for value in pairing_G*inverse_pairing_G-S.eye(2):
    assert zero_char_two(value)
    identities += 1
for value in a*J*a.T-f*inverse_pairing_G*f.T:
    assert zero_char_two(value)
    identities += 1
for value in a*J*a.T-w*J:
    assert zero_char_two(value)
    identities += 1

# A trace-zero twisted endomorphism maps to K, and scalars disappear in Q.
phi = S.Matrix([[c, b], [d, c]])
s0 = S.Matrix([1, 0])
s1 = S.Matrix([h, w])
first = u*phi*s1
second = phi*s0
contraction = first[1] + u*(h*second[1]+w*second[0])
assert zero_char_two(contraction)
image_Q = S.Matrix([first[0]+u*h*second[0], second[1]])
for value in image_Q-S.Matrix([u*w*b, d]):
    assert zero_char_two(value)
    identities += 1
identities += 1

# The isotropic-graph equation is precisely trace zero for a 2x2 matrix.
T = S.Matrix([[x, y], [z, t]])
for value in J*T+T.T*J-(x+t)*J:
    assert zero_char_two(value)
    identities += 1

# The one-line conclusion is checked by its universal polynomial identity.
N = S.Matrix([[0, 1], [0, 0]])
B = S.Matrix([[x, y], [z, x]])
assert zero_char_two((N+t*B).det()-(t*z+t*t*(x*x+y*z)))
identities += 1

# Independent finite supplement: every pair of independent nonzero nilpotent
# traceless matrices over F4 has nonsingular sum. This is not the proof.
def add(a, b):
    return a ^ b

def mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return result

def determinant(v):
    aa, bb, cc = v
    return mul(aa, aa) ^ mul(bb, cc)

nilpotents = [(aa, bb, cc) for aa in range(4) for bb in range(4)
              for cc in range(4) if (aa or bb or cc)
              and determinant((aa, bb, cc)) == 0]
pair_count = 0
for i, v in enumerate(nilpotents):
    line = {tuple(mul(c, entry) for entry in v) for c in range(4)}
    for other in nilpotents[i+1:]:
        if other in line:
            continue
        assert determinant(tuple(add(a, b) for a, b in zip(v, other))) != 0
        pair_count += 1

result = {
    'status': 'PASS',
    'actual_utc': datetime.now(timezone.utc).isoformat(),
    'elapsed_seconds': time.perf_counter()-start,
    'universal_scalar_identities': identities,
    'F4_nonzero_nilpotents': len(nilpotents),
    'F4_independent_nilpotent_pairs': pair_count,
    'local_unit_retained': 'e^2=u, trace pairing uJ, inverse pairing u^-1 J',
    'scope': 'Exact local identities only. Global acyclicity and duality are proved in the companion TeX; no variation-image lower bound is asserted.'
}
Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/outputs/root_positive_trace_zero_factorization.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
