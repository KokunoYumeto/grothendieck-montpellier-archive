import os, sys, json, itertools
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))
os.environ['HN'] = '3'; sys.path.insert(0, here)
src = open(os.path.join(here, 'hexagon.py'), encoding='utf-8').read().split("print('Gram matrix")[0]
exec(src)
v = sp.Symbol('v'); I = sp.I
cell = ['g2_1', 'g2_12', 'g2_21', 'g2_2']
ev = lambda e: sp.nsimplify(sp.simplify(sp.expand(sp.sympify(e).subs(v, I))))
Gv = {(a, b): ev(G[names.index(a), names.index(b)]) for a in names for b in names}
print("cell couplings at v=i:", [(a, b, Gv[(a, b)]) for a in cell for b in names if b not in cell and Gv[(a, b)] != 0])
C = json.load(open(os.path.join(here, 'e3_constants.json'), encoding='utf-8'))
tab = {(r['b'], r['bp'], r['bpp']): ev(r['c']) for r in C}
c = lambda x, y, z: tab.get((x, y, z), 0)
# T(x,y,w) = sum_z c(x,y;z) G[z,w], over the whole basis; cyclicity T(x,y,w) = T(y,w,x) must hold exactly
T = lambda x, y, w: sp.simplify(sum(c(x, y, z) * Gv[(z, w)] for z in names))
badcyc = sum(1 for x, y, w in itertools.product(cell, repeat=3) if sp.simplify(T(x, y, w) - T(y, w, x)) != 0)
print("cyclicity of T on cell triples at v=i (failures):", badcyc)
# do products of cell elements leave the cell at v=i?
out = [(x, y, z, c(x, y, z)) for x in cell for y in cell for z in names if z not in cell and c(x, y, z) != 0]
print("cell x cell -> outside components at v=i:", len(out), out[:6])
pi = {'g2_1': 'g2_2', 'g2_2': 'g2_1', 'g2_12': 'g2_12', 'g2_21': 'g2_21'}
wt = {z: Gv[(z, pi[z])] for z in cell}
pinv = {b: a for a, b in pi.items()}
bad = [(x, y, z) for x, y, z in itertools.product(cell, repeat=3)
       if sp.simplify(c(x, y, z) * wt[z] - c(y, pi[z], pinv[x]) * wt[pinv[x]]) != 0]
print("cell-level rotated relation c(x,y;z)w(z) = c(y,pi z;pi^-1 x)w(pi^-1 x) fails on", len(bad), "of 64 cell triples")
six = [('g2_1', 'g2_21', 'g2_1'), ('g2_12', 'g2_1', 'g2_1'), ('g2_2', 'g2_12', 'g2_2'), ('g2_21', 'g2_2', 'g2_2'),
       ('g2_12', 'g2_12', 'g2_12'), ('g2_21', 'g2_21', 'g2_21')]
rot = lambda t: (t[1], pi[t[2]], pinv[t[0]])
print("rotation on the six:", [six.index(rot(t)) if rot(t) in six else rot(t) for t in six])
print("values of the six at q=-1:", [c(*t) for t in six])
print("first failures:", bad[:8])
