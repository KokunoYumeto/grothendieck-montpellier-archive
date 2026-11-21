#!/usr/bin/env python3
"""Exact integer certificates for P-03--P-05; no random samples."""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json


def add_term(dst, key, value):
    dst[key] += value
    if dst[key] == 0:
        del dst[key]


def check_star(k, delta):
    # Store t^power times a_i tensor e_j tensor e_l, over Z[t,t^-1].
    expansion = defaultdict(int)
    for i in range(1, k + 1):
        for j, p, coeff_b in [(0, 0, 1), (i, 1, delta)]:
            for ell, q, coeff_c in [(0, 0, 1), (i, 1, 1)]:
                add_term(expansion, (p + q - 1, i, j, ell), coeff_b * coeff_c)
        add_term(expansion, (-1, i, 0, 0), -1)
    expected = defaultdict(int)
    for i in range(1, k + 1):
        expected[(0, i, 0, i)] = 1
        expected[(0, i, i, 0)] = delta
        expected[(1, i, i, i)] = delta
    assert dict(expansion) == dict(expected)
    assert all(p >= 0 for p, *_ in expansion)
    return {"k": k, "delta": delta, "terms_before_cancellation": k + 1,
            "identity_over": "Z[t,t^-1]", "pass": True}


def check_anchored(sigma):
    # One edge's finite-difference identity, with a=0,x=1,y=2,z=3.
    vectors = [([(0, 0, 1), (1, 1, 1), (2, 1, 1), (3, 2, sigma)], 1),
               ([(0, 0, 1), (1, 1, 1)], -1),
               ([(0, 0, 1), (2, 1, 1)], -1),
               ([(0, 0, 1)], 1)]
    expansion = defaultdict(int)
    for vector, sign in vectors:
        for i, p, c in vector:
            for j, q, d in vector:
                add_term(expansion, (p + q - 2, i, j), sigma * sign * c * d)
    assert all(p >= 0 for p, *_ in expansion)
    constant = {(i, j): val for (p, i, j), val in expansion.items() if p == 0}
    assert constant == {(0, 3): 1, (3, 0): 1, (1, 2): sigma, (2, 1): sigma}
    return {"sigma": sigma, "identity_over": "Z[t,t^-1]", "pass": True,
            "full_expansion": [[list(key), val] for key,val in sorted(expansion.items())]}


def row_slice(edge, sigma):
    a, b = edge
    return {(a, b): 1, (b, a): sigma}


def poly_slice(rectangle, sigma):
    (r, s), (c, d) = rectangle
    a, b, e, f = (r, c), (r, d), (s, c), (s, d)
    return {(a, f): 1, (f, a): 1, (b, e): sigma, (e, b): sigma}


def koszul_minor(slices):
    # Choose one nonzero column for each row of [-Q2 | Q1].
    # As every selected slice is a signed matching, each selected column
    # has exactly one nonzero entry, producing a signed permutation minor.
    ordered = [(slices[1], -1), (slices[0], 1)]
    support = sorted({row for sl, _ in ordered for row, col in sl})
    chosen = []
    signs = []
    for row in support:
        found = False
        for block, (sl, block_sign) in enumerate(ordered):
            candidates = [(col, val) for (rr, col), val in sl.items() if rr == row]
            if candidates:
                col, val = candidates[0]
                assert sum(cc == col for rr, cc in sl) == 1
                chosen.append((block, col))
                signs.append(block_sign * val)
                found = True
                break
        assert found
    assert len(set(chosen)) == len(chosen)
    determinant = 1
    for val in signs:
        determinant *= val
    assert determinant in (-1, 1)
    return len(support), determinant, chosen


def run():
    stars = [check_star(k, delta) for k in range(1, 6) for delta in (-1, 1)]
    edges = list(combinations(range(4), 2))
    rectangles = [(I, J) for I in edges for J in edges]
    output = {"star_identities": stars,
              "anchored_finite_difference_identities": [check_anchored(sigma) for sigma in (-1, 1)],
              "families": {}}
    for label, objects, make_slice in [
        ("row", edges, row_slice), ("polynomial", rectangles, poly_slice)
    ]:
        for sigma in (-1, 1):
            counts = defaultdict(int)
            witnesses = {}
            for x, y in combinations(objects, 2):
                rank, determinant, chosen = koszul_minor([make_slice(x, sigma), make_slice(y, sigma)])
                if label == "row":
                    expected = len(set(x) | set(y))
                else:
                    (I, J), (K, L) = x, y
                    expected = 8 - len(set(I) & set(K)) * len(set(J) & set(L))
                assert rank == expected
                counts[rank] += 1
                witnesses.setdefault(rank, {"pair": [x, y], "minor_determinant": determinant,
                                           "minor_columns": chosen})
            name = label + ("_det" if sigma == -1 else "_per")
            output["families"][name] = {
                "pencil_count": sum(counts.values()),
                "koszul_rank_histogram": dict(sorted(counts.items())),
                "minimum": min(counts), "witnesses": witnesses,
                "valid_in_every_characteristic": True,
                "certificate": "Every lower minor has determinant +1 or -1 over Z."
            }
    # The polynomial adjacent pair is exactly two disjoint symmetric stars.
    for sigma in (-1, 1):
        first = poly_slice(((0, 1), (0, 1)), sigma)
        second = poly_slice(((0, 1), (0, 2)), sigma)
        a, b, c, d, e, f = (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)
        assert first == {(a, e): 1, (e, a): 1, (d, b): sigma, (b, d): sigma}
        assert second == {(a, f): 1, (f, a): 1, (d, c): sigma, (c, d): sigma}
    output["adjacent_polynomial_two_star_identity"] = "PASS over Z"
    path = Path(__file__).with_name("pencil_certificate.json")
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "certificate": str(path),
                      "families": {k: {x:v[x] for x in ["pencil_count", "koszul_rank_histogram", "minimum"]}
                                   for k,v in output["families"].items()}}, indent=2))


if __name__ == "__main__":
    run()
