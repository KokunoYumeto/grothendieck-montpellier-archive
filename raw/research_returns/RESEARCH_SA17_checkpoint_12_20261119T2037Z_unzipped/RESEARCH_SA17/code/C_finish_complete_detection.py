"""Exact bounded certificate for the formal rank-five detection example.

The polynomial action identities are checked over F3 with indeterminate
matrix entries, not merely at finite group points. The unbounded and
undecidability conclusions have written proofs, not finite certificates.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
import sympy as s

started = time.perf_counter()
root = Path(__file__).resolve().parents[1]
x, y, h, t = s.symbols('x y h t')
a, b, c, d, A, B, C, D = s.symbols('a b c d A B C D')
variables = (a,b,c,d,A,B,C,D,h,t)
powers = [(4,0),(3,1),(1,3),(0,4),(2,2)]

def reduce(poly):
    return s.Poly(s.expand(poly), *variables, modulus=3).as_expr()

def rho(g):
    image_x = g[0,0]*x + g[1,0]*y
    image_y = g[0,1]*x + g[1,1]*y
    result = s.zeros(5)
    for j,(r,q) in enumerate(powers):
        polynomial = s.Poly(s.expand(image_x**r * image_y**q),x,y)
        for i,(u,v) in enumerate(powers):
            result[i,j] = reduce(polynomial.coeff_monomial(x**u*y**v))
    return result

g = s.Matrix([[a,b],[c,d]])
gprime = s.Matrix([[A,B],[C,D]])
rg, rp, rproduct = rho(g), rho(gprime), rho(g*gprime)
assert all(reduce(rg[4,j]) == 0 for j in range(4))
assert reduce(rg[4,4] - (a*d-b*c)**2) == 0
action_checks = 0
for value in rg*rp-rproduct:
    assert reduce(value) == 0
    action_checks += 1

def deform(matrix):
    result = matrix.copy()
    for j in range(4):
        result[j,4] *= h
    return result

dg, dp, dproduct = map(deform,(rg,rp,rproduct))
deformed_action_checks = 0
for value in dg*dp-dproduct:
    assert reduce(value) == 0
    deformed_action_checks += 1

basis_change = s.diag(1,1,1,1,h)
assert all(reduce(v) == 0 for v in rg*basis_change-basis_change*dg)

split = rg.copy()
for j in range(4):
    split[j,4] = 0
truncations = []
for exponent in range(1,9):
    for level in range(1,exponent+1):
        differences = dg.subs(h,t**exponent)-split
        for value in differences:
            polynomial = s.Poly(s.expand(value),t)
            assert all(reduce(polynomial.nth(j)) == 0 for j in range(level))
        truncations.append([exponent,level])

upper = rho(s.Matrix([[1,t],[0,1]]))
lower = rho(s.Matrix([[1,0],[t,1]]))
assert reduce(upper[0,4]-t**2) == 0
assert reduce(upper[1,4]-2*t) == 0
assert [reduce(lower[i,0]) for i in range(4)] == [1,t,t**3,t**4]

output = {
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'status':'PASS',
    'scope':'Exact polynomial GL2 Sym4 and scaled-cocycle action identities over F3; invariant four-space and determinant-square quotient; generic scaling intertwiner; all t-adic levels a<=b for b=1..8; explicit unipotent coefficients. The written argument supplies simplicity, all b, O3 descent and the coefficient-stream impossibility theorem.',
    'rank':5,
    'symbolic_action_entries':action_checks,
    'symbolic_scaled_action_entries':deformed_action_checks,
    'generic_intertwiner_entries':25,
    'truncation_pairs':truncations,
    'truncation_pair_count':len(truncations),
    'elapsed_seconds':time.perf_counter()-started,
}
(root/'logs/C_finish_complete_detection.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output))
