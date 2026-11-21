#!/usr/bin/env python3
"""Exact finite supplement for SF-E838; no module-deformation claim.

Reconstructs both ten-by-ten determinant pencils from actual gradients,
the arbitrary-coefficient nonsquare triangular calculation, a nontrivial
generator change, Hilbert pieces and cubic-perturbation quadratic jets.
The universal filtered matrix lemma and Grassmannian argument are proofs
in the adjoining text, not assertions verified by this finite script.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
import sympy as sp
from sympy.polys.matrices import DomainMatrix

started = time.perf_counter()
z = sp.symbols("z1:5")
a, b = sp.symbols("a b")
pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
mons = [x**2 for x in z] + [z[i]*z[j] for i, j in pairs]
J = sp.Matrix([
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [-sp.Rational(3, 5), 1, -sp.Rational(9, 5), 2],
    [-sp.Rational(8, 5), 1, -sp.Rational(16, 5), 3],
])
ell = list(J*sp.Matrix(z))
F = [sp.expand(x*x) for x in ell]
Fsharp = F.copy()
Fsharp[0] = sp.expand(Fsharp[0] + ell[1]*ell[2])
records = []

def check(name, truth, data=None):
    assert truth, name
    records.append({"name": name, "pass": True, "data": data})

def bracket(f, g, k):
    return sp.expand(sp.diff(f, z[k])*sp.diff(g, z[k+1])
                     - sp.diff(f, z[k+1])*sp.diff(g, z[k]))

def coeff_matrix(polys, basis=mons):
    return sp.Matrix([[sp.Poly(f, z).coeff_monomial(mon) for f in polys]
                      for mon in basis])

def pencil(fs):
    plus = [bracket(fs[i], fs[j], 0) for i,j in pairs]
    minus = [bracket(fs[i], fs[j], 2) for i,j in pairs]
    return coeff_matrix(fs + [a*x+b*y for x,y in zip(plus,minus)])

expected = -sp.Rational(100663296, 78125)*(a+b)**2*(a+2*b)**2*(a+3*b)**2
check("linear_parameter_determinant", J.det() == -sp.Rational(4,5))
pencils = {}
for name, fs in [("four_squares", F), ("nonsquare", Fsharp)]:
    mat = pencil(fs)
    det = sp.factor(DomainMatrix.from_Matrix(mat).det().as_expr())
    check(name+"_entire_pencil", sp.expand(det-expected) == 0, str(det))
    for aa,bb in [(1,0),(0,1),(1,1)]:
        rank = DomainMatrix.from_Matrix(mat.subs({a:aa,b:bb})).rank()
        check(name+f"_rank_{aa}_{bb}", rank == 10, rank)
    pencils[name] = {
        "determinant":str(det),
        "coefficients_a6_to_b6":[str(sp.Poly(det,a,b).coeff_monomial(a**(6-j)*b**j))
                                 for j in range(7)],
    }

# Full symbolic triangular computation in the ell variables, with six
# unrelated constant bivector coefficients. No decomposability assumed.
P = sp.symbols("P12 P13 P14 P23 P24 P34")
form = sp.zeros(4)
for (i,j),p in zip(pairs,P):
    form[i,j] = p
    form[j,i] = -p
g = [z[0]**2+z[1]*z[2], z[1]**2, z[2]**2, z[3]**2]
raw = []
for i,j in pairs:
    raw.append(sp.expand(sum(form[k,l]*sp.diff(g[i],z[k])*sp.diff(g[j],z[l])
                             for k in range(4) for l in range(4))))
reduced = []
for poly in raw:
    coeffs = list(coeff_matrix([poly]))
    pair_coeffs = coeffs[4:]
    pair_coeffs[3] -= coeffs[0]  # z1² = -z2z3
    reduced.append(pair_coeffs)
quotient_matrix = sp.Matrix.hstack(*(sp.Matrix(c) for c in reduced))
check("six_unrestricted_coefficients_triangular",
      quotient_matrix.det() == 4**6*sp.prod(P),
      str(quotient_matrix))

# A non-unimodular, nondiagonal generator change checks the exponent four.
T = sp.Matrix([[2,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,2]])
TF = [sp.expand(v) for v in T*sp.Matrix(Fsharp)]
det_TF = DomainMatrix.from_Matrix(pencil(TF)).det().as_expr()
check("generator_change_det_four",
      sp.expand(det_TF-T.det()**4*expected) == 0,
      {"det_T":str(T.det())})

def monomials_degree(n):
    return [sp.prod(z[i]**es[i] for i in range(4))
            for es0 in range(n+1)
            for es1 in range(n-es0+1)
            for es2 in range(n-es0-es1+1)
            for es in [(es0,es1,es2,n-es0-es1-es2)]]

hilbert = {}
for name,fs in [("four_squares",F),("nonsquare",Fsharp)]:
    dims = []
    for degree in range(6):
        basis = monomials_degree(degree)
        if degree < 2:
            dims.append(len(basis))
        else:
            inputs = monomials_degree(degree-2)
            mat = coeff_matrix([sp.expand(f*g) for f in fs for g in inputs],basis)
            dims.append(len(basis)-DomainMatrix.from_Matrix(mat).rank())
    check(name+"_hilbert_to_degree_five", dims == [1,4,6,4,1,0],dims)
    hilbert[name] = dims

# Higher-order perturbations do not change the actual leading brackets.
higher = [
    z[0]*z[1]*z[2]+z[3]**4,
    z[0]**3-z[1]*z[3]**2,
    z[0]*z[2]**2+z[1]**4,
    z[1]*z[2]*z[3]+z[0]**5,
]
perturbed = [sp.expand(f+h) for f,h in zip(Fsharp,higher)]
def degree_two(poly):
    return sp.expand(sum(c*sp.prod(z[i]**exp[i] for i in range(4))
                         for exp,c in sp.Poly(poly,z).terms() if sum(exp)==2))
for i,j in pairs:
    for k in (0,2):
        check(f"quadratic_jet_{i}{j}_{k}",
              degree_two(bracket(perturbed[i],perturbed[j],k))
              == bracket(Fsharp[i],Fsharp[j],k))

elapsed = time.perf_counter()-started
output = {
    "status":"PASS",
    "completed_utc":datetime.now(timezone.utc).isoformat(),
    "runtime_seconds":elapsed,
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope":"Finite exact algebra supplement only; no universal matrix or module-deformation verification.",
    "checks":records,
    "pencils":pencils,
    "hilbert_pieces":hilbert,
}
out = Path(__file__).with_name("rm_quadratic_jet_certificate_output.json")
out.write_text(json.dumps(output,indent=2)+"\n")
print(json.dumps({"status":"PASS","checks":len(records),"runtime_seconds":elapsed,
                  "output":str(out)},indent=2))
