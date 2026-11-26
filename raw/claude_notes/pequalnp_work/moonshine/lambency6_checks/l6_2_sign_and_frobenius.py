"""Lambency-6 pass, check 2: the sign in Alpoge's Gauss-sum mechanism and the Frobenius tower of the lambency-6
twined shadow.

(a) Normalized quadratic Gauss sums eps_c = g(c)/sqrt(c) (Jacobi symbol mod odd squarefree c > 0): eps_c^2 = chi_-4(c)
    and the reciprocity cocycle eps_{cc'}/(eps_c eps_c') = (-1)^{x x'}, x = (c-1)/2 mod 2; for k factors the defect is
    (-1)^{e_2(x_1..x_k)} (the complete-graph quadratic form over F2).
(b) The lambency-6 theta Gauss sum sum_{r mod 12} e(r^2/24) = sqrt(12) e(1/8) factors as (2-part)(3-part).
(c) For p = 1 mod 6: g(chi2) g(chi3) = J(chi2, chi3) g(chi2 chi3), and a_p(y^2 = x^3 + 1) = -2 Re J(chi2, chi3):
    the multiplicativity defect between the order-2 (sign) and order-3 (phase) Gauss sums is the Frobenius of 36a1, the
    curve of eta(6 tau)^4.
(d) On E: y^2 = x^3 - 3x + 1 (j = 2304, mod-3 image GL2(F3)): the twined-shadow class functions at Frob_p read off the
    quotient tower of the umbral group: s = chi_-3(p), c = (#cube roots of Disc(E) mod p) - 1, a = #roots of the
    3-division quartic, b = n_+ - n_-; and b = chi_2'(Frob) c, a = chi_2'(Frob)^2 - s + 1.

Run: python -I -B l6_2_sign_and_frobenius.py
"""
import cmath, math
from itertools import product, combinations
from collections import Counter

out = []
def say(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

def e(x): return cmath.exp(2j * math.pi * x)

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]

def jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

def squarefree(n):
    return all(n % (p * p) for p in range(2, int(n ** 0.5) + 1))

# (a) -----------------------------------------------------------------------------------------------------------------
def eps(c):
    g = sum(jacobi(x, c) * e(x / c) for x in range(c))
    return g / math.sqrt(c)
odd_sf = [c for c in range(3, 400, 2) if squarefree(c)]
bad = 0
for c in odd_sf:
    ec = eps(c)
    want = 1 if c % 4 == 1 else 1j
    if abs(ec - want) > 1e-7: bad += 1
    chi4 = 1 if c % 4 == 1 else -1
    if abs(ec * ec - chi4) > 1e-7: bad += 1
say("(a) eps_c = 1 (c=1 mod 4), i (c=3 mod 4) and eps_c^2 = chi_-4(c) for", len(odd_sf), "odd squarefree c < 400; failures:", bad)
bad = 0; npairs = 0
for c, d in combinations([c for c in odd_sf if c < 120], 2):
    if math.gcd(c, d) != 1 or not squarefree(c * d): continue
    npairs += 1
    x, y = (c - 1) // 2 % 2, (d - 1) // 2 % 2
    lhs = eps(c * d) / (eps(c) * eps(d))
    if abs(lhs - (-1) ** (x * y)) > 1e-7: bad += 1
    # equivalently the Gauss sums: g(cd) = (c/d)(d/c) g(c) g(d)
say("    eps_{cd} = eps_c eps_d (-1)^{x(c)x(d)} on", npairs, "coprime pairs; failures:", bad)
bad = 0; ntrip = 0
pr = [p for p in primes_upto(60) if p > 2]
for k in (3, 4, 5):
    for cs in combinations(pr, k):
        n = math.prod(cs)
        if n > 20000: continue
        ntrip += 1
        xs = [(c - 1) // 2 % 2 for c in cs]
        e2 = sum(xs[i] * xs[j] for i in range(k) for j in range(i + 1, k)) % 2
        want = (1 if n % 4 == 1 else 1j)
        prod_eps = math.prod([(1 if c % 4 == 1 else 1j) for c in cs])
        if abs(want - prod_eps * (-1) ** e2) > 1e-9: bad += 1
say("    k-fold products (k = 3, 4, 5): eps_{c1..ck} = prod eps_ci (-1)^{e2(x)}, checked on", ntrip, "products; failures:", bad)
say("    (-1)^{e2(x)} depends only on w = |x| mod 4: e2 = C(w,2) mod 2 =", [math.comb(w, 2) % 2 for w in range(8)])

# (b) -----------------------------------------------------------------------------------------------------------------
G12 = sum(e(r * r / 24) for r in range(12))
G2 = sum(e(3 * r * r / 8) for r in range(4))
G3 = sum(e(-r * r / 3) for r in range(3))
say("(b) sum_{r mod 12} e(r^2/24) =", round(G12.real, 9), "+", round(G12.imag, 9), "i ; sqrt12 e(1/8) =",
    complex(round((math.sqrt(12) * e(1 / 8)).real, 9), round((math.sqrt(12) * e(1 / 8)).imag, 9)))
say("    2-part sum_{r mod 4} e(3r^2/8) =", complex(round(G2.real, 9), round(G2.imag, 9)), "= 2 e(3/8);",
    "3-part sum_{r mod 3} e(-r^2/3) =", complex(round(G3.real, 9), round(G3.imag, 9)), "= -i sqrt3;  product matches:",
    abs(G2 * G3 - G12) < 1e-9)
say("    (1/24 = 3/8 - 1/3; the eighth root e(1/8) = e(3/8) e(-1/4): the local Weil indices at 2 and 3)")

# (c) -----------------------------------------------------------------------------------------------------------------
def prim_root(p):
    fac = [q for q in primes_upto(p) if (p - 1) % q == 0]
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac): return g
def char_table(p, order):
    g = prim_root(p)
    lg = {}
    x = 1
    for k in range(p - 1):
        lg[x] = k; x = x * g % p
    def chi(t, m=1):  # character of exact order dividing `order`, chi(g) = e(m/order)
        t %= p
        if t == 0: return 0
        return e(m * lg[t] / order)
    return chi
