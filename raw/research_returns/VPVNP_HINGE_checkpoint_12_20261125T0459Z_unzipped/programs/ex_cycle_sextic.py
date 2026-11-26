#!/usr/bin/env python3
"""Exact coefficient, Jacobian and degeneration certificates for EX34--36."""
import functools
import itertools
import json
import math
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PARAMS = json.loads((ROOT / "inputs/ex_cycle_sextic_parameters.json").read_text())
variables = sp.symbols("t0:16")
x0, x1, z0, z1 = sp.symbols("x0 x1 z0 z1")
x, z = (x0, x1), (z0, z1)
matrix = sp.zeros(2)
for a, b, c, d in itertools.product(range(2), repeat=4):
    matrix[b, d] += variables[8*a + 4*b + 2*c + d] * x[a] * z[c]
form = sp.Poly(sp.expand(matrix.det()), x0, x1, z0, z1)
exponents = ((2, 0), (1, 1), (0, 2))
coefficients = sp.Matrix(3, 3, lambda i, j: form.coeff_monomial(
    x0**exponents[i][0] * x1**exponents[i][1]
    * z0**exponents[j][0] * z1**exponents[j][1]))
invariant = sp.Poly(sp.expand(coefficients.det()), *variables)
target = {variable: int(index in (0, 5, 10, 15))
          for index, variable in enumerate(variables)}
coefficient_gcd = functools.reduce(math.gcd, map(int, invariant.coeffs()))
assert coefficient_gcd == 1
assert len(invariant.terms()) == 144
assert set(map(int, invariant.coeffs())) == {-1, 1}
assert coefficients.subs(target) == sp.diag(1, 2, 1)
assert invariant.as_expr().subs(target) == 2

