"""Exact finite checks for the controlled-tree and exterior-module encoding.

These checks certify only the listed small trees and the explicit toy orbit
map. They are not a substitute for the all-dimension proof in the TeX file.
"""
from pathlib import Path
import itertools
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]

def tuples_bounded_sum(variables, bound):
    if variables == 1:
        for a in range(bound + 1):
            yield (a,)
        return
    for a in range(bound + 1):
        for tail in tuples_bounded_sum(variables - 1, bound - a):
            yield (a,) + tail

def controlled_tree(variables, degree):
    level = [()]
    counts = [1]
    last = ()
    depth = 0
    while level:
        following = []
        for prefix in level:
            for alpha in tuples_bounded_sum(variables, degree * (2 ** depth)):
                if all(not all(b <= a for b, a in zip(beta, alpha)) for beta in prefix):
                    following.append(prefix + (alpha,))
        if following:
            last = following[-1]
        counts.append(len(following))
        if not following:
            break
        level = following
        depth += 1
    return {"variables": variables, "degree": degree, "height": depth,
            "level_sizes": counts, "maximal_witness": last}

tree_checks = [controlled_tree(1, d) for d in range(1, 5)]
tree_checks.append(controlled_tree(2, 1))
for item in tree_checks:
    expected = item["degree"] + 1 if item["variables"] == 1 else 4
    assert item["height"] == expected

# Toy super-orbit graph: z=x, theta_1=eta, theta_2=x*eta.
# Its schematic kernel is (theta_2-z*theta_1), including its odd multiple.
x, z = sp.symbols("x z")
ys = sp.symbols("y0:8")
good = (0, 1, 2, 3)  # exterior monomials in theta_1 and theta_2 only
bad = (4, 5, 6, 7)   # exterior monomials involving eta

def exterior_multiply(left, right):
    if left & right:
        return None, 0
    inversions = sum(1 for i in range(3) for j in range(3)
                     if (left >> i) & 1 and (right >> j) & 1 and i > j)
    return left | right, (-1) ** inversions

graph = [{1: sp.Integer(1), 4: -sp.Integer(1)},
         {2: sp.Integer(1), 4: -x},
         {0: z - x}]
module_generators = []
for monomial in range(8):
    for relation in graph:
        value = 0
        for mask, coeff in relation.items():
            product, sign = exterior_multiply(monomial, mask)
            if sign:
                value += sign * coeff * ys[product]
        if value:
            module_generators.append(sp.expand(value))
square_zero = [ys[i] * ys[j] for i in range(8) for j in range(i, 8)]
order = (x,) + tuple(ys[i] for i in bad) + (z,) + tuple(ys[i] for i in good)
gb = sp.groebner(module_generators + square_zero, *order, order="lex", domain=sp.QQ)
eliminated_vars = {x} | {ys[i] for i in bad}
elimination = [p.as_expr() for p in gb.polys
               if not (p.as_expr().free_symbols & eliminated_vars)]
retained = (z,) + tuple(ys[i] for i in good)
expected_generators = [ys[2] - z * ys[1], ys[3]]
expected_generators += [ys[i] * ys[j] for i in good for j in good if i <= j]
expected_gb = sp.groebner(expected_generators, *retained, order="lex", domain=sp.QQ)
actual_gb = sp.groebner(elimination, *retained, order="lex", domain=sp.QQ)
assert all(expected_gb.reduce(p)[1] == 0 for p in elimination)
assert all(actual_gb.reduce(p)[1] == 0 for p in expected_generators)
linear_part = []
for p in elimination:
    poly = sp.Poly(p, *retained)
    y_degrees = {sum(monomial[1:]) for monomial, _ in poly.terms()}
    if y_degrees == {1}:
        linear_part.append(str(p))

report = {
    "scope": "Exact checks of five finite controlled trees and one explicit super-orbit graph; no actual geometric universal cut-off is enumerated.",
    "controlled_trees": tree_checks,
    "square_zero_encoding": {
        "graph": ["z=x", "theta_1=eta", "theta_2=x*eta"],
        "exterior_rank": 8,
        "ordinary_variables": len(order),
        "graph_module_generators": len(module_generators),
        "ordinary_groebner_basis_size": len(gb.polys),
        "elimination_basis_size": len(elimination),
        "linear_y_elimination_generators": linear_part,
        "expected_kernel": ["theta_2-z*theta_1", "theta_1*theta_2"],
        "mutual_ideal_membership_checks": "passed over Q",
    },
    "all_checks_passed": True,
}
target = ROOT / "code" / "part_c" / "check_uniform_bound_output.json"
target.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
