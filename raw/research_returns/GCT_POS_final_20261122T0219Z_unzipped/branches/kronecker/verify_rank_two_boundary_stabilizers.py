"""Exact support and balance-vertex certificate for K-035.

No numerical optimization is used.  All bases of the reduced, three-row
balance system are exhausted using integer determinants.  The subsequent
critical-point and full-stabilizer arguments are proved in the manuscript.
The only input is the already checked K-020 n=9 support/mass/spectrum record.
"""
from collections import Counter
from fractions import Fraction
from functools import reduce
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
old = json.loads((ROOT/'amplifier_spectral_diagnostics_output4.json').read_text())[0]
assert (old['n'], old['M']) == (9, 512)
old_edges = [tuple(e) for e in old['support']]
old_mass = [Fraction(p) for p in old['masses']]
old_weights = old['W']
selected = (8, 6, 6)
assert old_edges[7] == selected and old_mass[7] == Fraction(293, 512)
assert len(old_edges) == 25
assert len(set(old_edges)) == 25
for a in range(3):
    assert len({tuple(e[b] for b in range(3) if b != a) for e in old_edges}) == 25
    assert all(sum(p for e, p in zip(old_edges, old_mass) if e[a] == j) == 1
               for j in range(9))
    assert len(set(old_weights[a])) == 9
assert all(p > 0 for p in old_mass)
assert gcd(sum(map(sum, old_weights)), 512) == 1
assert set(old_edges) == {e for e in product(range(9), repeat=3)
                         if sum(old_weights[a][e[a]] for a in range(3)) % 512 == 0}

old_inc = sp.zeros(27, 25)
for j, e in enumerate(old_edges):
    for a in range(3):
        old_inc[9*a+e[a], j] = 1
old_keep = [i for i in range(27) if i not in (17, 26)]
old_minor = int(old_inc[old_keep, :].det())
assert abs(old_minor) == 512

# Bit one denotes the new coordinate 9; bit zero the selected old coordinate.
group_old_indices = [7, 15, 24, 5, 13, 17]
group_numerators = [805, 55, 164, 219, 200, 19]
features = [list(product((0, 1), repeat=3))]
for axis in (0, 0, 1, 2, 2):
    unit = tuple(int(a == axis) for a in range(3))
    features.append([(0, 0, 0), unit])
groups = []
offset = 0
feature_by_var = []
group_by_var = []
expanded_edges = []
for g, choices in enumerate(features):
    groups.append(list(range(offset, offset+len(choices))))
    for bit in choices:
        feature_by_var.append(bit)
        group_by_var.append(g)
        edge = list(old_edges[group_old_indices[g]])
        for a in range(3):
            if bit[a]:
                assert edge[a] == selected[a]
                edge[a] = 9
        expanded_edges.append(tuple(edge))
    offset += len(choices)
assert offset == 18
scalar_indices = [j for j in range(25) if j not in group_old_indices]
scalar_edges = [old_edges[j] for j in scalar_indices]
assert len(scalar_edges) == 19
H = [mode+[mode[selected[a]]] for a, mode in enumerate(old_weights)]
fixed = {e for e in product(range(10), repeat=3)
         if sum(H[a][e[a]] for a in range(3)) % 512 == 0}
assert fixed == set(expanded_edges+scalar_edges) and len(fixed) == 37
antipodal = [[(i, j) for i in range(10) for j in range(i+1, 10)
              if (H[a][i]-H[a][j]) % 512 == 256] for a in range(3)]
assert not antipodal[0] and not antipodal[2]
for g, j in enumerate(group_old_indices):
    assert Fraction(group_numerators[g], 512) == old_mass[j]+(g == 0)

def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))

def det3(a, b, c):
    """Determinant with the three arguments as columns."""
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - b[0]*(a[1]*c[2]-a[2]*c[1])
            + c[0]*(a[1]*b[2]-a[2]*b[1]))

