"""Finite independent comparisons for the cubic Euler-product decomposition."""
from collections import defaultdict
from functools import lru_cache
from math import isqrt, gcd, log

P = 269


def mul(z, w):
    a, b = z
    c, d = w
    return (a*c - b*d) % P, (a*d + b*c - b*d) % P


@lru_cache(maxsize=None)
def cubic(a, b):
    if a == b == 0:
        return 0, 0
    power = (P*P-1)//3
    result = (1, 0)
    base = (a, b)
    while power:
        if power & 1:
            result = mul(result, base)
        base = mul(base, base)
        power //= 2
    return {(1, 0):(1, 0), (0, 1):(0, 1), (P-1, P-1):(-1, -1)}[result]


def primes(limit):
    return [p for p in range(2, limit+1) if
            all(p % k for k in range(2, isqrt(p)+1))]


def check(limit, z):
    # Compute the complete Hecke coefficient by counting each ideal's six generators.
    doubled_bound = 2*isqrt(limit)+2
    coefficients = [[0, 0] for _ in range(limit+1)]
    for a in range(-doubled_bound, doubled_bound+1):
        for b in range(-doubled_bound,doubled_bound+1):
            n = a*a-a*b+b*b
            if 0 < n <= limit:
                real, omega = cubic(a%P, b%P)
                coefficients[n][0] += real
                coefficients[n][1] += omega
    assert all(w == 0 and v % 6 == 0 for v, w in coefficients)
    coeff = [v//6 for v, w in coefficients]
    # Work on norms prime to 3*269, as in the prime race.
    H = [0]*(limit+1)
    H[1] = 1
    F = [0]*(limit+1)
    F[1] = 1
    prime_logs = defaultdict(float)
    for p in primes(limit):
        if p in (3, P):
            continue
        sign = 1 if p % 3 == 1 else -1
        t = 0 if sign < 0 else 3*(pow(P, (p-1)//3, p)==1)-1
        assert t == coeff[p]
        if p <= z:
            local = [(p, -t), (p*p, sign)]
        else:
            local = [(p*p, sign-t*t), (p*p*p, t*sign)]
            for n in range(limit//p, 0, -1):
                F[n*p] += t*F[n]
            if t:
                prime_logs[p] = t*log(p)
        local = [(d, value) for d, value in local if d <= limit and value]
        max_index = limit // min((d for d, _ in local), default=limit+1)
        for n in range(max_index, 0, -1):
            for d, value in local:
                if n*d <= limit:
                    H[n*d] += value*H[n]
    conv = [0]*(limit+1)
    for d in range(1, limit+1):
        if H[d]:
            for n in range(1, limit//d+1):
                conv[n*d] += H[d]*coeff[n]
    assert all(conv[n]==F[n] for n in range(1,limit+1) if gcd(n, 3*P)==1)
    for m in (3, 12, 3*P, 3*P*P):
        allowed = [n for n in range(1, limit+1) if gcd(n,3*P)==1 and n % m == 1]
        prime_sum = sum(prime_logs[n] for n in allowed if n in prime_logs)
        composite_sum = sum(F[n]*log(n) for n in allowed if n not in prime_logs)
        total = sum(conv[n]*log(n) for n in allowed)
        assert abs(prime_sum+composite_sum-total)<1e-7
        print(limit, z, m, round(prime_sum, 3), round(composite_sum, 3), round(total, 3))


if __name__=="__main__":
    check(30000, 11)
