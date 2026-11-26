"""Lambency-6 pass, check 4: GL(2) x GL(3) -> GL(6) at the lambency-6 CM point and at the two elliptic points.

f_w = eta(6t)^4 (36a1, CM by Q(omega); Mason form of the ES generator rho(289), Frame shape 6^4 on N(A5^4 D4)),
f_i = eta(4t)^2 eta(8t)^2 (32a, CM by Q(i), the j = 1728 curve y^2 = x^3 - x up to isogeny/twist).
Checks (Euler factors at p >= 5):
 (1) Sym^2 f_w = eta(2t)^3 eta(6t)^3 (+) chi_-3 |.|   i.e. a_p(f_w)^2 - p = a_p(eta(2t)^3 eta(6t)^3) + chi_-3(p) p
 (2) Sym^2 f_i = eta(4t)^6 (+) chi_-4 |.|            i.e. a_p(f_i)^2 - p = a_p(eta(4t)^6) + chi_-4(p) p
 (3) Sym^3 f_w = eta(3t)^8 (+) f_w(1)  (the atlas's B4), so f_w x Sym^2 f_w = eta(3t)^8 (+) f_w(1) (+) f_w(1)
 (4) the cross products: f_w x Sym^2 f_i = [4-dim, supported on p = 1 mod 12] (+) f_w x chi_-4 (1), and
     f_i x Sym^2 f_w = [4-dim] (+) f_i x chi_-3 (1); the 4-dim trace vanishes unless p splits in Q(zeta12).
 (5) Frame shapes: 2^3 6^3 and 4^6 have degree 24; is 2^3 6^3 the Frame shape of an automorphism of N(A5^4 D4)?
     (A5 summand: Weyl group S6 x {+-1}; we list the Frame shapes on A5 and on D4 and search sums.)
 (6) the weight-4 level-6 newform h = eta(t)^2 eta(2t)^2 eta(3t)^2 eta(6t)^2 (Mason form of M24 class 1^2 2^2 3^2 6^2):
     not CM (a_p != 0 for primes of both residue classes mod 3 and mod 4), Atkin-Lehner signs from a_2, a_3.
Run: python -I -B l6_4_rankin_selberg.py
"""
from collections import Counter
import itertools

out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

N = 1200
def eta_product(spec, N):
    """q-expansion (integer exponents only) of prod eta(d t)^{r_d}; returns dict exponent->coeff up to N
    together with the leading exponent shift (sum d r_d / 24 must be an integer)."""
    shift = sum(d * r for d, r in spec.items())
    assert shift % 24 == 0, spec
    shift //= 24
    ser = [0] * (N + 1); ser[0] = 1
    for d, r in spec.items():
        # multiply by prod_{n>=1} (1 - q^{dn})^r
        for n in range(1, N // d + 1):
            e = n * d
            if r > 0:
                for _ in range(r):
                    for k in range(N, e - 1, -1):
                        ser[k] -= ser[k - e]
            else:
                for _ in range(-r):
                    for k in range(e, N + 1):
                        ser[k] += ser[k - e]
    coeffs = [0] * (N + 1 + shift)
    for k in range(N + 1):
        if k + shift <= N: coeffs[k + shift] = ser[k]
    return coeffs[:N + 1]

def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]
P = [p for p in primes_upto(N) if p >= 5]
chi3 = lambda p: 1 if p % 3 == 1 else -1
chi4 = lambda p: 1 if p % 4 == 1 else -1

fw = eta_product({6: 4}, N)
fi = eta_product({4: 2, 8: 2}, N)
g3w = eta_product({2: 3, 6: 3}, N)
g3i = eta_product({4: 6}, N)
s3w = eta_product({3: 8}, N)
h = eta_product({1: 2, 2: 2, 3: 2, 6: 2}, N)

