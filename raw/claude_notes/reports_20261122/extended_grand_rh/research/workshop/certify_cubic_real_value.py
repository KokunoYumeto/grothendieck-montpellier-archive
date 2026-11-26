"""Certify L(2/3, psi_269) via its completed theta Mellin transform.

Run with Python and python-flint (tested using python-flint 0.9.0).
Every transcendental quantity is an Arb real ball. Euler coefficients are integers.
"""
from math import isqrt
from flint import arb, ctx


def smallest_prime_factors(limit):
    factors = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if factors[p] != p:
            continue
        for k in range(p*p, limit+1, p):
            if factors[k] == k:
                factors[k] = p
    return factors


def prime_power_coefficient(p, k):
    if p == 3:
        return 1
    if p == 269:
        return 0
    if p % 3 == 2:
        return int(k % 2 == 0)
    if pow(269, (p-1)//3, p) == 1:
        return k + 1
    return (1, -1, 0)[k % 3]


def coefficients(limit):
    spf = smallest_prime_factors(limit)
    result = [0, 1] + [0] * (limit - 1)
    for n in range(2, limit+1):
        p, k, m = spf[n], 0, n
        while m % p == 0:
            m //= p
            k += 1
        result[n] = result[m] * prime_power_coefficient(p, k)
    # Good-prime traces also equal fixed roots of the cubic minus one.
    for p in range(2, min(limit, 600) + 1):
        if spf[p] == p and p not in (3, 269):
            count = sum(pow(t, 3, p) == 269 % p for t in range(p))
            assert result[p] == count - 1
    return result


def completed_ball(limit, precision):
    ctx.prec = precision
    s = arb(2) / 3
    one_minus_s = arb(1) - s
    step = 2 * arb.pi() / arb(217083).sqrt()
    partial = arb(0)
    for n, coefficient in enumerate(coefficients(limit)):
        if not coefficient:
            continue
        x = step * n
        weight = x.gamma_upper(s) / x**s + x.gamma_upper(one_minus_s) / x**one_minus_s
        partial += coefficient * weight
    tail = (2 / step) * (-step*(limit+1)).exp() / (1 - (-step).exp())
    total = partial + arb(0, tail.upper())
    ordinary = total * step**s / s.gamma()
    return total, ordinary, tail


if __name__ == "__main__":
    for terms, bits in [(1200, 96), (3000, 160)]:
        completed, ordinary, tail = completed_ball(terms, bits)
        print(f"N={terms}, precision={bits} bits")
        print("completed:", completed.str(30))
        print("ordinary: ", ordinary.str(30))
        print("absolute completed tail bound:", tail.str(8))
        assert ordinary > 0
        if terms == 3000:
            assert ordinary > arb("2.54362759809209")
            assert ordinary < arb("2.54362759809211")
            assert tail < arb("2.94e-14")
            third = arb(1) / 3
            step = 2 * arb.pi() / arb(217083).sqrt()
            dual = completed * step**third / third.gamma()
            assert dual > arb("5.40163146502760") and dual < arb("5.40163146502764")
            print("ordinary at 1/3 via the functional equation:", dual.str(30))
