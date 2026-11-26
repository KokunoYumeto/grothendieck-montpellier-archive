"""Integer cross-checks for two S3 cubics, rough trace products and quadratic norm fibres."""
from collections import Counter
from functools import cache
from math import fsum, gcd, isclose, isqrt, log


CUBICS = [(-1, -1, -23), (-4, 1, 229)]  # x^3 + ax + b and discriminant
WINDOWS = [512, 2048, 8192]


def least_primes(limit):
    sieve = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if sieve[p] == p:
            for n in range(p * p, limit + 1, p):
                if sieve[n] == n:
                    sieve[n] = p
    return sieve


def split_symbol(discriminant, p):
    if p == 2:
        return 1 if discriminant % 8 == 1 else -1
    value = pow(discriminant % p, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def frobenius_x(a, b, p):
    """Compute X^p mod (p, X^3+aX+b) by binary powering."""
    def multiply(left, right):
        c = [0] * 5
        for i, u in enumerate(left):
            for j, v in enumerate(right):
                c[i+j] += u*v
        for j in (4, 3):
            c[j-2] -= a*c[j]
            c[j-3] -= b*c[j]
        return tuple(x % p for x in c[:3])

    value, base, e = (1, 0, 0), (0, 1, 0), p
    while e:
        if e % 2:
            value = multiply(value, base)
        base = multiply(base, base)
        e //= 2
    return value


def local_data(a, b, discriminant, primes):
    traces, polynomials = {}, {}
    assert -4*a**3 - 27*b*b == discriminant
    for p in primes:
        roots = sum(((x*x + a)*x + b) % p == 0 for x in range(p))
        if discriminant % p == 0:
            # Tame inertia interchanges the double pair. The third root is fixed.
            assert p > 3 and roots == 2
            polynomials[p] = (1, -1)
            continue
        traces[p] = roots - 1
        determinant = split_symbol(discriminant, p)
        if determinant == -1:
            trace = 0
        else:
            trace = 2 if frobenius_x(a, b, p) == (0, 1, 0) else -1
        polynomials[p] = (1, -trace, determinant)
        assert trace == traces[p], (p, a, b)
    return traces, polynomials


def coefficients(factors, local_values):
    result = [0, 1] + [0] * (len(factors) - 2)
    for n in range(2, len(factors)):
        p, rest, e = factors[n], n, 0
        while rest % p == 0:
            rest //= p
            e += 1
        result[n] = result[rest] * local_values(p, e)
    return result


def artin_coefficients(factors, polys):
    @cache
    def at(p, e):
        if e == 0:
            return 1
        return -sum(c*at(p, e-j) for j, c in enumerate(polys[p][1:], 1) if j <= e)
    return coefficients(factors, at)


def squarefree_and_correction(factors, traces, polys, z):
    direct = coefficients(factors, lambda p,e: traces.get(p, 0) if e == 1 and p > z else 0)
    def correction(p, e):
        polynomial = polys[p]
        keep = len(polynomial) == 3 and p > z
        # Multiply the full reciprocal polynomial by 1+tT at good large primes.
        c = polynomial[e] if e < len(polynomial) else 0
        if keep and e <= len(polynomial):
            c -= polynomial[1]*polynomial[e-1]
        return c
    return direct, coefficients(factors, correction)


def progression_check(x, m, residue, direct, artin, support):
    """The complementary class varies with the correction divisor, also for m>x^(1/2)."""
    assert gcd(m, residue) == 1
    exact_mass = 0
    logs = []
    for d, h in support:
        if d > 2*x:
            break
        if gcd(d, m) != 1:
            continue
        target = residue * pow(d, -1, m) % m
        lo = x//d + 1
        for k in range(lo+(target-lo) % m, 2*x//d+1, m):
            weight = h*artin[k]
            if weight:
                exact_mass += weight
                logs.append(weight*log(d*k))
    start = x + 1 + (residue-x-1) % m
    terms = [(n, direct[n]) for n in range(start, 2*x+1, m) if direct[n]]
    assert exact_mass == sum(w for _, w in terms)
    assert isclose(fsum(logs), fsum(w*log(n) for n,w in terms), abs_tol=2e-10)
    return terms


def traces_and_windows():
    limit = 2*max(WINDOWS)
    factors = least_primes(limit)
    primes = [p for p in range(2, limit+1) if factors[p] == p]
    for a, b, discriminant in CUBICS:
        traces, polys = local_data(a, b, discriminant, primes)
        artin = artin_coefficients(factors, polys)
        degrees = Counter(len(factor)-1 for factor in polys.values())
        print(f"D={discriminant}: {len(primes)} primes <= {limit}; local polynomial degrees {dict(sorted(degrees.items()))}")
        rowcount = 0
        for x in WINDOWS:
            for label, z in (("log", int(log(x))), ("log2/3", int(log(x)**2/3)), ("log2", int(log(x)**2))):
                direct, h = squarefree_and_correction(factors[:2*x+1], traces, polys, z)
                support = [(d,c) for d,c in enumerate(h) if c]
                convolution = [0] * (2*x+1)
                for d,c in support:
                    for k in range(1, 2*x//d + 1):
                        convolution[d*k] += c*artin[k]
                assert convolution == direct
                for m in (1, 5, 23, 131, 229):
                    for residue in (r for r in range(m) if gcd(r,m)==1):
                        terms = progression_check(x,m,residue,direct,artin,support)
                        rowcount += 1
                        if (x, label, m, residue) in TABLE:
                            prime_logs = [w*log(n) for n,w in terms if factors[n]==n]
                            composite_logs = [w*log(n) for n,w in terms if factors[n]!=n]
                            print(f"  {x:4d}  {label:6s}  {z:2d}  {m:3d}  {residue:3d}  {len(prime_logs):3d} {len(composite_logs):3d}   {fsum(prime_logs):12.6f} {fsum(composite_logs):12.6f}")
        print(f"  {rowcount} reduced-class interval comparisons")


TABLE = {(512,"log",5,1), (2048,"log2/3",23,1), (2048,"log",131,15), (8192,"log2",5,1)}


def norm_fibres():
    # Positive and indefinite norm forms in integral bases, with alternate primitive forms.
    examples = [(-23, 1,1,6), (-23, 2,1,3), (229, 1,1,-57), (229, 3,1,-19),
                (-4, 1,0,1), (8, 1,0,-2)]
    # An integral change of variables (x,y) -> (x+y,x+2y) has determinant one.
    examples += [(D, a+b+c, 2*a+3*b+4*c, a+2*b+4*c) for D,a,b,c in examples]
    total = 0
    for discriminant, a,b,c in examples:
        assert b*b - 4*a*c == discriminant
        powers = {2:6, 3:3, 5:2, 7:2}
        if discriminant == -23:
            powers[23] = 2
        if discriminant == 229:
            powers[229] = 1
        for p, max_e in powers.items():
            for e in range(1, max_e+1):
                q = p**e
                counts = Counter((a*x*x+b*x*y+c*y*y) % q for x in range(q) for y in range(q))
                for u in range(1,q):
                    if u % p == 0:
                        continue
                    if discriminant % p:
                        expected = (p - split_symbol(discriminant,p)) * p**(e-1)
                    elif p > 2:
                        expected = 2*q if split_symbol(a*u,p)==1 else 0
                    elif discriminant == -4:
                        expected = q if e==1 else (2*q if u%4==1 else 0)
                    else:  # x^2-2y^2, discriminant 8
                        expected = q if e<=2 else (2*q if u%8 in (1,7) else 0)
                    assert counts[u] == expected, (discriminant, (a,b,c),q,u,counts[u],expected)
                    total += 1
    print(f"{total} quadratic-form unit fibres checked")


if __name__ == "__main__":
    traces_and_windows()
    norm_fibres()
