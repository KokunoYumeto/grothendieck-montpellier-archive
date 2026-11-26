# Computations for the attack-read of LM8_PUSH D.23 (CONFERENCE/ATTACK_D23.md).
# Claude Opus 5.5 at effort max, 25 Nov 2026. Exact arithmetic (fractions, sympy) except the
# L-values, which are rapidly convergent series with an explicit tail bound.
from fractions import Fraction as Fr
import math
import sympy as sp

out = []
def say(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    out.append(s)

# ---------------------------------------------------------------- 1. Cusp expansions (D.22)
say('== 1. Legendre 1/j at the three rational cusps of the Fermat curve (D.22.3)')
t = sp.symbols('t')
lam = sp.symbols('lam')
j = 256*(lam**2 - lam + 1)**3/(lam**2*(1 - lam)**2)
for n in (3, 5, 7, 9, 11):
    for name, lamt in (('X/Z=t, lam=-t^n', -t**n), ('Y/Z=t, lam=1+t^n', 1 + t**n), ('Z/X=t, lam=-t^-n', -t**(-n))):
        inv = sp.simplify(1/j.subs(lam, lamt))
        ser = sp.series(inv, t, 0, 4*n + 1).removeO()
        poly = sp.Poly(sp.expand(ser), t)
        terms = sorted(poly.terms(), key=lambda m: m[0][0])
        (e0,), c0 = terms[0]
        (e1,), c1 = terms[1]
        say(f'  n={n:2d} {name:18s}: leading {c0}*t^{e0}; next term exponent {e1} (= leading + {e1 - e0})')
        assert c0 == sp.Rational(1, 256) and e0 == 2*n and e1 - e0 == n
say('  q = 1/j + 744/j^2 + ..., so q has the same leading term 2^-8 t^(2n) and relative error O(t^n).')

# ---------------------------------------------------------------- 2. Kummer class of the cusp constant
say('== 2. The class kappa(2^-8) mod l (D.22.1, D.23.2): ramified at 2, nonzero unramified at some odd p')
def is_lth_power_mod(a, l, p):
    return pow(a % p, (p - 1)//math.gcd(l, p - 1), p) == 1
for l in (3, 5, 7, 11, 13):
    say(f'  l={l}: v_2(2^-8) = -8 = {(-8) % l} mod l (nonzero, so the class is ramified at 2 and 2^-8 is not a 2l-th power)')
    found = []
    p = 3
    while len(found) < 3:
        if sp.isprime(p) and p != l and (p - 1) % l == 0:
            inv256 = pow(256, -1, p)
            if not is_lth_power_mod(inv256, l, p):
                found.append(p)
        p += 2
    say(f'        first odd primes p = 1 mod l where 2^-8 is not an l-th power mod p: {found}')
say('  So the residual representation of the unit-tangent cusp section is a NON-split extension of Z/l by mu_l')
say('  (up to a quadratic twist): tamely ramified at 2, unramified but non-split at the primes listed.')
say('  This refutes the splitting asserted in Steklov Prop. 5.10 (from Prop. 4.6), not the l-Fermat conclusion.')

# ---------------------------------------------------------------- 3. Weierstrass arithmetic
class Curve:
    def __init__(s, a1, a2, a3, a4, a6):
        s.a = [Fr(x) for x in (a1, a2, a3, a4, a6)]
        a1, a2, a3, a4, a6 = s.a
        b2 = a1*a1 + 4*a2; b4 = 2*a4 + a1*a3; b6 = a3*a3 + 4*a6
        b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
        s.disc = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
        c4 = b2*b2 - 24*b4
        s.j = c4**3/s.disc
    def on(s, P):
        if P is None: return True
        x, y = P; a1, a2, a3, a4, a6 = s.a
        return y*y + a1*x*y + a3*y == x**3 + a2*x*x + a4*x + a6
    def neg(s, P):
        if P is None: return None
        x, y = P; a1, a2, a3, a4, a6 = s.a
        return (x, -y - a1*x - a3)
    def add(s, P, Q):
        if P is None: return Q
        if Q is None: return P
        a1, a2, a3, a4, a6 = s.a
        x1, y1 = P; x2, y2 = Q
        if x1 == x2 and y1 + y2 + a1*x2 + a3 == 0: return None
        if x1 == x2:
            m = (3*x1*x1 + 2*a2*x1 + a4 - a1*y1)/(2*y1 + a1*x1 + a3)
        else:
            m = (y2 - y1)/(x2 - x1)
        x3 = m*m + a1*m - a2 - x1 - x2
        y3 = -(m + a1)*x3 - (y1 - m*x1) - a3
        return (x3, y3)
    def order(s, P, bound=50):
        Q = P
        for k in range(1, bound + 1):
            if Q is None: return k
            Q = s.add(Q, P)
        return None
    def count_mod(s, p):
        # all projective points of the reduction (singular point included): a_p = p + 1 - count
        a1, a2, a3, a4, a6 = [int(x) % p for x in s.a]
        cnt = 1
        for x in range(p):
            r = (x**3 + a2*x*x + a4*x + a6) % p
            for y in range(p):
                if (y*y + a1*x*y + a3*y - r) % p == 0:
                    cnt += 1
        return cnt

say('== 3. LM6 E.10 / FERMAT_SUCCESSOR A.9: a rational point of order 7 (refutes "Y_1(7)(Q) is empty")')
E7 = Curve(-1, -4, -4, 0, 0)   # y^2 - xy - 4y = x^3 - 4x^2
P = (Fr(0), Fr(0))
assert E7.on(P)
say(f'  y^2 - xy - 4y = x^3 - 4x^2: discriminant {E7.disc} = {sp.factorint(int(E7.disc))}, j = {E7.j}')
say(f'  order of (0,0): {E7.order(P)}')
mults = []
Q = P
for k in range(1, 8):
    mults.append(Q); Q = E7.add(Q, P)
say('  multiples 1P..6P: ' + ', '.join(str(tuple(str(c) for c in m)) if m else 'O' for m in mults[:6]))

# ---------------------------------------------------------------- 4. Exponent 3
say('== 4. Exponent 3: F_3 = X_0(27) (D.23, case n = 3)')
X, Y, Z = sp.symbols('X Y Z')
u = -3*Z/(X + Y)
w = (X - Y)/(X + Y)
v = (9*w - 1)/2
expr = sp.together(v**2 + v - (u**3 - 7))
num = sp.factor(sp.numer(expr))
say(f'  v^2 + v - (u^3 - 7) has numerator {num}  (a multiple of X^3 + Y^3 + Z^3)')
assert sp.simplify(sp.numer(expr)/(X**3 + Y**3 + Z**3)).is_polynomial(X, Y, Z) or sp.rem(sp.expand(sp.numer(expr)), X**3 + Y**3 + Z**3, X) == 0
uu, vv = sp.symbols('u v')
xx, yy = 4*uu, 8*vv + 4
say(f'  (x,y) = (4u, 8v+4): y^2 - (x^3 - 432) = {sp.expand(yy**2 - (xx**3 - 432) - 64*(vv**2 + vv - uu**3 + 7))} + 64*(v^2+v-u^3+7)')
E27 = Curve(0, 0, 1, 0, -7)
say(f'  v^2 + v = u^3 - 7 (Cremona 27a1): discriminant {E27.disc} = {sp.factorint(int(E27.disc))}')
for (Xc, Yc, Zc) in ((0, -1, 1), (-1, 0, 1), (1, -1, 0)):
    if Xc + Yc == 0:
        say(f'  cusp ({Xc}:{Yc}:{Zc}) -> origin (X+Y=0)')
    else:
        uc = Fr(-3*Zc, Xc + Yc); wc = Fr(Xc - Yc, Xc + Yc); vc = (9*wc - 1)/2
        assert E27.on((uc, vc))
        say(f'  cusp ({Xc}:{Yc}:{Zc}) -> (u,v) = ({uc},{vc}), order {E27.order((uc, vc))}')
say(f'  #E(F_5) = {E27.count_mod(5)}, #E(F_7) = {E27.count_mod(7)}: torsion order divides gcd = {math.gcd(E27.count_mod(5), E27.count_mod(7))}')

# ---------------------------------------------------------------- 5. Analytic rank zero for the curves Stoll's Cor 8.8 uses here
say('== 5. L(E,1) for the curves behind X_0(27), X_0(20), X_0(28) -> X_0(14), X_0(52) -> X_0(26)')
def an_list(E, M, N):
    ap = {}
    for p in sp.primerange(2, M + 1):
        ap[p] = p + 1 - E.count_mod(p)
    a = [0]*(M + 1); a[1] = 1
    for n in range(2, M + 1):
        f = sp.factorint(n)
        if len(f) == 1:
            (p, k), = f.items()
            if k == 1: a[n] = ap[p]
            elif N % p == 0: a[n] = ap[p]*a[n//p]
            else: a[n] = ap[p]*a[n//p] - p*a[n//(p*p)]
        else:
            p, k = next(iter(f.items()))
            a[n] = a[p**k]*a[n//p**k]
    return a, ap
for name, coeffs, N in (('27a1', (0, 0, 1, 0, -7), 27), ('20a1', (0, 1, 0, 4, 4), 20),
                        ('14a1', (1, 0, 1, 4, -6), 14), ('26a1', (1, 0, 1, -5, -8), 26), ('26b1', (1, -1, 1, -3, 3), 26)):
    E = Curve(*coeffs)
    M = 160
    a, ap = an_list(E, M, N)
    def S(tt):
        c = 2*math.pi*tt/math.sqrt(N)
        return sum(a[n]/n*math.exp(-c*n) for n in range(1, M + 1))
    vals = {}
    for wsign in (+1, -1):
        vals[wsign] = [S(tt) + wsign*S(1/tt) for tt in (1.0, 1.25, 1.6)]
    good = [ws for ws in (1, -1) if max(vals[ws]) - min(vals[ws]) < 1e-12]
    # tail bound: |a_n| <= d(n) sqrt(n) <= n, so tail < sum_{n>M} exp(-c n) with c for tt = 1/1.6
    ctail = 2*math.pi/1.6/math.sqrt(N)
    tail = math.exp(-ctail*(M + 1))/(1 - math.exp(-ctail))
    Lval = 2*S(1.0)   # L(E,1) = (1 + w) sum a_n/n exp(-2 pi n/sqrt N), w = +1
    say(f'  {name}: disc {sp.factorint(int(E.disc))}; root number consistent with t-independence: {good}; '
        f'L(E,1) = 2*sum a_n/n e^(-2 pi n/sqrt N) = {Lval:.12f} (tail < {tail:.1e})')
    assert good == [1] and Lval > 1e-6

# ---------------------------------------------------------------- 6. Genera of X_0(N)
say('== 6. Genus of X_0(N): D.23.3 g(X_0(4l)) = (l-3)/2; Steklov uses X_0(2l)')
def genus_X0(N):
    f = sp.factorint(N)
    mu = N
    for p in f: mu = mu*(p + 1)//p
    nu2 = 0
    if N % 4 != 0:
        nu2 = 1
        for p in f:
            nu2 *= (1 + (sp.legendre_symbol((-1) % p, p) if p > 2 else 0))
    nu3 = 0 if N % 9 == 0 else 1
    if N % 9 != 0:
        for p in f:
            if p == 3: nu3 *= 1
            elif p == 2: nu3 *= 0
            else: nu3 *= (1 + sp.legendre_symbol((-3) % p, p))
    cusps = sum(sp.totient(math.gcd(d, N//d)) for d in sp.divisors(N))
    g = 1 + Fr(mu, 12) - Fr(nu2, 4) - Fr(nu3, 3) - Fr(cusps, 2)
    return int(g), mu, nu2, nu3, cusps
for l in (3, 5, 7, 11, 13, 17, 19, 23):
    g, mu, n2, n3, c = genus_X0(4*l)
    g2 = genus_X0(2*l)[0]
    say(f'  l={l:2d}: X_0({4*l}) index {mu} = 6(l+1)? {mu == 6*(l+1)}, nu2={n2}, nu3={n3}, cusps={c}, genus {g} = (l-3)/2? {g == (l-3)//2};  genus X_0({2*l}) = {g2}')
for N in (14, 20, 26, 27, 28, 52):
    say(f'  genus X_0({N}) = {genus_X0(N)[0]}')

# ---------------------------------------------------------------- 7. Mazur's list
say("== 7. Mazur's Theorem (8): Z/m (m <= 10, 12) or Z/2 x Z/2nu (nu <= 4)")
for l in (5, 7, 11, 13):
    say(f'  Z/2 x Z/{2*l} on the list? {l <= 4};   Z/{l} on the list? {l <= 10}')

open(__file__.replace('.py', '.out'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
