"""Reproduce the private Kummer auxiliary-prime examples with Python 3."""
from math import ceil, isqrt, log, prod


def primes_up_to(limit):
    flags = bytearray([1]) * (limit + 1)
    flags[:2] = bytes(2)
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            flags[p * p::p] = bytes((limit - p * p) // p + 1)
    return [i for i, flag in enumerate(flags) if flag]


def field_product(left, right, p):
    a, b = left
    c, d = right
    return ((a * c - b * d) % p, (a * d + b * c - b * d) % p)


def field_power(element, exponent, p):
    result = (1, 0)
    while exponent:
        if exponent % 2:
            result = field_product(result, element, p)
        element = field_product(element, element, p)
        exponent //= 2
    return result


def table_check(primes, exponent, modulus, start):
    count = ceil(log(start) / (2 * log(exponent)))
    table = [ell for ell in primes if ell % modulus == 1][:count]
    candidates = [p for p in primes if start < p <= 2 * start]
    def fails(p):
        return all(p == ell or pow(p, (ell - 1) // exponent, ell) == 1 for ell in table)
    exceptions = [p for p in candidates if fails(p)]
    print(f"r={exponent} X={start} modulus={modulus} table={table} "
          f"failures={len(exceptions)}/{len(candidates)}")


if __name__ == "__main__":
    primes = primes_up_to(200000)
    assert not any((t**3 + t**2 - 2*t - 1) % 17 == 0 for t in range(17))
    for a,b in [(3,1),(7,3),(9,1)]:
        ell = a*a - a*b + b*b
        v = field_power((a,b),96,17)
        assert (v == (1,0)) == (pow(17, (ell-1)//3, ell) == 1)
        print(f"norm({a}+{b}w)={ell}, cubic test={v}, modular test={pow(17,(ell-1)//3,ell)}")
    for p in primes:
        if p > 900 or p % 9 != 8:
            continue
        least = next(ell for ell in primes if ell % 3 == 1 and pow(p,(ell-1)//3,ell) != 1)
        radius = isqrt(2*least)+2
        norms = [a*a-a*b+b*b for a in range(-radius,radius+1)
                 for b in range(-radius,radius+1)
                 if 0 < a*a-a*b+b*b <= least and (a*a-a*b+b*b) % p and
                 field_power((a,b),(p*p-1)//3,p) != (1,0)]
        assert min(norms) == least
    for r,modulus in [(3,3),(3,36),(5,5),(7,7)]:
        for start in [1000,10000,100000]:
            table_check(primes, r, modulus, start)
