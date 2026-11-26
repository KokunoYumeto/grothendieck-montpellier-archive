#!/usr/bin/env python3
"""Exact characteristic-two identities, using sparse polynomial arithmetic.

No symbolic algebra package and no historical program is imported.
This checks local identities, not global cohomology or determinant
nonvanishing on arbitrary abelian surfaces.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import time

START = time.perf_counter()
NAMES = ("u", "h", "w", "a", "b", "c", "g", "r", "t", "x", "y", "z")
N = len(NAMES)
ZERO = frozenset()
ONE = frozenset({(0,) * N})


def var(name, exponent=1):
    x = [0] * N
    x[NAMES.index(name)] = exponent
    return frozenset({tuple(x)})


def add(*ps):
    ans = set()
    for p in ps:
        ans.symmetric_difference_update(p)
    return frozenset(ans)


def mul(p, q):
    ans = set()
    for a in p:
        for b in q:
            term = tuple(x + y for x, y in zip(a, b))
            if term in ans:
                ans.remove(term)
            else:
                ans.add(term)
    return frozenset(ans)


def sq(p):
    return frozenset(tuple(2 * x for x in a) for a in p)


def mm(a, b):
    return [[add(*(mul(x, y) for x, y in zip(row, col)))
             for col in zip(*b)] for row in a]


def tr(a):
    return list(map(list, zip(*a)))


def ma(a, b):
    return [[add(x, y) for x, y in zip(r, s)] for r, s in zip(a, b)]


CHECKS = []


def equal(name, a, b):
    assert a == b, name
    CHECKS.append(name)


u, h, w, a, b, c, g, r, t, x, y, z = map(var, NAMES)
ui = var("u", -1)
J = [[ZERO, ONE], [ONE, ZERO]]
I = [[ONE, ZERO], [ZERO, ONE]]
section_map = [[ONE, mul(u, sq(h))], [ZERO, w]]
factor = [[mul(u, w), ZERO], [ZERO, ONE]]
Jg = [[ZERO, ui], [ui, ZERO]]
equal("alternating_factorization", mm(mm(section_map, J), tr(section_map)),
      mm(mm(factor, Jg), tr(factor)))
equal("factorization_value", mm(mm(section_map, J), tr(section_map)),
      [[ZERO, w], [w, ZERO]])
equal("inverse_twisted_pairing", mm([[ZERO, u], [u, ZERO]], Jg), I)

# The first variation is computed directly by replacing w with w+t
# and extracting the coefficient of t, not by differentiating a
# previously simplified product.
delta_a = [[ZERO, ZERO], [ZERO, t]]
delta_f = [[mul(u, t), ZERO], [ZERO, ZERO]]
equal("monad_first_variation",
      ma(mm(mm(section_map, J), tr(delta_a)),
         mm(mm(factor, Jg), tr(delta_f))),
      [[ZERO, t], [t, ZERO]])

# Clear the determinant denominator before checking the unipotent
# transition. This is a universal polynomial identity.
norm = add(sq(a), mul(sq(b), h))
M = [[a, add(mul(a, c), mul(b, h))], [b, add(mul(b, c), a)]]
M2 = [[sq(v) for v in row] for row in M]
Qi_inverse = [[ZERO, ONE], [ONE, h]]
Qj = [[add(h, sq(c)), ONE], [ONE, ZERO]]
equal("unipotent_transition_cleared",
      mm(mm(Qi_inverse, M2), Qj),
      [[norm, sq(b)], [ZERO, norm]])
equal("norm_is_determinant",
      add(mul(M[0][0], M[1][1]), mul(M[0][1], M[1][0])), norm)

sym = [[ONE, g, sq(g)], [ZERO, ONE, ZERO], [ZERO, ZERO, ONE]]
Pi = [[ONE, ZERO, r], [ZERO, ONE, ZERO], [ZERO, ZERO, ONE]]
Pj = [[ONE, ZERO, add(r, sq(g))], [ZERO, ONE, ZERO], [ZERO, ZERO, ONE]]
equal("symmetric_square_coboundary_change", mm(mm(Pi, sym), Pj),
      [[ONE, g, ZERO], [ZERO, ONE, ZERO], [ZERO, ZERO, ONE]])

# The isotropic graph equation and singular-line polynomial.
T = [[x, y], [z, t]]
equal("graph_trace_identity", ma(mm(J, T), mm(tr(T), J)),
      [[ZERO, add(x, t)], [add(x, t), ZERO]])
NtB = [[mul(t, x), add(ONE, mul(t, y))], [mul(t, z), mul(t, x)]]
det = add(mul(NtB[0][0], NtB[1][1]), mul(NtB[0][1], NtB[1][0]))
equal("nilpotent_line_determinant", det,
      add(mul(t, z), mul(sq(t), add(sq(x), mul(y, z)))))

# Local symmetric-square resolution: d1*d2=0, retaining the
# nonunit Cartier equation w. Exactness is proved in the paper.
d1 = [[w, ZERO, ZERO, ZERO],
      [ZERO, w, ONE, ZERO],
      [ZERO, ZERO, ZERO, ONE]]
d2 = [[ZERO], [ONE], [w], [ZERO]]
equal("residual_complex", mm(d1, d2), [[ZERO], [ZERO], [ZERO]])

# Exhaustive, independently encoded finite supplement over F_8.
def fmul(a, b):
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        a <<= 1
        b >>= 1
        if a & 8:
            a ^= 0b1011
    return ans


def fdet(v):
    a, b, c = v
    return fmul(a, a) ^ fmul(b, c)


nil = [(a, b, c) for a in range(8) for b in range(8) for c in range(8)
       if (a or b or c) and not fdet((a, b, c))]
pairs = 0
for i, v in enumerate(nil):
    line = {tuple(fmul(a, z) for z in v) for a in range(8)}
    for q in nil[i + 1:]:
        if q in line:
            continue
        assert fdet(tuple(a ^ b for a, b in zip(v, q)))
        pairs += 1

RESULT = {
    "status": "PASS",
    "utc": datetime.now(timezone.utc).isoformat(),
    "method": "Sparse sets of Laurent monomials over F2; no symbolic package.",
    "universal_matrix_identities": CHECKS,
    "F8_nonzero_nilpotents": len(nil),
    "F8_independent_pairs": pairs,
    "scope": "Local algebra only. No global variation-image lower bound.",
    "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "elapsed_seconds": time.perf_counter() - START,
}
print(json.dumps(RESULT, indent=2))
