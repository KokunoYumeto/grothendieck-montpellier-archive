#!/usr/bin/env python3
"""Rebuild CUE_GCT R-13/R-24 differential minors; Python standard library only.

Examples: python check_projection.py 11 12 --workers 4
          python check_projection.py 17 --workers 4 --output results/r24.json
No saved matrix or original checker is read. Runtime is exponential in n.
"""
import argparse
import hashlib
import json
import math
import multiprocessing as mp
import time


def compositions(n, r):
    if r == 1:
        yield (n,)
    else:
        for a in range(n, -1, -1):
            for tail in compositions(n-a, r-1):
                yield (a,) + tail


def pencil(n):
    state = 20261121 + 1009*n
    out = []
    for _ in range(4*n*n):
        state = (1664525*state + 1013904223) % 2**32
        out.append((state >> 16) % 101)
    return out


def gradient(A, p=101):
    """Forward subset recurrence and its exact reverse differentiation."""
    n = len(A)
    size = 1 << n
    F = [1] + [0]*(size-1)
    for S in range(1, size):
        row = A[S.bit_count()-1]
        bits, value = S, 0
        while bits:
            bit = bits & -bits
            j = bit.bit_length()-1
            value += row[j]*F[S ^ bit]
            bits ^= bit
        F[S] = value % p
    B = [0]*size
    B[-1] = 1
    G = [[0]*n for _ in range(n)]
    for S in range(size-1, 0, -1):
        b = B[S] % p
        if not b:
            continue
        i = S.bit_count()-1
        row, g, bits = A[i], G[i], S
        while bits:
            bit = bits & -bits
            j, T = bit.bit_length()-1, S ^ bit
            B[T] += b*row[j]
            g[j] += b*F[T]
            bits ^= bit
    return [[v % p for v in row] for row in G]


def evaluate(task):
    n, coeff, point = task
    A = [[sum(coeff[4*(n*i+j)+k]*point[k] for k in range(4)) % 101
          for j in range(n)] for i in range(n)]
    G = gradient(A)
    return bytes(point[k]*G[i][j] % 101
                 for i in range(n) for j in range(n) for k in range(4))


def packed_eliminate(matrix, p=101, ordered_pivots=False):
    """Gaussian elimination in packed lanes; returns rank, columns, determinant.

    Each row is one Python integer. All lanes stay between 0 and p-1.
    For b=p.bit_length(), floor(x*floor(2^(2b)/p)/2^(2b))
    differs from floor(x/p) by at most one. A single correction suffices.
    Intermediate products fit in 3b bits; the lanes have at least 4b bits.
    The determinant includes the row-swap sign in original row order.
    """
    n, bits = len(matrix[0]), p.bit_length()
    lane_bytes = (4*bits+7)//8
    lane_bits = 8*lane_bytes
    one = ((1 << (lane_bits*n))-1)//((1 << lane_bits)-1)
    mask = (1 << bits)-1
    low = mask*one
    reciprocal = (1 << (2*bits))//p
    threshold = 1 << (bits+1)
    offset = p*(p-1)*one

    def reduce(x):
        q = ((x*reciprocal) >> (2*bits)) & low
        r = x-p*q
        return r-p*(((r+(threshold-p)*one) >> (bits+1)) & one)

    A = [int.from_bytes(b''.join(int(v).to_bytes(lane_bytes, 'little') for v in row),
                        'little') for row in matrix]
    rank, columns, det = 0, [], 1
    for j in range(n):
        shift = lane_bits*j
        pivot = next((i for i in range(rank, len(A))
                      if (A[i] >> shift) & mask), None)
        if pivot is None:
            continue
        if pivot != rank:
            A[rank], A[pivot] = A[pivot], A[rank]
            if not ordered_pivots:
                det = -det % p
        value = (A[rank] >> shift) & mask
        det = det*value % p
        A[rank] = reduce(A[rank]*pow(value, -1, p))
        row = A[rank]
        for i in range(rank+1, len(A)):
            value = (A[i] >> shift) & mask
            if value:
                A[i] = reduce(A[i]+offset-value*row)
        columns.append(j)
        rank += 1
        if rank == len(A):
            break
    return rank, columns, det


EXPECTED = {11: 42, 12: 87, 13: 25, 14: 69, 15: 73, 16: 8, 17: 88}


def check(n, workers):
    started = time.monotonic()
    points = list(compositions(n, 4))
    coeff = pencil(n)
    tasks = [(n, coeff, point) for point in points]
    if workers == 1:
        matrix = list(map(evaluate, tasks))
    else:
        with mp.Pool(workers) as pool:
            matrix = list(pool.imap(evaluate, tasks, chunksize=1))
    build_seconds = time.monotonic()-started
    digest = hashlib.sha256(b''.join(matrix)).hexdigest()
    if n == 17:
        omitted = {68*i+67 for i in range(1, 16)} | {1091+4*j for j in range(17)}
        selected = [j for j in range(4*n*n) if j not in omitted]
        minor = [bytes(row[j] for j in selected) for row in matrix[:1124]]
        rank, columns, determinant = packed_eliminate(minor)
        assert rank == len(selected) == 1124
    else:
        rank, selected, determinant = packed_eliminate(matrix)
        assert rank == math.comb(n+3, 3)
    assert determinant == EXPECTED[n], (n, determinant)
    return dict(n=n, prime=101, seed=20261121+1009*n, rows=len(points),
                columns=4*n*n, certified_rank=rank, determinant_mod_101=determinant,
                selected_columns=selected, row_major_matrix_sha256=digest,
                build_seconds=round(build_seconds, 3),
                total_seconds=round(time.monotonic()-started, 3),
                algorithm='subset recurrence plus reverse differentiation; packed exact Gaussian elimination')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('sizes', nargs='+', type=int, choices=range(11, 18))
    parser.add_argument('--workers', type=int, default=1)
    parser.add_argument('--output')
    args = parser.parse_args()
    results = []
    for n in args.sizes:
        result = check(n, args.workers)
        results.append(result)
        print(json.dumps(result), flush=True)
        if args.output:
            with open(args.output, 'w') as stream:
                json.dump(results, stream, indent=2)
                stream.write('\n')


if __name__ == '__main__':
    main()
