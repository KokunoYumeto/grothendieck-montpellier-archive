"""Exact certificates for THETA3-C16; Python standard library only.

The symbolic polynomial operations below independently verify the displayed
j-polynomial, the finite-field irreducibility certificate, and sample ordinary
reductions.  They are certificates for finite calculations, not substitutes for
the geometric proof in paper_C15_C16.tex.
"""
from fractions import Fraction as F
from math import gcd, isqrt


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c * x for x in a])


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def mod(a, f):
    a = [F(x) for x in trim(a)]
    while len(a) >= len(f):
        d = len(a) - len(f)
        c = a[-1] / f[-1]
        for i, x in enumerate(f):
            a[d + i] -= c * x
        a = trim(a)
    return a


def powmod(a, n, f):
    r = [F(1)]
    while n:
        if n & 1:
            r = mod(mul(r, a), f)
        a = mod(mul(a, a), f)
        n //= 2
    return r


def composemod(a, b, f):
    r = [F(0)]
    for c in reversed(a):
        r = mod(add(mul(r, b), [c]), f)
    return r


def fp(a, p):
    return trim([int(x) % p for x in a])


def fpmod(a, f, p):
    a = fp(a, p)
    while len(a) >= len(f):
        d = len(a) - len(f)
        c = a[-1] * pow(int(f[-1]), -1, p) % p
        for i, x in enumerate(f):
            a[d + i] = (a[d + i] - c * x) % p
        a = trim(a)
    return a


def fppow(a, n, f, p):
    r = [1]
    while n:
        if n & 1:
            r = fpmod(mul(r, a), f, p)
        a = fpmod(mul(a, a), f, p)
        n //= 2
    return r


phi = [-300, -100, -60, 0, 1]
j = scale([-1200, -130, 24, 1], F(-512, 405))
P = [6412351813189632, 37203006717952, -5096079360,
     -40310784, 19683]
assert gcd(*P) == 1

# After shifting x by -r/3, the branch cubic has these coefficients.
short_a = [-60, 0, F(2, 3)]
short_b = [-100, -40, 0, F(20, 27)]
four_a3 = scale(powmod(short_a, 3, phi), 4)
den = mod(add(four_a3, scale(powmod(short_b, 2, phi), 27)), phi)
num = scale(four_a3, 1728)
assert mod(add(mul(j, den), scale(num, -1)), phi) == [0]
assert composemod(P, j, phi) == [0]
print("j(r)=-512(r^3+24r^2-130r-1200)/405 verified modulo phi(r)")
print("P(j(r))=0 verified by rational polynomial division")

# Rabin's irreducibility criterion for a degree-four polynomial over F_11.
p = 11
P0 = [-5, 5, -5, -2, 1]
assert fp(scale(P0, 4), p) == fp(P, p)
r121 = [4, -5, -3, 5]
assert fppow([0, 1], 121, P0, p) == fp(r121, p)
assert fppow([0, 1], 14641, P0, p) == [0, 1]
u = [-3, -5, -5]
v = [2, -5, 4, 1]
q = add(r121, [0, -1])
assert fp(add(mul(u, P0), mul(v, q)), p) == [1]
print("mod11: X^121 remainder and X^14641=X verified")
print("mod11: displayed Bezout identity equals1; P is irreducible over Q")

# Exact point counts illustrate, but are not used to prove, the uniform argument.
for ell in [41, 61, 101, 181, 241]:
    count = 1
    for x in range(ell):
        y2 = (x**3 - 30*x - 25) % ell
        count += 1 if y2 == 0 else (2 if pow(y2, (ell-1)//2, ell) == 1 else 0)
    trace = ell + 1 - count
    assert count % 4 == 0
    assert trace % 4 == 2 and trace % ell != 0
    assert trace * trace <= 4 * ell
    print(f"p={ell}: #E(Fp)={count}, a_p={trace}, ordinary")

print("All finite C16 certificates passed.")
