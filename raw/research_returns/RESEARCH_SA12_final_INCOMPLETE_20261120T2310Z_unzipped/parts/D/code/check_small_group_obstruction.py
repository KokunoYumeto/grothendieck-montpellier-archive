"""Finite pigeonhole certificates for the profinite-group obstruction in notes.

This does not realize any of these groups as a geometric fundamental group.
It checks the finite numerical obstruction: d elements of S^m produce only
|S|^d coordinate d-tuples, so m > |S|^d forces repeated coordinates and
prevents generation of S^m.
"""
from math import factorial
from pathlib import Path
from time import perf_counter
import json

start = perf_counter()
certificates = []
for n in range(5, 16):
    order = factorial(n) // 2
    multiplicity = order**n + 1
    assert order % 2 == 0
    for d in range(n + 1):
        assert multiplicity > order**d
    certificates.append({
        "alternating_degree": n,
        "simple_factor_order": order,
        "multiplicity": multiplicity,
        "tested_generator_counts": list(range(n + 1)),
        "minimum_generator_count_lower_bound": n + 1,
    })
output = {
    "purpose": "Auxiliary finite inequalities for an infinite abstract profinite-group example; not a geometric counterexample",
    "certificates": certificates,
    "elapsed_seconds": perf_counter() - start,
}
path = Path(__file__).with_name("check_small_group_obstruction_output.json")
path.write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps({"certificates":len(certificates), "elapsed_seconds":output["elapsed_seconds"]}))
