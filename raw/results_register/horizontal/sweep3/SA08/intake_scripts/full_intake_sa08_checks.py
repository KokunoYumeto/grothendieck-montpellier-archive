# Computations for the full intake of RESEARCH_SA08 (final 20261119T1027Z), 22 Nov 2026.
# Claude Opus 5.5 at effort max, agent a34c04448e8299803. Standard library only; runs no program of the return.
import itertools, math, sys
sys.stdout.reconfigure(encoding='utf-8')
C = math.comb

print('B-12 (B-15): gcd(i+1, j+1) divides C(i+j, i) for 1 <= i, j <= 150:',
      all(C(i + j, i) % math.gcd(i + 1, j + 1) == 0 for i in range(1, 151) for j in range(1, 151)))

ok_e = ok_f = True; n = 0
for a in range(2, 21):
    for b in range(2, 21):
        w = a + b
        for s in range(a):
            lhs = C(a, s) * C(w, a) - C(w, s) * C(w - s - 1, a - s)
            rhs = C(w, s) * C(w - s - 1, a - s - 1)
            ok_e &= (lhs == rhs); n += 1
        ok_f &= (sum((-1)**s * C(w, s) * C(w - s - 1, a - s - 1) for s in range(a)) == (-1)**(a - 1))
print('D-027 (D-27e): I_s identity for 2 <= a, b <= 20, all s < a:', ok_e, '(', n, 'cases ); (D-27f) alternating sum = (-1)^(a-1):', ok_f)

# B-09: the 6-vertex RP^2 of the run
tri = [(0,1,2),(0,1,3),(0,2,4),(0,3,5),(0,4,5),(1,2,5),(1,3,4),(1,4,5),(2,3,4),(2,3,5)]
edges = sorted({e for t in tri for e in itertools.combinations(t, 2)})
idx = {e: i for i, e in enumerate(edges)}
inc = {e: sum(1 for t in tri if set(e) <= set(t)) for e in edges}
links_ok = True
for v in range(6):
    lk = [tuple(x for x in t if x != v) for t in tri if v in t]
    deg = {}
    for e in lk:
        for x in e:
            deg[x] = deg.get(x, 0) + 1
    links_ok &= (len(lk) == 5 and all(d == 2 for d in deg.values()) and len(deg) == 5)


def is_cocycle(c):
    return all((c[idx[(t[0], t[1])]] + c[idx[(t[1], t[2])]] + c[idx[(t[0], t[2])]]) % 2 == 0 for t in tri)


cocycles = [c for c in itertools.product((0, 1), repeat=len(edges)) if is_cocycle(c)]
cobound = {tuple((f[a] + f[b]) % 2 for (a, b) in edges) for f in itertools.product((0, 1), repeat=6)}
sq = [c for c in cocycles if sum(c[idx[(t[0], t[1])]] * c[idx[(t[1], t[2])]] for t in tri) % 2 == 1]
print('B-09: edges', len(edges), '; every edge in 2 triangles:', all(v == 2 for v in inc.values()),
      '; vertex links 5-cycles:', links_ok, '; cocycles', len(cocycles), '; coboundaries', len(cobound),
      '; cocycles with AW square 1 on the sum of triangles:', len(sq))
