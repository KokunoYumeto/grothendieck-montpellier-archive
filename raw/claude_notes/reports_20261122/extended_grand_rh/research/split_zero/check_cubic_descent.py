"""Exact checks for the cubic quotient, its order and its split-zero traces."""
from fractions import Fraction
from itertools import permutations
from math import gcd
from pathlib import Path
import hashlib


def dickson(n, r):
    if n == 0:
        return 2
    previous, current = 2, r
    for _ in range(1, n):
        previous, current = current, r * current + previous
    return current


def fold(z):
    return z - 1/z


def odd_map(n, z):
    sign = 1 if n % 4 == 1 else -1
    return sign * z ** (sign * n)


def determinant(matrix):
    a = [row.copy() for row in matrix]
    result = Fraction(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result *= -1
        result *= a[j][j]
        for i in range(j+1, len(a)):
            scale = Fraction(a[i][j], a[j][j])
            a[i] = [a[i][h] - scale*a[j][h] for h in range(len(a))]
    return result


def basis_index(n, a):
    """Power-basis determinant of y=x-x^{-1} in Q[x]/(x^n-a), n>=3."""
    cols = [[Fraction(1)] + [Fraction(0)] * (n-1)]
    for _ in range(1, n):
        curr = cols[-1]
        following = [Fraction(0)] * n
        for j, c in enumerate(curr):
            following[(j+1) % n] += c*(a if j+1 == n else 1)
            following[(j-1) % n] -= c/(a if j == 0 else 1)
        cols.append(following)
    return determinant(list(map(list, zip(*cols))))


def check():
    a = 269
    odd = list(range(1, 26, 2))
    for z in (Fraction(-3, 2), Fraction(2), Fraction(269), Fraction(5, 7)):
        for n in odd:
            assert fold(odd_map(n,z)) == dickson(n, fold(z))
            assert odd_map(n,z**3) == odd_map(n,z)**3
            assert odd_map(n,-1/z) == -1/odd_map(n,z)
            for m in (1,3,5):
                assert dickson(m,dickson(n,fold(z))) == dickson(m*n,fold(z))
    deck = {n: ((1 if n % 4 == 1 else -1) * n) % 3 for n in (1,3,5,7,9,11)}
    assert deck == {1:1, 3:0, 5:2, 7:2, 9:0, 11:1}
    for n in (3,5,7,9,11):
        for v in (2,5,a):
            val = basis_index(n,v)
            assert val == (1+Fraction(1,v*v))**((n-1)//2)
    assert a*a+1 == 2*97*373
    assert gcd(3*a, 97*373) == 1
    expected = {
        13: ([], []),
        37: ([7,33,34], [22,24,28]),
        97: ([22,81,91], [44,75]),
        373: ([69,104,200], [208,269]),
    }
    for p, pair in expected.items():
        r0 = (a-pow(a,-1,p)) % p
        roots = [j for j in range(p) if (j**3-a) % p == 0]
        quotient = [j for j in range(p) if (j**3+3*j-r0) % p == 0]
        assert (roots,quotient) == pair
        assert sorted({(x-pow(x,-1,p)) % p for x in roots}) == quotient
        if p in (97,373):
            assert (1+a*a) % p == 0 and p % 3 == 1
            assert (-2*a) % p != a % p
            assert all(((y-a)**2*(y+2*a) - (y**3+3*y-r0)) % p == 0 for y in range(p))
        print(f"p={p}: cubic roots {roots}, quotient roots {quotient}")
    for perm in permutations(range(3)):
        g = list(range(3))
        for _ in range(6):
            g = [perm[i] for i in g]
            fixed = sum(i == j for i,j in enumerate(g))
            b = fixed if fixed else None  # None is the absent scalar tau.
            v = -1 if b is None else -1+b
            assert v == fixed-1 and fixed in (0,1,3)
    print("Passed exact odd-map, 15 power-basis determinant and S3 trace checks.")


if __name__ == "__main__":
    check()
    for name in ("CUBIC_DESCENT.md", "check_cubic_descent.py"):
        p = Path(__file__).with_name(name)
        print(hashlib.sha256(p.read_bytes()).hexdigest(), name)

