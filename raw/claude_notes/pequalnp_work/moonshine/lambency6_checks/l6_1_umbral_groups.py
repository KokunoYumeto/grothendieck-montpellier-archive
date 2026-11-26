"""Lambency-6 pass, check 1: the umbral groups at Coxeter number 6 (and E6^4) from the glue codes.

Builds the glue codes of the Niemeier lattices N(A5^4 D4), N(D4^6), N(E6^4) from explicit generators, verifies that
each is an isotropic code of the right order whose nonzero words have minimal norm >= 4 (so the root system is exactly
X), computes G^X = the stabilizer of the glue code in Out(X) (permutations of isomorphic components and their diagram
automorphisms), and identifies the groups: order, centre, involutions, element orders, normal subgroup of order 3 and
how the odd part acts on it.

Run: python -I -B l6_1_umbral_groups.py
"""
from fractions import Fraction as Fr
from itertools import permutations, product
from collections import Counter

out = []
def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)

# ---------------------------------------------------------------------------------------------------------------------
# Generic finite-group helpers on hashable elements with an explicit multiplication.
def closure_order(gens, mul, ident):
    seen = {ident}
    frontier = [ident]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = mul(x, g)
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        frontier = nxt
    return seen

def element_order(g, mul, ident):
    k, x = 1, g
    while x != ident:
        x = mul(x, g)
        k += 1
    return k

def centre(G, mul):
    return [z for z in G if all(mul(z, g) == mul(g, z) for g in G)]

def derived_subgroup(G, mul, inv, ident):
    comms = {mul(mul(inv(a), inv(b)), mul(a, b)) for a in G for b in G}
    return closure_order(list(comms), mul, ident)

# ---------------------------------------------------------------------------------------------------------------------
# 1. N(A5^4 D4).  Components 0..3: A5 with discriminant Z/6 (class i has minimal norm i(6-i)/6, norm = 5 i^2/6 mod 2,
#    bilinear form 5ij/6 mod 1); component 4: D4 with discriminant (Z/2)^2 = {0,1,2,3} (XOR), every nonzero class of
#    minimal norm 1, bilinear form 1/2 between distinct nonzero classes.
def a5_min(i): return Fr(i * (6 - i), 6)
def a5_bil(i, j): return Fr(5 * i * j, 6) % 1
def d4_min(x): return 0 if x == 0 else 1
def d4_bil(x, y): return Fr(1, 2) if (x and y and x != y) else Fr(0)

def add_a5d4(u, v):
    return tuple((u[k] + v[k]) % 6 for k in range(4)) + (u[4] ^ v[4],)

def span(gens, add, zero):
    S = {zero}
    frontier = [zero]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = add(x, g)
                if y not in S:
                    S.add(y); nxt.append(y)
        frontier = nxt
    return S

# Glue generators: the tetracode in the 3-parts {0,2,4} of the four A5 classes, and a binary part in {0,3}^4 x D4.
tetra_gens = [(2, 0, 2, 4, 0), (2, 4, 0, 2, 0), (2, 2, 4, 0, 0)]   # [2(024)0]: 2 then cyclic shifts of (0,2,4)
bin_gens = [(3, 3, 0, 0, 1), (3, 0, 3, 0, 2), (3, 0, 0, 3, 3)]     # [33001], [30302], [30033]
C = span(tetra_gens + bin_gens, add_a5d4, (0, 0, 0, 0, 0))
say("A5^4 D4: glue code order", len(C), "(expected 72 = sqrt(6^4 * 4))")
ok_even = all((sum(Fr(5 * w[k] ** 2, 6) for k in range(4)) + d4_min(w[4])) % 2 == 0 for w in C)
ok_int = all((sum(a5_bil(u[k], v[k]) for k in range(4)) + d4_bil(u[4], v[4])) % 1 == 0 for u in C for v in C)
minnorm = min(sum(a5_min(w[k]) for k in range(4)) + d4_min(w[4]) for w in C if w != (0, 0, 0, 0, 0))
say("  isotropic (even norms):", ok_even, " integral bilinear:", ok_int, " min norm of nonzero glue:", minnorm)
assert len(C) == 72 and ok_even and ok_int and minnorm >= 4