def leg(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
def ap_curve(a1c, p):  # y^2 = x^3 + a x + b
    A, Bc = a1c
    return -sum(leg(x ** 3 + A * x + Bc, p) for x in range(p))
bad = Counter()
for p in P:
    if p < 400:
        if fw[p] != ap_curve((0, 1), p): bad["eta(6t)^4 != a_p(y^2 = x^3 + 1)"] += 1
        if fi[p] != ap_curve((-1, 0), p) and fi[p] != -ap_curve((-1, 0), p): bad["eta(4t)^2eta(8t)^2 vs y^2=x^3-x"] += 1
    if fw[p] ** 2 - p != g3w[p] + chi3(p) * p: bad["(1) Sym^2 f_w"] += 1
    if fi[p] ** 2 - p != g3i[p] + chi4(p) * p: bad["(2) Sym^2 f_i"] += 1
    if fw[p] ** 3 - 2 * p * fw[p] != s3w[p] + p * fw[p]: bad["(3) Sym^3 f_w"] += 1
    four = fw[p] * g3i[p]
    if fw[p] * (fi[p] ** 2 - p) != four + chi4(p) * p * fw[p]: bad["(4a)"] += 1
    if four != 0 and p % 12 != 1: bad["(4a) 4-dim part off p = 1 mod 12"] += 1
    four2 = fi[p] * g3w[p]
    if fi[p] * (fw[p] ** 2 - p) != four2 + chi3(p) * p * fi[p]: bad["(4b)"] += 1
    if four2 != 0 and p % 12 != 1: bad["(4b) 4-dim part off p = 1 mod 12"] += 1
say("Euler-factor checks at", len(P), "primes 5 <= p <=", N, "; failures:", dict(bad) if bad else "none")
say("  (1) Sym^2 eta(6t)^4 = eta(2t)^3 eta(6t)^3 (+) chi_-3|.|   (2) Sym^2 eta(4t)^2eta(8t)^2 = eta(4t)^6 (+) chi_-4|.|")
say("  (3) Sym^3 eta(6t)^4 = eta(3t)^8 (+) eta(6t)^4(1)  => f x Sym^2 f = eta(3t)^8 (+) f(1) (+) f(1): 6 = 2 + 2 + 2")
say("  (4) eta(6t)^4 x Sym^2(Q(i)-form) = [4-dim, nonzero only at p = 1 mod 12, i.e. GL1 over Q(zeta12)] (+) eta(6t)^4 x chi_-4;")
say("      and symmetrically with chi_-3: the central-character twist of each CM point is the other point's sign")
say("  first q-coefficients: eta(2t)^3eta(6t)^3:", g3w[:16], " eta(4t)^6:", g3i[:22])

# (5) Frame shapes on N(A5^4 D4) ------------------------------------------------------------------------------------
from sympy import symbols, Poly, factor, prod, cyclotomic_poly, div, cancel, expand
x = symbols("x")
def frame_of_charpoly(cp):
    # write cp as prod (x^d - 1)^{a_d} with integer a_d (Frame shape)
    cp = Poly(cp, x)
    deg = cp.degree()
    a = {}
    rem = cp
    # Moebius inversion on cyclotomic multiplicities
    mult = {}
    for n in range(1, 61):
        c = Poly(cyclotomic_poly(n, x), x)
        k = 0
        while True:
            q, r = div(rem, c)
            if r.is_zero:
                rem = q; k += 1
            else:
                break
        if k: mult[n] = k
    assert rem.degree() == 0
    # (x^d - 1) = prod_{n | d} Phi_n ; solve a_d from mult: mult[n] = sum_{d : n | d} a_d
    ds = sorted({d for d in range(1, 61) if any(d % n == 0 for n in mult)}, reverse=True)
    res = {}
    for n in sorted(set(list(mult.keys()) + [d for d in range(1, 61)]), reverse=True):
        m = mult.get(n, 0) - sum(res.get(d, 0) for d in res if d % n == 0 and d != n)
        if m: res[n] = m
    return {d: v for d, v in sorted(res.items()) if v}
# A5: elements of W(A5) = S6 acting on the sum-zero hyperplane, times +-1 (diagram automorphism with -1 in Aut).
def s6_charpoly(ct, sign):
    # permutation of cycle type ct on 6 points, restricted to sum-zero hyperplane; sign = +1 or -1 (times -I)
    cp = Poly(cancel(prod([(x ** c - 1) for c in ct]) / (x - 1)), x)
    if sign == -1:
        cp = Poly(expand(cp.as_expr().subs(x, -x) * (-1) ** cp.degree()), x)
    return cp
parts6 = [(6,), (5, 1), (4, 2), (4, 1, 1), (3, 3), (3, 2, 1), (3, 1, 1, 1), (2, 2, 2), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1, 1, 1, 1, 1, 1)]
A5frames = set()
for ct in parts6:
    for sg in (1, -1):
        fr = frame_of_charpoly(s6_charpoly(ct, sg))
        A5frames.add(tuple(sorted(fr.items())))
