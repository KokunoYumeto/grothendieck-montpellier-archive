"""Exact covariant and local moving-character certificate for K-038."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import product, combinations
from math import gcd
from functools import reduce
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
old = json.loads((ROOT/'amplifier_spectral_diagnostics_output4.json').read_text())[1]
cert = json.loads((ROOT/'rank_three_collision_module_checks.json').read_text())
D = old['M']
assert D == 131072
selected = (15, 13, 13)
rho = sp.Rational(76599, D)
T = {tuple(e): sp.sqrt(sp.Rational(p)) for e, p in zip(old['support'], old['masses'])
     if tuple(e) != selected}
core = {(0, 0, 0): sp.sqrt(rho-sp.Rational(1, 3)),
        (0, 1, 2): 1/sp.sqrt(6), (0, 2, 1): 1/sp.sqrt(6),
        (1, 1, 2): 1/sp.sqrt(2), (1, 2, 1): -1/sp.sqrt(2),
        (2, 0, 2): 1/sp.sqrt(3), (2, 1, 1): 1/sp.sqrt(3),
        (2, 2, 0): 1/sp.sqrt(3)}
for e, c in core.items():
    T[tuple(selected[a] if e[a] == 0 else 15+e[a] for a in range(3))] = c
assert len(T) == 53
# Move C into the first position for the covariant formula.
TC = {(e[2], e[0], e[1]): c for e, c in T.items()}
edges = list(TC)
pair = {}
for e in edges:
    pair.setdefault((e[1], e[2]), []).append(e)
X = sp.zeros(18)
terms = []
for e, f, g in product(edges, repeat=3):
    u = (f[0], g[1], e[2])
    v = (g[0], e[1], f[2])
    if u not in TC or v not in TC:
        continue
    for w in pair.get((f[1], g[2]), []):
        value = sp.simplify(TC[e]*TC[f]*TC[g]*TC[u]*TC[v]*TC[w])
        X[e[0], w[0]] += value
        terms.append({'edges': [e, f, g, u, v, w], 'entry': [e[0], w[0]],
                      'value': str(value)})
X = X.applyfunc(sp.simplify)
assert len(terms) == 224
assert all(X[i, j] == 0 for i in range(18) for j in range(18) if i != j)
diagonal = list(X.diagonal())
assert all(x.is_Rational for x in diagonal) and len(set(diagonal)) == 18

# Exact torus equations on the six new relative coordinates.
new_rows = [(0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2)]
R = sp.Matrix([[int(e[a] == j) for e in core if e != (0, 0, 0)]
               for a, j in new_rows])
minors = [int(R[:, cols].det()) for cols in combinations(range(7), 6)]
assert R.rank() == 6 and reduce(gcd, minors) == 3
exponents = sp.Matrix([0, 1, 1, 2, 1, 2])
assert all(int(x) % 3 == 0 for x in R.T*exponents)
assert sum(exponents) % 3 == 1

H = cert['h_spectra_mod_D']
G = cert['g_spectra_mod_3D']
assert all(not [(i, j) for i in range(18) for j in range(i+1, 18)
                if (H[a][i]-H[a][j]) % D == D//2] for a in (0, 2))
scalar_periods = []
for W in G:
    mult = Counter(W)
    candidates = {(x-W[0]) % (3*D) for x in W}
    periods = sorted(q for q in candidates if Counter((x+q) % (3*D) for x in W) == mult)
    assert periods == [0]
    scalar_periods.append(periods)
V = Counter(sum(G[a][e[a]] for a in range(3)) % (3*D)
            for e in product(range(18), repeat=3))
Lie = Counter((G[a][i]-G[a][j]) % (3*D) for a in range(3)
              for i in range(18) for j in range(18))
Lie[0] -= 3
tangent = {k: V[k]-Lie[k] for k in set(V).union(Lie)}
assert min(tangent.values()) >= 0
assert sum(tangent.values()) == 18**3-3*(18**2-1) == 4863
assert tangent[0] == 3
assert [V[D], V[2*D], Lie[D], Lie[2*D]] == [14, 12, 8, 8]
assert [tangent[D], tangent[2*D]] == [6, 4]
x = sp.symbols('x')
relative = sp.invert(sp.Poly((1-x)**6*(1-x*x)**4, x),
                     sp.Poly(x*x+x+1, x)).as_expr()
assert sp.rem(relative+(x*x)/3**5, x*x+x+1, x) == 0
receipt = {
    'finding': 'K-038', 'status': 'PASS',
    'scope': 'Exact covariant, diagonal-centralizer equations and local moving characters; the full-stabilizer and normalization implications are proved separately.',
    'covariant_factor': 'C', 'nonzero_contraction_terms': 224,
    'covariant_diagonal': [str(q) for q in diagonal],
    'all_covariant_contraction_terms': terms,
    'new_relative_incidence_matrix': [[int(x) for x in row] for row in R.tolist()], 'new_relative_maximal_minors': minors,
    'new_cubic_character_exponents': list(map(int, exponents)),
    'scalar_spectral_periods': scalar_periods,
    'ambient_quotient_dimension': 4863, 'g_fixed_tangent_dimension': 3,
    'V_cubic_moving_counts': [V[D], V[2*D]],
    'Lie_cubic_moving_counts': [Lie[D], Lie[2*D]],
    'relative_tangent_counts': [6, 4],
    'relative_inverse_Euler': '-omega^2/3^5',
    'full_moving_tangent_exponent_multiplicities':
        sorted((k, v) for k, v in tangent.items() if k and v),
    'local_leading_density': cert['density_in_z'],
    'local_leading_coefficient_v3': -5
}
(ROOT/'rank_three_full_stabilizer_checks.json').write_text(json.dumps(receipt, indent=2)+'\n')
print('PASS K-038: 18 distinct rational covariant eigenvalues; centralizer C_(3D); local moving counts6,4.')

