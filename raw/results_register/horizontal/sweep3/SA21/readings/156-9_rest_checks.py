# Checks for the page-by-page reading of 156-9 (reader C: Claude Opus 5.5 at effort max, sub-agent of a6d42bf6fe2b0d8a8),
# horizontal sweep 3, round 2, 19 Nov 2026.  Run: python -I -B 156-9_rest_checks.py [maxn]
import itertools, sys
MAXN = int(sys.argv[1]) if len(sys.argv) > 1 else 5

# ---------- finite posets ----------
def posets(n):
    """all naturally labelled posets on range(n) (i<j whenever i<j in the order), as sets of strict pairs; connected only"""
    pairs = [(i, j) for i in range(n) for j in range(n) if i < j]
    seen = set()
    for k in range(len(pairs) + 1):
        for rel in itertools.combinations(pairs, k):
            R = set(rel)
            if any((a, b) in R and (b, c) in R and (a, c) not in R for a in range(n) for b in range(n) for c in range(n)):
                continue
            fz = frozenset(R)
            if fz in seen: continue
            seen.add(fz)
            # connectivity of the comparability graph
            comp = {0}; ch = True
            while ch:
                ch = False
                for (a, b) in R:
                    if (a in comp) != (b in comp): comp |= {a, b}; ch = True
            if len(comp) == n: yield R

# ---------- the magasin of an ordered set, with the infinite intervals (156-8/90-92, 156-9/5-12) ----------
def build(n, lt):
    le = lambda a, b: a == b or (a, b) in lt
    mins = [a for a in range(n) if not any((b, a) in lt for b in range(n))]
    maxs = [a for a in range(n) if not any((a, b) in lt for b in range(n))]
    M = [('P', x) for x in range(n)] + [('I', a, b) for (a, b) in sorted(lt)]
    Mh = M + [('L', a) for a in range(n) if a not in mins] + [('R', a) for a in range(n) if a not in maxs]
    delta = lambda X: {X[1]} if X[0] in 'PLR' else {X[1], X[2]}
    def less(X, Y):  # positional order of 156-9/6 and 11
        if X == Y or Y[0] == 'L' or X[0] == 'R': return False
        return all(le(a, b) for a in delta(X) for b in delta(Y))
    def oo(X, Y):  # internal refinement X <<o Y
        if X == Y: return True
        t = (X[0], Y[0])
        if t == ('P', 'I'): return (Y[1], X[1]) in lt and (X[1], Y[2]) in lt
        if t == ('I', 'I'): return le(Y[1], X[1]) and le(X[2], Y[2])
        if Y[0] == 'L':
            if X[0] == 'L': return le(X[1], Y[1])
            if X[0] in 'PI': return X != ('P', Y[1]) and all(le(a, Y[1]) for a in delta(X))
            return False
        if Y[0] == 'R':
            if X[0] == 'R': return le(Y[1], X[1])
            if X[0] in 'PI': return X != ('P', Y[1]) and all(le(Y[1], a) for a in delta(X))
            return False
        return False
    circ = lambda X, Y: less(X, Y) or less(Y, X)
    inc = lambda X, Y: X != Y and X[0] == 'P' and Y[0] == 'I' and X[1] in (Y[1], Y[2])  # strict incidence
    return M, Mh, delta, less, oo, circ, inc, mins, maxs, le

def cosupp(M, circ, A): return frozenset(Z for Z in M if all(circ(Z, X) for X in A))
def supp(M, circ, A): return cosupp(M, circ, cosupp(M, circ, A))
def omb(M, oo, Phi): return frozenset(Z for Z in M if any(oo(Z, X) for X in Phi))

def interstitial(T, n, lt, mins, maxs):
    T = sorted(T, key=lambda t: sum((u, t) in lt for u in range(n)))
    out = [('P', t) for t in T] + [('I', T[i], T[i + 1]) for i in range(len(T) - 1)]
    if T[0] not in mins: out.append(('L', T[0]))
    if T[-1] not in maxs: out.append(('R', T[-1]))
    return frozenset(out)

