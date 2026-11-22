#!/usr/bin/env python3
"""Independent finite checks for the explicit normalization of SA09's R_n.

All matrix entries are integers.  No numerical rank or field reduction is used.
The mathematical proof covers all n; this certificate checks n=0,...,8 and
all of their potentially nonzero normalized degrees, with two extra degrees.
"""
from itertools import combinations_with_replacement
from math import comb
from time import perf_counter
import json
from pathlib import Path


def basis(n, m):
    """Characteristic functions of tuples containing 1,...,m."""
    required = set(range(1, m + 1))
    return [t for t in combinations_with_replacement(range(m + 1), n + 1)
            if required.issubset(t)]


def boundary(t, m):
    if m == 0 or 0 in t:
        return None
    return tuple(a - 1 for a in t)


def homotopy(t):
    if 0 not in t:
        return None
    return tuple(a + 1 for a in t)


def main():
    start = perf_counter()
    cases = []
    basis_checks = 0
    matrix_checks = 0
    for n in range(9):
        ranks = []
        for m in range(n + 4):
            b = basis(n, m)
            ranks.append(len(b))
            expected = comb(n + 1, m) if m <= n + 1 else 0
            assert len(b) == expected
            for t in b:
                basis_checks += 1
                dt = boundary(t, m)
                ht = homotopy(t)
                dh = boundary(ht, m + 1) if ht is not None else None
                hd = homotopy(dt) if dt is not None else None
                assert (dh == t and hd is None) or (hd == t and dh is None)
                matrix_checks += 1
                if dt is not None:
                    assert dt in basis(n, m - 1)
                    assert boundary(dt, m - 1) is None
                    matrix_checks += 1
                if ht is not None:
                    assert ht in basis(n, m + 1)
                    assert homotopy(ht) is None
                    matrix_checks += 1
        cases.append({"n": n, "normalized_ranks": ranks})
    result = {
        "statement_ids": ["SA09-A3.1", "A-S09-02"],
        "scope": "R_n for 0 <= n <= 8, 0 <= simplicial degree <= n+3",
        "coefficient_ring": "Z; identities consequently remain valid over any base ring",
        "cases": cases,
        "basis_elements_checked": basis_checks,
        "individual_matrix_identities_checked": matrix_checks,
        "identities": ["d^2=0", "h^2=0", "dh+hd=1", "rank N_m R_n=binomial(n+1,m)"],
        "success": True,
        "elapsed_seconds": perf_counter() - start,
    }
    target = Path(__file__).resolve().parents[1] / "logs" / "A_cosimplicial_tests.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
