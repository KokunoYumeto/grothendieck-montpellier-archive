# Second set of independent checks for the intake of RESEARCH_SA21 (19 Nov 2026).
# Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8. Usage: python -I -B INTAKE_RESEARCH_SA21_20261119_checks2.py
# 1. SA21-A11: the ten-element set model of 156-9 scan 113.  2. SA21-C (L4): the torus with a formal top cell.
# 3. SA21-B-K42/K43: C4 components of the multistrates of Fig(L), |L| = 1..4, using the definitions of our reader A's
#    156-5_sorite_checks.py (its definitions only are executed here).
from itertools import combinations, product
from collections import defaultdict
import os

# ---------------------------------------------------------------- 1. the ten-element ortholattice
I = ('i', "i'", 'j', 'k')
T = [frozenset(E) for r in range(5) for E in combinations(I, r) if ('i' in E) == ("i'" in E)]
T += [frozenset({'i'}), frozenset({"i'", 'j', 'k'})]
full = frozenset(I)
comp = lambda E: full - E
le = lambda a, b: a <= b
def meet(a, b):
    lb = [x for x in T if x <= a and x <= b]
    g = [x for x in lb if all(y <= x for y in lb)]
    return g[0] if len(g) == 1 else None
def join(a, b):
    ub = [x for x in T if a <= x and b <= x]
    l = [x for x in ub if all(x <= y for y in ub)]
    return l[0] if len(l) == 1 else None
lattice = all(meet(a, b) is not None and join(a, b) is not None for a in T for b in T)
ortho = all(comp(a) in T and meet(a, comp(a)) == frozenset() and join(a, comp(a)) == full for a in T)
covers = [(a, b) for a in T for b in T if a < b and not any(a < c < b for c in T)]
oml_fail = [(sorted(a), sorted(b)) for a in T for b in T if a < b and join(a, meet(b, comp(a))) != b]
# the transcribed reading "j, i' not in E" instead of "i, i' not in E"
T2 = [frozenset(E) for r in range(5) for E in combinations(I, r) if {'i', "i'"} <= set(E) or ('j' not in E and "i'" not in E)]
T2 = set(T2) | {frozenset({'i'}), frozenset({"i'", 'j', 'k'})}
print('SA21-A11: %d elements, lattice %s, orthocomplemented %s, covers %d, orthomodular failures %d (e.g. %s); '
      'with the transcribed second clause "j, i\' notin E" the family has %d elements'
      % (len(T), lattice, ortho, len(covers), len(oml_fail), oml_fail[0] if oml_fail else None, len(T2)))

# ---------------------------------------------------------------- 2. torus with a formal top cell (L4)
m = 3
V = [('v', a, b) for a in range(m) for b in range(m)]
E = [('h', a, b) for a in range(m) for b in range(m)] + [('w', a, b) for a in range(m) for b in range(m)]
F = [('f', a, b) for a in range(m) for b in range(m)]
def ends(e):
    t, a, b = e
    return [('v', a, b), ('v', (a + 1) % m, b)] if t == 'h' else [('v', a, b), ('v', a, (b + 1) % m)]
def fedges(f):
    _, a, b = f
    return [('h', a, b), ('h', a, (b + 1) % m), ('w', a, b), ('w', (a + 1) % m, b)]
TOP = ('T',)
cells = V + E + F + [TOP]
below = {c: set() for c in cells}           # covering relation: c covers d
for e in E: below[e] = set(ends(e))
for f in F: below[f] = set(fedges(f))
below[TOP] = set(F)
def interval_len2(x, z):
    return [y for y in cells if y in below[z] and x in below[y]]
diam = all(len(interval_len2(x, z)) == 2 for z in cells for y in below[z] for x in below[y])
# signs: vertices -> edges: [v:e] = -1 at the start, +1 at the end; edges -> faces by the boundary orientation;
# faces -> TOP: +1 (the torus is orientable)
def sgn(d, c):
    if c[0] in 'hw':
        return -1 if d == ends(c)[0] else 1
    if c[0] == 'f':
        _, a, b = c
        return {('h', a, b): 1, ('w', (a + 1) % m, b): 1, ('h', a, (b + 1) % m): -1, ('w', a, b): -1}[d]
    return 1
signs = all(sum(sgn(x, y) * sgn(y, z) for y in interval_len2(x, z)) == 0
            for z in cells for y0 in below[z] for x in below[y0])
bound = V + E + F                           # boundary of TOP
adj = defaultdict(set)
for c in bound:
    for d in below[c]:
        adj[c].add(d); adj[d].add(c)
seen, st = {V[0]}, [V[0]]
while st:
    x = st.pop()
    for y in adj[x]:
        if y not in seen: seen.add(y); st.append(y)
print('L4 torus (3x3 grid, %d cells + formal top): every length-2 interval a diamond %s, signs with zero diamond sums %s, '
      'boundary of the top cell connected %s, its Euler characteristic %d (a sphere would give 2)'
      % (len(bound), diam, signs, len(seen) == len(bound), len(V) - len(E) + len(F)))

# ---------------------------------------------------------------- 3. C4 components of the multistrates of Fig(L)
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'readings', '156-5_sorite_checks.py'), encoding='utf-8').read()
g = {}
exec(src.split('# ---- Prop 1')[0], g)
exec('def closed_in(P, F): return P <= F and all(B in P for A in P for B in F if sub(B, A))\n'
     'def le(P, F): return closed_in(P, F)\n', g)
for n in (1, 2, 3, 4):
    A_ = [Fm for Fm in g['fams'](n) if g['admissible'](Fm, n)]
    M = [Fm for Fm in A_ if Fm and any(all(g['sub'](B, X) for B in Fm) for X in Fm)]
    par = {X: X for X in M}
    def find(x):
        while par[x] != x: x = par[x]
        return x
    for X in M:
        for Y in M:
            if g['le'](X, Y): par[find(X)] = find(Y)
    comps = defaultdict(list)
    for X in M: comps[find(X)].append(X)
    sizes = sorted(len(c) for c in comps.values())
    print('C4 |L|=%d: %d multistrates, %d incidence components, sizes %s (run: 1 + |L| + 1 for |L| >= 3)'
          % (n, len(M), len(comps), sizes))

# ---------------------------------------------------------------- 4. Sumner's Dacey-graph condition on the crown
# Sumner 1974, p. 492: for every maximal clique E and distinct vertices u, v: E subset N(u) u N(v) => u ~ v.
crown = {(0, 2), (0, 3), (1, 2), (1, 3)}
Ls = lambda a, b: (a, b) in crown
Le = lambda a, b: a == b or Ls(a, b)
Ec = [('P', a) for a in range(4)] + [('I', a, b) for a, b in sorted(crown)]
endp = {e: ({e[1]} if e[0] == 'P' else {e[1], e[2]}) for e in Ec}
lt = lambda U, W: U != W and all(Le(u, w) for u in endp[U] for w in endp[W])
adjc = lambda U, W: lt(U, W) or lt(W, U)
Nb = {x: {y for y in Ec if adjc(x, y)} for x in Ec}
cliques = []
def bk(R, Pp, X):
    if not Pp and not X:
        cliques.append(R); return
    for v in list(Pp):
        bk(R | {v}, Pp & Nb[v], X & Nb[v]); Pp = Pp - {v}; X = X | {v}
bk(set(), set(Ec), set())
viol = [(u, v) for C in cliques for u in Ec for v in Ec if u != v and C <= (Nb[u] | Nb[v]) and not adjc(u, v)]
print('Sumner condition on M(crown): %d maximal cliques, violations %d' % (len(cliques), len(viol)))
