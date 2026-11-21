"""Exact arithmetic certificate for Finding A13.

Standard library only. This checks the finite arithmetic used in the proof;
it does not claim formal proof-assistant verification of the geometric inputs.
The independent parent certificate computes the Jacobian order by a resultant,
whereas this producer certificate uses the stated Newton recurrence.
"""
from math import isqrt
from pathlib import Path
import json


def multiply4(a, b):
    """Polynomial multiplication in F_2[u]/(u^2+u+1)."""
    answer = 0
    for _ in range(2):
        if b & 1:
            answer ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return answer


def power4(a, e):
    answer = 1
    for _ in range(e):
        answer = multiply4(answer, a)
    return answer


def polynomial_point_count(field_elements):
    # Smooth projective model: Y^2+(x^2+x)Y=x^5+x^3+x^2+x.
    # The odd degree-five model has one point at infinity.
    affine_points = []
    for x in field_elements:
        h = power4(x, 2) ^ x
        rhs = power4(x, 5) ^ power4(x, 3) ^ power4(x, 2) ^ x
        for y in field_elements:
            lhs = power4(y, 2) ^ multiply4(h, y)
            if lhs == rhs:
                affine_points.append((x, y))
    return len(affine_points) + 1, affine_points


N2, points2 = polynomial_point_count(range(2))
N4, points4 = polynomial_point_count(range(4))
assert (N2, N4) == (3, 3)
assert points2 == points4 == [(0, 0), (1, 0)]

s1, s2 = 2 + 1 - N2, 4 + 1 - N4
assert (s1 * s1 - s2) % 2 == 0
e2 = (s1 * s1 - s2) // 2
frobenius_polynomial = [1, -s1, e2, -2 * s1, 4]
assert frobenius_polynomial == [1, 0, -1, 0, 4]

traces = [2, 1]
for m in range(2, 8):
    traces.append(traces[-1] - 4 * traces[-2])
assert traces == [2, 1, -7, -11, 17, 61, -7, -251]
jacobian_order = 1 - traces[7] + 4**7
ell = 4159
assert jacobian_order == 16636 == 4 * ell
trial_limit = isqrt(ell)
assert trial_limit == 64
assert all(ell % divisor for divisor in range(2, trial_limit + 1))

candidate_order = 3**3 * 7 * 11
assert candidate_order == 2079
proper_quotient_residues = {
    str(prime): pow(2, candidate_order // prime, ell)
    for prime in (3, 7, 11)
}
assert pow(2, candidate_order, ell) == 1
assert proper_quotient_residues == {"3": 2554, "7": 1245, "11": 102}
assert all(residue != 1 for residue in proper_quotient_residues.values())
# Separate direct loop, not using the factor/order criterion.
residue, direct_order = 2, 1
while residue != 1:
    residue = (2 * residue) % ell
    direct_order += 1
    assert direct_order < ell
assert direct_order == candidate_order
assert direct_order % 2 == 1
assert 2 * direct_order == ell - 1

Q, subgroup_order = 128, ell
index = jacobian_order // subgroup_order
assert index == 4
sqrt_floor = isqrt(4 * (index + 1) ** 2 * Q)
assert sqrt_floor == 113
numerator = Q + 1 - sqrt_floor
theta_lower_bound = (numerator + index - 1) // index
assert theta_lower_bound == 4
assert Q > (2 * index + 3) ** 2

result = {
    "status": "PASS",
    "finite_field_model": "F_4 = F_2[u]/(u^2+u+1); integer bits 1,u",
    "affine_model": "Y^2+(x^2+x)Y=x^5+x^3+x^2+x",
    "point_counts": {"F2": N2, "F4": N4},
    "finite_affine_points": {"F2": points2, "F4": points4},
    "frobenius_polynomial_descending": frobenius_polynomial,
    "beta_power_sums_0_through_7": traces,
    "jacobian_order_F128": jacobian_order,
    "factorization": {"2": 2, "4159": 1},
    "prime_trial_division_maximum": trial_limit,
    "order_of_2_mod_4159": direct_order,
    "proper_quotient_residues": proper_quotient_residues,
    "minus_one_extends_to_full_unit_group": True,
    "Lang_quotient_degree": index,
    "Lang_cover_genus": index + 1,
    "Weil_error_floor": sqrt_floor,
    "theta_rational_point_lower_bound": theta_lower_bound,
    "formal_proof_assistant_verification": False,
}
output = Path(__file__).with_name("lang_weil_4159_certificate.json")
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
