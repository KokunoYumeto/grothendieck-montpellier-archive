"""Exact arithmetic for primitive shell marks and simultaneous Frobenius examples."""
from fractions import Fraction
from math import gcd, isqrt


def factors(n):
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            yield p, e
        p += 1 if p == 2 else 2
    if n > 1:
        yield n, 1


def prime(n):
    return n >= 2 and all(n % j for j in range(2, isqrt(n) + 1))


def divisors(n):
    entries = [1]
    for p, e in factors(n):
        entries = [d * p**j for d in entries for j in range(e + 1)]
    return entries


def marks(p, R, L, D):
    a = (p + R) // 4
    S = p*a
    uv = [d for d in divisors(a) if d <= D and gcd(d, L) == 1]
    triples = set()
    for u in uv:
        for v in uv:
            if u % R != 1 or v % R != R-1 or gcd(u,v) != 1:
                continue
            assert (p + R) % (u*v) == 0
            y, z = (S//v)*((u+v)//R), (S//u)*((u+v)//R)
            assert Fraction(1,a) + Fraction(1,y) + Fraction(1,z) == Fraction(4,p)
            triple = tuple(sorted((a,y,z)))
            assert triple not in triples
            triples.add(triple)
    return len(triples)


def mul(f, g, p):
    """Multiply modulo the monic 3-division polynomial over F_p."""
    h = [0] * 7
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            h[i+j] += a*b
    c = 4 * pow(3,-1,p) % p
    for k in (6,5,4):
        # x^4 = 4*x^2 + 3*x + 4/3
        h[k-4] += c*h[k]
        h[k-3] += 3*h[k]
        h[k-2] += 4*h[k]
    return tuple(v % p for v in h[:4])


def poly_pow(f, k, p):
    ans = (1,0,0,0)
    while k:
        if k & 1:
            ans = mul(ans,f,p)
        f = mul(f,f,p)
        k //= 2
    return ans


def all_three_torsion_rational(p):
    x = (0,1,0,0)
    return (poly_pow(x,p,p) == x and
            poly_pow((-3,-8,0,4),(p-1)//2,p) == (1,0,0,0))


def find_comparison():
    seen = {}
    # p=1 mod 840. Require complete splitting in E[3] and in Q(i, fourth-root(3)).
    for p in range(841, 9_000_000, 840):
        if not prime(p) or pow(3, (p-1)//4, p) != 1:
            continue
        if not all_three_torsion_rational(p):
            continue
        assert pow(269, (p-1)//3, p) == 1
        a = (p+3)//4
        witness = next((q for q,e in factors(a) if q % 3 == 2), None)
        sign = witness is not None
        if sign not in seen:
            seen[sign] = (p,a,list(factors(a)),witness)
        if len(seen) == 2:
            return seen
    return seen


def check_class_difference():
    """Check the difference of Dirichlet coefficients at every n, on units."""
    for a in range(1, 5001):
        if a % 3 == 0:
            continue
        ds = divisors(a)
        hist = {1: 0, 2: 0}
        for d in ds:
            hist[d % 3] += 1
            hist[4*a*d % 3] += 1
        pairing = 2 * hist[1] * hist[2]
        sign = 1 if a % 3 == 1 else -1
        character_sum = sum(1 if d % 3 == 1 else -1 for d in ds)
        assert sign * pairing == 2 * (sign * len(ds)**2 - character_sum**2)


def check_local_euler_product():
    """Use integer coefficients of cyclic group rings, without approximate roots."""
    for order in range(1, 15):
        for exponent in range(13):
            direct, expanded = [0]*order, [0]*order
            for i in range(exponent+1):
                for j in range(exponent+1):
                    direct[(i-j) % order] += 1
            # Expand (1-z²)/((1-z)²(1-tz)(1-t^{-1}z)).
            for shift, sign in ((0, 1), (2, -1)):
                degree = exponent - shift
                for i in range(degree+1):
                    for j in range(degree-i+1):
                        expanded[(i-j) % order] += sign * (degree-i-j+1)
            assert direct == expanded


if __name__ == "__main__":
    for R,L in [(3,12),(7,84),(11,132)]:
        dmax, xmax = 50, 7000
        primes = [p for p in range(max(R,4)+1, xmax) if p % 4 == 1 and prime(p)]
        via_shell = sum(marks(p,R,L,dmax) for p in primes)
        via_modulus = sum(sum((p+R) % (u*v) == 0 for p in primes)
                          for u in range(1,dmax+1) for v in range(1,dmax+1)
                          if u % R == 1 and v % R == R-1
                          and gcd(u,v) == 1 and gcd(u*v,L) == 1)
        assert via_shell == via_modulus
        print(f"R={R}, L={L}, primitive marks={via_shell}")
    examples = find_comparison()
    print(examples)
    assert examples == {True: (55441,13861,[(83,1),(167,1)],83),
                        False: (176401,44101,[(44101,1)],None)}
    for occupied, counts in ((True, (4,4)), (False, (4,0))):
        p, a, _, _ = examples[occupied]
        assert all_three_torsion_rational(p)
        assert pow(3,(p-1)//4,p) == pow(269,(p-1)//3,p) == 1
        ds = divisors(p*a)
        assert tuple(sum(d % 3 == g for d in ds) for g in (1, 2)) == counts
    assert sum(Fraction(1,d) for d in (13861,259242116,21517095628)) == Fraction(4,55441)
    check_class_difference()
    check_local_euler_product()
    print("Exact residue-class coefficient differences through 5000 and all 182 cyclic local Euler identities passed.")
