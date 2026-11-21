#!/usr/bin/env python3
"""T-037: all outer-four plethysm coefficients by fixed positive polytopes.

Runtime uses only fixed tables and integer arithmetic. It does not import a
character library, symmetric functions, invariant theory, or symbolic algebra.

Examples:
  python outer4_positive.py --outer 4 --inner 5 --output 10,6,3,1
  python outer4_positive.py --outer 3,1 --inner 5 --output 10,6,3,1 --export /tmp/p.json
  python outer4_positive.py --outer 4 --inner 3 --output 6,4,2 --points 20

The export gives exact equality/inequality matrices and separate tags for every
polytope. The optional points mode enumerates at most the requested number of
tagged lattice witnesses. Counting itself has no loops growing with the input.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Iterator

Partition = tuple[int, ...]
TRIV = (4,)
SIGN = (1, 1, 1, 1)
DOUBLE = (2, 2)
STANDARD = (3, 1)
ROTATION = (2, 1, 1)
LABELS = (TRIV, SIGN, DOUBLE, STANDARD, ROTATION)
F = {TRIV: (0,), SIGN: (3,), DOUBLE: (1, 2)}
E = {
    TRIV: (0, 9),
    SIGN: (3, 6),
    DOUBLE: (2, 4, 5, 7),
    STANDARD: (2, 3, 4, 5, 6, 7),
    ROTATION: (1, 3, 4, 5, 6, 8),
}
G = {
    TRIV: (0,),
    SIGN: (3,),
    DOUBLE: (1, 2),
    STANDARD: (0, 1, 2),
    ROTATION: (1, 2, 3),
}


def transpose(mu: Partition) -> Partition:
    return tuple(sum(v >= j for v in mu) for j in range(1, mu[0] + 1))


def tensor_labels(rho: Partition, tau: Partition) -> tuple[Partition, ...]:
    if rho == TRIV:
        return (tau,)
    if rho == SIGN:
        return (transpose(tau),)
    if tau in (TRIV, SIGN):
        return (DOUBLE,)
    if tau == DOUBLE:
        return (TRIV, SIGN, DOUBLE)
    return (STANDARD, ROTATION)


def coin23(N: int) -> int:
    """Number of nonnegative integer solutions of 2*x+3*y=N."""
    if N < 0:
        return 0
    high = N // 3
    first = N % 2
    return 0 if high < first else (high - first) // 2 + 1


def prefix23(N: int) -> int:
    """Number of solutions of 2*x+3*y<=N, in constant integer arithmetic."""
    if N < 0:
        return 0
    t = N // 6
    result = (t + 1) * (N // 2 + 1) - 3 * t * (t + 1) // 2
    if N >= 3:
        t = (N - 3) // 6
        result += (t + 1) * ((N - 3) // 2 + 1) - 3 * t * (t + 1) // 2
    return result


def interval23(low: int, high: int) -> int:
    return 0 if high < low else prefix23(high) - prefix23(low - 1)


def coin246(N: int) -> int:
    if N < 0 or N % 2:
        return 0
    # The coefficient of weight 2 is the uniquely determined slack variable.
    return prefix23(N // 2)


def interval46(low: int, high: int) -> int:
    if high < low:
        return 0
    return prefix23(high // 2) - prefix23((low - 1) // 2)


def solutions23(N: int) -> Iterator[tuple[int, int]]:
    for y in range(max(0, N // 3 + 1)):
        rem = N - 3 * y
        if rem >= 0 and rem % 2 == 0:
            yield rem // 2, y


def interval_solutions23(low: int, high: int) -> Iterator[tuple[int, int]]:
    if high < max(0, low):
        return
    for y in range(high // 3 + 1):
        lo = max(0, (low - 3 * y + 1) // 2)
        hi = (high - 3 * y) // 2
        for x in range(lo, hi + 1):
            yield x, y


def solutions246(N: int) -> Iterator[tuple[int, int, int]]:
    if N < 0 or N % 2:
        return
    for z in range(N // 6 + 1):
        for y in range((N - 6 * z) // 4 + 1):
            x = (N - 6 * z - 4 * y) // 2
            yield x, y, z


@dataclass(frozen=True)
class Polytope:
    kind: str
    tag: tuple
    parameters: tuple[int, ...]

    def count(self) -> int:
        if self.kind == "D":
            low, high, N = self.parameters
            return interval23(low, high) * coin23(N)
        if self.kind == "W":
            M, N = self.parameters
            return coin23(M) * coin246(N)
        if self.kind == "L":
            M, low, high = self.parameters
            return coin23(M) * interval46(low, high)
        raise ValueError("Unknown polytope kind")

    def points(self) -> Iterator[tuple[int, ...]]:
        if self.count() == 0:
            return
        if self.kind == "D":
            low, high, N = self.parameters
            for x in interval_solutions23(low, high):
                for y in solutions23(N):
                    yield x + y
        elif self.kind == "W":
            M, N = self.parameters
            for x in solutions23(M):
                for y in solutions246(N):
                    yield x + y
        else:
            M, low, high = self.parameters
            for x in solutions23(M):
                for y in interval_solutions23((low + 1) // 2, high // 2):
                    yield x + y

    def description(self) -> dict:
        """All coordinates are constrained >=0; inequalities are A*x<=rhs."""
        if self.kind == "D":
            low, high, N = self.parameters
            names = ("x2", "x3", "y2", "y3")
            eq = [[0, 0, 2, 3]]
            eq_rhs = [N]
            le = [[-2, -3, 0, 0], [2, 3, 0, 0]]
            le_rhs = [-low, high]
        elif self.kind == "W":
            M, N = self.parameters
            names = ("x2", "x3", "y2", "y4", "y6")
            eq = [[2, 3, 0, 0, 0], [0, 0, 2, 4, 6]]
            eq_rhs = [M, N]
            le, le_rhs = [], []
        else:
            M, low, high = self.parameters
            names = ("x2", "x3", "y4", "y6")
            eq = [[2, 3, 0, 0]]
            eq_rhs = [M]
            le = [[0, 0, -4, -6], [0, 0, 4, 6]]
            le_rhs = [-low, high]
        return dict(kind=self.kind, tag=self.tag, variables=names,
                    nonnegative=True, equality_matrix=eq, equality_rhs=eq_rhs,
                    inequality_matrix=le, inequality_rhs=le_rhs,
                    integer_points=self.count())


def _D(nu: Partition, low: int, high: int, b: int, component: str):
    if high < low or b < 0:
        return
    for rho, fs in F.items():
        for tau, gs in G.items():
            if nu not in tensor_labels(rho, tau):
                continue
            for f in fs:
                for g in gs:
                    yield Polytope("D", (component, rho, tau, f, g),
                                   (low - f, high - f, b - g))


def _W(nu: Partition, j: int, b: int, component: str):
    if j < 0 or b < 0:
        return
    for rho, fs in F.items():
        for tau, es in E.items():
            if nu not in tensor_labels(rho, tau):
                continue
            for f in fs:
                for e in es:
                    yield Polytope("W", (component, rho, tau, f, e),
                                   (j - f, b - e))


def _L(nu: Partition, j: int, b: int, component: str):
    if j < 0 or b < 0:
        return
    for rho, fs in F.items():
        for tau, es in E.items():
            if nu not in tensor_labels(rho, tau):
                continue
            for f in fs:
                for e in es:
                    yield Polytope("L", (component, rho, tau, f, e),
                                   (j - f, 1 - e, b + 1 - e))


def normalize(mu: Partition, n: int, lam: Partition) -> dict:
    mu, lam = tuple(mu), tuple(lam)
    if mu not in LABELS:
        raise ValueError("Outer partition must be a partition of 4")
    if n < 0 or any(v < 0 for v in lam) or tuple(sorted(lam, reverse=True)) != lam:
        raise ValueError("Use a nonnegative inner degree and a decreasing output partition")
    lam = tuple(v for v in lam if v)
    if sum(lam) != 4 * n:
        raise ValueError("The output partition must have size 4*n")
    if len(lam) > 4:
        return dict(mu=mu, n=n, lam=lam, support_zero=True, complemented=False)
    lam += (0,) * (4 - len(lam))
    complemented = lam[0] - lam[1] < lam[2] - lam[3]
    if complemented:
        height = lam[0]
        lam = tuple(height - v for v in reversed(lam))
        n = height - n
        if height % 2:
            mu = transpose(mu)
    a, b, c, d = lam[0]-lam[1], lam[2]-lam[3], lam[1]-lam[2], lam[3]
    k = max(0, lam[1]-n)
    assert a >= b and c >= 2*k
    nu = transpose(mu) if d % 2 else mu
    return dict(mu=mu, n=n, lam=lam, a=a, b=b, c=c, d=d, k=k, nu=nu,
                support_zero=False, complemented=complemented)


def polytopes(mu: Partition, n: int, lam: Partition) -> tuple[dict, list[Polytope]]:
    data = normalize(mu, n, lam)
    if data["support_zero"]:
        return data, []
    b, c, k, nu = (data[key] for key in ("b", "c", "k", "nu"))
    nu_t = transpose(nu)
    result = list(_D(nu, k, (c-3)//2, b, "bulk"))
    if c % 2:
        result.extend(_L(nu_t, (c-1)//2, b, "C1"))
    else:
        result.extend(_W(nu, c//2, b, "C0"))
        if c >= 2*k + 2:
            result.extend(_D(nu, (c-2)//2, (c-2)//2, b, "C2_induced"))
            result.extend(_W(nu_t, (c-2)//2, b-1, "C2_correction"))
        if c == 2*k:
            result.extend(_W(nu_t, k-1, b-1, "saturation"))
    bound = 36 if nu in (TRIV, SIGN) else 72 if nu == DOUBLE else 108
    assert len(result) <= bound
    return data, result


def coefficient(mu: Partition, n: int, lam: Partition) -> int:
    return sum(p.count() for p in polytopes(mu, n, lam)[1])


def _partition(text: str) -> Partition:
    if not text.strip():
        return ()
    return tuple(int(v) for v in text.split(","))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outer", default="4")
    parser.add_argument("--inner", type=int, required=True)
    parser.add_argument("--output", required=True, help="Comma-separated output parts")
    parser.add_argument("--export", type=Path, help="Write exact polytope matrices as JSON")
    parser.add_argument("--points", type=int, default=0,
                        help="Enumerate at most this many tagged integer witnesses")
    args = parser.parse_args()
    mu, lam = _partition(args.outer), _partition(args.output)
    data, pp = polytopes(mu, args.inner, lam)
    count = sum(p.count() for p in pp)
    print(count)
    if args.export:
        payload = dict(statement="T-037", outer=mu, inner=args.inner, output=lam,
                       oriented=data, coefficient=count,
                       polytopes=[p.description() for p in pp])
        args.export.write_text(json.dumps(payload, indent=2) + "\n")
    remaining = max(0, args.points)
    if remaining:
        for p in pp:
            for point in p.points():
                print(json.dumps(dict(tag=p.tag, point=point)))
                remaining -= 1
                if remaining == 0:
                    return


if __name__ == "__main__":
    main()

