"""Where does the trace form of E^opp(3) become monomial, and does the label hexagon's C3 then act on the table?
(main session, Claude Opus 5.5 at effort max, 21 Nov 2026 ~19:2x UTC). Uses hexagon.py's set-up (trace tau = the tensor
square of the standard Hecke trace on H-check_3, as built by agent a8d75352) and e3_constants.json (the 132 constants,
b2 = -(q+1)^2/q). tau is symmetric, so T(x, y, w) = tau(x y w) is cyclic: T(x, y, w) = T(y, w, x).
If the Gram matrix G is monomial with permutation pi at a point, then c(x, y; z) = T(x, y, pi z) / G[z, pi z] there, and
the cyclic rotation (x, y, w) -> (y, w, x) becomes the map (x, y; z) -> (y, pi z; pi^-1 x) on structure constants."""
import os, sys, json, itertools
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))
os.environ['HN'] = '3'; sys.path.insert(0, here)
src = open(os.path.join(here, 'hexagon.py'), encoding='utf-8').read().split("print('Gram matrix")[0]
exec(src)  # defines sp, L, B, names, E, tau, G (symbolic in v)
v = sp.Symbol('v')
cell = ['g2_1', 'g2_12', 'g2_21', 'g2_2']
pts = {'v=1 (q=1)': 1, 'v=-1': -1, 'v=i (q=-1)': sp.I, 'v=e^{i pi/3} (q=omega)': sp.exp(sp.I * sp.pi / 3),
       'v=e^{i pi/4} (q=i)': sp.exp(sp.I * sp.pi / 4), 'v=e^{i pi/6} (q=e^{i pi/3})': sp.exp(sp.I * sp.pi / 6)}
def ev(expr, val):
    return sp.nsimplify(sp.simplify(sp.expand(expr.subs(v, val))))
mono = {}
for lab, val in pts.items():
    Gv = sp.Matrix(len(names), len(names), lambda i, j: ev(G[i, j], val))
    nz = [[j for j in range(len(names)) if Gv[i, j] != 0] for i in range(len(names))]
    ismono = all(len(r) == 1 for r in nz) and sorted(r[0] for r in nz) == list(range(len(names)))
    print('%-28s rank %2d  monomial: %s' % (lab, Gv.rank(), ismono))
    if ismono:
        mono[lab] = (Gv, [r[0] for r in nz])
        print('   pairing:', {names[i]: names[r[0]] for i, r in enumerate(nz)})
    ci = [names.index(c) for c in cell]
    print('   cell block:', [[Gv[i, j] for j in ci] for i in ci])
    off = [(names[i], names[j]) for i in ci for j in range(len(names)) if j not in ci and Gv[i, j] != 0]
    print('   cell couples to the rest of the basis:', len(off), 'entries')
# the table at the monomial points
C = json.load(open(os.path.join(here, 'e3_constants.json'), encoding='utf-8'))
tab = {}
for r in C:
    tab[(r['b'], r['bp'], r['bpp'])] = sp.sympify(r['c'], locals={'v': v})
six = [('g2_1', 'g2_21', 'g2_1'), ('g2_12', 'g2_1', 'g2_1'), ('g2_2', 'g2_12', 'g2_2'), ('g2_21', 'g2_2', 'g2_2'),
       ('g2_12', 'g2_12', 'g2_12'), ('g2_21', 'g2_21', 'g2_21')]
for t in six:
    assert t in tab, t
for lab, (Gv, pi) in mono.items():
    val = pts[lab]
    P = {names[i]: names[pi[i]] for i in range(len(names))}
    Pinv = {b: a for a, b in P.items()}
    w = {names[i]: Gv[i, pi[i]] for i in range(len(names))}
    cv = {k: ev(e, val) for k, e in tab.items()}
    get = lambda x, y, z: cv.get((x, y, z), 0)
    # check the rotated relation on every triple: c(x,y;z) G[z,pi z] = c(y, pi z; pi^-1 x) G[pi^-1 x, x]
    bad = 0
    for x, y, z in itertools.product(names, repeat=3):
        lhs = sp.simplify(get(x, y, z) * w[z]); rhs = sp.simplify(get(y, P[z], Pinv[x]) * w[Pinv[x]])
        if sp.simplify(lhs - rhs) != 0:
            bad += 1
    print(lab, ': cyclic relation as a permutation of triples holds on all', len(names) ** 3, 'triples:', bad == 0)
    rot = lambda t: (t[1], P[t[2]], Pinv[t[0]])
    print('   rotation on the six:', [six.index(rot(t)) if rot(t) in six else rot(t) for t in six])
    print('   values of the six there:', [cv[t] for t in six])
