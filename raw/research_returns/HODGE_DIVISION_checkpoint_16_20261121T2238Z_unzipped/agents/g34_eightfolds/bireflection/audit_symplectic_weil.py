#!/usr/bin/env python3
"""Independent endpoint arithmetic for D-SPW01--03; no author code imported.

The universal trace and semilinear arguments are checked in the companion
whole-proof report.  This program only certifies the finite arithmetic after
their proved monotonicity and degree cutoff.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json


def ceilq(x):
    return -((-x.numerator) // x.denominator)


# Square comparisons establish the rational strict upper bounds on radicals.
sqrt3_upper = Q(26, 15)
assert sqrt3_upper ** 2 > 3
assert Q(1, 2) ** 2 > Q(1, 5)
inner_endpoints = {
    "q_ge_5": Q(1, 2) + Q(3, 2) / 24,
    "q3_n_ge_4": (27 * sqrt3_upper + 1) / 80,
    "q3_n3": (9 * sqrt3_upper + 1) / 26,
    "nontrivial_field": Q(2 * 9, 9 ** 2 - 1),
}
assert all(inner_endpoints[k] < Q(3, 5)
           for k in ("q_ge_5", "q3_n_ge_4", "nontrivial_field"))
assert inner_endpoints["q3_n3"] < Q(2, 3)
assert all(Q(a // 6 + 1, a) >= Q(1, 5) for a in (13, 14))

# The universal inequality gives e <= 15 before any finite enumeration.
assert Q(6, 1) / (Q(12, 5) - 2) == 15
allowed = [e for e in range(4, 16) if 12 * ceilq(Q(e, 5)) <= 2 * e + 6]
assert allowed == [4, 5, 9, 10, 15]

# Enumerate all odd prime powers q with q^2 <=31, then all n>=2 with q^n<=31.
def isprime(k):
    return k >= 2 and all(k % p for p in range(2, int(k ** .5) + 1))

prime_powers = set()
for p in range(3, 6, 2):
    if isprime(p):
        q = p
        while q * q <= 31:
            prime_powers.add(q)
            q *= p
cases = []
survivors = []
for q in sorted(prime_powers):
    n = 2
    while q ** n <= 31:
        cases.append([q, n])
        for sign in (-1, 1):
            a = (q ** n + sign) // 2
            if a in allowed:
                survivors.append([q, n, a])
        n += 1
assert cases == [[3, 2], [3, 3], [5, 2]]
assert survivors == [[3, 2, 4], [3, 2, 5]]
assert 4 * 4 > 15

proof = Path(__file__).resolve().parents[2] / "imprimitive/lie_small_fields/symplectic_weil_section.tex"
out = {
    "status": "PASS",
    "scope": "Independent exact finite endpoint and cutoff arithmetic; universal proof checked separately",
    "proof_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
    "trace_ratio_upper_bounds": {k: str(v) for k, v in inner_endpoints.items()},
    "allowed_total_degrees": allowed,
    "complete_prime_power_cases": cases,
    "survivors": survivors,
    "author_program_imported": False,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
