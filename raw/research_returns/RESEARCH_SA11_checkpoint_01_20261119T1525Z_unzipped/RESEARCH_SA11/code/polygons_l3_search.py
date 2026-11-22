#!/usr/bin/env python3
"""Search L3 against the fixed arrangement, using the exact local fan test."""
from itertools import combinations, permutations, product
import json
import time
from polygons_certificates import (vector_chi, q_from_word, combined_chi,
                                    basis_exchange)


def local_triangles(word, old_chi, q, n):
    result = []
    for a, b in zip(word, word[1:] + word[:1]):
        i, j = abs(a) - 1, abs(b) - 1
        if i == j or not q(i, j):
            continue
        eps, eta = (1 if a > 0 else -1), (1 if b > 0 else -1)
        tests = []
        good = True
        for k in range(n):
            if k in (i, j):
                continue
            terms = (old_chi(i, j, k) * q(i, j),
                     eps * q(i, k), eta * q(j, k))
            nonzero = set(terms) - {0}
            tests.append({"k": k + 1, "signs": terms})
            if len(nonzero) > 1:
                good = False
        if good:
            result.append({"arc": [a, b], "pair": [i + 1, j + 1],
                           "sign_tests": tests})
    return result


def gp_failure(chi, n):
    for lam in range(n):
        for a, b, c, d in combinations([x for x in range(n) if x != lam], 4):
            terms = (chi(lam, a, b) * chi(lam, c, d),
                     -chi(lam, a, c) * chi(lam, b, d),
                     chi(lam, a, d) * chi(lam, b, c))
            nz = set(terms) - {0}
            if len(nz) == 1:
                return {"lambda": lam + 1, "abcd": [x + 1 for x in (a, b, c, d)],
                        "terms": terms}
    return None


def search(vectors):
    n = len(vectors)
    chi = vector_chi(vectors)
    count = 0
    hist = {}
    for rest in permutations(range(2, n + 1)):
        for signs in product((-1, 1), repeat=n - 1):
            first = [1] + [i * s for i, s in zip(rest, signs)]
            word = first + [-i for i in first]
            q = q_from_word(word)
            tris = local_triangles(word, chi, q, n)
            count += 1
            hist[len(tris)] = hist.get(len(tris), 0) + 1
            if len(tris) < 3:
                continue
            ext = combined_chi(chi, q, n)
            fail = gp_failure(ext, n + 1)
            if fail:
                return {"n": n, "vectors": vectors, "searched": count,
                        "triangle_histogram_so_far": hist, "found": True,
                        "word": word, "q": [q(i, j) for i, j in combinations(range(n), 2)],
                        "old_chi": [chi(*t) for t in combinations(range(n), 3)],
                        "triangles": tris, "gp_failure": fail,
                        "full_basis_exchange": basis_exchange(ext, range(n + 1))}
    return {"n": n, "vectors": vectors, "searched": count,
            "triangle_histogram": hist, "found": False}


if __name__ == "__main__":
    start = time.perf_counter()
    families = [
        [(1, t, t*t) for t in range(4)],
        [(1, t, t*t) for t in range(5)],
        [(1, 0, 1), (2, 0, 1), (0, 1, 1), (0, 3, 1), (1, 1, 1), (4, 4, 1)],
        [(1, t, t*t) for t in range(6)],
    ]
    runs = []
    for v in families:
        runs.append(search(v))
        if runs[-1]["found"]:
            break
    print(json.dumps({"runs": runs, "runtime_seconds": time.perf_counter()-start}, indent=2))