vertices = set()
bases = 0
nonsingular = 0
feasible_bases = 0
det_hist = Counter()
for base in product(*groups):
    remaining = [j for j in range(18) if j not in base]
    diffs = {j: sub(feature_by_var[j], feature_by_var[base[group_by_var[j]]])
             for j in remaining}
    rhs = tuple(512-sum(group_numerators[g]*feature_by_var[base[g]][a]
                       for g in range(6)) for a in range(3))
    for extra in combinations(remaining, 3):
        bases += 1
        cols = [diffs[j] for j in extra]
        d = det3(*cols)
        if not d:
            continue
        nonsingular += 1
        det_hist[abs(d)] += 1
        assert abs(d) in (1, 2)
        numerators = []
        for a in range(3):
            replacement = cols.copy()
            replacement[a] = rhs
            numerator = 2*det3(*replacement)
            assert numerator % d == 0
            numerators.append(numerator//d)
        if min(numerators) < 0:
            continue
        v = [0]*18
        for j, q in zip(extra, numerators):
            v[j] = q
        for g, j in enumerate(base):
            v[j] = 2*group_numerators[g]-sum(v[k] for k in groups[g])
        if min(v) < 0:
            continue
        feasible_bases += 1
        vertices.add(tuple(v))

assert bases == 56320 and nonsingular == 32000
assert len(vertices) == 536
constraint = sp.zeros(9, 18)
for j in range(18):
    constraint[group_by_var[j], j] = 1
    for a in range(3):
        constraint[6+a, j] = feature_by_var[j][a]
support_hist = Counter()
den_hist = Counter()
degenerate_records = []
pair_hist = Counter()
for v in sorted(vertices):
    assert all(sum(v[j] for j in groups[g]) == 2*group_numerators[g]
               for g in range(6))
    assert all(sum(v[j]*feature_by_var[j][a] for j in range(18)) == 1024
               for a in range(3))
    positive = [j for j, q in enumerate(v) if q]
    rank = constraint[:, positive].rank()
    assert rank == len(positive)
    support_hist[len(positive)] += 1
    den = 1024//reduce(gcd, v, 1024)
    den_hist[den] += 1
    if len(positive) == 9:
        continue

    edges = scalar_edges+[expanded_edges[j] for j in positive]
    equations = []
    for edge in edges:
        row = [0]*30
        for a in range(3):
            row[10*a+edge[a]] = 1
        equations.append(row)
    for coordinate in (0, 10):
        row = [0]*30
        row[coordinate] = 1
        equations.append(row)
    kernel = sp.Matrix(equations).nullspace()
    assert len(kernel) == 9-len(positive)
    record = {'mass_numerators_over_1024': v, 'positive_variables': positive}
    if len(positive) == 8:
        q = kernel[0]
        scale = lcm(*(int(x.q) for x in q))
        q = [int(x*scale) for x in q]
        divisor = reduce(gcd, q)
        q = [x//divisor for x in q]
        if next(x for x in q if x) < 0:
            q = [-x for x in q]
        nz = [(j//10, j % 10, x) for j, x in enumerate(q) if x]
        assert len(nz) == 2 and sorted(x for _, _, x in nz) == [-1, 1]
        assert nz[0][0] != nz[1][0]
        assert all(j in (selected[a], 9) for a, j, _ in nz)
        record.update({'type': 'two_isolated_lines', 'gauge_fixed_kernel': [q],
                       'isolated_factor_coordinates': nz})
        pair_hist[','.join(str(a) for a, _, _ in nz)] += 1
    else:
        assert len(positive) == 7
        core = [j for j in positive if j < 8]
        assert len(core) == 2 and sorted(v[j] for j in core) == [586, 1024]
        isolated = next(j for j in core if v[j] == 1024)
        other = next(j for j in core if v[j] == 586)
        assert all(feature_by_var[isolated][a]+feature_by_var[other][a] == 1
                   for a in range(3))
        isolated_coords = expanded_edges[isolated]
        expected = []
        for a in (0, 1):
            q = [0]*30
            q[10*a+isolated_coords[a]] = 1
            q[20+isolated_coords[2]] = -1
            assert sp.Matrix(equations)*sp.Matrix(q) == sp.zeros(len(equations), 1)
            expected.append(q)
        assert sp.Matrix.hstack(*(sp.Matrix(q) for q in expected)).rank() == 2
        for g in range(1, 6):
            active = [j for j in positive if group_by_var[j] == g]
            assert len(active) == 1
            axis = next(a for a in range(3) if features[g][1][a])
            assert expanded_edges[active[0]][axis] != isolated_coords[axis]
        record.update({'type': 'three_isolated_lines',
                       'gauge_fixed_kernel': expected,
                       'isolated_factor_coordinates': isolated_coords})
    degenerate_records.append(record)

assert support_hist == {9: 472, 8: 56, 7: 8}
assert den_hist == {512: 504, 1024: 32}
assert len(degenerate_records) == 64

receipt = {
    'finding': 'K-035', 'status': 'PASS',
    'scope': 'Exact complete balance-vertex classification; geometric stabilizer implications are proved in the manuscript.',
    'old_n': 9, 'new_n': 10, 'target_M': 512,
    'old_support': old_edges, 'old_mass': [str(p) for p in old_mass],
    'selected_edge': selected, 'old_incidence_minor': old_minor,
    'target_spectra': H, 'target_character_exponent': sum(map(sum, H)) % 512,
    'antipodal_pairs': antipodal, 'complete_fixed_support_size': len(fixed),
    'scalar_edges': scalar_edges, 'expanded_edges': expanded_edges,
    'groups': groups, 'features': feature_by_var,
    'group_numerators_over_512': group_numerators,
    'all_bases': bases, 'nonsingular_bases': nonsingular,
    'feasible_bases_with_repetition': feasible_bases,
    'nonsingular_determinant_histogram': dict(det_hist),
    'vertices': len(vertices), 'positive_support_histogram': dict(support_hist),
    'denominator_histogram': dict(den_hist), 'isolated_pair_histogram': dict(pair_hist),
    'all_vertex_numerators_over_1024': sorted(vertices),
    'degenerate_vertex_classification': degenerate_records,
}
(ROOT/'rank_two_boundary_stabilizers_checks.json').write_text(json.dumps(receipt, indent=2)+'\n')
print('PASS K-035: all', bases, 'bases;', len(vertices), 'vertices;',
      dict(support_hist), '; all 64 degenerate diagonal kernels classified.')
