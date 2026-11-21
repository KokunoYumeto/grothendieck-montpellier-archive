"""Independent checks of the small algebraic inputs of A1-run B.23.

This supplements, rather than replaces, its whole Bezout certificates.
Requires python-flint 0.9.0. All arithmetic is exact.
"""
from functools import lru_cache
from flint import nmod_poly, fmpz_mod_poly_ctx, fq_default_ctx, fq_default_poly_ctx


def remainder(a, b):
    while a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def gcd(a, b):
    while b:
        a, b = b, remainder(a, b)
    return a


def square_mod(a, m):
    sq = sum(((a >> i) & 1) << (2*i) for i in range(a.bit_length()))
    return remainder(sq, m)


exponents = (38, 14, 10, 9, 8, 5, 2, 1, 0)
modulus = sum(1 << i for i in exponents)
x = 2
powers = {0: x}
for i in range(1, 39):
    powers[i] = square_mod(powers[i-1], modulus)
assert powers[38] == x
assert gcd(powers[2] ^ x, modulus) == 1
assert gcd(powers[19] ^ x, modulus) == 1
print("degree-38 modulus: irreducible by Rabin's criterion")

k = fq_default_ctx(modulus=fmpz_mod_poly_ctx(2)([int(i in exponents) for i in range(39)]),
                   var="t", fq_type="FQ_NMOD")
t = k.gen()
R = fq_default_poly_ctx(k)
u = R.gen()
d = t**3 + 1
a = u*u + t*t*u + t
b = t*u*u + u + t*t
assert a**3 + b**3 == d*(u**3+1)**2 + d*d*(u**3+1)
assert (b+t*a)/d == u
assert d != 0 and t*t/d**3 != 0
print("elliptic-map identity, birational joint coordinate, quintic coefficient: PASS")

X = nmod_poly([0, 1], 2)
one = nmod_poly([1], 2)


def reduced(n, d):
    g = n.gcd(d)
    return n//g, d//g


@lru_cache(None)
def x_multiplication(n):
    if n == 1:
        return X, one
    if n % 2 == 0:
        a, b = x_multiplication(n//2)
        return a**4, b**4
    j = n//2
    a, b = x_multiplication(j)
    c, d = x_multiplication(j+1)
    h, kden = reduced(a*d + b*c, b*d)
    return reduced(X*h*h + kden*kden, h*h)


@lru_cache(None)
def psi(n):
    if n in (1, 2, 4):
        return one
    if n == 3:
        return X**4+X
    if n % 2 == 0:
        return psi(n//2)**4
    j = n//2
    return psi(j+2)*psi(j)**3 + psi(j-1)*psi(j+1)**3


for n in (191, 229):
    a, b = x_multiplication(n)
    p = psi(n)
    assert a.gcd(b) == one
    assert b == p*p
    assert p.degree() == (n*n-1)//2
    print(f"n={n}: numerator degree {a.degree()}, denominator degree {b.degree()}, "
          f"division degree {p.degree()}, denominator=psi_n^2: PASS")
