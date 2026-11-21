"""Exact auxiliary certificate for O-011; no floating point computations."""
from itertools import permutations
from pathlib import Path
import json
import sympy as sp

OUT = Path(__file__).resolve().parent / "hessian_certificate.json"
m, s = sp.symbols("m s")
G = sp.Matrix([[(m-2)**2, 1], [1, m**2]]) / (m-1)**2
C = sp.Matrix([[s*(s-1)*m*(m-1), s*(m-1)], [s*(m-1), 0]])
claimed = (m+s-1)/(m-1) * (1-(m*m-3*m+1)*s)
residual = sp.factor((sp.eye(2)+C*G).det()-claimed)
assert residual == 0

checks = []
for size in range(2, 5):
    xs = sp.symbols(f"x0:{size*size}")
    perm = sum(sp.prod(xs[size*i+p[i]] for i in range(size))
               for p in permutations(range(size)))
    one = dict.fromkeys(xs, 1)
    B = sp.kronecker_product(sp.ones(size)-sp.eye(size),
                             sp.ones(size)-sp.eye(size))
    h = sp.factorial(size-2)
    e = sp.eye(size*size)[:, 0]
    u = sp.ones(size*size, 1)
    for padding in range(1, 4):
        F = xs[0]**padding * perm
        H = sp.hessian(F, xs).subs(one)
        expected = h*(B + padding*(size-1)*(e*u.T+u*e.T)
                      + padding*(padding-1)*size*(size-1)*(e*e.T))
        assert H == expected
        ratio = sp.cancel(H.det()/(h*B).det())
        value = claimed.subs({m: size, s: padding})
        assert ratio == value
        checks.append({"m": size, "padding": padding,
                       "direct_hessian_matches": True,
                       "determinant_ratio": str(ratio)})

xs = sp.symbols("x0:9")
perm = sum(sp.prod(xs[3*i+p[i]] for i in range(3))
           for p in permutations(range(3)))
F = xs[0]*perm
point = {x: (2 if i == 0 else 1) for i, x in enumerate(xs)}
H = sp.hessian(F, xs).subs(point)
E = sp.eye(9)
t = sp.sqrt(2)
vectors = [E[:,0], (E[:,1]+E[:,2])/t, (E[:,3]+E[:,6])/t,
           (E[:,4]+E[:,5]+E[:,7]+E[:,8])/2,
           (E[:,3]-E[:,6])/t, (E[:,4]+E[:,5]-E[:,7]-E[:,8])/2,
           (E[:,1]-E[:,2])/t, (E[:,4]-E[:,5]+E[:,7]-E[:,8])/2,
           (E[:,4]-E[:,5]-E[:,7]+E[:,8])/2]
Q = sp.Matrix.hstack(*vectors)
assert Q.T*Q == sp.eye(9)
A = sp.Matrix([[4,2*t,2*t,10],[2*t,0,4,2*t],
               [2*t,4,0,2*t],[10,2*t,2*t,4]])
D = sp.Matrix([[0,-2*t],[-2*t,-4]])
expected = sp.diag(A,D,D,sp.Matrix([[4]]))
assert sp.simplify(Q.T*H*Q-expected) == sp.zeros(9)
assert H.det() == 147456
assert F.subs(point) == 16
result = {"statement_id": "O-011", "run": "GCT_KRON_20261120",
          "arithmetic": "exact integers and rational functions; no floating point",
          "symbolic_ratio_residual": str(residual),
          "direct_small_hessian_checks": checks,
          "exception_m3_n4": {"point": [2]+[1]*8,
                               "F_value": 16,
                               "Hessian_integer_matrix": [list(map(int,H.row(i))) for i in range(9)],
                               "orthogonal_block_identity": True,
                               "block_determinants": [576,-8,-8,4],
                               "determinant": 147456}}
OUT.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({"symbolic_ratio_residual": str(residual),
                  "direct_hessian_checks": len(checks),
                  "exception_determinant": 147456,
                  "certificate": str(OUT)}))
