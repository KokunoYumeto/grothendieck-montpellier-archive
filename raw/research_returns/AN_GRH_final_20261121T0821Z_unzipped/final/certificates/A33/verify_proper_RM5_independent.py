#!/usr/bin/env python3
"""Independent small-field/count/resultant check for the A33 supplement.

Uses F16 as F4[v]/(v^2+v+u), unlike the producer's F2-polynomial
presentation. Counts y-solutions directly. SymPy supplies a separate
Sylvester-resultant implementation; no producer module is imported.
"""
from pathlib import Path
import hashlib
import itertools
import json
import sympy as s


def gf4mul(a, b):
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        a <<= 1
        if a & 4:
            a ^= 7
        b >>= 1
    return ans


def add(x, y):
    return (x[0] ^ y[0], x[1] ^ y[1])


def mul(x, y):
    a, b = x
    c, d = y
    bd = gf4mul(b, d)
    return (gf4mul(a, c) ^ gf4mul(2, bd),
            gf4mul(a, d) ^ gf4mul(b, c) ^ bd)


zero, one, u, u2 = (0, 0), (1, 0), (2, 0), (3, 0)
elements = list(itertools.product(range(4), repeat=2))
inverses = {x: next(y for y in elements if mul(x, y) == one)
            for x in elements if x != zero}
assert mul(u, u) == u2
assert add(add(mul((0, 1), (0, 1)), (0, 1)), u) == zero
counts, rows = {}, {}
for q, field in ((4, [(a, 0) for a in range(4)]), (16, elements)):
    count = 3
    data = []
    for x in field:
        if x in (zero, one):
            continue
        rhs = add(add(x, mul(u, inverses[x])),
                  mul(u2, inverses[add(x, one)]))
        ys = [y for y in field if add(mul(y, y), y) == rhs]
        count += len(ys)
        data.append({'x': x, 'rhs': rhs, 'solutions': ys})
    counts[q], rows[q] = count, data
assert counts == {4: 3, 16: 15}
X, t = s.symbols('X t')
P = X**4 - 2*X**3 + X**2 - 8*X + 16
A = 4*t**4 + 7*t**3 + 10*t**2 + 7*t + 4
B = 16*t**4 - 8*t**3 + t**2 - 8*t + 16
resultant = s.resultant(P, P.subs(X, t*X), X)
assert s.expand(resultant - 256*(t-1)**4*A**2*B) == 0
for polynomial, variable in ((P, X), (A, t), (B, t)):
    assert s.Poly(polynomial, variable, modulus=3).is_irreducible
    assert s.Poly(polynomial, variable).is_irreducible
assert s.expand(X**2*((X+4/X)**2 - 2*(X+4/X)-7) - P) == 0
output = {
    'field': 'F4=F2[u]/(u^2+u+1), F16=F4[v]/(v^2+v+u)',
    'encoding': '(a,b) means a+b*v; a,b are binary coefficients in 1,u',
    'counts': counts, 'all_point_checks': rows,
    'resultant_factorization': str(s.factor(resultant)),
    'irreducibility_over_Q_and_mod3': True,
    'real_trace_identity': True,
    'scope': 'Independent arithmetic calculation, not formal verification.',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps({'counts': counts, 'resultant_pass': True,
                  'irreducibility_pass': True, 'real_trace_identity_pass': True}))
