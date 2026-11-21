#!/usr/bin/env python3
"""Exact Fermat12 character census and integral projector certificate.

Checks all 144 characters of mu12^2 using Z[zeta12]=Z[t]/(t^4-t^2+1).
The degree and cycle bounds are proved in fermat12_degree_proofs.md; this
script verifies their finite character and coefficient inputs. It does not
compute the actual period lattice or saturate an integral Hodge lattice.
"""
from collections import Counter
from itertools import product
from math import gcd, factorial
from pathlib import Path
import hashlib
import json

N = 12
GROUP_ORDER = N * N
UNITS = (1, 5, 7, 11)
GROUP = list(product(range(N), repeat=2))
CHARACTERS = {
    (a, b) for a in range(1, N) for b in range(1, N) if (a + b) % N
}
HOLOMORPHIC = {x for x in CHARACTERS if sum(x) < N}

powers = [(1, 0, 0, 0)]
for _ in range(12):
    c0, c1, c2, c3 = powers[-1]
    powers.append((-c3, c0, c1 + c3, c2))
assert powers[12] == powers[0]
assert all(powers[j] != powers[0] for j in range(1, 12))
powers = powers[:12]


def root_sum(exponents):
    out = [0] * 4
    for exponent in exponents:
        for j, c in enumerate(powers[exponent % N]):
            out[j] += c
    return tuple(out)


seen = set()
records = []
for rep in sorted(CHARACTERS):
    if rep in seen:
        continue
    orbit = sorted({(u * rep[0] % N, u * rep[1] % N) for u in UNITS})
    assert not seen.intersection(orbit)
    seen.update(orbit)
    assert {(N - a, N - b) for a, b in orbit} == set(orbit)
    holo = [x for x in orbit if sum(x) < N]
    assert 2 * len(holo) == len(orbit)
    assert len(holo) in (1, 2)
    scalar_choices = []
    for field, exponent, targets in [
        ("Qi", 3, {3, 9}), ("Qomega", 4, {4, 8})
    ]:
        for axis in (0, 1):
            eigenvalues = {exponent * x[axis] % N for x in holo}
            if len(eigenvalues) == 1 and next(iter(eigenvalues)) in targets:
                scalar_choices.append({
                    "field": field,
                    "automorphism": f"sigma{axis+1}^{exponent}",
                    "zeta12_exponent": next(iter(eigenvalues)),
                })
                break
    assert len(scalar_choices) == 1
    coeff = []
    for x, y in GROUP:
        value = root_sum(-a * x - b * y for a, b in orbit)
        assert value[1:] == (0, 0, 0)
        coeff.append(value[0])
    coeff_map = dict(zip(GROUP, coeff))
    assert all(coeff_map[(x, y)] == coeff_map[(-x % N, -y % N)] for x, y in GROUP)
    assert max(abs(c) for c in coeff) <= len(orbit)

    # Exact Fourier action: 144 times the characteristic function of this orbit.
    for a, b in GROUP:
        image = [0] * 4
        for (x, y), c in zip(GROUP, coeff):
            value = powers[(a * x + b * y) % N]
            for j in range(4):
                image[j] += c * value[j]
        expected = [144 if (a, b) in orbit else 0, 0, 0, 0]
        assert image == expected
    records.append({
        "representative": rep, "orbit": orbit, "holomorphic_characters": holo,
        "dimension": len(holo),
        "conductor": N // gcd(N, gcd(*rep)),
        "pure_integral_scalar_action": scalar_choices[0],
        "integral_coefficients_of_144e": coeff,
        "all_144_Fourier_values_checked": True,
        "Rosati_symmetric_coefficients_checked": True,
    })

assert seen == CHARACTERS
assert len(CHARACTERS) == 110 and len(HOLOMORPHIC) == 55
assert len(records) == 34
factor_counts = Counter(
    (r["conductor"], r["pure_integral_scalar_action"]["field"], r["dimension"])
    for r in records
)
expected_counts = {
    (12, "Qi", 2): 12, (12, "Qomega", 2): 9,
    (6, "Qomega", 1): 9, (4, "Qi", 1): 3, (3, "Qomega", 1): 1
}
assert dict(factor_counts) == expected_counts
multiplicities = {
    field: sum(r["dimension"] for r in records
               if r["pure_integral_scalar_action"]["field"] == field)
    for field in ("Qi", "Qomega")
}
assert multiplicities == {"Qi": 27, "Qomega": 28}

# Arithmetic evaluations only; no geometric family for these tests is constructed.
cycle_bound_examples = [
    {"power": s, "codimension": k,
     "degree_bound": str(8**k * factorial(55*s) * 144**(55*s))}
    for s, k in [(1, 1), (1, 3), (2, 6)]
]
report = {
    "statement_ids": ["SF-F1201", "SF-F1202", "SF-F1203", "SF-F1204"],
    "status": "PASS",
    "coefficient_arithmetic": "exact Z[t]/(t^4-t^2+1)",
    "group_order": 144,
    "H1_character_count": 110,
    "genus": 55,
    "rational_factor_count": 34,
    "factor_counts": [
        {"conductor": d, "field": field, "dimension": dim, "count": count}
        for (d, field, dim), count in sorted(factor_counts.items())
    ],
    "elliptic_multiplicities": multiplicities,
    "projector_denominator_bound": 144,
    "projector_Fourier_values_checked": 34 * 144,
    "group_element_ordering": GROUP,
    "factors": records,
    "isogeny_degree_bound": "144^55",
    "polarization_lower_factor": "1/4",
    "polarization_upper_factor": 4 * 144**2,
    "coordinate_elliptic_degree_bound": 2 * 144**2,
    "divisor_generators_on_power_s": "1513*s^2",
    "cycle_degree_bound_on_power_s_codimension_k": "8^k*(55*s)!*144^(55*s)",
    "cycle_bound_arithmetic_examples": cycle_bound_examples,
    "scope": (
        "Finite character/projector assertions and scalar actions are checked. "
        "Polarization and effective-cycle bounds use the written full proof. "
        "No integral Hodge-lattice saturation or actual period-lattice basis "
        "is asserted to have been computed."
    ),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
target = Path(__file__).with_name("fermat12_certificate_output.json")
target.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({
    "status": "PASS", "factors": len(records), "elliptic_multiplicities": multiplicities,
    "projector_Fourier_values_checked": 34 * 144,
    "isogeny_degree_bound": "144^55",
    "cycle_degree_bound": "8^k*(55*s)!*144^(55*s)",
    "output": str(target),
}))

