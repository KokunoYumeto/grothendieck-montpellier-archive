# Independent finite checks for the intake of RESEARCH_SA10 (final of 19 Nov 2026).
# Written by Claude Opus 5.5 at effort max (agent a6d42bf6fe2b0d8a8) for the intake; it does not
# import or run any program of the return. Usage: python -I -B INTAKE_RESEARCH_SA10_20261119_checks.py
from itertools import permutations, product, combinations, combinations_with_replacement

out = []
def say(*a):
    out.append(' '.join(str(x) for x in a))

# ---------------------------------------------------------------- 1. A1.3: the plane 0 < R < C
# Zones: germ classes of points. o origin; pn,nn real points near 0 (pos/neg); pf,nf far real points;
# un,dn non-real points near 0; ur,dr non-real points near R but far from 0; uf,df far from R and 0.
cell = {'o': 'o', 'pn': 'p', 'pf': 'p', 'nn': 'n', 'nf': 'n',
        'un': 'u', 'ur': 'u', 'uf': 'u', 'dn': 'd', 'dr': 'd', 'df': 'd'}
adj = [('o', 'pn'), ('o', 'nn'), ('o', 'un'), ('o', 'dn'), ('pn', 'un'), ('pn', 'dn'), ('nn', 'un'),
       ('nn', 'dn'), ('pf', 'ur'), ('pf', 'dr'), ('nf', 'ur'), ('nf', 'dr')]   # specialisation -> generisation
disk = {'o', 'pn', 'nn', 'un', 'dn'}                          # core of germ_0 C
strip = {'o', 'pn', 'nn', 'pf', 'nf', 'un', 'dn', 'ur', 'dr'}  # core of germ_R C (contains a disk at 0)
seg = {'o', 'pn', 'nn'}                                         # core of germ_0 R
real = {'o', 'pn', 'nn', 'pf', 'nf'}
stones = {   # 151/057-060: V_ij = germ of X_i in X_j minus R_ij ; V*_ij = V_ij minus X_{j-1}; strata S_i
    'S0': {'o'}, 'S1': real - {'o'}, 'S2': set(cell) - real,
    'V01': seg, 'V01*': seg - {'o'}, 'V12': strip - {'o'}, 'V12*': strip - real,
    'V02': disk, 'V02*': disk - real}
# triple stones by (10)-(11) of 151/060 for (i,j,k)=(0,j,2): V^j_{0,2} = germ_0 C minus (R_{0,2} u S_{j,2})
R02 = set(); S = {0: real, 1: real, 2: set()}                  # S_{0,2}=X_0 u X_1=R, S_{1,2}=X_1=R, S_{2,2}=empty
for j in (0, 1, 2):
    t = disk - R02 - S[j]
    same = [k for k, v in stones.items() if v == t and k.startswith('V02')]
    say('A1.3 triple stone V^%d_{0,2} equals' % j, same)
incl = sorted((a, b) for a in stones for b in stones if a != b and stones[a] <= stones[b])
say('A1.3 nonidentity inclusions among the nine stones:', len(incl), incl)

def seen(st):
    return [x for x in adj if x[0] in stones[st] and x[1] in stones[st]]

def value(sheaf, st, a):   # value of the generisation map at adjacency a, None if the target stalk is a singleton
    return sheaf[st].get(cell[a[0]] + cell[a[1]]) if cell[a[1]] == 'u' else None

strong = {st: {} for st in stones}
strong['V12'] = {'pu': 1, 'nu': 1}
strong['V02'] = {'pu': 0, 'nu': 0, 'ou': 0}
succ = {st: {} for st in stones}
succ['V12'] = {'pu': 0, 'nu': 1}
for name, sh, used in (('strong (all pairs and triples)', strong, list(stones)),
                       ('successor', succ, ['S0', 'S1', 'S2', 'V01', 'V01*', 'V12', 'V12*'])):
    ok = all(value(sh, a, x) == value(sh, b, x) for a, b in incl if a in used and b in used for x in seen(a))
    # global sheaf near 0: cell functor with stalks o,p,n,d singletons and u={0,1}; functoriality gives
    # F(p->u)=F(n->u)=F(o->u)=a. Isomorphisms on the u-cell of each stone (connected there): a permutation.
    ustones = [st for st in used if any(cell[z] == 'u' for z in stones[st])]
    sols = 0
    for a in (0, 1):
        for perms in product((0, 1), repeat=len(ustones)):     # 0 = identity, 1 = swap
            phi = dict(zip(ustones, perms))
            if any(phi[x] != phi[y] for x, y in incl if x in phi and y in phi):
                continue                                         # cocone isomorphisms are identities
            good = True
            for st in ustones:
                for key in ('pu', 'nu', 'ou'):
                    if key in sh[st] and any(cell[p] + cell[q] == key for p, q in seen(st)):
                        if (a ^ phi[st]) != sh[st][key]:
                            good = False
            sols += good
    say('A1.3', name, ': cocone compatible on every inclusion:', ok, '; extensions to a sheaf near 0:', sols)

