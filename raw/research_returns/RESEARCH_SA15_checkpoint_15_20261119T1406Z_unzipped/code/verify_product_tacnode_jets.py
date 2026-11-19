"""Exact finite checks used in the product Hasse-divisor proof.

The tensor checks exhaust the relevant flag configurations over F_2.
They check the displayed linear algebra, not the geometric irreducibility
theorem, whose proof is independent of finite sampling.
"""
from itertools import product
from pathlib import Path
import json
import time

start = time.perf_counter()


def span(vectors):
    result = {0}
    for vector in vectors:
        result |= {old ^ vector for old in tuple(result)}
    return result


def tensor(a, b):
    return sum(((a >> i) & 1) * ((b >> j) & 1) << (3*i+j)
               for i in range(3) for j in range(3))


def jet(flag1, flag2):
    p1, plane1 = flag1
    p2, plane2 = flag2
    return span([tensor(p1, v) for v in plane2] +
                [tensor(v, p2) for v in plane1])


planes = sorted({tuple(sorted(span([a, b])))
                 for a in range(1, 8) for b in range(1, 8) if a != b})
flags = [(p, set(plane)) for plane in planes for p in plane if p]
assert len(planes) == 7 and len(flags) == 21
base = (1, {0, 1, 2, 3})
base_jet = jet(base, base)
assert len(base_jet) == 8
counts = {"rank5": 0, "rank6": 0, "same_point": 0,
          "excluded_bitangent": 0, "inconsistent_same_point_tangent": 0}
crossed_checked = 0
for flag1, flag2 in product(flags, repeat=2):
    p1, plane1 = flag1
    p2, plane2 = flag2
    if (p1 != 1 and plane1 == base[1]) or (p2 != 1 and plane2 == base[1]):
        counts["excluded_bitangent"] += 1
        continue
    if p1 == p2 == 1:
        # For the same geometric point its actual tangent plane is fixed.
        counts["same_point"] += 1
        continue
    if (p1 == 1 and plane1 != base[1]) or (p2 == 1 and plane2 != base[1]):
        counts["inconsistent_same_point_tangent"] += 1
        continue
    other = jet(flag1, flag2)
    common = base_jet & other
    assert len(common) in (1, 2)
    rank = 6 if len(common) == 1 else 5
    counts[f"rank{rank}"] += 1
    if p1 != 1 and p2 != 1:
        crossed = ((1 in plane1 and p2 in base[1]) or
                   (p1 in base[1] and 1 in plane2))
        assert (len(common) == 2) == crossed
        crossed_checked += 1
    else:
        assert len(common) == 2

# Quadratic partial derivatives of F=Y^2 Z+XYZ+X^3+Z^3.
# Monomials in the order X^2, XY, XZ, Y^2, YZ, Z^2.
partials = [0b010001, 0b000100, 0b101010]
assert len(span(partials)) == 8

# Local Cartier value at the tacnode extracts the coefficient of x*y.
# s=y*(y+x^2), u=y+x^2, and delta_s=x.
s = {(0, 2), (2, 1)}
u = {(0, 1), (2, 0)}
delta = {(1, 0)}


def multiply(a, b):
    out = set()
    for i, j in a:
        for k, l in b:
            exponent = (i+k, j+l)
            if exponent in out:
                out.remove(exponent)
            else:
                out.add(exponent)
    return out


for i in range(6):
    for j in range(6-i):
        assert (1, 1) not in multiply(s, {(i, j)})
assert (1, 1) in multiply(delta, u)

result = {
    "status": "PASS",
    "seconds": time.perf_counter()-start,
    "field": "F_2",
    "flags": len(flags),
    "flag_pairs_considered": len(flags)**2,
    "counts": counts,
    "crossed_incidence_equivalences_checked": crossed_checked,
    "independent_polar_quadratics": 3,
    "local_trace_test_monomials": 21,
    "local_trace_delta_u_xy_coefficient": 1,
    "scope": "Exact checks of the stated flag-rank and local polynomial identities; the complete algebraic-geometric proof, not these finite checks, proves all-degree Hasse irreducibility."
}
print(json.dumps(result, indent=2))
