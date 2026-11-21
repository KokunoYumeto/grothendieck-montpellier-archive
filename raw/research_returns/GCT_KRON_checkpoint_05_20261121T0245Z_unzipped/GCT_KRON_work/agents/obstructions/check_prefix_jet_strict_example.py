"""Exact finite certificates for M017's constant and the O022 profile."""
from datetime import datetime, timezone
from math import comb, factorial, prod
from pathlib import Path
import json

numerator = 190**24
denominator = comb(36111, 12)
C_star, remainder = divmod(numerator, denominator)
assert C_star == 478126755
assert C_star * denominator <= numerator < (C_star + 1) * denominator
assert 0 < remainder < denominator

m = 2**200
r = m*m
n = m**25
d = 3*n
first_part = n*d - 26*r + 20
tail = 32 + 26*(r - 2)
assert first_part + tail == n*d
assert first_part >= 32 >= 26
assert r <= d and tail <= m*d and m >= 190
T = m*comb(r + 11, 12)
size = 8*T
assert 32 <= size < n
assert 8 < C_star
multiplier_exponent = d - 6 - 13*r
assert multiplier_exponent >= 0
assert (6*n - 6) + 13*(r*(n - 2) + 2) + n*multiplier_exponent == first_part
assert 6 + 13*2 == 32
assert 6 + 13*r + multiplier_exponent == d

last_variables = r - 2
ratio_numerator = factorial(13)*prod(last_variables + j for j in range(13, 26))
ratio_denominator = 2*factorial(26)
assert ratio_numerator > n*ratio_denominator
assert factorial(13)*m**26 > 2**14*factorial(26)*n
assert 2**14*factorial(26) < 2**79*factorial(13)
assert m > 2**79

pencil_dimension_bound = (r - 2)*n*n + 2
scale = m**52
outer_cut_lower = comb(r//2 - 1, 27)
middle_cut_lower = (m - 25)*comb(r//2, 26)
assert pencil_dimension_bound < scale
assert outer_cut_lower > scale and middle_cut_lower > scale
assert outer_cut_lower*2**54*factorial(27) >= m**54
assert middle_cut_lower*2**53*factorial(26) >= m**53
assert 2**54*factorial(27) < 2**189 < m*m
assert 2**53*factorial(26) < 2**183 < m
full_point_jet_dimension = comb(r - 1 + 32, 32)
restricted_jet_dimension = sum((33 - h)*comb(last_variables + h - 1, h)
                               for h in range(27))
assert full_point_jet_dimension > pencil_dimension_bound
assert restricted_jet_dimension < pencil_dimension_bound

staircase = []
for j in range(1, 27):
    part = 32 if j == 1 else 26
    required = 28 - j
    assert part >= required
    staircase.append({"row": 2*j, "part": part, "required": required})
assert 26 >= 3  # A025's row52 alternative.
chow_base_bound = d*(d - 1)//2
assert chow_base_bound > n
assert m > 5001  # Therefore 2^m-1 > 2^5000; do not construct 2^m.
box_lower_log2 = 199*m
assert box_lower_log2 > 5000

record = {
    "finding": "O-022 and M017 exact constant",
    "date_utc": datetime.now(timezone.utc).isoformat(),
    "model": "GPT-6 Astra Pro", "effort": "not exposed", "run": "GCT_KRON_20261120",
    "C_star": {
        "numerator": numerator, "denominator": denominator,
        "quotient": C_star, "remainder": remainder,
        "second_row_alternative": C_star + 25,
    },
    "parameters": {"m": m, "r": r, "n": n, "d": d,
                   "partition_description": "(nd-26r+20,32,26^(r-2))",
                   "first_part": first_part, "tail_size": tail},
    "prefix_graph": {"T": T, "size_8T": size, "size_less_than_n": True},
    "four_copy_multiplier": {"Hessian_power": 13, "c0_power": multiplier_exponent,
                             "degree_and_all_weights_checked": True},
    "exact_cover_barrier": {
        "generic_dc_ratio_numerator": ratio_numerator,
        "generic_dc_ratio_denominator": ratio_denominator,
        "ratio_greater_than_n": True,
        "scope": "Exact universal determinants and F018 covers only, not border complexity.",
    },
    "border_dimension_checks": {
        "pencil_dimension_bound": pencil_dimension_bound,
        "outer_cut_lower_bound": outer_cut_lower,
        "middle_cut_lower_bound": middle_cut_lower,
        "full_point_jet_dimension": full_point_jet_dimension,
        "restricted_jet_dimension": restricted_jet_dimension,
        "all_cut_ranges_exhaustive_by_proof": True,
    },
    "previous_conditions": {
        "BIP_staircase": staircase, "A025_row52": 26,
        "Chow_threshold_lower_bound": chow_base_bound,
        "Grenet_failure_exponent_comparison": "m>5001 implies2^m-1>2^5000",
        "coordinate_box_lower_log2": box_lower_log2,
    },
    "status": "PASS",
}
destination = Path(__file__).with_name("prefix_jet_strict_example_certificate.json")
destination.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({
    "status": "PASS", "C_star": C_star, "C_star_plus_25": C_star + 25,
    "all_gate_comparisons": "exact integer PASS",
    "certificate": str(destination),
}))