def is_chain_L(T, lt):
    return all(a == b or (a, b) in lt or (b, a) in lt for a in T for b in T)

def polygons(n, lt, Mh, delta, less, mins, maxs):
    """nonempty chains Phi of (Mh,<) made of interstitial strata of T = delta(Phi), each t in T in Phi or an end of a member"""
    out = []
    els = list(Mh)
    def rec(chain, start):
        if chain:
            T = set().union(*(delta(X) for X in chain))
            if is_chain_L(T, lt):
                hat = interstitial(T, n, lt, mins, maxs)
                if all(X in hat for X in chain) and all(('P', t) in chain or any(t in delta(X) for X in chain if X[0] != 'P') for t in T):
                    out.append((frozenset(chain), frozenset(T), hat))
        for i in range(start, len(els)):
            Y = els[i]
            if all(less(X, Y) or less(Y, X) for X in chain): rec(chain + [Y], i + 1)
    rec([], 0)
    return out

def part_A(maxn):
    stats = dict(posets=0, polygons=0, th_fail=0, cor1_fail_hyp=0, cor1_fail_nohyp=0, cor1_cases_hyp=0, cor1_cases_nohyp=0,
                 omb_noninj=0, figs=0, supp1_fail=0, q3_fail=0, q3_cases=0)
    examples = {}
    for n in range(2, maxn + 1):
        for lt in posets(n):
            stats['posets'] += 1
            M, Mh, delta, less, oo, circ, inc, mins, maxs, le = build(n, lt)
            hyp = all(len(mins) == 1 or True for _ in [0])
            hyp = (len(mins) == 1) and (len(maxs) == 1) or (all(any((m, x) in lt or m == x for x in range(n)) for m in mins) and False)
            # Hyp of 156-9/16 (156-8/100): every minimal element is least and every maximal element is greatest
            hyp = len(mins) == 1 and len(maxs) == 1
            polys = polygons(n, lt, Mh, delta, less, mins, maxs)
            stats['polygons'] += len(polys)
            ombs = {}
            for (Phi, T, hat) in polys:
                star = hat - Phi
                cs = cosupp(M, circ, Phi)
                if cs != omb(M, oo, star):
                    stats['th_fail'] += 1; examples.setdefault('th', (n, sorted(lt), sorted(Phi)))
                o = omb(M, oo, Phi)
                ombs.setdefault(o, []).append(Phi)
                if star:  # Cor 1: supp(Phi) = Omb(Phi**), Phi** the complement of Phi* in its own flag
                    T2 = set().union(*(delta(X) for X in star))
                    hat2 = interstitial(T2, n, lt, mins, maxs)
                    star2 = hat2 - star
                    ok = supp(M, circ, Phi) == omb(M, oo, star2)
                    key = 'hyp' if hyp else 'nohyp'
                    stats['cor1_cases_' + key] += 1
                    if not ok:
                        stats['cor1_fail_' + key] += 1; examples.setdefault('cor1_' + key, (n, sorted(lt), sorted(Phi)))
            stats['omb_noninj'] += sum(1 for v in ombs.values() if len(v) > 1)
            fin = {}
            for (Phi, T, hat) in polys:
                if all(X[0] in 'PI' for X in Phi): fin.setdefault(omb(M, oo, Phi), []).append(Phi)
            nf = sum(1 for v in fin.values() if len(v) > 1)
            stats['omb_noninj_finite'] = stats.get('omb_noninj_finite', 0) + nf
            if nf: examples.setdefault('omb_finite', (n, sorted(lt), [sorted(v) for v in fin.values() if len(v) > 1][:1]))
            # figures: finite chains of (M,<) closed under incidence; Axiome supp 1 (156-8/88)
            figs = []
            def rec(chain, start):
                if chain and all(Y in chain for X in chain for Y in M if inc(Y, X)): figs.append(frozenset(chain))
                for i in range(start, len(M)):
                    Y = M[i]
                    if all(circ(X, Y) for X in chain): rec(chain + [Y], i + 1)
            rec([], 0)
            stats['figs'] += len(figs)
            for F in figs:
                sF = supp(M, circ, F)
                for k in range(len(F) + 1):
                    for P in itertools.combinations(sorted(F), k):
                        if sF & cosupp(M, circ, P) != supp(M, circ, F - set(P)):
                            stats['supp1_fail'] += 1; examples.setdefault('supp1', (n, sorted(lt), sorted(F), P))
            # Question of 156-9/3: for a lieu P_x, is there X =/= P_x with 0 =/= supp(X) c supp(P_x)?
            for x in range(n):
                sx = supp(M, circ, [('P', x)])
                stats['q3_cases'] += 1
                bad = [X for X in M if X != ('P', x) and supp(M, circ, [X]) and supp(M, circ, [X]) <= sx]
                if bad:
                    stats['q3_fail'] += 1; examples.setdefault('q3', (n, sorted(lt), x, bad[:3]))
    return stats, examples

