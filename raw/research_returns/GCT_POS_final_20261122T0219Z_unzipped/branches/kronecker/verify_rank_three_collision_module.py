"""Exact n18 collision tensor and supported-module Hilbert series, K-037.

The source is a finite centralizer quotient, not asserted to be the
normalization of its image.  No full-stabilizer or global-pole inference
is made from this finite computation.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
old = json.loads((ROOT/'amplifier_spectral_diagnostics_output4.json').read_text())[1]
assert (old['n'], old['M']) == (16, 131072)
D = old['M']
edges = [tuple(e) for e in old['support']]
masses = [Q(p) for p in old['masses']]
selected = (15, 13, 13)
j0 = edges.index(selected)
rho = masses[j0]
assert rho == Q(76599, D) and rho > Q(1, 3)
assert len(edges) == 46
for a in range(3):
    assert len({tuple(e[b] for b in range(3) if b != a) for e in edges}) == 46
    assert all(sum(p for e, p in zip(edges, masses) if e[a] == i) == 1
               for i in range(16))
    assert all(any(e[a] == i and all(e[b] != selected[b] for b in range(3) if b != a)
                   for e in edges) for i in range(16))
frame_indices = [[j for j, e in enumerate(edges)
                  if j != j0 and e[a] == selected[a]] for a in range(3)]
assert list(map(len, frame_indices)) == [2, 1, 2]
assert sorted(masses[j] for j in frame_indices[0]) == [Q(16189, D), Q(38284, D)]

# Weighted ternary core: all coefficients are real algebraic numbers.
r = sp.Rational(rho.numerator, rho.denominator)
core = {(0, 0, 0): sp.sqrt(r-sp.Rational(1, 3)),
        (0, 1, 2): 1/sp.sqrt(6), (0, 2, 1): 1/sp.sqrt(6),
        (1, 1, 2): 1/sp.sqrt(2), (1, 2, 1): -1/sp.sqrt(2),
        (2, 0, 2): 1/sp.sqrt(3), (2, 1, 1): 1/sp.sqrt(3),
        (2, 2, 0): 1/sp.sqrt(3)}
gram = []
for a in range(3):
    G = sp.zeros(3)
    for e, ce in core.items():
        for f, cf in core.items():
            if all(e[b] == f[b] for b in range(3) if b != a):
                G[e[a], f[a]] += ce*cf
    G = G.applyfunc(sp.simplify)
    assert G == sp.diag(r, 1, 1)
    gram.append([[str(x) for x in G.row(i)] for i in range(3)])
E = [[0, 0, 1], [0, 1, 2], [0, 1, 2]]
assert sum(map(sum, E)) % 3 == 1
assert all(sum(E[a][e[a]] for a in range(3)) % 3 == 0 for e in core)
assert all(E[a][0] == 0 for a in range(3))

def global_edge(e):
    return tuple(selected[a] if e[a] == 0 else 15+e[a] for a in range(3))

core_global = {global_edge(e): c for e, c in core.items()}
remaining = [(e, p) for j, (e, p) in enumerate(zip(edges, masses)) if j != j0]
for e, _ in remaining:
    for f in core_global:
        assert all(any(e[b] != f[b] for b in range(3) if b != a) for a in range(3))
# Thus there are no old/core cross terms in any reduced matrix; the verified
# core margins replace rho at each selected old coordinate and add two ones.

H = [mode+[mode[selected[a]], mode[selected[a]]] for a, mode in enumerate(old['W'])]
Eglobal = [[0]*16+E[a][1:] for a in range(3)]
Gweights = [[(3*H[a][i]+D*Eglobal[a][i]) % (3*D) for i in range(18)] for a in range(3)]
assert gcd(sum(map(sum, H)), D) == 1
assert gcd(sum(map(sum, Gweights)), 3*D) == 1
fixed_H = [e for e in product(range(18), repeat=3)
           if sum(H[a][e[a]] for a in range(3)) % D == 0]
fixed_G = [e for e in product(range(18), repeat=3)
           if sum(Gweights[a][e[a]] for a in range(3)) % (3*D) == 0]
lie_H = sum(sum(c*c for c in Counter(w).values())-1 for w in H)
lie_G = sum(sum(c*c for c in Counter(w).values())-1 for w in Gweights)
assert (len(fixed_H), lie_H, len(fixed_H)-lie_H) == (82, 69, 13)
assert (len(fixed_G), lie_G, len(fixed_G)-lie_G) == (56, 53, 3)
assert set(core_global).union(e for e, _ in remaining).issubset(fixed_G)

# Compress the unique double eigenvalue of G in factor A.
compA = {i: i for i in range(16)}
compA[16] = selected[0]
compA[17] = 16
group_edges = defaultdict(list)
for e in fixed_G:
    group_edges[(compA[e[0]], e[1], e[2])].append(e)
keys = sorted(group_edges)
assert len(keys) == 51
assert Counter(map(len, group_edges.values())) == {1: 46, 2: 5}
critical_mass = dict(remaining)
critical_mass.update({e: Q(sp.simplify(c*c)) for e, c in core_global.items()})
group_mass = [sum((critical_mass.get(e, Q(0)) for e in group_edges[k]), Q(0)) for k in keys]
assert all(p > 0 for p in group_mass)
inc = sp.zeros(53, 51)
for j, (a, b, c) in enumerate(keys):
    inc[a, j] = inc[17+b, j] = inc[35+c, j] = 1
target = [1]*53
target[selected[0]] = 2
assert inc*sp.Matrix([sp.Rational(p.numerator, p.denominator) for p in group_mass]) == sp.Matrix(target)
keep = [j for j in range(53) if j not in (17+15, 35+15)]
minor = int(inc[keep, :].det())
assert abs(minor) == 3*D
assert lcm(*(p.denominator for p in group_mass)) == 3*D
binary_mass = [group_mass[j] for j, k in enumerate(keys) if len(group_edges[k]) == 2]
assert sorted(binary_mass) == sorted([rho-Q(1, 3), Q(2, 3), Q(2, 3), Q(16189, D), Q(38284, D)])
S = 3*D
P = [3*rho.numerator-D, 2*D, 2*D, 3*16189, 3*38284]
assert sum(P) == 2*S

# SL2 character extraction on five binary vectors, valid in every degree.
a, z, u = sp.symbols('a z u')
polynomial = 0
subsets = []
for size in range(6):
    for I in combinations(range(5), size):
        slope = S-sum(P[i] for i in I)
        assert slope != 0
        if slope > 0:
            assert slope >= size
            q = slope*a-size+3
            polynomial += (-1)**size*q*(q-1)*(q-2)/6
            subsets.append({'indices': I, 'slope': slope, 'size': size})
polynomial = sp.expand(polynomial)
assert polynomial == 4531688675*a*a+131072*a+1

def direct_character(a):
    """Independent sliding-window product of five finite SL2 weight strings."""
    N = S*a
    coeff = [1]+[0]*N
    for p in P:
        degree = p*a
        new = []
        running = 0
        for j in range(N+1):
            running += coeff[j]
            if j > degree:
                running -= coeff[j-degree-1]
            new.append(running)
        coeff = new
    return coeff[N]-(coeff[N-1] if N else 0)

direct_checks = []
for aa in range(3):
    value = direct_character(aa)
    assert value == polynomial.subs(a, aa)
    direct_checks.append(value)
A, B = 4531688675, 131072
F = sp.cancel(A*z*(1+z)/(1-z)**3+B*z/(1-z)**2+1/(1-z))
numerator = 1+4531819745*z+4531557604*z*z
assert sp.cancel(F-numerator/(1-z)**3) == 0
local = sp.series(F.subs(z, (1-u)**3), u, 0, 1).removeO().expand()
principal = {str(k): str(local.coeff(u, -k)) for k in range(1, 4)}
assert principal == {'1': '4531295468/27', '2': '-1510519201/3', '3': '9063377350/27'}
assert (2*A) % 3 and 4531295468 % 3

receipt = {
    'finding': 'K-037', 'status': 'PASS',
    'scope': 'Actual n18 collision point and exact finite centralizer-quotient module; not asserted to be the image normalization or the specific global moving Koszul class.',
    'n': 18, 'D': D, 'higher_order': 3*D, 'selected_prefix_edge': selected,
    'rho': str(rho), 'core_coefficients': {str(e): str(c) for e, c in core.items()},
    'core_reduced_matrices': gram, 'core_order3_spectra': E,
    'h_spectra_mod_D': H, 'g_spectra_mod_3D': Gweights,
    'h_character_exponent': sum(map(sum, H)) % D,
    'g_character_exponent': sum(map(sum, Gweights)) % (3*D),
    'fixed_h_counts': [len(fixed_H), lie_H, 13],
    'fixed_g_counts': [len(fixed_G), lie_G, 3],
    'compressed_fixed_groups': [{'edge': k, 'coordinates': group_edges[k], 'mass': str(group_mass[j])}
                                for j, k in enumerate(keys)],
    'compressed_incidence_minor': minor,
    'binary_degree_coefficients': P, 's_per_a': S,
    'positive_slope_subsets': subsets, 'all_degree_coefficient_polynomial': str(polynomial),
    'independent_weight_string_values_at_a_0_1_2': direct_checks,
    'series_numerator': str(numerator), 'series_denominator': '(1-z)^3',
    'density_in_z': 2*A, 'principal_at_u_1_minus_tD': principal,
    'top_v3': -3, 'simple_v3': -3,
    'cyclic_orbit_top_v3': -2, 'cyclic_orbit_simple_v3': -2,
}
(ROOT/'rank_three_collision_module_checks.json').write_text(json.dumps(receipt, indent=2)+'\n')
print('PASS K-037: n18 weighted critical collision; all fixed weights;',
      'compressed index', abs(minor), '; exact five-vector series and actual module valuations.')
