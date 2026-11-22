#!/usr/bin/env python3
"""Exact controls for the two conductor branches of the Cohen U_p congruence.

One prescribed prime and nine prescribed indices; this is not a search for
auxiliary fields, a prime census, or a proof by finite computation.
"""
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path
import hashlib
import json


def bernoulli(n):
    out = [Fraction(1)]
    for m in range(1, n + 1):
        out.append(-sum(Fraction(comb(m + 1, j)) * out[j]
                        for j in range(m)) / (m + 1))
    return out


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    sign = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                sign = -sign
        a, n = n, a
        if a % 4 == n % 4 == 3:
            sign = -sign
        a %= n
    return sign if n == 1 else 0


def quadratic(D, a):
    assert a > 0
    sign = 1
    while a % 2 == 0:
        a //= 2
        if D % 2 == 0:
            return 0
        if D % 8 in (3, 5):
            sign = -sign
    return sign * jacobi(D, a)


def beta(r, D):
    B = bernoulli(r)
    if D == 1:
        return B[r] / r
    f = abs(D)
    sums = [sum(quadratic(D, a) * a ** k for a in range(1, f + 1))
            for k in range(r + 1)]
    return sum(Fraction(comb(r, j)) * B[j]
               * (Fraction(1, f) if j == 0 else f ** (j - 1))
               * sums[r - j] for j in range(r + 1)) / r


def factor(n):
    assert n >= 1
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def fundamental(n):
    assert n != 0 and n % 4 in (0, 1)
    rad = 1 if n > 0 else -1
    sq = 1
    for q, a in factor(abs(n)).items():
        rad *= q ** (a % 2)
        sq *= q ** (a // 2)
    if rad % 4 == 1:
        D, m = rad, sq
    else:
        assert sq % 2 == 0
        D, m = 4 * rad, sq // 2
    assert n == D * m * m
    return D, m


def cohen(r, n):
    if n == 0:
        return -bernoulli(2 * r)[2 * r] / (2 * r)
    signed = (-1) ** r * n
    if signed % 4 not in (0, 1):
        return Fraction(0)
    D, m = fundamental(signed)
    multiplier = 1
    for q, s in factor(m).items():
        multiplier *= (sum(q ** (i * (2 * r - 1)) for i in range(s + 1))
                       - quadratic(D, q) * q ** (r - 1)
                       * sum(q ** (i * (2 * r - 1)) for i in range(s)))
    return -beta(r, D) * multiplier


def residue(value, p):
    assert value.denominator % p
    return value.numerator * pow(value.denominator, -1, p) % p


def main():
    p = 31
    b = (p + 3) // 2
    indices = [0, 1, 2, 3, 4, p, 5 * p, 3 * p * p, 5 * p ** 3]
    rows = []
    for n in indices:
        lhs, rhs = cohen(b, n), cohen(2, p * n)
        left, right = residue(lhs, p), residue(rhs, p)
        assert left == right
        row = {"p": p, "b": b, "n": n,
               "H_b_mod_p": left, "H_2_pn_mod_p": right}
        if n and (-n) % 4 in (0, 1):
            D, m = fundamental(-n)
            Dstar, mstar = fundamental(p * n)
            row.update({"D": D, "m": m, "D_dagger": Dstar,
                        "m_dagger": mstar,
                        "p_divides_D": D % p == 0,
                        "p_divides_m": m % p == 0})
        rows.append(row)
    assert beta(3, -3) == Fraction(2, 9)
    assert beta(3, -43) == 166
    out = {"status": "PASS", "scope": __doc__,
           "arithmetic": "Python standard-library integers and Fraction",
           "cases": rows, "number_of_cases": len(rows),
           "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "claims_not_made": ["uniform theorem from finite testing",
                               "a simultaneous-unit seed",
                               "a prime or discriminant census",
                               "a modular realization of a Hadamard product"]}
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({"status": out["status"], "cases": len(rows),
                      "report": str(target),
                      "report_sha256": hashlib.sha256(target.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
