"""Exact odd ray symmetries of the three published rank3/delta3 extremizers.

The published classification is an external coverage input. This script
checks the three archived records with integer arithmetic and produces
one odd signed-column symmetry for each if present.
"""
from ast import literal_eval
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def detcols(a, b, c):
    return dot(a, cross(b, c))


def canonical(v):
    if v == (0, 0, 0):
        return v
    return v if next(x for x in v if x) > 0 else tuple(-x for x in v)


def facets(vertices):
    out = set()
    from math import gcd
    from functools import reduce
    for a, b, c in combinations(vertices, 3):
        n = cross(tuple(y-x for x,y in zip(a,b)), tuple(y-x for x,y in zip(a,c)))
        if n == (0,0,0):
            continue
        rhs = dot(n, a)
        vals = [dot(n,v)-rhs for v in vertices]
        if all(x <= 0 for x in vals):
            pass
        elif all(x >= 0 for x in vals):
            n = tuple(-x for x in n)
            rhs = -rhs
        else:
            continue
        g = reduce(gcd, (abs(x) for x in (*n, rhs)))
        out.add(tuple(x//g for x in (*n, rhs)))
    return sorted(out)


def parity(perm):
    return sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i+1,len(perm))) % 2


def matvec(a, v):
    return tuple(dot(row, v) for row in a)


def inverse_unimodular_columns(a,b,c):
    det = detcols(a,b,c)
    assert abs(det) == 1
    return tuple(tuple(x//det for x in row) for row in (cross(b,c),cross(c,a),cross(a,b)))


def matrix_from_images(images, inverse):
    return tuple(tuple(sum(images[k][i]*inverse[k][j] for k in range(3)) for j in range(3)) for i in range(3))


base = Path(__file__).parent
path = base / 'k12_source_data/delta_dim_3_delta_3_extremal.txt'
polytopes = literal_eval(path.read_text())
results = []
for index, raw_vertices in enumerate(polytopes, 1):
    vertices = [tuple(v) for v in raw_vertices]
    inequalities = facets(vertices)
    box = [range(min(v[i] for v in vertices), max(v[i] for v in vertices)+1) for i in range(3)]
    points = [v for v in product(*box) if all(dot(f[:3],v) <= f[3] for f in inequalities)]
    rays = sorted({canonical(v) for v in points if any(v)})
    assert len(points) == 25 and len(rays) == 12
    maxdet = max(abs(detcols(*a)) for a in combinations(rays, 3))
    assert maxdet == 3
    basis = next(a for a in combinations(rays, 3) if abs(detcols(*a)) == 1)
    inverse = inverse_unimodular_columns(*basis)
    signed = [v for v in points if any(v)]
    ray_index = {v:i for i,v in enumerate(rays)}
    odd = None
    symmetries = set()
    for images in permutations(signed, 3):
        if abs(detcols(*images)) != 1:
            continue
        u = matrix_from_images(images, inverse)
        mapped = [matvec(u,v) for v in rays]
        if any(canonical(v) not in ray_index for v in mapped):
            continue
        perm = [ray_index[canonical(v)] for v in mapped]
        assert len(set(perm)) == 12
        symmetries.add(u)
        if parity(perm) and odd is None:
            odd = {
                'matrix': u,
                'pair_permutation_zero_based': perm,
                'signs': [1 if v == canonical(v) else -1 for v in mapped],
                'permutation_sign': -1,
                'determinant': detcols(tuple(row[0] for row in u),tuple(row[1] for row in u),tuple(row[2] for row in u)),
            }
    results.append({
        'record': index,
        'vertices': vertices,
        'facets_n_dot_x_le_rhs': inequalities,
        'integer_point_count': len(points),
        'signed_pair_count': len(rays),
        'maximal_minor_absolute_value': maxdet,
        'rays': rays,
        'integral_linear_symmetry_count': len(symmetries),
        'all_integral_symmetry_matrices': sorted(symmetries),
        'all_symmetry_pair_permutation_signs': [
            -1 if parity([ray_index[canonical(matvec(u,v))] for v in rays]) else 1
            for u in sorted(symmetries)
        ],
        'odd_ray_symmetry': odd,
    })
result = {
    'source_url': 'https://raw.githubusercontent.com/mschymura/delta-classification/master/data/dim_3_delta_3_extremal.txt',
    'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
    'date': '2026-11-21',
    'scope': 'Exact per-record lattice-point and symmetry checks. Completeness of the three extremizers is the published Averkov-Schymura classification, not re-enumerated here.',
    'results': results,
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps([{'record':r['record'],'point_count':r['integer_point_count'],'symmetry_count':r['integral_linear_symmetry_count'],'odd':r['odd_ray_symmetry']} for r in results],indent=2))
