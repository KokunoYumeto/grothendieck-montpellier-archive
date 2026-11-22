#!/usr/bin/env python3
"""Exact matrix and complete-character checks for SF-E819.

This does not computationally certify the categorical deformation or trace
argument. Those require the written proof and independent whole-proof audit.
"""
from pathlib import Path
import json
import sympy as s

p = Path(__file__).resolve().parent
x, y = s.symbols('x y')
u = s.sqrt(2)

def trunc(f):
    poly = s.Poly(s.expand(f), x, y)
    return s.expand(sum(c*x**a*y**b for (a,b),c in poly.terms()
                        if a <= 2 and b <= 2))

def exp(f):
    return trunc(sum(f**j/s.factorial(j) for j in range(5)))

X = x+y
Y = u*(x-y)
H = s.expand(6*(exp(X)+exp(-X)) + 12*(exp(Y/2)+exp(-Y/2)))
E = s.expand(H-s.Rational(1,2)*x*x*y*y)
target = s.expand(36*(1+x*x/3)*(1+y*y/3))
assert s.expand(E-target) == 0
signed = s.expand(6*(exp(X)+exp(-X))+3*(exp(Y)+exp(-Y))-2)
assert s.expand(signed-16*(1+3*x*x/4)*(1+3*y*y/4)) == 0

A = s.Matrix([[1,1],[1,-1]])
U = s.diag(A,A)
S = s.diag(1,1,-1,-1)
T0 = s.Matrix([[1,0],[1,1+s.I]])
T = s.diag(T0,T0)
pull = s.simplify(T.conjugate().T*(U*S)*T)
assert pull == s.diag(2,-2,-2,2)
degree = s.simplify(T.det()*s.conjugate(T.det()))
assert degree == 4
assert U*U == 2*s.eye(4)

Euler = 4*trunc(E*E).coeff(x,2).coeff(y,2)
signed_Euler = 4*trunc(signed*signed).coeff(x,2).coeff(y,2)
assert Euler == signed_Euler == 2304

out = {
    'result':'PASS',
    'ring':'Q(sqrt(2))[x,y]/(x^3,y^3), integral x^2 y^2=4',
    'isogeny_matrix':[[str(z) for z in T.row(i)] for i in range(4)],
    'isogeny_degree':int(degree),
    'pullback_Y_matrix':[[str(z) for z in pull.row(i)] for i in range(4)],
    'integral_half_pullback_diagonal':[1,-1,-1,1],
    'full_hull_character':str(H),
    'full_nonpure_sheaf_character':str(E),
    'balanced_target':str(target),
    'rank':36,'q':'2/3','point_torsion_length':34,
    'point_quotient_length':36,'local_signed_defect':2,
    'extension_space_dimension':6*36*34,
    'five_class_signed_character':str(signed),
    'five_class_rank':16,'five_class_q':'3/2',
    'self_Euler':int(Euler),
    'limitation':'Only exact matrix and full-character identities are checked. The module deformation, map lifting, perfect-complex trace, and all-action obstruction require the written proof; no finite action or semiregular object is computationally constructed.'
}
(p/'rm_local_quantization_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['result','isogeny_degree','full_hull_character','full_nonpure_sheaf_character','five_class_signed_character','self_Euler']},indent=2))
