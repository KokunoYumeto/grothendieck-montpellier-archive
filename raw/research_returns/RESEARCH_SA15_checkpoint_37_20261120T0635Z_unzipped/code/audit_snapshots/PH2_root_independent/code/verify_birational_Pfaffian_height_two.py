#!/usr/bin/env python3
"""Exact, dependency-free F2 reconstruction of the PH2 counterexample.

The uniform proof is in the accompanying TeX.  This program checks five
specified sizes by perfect-matching Pfaffians, sparse polynomial arithmetic,
and exact binary ranks; it does not infer the uniform theorem from samples.
"""
from __future__ import annotations

import hashlib
import json
import time
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path


def run_size(n: int) -> dict:
    assert n >= 5 and n % 2 == 1
    m = (n - 1) // 2
    zero = frozenset()
    one = frozenset({(0,) * n})

    def variable(i):
        e = [0] * n
        e[i] = 1
        return frozenset({tuple(e)})

    x = [variable(i) for i in range(n)]

    def add(*ps):
        out = zero
        for p in ps:
            out = out ^ p
        return out

    def mul(a, b):
        out = set()
        for u in a:
            for v in b:
                w = tuple(ui + vi for ui, vi in zip(u, v))
                if w in out:
                    out.remove(w)
                else:
                    out.add(w)
        return frozenset(out)

    def power(p, e):
        out = one
        while e:
            if e & 1:
                out = mul(out, p)
            p = mul(p, p)
            e //= 2
        return out

    def compose(p, coordinates):
        out = zero
        for mon in p:
            term = one
            for j, e in enumerate(mon):
                if e:
                    term = mul(term, power(coordinates[j], e))
            out = add(out, term)
        return out

    def partner(i):
        assert 1 <= i < n
        return i + 1 if i % 2 else i - 1

    b = [[zero for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        b[0][i] = b[i][0] = x[i]
    for j in range(1, m):
        b[2 * j - 1][2 * j] = b[2 * j][2 * j - 1] = x[0]
    b[n - 2][n - 1] = b[n - 1][n - 2] = x[1]
    assert all(b[i][i] == zero for i in range(n))
    assert all(b[i][j] == b[j][i] for i in range(n) for j in range(n))

    @lru_cache(None)
    def pfaff(indices):
        if not indices:
            return one
        i = indices[0]
        out = zero
        for offset in range(1, len(indices)):
            j = indices[offset]
            if b[i][j]:
                rest = indices[1:offset] + indices[offset + 1:]
                out = add(out, mul(b[i][j], pfaff(rest)))
        return out

    raw = [pfaff(tuple(j for j in range(n) if j != i)) for i in range(n)]
    assert all(len(p) == 1 for p in raw)
    raw_exponents = [next(iter(p)) for p in raw]
    exact_gcd = tuple(min(e[j] for e in raw_exponents) for j in range(n))
    assert exact_gcd == (m - 2,) + (0,) * (n - 1)
    reduced = [
        frozenset({tuple(e[j] - exact_gcd[j] for j in range(n))})
        for e in raw_exponents
    ]
    sigma = [mul(x[0], x[1])]
    sigma += [mul(x[1], x[partner(i)]) for i in range(1, n - 2)]
    sigma += [mul(x[0], x[partner(i)]) for i in range(n - 2, n)]
    assert reduced == sigma
    reduced_gcd = tuple(
        min(next(iter(p))[j] for p in reduced) for j in range(n)
    )
    assert reduced_gcd == (0,) * n
    for i in range(n):
        assert add(*(mul(b[i][j], sigma[j]) for j in range(n))) == zero

    tau = [power(x[0], 2)]
    tau += [mul(x[0], x[partner(i)]) for i in range(1, n - 2)]
    tau += [mul(x[2], x[partner(i)]) for i in range(n - 2, n)]
    scalar_left = mul(x[0], power(x[1], 2))
    scalar_right = mul(power(x[0], 2), x[2])
    assert [compose(p, sigma) for p in tau] == [mul(scalar_left, t) for t in x]
    assert [compose(p, tau) for p in sigma] == [mul(scalar_right, t) for t in x]

    # Minimal primes of a monomial ideal are its minimal support hitting sets.
    covers = {frozenset()}
    for p in reduced:
        support = frozenset(j for j, e in enumerate(next(iter(p))) if e)
        candidates = set()
        for cover in covers:
            if cover & support:
                candidates.add(cover)
            else:
                candidates.update(cover | {j} for j in support)
        covers = {
            c for c in candidates if not any(d < c for d in candidates)
        }
    expected_primes = {frozenset({0, 1}), frozenset({1, n - 2, n - 1})}
    assert covers == expected_primes

    # Reconstruct M_s from the coefficient tensor of B_lambda.
    multiplication = [[zero for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for mon in b[i][j]:
                assert sum(mon) == 1
                k = mon.index(1)
                multiplication[k][j] = add(multiplication[k][j], x[i])
    for j in range(n):
        assert add(
            *(mul(multiplication[k][j], tau[k]) for k in range(n))
        ) == zero
    for k in range(n):
        assert add(
            *(mul(multiplication[k][j], x[j]) for j in range(n))
        ) == zero

    def evaluate(p, point):
        total = 0
        for mon in p:
            term = 1
            for j, exponent in enumerate(mon):
                if exponent and not point[j]:
                    term = 0
                    break
            total ^= term
        return total

    def binary_rank(matrix):
        rows = [sum((v & 1) << j for j, v in enumerate(row)) for row in matrix]
        rank = 0
        for j in range(n):
            pivot = next((i for i in range(rank, len(rows)) if rows[i] >> j & 1), None)
            if pivot is None:
                continue
            rows[rank], rows[pivot] = rows[pivot], rows[rank]
            for i in range(len(rows)):
                if i != rank and rows[i] >> j & 1:
                    rows[i] ^= rows[rank]
            rank += 1
        return rank

    section = [int(i in (0, 2)) for i in range(n)]
    functional = [int(i in (0, 1)) for i in range(n)]
    b_at = [[evaluate(p, functional) for p in row] for row in b]
    m_at = [[evaluate(p, section) for p in row] for row in multiplication]
    assert binary_rank(b_at) == binary_rank(m_at) == n - 1
    assert [evaluate(p, section) for p in tau] == functional
    assert [evaluate(p, functional) for p in sigma] == section
    assert all(sum(v * w for v, w in zip(row, section)) % 2 == 0 for row in b_at)
    assert all(
        sum(functional[k] * m_at[k][j] for k in range(n)) % 2 == 0
        for j in range(n)
    )

    return {
        "N": n,
        "m": m,
        "pfaffians_reconstructed": n,
        "raw_gcd_exponents": list(exact_gcd),
        "reduced_degree": 2,
        "reduced_gcd_is_one": True,
        "both_birational_compositions": True,
        "radical_and_reciprocal_tensor_identities": True,
        "minimal_primes": [sorted(c) for c in sorted(covers, key=lambda c: (len(c), sorted(c)))],
        "minimal_prime_heights": [2, 3],
        "common_pair_B_rank": n - 1,
        "common_pair_M_rank": n - 1,
        "status": "PASS",
    }


def main():
    started = time.perf_counter()
    cases = [run_size(n) for n in (5, 7, 9, 11, 13)]
    output = {
        "status": "PASS",
        "actual_utc": datetime.now(timezone.utc).isoformat(),
        "runtime_seconds": time.perf_counter() - started,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "cases": cases,
        "scope": (
            "Exact F2 polynomial reconstructions at five stated sizes. "
            "The accompanying written proof establishes all odd N>=5. "
            "No actual Cartier realization, Lang reducibility, or monodromy failure is asserted."
        ),
    }
    destination = Path(__file__).resolve().parents[1] / "outputs" / "birational_Pfaffian_height_two_checks.json"
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
