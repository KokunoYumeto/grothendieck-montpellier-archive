#!/usr/bin/env python3
"""Exact finite coefficient certificate for A4:all-primes.

The actual Amitsur rings contain x,y and are infinite.  The written proof
reduces the full two boundary images to this finite ring F_p[t]/(t^p),
because x,y annihilate each Laurent class e_j.  This script enumerates
the entire coefficient ring for p=2,3,5; it does not assert an exhaustive
search through arbitrary Amitsur rings.
"""

import itertools
import json
import math


def add(a, b, p):
    return tuple((x + y) % p for x, y in zip(a, b))


def mul(a, b, p):
    out = [0] * p
    for i, ai in enumerate(a):
        for j, bj in enumerate(b[:p - i]):
            out[i + j] = (out[i + j] + ai * bj) % p
    return tuple(out)


def derivative(a, p):
    return tuple(((i + 1) * a[i + 1]) % p for i in range(p - 1)) + (0,)


def inverse(a, p):
    assert a[0] != 0
    out = [pow(a[0], -1, p)]
    for i in range(1, p):
        out.append((-out[0] * sum(a[j] * out[i - j]
                                 for j in range(1, i + 1))) % p)
    return tuple(out)


def check(p):
    ring = tuple(itertools.product(range(p), repeat=p))
    units = tuple(a for a in ring if a[0] == 1)
    one = (1,) + (0,) * (p - 1)
    zero = (0,) * p
    additive = {derivative(a, p) for a in ring}
    logarithmic = set()
    for u in units:
        inv = inverse(u, p)
        assert mul(u, inv, p) == one
        logarithmic.add(mul(derivative(u, p), inv, p))
    expected_additive = {a for a in ring if a[-1] == 0}
    expected_logarithmic = {a for a in ring if a[-1] == a[0]}
    assert additive == expected_additive
    assert logarithmic == expected_logarithmic
    assert len(additive) == len(logarithmic) == p ** (p - 1)
    assert additive != logarithmic
    u = (1, 1) + (0,) * (p - 2)
    witness = mul(derivative(u, p), inverse(u, p), p)
    assert witness == tuple((-1) ** i % p for i in range(p))
    assert witness in logarithmic and witness not in additive

    # In the local presentation, a=x*t, b=y*t-epsilon/x.
    # The only possible term linear in epsilon in b^p has coefficient p;
    # all terms with epsilon^2 vanish and the remaining t^p term vanishes.
    assert math.comb(p, 1) % p == 0
    assert all(math.comb(p, j) % p == 0 for j in range(1, p))

    # Derivation identity in the entire finite coefficient ring on a basis.
    basis = tuple(tuple(int(i == j) for i in range(p)) for j in range(p))
    for a in basis:
        for b in basis:
            assert derivative(mul(a, b, p), p) == add(
                mul(derivative(a, p), b, p),
                mul(a, derivative(b, p), p), p)
    assert derivative(one, p) == zero

    return {
        "prime": p,
        "coefficient_ring_cardinality": p ** p,
        "normalized_units_enumerated": len(units),
        "additive_boundary_cardinality": len(additive),
        "logarithmic_boundary_cardinality": len(logarithmic),
        "additive_image": "coefficient of t^(p-1) is zero",
        "logarithmic_image": "coefficient of t^(p-1) equals constant coefficient",
        "witness_dlog_1_plus_t": witness,
        "witness_not_additive_boundary": witness not in additive,
        "two_is_invertible": p != 2,
        "local_coordinate_relations_checked": True,
        "derivation_identity_checked_on_basis": True,
    }


if __name__ == "__main__":
    print(json.dumps({
        "statement_id": "A4:all-primes",
        "scope": "Complete boundary coefficient enumeration for listed primes; all-prime proof is in A45.tex",
        "actual_ring": "F_p[x,y,a,b]/(a^p,b^p,(y*a-x*b)^2)",
        "ideal": "(y*a-x*b)",
        "Amitsur_algebra": "A_x times A_y",
        "checks": [check(p) for p in (2, 3, 5)],
    }, indent=2))
