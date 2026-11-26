"""Exact integer checks for the exponent-seventeen CM obstruction.

No analytic approximation or class-group assumption is used.
The formulas being checked are recorded in local_seventeen_gate.tex.
"""
from itertools import permutations
import json

p = 17
seen = set()
rows = []
for s in range(1, p - 1):
    if s in seen:
        continue
    triple = (1, s, p - 1 - s)
    orbit = sorted({(b * pow(a, -1, p)) % p
                    for a, b, c in permutations(triple)})
    seen.update(orbit)
    r, s, t = triple
    cm_type = [h for h in range(1, p)
               if sum((h * a) % p for a in triple) == p]
    z = (pow(r, r, p * p) * pow(s, s, p * p)
         * pow(t - p, t, p * p)) % (p * p)
    d = ((pow(z, p - 1, p * p) - 1) // p) % p
    residue = (r * s * t * d) % p
    legendre = pow(residue, (p - 1) // 2, p)
    assert legendre in (1, p - 1)
    rows.append({
        "triple": triple,
        "s_orbit": orbit,
        "multiplicity": len(orbit),
        "cm_type": cm_type,
        "inverse_sum_mod17": sum(pow(h, -1, p) for h in cm_type) % p,
        "z_mod289": z,
        "d_mod17": d,
        "rst_d_mod17": residue,
        "hecke_conductor_exponent": 2,
        "hilbert_local_conductor_exponent": 3,
        "root_number": -1 if legendre == 1 else 1,
    })

assert seen == set(range(1, 16))
assert [r["multiplicity"] for r in rows] == [3, 6, 6]
assert [r["d_mod17"] for r in rows] == [8, 13, 11]
assert [r["root_number"] for r in rows] == [-1, 1, -1]
print(json.dumps({"prime": p, "exact_checks": "PASS", "rows": rows}, indent=2))
