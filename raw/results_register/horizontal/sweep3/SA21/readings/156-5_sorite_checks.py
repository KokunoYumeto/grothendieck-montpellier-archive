# 156-5 brute-force checks, reader A (Claude Opus 5.5 at effort max), horizontal sweep 3, 19 Nov 2026. Run: python -I -B 156-5_sorite_checks.py
# Brute-force checks of 156-5 "Sorite ensembliste" (reader A, sweep 3). Subsets of L as bitmasks; families as frozensets.
import itertools, sys
from collections import defaultdict
sys.stdout.reconfigure(encoding='utf-8')

def sub(a, b): return a & ~b == 0          # a subset of b
def supp(F):
    s = 0
    for A in F: s |= A
    return s
def bd(F, A):
    s = 0
    for B in F:
        if B != A and sub(B, A): s |= B
    return s
def op(F, A): return A & ~bd(F, A)
def bits(m, n): return [i for i in range(n) if m >> i & 1]
def smallest(cands):
    for A in cands:
        if all(sub(A, B) for B in cands): return A
    return None
def pre1(F, n):   # 1 deg
    for x in bits(supp(F), n):
        c = [A for A in F if A >> x & 1]
        if smallest(c) is None: return False
    return True
def alpha(F):
    for A in F:
        for B in F:
            u = 0
            for C in F:
                if sub(C, A & B): u |= C
            if u != A & B: return False
    return True
def beta(F, n):
    return all(any((op(F, A) >> x) & 1 for A in F) for x in bits(supp(F), n))
def gamma(F):
    P = [op(F, A) for A in F if op(F, A)]
    u = 0
    for p in P: u |= p
    if u != supp(F): return False
    Ls = [A for A in F if op(F, A)]
    for A, B in itertools.combinations(Ls, 2):
        if op(F, A) & op(F, B): return False
    return True
def delta(F):
    P = set(op(F, A) for A in F if op(F, A))
    return all(not (A & p) or sub(p, A) for A in F for p in P)
def eta(F):
    return all(sub(A, B) for A in F for B in F if op(F, A) and sub(op(F, A), B))
def deltap(F):
    for A in F:
        u = 0
        for B in F:
            if sub(B, A): u |= op(F, B)
        if u != A: return False
    return True
def admissible(F, n): return pre1(F, n) and all(op(F, A) for A in F)

def fams(n):
    subsets = list(range(1 << n))
    for k in range(len(subsets) + 1):
        for c in itertools.combinations(subsets, k):
            yield frozenset(c)

out = []
# ---- Prop 1 (156-5/2-3), all families on n <= 4 points
for n in range(1, 5):
    cnt = defaultdict(int)
    for F in fams(n):
        c1 = pre1(F, n); c2 = alpha(F) and beta(F, n); c3 = gamma(F) and delta(F) and eta(F)
        c3p = gamma(F) and deltap(F)
        cnt['total'] += 1
        if not (c1 == c2 == c3): cnt['Prop1 fails'] += 1
        if c3p != c1: cnt['gamma+delta-prime != 1deg'] += 1
        if gamma(F) and delta(F) and not eta(F): cnt['gamma+delta without eta'] += 1
    out.append(f'Prop1 n={n}: {dict(cnt)}')

n = 3
ADM = [F for F in fams(n) if admissible(F, n)]
ADMSET = set(ADM)
out.append(f'admissible families on 3 points (incl. empty family): {len(ADM)}')
def closed_in(P, F): return P <= F and all(B in P for A in P for B in F if sub(B, A))
def le(P, F): return closed_in(P, F)
def compat_a(P, Q, n): U = P | Q; return admissible(U, n) and closed_in(P, U) and closed_in(Q, U)
def compat_b(P, Q):
    I = P & Q
    return closed_in(I, P) and closed_in(I, Q) and supp(P) & supp(Q) == supp(I)
def fclosed(F, S):   # S is F-closed in |F|: union of the members of F inside S
    u = 0
    for A in F:
        if sub(A, S): u |= A
    return u == S
def compat_c(P, Q):
    T = supp(P) & supp(Q)
    if not (fclosed(P, T) and fclosed(Q, T)): return False
    for A in P | Q:
        if sub(A, T) and ((A in P) != (A in Q)): return False
    return True
