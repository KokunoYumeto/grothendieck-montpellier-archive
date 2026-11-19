"""Finite checks for cote 119, scans 155-160 (the 'Digressions combinatoires').
Claude Opus 5.5 at effort max, reader 119_144-161_276-281, horizontal sweep 3, 19 Nov 2026.
Plain Python, exhaustive enumeration; a computation, not a proof-assistant certificate."""
import itertools as it
from collections import Counter

def comp(p, q):              # p o q : first q, then p
    return tuple(p[i] for i in q)
def inv(p):
    r = [0] * len(p)
    for i, x in enumerate(p):
        r[x] = i
    return tuple(r)
def ctype(p):
    n = len(p); seen = [False] * n; c = []
    for i in range(n):
        if not seen[i]:
            l = 0; j = i
            while not seen[j]:
                seen[j] = True; j = p[j]; l += 1
            c.append(l)
    return tuple(sorted(c, reverse=True))
def sign(p):
    return (-1) ** (len(p) - len(ctype(p)))
def order(p):
    from math import lcm
    o = 1
    for l in ctype(p):
        o = lcm(o, l)
    return o
def gen_group(gens, n):
    e = tuple(range(n)); G = {e}; fr = [e]
    while fr:
        nf = []
        for g in fr:
            for s in gens:
                h = comp(s, g)
                if h not in G:
                    G.add(h); nf.append(h)
        fr = nf
    return G

# ---------- 1. the outer automorphism of S6 via synthemes and totals ----------
S6 = list(it.permutations(range(6)))
duads = [frozenset(d) for d in it.combinations(range(6), 2)]
synth = set()
for a in duads:
    for b in duads:
        if a & b: continue
        c = frozenset(range(6)) - a - b
        synth.add(frozenset([a, b, c]))
synth = list(synth)
totals = []
for five in it.combinations(synth, 5):
    ds = [d for s in five for d in s]
    if len(set(ds)) == 15:
        totals.append(frozenset(five))
assert len(synth) == 15 and len(totals) == 6
tindex = {t: i for i, t in enumerate(totals)}
def act_duad(s, d): return frozenset(s[x] for x in d)
def act_synth(s, y): return frozenset(act_duad(s, d) for d in y)
def Phi(s):       # permutation of the 6 totals induced by s
    return tuple(tindex[frozenset(act_synth(s, y) for y in t)] for t in totals)
PH = {s: Phi(s) for s in S6}
assert len(set(PH.values())) == 720
assert all(PH[comp(a, b)] == comp(PH[a], PH[b]) for a, b in [(S6[5], S6[77]), (S6[300], S6[611]), (S6[123], S6[456])])
tr = (1, 0, 2, 3, 4, 5)
print("1. transposition -> cycle type", ctype(PH[tr]), "(outer: a triple transposition)")
# dictionary of the duality (155, 157): classes of subgroups
def stab(pred): return [s for s in S6 if pred(s)]
def orbits(perms, n):
    G = gen_group(perms, n) if len(perms) < 50 else set(perms)
    seen = set(); orbs = []
    for i in range(n):
        if i in seen: continue
        o = {g[i] for g in G}; seen |= o; orbs.append(sorted(o))
    return orbs
pt = stab(lambda s: s[0] == 0)
print("   point stabilizer (S5, order", len(pt), ") -> orbits on totals:", [len(o) for o in orbits([PH[s] for s in pt], 6)])
du = stab(lambda s: frozenset([s[0], s[1]]) == frozenset([0, 1]))
img = [PH[s] for s in du]
pairs3 = []
for p in it.combinations(it.combinations(range(6), 2), 3):
    if len(set(x for d in p for x in d)) == 6:
        P = frozenset(frozenset(d) for d in p)
        if all(frozenset(frozenset(g[x] for x in d) for d in P) == P for g in img):
            pairs3.append(P)
print("   duad stabilizer (S2xS4, order", len(du), ") -> orbits on totals", [len(o) for o in orbits(img, 6)],
      "; preserved (2,2,2)-partitions of the totals:", len(pairs3))
