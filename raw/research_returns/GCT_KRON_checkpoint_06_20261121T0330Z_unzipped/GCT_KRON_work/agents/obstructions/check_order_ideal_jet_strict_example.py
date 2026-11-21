"""Exact finite certificate for the O023 order-ideal strict example."""
from datetime import datetime, timezone
from math import comb, factorial
from pathlib import Path
import json

m = 2**200
r = m*m
n = m**25
d = 3*n
C_star = 190**24 // comb(36111, 12)
order_ideal_size = sum(999975 - c for c in range(29))
assert order_ideal_size == 28998869
assert 1 + order_ideal_size < C_star == 478126755
T = m*comb(r + 11, 12)
size = T*(1 + order_ideal_size)
assert size < n
tail = 1000000 + 28 + 26*(r - 3)
first_part = n*d - 26*r - 1000000 + 50
assert tail == 26*r + 999950
assert first_part + tail == n*d
assert first_part >= 1000000 >= 28 >= 26
assert tail <= m*d and r <= d
exponent = d - 13*r - 999975
assert exponent >= 0
assert 6 + 13*r + 3 + 2*499983 + exponent == d
assert (6*n - 6) + 13*(r*(n - 2) + 2) + (3*n - 4) + 499983*(2*n - 2) + n*exponent == first_part
assert 6 + 26 + 2 + 2*499983 == 1000000
assert 26 + 2 == 28
assert m*m > factorial(13)
large_core = 2*m*comb(r + 12, 13)
small_base_large_prefix = m*comb(r + 12, 13)
simplex_factor = 1 + comb(999976, 2)
assert large_core > n
assert small_base_large_prefix > n
assert simplex_factor > factorial(12)
assert T*simplex_factor > n
assert d - 1 > n
assert (1000000, 28, 26) >= (32, 26, 26)

record = {
    "finding": "O-023",
    "date_utc": datetime.now(timezone.utc).isoformat(),
    "model": "GPT-6 Astra Pro", "effort": "not exposed", "run": "GCT_KRON_20261120",
    "parameters": {"m": m, "r": r, "n": n, "d": d,
                   "partition_description": "(nd-26r-999950,1000000,28,26^(r-3))",
                   "first_part": first_part, "tail": tail},
    "order_ideal": {"size": order_ideal_size, "C_star": C_star,
                    "matrix_size": size, "matrix_size_less_than_n": True},
    "four_copy_multiplier": {"Wr_power": 13, "W3_power": 1,
                             "W2_power": 499983, "c0_power": exponent,
                             "all_degrees_and_weights_checked": True},
    "M017_exhaustive_cases": {
        "b_ge_28_core_lower_bound": large_core,
        "b_26_simplex_factor": simplex_factor,
        "b_26_matrix_lower_bound": T*simplex_factor,
        "b_le_24_prefix_lower_bound": small_base_large_prefix,
        "all_strictly_greater_than_n": True,
    },
    "previous_failures": {
        "support_inclusion": "Gamma_O022 is contained in Gamma_O023",
        "referenced_exact_certificate": "prefix_jet_strict_example_certificate.json",
        "shape_Chow_threshold_lower_bound": d - 1,
    },
    "scope": "Exact finite inequalities and weights; all-parameter M017 cases and support inclusion are proved in text.",
    "status": "PASS",
}
destination = Path(__file__).with_name("order_ideal_jet_strict_example_certificate.json")
destination.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "order_ideal_size": order_ideal_size,
                  "simplex_factor": simplex_factor, "certificate": str(destination)}))
