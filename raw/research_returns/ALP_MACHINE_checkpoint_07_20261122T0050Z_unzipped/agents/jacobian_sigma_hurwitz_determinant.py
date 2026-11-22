#!/usr/bin/env python3
"""Exact finite Sato determinant in a truncated Hurwitz residue ring.

The output coefficient n is the nth derivative, not a divided Taylor
coefficient. No factorial is inverted modulo the prime.

For the frame v_j=t^(2-n_j) A(t^14)^(-floor(n_j/2)), with A=1-T A^7,
tau restricted to KP time d is det(sum_m a_mj h_(m+i)), i,j=1..L.
Here h_(d*n)=T^n/n!, all other h vanish. Cauchy--Binet and
Jacobi--Trudi show that L>=d*N captures every derivative through N.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from functools import lru_cache
from hashlib import sha256
import json
from math import comb
from pathlib import Path
from time import monotonic


def binomial_integer(n: int, k: int) -> int:
    if k < 0:
        return 0
    if n >= 0:
        return comb(n, k) if k <= n else 0
    return (-1) ** k * comb(k - n - 1, k)


@lru_cache(None)
def frame_coefficient(m: int, k: int) -> int:
    if k == 0:
        return 1
    numerator = (-1) ** (k - 1) * m * binomial_integer(7*k-m-1, k-1)
    assert numerator % k == 0
    return numerator // k


class Hurwitz:
    def __init__(self, p: int, n: int):
        self.p, self.n = p, n
        self.zero = (0,) * (n+1)
        self.one = (1,) + (0,) * n
        self.binomial = [[comb(i+j, i) % p for j in range(n+1-i)]
                         for i in range(n+1)]

    def add(self, a, b):
        return tuple((x+y) % self.p for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple((x-y) % self.p for x, y in zip(a, b))

    @lru_cache(65536)
    def mul(self, a, b):
        if a == self.zero or b == self.zero:
            return self.zero
        if a == self.one:
            return b
        if b == self.one:
            return a
        out = [0] * (self.n+1)
        right = [(j, y) for j, y in enumerate(b) if y]
        for i, x in enumerate(a):
            if not x:
                continue
            row = self.binomial[i]
            for j, y in right:
                if i+j > self.n:
                    break
                c = row[j]
                if c:
                    out[i+j] += c*x*y
        return tuple(x % self.p for x in out)

    def inv(self, a):
        assert a[0] % self.p
        out = [pow(a[0], -1, self.p)]
        for n in range(1, self.n+1):
            val = sum(comb(n, k)*a[k]*out[n-k] for k in range(1, n+1))
            out.append(-out[0]*val % self.p)
        ans = tuple(out)
        assert self.mul(a, ans) == self.one
        return ans


def determinant(ring: Hurwitz, matrix):
    """Complete unit pivoting, then the exact remaining 2x2 determinant."""
    a = [row[:] for row in matrix]
    size = len(a)
    acc = ring.one
    rank = 0
    while rank < size:
        pivot = next(((i, j) for i in range(rank, size)
                      for j in range(rank, size) if a[i][j][0]), None)
        if pivot is None:
            break
        i0, j0 = pivot
        if i0 != rank:
            a[rank], a[i0] = a[i0], a[rank]
            acc = ring.sub(ring.zero, acc)
        if j0 != rank:
            for row in a:
                row[rank], row[j0] = row[j0], row[rank]
            acc = ring.sub(ring.zero, acc)
        pivot_value = a[rank][rank]
        inverse = ring.inv(pivot_value)
        acc = ring.mul(acc, pivot_value)
        row_entries = [(j, a[rank][j]) for j in range(rank+1, size)
                       if a[rank][j] != ring.zero]
        for i in range(rank+1, size):
            if a[i][rank] == ring.zero:
                continue
            factor = ring.mul(a[i][rank], inverse)
            for j, entry in row_entries:
                a[i][j] = ring.sub(a[i][j], ring.mul(factor, entry))
            a[i][rank] = ring.zero
        rank += 1
    assert size-rank == 2, (size, rank)
    rest = ring.sub(ring.mul(a[rank][rank], a[rank+1][rank+1]),
                    ring.mul(a[rank][rank+1], a[rank+1][rank]))
    return ring.mul(acc, rest), rank


def sigma_jets(p: int, direction: int, order: int, tail: int = 0):
    time = {1: 5, 2: 3, 3: 1}[direction]
    size = max(3, time*order) + tail
    ring = Hurwitz(p, order)
    matrix = []
    for i in range(1, size+1):
        row = []
        for j in range(1, size+1):
            nongap = {1: 0, 2: 2, 3: 4}.get(j, j+2)
            rj = 2-nongap
            m = nongap//2
            coeff = [0] * (order+1)
            low = max(0, -(rj+i)//14)
            high = (time*order-rj-i)//14
            for k in range(low, high+1):
                degree = rj+14*k+i
                if degree >= 0 and degree % time == 0:
                    n = degree//time
                    if n <= order:
                        coeff[n] = (coeff[n]+frame_coefficient(m, k)) % p
            row.append(tuple(coeff))
        matrix.append(row)
    tau, rank = determinant(ring, matrix)
    sigma = [4*pow(pow(2, n, p), -1, p)*x % p
             for n, x in enumerate(tau)]
    return {"prime": p, "direction": direction, "order": order,
            "time": time, "matrix_size": size, "constant_rank": rank,
            "extra_tail": tail, "tau_hurwitz": list(tau),
            "sigma_q_hurwitz": sigma,
            "nonzero_sigma_derivatives": {str(n): x for n, x in enumerate(sigma) if x}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, required=True)
    parser.add_argument("--direction", type=int, required=True, choices=[1, 2, 3])
    parser.add_argument("--order", type=int, required=True)
    parser.add_argument("--tail", type=int, default=0)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    started = monotonic()
    result = sigma_jets(args.prime, args.direction, args.order, args.tail)
    result.update({
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": monotonic()-started,
        "method": "Exact finite Sato/Jacobi-Trudi determinant with unit pivoting in the Hurwitz ring modulo p; no division by a factorial.",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "status": "COMPLETED_EXACT_ARITHMETIC",
    })
    Path(args.output).write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in (
        "prime", "direction", "order", "matrix_size", "constant_rank",
        "nonzero_sigma_derivatives", "elapsed_seconds")}))


if __name__ == "__main__":
    main()