def rank_mod2(rows):
    rows = [[int(v) % 2 for v in row] for row in rows]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[pivot], rows[rank] = rows[rank], rows[pivot]
        for i in range(len(rows)):
            if i != rank and rows[i][column]:
                rows[i] = [a ^ b for a, b in zip(rows[i], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank

# Torus-weight-zero quadratic forms and their unipotent constraints.
unipotent_parameter = sp.symbols("u")
quadratic_basis = [variables[i] * variables[15-i] for i in range(8)]
constraint_rows = []
for party in range(4):
    bit = 1 << (3-party)
    substitution = {variables[i]: variables[i] + unipotent_parameter*variables[i|bit]
                    for i in range(16) if not i & bit}
    coefficient_rows = {}
    for index, quadric in enumerate(quadratic_basis):
        difference = sp.Poly(sp.expand(quadric.subs(substitution, simultaneous=True)-quadric),
                             *variables, unipotent_parameter)
        for monomial, coefficient in difference.terms():
            coefficient_rows.setdefault(monomial, [0]*8)[index] = int(coefficient) % 2
    constraint_rows += [row for row in coefficient_rows.values() if any(row)]
assert rank_mod2(constraint_rows) == 7
assert all(sum(row) % 2 == 0 for row in constraint_rows)
h_point = PARAMS["h_zero_sextic_nonzero_point"]
h_value = sum(h_point[i]*h_point[15-i] for i in range(8))
i_value = int(invariant.as_expr().subs(dict(zip(variables, h_point))))
assert h_value % 2 == 0 and i_value % 2 == 1

# Nonzero Jacobian minor of the 32-parameter trace parametrization.
local_point = [[sp.Matrix(matrix) for matrix in party]
               for party in PARAMS["jacobian_point"]]
jacobian = []
for output_tuple in itertools.product(range(2), repeat=4):
    row = []
    for site, value, i, j in itertools.product(range(4), range(2), range(2), range(2)):
        if output_tuple[site] != value:
            row.append(0)
            continue
        product = sp.eye(2)
        for party in range(4):
            if party == site:
                elementary = sp.zeros(2)
                elementary[i, j] = 1
                product = product * elementary
            else:
                product = product * local_point[party][output_tuple[party]]
        row.append(int(sp.trace(product)))
    jacobian.append(row)
minor = sp.Matrix([[jacobian[i][j] for j in PARAMS["jacobian_minor_columns"]]
                   for i in PARAMS["jacobian_minor_rows"]])
minor_determinant = int(minor.det())
assert minor_determinant == -1 and rank_mod2(jacobian) == 15

# An integer identity specializing to a same-field F2 degeneration.
t = sp.symbols("t")
identity = sp.eye(2)
e = sp.diag(0, 1)
swap = sp.Matrix([[0, 1], [1, 0]])
local_family = [[identity, t*e], [identity, swap], [t*e, identity], [identity, swap]]
family_entries = []
for a, b, c, d in itertools.product(range(2), repeat=4):
    value = sp.expand(sp.trace(local_family[0][a]*local_family[1][b]
                              *local_family[2][c]*local_family[3][d]))
    expected = (2*int(a == 0 and c == 1 and b == d)
                + t*int(a == c and b == d)
                + t*t*int((a, b, c, d) == (1, 0, 0, 0)))
    assert sp.expand(value-expected) == 0
    family_entries.append(str(value))
routing_cases = 0
for a, c, d in itertools.product(range(PARAMS["routing_max_parameter"] + 1), repeat=3):
    b = c + d - a
    if not (a <= c <= d <= b):
        continue
    twice_x, twice_y = 2*a*c - a*a, a*a
    flows = (twice_x, 2*a*b - twice_x, twice_y, 2*c*d - twice_y)
    assert min(flows) >= 0
    loads = (twice_x + twice_y,
             2*a*b - twice_x + twice_y,
             twice_x + 2*c*d - twice_y,
             2*a*b - twice_x + 2*c*d - twice_y)
    capacities = (2*a*c, 2*a*d, 2*b*c, 2*b*d)
    assert [v-u for u, v in zip(loads, capacities)] == [
        0, 0, 2*(c-a)**2, 2*(d-a)**2]
    routing_cases += 1
result = {
    "parameters": PARAMS,
    "variable_order": [format(i, "04b") for i in range(16)],
    "coefficient_matrix": [[str(coefficients[i, j]) for j in range(3)] for i in range(3)],
    "invariant_monomials": [{"exponents": list(m), "coefficient": int(c)}
                            for m, c in invariant.terms()],
    "monomial_count": len(invariant.terms()),
    "coefficient_gcd": coefficient_gcd,
    "coefficient_values": sorted(set(map(int, invariant.coeffs()))),
    "crossed_bell_coefficient_matrix": [[1, 0, 0], [0, 2, 0], [0, 0, 1]],
    "crossed_bell_invariant_value": 2,
    "characteristic_two_invariant_value": 0,
    "quadratic_unipotent_constraint_matrix_mod2": constraint_rows,
    "quadratic_unipotent_constraint_rank_mod2": 7,
    "h_witness_integer_value": h_value,
    "sextic_witness_integer_value": i_value,
    "jacobian": jacobian,
    "jacobian_minor": [[int(v) for v in row] for row in minor.tolist()],
    "jacobian_minor_integer_determinant": minor_determinant,
    "jacobian_rank_mod2": 15,
    "explicit_family_integer_entries": family_entries,
    "four_group_routing_cases": routing_cases,
    "scope": "Primitive sextic does not obstruct characteristic2. Explicit maps give tP+t²U in characteristic2. Rank15 and the irreducibility argument independently characterize the geometric image closure. Routing checks supplement the symbolic proof."
}
output = ROOT / "outputs/ex_cycle_sextic_results.json"
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({key: result[key] for key in (
    "monomial_count", "coefficient_gcd", "coefficient_values",
    "crossed_bell_invariant_value", "four_group_routing_cases",
    "quadratic_unipotent_constraint_rank_mod2", "jacobian_minor_integer_determinant",
    "jacobian_rank_mod2")}))