def compat_d(P, Q):
    for A in P:
        for B in Q:
            C = A & B
            if not (fclosed(frozenset(X for X in P if sub(X, A)), C) and fclosed(frozenset(X for X in Q if sub(X, B)), C)): return False
            if frozenset(X for X in P if sub(X, C)) != frozenset(X for X in Q if sub(X, C)): return False
    return True
cnt = defaultdict(int)
for P in ADM:
    for Q in ADM:
        a = compat_a(P, Q, n); b = compat_b(P, Q); c = compat_c(P, Q); d = compat_d(P, Q)
        cnt['pairs'] += 1
        if not (a == b == c == d): cnt['a,b,c,d disagree'] += 1; ex = (P, Q, a, b, c, d)
        if a:
            if (sub(supp(P), supp(Q))) != (P <= Q): cnt['Cor2 fails'] += 1
out.append(f'compatibility (156-5/8-12) n=3: {dict(cnt)}')
if cnt['a,b,c,d disagree']: out.append(f'  example: {[sorted(x) if isinstance(x, frozenset) else x for x in ex]}')

# ---- multistrates and connectedness (156-5/13-15), C4
for n in (1, 2, 3):
    A_ = [F for F in fams(n) if admissible(F, n)]
    M = [F for F in A_ if F and any(all(sub(B, X) for B in F) for X in F)]
    idx = {F: i for i, F in enumerate(M)}
    par = list(range(len(M)))
    def find(i):
        while par[i] != i: par[i] = par[par[i]]; i = par[i]
        return i
    for X in M:
        for Y in M:
            if le(X, Y): par[find(idx[X])] = find(idx[Y])
    comps = defaultdict(list)
    for X in M: comps[find(idx[X])].append(X)
    bad = 0
    for X in M:
        for Y in M:
            if find(idx[X]) != find(idx[Y]) and not compat_a(X, Y, n): bad += 1; exb = (X, Y)
    out.append(f'multistrates n={n}: {len(M)}, components {len(comps)}, pairs in different components not compatible: {bad}')
    if n == 2:
        out.append('  components n=2: ' + ' | '.join(str([sorted(F) for F in c]) for c in comps.values()))
    if bad: out.append(f'  e.g. {sorted(exb[0])} and {sorted(exb[1])}')
# the multistrate of 156-5/13: {A, {x}, A u {x}}
out.append(f"{{A,{{x}},A u {{x}}}} with A={{0}}, x=1 admissible? {admissible(frozenset([1, 2, 3]), 2)}")

# ---- refinement (156-5/20-23), subdivision (23-24), F.G (28-29), C7 (30-32)
n = 3
def Asm(F, x):
    return smallest([A for A in F if A >> x & 1])
def ref_a(F, G):
    for A in F:
        if smallest([B for B in G if sub(A, B)]) is None: return False
        for B in G:
            if not fclosed(F, A & B): return False
    return True
def ref_b(F, G):
    phi = {}
    for A in F:
        Bs = [B for B in G if op(F, A) and sub(op(F, A), op(G, B))]
        if not Bs: return False
        phi[A] = Bs[0]
    return all(sub(phi[A1], phi[A]) for A in F for A1 in F if sub(A1, A))
def ref_bp(F, G):
    for A in F:
        if not any(sub(op(F, A), op(G, B)) for B in G): return False
    return all(sub(A, B) for A in F for B in G if sub(op(F, A), B))
def ref_bpp(F, G):
    if not sub(supp(F), supp(G)): return False
    for x in bits(supp(F), n):
        for y in bits(supp(F), n):
            if (Asm(F, y) >> x) & 1 and not (Asm(G, y) >> x) & 1: return False
    return True
cnt = defaultdict(int); REF = {}
for F in ADM:
    for G in ADM:
        a, b, bp, bpp = ref_a(F, G), ref_b(F, G), ref_bp(F, G), ref_bpp(F, G)
        cnt['pairs'] += 1
        if not (a == b == bp): cnt['a,b,b-prime disagree'] += 1; exr = (F, G, a, b, bp, bpp)
        if bpp != a: cnt['b-second != a'] += 1; exr2 = (F, G, a, bpp)
        REF[(F, G)] = a
