# Intake of RESEARCH_SA10 (19 Nov 2026), Claude Opus 5.5 at effort max (agent a6d42bf6fe2b0d8a8).
# Rational homology of the homotopy colimit of the stone diagrams of A1.3 (X = C, X_0 = {0} < X_1 = R < X_2 = C),
# with each stone replaced by its homotopy type: V12 = germ_R C minus 0 is a circle around 0 on which the rays
# (r+, r-) and the half-strips (u, d) sit as four vertices in the cyclic order r+, u, r-, d; the other stones are
# finite sets. Bousfield-Kan double complex over the poset of stones (inclusions). C itself is contractible.
# Usage: python -I -B INTAKE_RESEARCH_SA10_20261119_hocolim.py
from fractions import Fraction
from itertools import combinations

CIRCLE = (['r+', 'u', 'r-', 'd'], [('r+', 'u'), ('u', 'r-'), ('r-', 'd'), ('d', 'r+')])
SP = {  # stone: (vertices, edges)
    'S0': (['o'], []), 'S1': (['p', 'n'], []), 'S2': (['U', 'D'], []), 'V01': (['o'], []),
    'V01*': (['p', 'n'], []), 'V12': CIRCLE, 'V12*': (['U', 'D'], []), 'V02': (['o'], []), 'V02*': (['U', 'D'], [])}
VMAP = {  # vertex maps along the inclusions (the 14 of A1.3; edges are mapped vertex-wise)
    ('S0', 'V01'): {'o': 'o'}, ('S0', 'V02'): {'o': 'o'}, ('S1', 'V12'): {'p': 'r+', 'n': 'r-'},
    ('V01', 'V02'): {'o': 'o'}, ('V01*', 'S1'): {'p': 'p', 'n': 'n'}, ('V01*', 'V01'): {'p': 'o', 'n': 'o'},
    ('V01*', 'V02'): {'p': 'o', 'n': 'o'}, ('V01*', 'V12'): {'p': 'r+', 'n': 'r-'},
    ('V02*', 'S2'): {'U': 'U', 'D': 'D'}, ('V02*', 'V02'): {'U': 'o', 'D': 'o'},
    ('V02*', 'V12'): {'U': 'u', 'D': 'd'}, ('V02*', 'V12*'): {'U': 'U', 'D': 'D'},
    ('V12*', 'S2'): {'U': 'U', 'D': 'D'}, ('V12*', 'V12'): {'U': 'u', 'D': 'd'}}

def rank(rows, ncols):
    m = [[Fraction(x) for x in r] for r in rows]
    rk, col = 0, 0
    while rk < len(m) and col < ncols:
        piv = next((i for i in range(rk, len(m)) if m[i][col] != 0), None)
        if piv is None:
            col += 1; continue
        m[rk], m[piv] = m[piv], m[rk]
        for i in range(len(m)):
            if i != rk and m[i][col] != 0:
                f = m[i][col] / m[rk][col]
                m[i] = [a - f * b for a, b in zip(m[i], m[rk])]
        rk += 1; col += 1
    return rk

def homology(stones):
    less = {(a, b) for a, b in VMAP if a in stones and b in stones}
    chains = [(s,) for s in stones]
    k = 1
    while True:
        new = [c + (s,) for c in chains if len(c) == k for s in stones if (c[-1], s) in less]
        if not new:
            break
        chains += new; k += 1
    def mapcell(cell, a, b):          # image of a vertex or an edge of F(a) in F(b)
        m = VMAP[(a, b)]
        if isinstance(cell, tuple):
            x, y = m[cell[0]], m[cell[1]]
            return None if x == y else ((x, y) if (x, y) in SP[b][1] else (y, x), 1 if (x, y) in SP[b][1] else -1)
        return (m[cell], 1)
    gens = {}                          # total degree -> list of (chain, cell)
    for c in chains:
        verts, edges = SP[c[0]]
        for v in verts:
            gens.setdefault(len(c) - 1, []).append((c, v))
        for e in edges:
            gens.setdefault(len(c), []).append((c, e))
    index = {n: {g: i for i, g in enumerate(gs)} for n, gs in gens.items()}
    def boundary(n):
        rows = []
        for (c, cell) in gens.get(n, []):
            vec = [0] * len(gens.get(n - 1, []))
            kk = len(c) - 1
            for i in range(len(c)):                # nerve faces
                if kk == 0:
                    break
                if i == 0:
                    img = mapcell(cell, c[0], c[1])
                    if img is None:
                        continue
                    cell2, sgn = img
                    g = (c[1:], cell2)
                else:
                    sgn, g = 1, (c[:i] + c[i + 1:], cell)
                vec[index[n - 1][g]] += (-1) ** i * sgn
            if isinstance(cell, tuple):            # the edge boundary, sign (-1)^k
                for v, s in ((cell[1], 1), (cell[0], -1)):
                    vec[index[n - 1][(c, v)]] += (-1) ** kk * s
            rows.append(vec)
        return rows
    top = max(gens)
    ranks = {n: rank(boundary(n), len(gens.get(n - 1, []))) if n > 0 else 0 for n in range(top + 2)}
    return [len(gens.get(n, [])) - ranks[n] - ranks.get(n + 1, 0) for n in range(top + 1)]

allp = list(SP)
succ = ['S0', 'S1', 'S2', 'V01', 'V01*', 'V12', 'V12*']
print('all pair and triple stones: rational Betti numbers of the homotopy colimit', homology(allp))
print('successor stones:           rational Betti numbers of the homotopy colimit', homology(succ))
