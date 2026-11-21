"""Does each sheet carry its own C3 where the other sheet dies?  Cell 2 (inert, lambda_2 = (D-2)^2) was tested at q = -1
(D = 0, lambda_1 = 0) by cell_c3_check.py.  Here: both cells at both points, q = -1 (v = i) and q = i (v = e^{i pi/4},
D = 2, lambda_2 = 0).  For each (cell, point): is the trace form's block on the cell monomial, and does the weighted
cyclic slot relation c(x,y;z) w(z) = c(y, pi z; pi^-1 x) w(pi^-1 x) hold on all 64 cell triples?
Main session, Claude Opus 5.5 at effort max, 21 Nov 2026 ~20:1x UTC."""
import os, sys, json, itertools
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))
os.environ['HN'] = '3'; sys.path.insert(0, here)
src = open(os.path.join(here, 'hexagon.py'), encoding='utf-8').read().split("print('Gram matrix")[0]
exec(src)
v = sp.Symbol('v')
C = json.load(open(os.path.join(here, 'e3_constants.json'), encoding='utf-8'))
WORDS = ['1', '12', '21', '2']
for label, val in (('q=-1 (v=i, D=0)', sp.I), ('q=i (v=e^{i pi/4}, D=2)', sp.exp(sp.I * sp.pi / 4))):
    ev = lambda e: sp.nsimplify(sp.simplify(sp.expand(sp.sympify(e, locals={'v': v}).subs(v, val))))
    Gv = {(a, b): ev(G[names.index(a), names.index(b)]) for a in names for b in names}
    tab = {(r['b'], r['bp'], r['bpp']): ev(r['c']) for r in C}
    c = lambda x, y, z: tab.get((x, y, z), 0)
    for cell in ('g1', 'g2'):
        cl = [cell + '_' + w for w in WORDS]
        block = [[Gv[(a, b)] for b in cl] for a in cl]
        nz = [[j for j in range(4) if block[i][j] != 0] for i in range(4)]
        mono = all(len(r) == 1 for r in nz) and sorted(r[0] for r in nz) == list(range(4))
        line = '%-26s %s: block %s  monomial: %s' % (label, cell, block, mono)
        if mono:
            pi = {cl[i]: cl[nz[i][0]] for i in range(4)}
            pinv = {b: a for a, b in pi.items()}
            wt = {z: Gv[(z, pi[z])] for z in cl}
            bad = sum(1 for x, y, z in itertools.product(cl, repeat=3)
                      if sp.simplify(c(x, y, z) * wt[z] - c(y, pi[z], pinv[x]) * wt[pinv[x]]) != 0)
            line += '  pairing %s  C3 relation fails on %d of 64' % ({k.split('_')[1]: v2.split('_')[1] for k, v2 in pi.items()}, bad)
        print(line)
