#!/usr/bin/env python3
"""Complete exact certificate for D032: mixed arity-six 2-torsion."""
from pathlib import Path
import json
import time
import sympy as sp
from D_bar_indecomposables import analyze, serialize_matrix

started = time.perf_counter()
case = analyze((4, 2))
d6 = sp.Matrix(case["differentials"][6]["matrix"])
d7 = sp.Matrix(case["differentials"][5]["matrix"])
expected = sp.Matrix([
    [-2, 0, 0], [2, 0, 0], [-2, 0, 0],
    [0, -2, 2], [0, 2, -2], [0, 0, -4],
    [0, 1, 1], [0, -1, 1], [0, 0, 0],
    [1, 0, 0], [-2, 0, 0],
])
z = sp.Matrix([0, 0, 0, 0, 0, -2, 1, 0, 0, 0, 0])
lift = sp.Matrix([0, 1, 1])
detector = sp.Matrix([[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]])
checks = 0
assert d6 == expected; checks += 1
assert d7 * d6 == sp.zeros(18, 3); checks += 1
assert d7 * z == sp.zeros(18, 1); checks += 1
assert d6 * lift == 2 * z; checks += 1
assert all(int(c) % 2 == 0 for c in detector * d6); checks += 1
assert int((detector * z)[0]) % 2 == 1; checks += 1
assert d6.extract([6, 7, 9], [0, 1, 2]).det() == 2; checks += 1
assert case["homology_by_form_degree"][7] == {
    "free_rank": 0, "torsion": [2]}; checks += 1
receipt = {
    "statement": "D032: mixed bar PD indecomposables have nonzero arity-six H7",
    "ring": "Z", "parameter": "Z a + Z b", "multidegree": "a^2 b^4",
    "generator_order": "a=(0,1)<b=(1,0); A=gamma2(a), B=gamma2(b), C=ab",
    "form6_basis": ["aabbbb", "ababbb", "abbabb"],
    "form7_basis": ["aabbB", "aabBb", "aaBbb", "ababB", "abaBb",
                    "abbaB", "abbbC", "abbCb", "abCbb", "aCbbb", "Abbbb"],
    "d_form6": serialize_matrix(d6),
    "d_form7": serialize_matrix(d7),
    "order_two_cycle": list(map(int, z)),
    "lift_of_twice_cycle": list(map(int, lift)),
    "mod2_nonboundary_detector": list(map(int, detector)),
    "detector_on_image": serialize_matrix(detector * d6),
    "detector_on_cycle": int((detector * z)[0]),
    "full_exact_complex": case,
    "checks": checks, "runtime_seconds": time.perf_counter() - started,
    "status": "PASS",
}
out = Path(__file__).resolve().parents[1] / "logs/D_bar_mixed_counterexample.json"
out.write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps({"statement": "D032", "checks": checks,
                  "runtime_seconds": receipt["runtime_seconds"],
                  "status": "PASS"}))
