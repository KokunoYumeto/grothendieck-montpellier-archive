# Sanity checks (finite model) for statements of Section 3 of Q02-solution.tex.
# A finite simply connected triangular 2-complex: an N x N grid of squares, each cut by a diagonal.
# This is evidence on a finite example, not a proof; D_0 = D on a finite graph, so "not constant at infinity" is not tested.
import itertools, random, sys
from fractions import Fraction
import numpy as np

random.seed(20261125)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 14
V = [(i, j) for i in range(N + 1) for j in range(N + 1)]
idx = {v: k for k, v in enumerate(V)}
edges = set()
tris = []
for i in range(N):
    for j in range(N):
        a, b, c, d = (i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)
        # random diagonal direction makes the triangulation less symmetric
        if random.random() < 0.5:
            tris.append((a, b, c)); tris.append((a, c, d))
        else:
            tris.append((a, b, d)); tris.append((b, c, d))
def E(u, v):
    return (u, v) if idx[u] < idx[v] else (v, u)
for t in tris:
    for u, v in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0])):
        edges.add(E(u, v))
edges = sorted(edges, key=lambda e: (idx[e[0]], idx[e[1]]))
eidx = {e: k for k, e in enumerate(edges)}
tri_edges = [[eidx[E(t[0], t[1])], eidx[E(t[1], t[2])], eidx[E(t[2], t[0])]] for t in tris]
adj = {v: [] for v in V}
for (u, v) in edges:
    adj[u].append(v); adj[v].append(u)
# cells containing each edge
edge_cells = {k: [] for k in range(len(edges))}
for ci, te in enumerate(tri_edges):
    for k in te:
        edge_cells[k].append(ci)

def potential(a, b):
    """Minimum-energy f with f(a)=0, f(b)=1 (free elsewhere): solve the Dirichlet problem."""
    n = len(V)
    L = np.zeros((n, n))
    for (u, v) in edges:
        i, j = idx[u], idx[v]
        L[i, i] += 1; L[j, j] += 1; L[i, j] -= 1; L[j, i] -= 1
    free = [k for k in range(n) if k not in (idx[a], idx[b])]
    rhs = -L[np.ix_(free, [idx[b]])].ravel() * 1.0
    x = np.linalg.solve(L[np.ix_(free, free)], rhs)
    f = np.zeros(n); f[idx[b]] = 1.0; f[free] = x
    return f

def components(vertex_ok, edge_ok=lambda e: True):
    seen = {}
    comps = []
    for v in V:
        if not vertex_ok(v) or v in seen:
            continue
        comp = [v]; seen[v] = len(comps); stack = [v]
        while stack:
            u = stack.pop()
            for w in adj[u]:
                if vertex_ok(w) and w not in seen and edge_ok(E(u, w)):
                    seen[w] = len(comps); comp.append(w); stack.append(w)
        comps.append(comp)
    return comps, seen

def cut(F, t):
    return [k for k, (u, v) in enumerate(edges) if min(F[idx[u]], F[idx[v]]) < t < max(F[idx[u]], F[idx[v]])]

def dual_components(S):
    S = set(S); seen = set(); out = []
    for s in S:
        if s in seen: continue
        comp = {s}; seen.add(s); stack = [s]
        while stack:
            e = stack.pop()
            for ci in edge_cells[e]:
                for e2 in tri_edges[ci]:
                    if e2 in S and e2 not in seen:
                        seen.add(e2); comp.add(e2); stack.append(e2)
        out.append(comp)
    return out

