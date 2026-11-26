"""Lambency-6 pass, check 3: layer 4 (level 4, Z[i], genus two, Sp4(F2) = S6) against the S6 example P205.

(a) The six ramification points of P205's base cover t = (z + 1/z)^2/4 are {0, oo, 1, -1, i, -i}: the octahedron's
    vertices and the Weierstrass points of the Bolza curve C: w^2 = z^5 - z.  Compute Aut(C) (lifts of the Moebius
    stabilizer of the six points), identify it (GL2(3) vs binary octahedral vs S4 x C2), and the preimage of P205's
    deck group D = {z, -z, -1/z, 1/z}.
(b) SL2(Z/4) and PSL2(Z/4): same projective group S4 as GL2(F3)/{+-1}, different double cover?
(c) P205's integral monodromy A1, A2, A3 (Codex's integral basis): invariant alternating forms over F2 and over Z; local
    eigenvalues; the mod-4 squares; the F2[D]-module H/2H against Jac(C)[2] with D acting through the Weierstrass points.
(d) Jac(C) ~ E x E' with E, E' of CM by Z[sqrt(-2)] (point counts).

Run: python -I -B l6_3_layer4.py
"""
import cmath, itertools
from collections import Counter
from fractions import Fraction as Fr

out = []
def say(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

# (a) ------------------------------------------------------------------------------------------------------------------
INF = "inf"
B = [0, INF, 1, -1, 1j, -1j]
def mob(M, z):
    a, b, c, d = M
    if z == INF:
        return INF if abs(c) < 1e-12 else a / c
    den = c * z + d
    if abs(den) < 1e-12: return INF
    return (a * z + b) / den
def same(z, w):
    if z == INF or w == INF: return z == w
    return abs(z - w) < 1e-9
def idx(z):
    for k, w in enumerate(B):
        if same(z, w): return k
    return None
def mobius_from_triples(src, dst):
    # Moebius map sending src[0..2] -> dst[0..2]: compose cross-ratio normalizations
    def to_std(p, q, r):  # map p->0, q->1, r->oo
        # z -> ((z - p)(q - r))/((z - r)(q - p)) with infinity handling
        def M_of(p, q, r):
            if p == INF: return (0, (q - r) if q != INF else 1, 1, -r) if r != INF else None
            if q == INF: return (1, -p, 1, -r) if r != INF else None
            if r == INF: return (1, -p, 0, q - p)
            return ((q - r), -p * (q - r), (q - p), -r * (q - p))
        return M_of(p, q, r)
    S = to_std(*src); T = to_std(*dst)
    if S is None or T is None: return None
    a, b, c, d = T
    Ti = (d, -b, -c, a)
    def mul(X, Y):
        return (X[0] * Y[0] + X[1] * Y[2], X[0] * Y[1] + X[1] * Y[3], X[2] * Y[0] + X[3] * Y[2], X[2] * Y[1] + X[3] * Y[3])
    return mul(Ti, S)
stab = []
for src in [(B[0], B[2], B[1])]:   # 0 -> ?, 1 -> ?, oo -> ? determines the map
    for dst in itertools.permutations(B, 3):
        M = mobius_from_triples(src, dst)
        if M is None: continue
        if any(abs(x) > 1e12 for x in M): continue
        img = [mob(M, z) for z in B]
        ids = [idx(w) for w in img]
        if None in ids or sorted(ids) != list(range(6)): continue
        # normalize to det 1
        det = M[0] * M[3] - M[1] * M[2]
        s = cmath.sqrt(det)
        Mn = tuple(x / s for x in M)
        perm = tuple(ids)
        if perm not in [q for q, _ in stab]:
            stab.append((perm, Mn))
say("(a) Moebius maps preserving {0, oo, 1, -1, i, -i}:", len(stab), "(octahedral rotation group has 24)")
# sextic form F(X, Y) = X^5 Y - X Y^5 (w^2 = z^5 - z with the root at infinity)
def F(X, Y): return X ** 5 * Y - X * Y ** 5
def mu_of(M):
    a, b, c, d = M
    vals = []
    for X, Y in [(0.3 + 0.2j, 1.1 - 0.4j), (1.7 - 0.5j, 0.2 + 0.9j), (-0.6 + 1.3j, 0.8 + 0.1j)]:
        vals.append(F(a * X + b * Y, c * X + d * Y) / F(X, Y))
    assert max(abs(v - vals[0]) for v in vals) < 1e-8, vals
    return vals[0]
# group elements: (M, lam) with lam^2 = mu(M), modulo (M, lam) ~ (tM, t^3 lam); with det M = 1, t = +-1: (-M, -lam).
elems = []
for perm, M in stab:
    mu = mu_of(M)
    l = cmath.sqrt(mu)
    elems.append((M, l)); elems.append((M, -l))
def key(g):
    M, l = g
    # canonical representative under (M, l) ~ (-M, -l): make the first nonzero entry of M have positive real part (or imag)
    for x in M:
        if abs(x) > 1e-9:
            if x.real < -1e-9 or (abs(x.real) < 1e-9 and x.imag < 0):
                M = tuple(-y for y in M); l = -l
            break
    return tuple((round(x.real, 6) + 0.0, round(x.imag, 6) + 0.0) for x in M) + ((round(l.real, 6) + 0.0, round(l.imag, 6) + 0.0),)
G = {}
for g in elems: G[key(g)] = g
say("    lifts to the curve: |Aut(C)| =", len(G))
def gmul(g, h):
    (a, b, c, d), l1 = g; (e_, f, gg, hh), l2 = h
    return ((a * e_ + b * gg, a * f + b * hh, c * e_ + d * gg, c * f + d * hh), l1 * l2)
ident = ((1, 0, 0, 1), 1)
def gorder(g):
    k, x = 1, g
    while key(x) != key(ident):
        x = gmul(x, g); k += 1
        if k > 100: return None
    return k
ords = Counter(gorder(g) for g in G.values())
say("    element orders of Aut(C):", sorted(ords.items()))
say("    13 involutions and 12 elements of order 8 -> GL2(F3) (binary octahedral would have 1 involution, S4 x C2 19):",
    ords[2] == 13 and ords[8] == 12)
# P205's deck involutions z -> -z, -1/z, 1/z and their lifts
deck = {"-z": (1j, 0, 0, -1j), "-1/z": (0, 1, -1, 0), "1/z": (0, 1j, 1j, 0)}
for name, M in deck.items():
    mu = mu_of(M); l = cmath.sqrt(mu)
    o1, o2 = gorder((M, l)), gorder((M, -l))
    sq = gmul((M, l), (M, l))
    say(f"    lifts of {name}: orders {o1}, {o2}; square = hyperelliptic involution:", key(sq) == key(((1, 0, 0, 1), -1)))

# (b) ------------------------------------------------------------------------------------------------------------------
SL = [(a, b, c, d) for a, b, c, d in itertools.product(range(4), repeat=4) if (a * d - b * c) % 4 == 1]
def m4(g, h):
    a, b, c, d = g; e_, f, gg, hh = h
    return ((a * e_ + b * gg) % 4, (a * f + b * hh) % 4, (c * e_ + d * gg) % 4, (c * f + d * hh) % 4)
def o4(g):
    k, x = 1, g
    while x != (1, 0, 0, 1):
        x = m4(x, g); k += 1
    return k
o_sl = Counter(o4(g) for g in SL)
Zsl = [g for g in SL if all(m4(g, h) == m4(h, g) for h in SL)]
ker2 = [g for g in SL if (g[0] % 2, g[1] % 2, g[2] % 2, g[3] % 2) == (1, 0, 0, 1)]
say("(b) |SL2(Z/4)| =", len(SL), "; element orders", sorted(o_sl.items()), "; |centre| =", len(Zsl),
    "; kernel of reduction mod 2 has order", len(ker2), "and is elementary abelian:",
    all(m4(g, g) == (1, 0, 0, 1) for g in ker2))
# PSL2(Z/4) = SL/{+-1}
pcls = {}
for g in SL:
    k = min(g, tuple((-x) % 4 for x in g))
    pcls[k] = g
def po(g):
    k, x = 1, g
    while x not in ((1, 0, 0, 1), (3, 0, 0, 3)):
        x = m4(x, g); k += 1
    return k
say("    PSL2(Z/4): order", len(pcls), "; element orders", sorted(Counter(po(g) for g in pcls.values()).items()),
    "(S4: 1, 9, 8, 6)")
say("    => PSL2(Z/4) = S4 = PGL2(F3) = GL2(F3)/{+-1}, but SL2(Z/4) has", o_sl[2], "involutions (its normal (Z/2)^3 minus 1),")
say("       GL2(F3) has 13 involutions and normal Q8: the two sign extensions of S4 differ.")

# (c) ------------------------------------------------------------------------------------------------------------------
import sympy as sp
A = [sp.Matrix([[1, 0, 0, 0], [0, -1, 2, 0], [0, 0, -1, 0], [0, 1, 0, 1]]),
     sp.Matrix([[-1, 0, 0, 0], [0, 1, 0, 0], [2, 0, -1, 0], [0, 0, 1, 1]]),
     sp.Matrix([[-1, 0, 0, 0], [0, -1, -2, 0], [-2, 0, 1, 0], [2, 1, 1, 1]])]
assert A[0] * A[1] * A[2] == sp.eye(4)
x = sp.symbols("x")
say("(c) P205 local monodromies: characteristic polynomials", [sp.factor((Ai.charpoly(x)).as_expr()) for Ai in A])
say("    A_i^2 - I nilpotent and nonzero (quasi-unipotent of order 2 up to unipotent):",
    [((Ai * Ai - sp.eye(4)) ** 2 == sp.zeros(4), Ai * Ai != sp.eye(4)) for Ai in A])
# invariant alternating forms over Q / Z
w = sp.symbols("w0:6")
Om = sp.Matrix([[0, w[0], w[1], w[2]], [-w[0], 0, w[3], w[4]], [-w[1], -w[3], 0, w[5]], [-w[2], -w[4], -w[5], 0]])
eqs = []
for Ai in A:
    eqs += list(Ai.T * Om * Ai - Om)
sol = sp.solve(eqs, w, dict=True)
say("    alternating forms over Q with A_i^T W A_i = W for all i:", sol)
Sy = sp.symbols("s0:10")
Smat = sp.Matrix([[Sy[0], Sy[1], Sy[2], Sy[3]], [Sy[1], Sy[4], Sy[5], Sy[6]], [Sy[2], Sy[5], Sy[7], Sy[8]], [Sy[3], Sy[6], Sy[8], Sy[9]]])
eqs = []
for Ai in A:
    eqs += list(Ai.T * Smat * Ai - Smat)
sols = sp.solve(eqs, Sy, dict=True)
say("    symmetric forms over Q preserved by all A_i:", sols)
# over F2
A2 = [Ai.applyfunc(lambda t: t % 2) for Ai in A]
def mat2(M): return [[int(M[i, j]) % 2 for j in range(4)] for i in range(4)]
A2l = [mat2(Ai) for Ai in A]
def mmul2(X, Y): return [[sum(X[i][k] * Y[k][j] for k in range(4)) % 2 for j in range(4)] for i in range(4)]
def tr(X): return [[X[j][i] for j in range(4)] for i in range(4)]
inv_forms = []
for bits in itertools.product((0, 1), repeat=6):
    W = [[0] * 4 for _ in range(4)]
    k = 0
    for i in range(4):
        for j in range(i + 1, 4):
            W[i][j] = W[j][i] = bits[k]; k += 1
    if all(mmul2(mmul2(tr(Ai), W), Ai) == W for Ai in A2l):
        M = sp.Matrix(W)
        inv_forms.append((bits, int(M.det()) % 2))
say("    alternating forms over F2 preserved by D (bits w12 w13 w14 w23 w24 w34, det mod 2):", inv_forms)
say("    nondegenerate (symplectic) ones:", [f for f in inv_forms if f[1] == 1])
# mod-2 image and the mod-4 squares
I4 = sp.eye(4)
T = [(Ai - I4).applyfunc(lambda t: t % 2) for Ai in A]
K = [((Ai * Ai - I4) / 2).applyfunc(lambda t: t % 2) for Ai in A]
say("    T_i = A_i - I mod 2 (rank-one, image e4):", [list(Ti.row(3)) for Ti in T], " K_i = (A_i^2 - I)/2 mod 2:",
    [list(Ki.row(3)) for Ki in K])
say("    K_1 != K_2 = K_3:", K[0] != K[1] and K[1] == K[2], "(in Q8 = preimage of V4 in GL2(F3) all three squares are -1)")
# mod-4 image group order
def red4(M): return tuple(int(M[i, j]) % 4 for i in range(4) for j in range(4))
def mul4(X, Y):
    return tuple(sum(X[4 * i + k] * Y[4 * k + j] for k in range(4)) % 4 for i in range(4) for j in range(4))
gens4 = [red4(Ai) for Ai in A]
id4 = red4(I4)
grp = {id4}; fr = [id4]
while fr:
    nx = []
    for g in fr:
        for h in gens4:
            y = mul4(g, h)
            if y not in grp: grp.add(y); nx.append(y)
    fr = nx
def ord4(g):
    k, y = 1, g
    while y != id4:
        y = mul4(y, g); k += 1
    return k
say("    mod-4 monodromy group: order", len(grp), "; element orders", sorted(Counter(ord4(g) for g in grp).items()),
    "; abelian:", all(mul4(g, h) == mul4(h, g) for g in grp for h in grp))
# F2[D]-module comparison with Jac(C)[2]
# H/2H: matrices A2l acting on column vectors
def fixdim(Ms):
    # dimension of common fixed space over F2
    rows = []
    for M in Ms:
        for i in range(4):
            rows.append([(M[i][j] - (1 if i == j else 0)) % 2 for j in range(4)])
    R = sp.Matrix(rows)
    # rank over F2
    Mx = [list(r) for r in rows]
    rank = 0; cols = 4; rr = 0
    Mx = [[int(v) % 2 for v in r] for r in Mx]
    for c in range(cols):
        piv = None
        for r in range(rr, len(Mx)):
            if Mx[r][c]: piv = r; break
        if piv is None: continue
        Mx[rr], Mx[piv] = Mx[piv], Mx[rr]
        for r in range(len(Mx)):
            if r != rr and Mx[r][c]:
                Mx[r] = [(a + b) % 2 for a, b in zip(Mx[r], Mx[rr])]
        rr += 1
    return 4 - rr
say("    H/2H (P205): fixed-space dims of g1, g2, g3:", [fixdim([M]) for M in A2l], "; common fixed:", fixdim(A2l))
# Jac(C)[2]: even subsets of the 6 Weierstrass points modulo complement; D acts through the permutations of B.
perm_of = {}
for name, M in deck.items():
    perm_of[name] = tuple(idx(mob(M, z)) for z in B)
evens = [frozenset(s) for k in (0, 2, 4, 6) for s in itertools.combinations(range(6), k)]
def canon(S):
    comp = frozenset(range(6)) - S
    return min(tuple(sorted(S)), tuple(sorted(comp)))
classes = sorted({canon(S) for S in evens})
say("    Jac(C)[2]: ", len(classes), "classes")
def fixcount(perms):
    return sum(1 for cl in classes if all(canon(frozenset(p[i] for i in cl)) == cl for p in perms))
pl = list(perm_of.values())
import math
say("    Jac(C)[2]: fixed-space dims of the three deck involutions:", [round(math.log2(fixcount([p]))) for p in pl],
    "; common fixed:", round(math.log2(fixcount(pl))))
say("    (an F2[D]-isomorphism would need equal fixed-space dimensions for every element and for D)")

# (d) ------------------------------------------------------------------------------------------------------------------
def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]
def leg(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
def a1_curve(fcoef, p):  # w^2 = f(z), deg f = 5: one point at infinity
    cnt = 1
    for z in range(p):
        v = 0
        for c in fcoef: v = (v * z + c) % p
        cnt += 1 + leg(v, p)
    return p + 1 - cnt
def ap_E(a2, a4, a6, p):  # y^2 = x^3 + a2 x^2 + a4 x + a6
    cnt = 1
    for xx in range(p):
        cnt += 1 + leg(xx ** 3 + a2 * xx * xx + a4 * xx + a6, p)
    return p + 1 - cnt
bolza = [1, 0, 0, 0, -1, 0]   # z^5 - z
cands = {"E: y^2=x^3+4x^2+2x (j=8000)": (4, 2, 0)}
for d in (-1, 2, -2):
    cands[f"E^({d})"] = (4 * d, 2 * d * d, 0)
rows = []
match = Counter()
for p in [q for q in primes_upto(400) if q > 2]:
    a1 = a1_curve(bolza, p)
    aps = {k: ap_E(*v, p) for k, v in cands.items()}
    for k1, k2 in itertools.combinations_with_replacement(list(cands), 2):
        if a1 == aps[k1] + aps[k2]: match[(k1, k2)] += 1
    rows.append((p, a1, aps["E: y^2=x^3+4x^2+2x (j=8000)"]))
np_ = len(rows)
best = [(k, v) for k, v in match.items() if v == np_]
say("(d) Bolza C: w^2 = z^5 - z. Pairs (E1, E2) with a_1(C) = a_p(E1) + a_p(E2) at all", np_, "odd primes < 400:", best)
say("    (CM by Z[sqrt-2]: a_p(E) = 0 for p = 5, 7 mod 8):",
    all(r[2] == 0 for r in rows if r[0] % 8 in (5, 7)))

with open(__file__.replace(".py", "_output.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")
