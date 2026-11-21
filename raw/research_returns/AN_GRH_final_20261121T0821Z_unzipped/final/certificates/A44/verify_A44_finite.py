"""Exact finite algebra for A44, separate from the RR probe.

The theorem for all surfaces/all tower levels is proved in the TeX source.
This script checks its factor identities, a bounded residue sanity check,
and the finite A13 recurrence/norm illustration. It is not formal
verification and does not assert a second RR enumeration implementation.
"""
from pathlib import Path
import hashlib
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
T, q, s, a, b = sp.symbols("T q s a b")
symbolic = []
for epsilon in (1, -1):
    aa = (1 + epsilon * q) * s
    bb = epsilon * (1 + q**2 + q * s**2)
    P = T**4 - aa * T**3 + bb * T**2 - q * aa * T + q**2
    fact = (T**2 - s * T + epsilon) * (
        T**2 - epsilon * q * s * T + epsilon * q**2)
    D = (epsilon * bb - q**2 - 1) * (q + epsilon)**2 - q * aa**2
    assert sp.expand(P - fact) == 0
    assert sp.expand(D) == 0
    symbolic.append({"epsilon": epsilon, "factor_identity": True,
                     "elimination_identity": True})

residue_checks = []
for m in range(5, 17):
    modulus = 1 << m
    counts = {"degree2": 0, "degree4": 0}
    for u in range(1, modulus, 2):
        if u % 8 == 1 or pow(u, 4, modulus) != 1:
            continue
        assert u % 8 == 7
        assert u != 1
        if pow(u, 2, modulus) == 1:
            assert (1 + u) % modulus in (0, modulus // 2)
            counts["degree2"] += 1
        else:
            assert (1 + u + u*u + u*u*u) % modulus == modulus // 2
            counts["degree4"] += 1
    residue_checks.append({"m": m, **counts})

P2 = T**4 - T**2 + 4
N16 = int(sp.resultant(P2, T**16 - 1, T))
traces = [2, 1]
for j in range(2, 9):
    traces.append(traces[-1] - 4 * traces[-2])
elliptic_count8 = 4**8 + 1 - traces[8]
assert elliptic_count8 == 65760
assert N16 == elliptic_count8**2
Dplus, Dminus = -54, -4
L = abs(N16 * (2**4 - 1) * Dplus * Dminus)
factors = {int(k): int(v) for k, v in sp.factorint(L).items()}


def signed_unit_order(ell):
    powers = set()
    value = 1
    while value not in powers:
        powers.add(value)
        value = value * 2 % ell
    return len(powers | {(-x) % ell for x in powers})


eligible = [ell for ell in factors if ell != 2
            and signed_unit_order(ell) == ell - 1]
assert eligible == [3, 5]
assert 137 % 8 == 1
exponents = {}
for ell in eligible:
    group_order = sp.prod(ell**j - 1 for j in range(1, 5))
    value, v = int(group_order), 0
    while value % 2 == 0:
        value //= 2
        v += 1
    exponents[str(ell)] = v
assert exponents == {"3": 9, "5": 11}

X, r, z = sp.symbols("X r z")
h = X**2 + X
f = X**5 + X**3 + X**2 + X
gb = sp.groebner([r**2 + r + 1, z**2 + z + r**2],
                z, r, X, modulus=2)
norm_residual = gb.reduce(f + (z*z + z)*h*h - h*(X+r)**3)[1]
point_residual = gb.reduce(z*z + (r*r+r)*z
                           - (r**5+r**3+r*r+r))[1]
conjugate_residual = gb.reduce(z + (r*r+r) + z*(r*r+r) - 1)[1]
assert norm_residual == point_residual == conjugate_residual == 0

probe_path = ROOT / "probe_A44_theta15.json"
probe = json.loads(probe_path.read_text())
assert probe["rational_projective_count"] == 223
assert probe["nonbranch_count"] == 220
assert probe["rank_histogram"] == {"15": 4, "16": 216}
# This records the probe's output; it does not recompute its matrices.
out = {
    "scope": "Exact symbolic identities and finite A13 values; no formal proof",
    "symbolic_factor_and_D_identities": symbolic,
    "residue_sanity_scope": "Every odd residue mod2^m for 5<=m<=16 only",
    "residue_checks": residue_checks,
    "A13": {
        "frobenius_polynomial": str(P2),
        "quadratic_traces_0_through_8": traces,
        "N16_resultant": N16,
        "N16_factorization": {str(k): int(v) for k, v in sp.factorint(N16).items()},
        "Dplus": Dplus, "Dminus": Dminus,
        "L_factorization": {str(k): v for k, v in factors.items()},
        "eligible_prime_list": eligible,
        "universal_field_bound_exponents": exponents,
        "norm_identity": True, "point_equation": True,
        "nonzero_conjugate_value_one": True,
    },
    "RR_probe_reference": {
        "file": probe_path.name,
        "sha256": hashlib.sha256(probe_path.read_bytes()).hexdigest(),
        "scope": "Separate single implementation retained; not independently rerun here",
        "rank_histogram": probe["rank_histogram"],
        "candidate_points": probe["candidate_points"],
    },
}
target = ROOT / "verify_A44_finite.json"
target.write_text(json.dumps(out, indent=2) + "\n")
print("PASS", json.dumps(out["A13"]))
print("output_sha256", hashlib.sha256(target.read_bytes()).hexdigest())