# ---------------------------------------------------------------- 2. A4.2: seven indices, nineteen points
I = [frozenset(s) for r in range(3) for s in combinations((1, 2, 3), r)]
def tmap(i, j, bottom=True):
    if i == j:
        return {x: x for x in pts(i, bottom)}
    if not i:
        return {'*': '*'} if bottom else {}
    if i == frozenset({1}) and j == frozenset({1, 2}):
        return {x: {0: 1, 1: 0}.get(x, x) for x in pts(i, bottom)}
    return {x: x for x in pts(i, bottom)}
def pts(i, bottom=True):
    return (['*'] if bottom else []) + ([0, 1] if i else [])
for bottom in (True, False):
    le = [(i, j) for i in I for j in I if i <= j]
    functor = all(all(tmap(j, k, bottom)[tmap(i, j, bottom)[x]] == tmap(i, k, bottom)[x] for x in pts(i, bottom))
                  for i, j in le for k in I if j <= k)
    P = [(i, x) for i in I for x in pts(i, bottom)]
    par = {p: p for p in P}
    def f(p):
        while par[p] != p:
            p = par[p]
        return p
    for i, j in le:
        for x, y in tmap(i, j, bottom).items():
            par[f((i, x))] = f((j, y))
    classes = len({f(p) for p in P})
    rel = {((i, x), (j, y)) for i, j in le for x, y in tmap(i, j, bottom).items()}
    order = (all((p, p) in rel for p in P) and all(not ((a, b) in rel and (b, a) in rel and a != b) for a, b in rel)
             and all((a, c) in rel for a, b in rel for b2, c in rel if b2 == b))
    emb = all(len({f((i, x)) for x in pts(i, bottom)}) == len(pts(i, bottom)) for i in I)
    i1, i2, k = frozenset({1}), frozenset({2}), frozenset({1, 2})
    fib = [(x, y) for x in pts(i1, bottom) for y in pts(i2, bottom) if tmap(i1, k, bottom)[x] == tmap(i2, k, bottom)[y]]
    say('A4.2 bottom=%s: functor %s, points %d, colimit classes %d, order relation %s, members embed %s, '
        '|X_1 x_{X_12} X_2| = %d vs |X_meet| = %d' % (bottom, functor, len(P), classes, order, emb, len(fib),
                                                       len(pts(frozenset(), bottom))))

# ---------------------------------------------------------------- 3. A4.5 / L4: stable graphs
def canon(G):
    gen, legs, edges = G
    V = len(gen)
    best = None
    for pm in permutations(range(V)):
        inv = {pm[v]: v for v in range(V)}
        key = (tuple(gen[inv[v]] for v in range(V)), tuple(pm[l] for l in legs),
               tuple(sorted(tuple(sorted((pm[a], pm[b]))) for a, b in edges)))
        if best is None or key < best:
            best = key
    return best
def connected(V, edges):
    seenv, st = {0}, [0]
    while st:
        v = st.pop()
        for a, b in edges:
            for x, y in ((a, b), (b, a)):
                if x == v and y not in seenv:
                    seenv.add(y); st.append(y)
    return len(seenv) == V
def stable(gen, legs, edges):
    val = [0] * len(gen)
    for a, b in edges:
        val[a] += 1; val[b] += 1
    for l in legs:
        val[l] += 1
    return all(2 * gen[v] - 2 + val[v] > 0 for v in range(len(gen)))
