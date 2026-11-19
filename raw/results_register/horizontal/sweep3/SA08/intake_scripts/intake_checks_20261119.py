# Checks for the intake of RESEARCH_SA08 (final of 19 Nov 2026).
# a34c04448e8299803 (Claude Opus 5.5 at effort max), 19 Nov 2026. Pure integer and rational arithmetic, no imports beyond stdlib.
from fractions import Fraction as Fr
from math import comb, factorial


def polymul(a, b, mod=None):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return [c % mod for c in r] if mod else r


def binom_poly(p):
    """coefficients (low to high) of p*C(T,p) = T(T-1)...(T-p+1)/(p-1)!, as Fractions"""
    poly = [Fr(1)]
    for k in range(p):
        poly = polymul(poly, [Fr(-k), Fr(1)])
    return [c / factorial(p - 1) for c in poly]


print("1. A-026 step: p*C(T,p) mod p is a unit multiple of T^p - T")
for p in (3, 5, 7, 11):
    cs = binom_poly(p)
    red = [int(c.numerator * pow(c.denominator, -1, p)) % p for c in cs]
    target = [0] * (p + 1); target[1] = p - 1; target[p] = 1          # T^p - T
    unit = red[p]
    ok = all((red[i] - unit * target[i]) % p == 0 for i in range(p + 1))
    print("   p=%d: leading coeff %d, proportional to T^p - T: %s" % (p, unit, ok))

print("2. A-026 step: C(2p,p) mod p")
for p in (3, 5, 7, 11):
    print("   p=%d: %d" % (p, comb(2 * p, p) % p))


def C(t, n):
    return Fr(comb(t, n)) if t >= 0 else Fr(0)


print("3. A-026 on the evaluation-ideal lattices J1 = {f in Int(Z): f(0)=0}, J2 = {f: f(0)=f(1)=0}, p = 3")
# bottom generators m_1 = T (weight 1), n_2 = C(T,2) (weight 2); a pairing with gr = PD product is beta(x,y) = 2*x*y/T^2 * C(T,2)
# in the identifications; take x = y = C(T,3) in J1: beta = 2*C(T,3)^2 * C(T,2)/T^2 must lie in J2.
def beta_val(t):
    if t == 0:
        return Fr(0)
    return 2 * C(t, 3) ** 2 * C(t, 2) / Fr(t * t)
vals = {t: beta_val(t) for t in range(0, 8)}
print("   values at T=0..7:", {t: str(v) for t, v in vals.items()})
print("   integer-valued:", all(v.denominator == 1 for v in vals.values()), "(not integer at T=3: the pairing leaves J2, as A-026 says)")

print("3b. A-026(1), every pairing vanishes, on the same lattices: b(T,T) = c*C(T,2) forces b(x,y) = c*x*y*C(T,2)/T^2;")
print("    at x = y = C(T,p), T = p the value is c*(p-1)/(2p), integral only if p | c, for every odd p, so c = 0")
for p in (3, 5, 7, 11, 13):
    v = Fr(comb(p, p) ** 2 * comb(p, 2), p * p)
    print("   p=%d: value / c = %s ; denominator %d" % (p, v, v.denominator))

print("4. D-C15 (scan 334): gamma^2(gamma^3(x)) coefficient")
p, q = 2, 3
right = factorial(p * q) // (factorial(p) * factorial(q) ** p)
page = factorial(p * q) // (factorial(p) ** q * factorial(q))
print("   (pq)!/(p!(q!)^p) =", right, "; the page's (pq)!/((p!)^q q!) =", page)
# from the definition gamma_n(y) = y^n/n!, as multiples of gamma_6(x) = x^6/6!
g2g3 = Fr(1, factorial(3) ** 2 * factorial(2)) * factorial(6)    # gamma_2(gamma_3(x)) = (x^3/3!)^2/2!
g3g2 = Fr(1, factorial(2) ** 3 * factorial(3)) * factorial(6)    # gamma_3(gamma_2(x)) = (x^2/2!)^3/3!
print("   from the definition: gamma_2(gamma_3(x)) = %s gamma_6(x); gamma_3(gamma_2(x)) = %s gamma_6(x)" % (g2g3, g3g2))
print("   (the page's 15 is the coefficient of (x^(2))^(3), the order of scans 332-333)")

print("5. B-C01: condition (M) at (i,j)=(1,2) over F2 with A=X, B2=1, others 0")
# (M): C(i+j,i) B_{i+j} = A^{(i)} B_j + A^{(j)} B_i ; here LHS = 3*B3 = 0, RHS = X*B2 + X^{(2)}*B1 = X
print("   LHS = %d*B3 = 0, RHS = X*1 + X^(2)*0 = X : (M) fails by X (times dX)" % comb(3, 1))

print("6. B-C04: (T^(5))^2 = C(10,5) T^(10); C(10,5) mod 3 =", comb(10, 5) % 3, "(so F3{T} is not reduced)")

print("7. B-C08: T -> T + T^(2) is integral: (T^(2))^(b) = (2b)!/(2^b b!) T^(2b)")
print("   all integral for b<=30:", all(factorial(2 * b) % (2 ** b * factorial(b)) == 0 for b in range(31)))

print("8. D-C24/25 (scan 376): dimension over k of k[F]/F^d for d = v_p(i) (page) and v_p(i)+1 (run), p = 3")
def vp(n, p):
    v = 0
    while n % p == 0:
        n //= p; v += 1
    return v
print("   i:", list(range(1, 10)))
print("   page d=v_3(i):   ", [vp(i, 3) for i in range(1, 10)])
print("   run  v_3(i)+1:   ", [vp(i, 3) + 1 for i in range(1, 10)])
print("   (the page gives Ext^{2i} = 0 for every i prime to p; the run gives k there)")

print("9. D-C26: the Witt extension 0 -> Ga -> W_2 -> Ga -> 0 is not one of F_p-module sheaves: p*(x,0) in W_2")
# ghost components w0 = a0, w1 = a0^p + p*a1; p*(x,0) has ghost (p x, p x^p); solve c0 = p x, c1 = (p x^p - (p x)^p)/p
for p in (2, 3, 5):
    c0 = {1: p}                                   # polynomial in x as {exponent: coefficient}
    c1 = {p: (p - p ** p) // p}
    red = ({e: a % p for e, a in c0.items() if a % p}, {e: a % p for e, a in c1.items() if a % p})
    print("   p=%d: p*(x,0) = (%s, %s) over Z; mod p: %s" % (p, c0, c1, red))
print("   so p*(x,0) = (0, x^p) is nonzero over F_p: W_2 is not killed by p, its class lies in Ext^1_Z, not Ext^1_{F_p}")