# The ternary part is the tetracode on F3^4 (classes 2,4 -> 1,2 mod 3 via i -> i/2 mod 3).
tern = {tuple((w[k] // 2) % 3 if w[k] % 2 == 0 else None for k in range(4)) for w in C if all(w[k] % 2 == 0 for k in range(4)) and w[4] == 0}
tern = {t for t in tern if None not in t}
say("  ternary part:", len(tern), "words; weights", sorted(Counter(sum(1 for x in t if x) for t in tern).items()))

# Out(A5^4 D4) = ({+-1}^4 x| S4) x S3; element = (perm p of 4, signs e (tuple of +-1), sigma perm of {1,2,3}).
S3perms = list(permutations((1, 2, 3)))
def act_a5d4(g, w):
    p, e, sg = g
    res = [0] * 4
    for k in range(4):
        res[p[k]] = (e[k] * w[k]) % 6
    d = w[4] if w[4] == 0 else sg[w[4] - 1]
    return tuple(res) + (d,)

def mul_a5d4(g, h):  # (g*h)(w) = g(h(w))
    pg, eg, sg = g
    ph, eh, sh = h
    p = tuple(pg[ph[k]] for k in range(4))
    e = tuple(eh[k] * eg[ph[k]] for k in range(4))
    s = tuple(sg[sh[i] - 1] for i in range(3))
    return (p, e, s)

ident_a = ((0, 1, 2, 3), (1, 1, 1, 1), (1, 2, 3))
allg = [(p, e, s) for p in permutations(range(4)) for e in product((1, -1), repeat=4) for s in S3perms]
say("  |Out(A5^4 D4)| =", len(allg), "= 48^2" if len(allg) == 48 ** 2 else "")
# sanity: action is a homomorphism
import random
random.seed(1)
for _ in range(200):
    g, h = random.choice(allg), random.choice(allg)
    w = random.choice(list(C))
    assert act_a5d4(mul_a5d4(g, h), w) == act_a5d4(g, act_a5d4(h, w))
GA = [g for g in allg if all(act_a5d4(g, w) in C for w in C)]
say("  G^X = Stab(glue) has order", len(GA))

def inv_generic(G, mul, ident):
    d = {}
    for g in G:
        for h in G:
            if mul(g, h) == ident:
                d[g] = h; break
    return d

def describe(G, mul, ident, name):
    orders = Counter(element_order(g, mul, ident) for g in G)
    Z = centre(G, mul)
    invd = inv_generic(G, mul, ident)
    D = derived_subgroup(G, mul, lambda x: invd[x], ident)
    say(f"  {name}: order {len(G)}, element orders {sorted(orders.items())}, |centre| = {len(Z)}, |derived| = {len(D)}")
    return orders, Z, D, invd

ordA, ZA, DA, invA = describe(GA, mul_a5d4, ident_a, "G^X(A5^4D4)")
# GL2(3): order 48, centre 2, 13 involutions, elements of order 8, derived subgroup SL2(3) of order 24.
isGL23 = len(GA) == 48 and len(ZA) == 2 and ordA[2] == 13 and ordA[8] == 12 and len(DA) == 24
say("  identified as GL2(F3) (48, |Z|=2, 13 involutions, 12 elements of order 8, derived of order 24):", isGL23)
zA = [z for z in ZA if z != ident_a][0]
say("  its central involution:", zA, "-> negates all four A5 classes, fixes D4 (the 'flip' of every A5)")
# binary-octahedral would have 1 involution, S4 x C2 would have 19.

# The centre acts on the tetracode part by -1 and trivially on the binary part {0,3}:
say("  centre on ternary words: x -> -x;  on binary words (classes 0,3): trivial:",
    all(act_a5d4(zA, w) == tuple((-w[k]) % 6 for k in range(4)) + (w[4],) for w in C))

# ---------------------------------------------------------------------------------------------------------------------
# 2. N(E6^4): E6 discriminant Z/3 (class 1, 2 of minimal norm 4/3), Out(E6) = +-1 (diagram flip = -1 on Z/3).
tetracode = span([(1, 1, 1, 0), (0, 1, 2, 1)], lambda u, v: tuple((u[k] + v[k]) % 3 for k in range(4)), (0, 0, 0, 0))
say("E6^4: tetracode order", len(tetracode), "weights", sorted(Counter(sum(1 for x in t if x) for t in tetracode).items()))
ok = all(sum(Fr(4, 3) * (1 if x else 0) for x in t) % 2 == 0 for t in tetracode)
ok2 = all(sum(Fr(4 * x * y, 3) for x, y in zip(u, v)) % 1 == 0 for u in tetracode for v in tetracode)  # E6 bilinear 4ij/3 mod 1
say("  even:", ok, " integral:", ok2, " min norm:", min(sum(Fr(4, 3) for x in t if x) for t in tetracode if any(t)))
def act_e6(g, w):
    p, e = g
    res = [0] * 4
    for k in range(4):
        res[p[k]] = (e[k] * w[k]) % 3
    return tuple(res)
def mul_e6(g, h):
    pg, eg = g; ph, eh = h
    return (tuple(pg[ph[k]] for k in range(4)), tuple(eh[k] * eg[ph[k]] for k in range(4)))
ident_e = ((0, 1, 2, 3), (1, 1, 1, 1))
GE = [(p, e) for p in permutations(range(4)) for e in product((1, -1), repeat=4)
      if all(act_e6((p, e), w) in tetracode for w in tetracode)]
ordE, ZE, DE, invE = describe(GE, mul_e6, ident_e, "G^X(E6^4)")
say("  identified as GL2(F3):", len(GE) == 48 and len(ZE) == 2 and ordE[2] == 13 and ordE[8] == 12 and len(DE) == 24)

# ---------------------------------------------------------------------------------------------------------------------
# 3. N(D4^6): glue = hexacode over F4 = D4^*/D4 (0, 1=s, 2=w=v, 3=wbar=c; addition XOR).
F4mul = {}
for x in range(4):
    for y in range(4):
        # represent 1 = (1,0), w = (0,1), wbar = (1,1); w^2 = wbar, w*wbar = 1
        if x == 0 or y == 0:
            F4mul[x, y] = 0
        else:
            lg = {1: 0, 2: 1, 3: 2}
            ex = {0: 1, 1: 2, 2: 3}
            F4mul[x, y] = ex[(lg[x] + lg[y]) % 3]
def fm(x, y): return F4mul[x, y]
def fa(x, y): return x ^ y
W, WB = 2, 3
hexacode = set()
for a, b, c in product(range(4), repeat=3):
    phi = lambda x: fa(fa(fm(a, fm(x, x)), fm(b, x)), c)
    hexacode.add((a, b, c, phi(1), phi(W), phi(WB)))
say("D4^6: hexacode order", len(hexacode), "weights", sorted(Counter(sum(1 for x in t if x) for t in hexacode).items()))
ok_even = all(sum(d4_min(x) for x in t) % 2 == 0 for t in hexacode)
ok_int = all(sum(d4_bil(x, y) for x, y in zip(u, v)) % 1 == 0 for u in hexacode for v in hexacode)
say("  even:", ok_even, " integral:", ok_int, " min norm:", min(sum(d4_min(x) for x in t) for t in hexacode if any(t)))
assert ok_even and ok_int

# F2-basis of the hexacode and the information set {0,1,2}
basis = []
for a, b, c in [(1, 0, 0), (2, 0, 0), (0, 1, 0), (0, 2, 0), (0, 0, 1), (0, 0, 2)]:
    phi = lambda x: fa(fa(fm(a, fm(x, x)), fm(b, x)), c)
    basis.append((a, b, c, phi(1), phi(W), phi(WB)))
by_head = {t[:3]: t for t in hexacode}
sig = list(permutations((1, 2, 3)))   # sigma as images of 1,2,3; 0 fixed
def sapp(s, x): return 0 if x == 0 else s[x - 1]
GD = []
for pi in permutations(range(6)):
    pinv = [0] * 6
    for i in range(6): pinv[pi[i]] = i
    for s0, s1, s2 in product(sig, repeat=3):
        heads = [(sapp(s0, w[pinv[0]]), sapp(s1, w[pinv[1]]), sapp(s2, w[pinv[2]])) for w in basis]
        targets = [by_head[h] for h in heads]
        rest = []
        good = True
        for j in (3, 4, 5):
            cands = [s for s in sig if all(sapp(s, w[pinv[j]]) == t[j] for w, t in zip(basis, targets))]
            if not cands:
                good = False; break
            rest.append(cands)
        if not good:
            continue
        for s3, s4, s5 in product(*rest):
            g = (pi, (s0, s1, s2, s3, s4, s5))
            GD.append(g)
def act_d4(g, w):
    pi, ss = g
    res = [0] * 6
    for i in range(6):
        res[pi[i]] = sapp(ss[pi[i]], w[i])
    return tuple(res)
assert all(act_d4(g, w) in hexacode for g in GD for w in hexacode)
say("  G^X(D4^6) = Stab(hexacode) in S3 wr S6: order", len(GD))
def mul_d4(g, h):
    pg, sgs = g; ph, shs = h
    # (g h)(w) = g(h(w)); h: w_i -> pos ph[i] with sh[ph[i]]; then g: pos j -> pg[j] with sg[pg[j]]
    p = tuple(pg[ph[i]] for i in range(6))
    s = [None] * 6
    for i in range(6):
        j = ph[i]
        k = pg[j]
        s1 = shs[j]; s2 = sgs[k]
        s[k] = tuple(sapp(s2, sapp(s1, x)) for x in (1, 2, 3))
    return (p, tuple(s))
ident_d = (tuple(range(6)), tuple((1, 2, 3) for _ in range(6)))
for _ in range(300):
    g, h = random.choice(GD), random.choice(GD)
    w = random.choice(list(hexacode))
    assert act_d4(mul_d4(g, h), w) == act_d4(g, act_d4(h, w))
images = Counter(g[0] for g in GD)
say("  image in S6:", len(images), "permutations; kernel order", len(GD) // len(images))
kernel = [g for g in GD if g[0] == tuple(range(6))]
say("  kernel elements (pi = id):", [g[1][0] for g in kernel], "(the same sigma on every coordinate?)",
    all(len(set(g[1])) == 1 for g in kernel))
omega_mult = tuple(fm(W, x) for x in (1, 2, 3))
say("  multiplication by w on F4^*:", omega_mult, " kernel = {1, w, wbar} scalars:",
    sorted(g[1][0] for g in kernel) == sorted([(1, 2, 3), omega_mult, tuple(fm(WB, x) for x in (1, 2, 3))]))
ordD = Counter(element_order(g, mul_d4, ident_d) for g in GD)
ZD = centre(GD, mul_d4)
say("  element orders", sorted(ordD.items()), " |centre| =", len(ZD))
# how do elements act on the normal subgroup N = kernel (order 3)?  centralize or invert
Nnon = [g for g in kernel if g != ident_d]
def conj(g, x, invd):
    return mul_d4(mul_d4(g, x), invd[g])
invD = {}
Dset = set(GD)
for g in GD:
    # inverse: invert permutation and sigmas
    pi, ss = g
    pinv = [0] * 6
    for i in range(6): pinv[pi[i]] = i
    s = [None] * 6
    for i in range(6):
        # g sends pos i -> pi[i] with ss[pi[i]]; inverse sends pos pi[i] -> i with ss[pi[i]]^{-1}
        sg = ss[pi[i]]
        sinv = [0, 0, 0]
        for x in (1, 2, 3):
            sinv[sg[x - 1] - 1] = x
        s[i] = tuple(sinv)
    hinv = (tuple(pinv), tuple(s))
    assert mul_d4(g, hinv) == ident_d
    invD[g] = hinv
def parity(p):
    p = list(p); sgn = 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; sgn = -sgn
    return sgn
cent = Counter()
for g in GD:
    x = Nnon[0]
    y = conj(g, x, invD)
    cent[(parity(g[0]), "centralizes" if y == x else "inverts")] += 1
say("  action on the normal 3 by (sign of the S6 image):", dict(cent))
DD = derived_subgroup(GD, mul_d4, lambda x: invD[x], ident_d)
say("  derived subgroup order", len(DD), " contains the normal 3:", all(k in DD for k in kernel))
say("  => G^X(D4^6) = 3.S6: normal 3 = simultaneous triality (scalar w on all six D4 classes), central in the index-2")
say("     subgroup 3.A6 (derived), inverted by the odd elements (field automorphism); centre of the whole group trivial.")

# ---------------------------------------------------------------------------------------------------------------------
# 4. Codex's twined-shadow class functions on GL2(F3) (row action on the four projective lines of the tetracode).
F3lines = [(1, 0), (0, 1), (1, 1), (1, 2)]
def norm_line(v):
    x, y = v[0] % 3, v[1] % 3
    if x: inv = 1 if x == 1 else 2
    else: inv = 1 if y == 1 else 2
    return ((x * inv) % 3, (y * inv) % 3)
GL23 = [(a, b, c, d) for a, b, c, d in product(range(3), repeat=4) if (a * d - b * c) % 3]
def act(g, v):
    a, b, c, d = g
    return ((a * v[0] + b * v[1]) % 3, (c * v[0] + d * v[1]) % 3)
pairs = [frozenset({frozenset({(1, 0), (0, 1)}), frozenset({(1, 1), (1, 2)})}),
         frozenset({frozenset({(1, 0), (1, 1)}), frozenset({(0, 1), (1, 2)})}),
         frozenset({frozenset({(1, 0), (1, 2)}), frozenset({(0, 1), (1, 1)})})]
def stats(g):
    a = b = 0
    perm = {}
    for l in F3lines:
        im = act(g, l)
        nl = norm_line(im)
        perm[l] = nl
        if nl == l:
            a += 1
            b += 1 if im == l else -1
    pp = []
    for P in pairs:
        Q = frozenset(frozenset(perm[x] for x in blk) for blk in P)
        pp.append(pairs.index(Q))
    c = sum(1 for i in range(3) if pp[i] == i) - 1
    s = parity(pp)
    det = (g[0] * g[3] - g[1] * g[2]) % 3
    return a, b, c, s, (1 if det == 1 else -1)
st = {g: stats(g) for g in GL23}
say("Twined-shadow class functions (Codex's a, b, c, s) on GL2(F3):")
say("  s equals det (as +-1) for all 48:", all(st[g][3] == st[g][4] for g in GL23))
neg = lambda g: tuple((-x) % 3 for x in g)
say("  centre -I: a, c, s unchanged and b negated for all g:",
    all(st[neg(g)][0] == st[g][0] and st[neg(g)][2] == st[g][2] and st[neg(g)][3] == st[g][3] and st[neg(g)][1] == -st[g][1] for g in GL23))
# shadow matrix diag(a+1, b, a+c, b, a+1) + s in the (1,5) corners: components r=1..5
def shadow_matrix(g):
    a, b, c, s, _ = st[g]
    return [[a + 1, 0, 0, 0, s], [0, b, 0, 0, 0], [0, 0, a + c, 0, 0], [0, 0, 0, b, 0], [s, 0, 0, 0, a + 1]]
I3 = (1, 0, 0, 1)
say("  identity:", shadow_matrix(I3), " (= 5I + J restricted: 5S1+S5, 4S2, 6S3, 4S4, S1+5S5)")
say("  -I      :", shadow_matrix(neg(I3)), " -> the centre acts by (-1)^(r+1) on component r")

# Character table of GL2(3) by explicit classes; decompose a, b, c, s.
def mat_mul(g, h):
    a, b, c, d = g; e, f, gg, hh = h
    return ((a * e + b * gg) % 3, (a * f + b * hh) % 3, (c * e + d * gg) % 3, (c * f + d * hh) % 3)
def m_inv(g):
    for h in GL23:
        if mat_mul(g, h) == I3: return h
classes = []
seen = set()
for g in GL23:
    if g in seen: continue
    cl = {mat_mul(mat_mul(h, g), m_inv(h)) for h in GL23}
    seen |= cl
    classes.append(sorted(cl))
def mo(g):
    k, x = 1, g
    while x != I3:
        x = mat_mul(x, g); k += 1
    return k
classes.sort(key=lambda cl: (mo(cl[0]), len(cl)))
say("  classes (order, size, rep):", [(mo(cl[0]), len(cl), cl[0]) for cl in classes])
import cmath
r2 = cmath.sqrt(-2)
def chi_table(g):
    # standard values by class type, computed from invariants (order, trace, det)
    o = mo(g); tr = (g[0] + g[3]) % 3; det = (g[0] * g[3] - g[1] * g[2]) % 3
    return o, tr, det
table = {}
# build characters: trivial, sign, S3 2-dim (pair partitions), perm-on-lines minus 1 (3-dim), 3' = 3 x sign,
# faithful 4-dim = signed line rep (b), faithful 2-dims: from the class of order-8 elements by trace.
def chars(g):
    a, b, c, s, d = st[g]
    o = mo(g)
    chi1 = 1
    chi2 = d
    chi3 = c                     # perm on 3 pair partitions minus 1
    chi4 = a - 1                 # perm on 4 lines minus 1
    chi5 = (a - 1) * d
    chi8 = b
    # 2-dim faithful: value at -I is -2; at order 8 elements +- i sqrt2 according to trace (tr = 1 or 2 mod 3)
    if g == I3: chi6 = 2
    elif g == neg(I3): chi6 = -2
    elif o == 3: chi6 = -1
    elif o == 6: chi6 = 1
    elif o == 8: chi6 = r2 if (g[0] + g[3]) % 3 == 1 else -r2
    else: chi6 = 0
    chi7 = chi6.conjugate() if isinstance(chi6, complex) else chi6
    return [chi1, chi2, chi3, chi4, chi5, chi6, chi7, chi8]
names = ["1", "sgn", "2(S3)", "3(S4)", "3'", "2'", "2''", "4"]
G = GL23
M = [[complex(x) for x in chars(g)] for g in G]
# orthonormality
ok_orth = True
for i in range(8):
    for j in range(8):
        ip = sum(M[k][i] * M[k][j].conjugate() for k in range(48)) / 48
        if abs(ip - (1 if i == j else 0)) > 1e-9:
            ok_orth = False
say("  the eight class functions [1, sgn, 2(S3)=c, 3(S4)=a-1, 3'=(a-1)sgn, 2', 2'', 4=b] are orthonormal:", ok_orth)
# product identities
say("  b = 2' x 2(S3) for all g:", all(abs(complex(st[g][1]) - complex(chars(g)[5]) * chars(g)[2]) < 1e-9 for g in G))
say("  2'^2 = sgn + 3(S4) for all g:", all(abs(complex(chars(g)[5]) ** 2 - (chars(g)[1] + chars(g)[3])) < 1e-9 for g in G))
say("  #Fix(g on F3^2) = 1 + a + b (= U + V) and #Fix(-g) = 1 + a - b (= U - V):",
    all(sum(act(g, v) == v for v in product(range(3), repeat=2)) == 1 + st[g][0] + st[g][1] and
        sum(act(neg(g), v) == v for v in product(range(3), repeat=2)) == 1 + st[g][0] - st[g][1] for g in G))
say("  power map: (U+V)(g^2) = (U+V)(g) (U-V)(g) for all g:",
    all(1 + st[mat_mul(g, g)][0] + st[mat_mul(g, g)][1] == (1 + st[g][0] + st[g][1]) * (1 + st[g][0] - st[g][1]) for g in G))

with open(__file__.replace(".py", "_output.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(out) + "\n")