report = []
# 1. compact:potential -- connected level sides and dually connected cuts, at every regular level class.
pairs = [((0, 0), (N, N)), ((2, 3), (N - 1, 4)), ((N // 2, N // 2), (N // 2 + 1, N // 2 + 3)), ((0, N), (5, 1))]
funcs = []
bad = 0; levels_tested = 0
for (a, b) in pairs:
    f = potential(a, b)
    funcs.append(f)
    assert f.min() >= -1e-12 and f.max() <= 1 + 1e-12
    vals = sorted(set(np.round(f, 12)))
    for lo, hi in zip(vals, vals[1:]):
        if hi - lo < 1e-9: continue
        t = (lo + hi) / 2
        levels_tested += 1
        up, _ = components(lambda v: f[idx[v]] > t)
        dn, _ = components(lambda v: f[idx[v]] < t)
        dc = dual_components(cut(f, t))
        if len(up) != 1 or len(dn) != 1 or len(dc) != 1:
            bad += 1
report.append(("compact:potential: levels tested / violations", levels_tested, bad))
# 2. coarea identity: integral over t of #S(F,t) equals sum |dF(e)|
for f in funcs[:2]:
    vals = sorted(set(np.round(f, 12)))
    integ = 0.0
    for lo, hi in zip(vals, vals[1:]):
        t = (lo + hi) / 2
        integ += (hi - lo) * len(cut(f, t))
    tot = sum(abs(f[idx[u]] - f[idx[v]]) for (u, v) in edges)
    report.append(("coarea: integral, sum|dF|, diff", round(integ, 9), round(tot, 9), abs(integ - tot)))
# 3. boxes: finiteness count bound of compact:good-boxes, localized energy and shifted-wall inclusion
viol_energy = viol_incl = viol_count = boxes = 0
for trial in range(300):
    m = random.choice([1, 2, 3])
    Fs = [random.choice(funcs) for _ in range(m)]
    box = []
    for F in Fs:
        a_ = random.uniform(-0.1, 0.8); b_ = random.uniform(a_ + 0.05, 1.1)
        box.append((F, a_, b_))
    inO = lambda v: all(a_ < F[idx[v]] < b_ for (F, a_, b_) in box)
    comps, lab = components(inO)
    if not comps: continue
    boxes += 1
    cuts = []
    for (F, a_, b_) in box:
        cuts.append(set(cut(F, a_))); cuts.append(set(cut(F, b_)))
    allcut = set().union(*cuts)
    # E = cut edges also in another cut or sharing a cell with an edge of another cut
    Eset = set()
    for i, Si in enumerate(cuts):
        others = set().union(*[Sj for j, Sj in enumerate(cuts) if j != i]) if len(cuts) > 1 else set()
        for e in Si:
            if e in others: Eset.add(e); continue
            for ci in edge_cells[e]:
                if any(e2 in others for e2 in tri_edges[ci]):
                    Eset.add(e); break
    ndual = sum(len(dual_components(Si - Eset)) for Si in cuts)
    gcomps, _ = components(lambda v: True, edge_ok=lambda e: eidx[e] not in allcut)
    if allcut and len(gcomps) > 2 * ndual + 2 * len(Eset):
        viol_count += 1
    # the box's components are exactly the G' components with the right signs
    gset = {frozenset(c) for c in gcomps}
    for c in comps:
        if frozenset(c) not in gset: viol_count += 1
    def psi(v):
        return max(0.0, min([1.0] + [x for (F, a_, b_) in box for x in (F[idx[v]] - a_, b_ - F[idx[v]])]))
    for U in comps:
        Uset = set(U)
        h = {v: (psi(v) if v in Uset else 0.0) for v in V}
        for (u, v) in edges:
            if abs(h[u] - h[v]) > max(abs(F[idx[u]] - F[idx[v]]) for (F, _, _) in box) + 1e-12:
                viol_energy += 1
        for _ in range(3):
            t = random.uniform(0.001, 0.999)
            Sh = [k for k, (u, v) in enumerate(edges) if min(h[u], h[v]) < t < max(h[u], h[v])]
            cover = set()
            for (F, a_, b_) in box:
                cover |= set(cut(F, a_ + t)) | set(cut(F, b_ - t))
            if not set(Sh) <= cover: viol_incl += 1
report.append(("boxes tested, count-bound/component violations, energy violations, shifted-wall violations", boxes, viol_count, viol_energy, viol_incl))
for r in report: print(r)
