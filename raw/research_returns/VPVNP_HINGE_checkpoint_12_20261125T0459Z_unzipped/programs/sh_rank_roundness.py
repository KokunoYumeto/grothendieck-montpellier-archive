#!/usr/bin/env python3
"""Exhaustively test roundness two for sqrt(rank(A-B)) over F_2.

Translation invariance permits the first of four matrices to be zero.
No floating-point arithmetic is used: squared distances are ranks.
The original research computation used this direct enumeration.
"""
import itertools


def binary_rank(a, n):
    rows = [(a >> (i * n)) & ((1 << n) - 1) for i in range(n)]
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, n) if rows[i] >> col & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(n):
            if i != rank and rows[i] >> col & 1:
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def main():
    for n in (2, 3):
        q = 1 << (n * n)
        ranks = [binary_rank(a, n) for a in range(q)]
        best = (-999, None)
        for b, c, d in itertools.product(range(q), repeat=3):
            violation = (
                ranks[c] + ranks[b ^ d]
                - ranks[b] - ranks[b ^ c] - ranks[c ^ d] - ranks[d]
            )
            if violation > best[0]:
                best = (violation, (0, b, c, d))
            if violation > 0:
                break
        print(n, best, flush=True)


if __name__ == '__main__':
    main()
