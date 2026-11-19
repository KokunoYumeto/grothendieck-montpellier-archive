"""PGL_2(F_5) on the 6 points of P^1(F_5): stabilizers behind 157 A'), B'), C') (bi-icosahedron + vertex / edge / biface).
Claude Opus 5.5 at effort max, reader 119_144-161_276-281, horizontal sweep 3."""
import itertools as it
from collections import Counter
P = list(range(5)) + ['inf']
def mob(a, b, c, d, x):
    if x == 'inf':
        return 'inf' if c == 0 else a * pow(c, 3, 5) % 5
    den = (c * x + d) % 5
    if den == 0: return 'inf'
    return (a * x + b) * pow(den, 3, 5) % 5
G = set()
for a, b, c, d in it.product(range(5), repeat=4):
    if (a * d - b * c) % 5:
        G.add(tuple(P.index(mob(a, b, c, d, x)) for x in P))
def sign(p):
    n = len(p); seen = [0] * n; cyc = 0
    for i in range(n):
        if not seen[i]:
            cyc += 1; j = i
            while not seen[j]: seen[j] = 1; j = p[j]
    return (-1) ** (n - cyc)
A5 = {g for g in G if sign(g) == 1}
print("|PGL2(5)| =", len(G), " |PSL2(5)| (even part) =", len(A5))
inf = 5
st_pt = [g for g in G if g[inf] == inf]
print("A') stabilizer of a point:", len(st_pt), "; in A5:", sum(1 for g in st_pt if g in A5))
duad = frozenset([0, inf])
st_du = [g for g in G if frozenset(g[x] for x in duad) == duad]
rest = [1, 2, 3, 4]
acts = {tuple(g[x] for x in rest) for g in st_du}
print("B') stabilizer of a duad:", len(st_du), "; faithful on the other 4 points:", len(acts) == len(st_du),
      "; preserved pairings of {1,2,3,4}:",
      [p for p in [((1, 4), (2, 3)), ((1, 2), (3, 4)), ((1, 3), (2, 4))]
       if all(frozenset(frozenset(g[x] for x in q) for q in p) == frozenset(frozenset(q) for q in p) for g in st_du)])
swap = Counter((frozenset(g[x] for x in [0]) == frozenset([0]), sign(tuple(rest.index(g[x]) for x in rest))) for g in st_du)
print("    (fixes 0 ?, sign on the square) counts:", dict(swap))
trip = [frozenset(t) for t in it.combinations(range(6), 3)]
orbA5 = []
seen = set()
for t in trip:
    if t in seen: continue
    o = {frozenset(g[x] for x in t) for g in A5}; seen |= o; orbA5.append(o)
print("C') A5-orbits on the 20 triples:", [len(o) for o in orbA5],
      "; complement maps each A5-orbit to the other:", all((frozenset(range(6)) - t) not in o for o in orbA5 for t in o))
T = next(iter(orbA5[0]))
st_dt = [g for g in G if frozenset(g[x] for x in T) in (T, frozenset(range(6)) - T)]
st_t = [g for g in G if frozenset(g[x] for x in T) == T]
print("    stabilizer of the ditriad {T, T^c} (a 'biface'):", len(st_dt), "; of T alone:", len(st_t),
      "; acting on T as:", len({tuple(sorted((x, g[x]) for x in T)) for g in st_t}), "permutations")
