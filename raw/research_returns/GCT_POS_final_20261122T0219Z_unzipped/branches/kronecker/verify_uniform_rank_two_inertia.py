"""Exact finite inputs for the uniform geometric proof K-036.

This checks all cube planes and segments, and the full positivity-interval
inequalities for the selected K-020 frame masses.  The stabilizer theorem
is proved symbolically in UNIFORM_RANK_TWO_INERTIA.tex.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from math import gcd
from functools import reduce
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
cube = list(product((0, 1), repeat=3))

def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])

planes = []
normal_hist = Counter()
for triple in combinations(cube, 3):
    base = triple[0]
    reflected = [tuple(x[a] if base[a] == 0 else 1-x[a] for a in range(3))
                 for x in triple]
    assert reflected[0] == (0, 0, 0)
    normal = cross(reflected[1], reflected[2])
    assert any(normal) and all(x in (-1, 0, 1) for x in normal)
    assert reduce(gcd, normal) == 1
    ones = [a for a in range(3) if normal[a]]
    second_reflection = [tuple(1-x[a] if normal[a] < 0 else x[a]
                               for a in range(3)) for x in reflected]
    levels = {sum(x[a] for a in ones) for x in second_reflection}
    assert len(levels) == 1
    level = levels.pop()
    if len(ones) == 1:
        assert level in (0, 1)
    elif len(ones) == 2:
        assert level == 1
    else:
        assert level in (1, 2)
    normal_hist[len(ones)] += 1
    planes.append({'vertices': triple, 'first_reflection': base,
                   'normal': normal, 'positive_normal_level': level})
assert len(planes) == 56

segments = []
for a, b in combinations(cube, 2):
    all_coordinates_interior_possible = all(a[j] != b[j] for j in range(3))
    antipodal = tuple(1-x for x in a) == b
    assert all_coordinates_interior_possible == antipodal
    if antipodal:
        segments.append((a, b))
assert len(segments) == 4

# Linear forms are numerator pairs (constant, coefficient of r), all /256.
forms = {'rho': (125, 43), 'alpha1': (-1, 57), 'alpha2': (132, -100),
         'beta': (131, -43), 'gamma1': (136, -72), 'gamma2': (-5, 29)}
assert tuple(forms['alpha1'][j]+forms['alpha2'][j] for j in range(2)) == forms['beta']
assert tuple(forms['gamma1'][j]+forms['gamma2'][j] for j in range(2)) == forms['beta']
assert tuple(forms['rho'][j]+forms['beta'][j] for j in range(2)) == (256, 0)
endpoints = [Q(3, 11), Q(37, 61)]
endpoint_records = []
for r in endpoints:
    values = {name: (Q(p)+u*r)/256 for name, (p, u) in forms.items()}
    assert all(x > 0 for x in values.values())
    assert Q(1, 2) < values['rho'] < 1
    assert values['gamma2'] < values['alpha1'] < values['alpha2'] < values['gamma1']
    endpoint_records.append({'r': str(r), 'masses': {k: str(v) for k, v in values.items()}})
# Each relevant difference is affine, so strict endpoint positivity proves it
# throughout the whole closed interval and hence on the required open interval.

receipt = {
    'finding': 'K-036', 'status': 'PASS_EXACT_FINITE_INPUTS',
    'scope': 'Cube geometry and complete affine-interval mass inequalities; the uniform full-stabilizer argument is a separate complete proof.',
    'cube_plane_triples': len(planes), 'normal_support_histogram': dict(normal_hist),
    'all_cube_plane_certificates': planes, 'interior_cube_segments': segments,
    'affine_mass_numerators_over_256': forms,
    'positivity_interval_endpoints': endpoint_records,
    'box_sum_lower_minus_1': '(1-2t)/(2-t)',
    '2_minus_box_sum_upper': '(1-2t)/(2-t)',
}
(ROOT/'uniform_rank_two_inertia_checks.json').write_text(json.dumps(receipt, indent=2)+'\n')
print('PASS K-036:', len(planes), 'cube triples,', len(segments),
      'interior segments, all affine mass inequalities on (3/11,37/61).')
