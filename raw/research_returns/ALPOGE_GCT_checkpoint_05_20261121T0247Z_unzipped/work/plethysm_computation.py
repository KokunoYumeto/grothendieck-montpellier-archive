"""Exact finite computations supplementing PL findings; not formal certificates."""
from itertools import permutations, combinations_with_replacement, product
from collections import Counter
from fractions import Fraction
from math import floor, ceil, gcd
import json


def canon_pairing(p):
    return tuple(sorted(tuple(sorted(e)) for e in p))


pairings = [canon_pairing(p) for p in (
    ((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))
)]


def ctype(p):
    seen, out = set(), []
    for i in range(len(p)):
        if i in seen:
            continue
        j, size = i, 0
        while j not in seen:
            seen.add(j)
            size += 1
            j = p[j]
        out.append(size)
    return tuple(sorted(out, reverse=True))


classes = {}
cube_sum = norm_sum = 0
for p in permutations(range(4)):
    fixed = sum(canon_pairing(tuple(tuple(p[i] for i in edge) for edge in q)) == q
                for q in pairings)
    chi = fixed - 1
    typ = ctype(p)
    data = classes.setdefault(str(typ), {"size": 0, "fixed_pairings": fixed,
                                         "quotient_character": chi})
    assert data["quotient_character"] == chi
    data["size"] += 1
    cube_sum += chi**3
    norm_sum += chi**2
assert cube_sum == norm_sum == 24

# C2 free orbit: diagonal action on pairs and on multisets.
points = (0, 1)
pair_fixed = sum((1-x, 1-y) == (x, y) for x, y in product(points, repeat=2))
multisets = list(combinations_with_replacement(points, 2))
multi_fixed = sum(tuple(sorted((1-x, 1-y))) == (x, y) for x, y in multisets)
assert pair_fixed == 0 and multi_fixed == 1

# Regular V4: xor action. Invariant multisets of size two do not exist.
v4 = range(4)
v4_multisets = list(combinations_with_replacement(v4, 2))
v4_fixed = sum(all(tuple(sorted((x ^ g, y ^ g))) == (x, y) for g in v4)
               for x, y in v4_multisets)
assert v4_fixed == 0

# KM ray: both 3-variable and genuine 2-variable models, for a finite range.
ray = []
for s in range(101):
    triples = [(a, b, z) for z in range(2) for a in range(s//2+1)
               for b in range(s//3+1) if 2*a+3*b+4*z == s]
    poly = [(t, z) for z in range(2) for t in range(s+1)
            if 3*t+4*z >= s and 2*t+4*z <= s]
    expected = s//3 + int(s % 2 == 0)
    assert len(triples) == len(poly) == expected
    assert {(a+b, z) for a, b, z in triples} == set(poly)
    if s <= 12:
        ray.append({"s": s, "count": expected})

# Independent monomial calculation of binary-dihedral invariants.
for degree in range(201):
    a_invariant_powers = [p for p in range(degree+1)
                          if (2*p-degree) % 6 == 0]
    if degree % 2:
        assert not a_invariant_powers
        continue
    half_degree = degree//2
    invariant_dimension = sum(p < degree-p for p in a_invariant_powers)
    invariant_dimension += int(half_degree in a_invariant_powers
                               and half_degree % 2 == 0)
    assert invariant_dimension == half_degree//3 + int(half_degree % 2 == 0)

# PLE-F6: finite verification of constructive interval cases and reciprocity obstruction.
rescaling_allowed = []
for q in range(1, 37):
    if q % 2 == 0:
        endpoints = (Fraction(0), Fraction(q, 3))
    elif q % 3 == 0:
        endpoints = (Fraction(1, 2), Fraction(q, 3)+Fraction(1, 2))
    else:
        closed_count = q//3
        negative_extension = (-q)//3
        assert -negative_extension == closed_count+1
        continue
    assert gcd(q, 6) > 1
    rescaling_allowed.append(q)
    for s in range(61):
        count = floor(s*endpoints[1])-ceil(s*endpoints[0])+1
        assert count == (q*s)//3 + int((q*s) % 2 == 0)

# Independent direct point enumeration of the hypersurface over small prime fields.
prime_field_counts = {}
for q in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
    count = sum((z*z-u*v*v-4*u**4) % q == 0
                for u in range(q) for v in range(q) for z in range(q))
    assert count == q*q
    prime_field_counts[str(q)] = count

result = {
    "status": "all exact finite checks passed",
    "S4_character_classes": classes,
    "S4_character_norm": norm_sum//24,
    "S4_triple_invariant_dimension": cube_sum//24,
    "C2_pair_fixed_points": pair_fixed,
    "C2_multiset_fixed_points": multi_fixed,
    "V4_regular_two_multiset_fixed_points": v4_fixed,
    "KM_polytope_range_checked": [0, 100],
    "KM_initial_values": ray,
    "binary_dihedral_ordinary_degrees_checked": [0, 200],
    "PLE_F6_q_range_checked": [1, 36],
    "PLE_F6_s_range_checked": [0, 60],
    "PLE_F6_allowed_q": rescaling_allowed,
    "PLE_F7_direct_prime_field_point_counts": prime_field_counts,
    "scope": "finite checks only; whole proofs are read separately"
}
print(json.dumps(result, indent=2))
