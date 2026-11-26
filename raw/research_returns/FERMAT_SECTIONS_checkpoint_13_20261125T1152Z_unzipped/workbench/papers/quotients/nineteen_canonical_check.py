#!/usr/bin/env python3
"""Exact quotient identification with the published canonical quartic X15.

The model is credited to Kilicer et al. (2018), as detailed in the paper.

No numerical or class-group assumptions enter this calculation.  The output
records pullback signs, rational matrix ranks, the quartic relation, and small
prime point counts (the latter are checks of this plane model, not good-
reduction assertions).
"""
import hashlib
import json
from pathlib import Path

import sympy as s

x, y, A, B, C = s.symbols("x y A B C")
hs = [5, 8, 10, 12, 13, 15, 16, 17, 18]
pullback = []
for h in hs:
    b = 7*h//19
    hp = 7*h % 19
    sign = (-1)**(b-h)
    assert hp in hs and sign in (-1, 1)
    vals = [18-h, 19*b+18-7*h, 8*h-19*b-20]
    assert min(vals) >= 0
    pullback.append({"h": h, "h_image": hp, "sign": int(sign),
                     "orders_at_0_1_infinity": vals})

P = [(1-x)*y**13 + (1-x)**5*y**2 - (1-x)**6*y,
     (1-x)**2*y**10 + (1-x)**6 + (1-x)**4*y**6,
     (1-x)**3*y**8 - (1-x)**4*y**5 + (1-x)**5*y**3]

def reduce_curve(expr):
    ans = 0
    for (i,j), coeff in s.Poly(expr, x, y).terms():
        q,r = divmod(j,19)
        ans += coeff*x**(i+q)*(1-x)**(7*q)*y**r
    return s.Poly(s.expand(ans), x, y)

def relation_matrix(d):
    exps = [(i,j,d-i-j) for i in range(d,-1,-1)
            for j in range(d-i,-1,-1)]
    polys = [reduce_curve(P[0]**i*P[1]**j*P[2]**k)
             for i,j,k in exps]
    mons = sorted(set().union(*(set(p.monoms()) for p in polys)))
    maps = [p.as_dict() for p in polys]
    mat = s.Matrix([[p.get(m,0) for p in maps] for m in mons])
    return exps,mat

exps2, m2 = relation_matrix(2)
assert m2.rank() == 6
exps4, m4 = relation_matrix(4)
ker = m4.nullspace()
assert len(ker) == 1
q = A**4-A**3*B+2*A**3*C+2*A**2*B*C+2*A**2*C**2 \
    -2*A*B**2*C+4*A*B*C**2-B**3*C+3*B**2*C**2+2*B*C**3+C**4
qcoeff = s.Matrix([s.Poly(q,A,B,C).coeff_monomial(A**i*B**j*C**k)
                   for i,j,k in exps4])
assert m4*qcoeff == s.zeros(m4.rows,1)
assert reduce_curve(q.subs({A:P[0],B:P[1],C:P[2]}, simultaneous=True)).is_zero

qfun = s.lambdify((A,B,C),q,"math")
counts={}
for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43]:
    count = sum(qfun(a,b,1)%p == 0 for a in range(p) for b in range(p))
    count += sum(qfun(a,1,0)%p == 0 for a in range(p))
    count += (qfun(1,0,0)%p == 0)
    counts[str(p)] = {"points": int(count), "trace_if_smooth": p+1-count}

result={"status":"PASS", "base_curve":"y^19=x(1-x)^7",
        "canonical_coordinates": [str(v) for v in P],
        "pullback":pullback, "quadratic_matrix_shape":list(m2.shape),
        "quadratic_rank":6, "quartic_matrix_shape":list(m4.shape),
        "quartic_kernel_dimension":1,"quartic":str(q),
        "quartic_relation_exact":True,"small_prime_plane_counts":counts,
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
