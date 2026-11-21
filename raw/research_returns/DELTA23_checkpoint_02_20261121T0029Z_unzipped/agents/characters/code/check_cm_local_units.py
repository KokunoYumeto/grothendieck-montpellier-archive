#!/usr/bin/env python3
"""Finite checks for D23.C4's local unit algebra.

These are independent bounded checks of the integral formulas.  They do not
replace the Hilbert-90 proof, CM reciprocity, or the geometric comparison C5.
No external computer-algebra system is required.
"""
from itertools import product
from math import gcd
import json
from pathlib import Path


def norm(u, ring):
    a, b = u
    return a * a + b * b - (a * b if ring == 3 else 0)


def mul(u, v, ring, m):
    a, b = u
    c, d = v
    return ((a*c-b*d) % m, (a*d+b*c-(b*d if ring == 3 else 0)) % m)


def ratio(u, ring, m):
    n_inv = pow(norm(u, ring), -1, m)
    a, b = mul(u, u, ring, m)
    return (a*n_inv % m, b*n_inv % m)


def residues(m):
    return product(range(m), repeat=2)


def c4(u):
    a, b = u
    return a % 2 == 1 and b % 2 == 0 and (a-1-b) % 4 == 0


rows = []
for k in range(2, 8):
    m = 2**k
    image = {ratio(u, 3, m) for u in residues(m) if u[0] % 2 == 1 and u[1] % 2 == 0}
    target = {u for u in residues(m) if norm(u, 3) % m == 1 and u[0] % 2 == 1 and u[1] % 2 == 0}
    assert image == target, ("O3 at 2", k, image ^ target)
    rows.append({"ring": "O3", "prime": 2, "exponent": k,
                 "condition": "ratio(1+2O)=norm-one and 1 mod 2",
                 "image_order": len(image), "target_order": len(target), "pass": True})

for k in range(1, 6):
    m = 3**k
    domain = [u for u in residues(m) if sum(u) % 3 == 1]
    image = {ratio(u, 3, m) for u in domain}
    target = {u for u in residues(m) if norm(u, 3) % m == 1 and sum(u) % 3 == 1}
    assert image == target, ("O3 at 3", k, image ^ target)
    rows.append({"ring": "O3", "prime": 3, "exponent": k,
                 "condition": "ratio(1+sqrt(-3)O)=norm-one and residue +1",
                 "image_order": len(image), "target_order": len(target), "pass": True})

for k in range(2, 8):
    m = 2**k
    image = {ratio(u, 4, m) for u in residues(m) if c4(u)}
    # The ramified norm-one group scheme at 2 is not smooth: imposing only
    # norm=1 modulo m retains nonlifting solutions.  Reduce solutions two
    # levels farther down to compare with the genuine 2-adic target.
    M = 4*m
    target = {(a % m, b % m) for a, b in residues(M)
              if a % 4 == 1 and b % 4 == 0 and (a*a+b*b) % M == 1}
    assert image == target, ("O4 at 2", k, image ^ target)
    rows.append({"ring": "O4", "prime": 2, "exponent": k,
                 "condition": "ratio(1+(1+i)^3 O)=reduction of norm-one and 1 mod 4",
                 "image_order": len(image), "target_order": len(target),
                 "lift_check_modulus": M, "pass": True})

# For the cubic two-component, norm-one residues 1 mod 2 are exactly +-1 mod 4.
assert {u for u in residues(4) if norm(u, 3) % 4 == 1 and u[0] % 2 == 1 and u[1] % 2 == 0} == {(1, 0), (3, 0)}

# Check the complete sign-normalization map at representative finite levels.
for k2, k3 in [(2, 1), (3, 2), (4, 2)]:
    m2, m3 = 2**k2, 3**k3
    m_two = [u for u in residues(m2) if norm(u, 3) % m2 == 1 and u[0] % 2 == 1 and u[1] % 2 == 0]
    m_three = [u for u in residues(m3) if norm(u, 3) % m3 == 1 and sum(u) % 3 == 1]
    n_two = [u for u in residues(m2) if norm(u, 3) % m2 == 1 and u[0] % 4 == 1 and u[1] % 4 == 0]
    n_three = [u for u in residues(m3) if norm(u, 3) % m3 == 1]
    image = set()
    for u2, u3 in product(m_two, m_three):
        eps = 1 if u2[0] % 4 == 1 else -1
        v2 = tuple(eps*a % m2 for a in u2)
        v3 = tuple(eps*a % m3 for a in u3)
        image.add((v2, v3))
        invsign = 1 if sum(v3) % 3 == 1 else -1
        assert tuple(invsign*a % m2 for a in v2) == u2
        assert tuple(invsign*a % m3 for a in v3) == u3
    assert image == set(product(n_two, n_three))
    assert len(image) == len(m_two)*len(m_three)
    rows.append({"ring": "O3", "condition": "global sign normalization is bijective",
                 "moduli": [m2, m3], "order": len(image), "pass": True})

out = Path(__file__).resolve().parents[1] / "records" / "cm_local_units.json"
out.write_text(json.dumps({"statement": "D23.C4", "scope": "bounded exact checks only", "checks": rows}, indent=2) + "\n")
print(f"PASS: {len(rows)} bounded local-image / normalization checks; certificate: {out}")