def gauss(chi, p): return sum(chi(x) * e(x / p) for x in range(1, p))
def ap_curve(A, B, p):  # y^2 = x^3 + A x + B
    cnt = 1
    for x in range(p):
        r = (x ** 3 + A * x + B) % p
        cnt += 1 + (0 if r == 0 else (1 if pow(r, (p - 1) // 2, p) == 1 else -1))
    return p + 1 - cnt
bad = 0; rows = []
for p in [p for p in primes_upto(400) if p % 6 == 1]:
    chi6 = char_table(p, 6)
    chi2 = lambda t: chi6(t, 3)
    chi3 = lambda t: chi6(t, 2)
    chi5 = lambda t: chi6(t, 5)
    J = sum(chi2(x) * chi3(1 - x) for x in range(2, p))
    lhs = gauss(chi2, p) * gauss(chi3, p)
    rhs = J * gauss(chi5, p)
    if abs(lhs - rhs) > 1e-6: bad += 1
    ap = ap_curve(0, 1, p)
    if abs(ap + 2 * J.real) > 1e-6: bad += 1
    if abs(abs(J) ** 2 - p) > 1e-6: bad += 1
    rows.append((p, ap, complex(round(J.real, 6), round(J.imag, 6))))
say("(c) p = 1 mod 6, p < 400:", len(rows), "primes; g(chi2)g(chi3) = J(chi2,chi3) g(chi2 chi3), |J|^2 = p and",
    "a_p(y^2 = x^3 + 1) = -2 Re J(chi2, chi3): failures", bad)
say("    first rows (p, a_p(36a1), J):", rows[:5])

# (d) -----------------------------------------------------------------------------------------------------------------
# E: y^2 = x^3 - 3x + 1. Disc = -16(4(-3)^3 + 27(1)^2) = 1296 = 6^4. 3-division quartic h = x^4 - 6x^2 + 4x - 3.
A, B = -3, 1
disc = -16 * (4 * A ** 3 + 27 * B ** 2)
say("(d) E: y^2 = x^3 - 3x + 1, discriminant", disc, "= 6^4:", disc == 6 ** 4)
def roots_mod(coeffs, p):  # coeffs high->low
    rs = []
    for x in range(p):
        v = 0
        for c in coeffs: v = (v * x + c) % p
        if v == 0: rs.append(x)
    return rs
def qr(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
GL23 = [(a, b, c, d) for a, b, c, d in product(range(3), repeat=4) if (a * d - b * c) % 3]
def mat_mul(g, h):
    a, b, c, d = g; e_, f, gg, hh = h
    return ((a * e_ + b * gg) % 3, (a * f + b * hh) % 3, (c * e_ + d * gg) % 3, (c * f + d * hh) % 3)
def mo(g):
    k, x = 1, g
    while x != (1, 0, 0, 1):
        x = mat_mul(x, g); k += 1
    return k
lines = [(1, 0), (0, 1), (1, 1), (1, 2)]
def nl(v):
    x, y = v[0] % 3, v[1] % 3
    inv = (1 if x == 1 else 2) if x else (1 if y == 1 else 2)
    return ((x * inv) % 3, (y * inv) % 3)
def act(g, v):
    a, b, c, d = g
    return ((a * v[0] + b * v[1]) % 3, (c * v[0] + d * v[1]) % 3)
def class_stats(g):
    a = b = 0
    for l in lines:
        im = act(g, l)
        if nl(im) == l:
            a += 1; b += 1 if im == l else -1
    return a, b
def chi2p(g):  # faithful 2-dim character (values 2, -2, 0, -1, 1, +-i sqrt2), chosen by order and trace
    o = mo(g); tr = (g[0] + g[3]) % 3
    if g == (1, 0, 0, 1): return 2
    if g == (2, 0, 0, 2): return -2
    if o == 3: return -1
    if o == 6: return 1
    if o == 8: return cmath.sqrt(-2) if tr == 1 else -cmath.sqrt(-2)
    return 0
# For each p, the Frobenius class is pinned (up to conjugacy) by (trace, det, number of fixed lines, signed count);
# we find all GL2(3) elements with trace = a_p mod 3, det = p mod 3, #fixed lines = a(p), signed = b(p).
bad = Counter(); n = 0
tower_rows = []
for p in primes_upto(3000):
    if p < 5: continue
    n += 1
    ap = ap_curve(A, B, p)
    hr = roots_mod([1, 0, -6, 4, -3], p)
    a_p = len(hr)
    nplus = sum(1 for x in hr if qr(x ** 3 + A * x + B, p) == 1)
    nminus = sum(1 for x in hr if qr(x ** 3 + A * x + B, p) == -1)
    b_p = nplus - nminus
    cube = sum(1 for x in range(1, p) if (x ** 3 - disc) % p == 0)
    c_p = cube - 1
    s_p = 1 if p % 3 == 1 else -1
    # matching GL2(3) elements
    cands = [g for g in GL23 if (g[0] + g[3]) % 3 == ap % 3 and (g[0] * g[3] - g[1] * g[2]) % 3 == p % 3
             and class_stats(g) == (a_p, b_p)]
    if not cands: bad["no GL2(3) element matches (trace, det, fixed lines, signed lines)"] += 1; continue
    vals = {(round(complex(chi2p(g)).real, 6), round(complex(chi2p(g)).imag, 6)) for g in cands}
    if len(vals) != 1: bad["2' value not determined"] += 1
    t2 = complex(chi2p(cands[0]))
    # the S3 character c from the matrix: pair partitions fixed - 1 must equal cube roots of Disc - 1
    # (computed via a = fixed lines and the S4 -> S3 map: here directly compare with the group-side c)
    def c_of(g):
        perm = {l: nl(act(g, l)) for l in lines}
        P = [frozenset({frozenset({(1, 0), (0, 1)}), frozenset({(1, 1), (1, 2)})}),
             frozenset({frozenset({(1, 0), (1, 1)}), frozenset({(0, 1), (1, 2)})}),
             frozenset({frozenset({(1, 0), (1, 2)}), frozenset({(0, 1), (1, 1)})})]
        return sum(1 for Q in P if frozenset(frozenset(perm[x] for x in blk) for blk in Q) == Q) - 1
    cg = {c_of(g) for g in cands}
    if cg != {c_p}: bad["c(Frob) != #cube roots of Disc - 1"] += 1
    if (1 if (cands[0][0] * cands[0][3] - cands[0][1] * cands[0][2]) % 3 == 1 else -1) != s_p: bad["s != chi_-3"] += 1
    if abs(b_p - t2 * c_p) > 1e-9: bad["b != chi_2'(Frob) c"] += 1
    if abs(a_p - (t2 * t2 - s_p + 1)) > 1e-9: bad["a != chi_2'^2 - s + 1"] += 1
    if 1 + a_p + b_p != 1 + 2 * nplus: bad["#E[3] formula"] += 1
    tower_rows.append((p, ap, a_p, b_p, c_p, s_p, t2))
say("    primes 5 <= p < 3000:", n, "; failures:", dict(bad) if bad else "none")
say("    s(p) = chi_-3(p) = det Frob;  c(p) = #{cube roots of Disc(E) = 6^4 in F_p} - 1 (the S3 / cubic-Kummer layer,")
say("    Q(omega, cbrt 6));  a(p) = #roots of the 3-division quartic (S4 layer);  b(p) = n_+ - n_- (faithful layer).")
say("    b(p) = chi_2'(Frob_p) c(p) and a(p) = chi_2'(Frob_p)^2 - chi_-3(p) + 1 hold at every prime.")
dist = Counter((r[2], r[3], r[4], r[5]) for r in tower_rows)
say("    distribution of (a, b, c, s) over the", len(tower_rows), "primes:", sorted(dist.items(), key=lambda kv: -kv[1])[:10])
say("    first rows (p, a_p(E), a, b, c, s, chi_2'):", [(r[0], r[1], r[2], r[3], r[4], r[5], complex(round(complex(r[6]).real, 3), round(complex(r[6]).imag, 3))) for r in tower_rows[:8]])

with open(__file__.replace(".py", "_output.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")
