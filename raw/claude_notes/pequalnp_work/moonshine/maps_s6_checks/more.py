import sys; sys.path.insert(0, '.')
from fractions import Fraction as Fr
from qs import mul, inv, powr, eprod, etaq
import mpmath as mp
N = 20
T = etaq({1: 5, 3: 1, 2: -1, 6: -5}, N)        # q^-1 * T
def lser(a, lead): return {i+lead: x for i, x in enumerate(a)}
def lmul(a, b, top=10):
    c = {}
    for i, x in a.items():
        for k, y in b.items():
            if i+k <= top: c[i+k] = c.get(i+k, 0) + x*y
    return c
def linv(a, top=10):
    # a = c q^m (1 + ...) -> inverse
    m = min(k for k, v in a.items() if v != 0)
    s = [a.get(m+i, 0) for i in range(top - m + 12)]
    si = inv(s, len(s))
    return {i - m: x for i, x in enumerate(si) if i - m <= top}
def ladd(*ts):
    c = {}
    for t in ts:
        for k, v in t.items(): c[k] = c.get(k, 0) + v
    return c
def show(a, top=6): return [(k, a.get(k, 0)) for k in range(-1, top+1)]
Tl = lser(T, -1)
one = {0: 1}
def sc(c, a): return {k: c*v for k, v in a.items()}
# W3: T -> -9(T+8)/(T+9) ; W2: T -> -8(T+9)/(T+8) ; W6: T -> 72/T
W3 = sc(-9, lmul(ladd(Tl, sc(8, one)), linv(ladd(Tl, sc(9, one)))))
W2 = sc(-8, lmul(ladd(Tl, sc(9, one)), linv(ladd(Tl, sc(8, one)))))
W6 = sc(72, linv(Tl))
print("T6 + W3 T6        :", show(ladd(Tl, W3)))
print("T(T+8)/(T+9)      :", show(lmul(lmul(Tl, ladd(Tl, sc(8, one))), linv(ladd(Tl, sc(9, one))))))
print("T6 + W2 T6        :", show(ladd(Tl, W2)))
print("T6 + W6 T6 (=J6-5):", show(ladd(Tl, W6)))
print("T+W2T+W3T+W6T     :", show(ladd(Tl, W2, W3, W6)))
# Theta_M = E4^3 - 648 Delta in a, b
from qs import E, shift, subs
import sympy as sp
M = 14
E4 = E(4, M); D = shift(powr(eprod(1, M), 24, M), 1, M)
ThM = [x - 648*y for x, y in zip(powr(E4, 3, M), D)]
a = [0]*M
for m in range(-20, 21):
    for n in range(-20, 21):
        v = m*m + m*n + n*n
        if v < M: a[v] += 1
b = shift(mul(powr(eprod(3, M), 9, M), powr(eprod(1, M), -3, M), M), 1, M)
mons = [mul(powr(a, 12 - 3*i, M), powr(b, i, M), M) for i in range(5)]
cs = sp.symbols('c0:5')
sol = sp.solve([sum(cs[i]*sp.Rational(mons[i][k]) for i in range(5)) - ThM[k] for k in range(M)], cs, dict=True)
print("Theta_{A2^12 Niemeier} = E4^3-648Delta in a,b:", sol)
# Leech
ThL = [x - 720*y for x, y in zip(powr(E4, 3, M), D)]
sol = sp.solve([sum(cs[i]*sp.Rational(mons[i][k]) for i in range(5)) - ThL[k] for k in range(M)], cs, dict=True)
print("Theta_Leech in a,b:", sol)
# S6-026: 2 e^{-pi/6} prod (1+e^{-2 pi n})^2 vs 2^{1/4}
mp.mp.dps = 30
val = 2*mp.e**(-mp.pi/6)*mp.nprod(lambda n: (1 + mp.e**(-2*mp.pi*n))**2, [1, mp.inf])
print("S6-026 value:", val, " 2^(1/4) =", mp.mpf(2)**0.25)
# S6-019: j(tau)/(tau-rho)^3 -> -512 i pi^3 E6(rho)
rho = mp.e**(1j*mp.pi/3)
def E6(t):
    q = mp.e**(2j*mp.pi*t)
    return 1 - 504*mp.nsum(lambda n: n**5*q**n/(1 - q**n), [1, mp.inf])
def jf(t):
    q = mp.e**(2j*mp.pi*t)
    E4v = 1 + 240*mp.nsum(lambda n: n**3*q**n/(1 - q**n), [1, mp.inf])
    return E4v**3/(q*mp.qp(q)**24)
eps = mp.mpf('1e-6')*(1+1j)
print("j(rho+e)/e^3 =", mp.nstr(jf(rho+eps)/eps**3, 10), "  -512 i pi^3 E6(rho) =", mp.nstr(-512j*mp.pi**3*E6(rho), 10), " E6(rho) =", mp.nstr(E6(rho), 12))
# S_840 -> mu2 x mu3 via quartic char mod 5 (gen 2) and cubic char mod 7 (gen 3)
S = [1, 121, 169, 289, 361, 529]
def dlog(x, g, p):
    k, y = 0, 1
    while y != x % p: y = y*g % p; k += 1
    return k
print("S840 images (k5 mod 4, k7 mod 3):", [(dlog(s % 5, 2, 5) % 4, dlog(s % 7, 3, 7) % 3) for s in S])
print("squares:", [n*n % 840 for n in (1, 11, 13, 17, 19, 23)])
print("1201 % 840 =", 1201 % 840, " 8803369 % 840 =", 8803369 % 840, " 2521 % 840 =", 2521 % 840, " 3361 % 840 =", 3361 % 840)
