"""Exact algebra in C.3ag; no computational assertion about generic Hodge groups."""
from pathlib import Path
from itertools import product
import datetime
import json
import time
import sympy as sp

started = time.perf_counter()
h, a, g0, g1, b0, b1, b2 = sp.symbols("h a g0 g1 b0 b1 b2")

def push(expr):
    poly = sp.Poly(sp.expand(expr), h)
    return sp.expand(poly.coeff_monomial(h) + a * poly.coeff_monomial(h**2))

boundary = push((h - 2*a)*(h + a)*(g0 + h*g1))
source = push((h - 2*a)*(b0 + h*b1 + h*h*b2))
assert sp.expand(boundary + 3*a*a*g1) == 0
assert sp.expand(source - (b0 - a*b1 - 2*a*a*b2)) == 0
assert push(h - 2*a) == 1
gram = sp.Matrix([[4, 1], [1, -2]])
tau = sp.Matrix([-1, 4])
hyperplane, line = sp.Matrix([1, 0]), sp.Matrix([0, 1])
pair = lambda u, v: int((u.T * gram * v)[0])
assert (gram.det(), pair(tau, hyperplane), pair(tau, line), pair(tau, tau)) == (-9, 0, -9, -36)
quartic_monomials = [e for e in product(range(5), repeat=4) if sum(e) == 4 and e[0]+e[1] > 0]
assert len(quartic_monomials) == 30
transverse_base_degree = 3 * 4 * 4
assert transverse_base_degree == 48
t_hodge = {(2, 0): 1, (1, 1): 18, (0, 2): 1}
e_hodge = {(1, 0): 1, (0, 1): 1}
tensor_hodge = {}
for (p, q), dim in t_hodge.items():
    for (u, v), dim2 in e_hodge.items():
        key = f"{p+u},{q+v}"
        tensor_hodge[key] = tensor_hodge.get(key, 0) + dim*dim2
assert tensor_hodge == {"3,0": 1, "2,1": 19, "1,2": 19, "0,3": 1}
record = {
    "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "input_scope": "Formal incidence intersection identities, prescribed rank-two intersection lattice, degree and Hodge-number arithmetic only.",
    "push_rules": {"1": "0", "h": "1", "h^2": "a", "h^j for j>=3": "0"},
    "boundary_push": str(boundary),
    "source_push": str(source),
    "target_push_multiplier": str(push(h - 2*a)),
    "NS_gram": [list(map(int, row)) for row in gram.tolist()],
    "NS_determinant": int(gram.det()),
    "tau_H": pair(tau, hyperplane),
    "tau_D": pair(tau, line),
    "tau_squared": pair(tau, tau),
    "quartic_coefficient_count": len(quartic_monomials),
    "section_coefficient_count": 3*4*3,
    "transverse_base_degree": transverse_base_degree,
    "T_tensor_E_hodge_numbers": tensor_hodge,
    "runtime_seconds": time.perf_counter() - started,
    "status": "pass",
    "limits": "This does not certify an arithmetic quartic, a genericity condition by sampling, Picard rank, a Hodge-group theorem, or existence of a cycle. Those are proved using the specified source inputs and geometric arguments in C.3ag."
}
out = Path(__file__).with_name("check_dimension_six_incidence_output.json")
out.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
