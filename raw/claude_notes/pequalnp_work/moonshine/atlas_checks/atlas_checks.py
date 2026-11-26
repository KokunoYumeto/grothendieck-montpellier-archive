"""Checks behind the new combined statements of MOONSHINE_ATLAS.md (X1-X16). Exact integer arithmetic only.
Run: python -I -B atlas_checks.py   (prints PASS/FAIL lines)."""
import itertools

N = 2400  # q-expansion length (in the variable q of each series)

def eta_power_series(d, e, n=N):
    """coefficients of prod_{m>=1} (1 - q^{dm})^e  up to q^n (integers)."""
    c = [0] * (n + 1)
    c[0] = 1
    for m in range(1, n // d + 1):
        step = d * m
        # multiply by (1 - q^step)^e, e may be negative
        if e > 0:
            for _ in range(e):
                for k in range(n, step - 1, -1):
                    c[k] -= c[k - step]
        else:
            for _ in range(-e):
                for k in range(step, n + 1):
                    c[k] += c[k - step]
    return c

def chi_m3(n):
    r = n % 3
    return 0 if r == 0 else (1 if r == 1 else -1)

def chi_m4(n):
    r = n % 4
    return 0 if r % 2 == 0 else (1 if r == 1 else -1)

out = []
def rep(name, ok, info=''):
    out.append(('PASS' if ok else 'FAIL') + ' ' + name + (' :: ' + info if info else ''))

# ---------- X1/X2: lambency-6 theta and shadow components as Dirichlet unary theta series ----------
# Work in the variable Q = q^{1/24}: exponent of q^{k^2/24} is k^2 in Q.
M = 6000  # max Q-exponent
def S6r(r):
    s = [0] * (M + 1)
    for k in range(-200, 201):
        if k % 12 == r % 12 and k * k <= M:
            s[k * k] += k
    return s
S = {r: S6r(r) for r in range(12)}
def unary(coef, scale=1):
    s = [0] * (M + 1)
    for n in range(1, 200):
        e = scale * n * n
        if e <= M:
            s[e] += coef(n) * n
    return s
# S_{6,1} - S_{6,5} = sum_{(n,6)=1} chi_-3(n) n Q^{n^2}
lhs = [a - b for a, b in zip(S[1], S[5])]
rhs = unary(lambda n: chi_m3(n) if n % 2 else 0)
rep('X1a S61-S65 = sum_{(n,6)=1} chi_-3(n) n q^{n^2/24}', lhs == rhs)
lhs = [a + b for a, b in zip(S[1], S[5])]
rhs = unary(lambda n: chi_m4(n) if n % 3 else 0)
rep('X1b S61+S65 = sum_{(n,6)=1} chi_-4(n) n q^{n^2/24}', lhs == rhs)
# S_{6,3} = sum_n chi_-4(n) (3n) q^{9n^2/24}
rhs = [0] * (M + 1)
for n in range(1, 200):
    if 9 * n * n <= M:
        rhs[9 * n * n] += chi_m4(n) * 3 * n
rep('X1c S63 = 3 sum chi_-4(n) n q^{3n^2/8}', S[3] == rhs)
# S_{6,2} = 2 sum_{(m,6)=1} chi_-3(m) m q^{m^2/6}  (Q-exponent 4 m^2)
rhs = [0] * (M + 1)
for m in range(1, 200):
    if 4 * m * m <= M and m % 2:
        rhs[4 * m * m] += 2 * chi_m3(m) * m
rep('X1d S62 = 2 sum_{(m,6)=1} chi_-3(m) m q^{m^2/6}', S[2] == rhs)
# S_{6,4} = 4 sum chi_-3(m) m q^{2m^2/3}  (Q-exponent 16 m^2)
rhs = [0] * (M + 1)
for m in range(1, 200):
    if 16 * m * m <= M:
        rhs[16 * m * m] += 4 * chi_m3(m) * m
rep('X1e S64 = 4 sum chi_-3(m) m q^{2m^2/3}', S[4] == rhs)
rep('X1f S60 = S66 = 0', all(v == 0 for v in S[0]) and all(v == 0 for v in S[6]))
# eta(tau) = sum chi12(n) q^{n^2/24}; eta^3 = sum chi_-4(n) n q^{n^2/8}
def chi12(n):
    r = n % 12
    return {1: 1, 11: 1, 5: -1, 7: -1}.get(r, 0)
e1 = eta_power_series(1, 1, M // 24)
lhs = [0] * (M + 1)
for k, v in enumerate(e1):
    if 24 * k + 1 <= M:
        lhs[24 * k + 1] += v
rhs = [0] * (M + 1)
for n in range(1, 400):
    if n * n <= M:
        rhs[n * n] += chi12(n)
rep('X2a eta = sum chi12(n) q^{n^2/24}', lhs == rhs)
e3 = eta_power_series(1, 3, M // 24)
lhs = [0] * (M + 1)
for k, v in enumerate(e3):
    if 24 * k + 3 <= M:
        lhs[24 * k + 3] += v
rhs = [0] * (M + 1)
for n in range(1, 200):
    if 3 * n * n <= M:
        rhs[3 * n * n] += chi_m4(n) * n
rep('X2b eta^3 = sum chi_-4(n) n q^{n^2/8}', lhs == rhs)
# X4: the lambency-6 shadow S^X = (5I + J) S_6, J: r -> 5r.  Components 1, 5 are not single characters.
SX = {r: [5 * a + b for a, b in zip(S[r], S[(5 * r) % 12])] for r in range(12)}
c = {}
for n in range(1, 60):
    if n * n <= M:
        c[n] = SX[1][n * n] // n if n * n <= M else None
# coefficient function of S^X_1 on n coprime to 6 (as sum c(n) n q^{n^2/24})
cf = {n: c[n] for n in c if n % 2 and n % 3}
mult_fail = [(a, b) for a in cf for b in cf if a * b in cf and cf[a] * cf[b] != cf[a * b] * cf[1]]
rep('X4 S^X_1 coefficient function is not multiplicative (not one Dirichlet character)', len(mult_fail) > 0,
    'c(1),c(5),c(7),c(11) = %s; e.g. pair %s' % ([cf.get(i) for i in (1, 5, 7, 11)], mult_fail[:1]))
d13 = [a - b for a, b in zip(SX[1], SX[5])]
rep('X4b S^X_1 - S^X_5 = 4 (S61 - S65)', d13 == [4 * (a - b) for a, b in zip(S[1], S[5])])
s13 = [a + b for a, b in zip(SX[1], SX[5])]
rep('X4c S^X_1 + S^X_5 = 6 (S61 + S65)', s13 == [6 * (a + b) for a, b in zip(S[1], S[5])])

# ---------- X5/X6: Epstein zeta functions (as coefficient identities) ----------
def theta_count(gram, nmax):
    # count vectors of (x,x)/2 = n by brute force in a box
    dim = len(gram)
    cnt = [0] * (nmax + 1)
    R = 4
    for v in itertools.product(range(-R, R + 1), repeat=dim):
        q2 = sum(gram[i][j] * v[i] * v[j] for i in range(dim) for j in range(dim))
        if q2 % 2 == 0 and q2 // 2 <= nmax:
            cnt[q2 // 2] += 1
    return cnt
D4 = [[2, -1, 0, 0], [-1, 2, -1, -1], [0, -1, 2, 0], [0, -1, 0, 2]]
cD4 = theta_count(D4, 6)
sig_odd = lambda n: sum(d for d in range(1, n + 1) if n % d == 0 and d % 2)
rep('X5 r_D4(n) = 24 sigma_odd(n), n = 1..6 (Epstein = 24(1-2^{1-s}) zeta(s) zeta(s-1))',
    all(cD4[n] == 24 * sig_odd(n) for n in range(1, 7)), str(cD4[1:7]))
A2 = [[2, -1], [-1, 2]]
cA2 = [0] * 31
for x in range(-12, 13):
    for y in range(-12, 13):
        n = x * x - x * y + y * y
        if n <= 30:
            cA2[n] += 1
rep('X6 r_A2(n) = 6 sum_{d|n} chi_-3(d), n = 1..30 (Epstein = 6 zeta(s) L(s, chi_-3))',
    all(cA2[n] == 6 * sum(chi_m3(d) for d in range(1, n + 1) if n % d == 0) for n in range(1, 31)))
cZi = [0] * 31
for x in range(-12, 13):
    for y in range(-12, 13):
        n = x * x + y * y
        if n <= 30:
            cZi[n] += 1
rep('X6b r_Z[i](n) = 4 sum_{d|n} chi_-4(d) (Epstein = 4 zeta(s) L(s, chi_-4))',
    all(cZi[n] == 4 * sum(chi_m4(d) for d in range(1, n + 1) if n % d == 0) for n in range(1, 31)))

# ---------- X15/X16: the Mason forms of the ES residue group S840 ----------
LIM = 2400
def eta_prod_coeffs(d, e, lim):
    """q-expansion of eta(d tau)^e = q^{de/24} prod (1-q^{dm})^e, returned as dict exponent->coef
    in the variable q, assuming de/24 is an integer."""
    shift = d * e // 24
    base = eta_power_series(d, e, lim)
    return {k + shift: v for k, v in enumerate(base) if v and k + shift <= lim}
f64 = eta_prod_coeffs(6, 4, LIM)    # 6^4, weight 2, level 36
f38 = eta_prod_coeffs(3, 8, LIM)    # 3^8, weight 4, level 9
f212 = eta_prod_coeffs(2, 12, LIM)  # 2^12, weight 6, level 4
f124 = eta_prod_coeffs(1, 24, LIM)  # 1^24 = Delta
primes = [p for p in range(5, 400) if all(p % k for k in range(2, int(p ** 0.5) + 1))]
a = lambda f, n: f.get(n, 0)
rep('X16a 6^4 and 3^8 vanish at p = 2 mod 3 (CM by Q(omega))',
    all(a(f64, p) == 0 and a(f38, p) == 0 for p in primes if p % 3 == 2))
rep('X16b 2^12 and 1^24 are not CM by Q(omega) or Q(i) (a_p != 0 for some p = 2 mod 3 and some p = 3 mod 4)',
    any(a(f212, p) for p in primes if p % 3 == 2) and any(a(f212, p) for p in primes if p % 4 == 3)
    and any(a(f124, p) for p in primes if p % 3 == 2), 'a_5(2^12)=%d a_7(2^12)=%d' % (a(f212, 5), a(f212, 7)))
ok = all(a(f38, p) == a(f64, p) ** 3 - 3 * p * a(f64, p) for p in primes if p % 3 == 1 and p < 400)
rep('X15 a_p(eta(3t)^8) = a_p(eta(6t)^4)^3 - 3p a_p(eta(6t)^4) for p = 1 mod 3, p < 400', ok)
ok = all(a(f64, p) ** 3 - 2 * p * a(f64, p) == a(f38, p) + p * a(f64, p) for p in primes if p < 400)
rep('X15b Sym^3 trace a^3 - 2pa = a_p(3^8) + p a_p(6^4) for all 5 <= p < 400 (L(Sym^3 f64,s) = L(f38,s) L(f64,s-1))', ok)
# multiplicativity (Hecke eigenforms) on a few coprime products
def multok(f, pairs):
    return all(a(f, m * n) == a(f, m) * a(f, n) for m, n in pairs)
pairs = [(5, 7), (7, 11), (5, 13), (11, 13), (7, 17)]
rep('X16c the four Mason forms are multiplicative on coprime pairs', all(multok(f, pairs) for f in (f64, f38, f212, f124)))
# S840 frame shapes: rho(289) Coxeter of A5 on four A5, trivial on D4
import cmath
def frame_of_power(k):
    # eigenvalues zeta6^{jk}, j = 1..5, on each A5 (four copies), and 1 (x4) on D4: return char poly as multiset of orders
    from fractions import Fraction
    orders = []
    for _ in range(4):
        for j in range(1, 6):
            t = (j * k) % 6
            from math import gcd
            orders.append(6 // gcd(t, 6) if t else 1)
    orders += [1] * 4
    return sorted(orders)
res = {}
for r, k in ((1, 0), (289, 1), (361, 2), (169, 3), (121, 4), (529, 5)):
    res[r] = frame_of_power(k)
def shape(orders):
    # Frame shape from eigenvalue orders: the multiset of eigenvalue orders determines prod (x^d - 1)^{a_d}
    from collections import Counter
    c = Counter(orders)  # number of eigenvalues of each order m
    # number of primitive m-th roots = phi(m); a_d via Moebius-type peeling from largest d
    from math import gcd
    def phi(m):
        return sum(1 for i in range(1, m + 1) if gcd(i, m) == 1)
    a_d = {}
    rem = dict(c)
    for d in sorted(rem, reverse=True):
        pass
    # direct: char poly = prod over eigenvalue orders m of Phi_m^{c[m]/phi(m)}; x^d - 1 = prod_{m|d} Phi_m
    e = {m: c[m] // phi(m) for m in c}
    divs = sorted(set(list(e.keys()) + [1, 2, 3, 6]), reverse=True)
    for d in divs:
        k = e.get(d, 0)
        if k:
            a_d[d] = a_d.get(d, 0) + k
            for m in [m for m in range(1, d + 1) if d % m == 0]:
                e[m] = e.get(m, 0) - k
    return {d: v for d, v in a_d.items() if v}
shapes = {r: shape(o) for r, o in res.items()}
rep('X16d S840 Frame shapes on N(x)Q: 1 -> 1^24, 289,529 -> 6^4, 361,121 -> 3^8, 169 -> 2^12',
    shapes[1] == {1: 24} and shapes[289] == {6: 4} and shapes[529] == {6: 4} and shapes[361] == {3: 8}
    and shapes[121] == {3: 8} and shapes[169] == {2: 12}, str(shapes))
# 289 powers mod 840
pw = [pow(289, k, 840) for k in range(6)]
rep('X16e 289^k mod 840 = 1, 289, 361, 169, 121, 529', pw == [1, 289, 361, 169, 121, 529], str(pw))
# cubic character mod 7 and quartic character mod 5 on S840 (generator 3 mod 7, 2 mod 5)
def ind(g, x, m):
    for k in range(m):
        if pow(g, k, m) == x % m:
            return k
cub = {r: ind(3, r, 7) % 3 for r in pw}
qua = {r: ind(2, r, 5) % 4 for r in pw}
rep('X16f CM by Q(omega) exactly where the cubic character mod 7 is nontrivial',
    all((cub[r] != 0) == (shapes[r] in ({6: 4}, {3: 8})) for r in pw), 'cubic index %s quartic index %s' % (cub, qua))

# ---------- X9: L-meta-1303 / 907 lines = tetracode coordinates minus one ----------
F3 = range(3)
words = {(a_, b_): ((a_ + b_) % 3, (a_ + 2 * b_) % 3, a_, b_) for a_ in F3 for b_ in F3}
tetra_lines = {(i, v): frozenset(p for p, w in words.items() if w[i] == v) for i in range(4) for v in F3}
fleet_lines = {(m, c_): frozenset((x, y) for x in F3 for y in F3 if y == (m * x + c_) % 3) for m in F3 for c_ in F3}
nonvert = set(L for (i, v), L in tetra_lines.items() if i != 2)
rep('X9 the 9 lines y = mx + c of L-meta-1303/907 are the tetracode lines of coordinates 1, 2, 4 (point (x,y) = (a,b))',
    set(fleet_lines.values()) == nonvert)
# symmetry: affine maps of F3^2 preserving the set of 9 non-vertical lines
cnt = 0
for A in itertools.product(F3, repeat=4):
    det = (A[0] * A[3] - A[1] * A[2]) % 3
    if det == 0:
        continue
    for t in itertools.product(F3, repeat=2):
        f = lambda p: ((A[0] * p[0] + A[1] * p[1] + t[0]) % 3, (A[2] * p[0] + A[3] * p[1] + t[1]) % 3)
        img = set(frozenset(f(p) for p in L) for L in fleet_lines.values())
        if img == set(fleet_lines.values()):
            cnt += 1
rep('X9b affine symmetries of the Pappus/1303 instance: order 108 = 9 x |Borel of GL2(F3)|', cnt == 108, str(cnt))

# ---------- X10: Fano encoding = octonion lines = Singer {0,1,3} mod 7 with multipliers 1,2,4 ----------
D = {0, 1, 3}
mults = [m for m in range(1, 7) if any({(m * d + s) % 7 for d in D} == {(d + 0) % 7 for d in D} or
                                        {(m * d) % 7 for d in D} == {(d + s) % 7 for d in D} for s in range(7))]
rep('X10 multipliers of the Fano difference set {0,1,3} mod 7 are 1, 2, 4', sorted(mults) == [1, 2, 4], str(mults))
D13 = {0, 1, 3, 9}
mults13 = [m for m in range(1, 13) if any({(m * d) % 13 for d in D13} == {(d + s) % 13 for d in D13} for s in range(13))]
rep('X10b multipliers of {0,1,3,9} mod 13 are 1, 3, 9 (Singer normalizer 13 x 3 = 39)', sorted(mults13) == [1, 3, 9], str(mults13))

# ---------- X13: IP gadget on 4 bits = hyperbolic form on F2^4: 10 zeros (even thetas), 6 ones (odd thetas) ----------
z = sum(1 for v in itertools.product((0, 1), repeat=4) if (v[0] * v[2] + v[1] * v[3]) % 2 == 0)
rep('X13 IP_4 has 10 zeros and 6 ones (= 10 even, 6 odd genus-2 theta characteristics)', z == 10, str(z))
for m in (2, 4, 12):
    sing = (2 ** m - 1) * (2 ** (m - 1) + 1)
    nons = 2 ** (2 * m - 1) - 2 ** (m - 1)
    out.append('INFO X13b O+(%d,2): nonzero singular %d, nonsingular %d' % (2 * m, sing, nons))

# ---------- X11: circulant norm = ES Jordan norm factorization (integer check on a box) ----------
okc = True
for x, y, w in itertools.product(range(-4, 5), repeat=3):
    lhs = x ** 3 + y ** 3 + w ** 3 - 3 * x * y * w
    rhs = (x + y + w) * (x * x + y * y + w * w - x * y - y * w - w * x)
    okc &= (lhs == rhs)
rep('X11 x^3+y^3+z^3-3xyz = (x+y+z)(x^2+y^2+z^2-xy-yz-zx): ES Jordan norm is a linear form times an Eisenstein norm', okc)

print('\n'.join(out))
