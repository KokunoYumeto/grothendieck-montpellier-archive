"""Exact finite checks of the new prime-cancellation examples.

These corroborate the symbolic examples, not the general nullity theorem.
"""
from pathlib import Path
import json
import sympy as sp

A, B, C, Q, R, S = sp.symbols("A B C Q R S")
T = sp.Symbol("T")
variables = (A, B, C, Q, R, S)
weights = (1663, 523, 139, 127, 1093, 331)
f = (1-A)*(1-S**2) - (1-R**2)*(1-C) - C*(1-B)*(1-Q**12)
assert all(sp.isprime(p) for p in weights)
assert len(set(weights)) == 6
h = 2*12*(6-1)
bound = 16*(h+6*13+2)**2
assert all(h < p <= bound for p in weights)
assert sp.Poly(f, *variables).coeff_monomial(A*S**2) == 1
image = sp.expand(f.subs(dict(zip(variables, (T**p for p in weights)))))
assert image == 0
free_a = sp.expand(f.subs({v:T**p for v,p in zip(variables,weights) if v != A}))
assert sp.expand(free_a - (T**1663-A)*(1-T**662)) == 0

x = sp.symbols("x1:9")
p = (17,19,23,29,31,37,41,43)
first = x[0]*x[7]-x[1]*x[6]
second = x[2]*x[5]-x[3]*x[4]
g = first*second
assert all(sp.isprime(a) and a > 14 for a in p)
base_substitution = dict(zip(x,(T**a for a in p)))
assert sp.expand(first.subs(base_substitution)) == 0
assert sp.expand(second.subs(base_substitution)) == 0
single_cylinders = []
for i in range(8):
    value = sp.expand(g.subs({x[j]:T**p[j] for j in range(8) if j != i}))
    assert value == 0
    single_cylinders.append(True)
two = sp.expand(g.subs({x[j]:T**p[j] for j in range(8) if j not in (0,2)}))
assert two != 0

# Rows [1,U1,U2,U1*U2], columns [1,V1,V2,V1*V2].
flattening = sp.Matrix([[0,0,0,1],[0,0,-1,0],[0,-1,0,0],[1,0,0,0]])
assert flattening.det() in (1,-1)

result = {
    "three_product_additive_identity": {
        "weights": weights,
        "threshold": h,
        "weight_bound": bound,
        "all_distinct_primes": True,
        "nonzero_original_and_zero_prime_image": True,
        "free_coordinate_repair": True,
        "scope": "Integer polynomial identity, hence every characteristic."
    },
    "rank_four_single_cylinder_obstruction": {
        "weights": p,
        "all_eight_single_coordinate_cylinders_zero": all(single_cylinders),
        "two_coordinate_cylinder_nonzero": True,
        "flattening_determinant": int(flattening.det()),
        "tensor_rank_exactly_four_in_every_characteristic": True
    },
    "scope": "Finite exact corroboration of examples; not a formal certificate of the general theorem."
}
Path(__file__).with_name("I34_computation_checks.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
