"""Check formula (2) by enumerating multiplication matrices over finite fields."""
from fractions import Fraction
from itertools import combinations, product
from math import gcd, isqrt, prod


def kernel_dimension(u, v, w, p):
    # Integral basis 1, a, b for a^3=269 and b=(a^2-a+1)/3.
    # a^2=a+3b-1, ab=90-b, b^2=30a+b-60. The basis discriminant
    # is -3*269^2, the field discriminant. Columns multiply the basis.
    rows = ((u, -v + 90*w, 90*v - 60*w),
            (v, u + v, 30*w),
            (w, 3*v - w, u - v + w))
    a, b, c = rows
    det = sum(a[i] * (b[(i+1) % 3]*c[(i+2) % 3]
                      - b[(i+2) % 3]*c[(i+1) % 3]) for i in range(3))
    if det % p:
        return 0
    for r, s in combinations(rows, 2):
        if any((r[i]*s[j] - r[j]*s[i]) % p for i, j in combinations(range(3), 2)):
            return 1
    return 2 if any(entry % p for row in rows for entry in row) else 3


def decomposition(p):
    if p == 3:
        return [(1, 1), (2, 1)]
    if p == 269:
        return [(3, 1)]
    roots = sum(pow(u, 3, p) == 269 % p for u in range(p))
    return {0: [(1, 3)], 1: [(1, 1), (1, 2)], 3: [(1, 1)]*3}[roots]


def finite_mean(types, p, k):
    return sum(f*sum(Fraction(1, p**(f*j)) for j in range(1, k*e+1))
               for e, f in types)


def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    types_checked = set()
    for p in primes:
        types = decomposition(p)
        observed = sum(kernel_dimension(*a, p) for a in product(range(p), repeat=3))
        assert Fraction(observed, p**3) == finite_mean(types, p, 1)
        types_checked.add(tuple(types))
        print(f"p={p}, {p**3} elements, mean kernel dimension {Fraction(observed, p**3)}")
    assert len(types_checked) == 4  # all three good cycle types and the ramified prime 3
    assert finite_mean(decomposition(3), 3, 1) - Fraction(1, 3) == Fraction(4, 9)
    # At 269, O/(269) = F_269[a]/(a^3) since 3 is a unit.
    # Valuations 0,1,2,3 have strata of sizes p^3-p^2,p^2-p,p-1,1.
    p = 269
    strata = [p**3-p**2, p**2-p, p-1, 1]
    assert sum(strata) == p**3
    observed = Fraction(sum(j*size for j, size in enumerate(strata)), p**3)
    assert observed == finite_mean(decomposition(p), p, 1)
    assert observed - Fraction(1, p) == Fraction(p+1, p**3)
    for p in primes + [269]:
        types = decomposition(p)
        limit = sum(Fraction(f, p**f-1) for _, f in types)
        assert 0 < limit - finite_mean(types, p, 1) <= Fraction(6, p**2)
    for y in [270, 512]:
        window = [p for p in range(y+1, 2*y+1)
                  if all(p % k for k in range(2, isqrt(p)+1))]
        modulus = prod(window)
        h = isqrt(y**3-1) + 1
        for start in [0, 71]:
            direct = prod(gcd(abs(a**3-269), modulus) for a in range(start+1, start+h+1))
            expected = 1
            for p in window:
                roots = [u for u in range(p) if pow(u, 3, p) == 269 % p]
                visits = sum((start+h-u)//p - (start-u)//p for u in roots)
                assert abs(p*visits - h*len(roots)) <= p*len(roots)
                expected *= p**visits
            assert direct == expected
        print(f"y={y}, H={h}: exact gcd products agree on two translated intervals.")
    print("All good splitting types and both ramified primes verified.")


if __name__ == "__main__":
    main()
