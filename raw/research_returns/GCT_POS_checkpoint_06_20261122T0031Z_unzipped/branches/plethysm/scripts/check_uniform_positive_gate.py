#!/usr/bin/env python3
"""Exact supplementary checks for PNEW-010 and PNEW-011.

The all-parameter statements have symbolic proofs in the companion TeX.
No floating point arithmetic or external algebra system is used here.
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


def restricted_partitions(total: int, degrees: range) -> int:
    coefficients = [0] * (total + 1)
    coefficients[0] = 1
    for degree in degrees:
        for n in range(degree, total + 1):
            coefficients[n] += coefficients[n - degree]
    return coefficients[total]


def main() -> None:
    rows = []
    for r in range(2, 17):
        m, degree = 2 * r, r * (r + 1)
        distinct = set()
        for mask in range(1 << (r - 1)):
            exponents = [0] * (m - 1)
            used_degree = 0
            for j in range(2, r + 1):
                if mask & (1 << (j - 2)):
                    exponents[2 * j - 2] = 1
                    used_degree += 2 * j
            assert used_degree <= degree and (degree - used_degree) % 2 == 0
            exponents[0] = (degree - used_degree) // 2
            assert sum((i + 2) * a for i, a in enumerate(exponents)) == degree
            distinct.add(tuple(exponents))
        invariant_dimension = restricted_partitions(degree, range(2, m + 1))
        assert len(distinct) == 2 ** (r - 1) <= invariant_dimension
        rows.append({"r": r, "m": m, "b": degree + 1,
                     "explicit_independent_monomials": len(distinct),
                     "exact_lowest_invariant_dimension": invariant_dimension})

    # Enumerate every degree-at-most-four Pluecker monomial for m=4,5,6.
    # Independent Picard- and column-degree calculations must agree.
    dictionary_checks = 0
    symmetric_checks = 0
    for m in (4, 5, 6):
        pairs = list(itertools.combinations(range(m + 1), 2))
        for q in range(5):
            for word in itertools.combinations_with_replacement(range(len(pairs)), q):
                column = [0] * (m + 1)
                exceptional = [0] * m
                c = 0
                for position in word:
                    i, j = pairs[position]
                    column[i] += 1
                    column[j] += 1
                    if j == m:
                        exceptional[i] += 1
                    else:
                        c += 1
                        for h in range(m):
                            if h not in (i, j):
                                exceptional[h] -= 1
                assert all(exceptional[h] == column[h] - c for h in range(m))
                assert column[m] == q - c
                dictionary_checks += 1
                if len(set(exceptional)) == 1 and exceptional[0] <= 0:
                    k = -exceptional[0]
                    assert column == [c-k] * m + [(m-2)*c-m*k]
                    assert q == (m-1)*c-m*k
                    assert q - column[m] == c
                    symmetric_checks += 1

    payload = {
        "status": "PASS",
        "scope": "Supplementary finite exact calibration; symbolic proofs establish all parameters.",
        "minimal_cover_rows": rows,
        "pluecker_monomial_dictionary_checks": dictionary_checks,
        "uniform_exceptional_degree_checks": symmetric_checks,
        "outer_six_quadrics": {"c": 2, "k": 1, "column_weights": [1]*6+[2],
                               "pluecker_degree": 4, "specht_partition": [4, 2],
                               "dimension": 9},
    }
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    encoded = json.dumps(payload, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    print(encoded)


if __name__ == "__main__":
    main()