def enumerate_graphs(g, n):
    found = set()
    for V in range(1, 2 * g - 2 + n + 1):
        pairs = [(a, b) for a in range(V) for b in range(a, V)]
        for gen in product(range(g + 1), repeat=V):
            E = g - sum(gen) + V - 1
            if E < V - 1 or E < 0:
                continue
            for edges in combinations_with_replacement(pairs, E):
                if not connected(V, edges):
                    continue
                for legs in product(range(V), repeat=n):
                    if stable(gen, legs, edges):
                        found.add(canon((gen, legs, edges)))
    return sorted(found)
def contract(G, sub):
    gen, legs, edges = G
    V = len(gen)
    par = list(range(V))
    def f(v):
        while par[v] != v:
            v = par[v]
        return v
    for e in sub:
        a, b = edges[e]
        par[f(a)] = f(b)
    roots = sorted({f(v) for v in range(V)})
    idx = {r: i for i, r in enumerate(roots)}
    ng = [0] * len(roots); nv = [0] * len(roots); ne = [0] * len(roots)
    for v in range(V):
        ng[idx[f(v)]] += gen[v]; nv[idx[f(v)]] += 1
    for e in sub:
        ne[idx[f(edges[e][0])]] += 1
    ng = [ng[c] + ne[c] - nv[c] + 1 for c in range(len(roots))]
    rest = [(idx[f(a)], idx[f(b)]) for e, (a, b) in enumerate(edges) if e not in sub]
    return canon((tuple(ng), tuple(idx[f(l)] for l in legs), tuple(rest)))
