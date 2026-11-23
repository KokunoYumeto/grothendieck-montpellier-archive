#!/usr/bin/env python3
"""Exact auxiliary checks for HD-S17--S20; no existence claim is encoded."""
from pathlib import Path
import json
import sympy as s

root = Path(__file__).resolve().parent
t, n, delta = s.symbols('t n delta', real=True)
m = n-t+1
gram = s.Matrix([[0,1,1,n],[1,0,1,1],[1,1,0,m],[n,1,m,0]])
assert s.expand(gram.det()) == t*t-4*n

# Complex-linear commutant: AB=BA for every elementary 3x3 matrix.
z = s.symbols('z0:9')
Z = s.Matrix(3,3,z)
linear, anti = [], []
for i in range(3):
    for j in range(3):
        E = s.zeros(3)
        E[i,j] = 1
        linear.extend(list(Z*E-E*Z))
        anti.extend(list(Z*E.T-E*Z))
Lc, _ = s.linear_eq_to_matrix(linear,z)
La, _ = s.linear_eq_to_matrix(anti,z)
assert Lc.rank() == 8
assert La.rank() == 9
assert len(Lc.nullspace()) == 1
assert s.Matrix(3,3,Lc.nullspace()[0]) == s.eye(3)

divisor_bound = 2*(1+n)
# For row (1,alpha), norm(alpha)=n, the difference matrix is
# 2[[n,-alpha],[-bar(alpha),(1+n)delta-n]].
last_leading = 2*n
last_determinant = s.expand(4*(n*((1+n)*delta-n)-n))
assert s.expand(last_determinant - 4*n*(n+1)*(delta-1)) == 0
# For row (1,1), the same global bound is valid for n,delta>=1.
third_det = s.expand((divisor_bound-2)*(divisor_bound*delta-2)-4)
assert s.expand(third_det - 4*(n+1)*(delta*n-1)) == 0

classes = [1,2,3,7,11,19,43,67,163]
rows = []
for d in classes:
    N = d if d in (1,2) else (d+1)//4
    T = 0 if d in (1,2) else 1
    disc = T*T-4*N
    assert disc == (-4*d if d in (1,2) else -d)
    rows.append(dict(d=d, trace_alpha=T, norm_alpha=N,
                     Gram_determinant=disc,
                     doubled_Gram_determinant=256*disc,
                     divisor_nef_constant=2*(1+N),
                     sixfold_contraction_cost=str(s.Rational(1+N,2))))

data = dict(
    statements=['HD-S17','HD-S18','HD-S19','HD-S20'],
    date='2026-11-21',
    model='GPT-6 Astra Pro; inherited effort not exposed; /root/sixfolds',
    arithmetic='exact symbolic integer/rational arithmetic',
    surface_Gram=[[str(v) for v in gram.row(i)] for i in range(4)],
    surface_Gram_determinant=str(s.factor(gram.det())),
    commutant_complex_linear_rank=int(Lc.rank()),
    commutant_antilinear_rank=int(La.rank()),
    commutant_complex_linear_dimension=1,
    commutant_antilinear_dimension=0,
    last_divisor_difference_leading=str(last_leading),
    last_divisor_difference_determinant=str(s.factor(last_determinant)),
    third_divisor_difference_determinant=str(s.factor(third_det)),
    diagonal_degree_coefficient=int(2**6*s.factorial(6)),
    fields=rows,
    scope='Checks explicit matrices only; no new eightfold supplier or nonsplit-sixfold detector asserted.'
)
(root/'nonsplit_routes_certificate.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