dt = stab(lambda s: frozenset(s[x] for x in (0, 1, 2)) in (frozenset([0, 1, 2]), frozenset([3, 4, 5])))
img = [PH[s] for s in dt]
dits = [frozenset([frozenset(a), frozenset(range(6)) - frozenset(a)]) for a in it.combinations(range(6), 3) if 0 in a]
pres = [D for D in dits if all(frozenset(frozenset(g[x] for x in h) for h in D) == D for g in img)]
print("   ditriad stabilizer (S3 wr S2, order", len(dt), ") -> preserved ditriads of the totals:", len(pres))
# transitive S5s and A5s: S* and Ic(S)
def subgroups_transitive_S5():
    # the transitive S5's are the images under Phi^{-1} of point stabilizers of the totals
    PHinv = {v: k for k, v in PH.items()}
    out = []
    for j in range(6):
        out.append(frozenset(PHinv[g] for g in S6 if g[j] == j))
    return out
TS5 = subgroups_transitive_S5()
print("   transitive S5's on S:", len(TS5), "; transitive on S:", all(len(orbits(list(H), 6)) == 1 for H in TS5))
TA5 = [frozenset(g for g in H if sign(g) == 1) for H in TS5]
ic = set()
for H in TA5:
    ic.add(H)
print("   transitive A5's, one in each transitive S5:", len(ic),
      "; each S5 also contains odd permutations:", all(any(sign(g) == -1 for g in H) for H in TS5))
# all transitive A5 subgroups = conjugates of one; count them
H0 = next(iter(ic))
conj = set()
for s in S6:
    si = inv(s)
    conj.add(frozenset(comp(comp(s, h), si) for h in H0))
print("   conjugates of a transitive A5 in S6:", len(conj), "(the 12 icosahedral structures S6/A5 map 2:1 onto them)")
A6 = [s for s in S6 if sign(s) == 1]
orbA6 = set()
for s in A6:
    si = inv(s); orbA6.add(frozenset(comp(comp(s, h), si) for h in H0))
print("   A6-orbit of a transitive A5 among the subgroups:", len(orbA6), "(so A6 has two orbits of 6 on the 12 structures, each mapping bijectively to S*: Ic(S) = S* x omega(S))")
# (a) of 155: s in S, s' in S*: stabilizer and equivariant bijection S-{s} = S*-{s'}
st = [s for s in S6 if s[0] == 0 and PH[s][0] == 0]
o1 = orbits(st, 6); o2 = orbits([PH[s] for s in st], 6)
eq = []
for f in it.permutations(range(1, 6)):
    m = dict(zip(range(1, 6), f))
    if all(PH[s][m[x]] == m[s[x]] for s in st for x in range(1, 6)):
        eq.append(m)
print("2. (155, item 3a) |Stab(s) n Stab(s')| =", len(st), "; orbits on S:", [len(o) for o in o1],
      "on S*:", [len(o) for o in o2], "; equivariant bijections S-{s} -> S*-{s'}:", len(eq))

# ---------- 3. the square characters of 156-157 ----------
Q = (0, 1, 2, 3)          # square with cyclic order 0-1-2-3, complement eps = {4,5}
diag = [frozenset([0, 2]), frozenset([1, 3])]
sides = [frozenset([frozenset([0, 1]), frozenset([2, 3])]), frozenset([frozenset([1, 2]), frozenset([3, 0])])]
def preserves_square(s):
    if frozenset(s[x] for x in Q) != frozenset(Q): return False
    return frozenset(frozenset(s[x] for x in d) for d in diag) == frozenset(diag)
H = [s for s in S6 if preserves_square(s)]
print("3. stabilizer of (square on 4 points, complementary pair): order", len(H))
img = [PH[s] for s in H]
ob = orbits(img, 6)
epsS = [o for o in ob if len(o) == 2][0]; QS = [o for o in ob if len(o) == 4][0]
# diagonals of Q*: the unique pairing of QS preserved by the image
pairings = []
for a in QS[1:]:
    p1 = frozenset([QS[0], a]); p2 = frozenset(QS) - p1
    P = frozenset([p1, frozenset(p2)])
    if all(frozenset(frozenset(g[x] for x in d) for d in P) == P for g in img):
        pairings.append(P)
assert len(pairings) == 1
diagS = list(pairings[0])
d0 = sorted(diagS[0]); d1 = sorted(diagS[1])
sidesS = [frozenset([frozenset([d0[0], d1[0]]), frozenset([d0[1], d1[1]])]),
          frozenset([frozenset([d0[0], d1[1]]), frozenset([d0[1], d1[0]])])]
