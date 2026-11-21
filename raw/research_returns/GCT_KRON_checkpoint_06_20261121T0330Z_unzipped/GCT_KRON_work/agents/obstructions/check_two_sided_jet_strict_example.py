"""Exact certificates for all one-sided base orders in O025."""
from datetime import datetime, timezone
from math import comb, factorial
from pathlib import Path
import json

m = 2**200
r = m*m
n = m**25
d = 3*n
B0 = 1000000
C_star = 190**24 // comb(36111, 12)
T = m*comb(r + 11, 12)
axis_sizes = (B0 - 19, B0 - 25)
two_sided_size = T*sum(axis_sizes)
assert sum(axis_sizes) == 1999956 < C_star == 478126755
assert two_sided_size < n
tail = (B0 + 6) + B0 + 26*(r - 3)
first_part = n*d - 26*r - 1999928
assert tail == 26*r + 1999928
assert first_part + tail == n*d
assert first_part >= B0 + 6 >= B0 >= 26
assert tail <= m*d and r <= d
exponent = d - 13*r - 1499967
assert exponent >= 0
assert 6 + 13*r + 3*499987 + exponent == d
assert 6 + 26 + 2*499987 == B0 + 6
assert 26 + 2*499987 == B0
assert (6*n - 6) + 13*(r*(n - 2) + 2) + 499987*(3*n - 4) + n*exponent == first_part

large_order_lower = 2*m*comb(r + 12, 13)
assert large_order_lower > n
assert T*factorial(12) >= n
assert r - 3 > factorial(12)
forced_prefix_size = comb(B0 - 24, 2)
assert forced_prefix_size == 499975500300 > factorial(12) == 479001600

small_orders = []
for ell in range(12):
    b = 2*ell + 2
    k = 26 - b
    core_half = m*comb(r - 1 + ell, ell)
    cover_numerator = comb(r - 3, k)
    cover_denominator = comb(26, k)
    assert core_half*cover_numerator > n*cover_denominator
    assert 2**k*factorial(ell)*factorial(26) < 2**139 < r
    assert (r - 3) - (k - 1) >= r//2
    small_orders.append({
        "ell": ell, "base_order": b, "forced_subset_degree": k,
        "core_half_size": core_half,
        "cover_lower_numerator": cover_numerator,
        "cover_lower_denominator": cover_denominator,
        "exact_cross_product_exceeds_n": True,
    })
assert 2**24*factorial(11)*factorial(26) < 2**139
assert d - 1 > n

record = {
    "finding": "O-025", "date_utc": datetime.now(timezone.utc).isoformat(),
    "model": "GPT-6 Astra Pro", "effort": "not exposed", "run": "GCT_KRON_20261120",
    "parameters": {"m": m, "r": r, "n": n, "d": d, "B0": B0,
                   "partition_description": "(nd-26r-1999928,1000006,1000000,26^(r-3))",
                   "first_part": first_part, "tail": tail},
    "two_sided_construction": {"axis_sizes": axis_sizes, "C_star": C_star,
                               "size": two_sided_size, "size_less_than_n": True},
    "four_copy_multiplier": {"Wr_power": 13, "W3_power": 499987,
                             "c0_power": exponent, "all_weights_and_degree_checked": True},
    "one_sided_large_orders": {"b_at_least": 28, "matrix_lower_bound": large_order_lower,
                               "exceeds_n": True},
    "one_sided_order26": {"maximum_1_plus_A_budget": factorial(12),
                          "suffix_variables": r - 3,
                          "forced_prefix_size": forced_prefix_size,
                          "contradiction": True},
    "one_sided_small_orders": small_orders,
    "inherited_certificate": "prefix_jet_strict_example_certificate.json",
    "scope": "Every even M018 base order is covered by the three proved cases; no universal lower bound against other coefficient maps is asserted.",
    "status": "PASS",
}
destination = Path(__file__).with_name("two_sided_jet_strict_example_certificate.json")
destination.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "small_order_cases": len(small_orders),
                  "two_sided_factor": sum(axis_sizes),
                  "forced_prefix_size": forced_prefix_size,
                  "certificate": str(destination)}))