# D4: Aut(D4) = W(D4) x| S3 = W(F4); use W(F4) char polys: build W(F4) by generating reflections in R^4 is heavy;
# instead use the known list of characteristic polynomials of W(F4) elements (classes), computed from generators.
import numpy as np
roots = []
for i in range(4):
    for s in (1, -1):
        v = [0] * 4; v[i] = s; roots.append(tuple(v))
for i, j in itertools.combinations(range(4), 2):
    for s, t in itertools.product((1, -1), repeat=2):
        v = [0] * 4; v[i] = s; v[j] = t; roots.append(tuple(v))
for signs in itertools.product((1, -1), repeat=4):
    roots.append(tuple(s * 0.5 for s in signs))
def refl(r):
    r = np.array(r, dtype=float)
    return np.eye(4) - 2 * np.outer(r, r) / r.dot(r)
gens = [refl(r) for r in [(0, 1, -1, 0), (0, 0, 1, -1), (0, 0, 0, 1), (0.5, -0.5, -0.5, -0.5)]]
seen = {}
frontier = [np.eye(4)]
def k(M): return tuple(np.round(M, 6).flatten())
seen[k(np.eye(4))] = np.eye(4)
while frontier:
    nxt = []
    for M in frontier:
        for g in gens:
            Y = g @ M
            kk = k(Y)
            if kk not in seen:
                seen[kk] = Y; nxt.append(Y)
    frontier = nxt
say("(5) |W(F4)| =", len(seen), "(= |Aut(D4)| = 1152)")
D4frames = set()
for M in seen.values():
    cpc = np.round(np.poly(M)).astype(int)
    cp = sum(int(c) * x ** (4 - i) for i, c in enumerate(cpc))
    D4frames.add(tuple(sorted(frame_of_charpoly(cp).items())))
def add_frames(*frs):
    tot = Counter()
    for fr in frs:
        for d, v in fr: tot[d] += v
    return tuple(sorted((d, v) for d, v in tot.items() if v))
targets = {"2^3 6^3": ((2, 3), (6, 3)), "6^4": ((6, 4),), "4^6": ((4, 6),), "1^2 2^2 3^2 6^2": ((1, 2), (2, 2), (3, 2), (6, 2))}
A5l = sorted(A5frames); D4l = sorted(D4frames)
found = {t: [] for t in targets}
for combo in itertools.combinations_with_replacement(A5l, 4):
    for d4 in D4l:
        tot = add_frames(*combo, d4)
        for name, tg in targets.items():
            if tot == tg and len(found[name]) < 3:
                found[name].append((combo, d4))
for name in targets:
    say("    Frame shape", name, "as (A5 x4 elements, D4 element) of Aut(A5)^4 x Aut(D4) [glue preservation not imposed]:",
        found[name][:2] if found[name] else "none")

# (6) ---------------------------------------------------------------------------------------------------------------
say("(6) h = eta(t)^2eta(2t)^2eta(3t)^2eta(6t)^2: q-expansion", h[:14])
nonzero_classes = Counter((p % 3, p % 4) for p in P if h[p] != 0)
say("    a_p(h) != 0 at primes in residue classes (p mod 3, p mod 4):", sorted(nonzero_classes.items()),
    "-> no CM (a CM form vanishes on a whole class of inert primes)")
say("    a_2 =", h[2], ", a_3 =", h[3], "; for p || 6, weight 4: a_p = -lambda_p p, so W_2 =", -h[2] // 2, ", W_3 =", -h[3] // 3,
    "; root number (-1)^{k/2} W_2 W_3 =", (1) * (-h[2] // 2) * (-h[3] // 3))
with open(__file__.replace(".py", "_output.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")
