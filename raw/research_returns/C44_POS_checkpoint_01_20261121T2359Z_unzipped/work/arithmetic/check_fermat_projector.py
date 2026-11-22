"""Exact finite character and Frobenius checks for C44-F01--F02.

These computations verify only the displayed finite character calculation and
the Frobenius-11 unit, not Abel--Jacobi injectivity or an unramified group.
"""
from itertools import combinations
from fractions import Fraction
import json
from pathlib import Path

chars = [(1, 1), (1, 2), (2, 1), (3, 3), (3, 2), (2, 3)]
odd_invariants = {}
all_invariants = {}
for k in range(7):
    subsets = [s for s in combinations(range(6), k)
               if all(sum(chars[j][a] for j in s) % 4 == 0
                      for a in range(2))]
    all_invariants[str(k)] = [list(s) for s in subsets]
    odd_invariants[str(k)] = [list(s) for s in subsets] if k % 2 else []

assert [len(odd_invariants[str(k)]) for k in range(7)] == [0, 0, 0, 2, 0, 0, 0]
assert odd_invariants['3'] == [[0, 1, 2], [3, 4, 5]]

prime = 11
affine_points = [(x, y) for x in range(prime) for y in range(prime)
                 if (y*y-x*x*x-x) % prime == 0]
point_count = 1 + len(affine_points)
assert point_count == 12
unit = Fraction(prime + 1, prime)
unit_mod5 = unit.numerator * pow(unit.denominator, -1, 5) % 5
assert unit_mod5 == 2

result = {
    "scope": "Finite character calculation and Frobenius-11 unit only",
    "characters_mod4": chars,
    "G_invariant_exterior_basis_indices": all_invariants,
    "e_invariant_exterior_basis_indices": odd_invariants,
    "e_realization_ranks_in_degrees_0_through_6":
        [len(odd_invariants[str(k)]) for k in range(7)],
    "Eplus_equation": "y^2=x^3+x",
    "prime": prime,
    "Eplus_affine_points": affine_points,
    "Eplus_number_of_points_including_infinity": point_count,
    "Eplus_trace": prime + 1 - point_count,
    "Frobenius_polynomial_on_N_before_twist": [1, 0, prime**3],
    "Frobenius_polynomial_on_N_twist_2": ["1", "0", "1/11"],
    "det_one_minus_Frobenius": str(unit),
    "det_one_minus_Frobenius_mod5": unit_mod5,
}
out = Path(__file__).with_name('fermat_projector_certificate.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({"certificate": str(out), "checks": "passed", "ranks":
                  result['e_realization_ranks_in_degrees_0_through_6'],
                  "unit_mod5": unit_mod5}))
