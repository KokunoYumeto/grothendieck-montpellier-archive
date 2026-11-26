#!/usr/bin/env python3
"""Certify positivity of the 269 cubic theta kernel by exact finite arithmetic.

The proof of positivity uses Python integers only.  With --central, python-flint
is additionally used for a rigorous enclosure of the central L-value.  No PARI
call, stored coefficient table, or assertion about RH enters this program.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path


def euler_coefficients(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    for p in range(2, math.isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    a = [0] * (limit + 1)
    a[1] = 1
    for n in range(2, limit + 1):
        p, rest, k = spf[n], n, 0
        while rest % p == 0:
            rest //= p
            k += 1
        if p == 269:
            local = 0
        elif p == 3:
            local = 1
        elif p % 3 == 2:
            local = int(k % 2 == 0)
        else:
            tr = 2 if pow(269, (p - 1) // 3, p) == 1 else -1
            prev, local = 1, tr
            for _ in range(2, k + 1):
                prev, local = local, tr * local - prev
        a[n] = a[rest] * local
    return a


def fmul(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    # F_{269^2}=F_269[w]/(w^2+w+1).
    a, b = x
    c, d = y
    return (a * c - b * d) % 269, (a * d + b * c - b * d) % 269


def fpow(x: tuple[int, int], n: int) -> tuple[int, int]:
    ans = (1, 0)
    while n:
        if n & 1:
            ans = fmul(ans, x)
        x = fmul(x, x)
        n >>= 1
    return ans


def lattice_coefficients(limit: int) -> list[int]:
    totals = [0] * (limit + 1)
    bound = math.isqrt(4 * limit // 3) + 1
    for b in range(-bound, bound + 1):
        for a in range(-bound, bound + 1):
            norm = a * a - a * b + b * b
            if not 0 < norm <= limit:
                continue
            residue = (a % 269, b % 269)
            if residue == (0, 0):
                weight = 0
            else:
                cubic = fpow(residue, (269 * 269 - 1) // 3)
                assert cubic in {(1, 0), (0, 1), (268, 268)}
                weight = 2 if cubic == (1, 0) else -1
            totals[norm] += weight
    assert all(v % 12 == 0 for v in totals)
    return [v // 12 for v in totals]


def central_enclosure(a: list[int]) -> dict[str, object]:
    from flint import arb, ctx

    ctx.prec = 240
    alpha = 2 * arb.pi() / arb(217083).sqrt()
    value = arb(0)
    for n in range(1, len(a)):
        if a[n]:
            value += 2 * a[n] * (alpha * n).sqrt().erfc() / arb(n).sqrt()
    nmax = len(a) - 1
    # erfc(sqrt(alpha*n)) <= exp(-alpha*n)/sqrt(pi*alpha*n),
    # and |a(n)| <= d(n) <= n.
    tail = 2 * (-alpha * (nmax + 1)).exp()
    tail /= (arb.pi() * alpha).sqrt() * (1 - (-alpha).exp())
    enclosure = value + arb(0, tail.upper())
    assert enclosure > 0
    return {
        "precision_bits": ctx.prec,
        "terms": nmax,
        "alpha": str(alpha),
        "absolute_tail_bound": str(tail),
        "L_half": str(enclosure),
        "verified_positive": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--central", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    n = 2048
    limit = 8192 if args.central else n
    a = euler_coefficients(limit)
    lattice = lattice_coefficients(limit)
    assert a == lattice, "Independent lattice and Euler coefficients disagree"
    running = 0
    smallest = n
    locations = []
    for k in range(1, n + 1):
        running += a[k]
        if running < smallest:
            smallest, locations = running, [k]
        elif running == smallest:
            locations.append(k)
    assert smallest == 1
    # With r=75/76, sum_{k>n} k r^(k-1) =76(n+76)(75/76)^n.
    # These integer inequalities are the complete uniform tail certificate.
    assert 10**6 * 76 * (n + 76) * 75**n < 76**n
    # alpha > 1/75 follows from pi > 25/8 and sqrt(217083) < 466.
    assert 217083 < 466**2
    assert 2 * 25 * 75 > 8 * 466
    coefficient_bytes = (",".join(map(str, a[1:])) + "\n").encode()
    report: dict[str, object] = {
        "field": "Q(cuberoot(269))",
        "artin_conductor": 217083,
        "positivity_cutoff": n,
        "coefficient_agreement_through": limit,
        "coefficient_sha256": hashlib.sha256(coefficient_bytes).hexdigest(),
        "minimum_partial_sum": smallest,
        "minimum_locations": locations,
        "partial_sum_at_cutoff": running,
        "first_twenty_coefficients": a[1:21],
        "exact_uniform_tail_less_than": "1/1000000 times x",
        "theta_lower_bound_for_t_ge_1": "(999999/1000000) exp(-2*pi*t/sqrt(217083))",
        "checks_passed": True,
    }
    if args.central:
        report["central_value"] = central_enclosure(a)
    output = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