def ch_set_swap(g, two):     # +1 if g fixes each member of the 2-set 'two' (members are sets), -1 if it swaps
    a = two[0]
    ga = frozenset(g[x] for x in a) if not isinstance(next(iter(a)), frozenset) else frozenset(frozenset(g[x] for x in d) for d in a)
    return 1 if ga == a else -1
def sign_on(g, pts):
    pts = list(pts); idx = {p: i for i, p in enumerate(pts)}
    return sign(tuple(idx[g[p]] for p in pts))
chars = {}
for s in H:
    g = PH[s]
    chars.setdefault("eps", []).append(sign_on(s, (4, 5)))
    chars.setdefault("diagQ", []).append(ch_set_swap(s, diag))
    chars.setdefault("codiagQ", []).append(ch_set_swap(s, sides))
    chars.setdefault("sgn4(Q)", []).append(sign_on(s, Q))
    chars.setdefault("eps*", []).append(sign_on(g, epsS))
    chars.setdefault("diagQ*", []).append(ch_set_swap(g, diagS))
    chars.setdefault("codiagQ*", []).append(ch_set_swap(g, sidesS))
    chars.setdefault("sgn4(Q*)", []).append(sign_on(g, QS))
for k in ("diagQ", "codiagQ", "diagQ*", "codiagQ*"):
    pass
chars["rot(Q)"] = [a * b for a, b in zip(chars["diagQ"], chars["codiagQ"])]
chars["rot(Q*)"] = [a * b for a, b in zip(chars["diagQ*"], chars["codiagQ*"])]
names = list(chars)
rels = []
for r in range(1, 4):
    for comb in it.combinations(names, r):
        prod = [1] * len(H)
        for c in comb:
            prod = [a * b for a, b in zip(prod, chars[c])]
        if all(x == 1 for x in prod):
            rels.append(" ^ ".join(comb))
print("   trivial products of at most three of the torsors (= relations):")
for r_ in rels:
    print("     ", r_, "= 1")

# ---------- 4. AGL_2(F_3), its 12 lines, directions, pairings ----------
F3 = range(3)
pts = [(x, y) for x in F3 for y in F3]
pidx = {p: i for i, p in enumerate(pts)}
dirs = [(1, 0), (0, 1), (1, 1), (1, 2)]
lines = []
for d in dirs:
    seen = set()
    for p in pts:
        L = frozenset(((p[0] + t * d[0]) % 3, (p[1] + t * d[1]) % 3) for t in F3)
        if L not in seen:
            seen.add(L); lines.append((L, d))
lidx = {L: i for i, (L, d) in enumerate(lines)}
ldir = [dirs.index(d) for (L, d) in lines]
GL = [((a, b), (c, d)) for a in F3 for b in F3 for c in F3 for d in F3 if (a * d - b * c) % 3]
def aff(A, v, p): return ((A[0][0] * p[0] + A[0][1] * p[1] + v[0]) % 3, (A[1][0] * p[0] + A[1][1] * p[1] + v[1]) % 3)
AGL = {}
for A in GL:
    for v in pts:
        perm = tuple(lidx[frozenset(aff(A, v, p) for p in L)] for (L, d) in lines)
        AGL[perm] = (A, v)
print("4. |AGL_2(F_3)| =", len(AGL), "= 3 x 144:", len(AGL) == 3 * 144)
def dirperm(g): return tuple(ldir[g[[i for i in range(12) if ldir[i] == k][0]]] for k in range(4))
ker = [g for g in AGL if dirperm(g) == (0, 1, 2, 3)]
print("   kernel of the action on the 4 directions: order", len(ker))
Ei = [[i for i in range(12) if ldir[i] == k] for k in range(4)]
pairsig = Counter((sign_on(g, Ei[0]), sign_on(g, Ei[1])) for g in ker)
print("   kernel acting on (E_0, E_1): sign pairs", dict(pairsig), "(equal signs only: the (S3xS3)' of III.5)")
dbl = [g for g in AGL if ctype(dirperm(g)) == (2, 2)]
print("   lifts of double transpositions:", len(dbl), "; their orders:", Counter(order(g) for g in dbl))
alphas = [frozenset([frozenset([0, 1]), frozenset([2, 3])]), frozenset([frozenset([0, 2]), frozenset([1, 3])]),
          frozenset([frozenset([0, 3]), frozenset([1, 2])])]