# ---------- disjoncteurs: polarity lattices of graphs ----------
def closed_sets(V, adj):
    cos = lambda A: frozenset(v for v in V if all(adj[v][a] for a in A))
    cl = set()
    for k in range(len(V) + 1):
        for A in itertools.combinations(V, k):
            cl.add(cos(cos(A)))
    return cl, cos

def orthomodular(cl, cos, V):
    full = frozenset(V)
    join = lambda a, b: cos(cos(a | b))
    for a in cl:
        for b in cl:
            if a <= b and join(a, b & cos(a)) != b: return False
    return True

def has_induced_P4(V, adj):
    for q in itertools.permutations(V, 4):
        a, b, c, d = q
        if adj[a][b] and adj[b][c] and adj[c][d] and not adj[a][c] and not adj[b][d] and not adj[a][d]: return True
    return False

def part_B(maxn):
    res = {}
    for n in range(1, maxn + 1):
        V = list(range(n)); pairs = list(itertools.combinations(V, 2)); cnt = {}
        for mask in range(1 << len(pairs)):
            adj = [[False] * n for _ in V]
            for i, (a, b) in enumerate(pairs):
                if mask >> i & 1: adj[a][b] = adj[b][a] = True
            cl, cos = closed_sets(V, adj)
            key = (orthomodular(cl, cos, V), not has_induced_P4(V, adj))
            cnt[key] = cnt.get(key, 0) + 1
        res[n] = cnt
    return res

def comparability(V, adj):
    # transitive orientability by brute force (small n)
    E = [(a, b) for a in V for b in V if a < b and adj[a][b]]
    for bits in range(1 << len(E)):
        R = set()
        for i, (a, b) in enumerate(E): R.add((a, b) if bits >> i & 1 else (b, a))
        if all((a, c) in R for (a, b) in R for (b2, c) in R if b == b2): return True
    return False

def oml_with_p4(n):
    V = list(range(n)); pairs = list(itertools.combinations(V, 2)); out = []
    for mask in range(1 << len(pairs)):
        adj = [[False] * n for _ in V]
        for i, (a, b) in enumerate(pairs):
            if mask >> i & 1: adj[a][b] = adj[b][a] = True
        if not has_induced_P4(V, adj): continue
        cl, cos = closed_sets(V, adj)
        if orthomodular(cl, cos, V):
            out.append((tuple(p for i, p in enumerate(pairs) if mask >> i & 1), len(cl), comparability(V, adj)))
    return out

