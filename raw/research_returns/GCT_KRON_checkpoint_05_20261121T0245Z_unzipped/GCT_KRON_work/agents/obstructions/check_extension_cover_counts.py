"""Exact positive counts and fixed-architecture optimum checks for O026."""
from datetime import datetime, timezone
from math import comb
from pathlib import Path
import json

count_cases = 0
for u in range(21):
    for v in range(u + 1):
        count = (v + 1)*(u + 1) - v*(v + 1)//2
        direct = sum(u - j + 1 for j in range(v + 1))
        assert count == direct
        assert u + v + 2 == (u + 1) + (v + 1)
        count_cases += 1

m = 2**200
r = m*m
n = m**25
u, v = 999980, 999974
c = (v + 1)*(u + 1) - v*(v + 1)//2
pair_cost = u + v + 2
assert c == 499981500150 and pair_cost == 1999956
assert r - 3 > max(c, pair_cost)
T = m*comb(r + 11, 12)
one_sided_optimum = T*(c + 1)
two_sided_fixed_base_optimum = T*pair_cost
assert two_sided_fixed_base_optimum < n < one_sided_optimum
assert c + 1 < 2**39
assert T < n and one_sided_optimum < 2**39*n
large_order_lower = 2*m*comb(r + 12, 13)
assert large_order_lower > one_sided_optimum
small_order_checks = []
for ell in range(12):
    b = 2*ell + 2
    k = 26 - b
    Tb = m*comb(r - 1 + ell, ell)
    numerator = Tb*comb(r - 3, k)
    denominator = comb(26, k)
    assert numerator > one_sided_optimum*denominator
    small_order_checks.append({"base_order": b, "cover_subset_degree": k,
                               "lower_bound_exceeds_exact_order26_cost": True})
record = {
    "finding": "O-026", "date_utc": datetime.now(timezone.utc).isoformat(),
    "model": "GPT-6 Astra Pro", "effort": "not exposed", "run": "GCT_KRON_20261120",
    "positive_two_part_count_cases": count_cases,
    "O025_exact_counts": {"u": u, "v": v, "one_sided_unique_ideal_size": c,
                          "two_sided_minimum_sum": pair_cost,
                          "one_sided_global_M018_matrix_optimum": one_sided_optimum,
                          "two_sided_fixed_order26_matrix_optimum": two_sided_fixed_base_optimum,
                          "suffix_count": r - 3},
    "other_small_base_orders": small_order_checks,
    "all_base_orders_at_least28_excluded_by_monotone_lower_bound": True,
    "scope": "General count and uniqueness are proved by the missing-unit argument. No optimality for arbitrary maps or all M019 base orders is claimed.",
    "status": "PASS",
}
destination = Path(__file__).with_name("exact_extension_cover_counts_certificate.json")
destination.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"status": "PASS", "count_cases": count_cases,
                  "other_small_orders": len(small_order_checks),
                  "certificate": str(destination)}))