def act_alpha(g, al): dp = dirperm(g); return frozenset(frozenset(dp[x] for x in pr) for pr in al)
stabs = [[g for g in AGL if act_alpha(g, al) == al] for al in alphas]
print("   stabilizers of the three pairings alpha: orders", [len(s) for s in stabs])
lin = {AGL[g][0] for g in stabs[0]}
def mmul(A, B): return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % 3 for j in range(2)) for i in range(2))
def morder(A):
    I = ((1, 0), (0, 1)); M = A; o = 1
    while M != I:
        M = mmul(M, A); o += 1
    return o
I2 = ((1, 0), (0, 1))
print("   linear parts of Stab(alpha): order", len(lin), "; element orders", dict(Counter(morder(A) for A in lin)),
      "; involutions:", sum(1 for A in lin if morder(A) == 2), "(5 involutions and an element of order 8: semidihedral SD16)")

# ---------- 5. the three subgroups G_alpha (156): search ----------
transl = [g for g in AGL if AGL[g][0] == I2]
results = {}
for ai, al in enumerate(alphas):
    p1, p2 = sorted(sorted(x) for x in al)
    A_ = [i for i in range(12) if ldir[i] in p1]; B_ = [i for i in range(12) if ldir[i] in p2]
    # local indices
    a_loc = {x: i for i, x in enumerate(A_)}; b_loc = {x: i for i, x in enumerate(B_)}
    def restrict(g, part, loc): return tuple(loc[g[x]] for x in part)
    keeps = [g for g in stabs[ai] if all(g[x] in A_ for x in A_)]
    found = []
    # inner-type graphs: bijection h: A -> B (as local perm), theta(x) = h x h^-1
    # outer-type graphs: bijection f: A -> totals(B), theta(x) = PH^-1(f x f^-1)
    PHinv = {v: k for k, v in PH.items()}
    for kind in ("inner", "outer"):
        for f in it.permutations(range(6)):
            fi = inv(f)
            def theta(x):
                c = comp(comp(f, x), fi)
                return c if kind == "inner" else PHinv[c]
            ok = all(theta(restrict(t, A_, a_loc)) == restrict(t, B_, b_loc) for t in transl)
            if not ok: continue
            ok = all(comp(comp(restrict(g, B_, b_loc), theta(x)), inv(restrict(g, B_, b_loc))) ==
                     theta(comp(comp(restrict(g, A_, a_loc), x), inv(restrict(g, A_, a_loc))))
                     for g in keeps for x in [(1, 0, 2, 3, 4, 5), (1, 2, 3, 4, 5, 0)])
            if ok:
                found.append((kind, f))
    results[ai] = (A_, B_, found)
    print("5. alpha", ai, ": graphs containing the translations and normalized by the S-preserving part of Stab(alpha):",
          Counter(k for k, f in found))

# build G_alpha for the outer-type solution(s) and test the claims of 156
PHinv = {v: k for k, v in PH.items()}
Gs = []
for ai in range(3):
    A_, B_, found = results[ai]
    outs = [f for k, f in found if k == "outer"]
    if not outs:
        Gs.append(None); continue
    f = outs[0]; fi = inv(f)
    G = set()
    for x in S6:
        y = PHinv[comp(comp(f, x), fi)]
        perm = [0] * 12
        for i, a in enumerate(A_): perm[a] = A_[x[i]]
        for i, b in enumerate(B_): perm[b] = B_[y[i]]
        G.add(tuple(perm))
    Gs.append(frozenset(G))
    print("   G_alpha", ai, ": order", len(G), "; contains all translations:", all(t in G for t in transl),
          "; number of outer-type solutions:", len(outs))