def part_C():
    """Prop 4 of 156-9/95-97 and Lemma 1 of 156-9/72, Cor 1 of 156-9/84, on small disjoncteurs"""
    import random
    random.seed(1986)
    out = dict(trials=0, iv_vs_iii=0, iv_vs_cont=0, a_only_not_enough=0, cor1_ii_not_i=0, cor1_cases=0)
    def rand_graph(n):
        adj = [[False] * n for _ in range(n)]
        for a, b in itertools.combinations(range(n), 2):
            if random.random() < 0.5: adj[a][b] = adj[b][a] = True
        return adj
    for _ in range(3000):
        n, m = random.randint(1, 4), random.randint(1, 4)
        E, Ep = list(range(n)), list(range(m))
        adj, adjp = rand_graph(n), rand_graph(m)
        cl, cos = closed_sets(E, adj); clp, cosp = closed_sets(Ep, adjp)
        sup = lambda A: cos(cos(A)); supp_ = lambda A: cosp(cosp(A))
        alpha = {x: frozenset(y for y in Ep if random.random() < 0.4) for x in E}
        abar = lambda A: frozenset().union(*[alpha[x] for x in A]) if A else frozenset()
        astar = lambda S: supp_(abar(S))
        iii = all(frozenset(x for x in E if supp_(alpha[x]) <= Sp) in cl for Sp in clp)
        iv = all(frozenset(x for x in E if all(adjp[y][xp] for y in alpha[x])) in cl for xp in Ep)
        cont = all(astar(sup(frozenset(A))) == supp_(abar(frozenset(A))) for k in range(n + 1) for A in itertools.combinations(E, k))
        join = lambda a, b: sup(a | b); joinp = lambda a, b: supp_(a | b)
        a_sup = all(astar(join(s, t)) == joinp(astar(s), astar(t)) for s in cl for t in cl) and astar(frozenset(sup(frozenset()))) == supp_(frozenset())
        b_cond = all(astar(sup(frozenset([x]))) == supp_(alpha[x]) for x in E)
        out['trials'] += 1
        out['iv_vs_iii'] += iv != iii
        out['iv_vs_cont'] += iv != cont
        out['a_only_not_enough'] += (a_sup and not b_cond and not cont)
        if (a_sup and b_cond) != cont: out.setdefault('ii_vs_cont_mismatch', 0); out['ii_vs_cont_mismatch'] = out.get('ii_vs_cont_mismatch', 0) + 1
    # Cor 1 of 156-9/84: does injectivity of S -> S n E' (ii) imply density (i)?  exhaustive for graphs on <= 5 vertices
    for n in range(1, 6):
        V = list(range(n)); pairs = list(itertools.combinations(V, 2))
        for mask in range(1 << len(pairs)):
            adj = [[False] * n for _ in V]
            for i, (a, b) in enumerate(pairs):
                if mask >> i & 1: adj[a][b] = adj[b][a] = True
            cl, cos = closed_sets(V, adj)
            sigma = {x: cos(cos([x])) for x in V}
            for k in range(1, n + 1):
                for Ep in itertools.combinations(V, k):
                    out['cor1_cases'] += 1
                    inj = len({S & frozenset(Ep) for S in cl}) == len(cl)
                    dense = all(S == cos(cos(frozenset().union(*[sigma[x] for x in Ep if sigma[x] <= S]) if any(sigma[x] <= S for x in Ep) else frozenset())) for S in cl)
                    if inj and not dense: out['cor1_ii_not_i'] += 1
    return out

if __name__ == '__main__':
    sA, ex = part_A(MAXN)
    print('A. magasins of connected finite ordered sets, n <=', MAXN, ':', sA)
    for k, v in ex.items(): print('   example', k, v)
    print('B. polarity lattices of all labelled graphs: counts of (orthomodular, P4-free):', part_B(6 if MAXN >= 5 else 5))
    ex5 = oml_with_p4(5)
    print('B2. graphs on 5 vertices with an induced P4 and an orthomodular polarity lattice:', len(ex5), '; comparability graphs among them:', sum(1 for e in ex5 if e[2]), '; first:', ex5[:3])
    print('C. disjunctive correspondences and density:', part_C())
