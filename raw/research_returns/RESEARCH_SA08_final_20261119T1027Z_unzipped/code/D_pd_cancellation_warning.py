#!/usr/bin/env python3
"""Finite first-degree certificate for the C18 cancellation warning."""
from math import factorial, gcd
from pathlib import Path
import json
import time

started = time.perf_counter()
cases = []
for p in (2, 3, 5):
    a0 = factorial(p) // p
    coefficient = p * a0
    assert gcd(a0, p) == 1
    assert gcd(coefficient, p * p) == p
    assert {coefficient * x % p for x in range(p)} == {0}
    assert 1 not in {coefficient * x % p for x in range(p)}
    assert 2 * p * p - 2 > 2 * p - 1
    cases.append({
        "prime": p, "first_generator_form_degrees": [2 * p - 2, 2 * p - 1],
        "differential_matrix": [[coefficient]], "unit_factor": a0,
        "localized_smith_invariant": p,
        "first_cohomology": "Z/%d in form degree %d" % (p, 2 * p - 1),
        "next_repair_generator_degree": 2 * p * p - 2,
        "status": "PASS",
    })
out = {"statement": "Deleting the original odd identity disk from C18 need not preserve acyclicity",
       "scope": "first positive cohomology for p=2,3,5; general proof in D_global_local_repair_gate.md",
       "checks": 15, "cases": cases,
       "runtime_seconds": time.perf_counter() - started}
path = Path(__file__).resolve().parents[1] / "logs/D_pd_cancellation_warning.json"
path.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"checks": out["checks"], "cases": len(cases),
                  "runtime_seconds": out["runtime_seconds"], "status": "PASS"}))