if all(Gs):
    def conjset(g, G): gi = inv(g); return frozenset(comp(comp(g, h), gi) for h in G)
    perm_ok = all(conjset(g, G) in Gs for g in AGL for G in Gs)
    print("6. AGL_2(F_3) permutes the three G_alpha:", perm_ok,
          "; distinct:", len(set(Gs)) == 3)
    st0 = stabs[0]
    norm = all(conjset(g, Gs[0]) == Gs[0] for g in st0)
    inter = [g for g in st0 if g in Gs[0]]
    cent = [g for g in st0 if all(comp(g, h) == comp(h, g) for h in Gs[0])]
    print("   Stab(alpha) normalizes G_alpha:", norm, "; |Stab(alpha) n G_alpha| =", len(inter),
          "; elements of Stab(alpha) centralizing G_alpha:", len(cent),
          "-> Stab(alpha) embeds in Aut(G_alpha) (order 1440) with index", 1440 // len(st0))
    V0 = frozenset(transl)
    NG = [h for h in Gs[0] if conjset(h, V0) == V0]
    print("   V_0 (translations, order 9) is a Sylow 3-subgroup common to the G_alpha:", all(V0 <= G for G in Gs),
          "; |N_{G_alpha}(V_0)| =", len(NG), "; N/V_0 of order", len(NG) // 9)
    Q_ = [h for h in NG]
    # is N/V0 dihedral of order 8? count elements of order 4 in the quotient via coset representatives
    cos = {}
    for h in NG:
        key = frozenset(comp(h, v) for v in V0)
        cos[key] = h
    reps = list(cos.values())
    def qorder(h):
        o = 1; m = h
        while m not in V0:
            m = comp(h, m); o += 1
        return o
    print("   orders in N/V_0:", dict(Counter(qorder(h) for h in reps)), "(D4: 1,5 x 2,2 x 4)")

# ---------- 7. projective lines: IV.1, IV.2, III.4, II.1 ----------
def pgl_perms(q, mul, add, invf, elems):
    P1 = [(1, x) for x in elems] + [(0, 1)]
    def norm(v):
        a, b = v
        if a != 0:
            ia = invf(a); return (1, mul(ia, b))
        return (0, 1)
    perms = set()
    for a, b, c, d in it.product(elems, repeat=4):
        det = add(mul(a, d), neg(mul(b, c)))
        if det == 0: continue
        perm = tuple(P1.index(norm((add(mul(a, v[0]), mul(b, v[1])), add(mul(c, v[0]), mul(d, v[1]))))) for v in P1)
        perms.add(perm)
    return P1, perms
# F_4 = {0,1,2,3} with 2 = w, 3 = w^2 = w+1 ; addition = xor
def mul4(x, y):
    if x == 0 or y == 0: return 0
    lg = {1: 0, 2: 1, 3: 2}; ex = {0: 1, 1: 2, 2: 3}
    return ex[(lg[x] + lg[y]) % 3]
def neg(x): return x if MOD == 4 else (-x) % MOD
MOD = 4
P1, G4 = pgl_perms(4, mul4, lambda x, y: x ^ y, lambda a: {1: 1, 2: 3, 3: 2}[a], range(4))
frob = tuple(P1.index((v[0] and 1, mul4(v[1], v[1])) if v[0] else (0, 1)) for v in P1)
print("7. |PGL_2(F_4)| on 5 points:", len(G4), "; all even:", all(sign(g) == 1 for g in G4),
      "; Frobenius cycle type:", ctype(frob), "; <PGL, Frob> order:", len(gen_group(list(G4) + [frob], 5)))
MOD = 5
P1, G5 = pgl_perms(5, lambda x, y: x * y % 5, lambda x, y: (x + y) % 5, lambda a: pow(a, 3, 5), range(5))
print("   |PGL_2(F_5)| on 6 points:", len(G5), "; transitive:", len(orbits(list(G5), 6)) == 1,
      "; odd elements:", sum(1 for g in G5 if sign(g) == -1))
MOD = 3
P1, G3 = pgl_perms(3, lambda x, y: x * y % 3, lambda x, y: (x + y) % 3, lambda a: a, range(3))
print("   |PGL_2(F_3)| on 4 points:", len(G3), "(= S4)")
MOD = 2
P1, G2 = pgl_perms(2, lambda x, y: x * y % 2, lambda x, y: (x + y) % 2, lambda a: a, range(2))
print("   |PGL_2(F_2)| on 3 points:", len(G2), "(= S3)")
# III.2 margin: monomial 3x3 matrices over F_3 (preserving three lines forming a basis)
mono = []
for p in it.permutations(range(3)):
    for sg in it.product((1, 2), repeat=3):
        M = [[0] * 3 for _ in range(3)]
        for i in range(3): M[p[i]][i] = sg[i]
        mono.append(M)
def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])) % 3
print("   monomial group over F_3:", len(mono), "; with det 1:", sum(1 for M in mono if det3(M) == 1))
