#!/usr/bin/env python3
"""Exact finite certificates for RESEARCH_SA06, Part B and E.2.

Inputs: F_8 = F_2[t]/(t^3+t+1); E:y^2+xy=x^3+x^2+(t+1);
quadratic discriminant -23; Gaussian example lambda=15+20i, q=25.
All algebraic checks use exact arithmetic. No numerical root approximation
is used as proof of a Weil property or irreducibility.
"""
from itertools import combinations
from math import gcd, isqrt
from pathlib import Path
import json
import time
import sympy as sp

started = time.perf_counter()
out = Path(__file__).resolve().parents[1] / "output"
out.mkdir(exist_ok=True)

def gf8_mul(a, b):
    c = 0
    while b:
        if b & 1:
            c ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 0b1011
    return c

pts = []
for x in range(8):
    x2 = gf8_mul(x, x)
    rhs = gf8_mul(x2, x) ^ x2 ^ 3
    for y in range(8):
        if gf8_mul(y, y) ^ gf8_mul(x, y) == rhs:
            pts.append([x, y])
assert pts == [[0, 7], [3, 1], [3, 2], [4, 0], [4, 4]]
assert len(pts) + 1 == 6

x = sp.symbols("x")
fE = x*x - 3*x + 8
fA = fE.subs(x, x**3)
C = sp.zeros(6)
for j in range(5):
    C[j+1, j] = 1
C[0,5], C[3,5] = -8, 3
assert sp.expand(C.charpoly(x).as_expr() - fA) == 0
indices = list(combinations(range(6), 3))
ext3 = sp.Matrix([[C.extract(i,j).det() for j in indices] for i in indices])
fext3 = sp.factor(ext3.charpoly(x).as_expr())
expected_ext3 = (x*x - 3*x + 8)*(x**6 - 24*x**3 + 512)**3
assert sp.expand(fext3 - expected_ext3) == 0
assert sp.rem(fext3, fE, x) == 0

# Exhaustive reduced primitive positive binary quadratic forms of D=-23.
D = -23
forms = []
for a in range(1, isqrt(abs(D)//3) + 1):
    for b in range(-a, a+1):
        if (b*b-D) % (4*a):
            continue
        c = (b*b-D)//(4*a)
        if a > c or gcd(gcd(a, abs(b)), c) != 1:
            continue
        if (abs(b) == a or a == c) and b < 0:
            continue
        forms.append([a,b,c])
assert forms == [[1,1,6], [2,-1,3], [2,1,3]]

# N(a+b omega)=a^2+ab+6b^2 with omega=(1+sqrt(-23))/2.
# The bound 23*b^2/4 <= 2 forces b=0 for norm 2, then a^2=2.
norm2_solutions = [[a,b] for a in range(-3,4) for b in range(-1,2)
                   if a*a+a*b+6*b*b == 2]
assert not norm2_solutions
omega = (1+sp.sqrt(-23))/2
lam = 1+omega
assert sp.simplify(lam*sp.conjugate(lam)) == 8
assert sp.simplify(fE.subs(x,lam)) == 0

pi = 2+sp.I
gauss_lam = 15+20*sp.I
assert sp.expand(pi**3*sp.conjugate(pi)-gauss_lam) == 0
assert sp.expand(gauss_lam*sp.conjugate(gauss_lam)) == 25**2
u = sp.simplify(pi/sp.conjugate(pi))
assert sp.simplify(u*sp.conjugate(u)) == 1
assert sp.simplify(u-(3+4*sp.I)/5) == 0
assert sp.simplify(sp.I*u-u) != 0

result = {
  "field": "F_2[t]/(t^3+t+1), binary encoding t=2",
  "elliptic_curve": "y^2+xy=x^3+x^2+(t+1)",
  "affine_points": pts,
  "point_at_infinity": "[0:1:0]",
  "point_count": len(pts)+1,
  "F8_frobenius_polynomial": str(fE),
  "Res_F8_F2_frobenius_polynomial": str(fA),
  "exterior_cube_dimension": len(indices),
  "exterior_cube_polynomial": str(fext3),
  "reduced_forms_discriminant_minus_23": forms,
  "norm2_integer_solutions_in_certifying_bound": norm2_solutions,
  "weight3_lambda_norm": 8,
  "gaussian_lambda_factorization": "(2+i)^3(2-i)",
  "gaussian_lambda_q": 25,
  "gaussian_lambda_weight": 2,
  "gaussian_lambda_normalized_slopes": ["3/2", "1/2"],
  "gaussian_norm_one_generator": str(u),
  "all_assertions_passed": True,
  "runtime_seconds": round(time.perf_counter()-started,6),
  "sympy_version": sp.__version__,
}
(out/"verify_frobenius_cases.json").write_text(json.dumps(result,indent=2)+"\n")
(out/"verify_frobenius_cases.txt").write_text("\n".join(f"{k}: {v}" for k,v in result.items())+"\n")
print(json.dumps(result,indent=2))