out.append(f'refinement (156-5/20-23) n=3: {dict(cnt)}')
if cnt['a,b,b-prime disagree']: out.append(f'  example: {[sorted(x) if isinstance(x, frozenset) else x for x in exr]}')
if cnt['b-second != a']: out.append(f'  b-second example: {[sorted(x) if isinstance(x, frozenset) else x for x in exr2]}')
# order
anti = sum(1 for F in ADM for G in ADM if F != G and REF[(F, G)] and REF[(G, F)])
trans = 0
for F in ADM:
    for G in ADM:
        if not REF[(F, G)]: continue
        for H in ADM:
            if REF[(G, H)] and not REF[(F, H)]: trans += 1
out.append(f'refinement is an order: antisymmetry failures {anti}, transitivity failures {trans}; sub-figure => refinement failures {sum(1 for F in ADM for G in ADM if le(F, G) and not REF[(F, G)])}')
def subd(F, G): return REF[(F, G)] and supp(F) == supp(G)
cnt = defaultdict(int)
for F in ADM:
    for G in ADM:
        a = REF[(F, G)] and not any(F2 != F and le(F, F2) and REF[(F2, G)] for F2 in ADM)
        b = subd(F, G)
        c = REF[(F, G)] and all(fclosed(F, B) and sub(B, supp(F)) for B in G)
        d = all(fclosed(F, B) and sub(B, supp(F)) for B in G) and all(smallest([B for B in G if sub(A, B)]) is not None for A in F)
        cnt['pairs'] += 1
        if not (a == b == c == d): cnt['a,b,c,d disagree'] += 1; exs = (F, G, a, b, c, d)
out.append(f'subdivision (156-5/23-24) n=3: {dict(cnt)}')
if cnt['a,b,c,d disagree']: out.append(f'  example: {[sorted(x) if isinstance(x, frozenset) else x for x in exs]}')
# Prop 156-5/26 and NB 27
bad26 = 0; bad27 = 0
for F in ADM:
    for G in ADM:
        if REF[(F, G)]:
            G2 = F | frozenset(1 << x for x in bits(supp(G) & ~supp(F), n))
            if not (G2 in ADMSET and le(F, G2) and subd(G2, G)): bad26 += 1
        if le(F, G) and subd(F, G) and F != G: bad27 += 1
out.append(f'156-5/26 (refines iff sub-figure of a subdivision, explicit G-prime) failures {bad26}; 156-5/27 (F<=G and F subdivides G => F=G) failures {bad27}')
# F.G
badFG = defaultdict(int)
for F in ADM:
    for G in ADM:
        FG = frozenset(A & B for A in F for B in G if op(F, A) & op(G, B))
        if FG not in ADMSET: badFG['not admissible'] += 1; continue
        if not (REF[(FG, F)] and REF[(FG, G)]): badFG['not a lower bound'] += 1
        for H in ADM:
            if REF[(H, F)] and REF[(H, G)] and not REF[(H, FG)]: badFG['not the Inf'] += 1; break
        if compat_a(F, G, n) and FG != (F & G): badFG['compatible but F.G != F cap G'] += 1
        if supp(FG) != supp(F) & supp(G): badFG['support'] += 1
out.append(f'F.G (156-5/28-29) n=3 failures: {dict(badFG)}')
# C7: extension of subdivisions
bad7 = defaultdict(int); tested = 0
for F in ADM:
    for G in ADM:
        if not le(G, F): continue
        for G1 in ADM:
            if not subd(G1, G): continue
            tested += 1
            F1 = G1 | (F - G)
            if F1 not in ADMSET: bad7['not admissible'] += 1; exc = (F, G, G1); continue
            if not subd(F1, F): bad7['not a subdivision'] += 1
            if frozenset(A for A in F1 if sub(A, supp(G))) != G1: bad7['does not induce G-prime'] += 1
out.append(f'C7 extension F-prime = G-prime u (F - G) (156-5/30-32) n=3: tested {tested}, failures {dict(bad7)}')
if bad7: out.append(f'  example: {[sorted(x) for x in exc]}')
print('\n'.join(out))
