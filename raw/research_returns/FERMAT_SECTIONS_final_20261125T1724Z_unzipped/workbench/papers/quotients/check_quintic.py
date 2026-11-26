#!/usr/bin/env python3
"""Exact Euler factors and rigorous central-value certificate for y²+y=x⁵.

The analytic input (CM functional equation, conductor 3125, gamma factor
Gamma(s)^2) is stated and sourced in main.tex. No rank or root-number table
is used. Point counts and Dirichlet coefficients use integer arithmetic;
python-flint/Arb evaluates the two Bessel sums and the proved tail bounds.
"""
from __future__ import annotations
import argparse
import json
from math import isqrt
from pathlib import Path
from flint import arb, ctx


def primes_and_spf(limit: int):
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return [p for p in range(2, limit + 1) if spf[p] == p], spf


def count_fq(p: int) -> int:
    if p == 2:
        return 1 + sum((y*y+y-x**5) % p == 0
                       for x in range(p) for y in range(p))
    def legendre(n: int) -> int:
        r = pow(n % p, (p - 1) // 2, p)
        return -1 if r == p - 1 else r
    return 1 + sum(1 + legendre(1 + 4 * pow(x, 5, p))
                   for x in range(p))


def count_fq2(p: int) -> int:
    # F_4 = F_2[t]/(t²+t+1); odd fields use t²=d with d nonsquare.
    d = 1 if p == 2 else next(a for a in range(1, p)
                              if pow(a, (p - 1) // 2, p) == p - 1)
    def mul(x, y):
        a, b = x
        c, e = y
        return ((a*c+d*b*e) % p,
                (a*e+b*c+(b*e if p == 2 else 0)) % p)
    def fifth(x):
        sq = mul(x, x)
        return mul(mul(sq, sq), x)
    elements = [(a, b) for a in range(p) for b in range(p)]
    counts = {}
    for y in elements:
        yy = mul(y, y)
        rhs = ((yy[0]+y[0]) % p, (yy[1]+y[1]) % p)
        counts[rhs] = counts.get(rhs, 0) + 1
    return 1 + sum(counts.get(fifth(x), 0) for x in elements)


def euler_and_coefficients(limit: int):
    primes, spf = primes_and_spf(limit)
    local = {}
    prime_powers = {}
    for p in primes:
        max_exp = 0
        q = p
        while q <= limit:
            max_exp += 1
            q *= p
        if p == 5:
            polynomial = [1]  # no inertia invariants: CM conductor lambda²
            n1 = n2 = None
        else:
            n1 = count_fq(p)
            trace = p + 1 - n1
            polynomial = [1, -trace]
            n2 = count_fq2(p) if max_exp >= 2 else None
            if n2 is not None:
                numerator = n2 - p*p - 1 + trace*trace
                assert numerator % 2 == 0
                polynomial += [numerator // 2, -p*trace, p*p]
        b = [1]
        for e in range(1, max_exp + 1):
            b.append(-sum(polynomial[j] * b[e-j]
                          for j in range(1, min(e, len(polynomial)-1)+1)))
        prime_powers[p] = b
        local[p] = {"N1": n1, "N2": n2,
                    "Euler_polynomial_known": polynomial,
                    "inverse_coefficients_used": b}
    coefficients = [0] * (limit + 1)
    coefficients[1] = 1
    for n in range(2, limit + 1):
        p = spf[n]
        m, e = n, 0
        while m % p == 0:
            m //= p
            e += 1
        coefficients[n] = coefficients[m] * prime_powers[p][e]
    # Structural consistency checks, independent of subsequent analysis.
    assert all(a == 0 for n, a in enumerate(coefficients) if n % 5 != 1)
    assert local[3]["Euler_polynomial_known"] == [1, 0, 0, 0, 9]
    assert local[11]["Euler_polynomial_known"] == [1, 1, -9, 11, 121]
    assert sum(local[3]["Euler_polynomial_known"]) == 10
    assert sum(local[11]["Euler_polynomial_known"]) == 125
    return local, coefficients


def certificate(limit: int, precision: int):
    ctx.prec = precision
    local, coefficients = euler_and_coefficients(limit)
    pi = arb.pi()
    c = 4*pi/arb(3125).sqrt().sqrt()
    theta = arb(0)
    central = arb(0)
    for n, a in enumerate(coefficients):
        if not a:
            continue
        sn = arb(n).sqrt()
        z = c*sn
        theta += 2*a*z.bessel_k(0)
        central += 2*c*a*z.bessel_k(1)/sn
    # |a_n| <= d_4(n) sqrt(n) <= n^(7/2).
    # K_0(t) <= e^-t sqrt(pi/(2t));
    # K_1(t) <= e^-t sqrt(pi/(2t)) exp(1/(2t)).
    # For decreasing f, sum_{n>N} f(n) <= integral_N^infty f(x) dx.
    z0 = c*arb(limit).sqrt()
    assert z0 > arb(13)/2  # monotonicity for the larger exponent 13/4
    common = (pi/(2*c)).sqrt()
    theta_tail = 4*common*c**(-arb(17)/2)*z0.gamma_upper(arb(17)/2)
    central_tail = (4*c*common*(1/(2*z0)).exp()
                    *c**(-arb(15)/2)*z0.gamma_upper(arb(15)/2))
    theta_ball = theta + arb(0, theta_tail.upper())
    central_ball = central + arb(0, central_tail.upper())
    assert theta_ball > 0, "Root number not certified by this truncation"
    assert central_ball > 0, "Nonvanishing not certified by this truncation"
    return {
        "curve": "y^2+y=x^5", "conductor": 3125,
        "coefficient_bound": "abs(a_n) <= d_4(n)*sqrt(n) <= n^(7/2)",
        "limit": limit, "precision_bits": precision,
        "c": str(c), "theta_at_one": str(theta_ball),
        "theta_omitted_tail_upper": str(theta_tail.upper()),
        "root_number": 1, "L_at_one": str(central_ball),
        "L_omitted_tail_upper": str(central_tail.upper()),
        "positive_theta": True, "positive_L": True,
        "local_factors": local,
        "coefficients": coefficients[1:]
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=4096)
    parser.add_argument("--precision", type=int, default=192)
    parser.add_argument("--output", type=Path, default=Path("quintic_certificate.json"))
    args = parser.parse_args()
    result = certificate(args.limit, args.precision)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    for key in ["limit", "precision_bits", "theta_at_one", "theta_omitted_tail_upper",
                "root_number", "L_at_one", "L_omitted_tail_upper"]:
        print(f"{key}: {result[key]}")
