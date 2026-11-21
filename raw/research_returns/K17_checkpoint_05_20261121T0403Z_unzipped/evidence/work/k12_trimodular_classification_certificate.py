"""Exact checks of the three published trimodular extremal templates.

The published values h(3,3)=25 and number of extremal equivalence classes3
are external coverage inputs, not re-enumerated by this program. This
standalone verifier checks each displayed record, the first obstruction,
the second identification and the third odd symmetry exactly.
"""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
import json

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

def detcols(a, b, c):
    return dot(a, cross(b, c))

def canonical(v):
    v = tuple(v)
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

def det3(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-b[0]*(a[1]*c[2]-a[2]*c[1])+c[0]*(a[1]*b[2]-a[2]*b[1])

def reconstruct_dual(rays):
    pivot=next(j for j in combinations(range(len(rays)),3) if abs(det3(*(rays[i] for i in j)))==1)
    a,b,c=(rays[j] for j in pivot);det=det3(a,b,c)
    inverse=[[F(x,det) for x in row] for row in (cross(b,c),cross(c,a),cross(a,b))]
    others=[j for j in range(len(rays)) if j not in pivot]
    order=others+list(pivot)
    bnorm=[[sum(row[k]*rays[j][k] for k in range(3)) for j in order] for row in inverse]
    assert all(x.denominator==1 for row in bnorm for x in row)
    n=len(rays)-3
    vectors=[tuple(int(i==j) for i in range(n)) for j in range(n)]+[tuple(-int(bnorm[j][i]) for i in range(n)) for j in range(3)]
    assert all(sum(bnorm[i][j]*vectors[j][k] for j in range(len(rays)))==0 for i in range(3) for k in range(n))
    return vectors,[[int(x) for x in row] for row in bnorm],order

VERTEX_RECORDS = [[[-3, -1, 0], [-3, -1, 1], [-3, 0, 0], [-3, 0, 1], [0, -1, 0], [0, 0, -1], [0, 0, 1], [0, 1, 0], [3, 0, -1], [3, 0, 0], [3, 1, -1], [3, 1, 0]], [[-3, 0, 0], [-3, 1, 1], [-2, 1, 0], [-1, 0, 1], [0, -1, -1], [0, -1, 0], [0, 0, -1], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, -1], [2, -1, 0], [3, -1, -1], [3, 0, 0]], [[-3, 0, 0], [-3, 1, 1], [-2, 0, 1], [-2, 1, 0], [-1, 1, 1], [0, -1, 0], [0, 0, -1], [0, 0, 1], [0, 1, 0], [1, -1, -1], [2, -1, 0], [2, 0, -1], [3, -1, -1], [3, 0, 0]]]
GALE_RECORDS = [[[0, 0, 1], [0, 1, 0], [1, 0, -1], [1, 0, 0], [1, 1, 0], [2, 0, -1], [2, 0, 0], [2, 1, 0], [3, 0, -1], [3, 0, 0], [3, 1, -1], [3, 1, 0]], [[0, 0, 1], [0, 1, 0], [0, 1, 1], [1, -1, -1], [1, -1, 0], [1, 0, -1], [1, 0, 0], [2, -1, -1], [2, -1, 0], [2, 0, 0], [3, -1, -1], [3, 0, 0]], [[0, 0, 1], [0, 1, 0], [1, -1, -1], [1, -1, 0], [1, 0, -1], [1, 0, 0], [2, -1, -1], [2, -1, 0], [2, 0, -1], [2, 0, 0], [3, -1, -1], [3, 0, 0]]]
OUTSIDE_VECTORS = [[0, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 2, 2, 2, 2]]
TAU_VECTORS = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, -1, 0, -1, -1, -2, -2, -2, -3], [-1, 0, -1, -1, -1, -1, -2, -2, -3], [0, -1, -1, -1, -2, -2, -2, -3, -3]]
ODD_MATRIX = [[-1, 0, -3], [0, -1, 1], [0, 0, 1]]

results=[]
for vertices0,rays0 in zip(VERTEX_RECORDS,GALE_RECORDS):
 vertices=[tuple(v)for v in vertices0];rays=[tuple(v)for v in rays0]
 ineq=facets(vertices)
 box=[range(min(v[i]for v in vertices),max(v[i]for v in vertices)+1)for i in range(3)]
 points={z for z in product(*box)if all(dot(f[:3],z)<=f[3]for f in ineq)}
 expected={(0,0,0)}|set(rays)|{tuple(-x for x in z)for z in rays}
 assert points==expected and len(points)==25 and len(rays)==12
 assert all(canonical(z)==z for z in rays) and len(set(rays))==12
 minors=[abs(detcols(*a))for a in combinations(rays,3)]
 assert max(minors)==3 and 1 in minors
 results.append({'lattice_points':25,'signed_nonzero_pairs':12,'maximal_minor':3,'unit_minor_exists':True})
V1,_,_=reconstruct_dual(GALE_RECORDS[0]);V2,_,_=reconstruct_dual(GALE_RECORDS[1])
assert V2==[tuple(z)for z in TAU_VECTORS]
assert len(OUTSIDE_VECTORS)==6
S={canonical(z)for z in V1}
assert all(any(z)and canonical(z)not in S for z in OUTSIDE_VECTORS)
assert len({canonical(z)for z in OUTSIDE_VECTORS})==6
# sum outside quadratic forms = first five coordinate rays + twelfth ray.
right=[V1[i]for i in [0,1,2,3,4,11]]
assert all(sum(z[i]*z[j]for z in OUTSIDE_VECTORS)==sum(z[i]*z[j]for z in right)for i in range(9)for j in range(9))
rays=[tuple(z)for z in GALE_RECORDS[2]];lookup={z:i for i,z in enumerate(rays)}
images=[matvec(ODD_MATRIX,z)for z in rays]
assert all(canonical(z)in lookup for z in images)
perm=[lookup[canonical(z)]for z in images]
assert perm==[10,1,8,3,6,5,4,7,2,9,0,11] and parity(perm)==1
assert abs(detcols(*(tuple(row[j]for row in ODD_MATRIX)for j in range(3))))==1
out={'scope':'Per-record exact checks only; published extremal coverage is an explicit external input. No assertion that all target cells have index at most3 or generate their ambient lattice.',
 'published_parameters':{'h_3_3':25,'extremal_class_count':3,'source':'Averkov-Schymura 2024 section5.2 Tables1,3 p85'},
 'records':results,'first_dual_vectors':V1,'first_outside_vectors':OUTSIDE_VECTORS,'first_quadratic_identity_indices_one_based':[1,2,3,4,5,12],
 'first_template_complete_minimum_impossible':True,'second_dual_is_tau':True,
 'third_odd_matrix':ODD_MATRIX,'third_pair_permutation_zero_based':perm,
 'third_swaps_one_based':[[1,11],[3,9],[5,7]],'consequence':'Under ambient minimum generation and maximal index<=3, each rank10 degree12 orientation generator is zero or the previously certified boundary sigma.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'records_checked':3,'first_impossible':True,'second_is_tau':True,'third_odd':True,'classification_coverage_recomputed':False},indent=2))