for g, n in ((0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (3, 0)):
    Gs = enumerate_graphs(g, n)
    up = {G: {contract(G, set(s)) for r in range(len(G[2]) + 1) for s in combinations(range(len(G[2])), r)}
          for G in Gs}
    bad = 0; withlb = 0
    for A, B in combinations(Gs, 2):
        L = [H for H in Gs if A in up[H] and B in up[H]]
        if not L:
            continue
        withlb += 1
        maxl = [H for H in L if not any(H2 != H and H2 in up[H] for H2 in L)]
        bad += (len(maxl) != 1)
    say('A4.5 (g,n)=(%d,%d): stable graphs %d, unordered pairs %d, with a common refinement %d, without infimum %d'
        % (g, n, len(Gs), len(Gs) * (len(Gs) - 1) // 2, withlb, bad))

# ---------------------------------------------------------------- 4. B6.1 and B6.3
def comp(*fs):                       # composite of maps given as dicts, applied right to left
    def h(x):
        for f in reversed(fs):
            x = f[x]
        return x
    return h
delta = {n: {i: i for i in range(1, n + 1)} for n in (1, 2, 3)}             # n -> n+1
K = {n: {**{i: i for i in range(1, n + 1)}, n + 1: n} for n in (1, 2, 3)}    # n+1 -> n
t12 = {1: 2, 2: 1}; t13 = {1: 3, 2: 2, 3: 1}
lhs = [comp(t12, K[2], t13, delta[2])(x) for x in (1, 2)]
rhs = [comp(delta[1], K[1])(x) for x in (1, 2)]
say('B6.1 (1 2)K_2(1 3)delta_2 =', lhs, ' delta_1 K_1 =', rhs, ' K_n delta_n = id:',
    all(comp(K[n], delta[n])(i) == i for n in (1, 2, 3) for i in range(1, n + 1)))
# countermodel: E_1={0}, E_n={0,1} (n>=2), permutations trivial; p_1 unique, d_1 = inclusion of 0, p_n=d_n=id
p1 = {0: 0, 1: 0}; d1 = {0: 0}; idE = {0: 0, 1: 1}
say('B6.1 countermodel: p_n d_n = id:', comp(p1, d1)(0) == 0 and all(comp(idE, idE)(x) == x for x in (0, 1)),
    '; image of (B6.1.1): left', [comp(idE, idE)(x) for x in (0, 1)], 'right', [comp(d1, p1)(x) for x in (0, 1)])
X = (0, 1, 2)
pmap = lambda v: (v[0],); dmap = lambda v: (v[0], v[0]); qmap = lambda v: (v[0], v[1]); emap = lambda v: (v[1], v[0], v[0])
sig = lambda v: (v[1], v[0]); rho = lambda v: (v[1], v[2], v[0]); s1 = lambda v: (v[0], v[2], v[1]); s3 = lambda v: (v[1], v[0], v[2])
def eq(f, g, m):
    return all(f(v) == g(v) for v in product(X, repeat=m))
c = lambda *fs: (lambda v: comp_t(fs, v))
def comp_t(fs, v):
    for f in reversed(fs):
        v = f(v)
    return v
ident = lambda v: v
S3 = [ident, rho, c(rho, rho), s1, c(rho, s1), c(rho, rho, s1)]
rels = {'pd=1': eq(c(pmap, dmap), ident, 1), 'sigma d=d': eq(c(sig, dmap), dmap, 1), 'qe=sigma': eq(c(qmap, emap), sig, 2),
        'q rho e=dp': eq(c(qmap, rho, emap), c(dmap, pmap), 2), 'q rho^2 e=1': eq(c(qmap, rho, rho, emap), ident, 2),
        'sigma1 e=e': eq(c(s1, emap), emap, 2), 'q sigma3=sigma q': eq(c(qmap, s3), c(sig, qmap), 3),
        'g e d=e d (all g)': all(eq(c(g, emap, dmap), c(emap, dmap), 1) for g in S3),
        'p q sigma1=p q': eq(c(pmap, qmap, s1), c(pmap, qmap), 3)}
say('B6.3 corrected relations true in coordinates:', all(rels.values()), [k for k, v in rels.items() if not v])
say('B6.3 alternatives: sigma3 e=e', eq(c(s3, emap), emap, 2), '; p q sigma3 = p q', eq(c(pmap, qmap, s3), c(pmap, qmap), 3))
# generation: index maps a (coordinate map v -> (v[a(1)],...)) ; composite of coordinate maps f.g has index a_g o a_f
gens = {('E1', 'E0'): [(0,)], ('E0', 'E1'): [(0, 0)], ('E2', 'E1'): [(0, 1)], ('E1', 'E2'): [(1, 0, 0)],
        ('E1', 'E1'): [(1, 0)], ('E2', 'E2'): [(1, 2, 0), (0, 2, 1)]}
size = {'E0': 1, 'E1': 2, 'E2': 3}
maps = {(a, a): {tuple(range(size[a]))} for a in size}
for k, v in gens.items():
    maps.setdefault(k, set()).update(v)
changed = True
while changed:
    changed = False
    for (a, b), F in list(maps.items()):
        for (b2, cc), G in list(maps.items()):
            if b2 != b:
                continue
            for f_ in list(F):
                for g_ in list(G):
                    h = tuple(f_[g_[i]] for i in range(size[cc]))     # index of g.f (first f: a->b, then g: b->c)
                    if h not in maps.setdefault((a, cc), set()):
                        maps[(a, cc)].add(h); changed = True
total = sum(len(v) for v in maps.values())
say('B6.3 maps generated among E0,E1,E2:', total, 'matrix', [[len(maps.get((a, b), ())) for b in ('E0', 'E1', 'E2')] for a in ('E0', 'E1', 'E2')])

# ---------------------------------------------------------------- 5. 151/060, the aside after (12)
def aside(Xs, order, i, j, k):
    lt = lambda a, b: (a, b) in order
    Rjk = set().union(*[Xs[l] for l in Xs if lt(l, k) and not Xs[l] >= Xs[j]])
    Sjk = set().union(*[Xs[l] for l in Xs if (l == j or lt(j, l)) and lt(l, k)])
    dot = lambda a: set().union(*[Xs[h] for h in Xs if lt(h, a)])
    return Rjk & Sjk, dot(i), dot(j)
chain = {0: {0}, 1: {0, 1}, 2: {0, 1, 2}}
say('151/060 chain (i,j,k)=(0,1,2): R&S, dotX_i, dotX_j =', aside(chain, {(0, 1), (0, 2), (1, 2)}, 0, 1, 2))
# our STUDY example in R^2: m origin, l x-axis, j the point (0,5), l2 y-axis, all below k = R^2 (points as labels)
Xs = {'m': {'O'}, 'l': {'O', 'x'}, 'j': {'P'}, 'l2': {'O', 'y', 'P'}, 'k': {'O', 'x', 'y', 'P', 'z'}}
order = {('m', 'l'), ('m', 'l2'), ('j', 'l2'), ('m', 'k'), ('l', 'k'), ('j', 'k'), ('l2', 'k')}
say('151/060 STUDY example (j point, k plane): R&S, dotX_j =', aside(Xs, order, 'j', 'j', 'k')[0], aside(Xs, order, 'j', 'j', 'k')[2])
print('\n'.join(out))
