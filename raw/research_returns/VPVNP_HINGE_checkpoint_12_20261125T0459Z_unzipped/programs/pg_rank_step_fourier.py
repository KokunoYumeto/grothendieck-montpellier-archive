#!/usr/bin/env python3
"""Exact finite Fourier certificate for rank-step walks on Mat_n(F_2).

Run from the deliverable directory:
    python programs/pg_rank_step_fourier.py --max-n 4

Input: integer matrix size n, 2 <= n <= --max-n. Matrices are integers whose
bit (i*n+j) is entry (i,j). Representatives of dual-rank classes are diagonal
matrices. Output uses exact Fraction arithmetic; no numerical eigenproblem.
"""
import argparse
from fractions import Fraction


def gf2_rank(bits, n):
    rows = [(bits >> (n * i)) & ((1 << n) - 1) for i in range(n)]
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, n) if rows[i] & (1 << col)), None)
        if pivot is None:
            continue
        rows[pivot], rows[rank] = rows[rank], rows[pivot]
        for i in range(n):
            if i != rank and rows[i] & (1 << col):
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-n', type=int, default=4)
    args = parser.parse_args()
    if not 2 <= args.max_n <= 4:
        parser.error('Exhaustive certificate is deliberately limited to sizes 2,3,4.')
    print('n\tdual_rank\trank1_count\tfull_rank_count\tcharacter_rank1\tcharacter_full_rank\tenergy_ratio')
    for n in range(2, args.max_n + 1):
        rank1 = []
        full = []
        for bits in range(1 << (n*n)):
            r = gf2_rank(bits, n)
            if r == 1:
                rank1.append(bits)
            if r == n:
                full.append(bits)
        ratios = []
        for r in range(1, n + 1):
            b = sum(1 << (i*n+i) for i in range(r))
            c1 = Fraction(sum((-1) ** ((a & b).bit_count() % 2) for a in rank1), len(rank1))
            cn = Fraction(sum((-1) ** ((a & b).bit_count() % 2) for a in full), len(full))
            ratio = (1-cn)/(1-c1)
            ratios.append(ratio)
            print(n, r, len(rank1), len(full), c1, cn, ratio, sep='\t')
            q = 1 << n
            assert c1 == Fraction((1 << (2*n-r)) - (1 << (n+1)) + 1, (q-1)**2)
            denom = 1
            for i in range(n-r+1, n+1):
                denom *= (1 << i)-1
            assert cn == Fraction((-1)**r, denom)
        assert max(ratios) == 2*(1-Fraction(1, 1 << n))


if __name__ == '__main__':
    main()
