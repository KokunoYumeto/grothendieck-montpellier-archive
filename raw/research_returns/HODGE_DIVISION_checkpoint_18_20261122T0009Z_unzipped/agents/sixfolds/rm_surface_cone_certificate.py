#!/usr/bin/env python3
"""Exact complete-character and restriction-matrix checks for SF-E821.

This checks identities, not the coisotropy/deformation proof, finite-action
existence, or semiregularity of an object.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as s

p = Path(__file__).resolve().parent
a, b, k = s.symbols('a b k')


def trunc(v):
    return s.expand(sum(c*a**i*b**j for (i, j), c in
                        s.Poly(s.expand(v), a, b).terms() if i <= 2 and j <= 2))


def exp(v):
    return trunc(sum(v**j/s.factorial(j) for j in range(5)))


D = k*(a+b)
N = k*s.sqrt(2)*(a-b)
C = s.expand(18+exp(N)+exp(-N)-exp(D+N)-exp(-D-N)
             -exp(D-N)-exp(-D+N))
target = s.expand(16*(1-k*k*a*a/4)*(1-k*k*b*b/4))
assert s.expand(C-target) == 0
surface_plus = trunc(exp(N)*(exp(D)-2+exp(-D)))
surface_minus = trunc(exp(-N)*(exp(D)-2+exp(-D)))
B = s.expand(exp(N)+exp(-N)+surface_plus+surface_minus)
assert s.expand(C-(18-B)) == 0
Euler = s.expand(4*trunc(C*C).coeff(a, 2).coeff(b, 2))
assert Euler == 256*k**4
surface_euler = s.expand(4*surface_plus.coeff(a, 2).coeff(b, 2))
assert surface_euler == -6*k**4

U0 = s.Matrix([[1, 1], [1, -1]])
U = s.diag(U0, U0)
assert U*U == 2*s.eye(4)
assert U.det() == 4
restriction = []
for sign in (1, -1):
    H = s.eye(4)+sign*U
    assert H.det() == 1
    for ij in combinations(range(4), 2):
        K = H.extract(ij, ij)
        det, tr = K.det(), K.trace()
        kind = ('index1' if det < 0 else 'positive' if det > 0 and tr > 0
                else 'semipositive_rank1' if det == 0 and tr > 0 else 'zero')
        restriction.append({'sign': sign, 'free_coordinates':[j+1 for j in ij],
                            'matrix':list(map(list, K.tolist())), 'type':kind,
                            'determinant':int(det)})
assert [x['free_coordinates'] for x in restriction
        if x['sign'] == 1 and x['type'] == 'positive'] == [[1, 3]]
assert [x['free_coordinates'] for x in restriction
        if x['sign'] == -1 and x['type'] == 'positive'] == [[2, 4]]

out = {'result':'PASS', 'ring':'Q(sqrt(2),k)[a,b]/(a^3,b^3), integral a^2*b^2=4',
       'full_character':str(C), 'rank':16, 'q':'k^2/2',
       'self_Euler':str(Euler), 'individual_surface_Euler':str(surface_euler),
       'restriction_matrices':restriction,
       'limits':'No coisotropy theorem, actual Hochschild map, or finite action is computed. The local obstruction and explicit gluable construction require the written proof and independent review.'}
(p/'rm_surface_cone_certificate_output.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps({x:out[x] for x in ['result','full_character','self_Euler','individual_surface_Euler']},indent=2))
