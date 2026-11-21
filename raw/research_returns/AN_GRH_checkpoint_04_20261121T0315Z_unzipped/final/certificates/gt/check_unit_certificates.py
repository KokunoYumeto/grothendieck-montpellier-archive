#!/usr/bin/env python3
"""Read-only check of the saved unit-group certificates, without any BFS.

Each row supplies a literal prime word.  Re-evaluating all words proves that
every unit occurs.  Euler's product formula, rather than a traversal, supplies
an independent group-order check.  Bounds use the exact rational interval
routine documented in verify_gt_units.py, not rounded decimals.
"""
import csv
from collections import defaultdict
from math import gcd, prod
from pathlib import Path
from verify_gt_units import strict_log_square_cutoff


def prime_factors(n):
    answer = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            answer.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        answer.append(n)
    return answer


def integers(s):
    return tuple(map(int, s.split(','))) if s else ()


def main():
    here = Path(__file__).resolve().parent
    certificates = list(csv.DictReader((here / 'GT_UNIT_CERTIFICATES.tsv').open(), delimiter='\t'))
    words = defaultdict(list)
    for row in csv.DictReader((here / 'GT_UNIT_WORDS.tsv').open(), delimiter='\t'):
        words[int(row['N'])].append(row)
    assert len({int(r['N']) for r in certificates}) == len(certificates)
    total = 0
    for c in certificates:
        n = int(c['N'])
        basis = integers(c['greedy_prime_basis'])
        bound, _, _ = strict_log_square_cutoff(n, 2)
        assert bound == int(c['two_log_squared_exact_floor'])
        for p in basis:
            assert prime_factors(p) == [p] and gcd(p, n) == 1 and p <= bound
        residues = set()
        for w in words[n]:
            assert integers(w['prime_basis']) == basis
            exponents = integers(w['exponents'])
            assert len(exponents) == len(basis) and all(e >= 0 for e in exponents)
            r = prod(pow(p, e, n) for p, e in zip(basis, exponents)) % n
            assert r == int(w['residue']) == int(w['verified_product_mod_N'])
            assert gcd(r, n) == 1 and r not in residues
            residues.add(r)
        phi = n
        for p in prime_factors(n):
            phi = phi // p * (p - 1)
        assert len(residues) == phi == int(c['phi_N_by_enumeration'])
        assert phi == int(c['generated_group_order']) == int(c['word_certificate_rows'])
        assert c['two_bound_generation_verified'] == 'True'
        assert residues == {a for a in range(n) if gcd(a, n) == 1}
        total += phi
    assert set(words) == {int(c['N']) for c in certificates}
    print(f'PASS: {len(certificates)} moduli, {total} independently re-evaluated unit words; strict bounds exact.')


if __name__ == '__main__':
    main()
