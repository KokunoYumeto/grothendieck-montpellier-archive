#!/usr/bin/env python3
"""Exact exterior identities and actual balanced character for SF-E820.

The local lifting, extension classification and universal unit argument are
proved in the text, not certified by a finite search.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

root = Path(__file__).resolve().parent
g = s.symbols('g0:16')
q = s.symbols('q')
G = s.Matrix(4, 4, g)
J = s.diag(q, 1, 1, 1)*G
Pplus = s.zeros(4)
Pminus = s.zeros(4)
Pplus[0, 1], Pplus[1, 0] = 1, -1
Pminus[2, 3], Pminus[3, 2] = 1, -1
P = J*Pplus*J.T
Q = J*Pminus*J.T


def pfaff(M):
    return M[0, 1]*M[2, 3]-M[0, 2]*M[1, 3]+M[0, 3]*M[1, 2]


pp = s.expand(pfaff(P))
qq = s.expand(pfaff(Q))
cross = s.expand(pfaff(P+Q)-pfaff(P)-pfaff(Q))
assert pp == qq == 0
assert s.expand(cross-q*G.det()) == 0
t = s.symbols('t')
socles = []
for ell in range(1, 17):
    v = cross.subs(dict(zip(g, list(s.eye(4))))).subs(q, ell*t**(ell-1))
    reduced = s.rem(s.Poly(v, t), s.Poly(t**ell, t)).as_expr()
    assert reduced == ell*t**(ell-1) and reduced != 0
    socles.append({'length': ell, 'mixed_wedge': str(reduced)})

x, y = s.symbols('x y')
X = x+y
Y = s.sqrt(2)*(x-y)


def trunc(v):
    return s.expand(sum(c*x**a*y**b for (a, b), c in
                        s.Poly(s.expand(v), x, y).terms() if a <= 2 and b <= 2))


def exp(v):
    return trunc(sum(v**i/s.factorial(i) for i in range(5)))


H = s.expand(24+2*exp(X)+2*exp(-X)+exp(X+Y)+exp(-X-Y)
             +exp(X-Y)+exp(-X+Y))
target = 32*(1+x*x/4)*(1+y*y/4)
assert s.expand(H-target) == 0
Euler = 4*trunc(H*H).coeff(x, 2).coeff(y, 2)
assert Euler == 1024
output = {
    'result': 'PASS',
    'generic_matrix_variables': 16,
    'generic_jacobian_matrix': 'diag(q,1,1,1)*G',
    'first_self_pfaffian': str(pp),
    'second_self_pfaffian': str(qq),
    'mixed_wedge_identity': 'P(plus) wedge P(minus) = q*det(G)',
    'explicit_socle_checks': socles,
    'universal_socle_reason': 'ell*t^(ell-1) is nonzero modulo t^ell in characteristic zero',
    'full_rank32_character': str(H),
    'self_Euler': int(Euler),
    'extension_dimension_formula': '6*m^2*ell',
    'limits': 'No first-order module deformation, finite action, or semiregular object is computationally constructed. The complete universal unit and lifting arguments require the proof and its independent review.'
}
out = root/'rm_curvilinear_quantization_certificate_output.json'
out.write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps({k: output[k] for k in ['result', 'generic_matrix_variables',
                 'mixed_wedge_identity', 'full_rank32_character', 'self_Euler']}, indent=2))
