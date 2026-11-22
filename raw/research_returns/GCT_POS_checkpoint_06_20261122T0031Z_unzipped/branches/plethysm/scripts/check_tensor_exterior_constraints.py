#!/usr/bin/env python3
"""Exact small checks accompanying the established exterior constraint.

The representation-theoretic identity is proved in the route note and
credited to Briand--Orellana--Rosas/Stembridge. This script checks only
the explicit PNEW014 violation and the printed Remark9 sufficiency issue.
"""
from collections import Counter
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import json


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    for j in range(min(n, maximum or n), 0, -1):
        for tail in partitions(n-j, j):
            yield (j,)+tail


def chi_two_row_equal(r, cycle):
    # Young's rule: [r,r] = permutation character on r-subsets
    # minus the permutation character on (r-1)-subsets.
    p = [1]+[0]*r
    for j in cycle:
        for k in range(r, j-1, -1):
            p[k] += p[k-j]
    return p[r]-p[r-1]


def main():
    records = []
    total = Fraction(0)
    for mu in partitions(6):
        z = 1
        for j, count in Counter(mu).items():
            z *= j**count * factorial(count)
        chi = chi_two_row_equal(3, mu)
        term = Fraction(chi**3, z)
        total += term
        records.append(dict(cycle=list(mu), centralizer=z, character=chi,
                            contribution=str(term)))
    assert total == 0

    mask_records = []
    for m in (4, 6, 8):
        n = m*m
        E = 2*comb(n, 3)+1
        A = n*n
        L = 1 << (n-2)
        r = (L-A-2)//2
        assert r > m and E+1-A > m
        assert all(A+2*j > m for j in range(1,m))
        # At s=m: J=0, both waves=0, Q0=1, and Q=binomial(m+E,E).
        F = comb(m+E, E)+3
        exterior_bound = comb(m**3, n*m)
        assert exterior_bound == 1 and F > exterior_bound
        mask_records.append(dict(n=n, s=m, E=E, formal_F=str(F),
                                 actual_k=1, exterior_bound=exterior_bound))

    result = dict(status='PASS',
        scope='Established tensor identity; formal model violation; no strict-index theorem.',
        rectangular_33_cube=dict(value=str(total), character_sum=records),
        PNEW014_square_boundary_violations=mask_records)
    target = Path(__file__).resolve().parents[1]/'certificates'/'tensor_exterior_constraints.json'
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
