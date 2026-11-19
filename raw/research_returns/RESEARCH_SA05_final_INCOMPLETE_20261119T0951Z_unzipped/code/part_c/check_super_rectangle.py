"""Exact small checks of the super Young-symmetrizer and trace arguments.

This is a finite verification of representative cases, not a proof of the
general super FFT/SFT. Permutations act by their Koszul signs.
"""
from fractions import Fraction
from itertools import permutations, product
import json


def parity_of_permutation(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p))
                     for j in range(i + 1, len(p))) % 2 else 1


def action(p, word, a):
    """p sends old position i to new position p[i]."""
    sign = -1 if sum(p[i] > p[j] and word[i] >= a and word[j] >= a
                     for i in range(len(p))
                     for j in range(i + 1, len(p))) % 2 else 1
    image = [0] * len(word)
    for i, j in enumerate(p):
        image[j] = word[i]
    return sign, tuple(image)


def subgroup_from_blocks(blocks, n):
    for chosen in product(*(list(permutations(block)) for block in blocks)):
        p = list(range(n))
        for block, rearranged in zip(blocks, chosen):
            for i, j in zip(block, rearranged):
                p[i] = j
        yield tuple(p)


def rectangle_check(a, b):
    nrows, ncols = a + 1, b + 1
    n = nrows * ncols
    rows = [list(range(i * ncols, (i + 1) * ncols)) for i in range(nrows)]
    cols = [[i * ncols + j for i in range(nrows)] for j in range(ncols)]
    row_group = list(subgroup_from_blocks(rows, n))
    col_group = list(subgroup_from_blocks(cols, n))
    total = 0
    for word in product(range(a + b), repeat=n):
        result = {}
        for q in col_group:
            sq, wq = action(q, word, a)
            sq *= parity_of_permutation(q)
            for p in row_group:
                sp, wp = action(p, wq, a)
                result[wp] = result.get(wp, 0) + sp * sq
        assert all(v == 0 for v in result.values()), (a, b, word, result)
        total += 1
    return {"a": a, "b": b, "rectangle": [nrows, ncols],
            "tensor_degree": n, "basis_vectors_checked": total,
            "young_terms": len(row_group) * len(col_group),
            "young_symmetrizer_zero": True}


def exact_rank(columns):
    pivots = {}
    for col in columns:
        v = {i: Fraction(x) for i, x in col.items() if x}
        while v:
            i = min(v)
            if i not in pivots:
                scale = v[i]
                pivots[i] = {j: x / scale for j, x in v.items()}
                break
            scale = v[i]
            for j, x in pivots[i].items():
                v[j] = v.get(j, Fraction(0)) - scale * x
                if v[j] == 0:
                    v.pop(j, None)
    return len(pivots)


def permutation_image_rank(a, b, r):
    basis = list(product(range(a + b), repeat=r))
    indices = {x: i for i, x in enumerate(basis)}
    columns = []
    for p in permutations(range(r)):
        col = {}
        for j, word in enumerate(basis):
            sign, image = action(p, word, a)
            col[indices[image] * len(basis) + j] = sign
        columns.append(col)
    rank = exact_rank(columns)
    return {"a": a, "b": b, "degree": r,
            "group_algebra_dimension": len(columns), "image_rank": rank,
            "kernel_dimension": len(columns) - rank}


def main():
    checks = [rectangle_check(a, b) for a, b in
              [(2, 0), (1, 1), (0, 2), (2, 1), (1, 2)]]
    ranks = [permutation_image_rank(1, 1, r) for r in (3, 4)]
    assert ranks[0]["image_rank"] == 6
    assert ranks[1]["image_rank"] == 20
    # For GL(1|1), Ind_{g0}^g(1) has PBW basis 1,x,y,xy.
    pbw_parities = [0, 1, 1, 0]
    ordinary_dimension = len(pbw_parities)
    superdimension = sum((-1) ** p for p in pbw_parities)
    parity_supertrace = sum((-1) ** p * (-1) ** p for p in pbw_parities)
    assert superdimension == 0 and parity_supertrace == ordinary_dimension == 4
    print(json.dumps({"scope": "finite certificates only",
                      "rectangle_checks": checks,
                      "symmetric_group_image_ranks": ranks,
                      "projective_trace_check": {
                          "group": "GL(1|1)", "PBW_parities": pbw_parities,
                          "superdimension": superdimension,
                          "parity_supertrace": parity_supertrace,
                          "total_dimension": ordinary_dimension},
                      "all_checks_passed": True}, indent=2))


if __name__ == "__main__":
    main()
