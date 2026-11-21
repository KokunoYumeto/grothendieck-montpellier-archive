"""G-017: fixed positive polytopes for a five-row plethysm family.

Only the Python standard library is used.  No character or plethysm oracle
is called.  All input-dependent counting uses fixed-size integer formulas.
"""
from __future__ import annotations

import argparse
import json
from math import comb

WEIGHTS = (2, 4, 6, 10)
TAGS = {
    (5,): (0,1,1,1,2,2,3,3,3,4,3,3,3,2,2,1,1,1,0,0),
    (4,1): (1,1,2,5,6,9,11,12,14,14,14,13,12,10,8,6,3,2,1,0),
    (3,2): (0,1,3,5,8,11,13,16,17,17,18,17,15,13,10,7,5,2,1,1),
    (3,1,1): (0,1,3,5,9,12,16,19,20,22,21,21,19,16,13,9,6,3,1,0),
    (2,2,1): (0,1,2,4,7,10,13,15,17,18,18,17,16,14,11,8,5,3,1,0),
    (2,1,1,1): (0,0,1,3,5,8,10,12,14,14,15,14,13,12,9,7,4,2,1,0),
    (1,1,1,1,1): (0,0,0,1,1,1,3,3,3,4,3,4,4,2,3,2,1,1,0,0),
}


def _residue_polynomial():
    values = [1]
    for weight in (1, 2, 3, 5):
        updated = [0] * (len(values) + 30 - weight)
        for degree, coefficient in enumerate(values):
            for residue in range(30 // weight):
                updated[degree + weight * residue] += coefficient
        values = updated
    assert len(values) == 110 and sum(values) == 27000
    return tuple(values)


RESIDUES = _residue_polynomial()


def transpose(mu):
    return tuple(sum(part >= j for part in mu) for j in range(1, mu[0] + 1))


def coin_count(rhs):
    """Number of solutions to 2x+4y+6z+10w=rhs, in at most four terms."""
    if rhs < 0 or rhs % 2:
        return 0
    half = rhs // 2
    return sum(
        RESIDUES[j] * comb((half - j) // 30 + 3, 3)
        for j in range(half % 30, min(half, 109) + 1, 30)
    )


def parameters(k, d, outer=(5,)):
    if not isinstance(k, int) or not isinstance(d, int) or min(k, d) < 0:
        raise ValueError("k and d must be nonnegative integers")
    outer = tuple(outer)
    if outer not in TAGS:
        raise ValueError("outer must be a partition of five")
    effective = outer if d % 2 else transpose(outer)
    lam = (d + 3*k + 2, d + 2*k + 1, d + 1, d + 1, d)
    return outer, effective, d + k + 1, tuple(x for x in lam if x)


def coefficient(k, d, outer=(5,)):
    _, effective, _, _ = parameters(k, d, outer)
    return sum(count * coin_count(k - degree)
               for degree, count in enumerate(TAGS[effective]))


def polytopes(k, d, outer=(5,)):
    """Every tag is retained, including those with an empty polytope."""
    _, effective, _, _ = parameters(k, d, outer)
    return [
        {"tag": [degree, copy], "weights": list(WEIGHTS),
         "rhs": k - degree, "coordinate_lower_bounds": [0, 0, 0, 0]}
        for degree, count in enumerate(TAGS[effective])
        for copy in range(count)
    ]


def lattice_points(rhs):
    """Literal enumeration for review; the coefficient evaluator avoids it."""
    if rhs < 0 or rhs % 2:
        return
    for w in range(rhs // 10 + 1):
        for z in range((rhs - 10*w) // 6 + 1):
            for y in range((rhs - 10*w - 6*z) // 4 + 1):
                residual = rhs - 10*w - 6*z - 4*y
                yield (residual // 2, y, z, w)


def witnesses(k, d, outer=(5,)):
    for poly in polytopes(k, d, outer):
        for point in lattice_points(poly["rhs"]):
            yield {"tag": poly["tag"], "point": point}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--k", required=True, type=int)
    parser.add_argument("--d", required=True, type=int)
    parser.add_argument("--outer", default="5")
    parser.add_argument("--polytopes", action="store_true")
    parser.add_argument("--witnesses", action="store_true")
    args = parser.parse_args()
    outer = tuple(int(x) for x in args.outer.split(","))
    outer, effective, n, lam = parameters(args.k, args.d, outer)
    result = {"statement": "G-017", "outer": outer, "inner": n,
              "lambda": lam, "effective_label": effective,
              "coefficient": coefficient(args.k, args.d, outer),
              "polytope_count": sum(TAGS[effective])}
    if args.polytopes:
        result["polytopes"] = polytopes(args.k, args.d, outer)
    if args.witnesses:
        result["witnesses"] = list(witnesses(args.k, args.d, outer))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
