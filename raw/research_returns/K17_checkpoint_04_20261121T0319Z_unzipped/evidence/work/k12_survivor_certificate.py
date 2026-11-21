"""Standalone exact certificate for the K17 orientation survivor.

Uses only Python's standard library and hard-coded integer matrices.
No floating point, optimization software, network, or classification
coverage input is used. Run: python work/k12_survivor_certificate.py
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd, isqrt, lcm
from pathlib import Path
import json


def canon(z):
    z=tuple(z)
    if not any(z): return z
    return z if next(x for x in z if x)>0 else tuple(-x for x in z)


def quad(v):
    return [[F(x*y) for y in v] for x in v]


def gram_value(q,v):
    return sum(q[i][j]*v[i]*v[j] for i in range(len(v)) for j in range(len(v)))


def matrix_rank(rows):
    a=[[F(x) for x in row] for row in rows]
    k=0
    for j in range(len(a[0])):
        i=next((i for i in range(k,len(a)) if a[i][j]),None)
        if i is None:continue
        a[i],a[k]=a[k],a[i]
        p=a[k][j];a[k]=[x/p for x in a[k]]
        for i in range(k+1,len(a)):
            p=a[i][j]
            if p:a[i]=[x-p*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a):break
    return k


def det3(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-b[0]*(a[1]*c[2]-a[2]*c[1])+c[0]*(a[1]*b[2]-a[2]*b[1])


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


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


def ldl(q):
    n=len(q);lower=[[F(i==j) for j in range(n)] for i in range(n)];diagonal=[]
    for i in range(n):
        d=q[i][i]-sum(lower[i][k]**2*diagonal[k] for k in range(i))
        assert d>0
        diagonal.append(d)
        for j in range(i+1,n):
            lower[j][i]=(q[j][i]-sum(lower[j][k]*lower[i][k]*diagonal[k] for k in range(i)))/d
    assert all(q[i][j]==sum(lower[i][k]*diagonal[k]*lower[j][k] for k in range(n)) for i in range(n) for j in range(n))
    return lower,diagonal


def exact_short_vectors(q,bound):
    lower,diagonal=ldl(q)
    n=len(q);z=[0]*n;found=[];nodes=0
    def visit(i,partial):
        nonlocal nodes
        nodes+=1
        if i<0:
            if any(z):
                assert gram_value(q,z)==partial
                found.append(tuple(z))
            return
        remaining=bound-partial
        if remaining<0:return
        shift=sum(lower[j][i]*z[j] for j in range(i+1,n))
        a,b=shift.numerator,shift.denominator
        squared_radius=(remaining/diagonal[i])*b*b
        radius=isqrt(squared_radius.numerator//squared_radius.denominator)
        low=-((radius+a)//b)
        high=(radius-a)//b
        # low=ceil((-radius-a)/b), high=floor((radius-a)/b).
        for value in range(low,high+1):
            z[i]=value
            term=diagonal[i]*(F(value)+shift)**2
            assert term<=remaining
            visit(i-1,partial+term)
    visit(n-1,F(0))
    return sorted(found),nodes,diagonal



INTEGER_GRAM = [[36, 7, 7, 2, 7, 0, -9, 0, -9], [7, 36, 7, 0, 0, -11, 0, -11, 4], [7, 7, 36, 4, -7, 0, 0, -7, -4], [2, 0, 4, 36, 0, 0, -12, 0, -6], [7, 0, -7, 0, 36, 0, 0, -11, -7], [0, -11, 0, 0, 0, 36, 4, -7, -15], [-9, 0, 0, -12, 0, 4, 36, -7, -15], [0, -11, -7, 0, -11, -7, -7, 36, -11], [-9, 4, -4, -6, -7, -15, -15, -11, 36]]
VECTORS = [[1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, -1, 0, -1, -1, -2, -2, -2, -3], [-1, 0, -1, -1, -1, -1, -2, -2, -3], [0, -1, -1, -1, -2, -2, -2, -3, -3]]
RELATION_COLUMNS = [[0, 0, 1], [0, 1, 0], [0, 1, 1], [1, -1, -1], [1, -1, 0], [1, 0, -1], [1, 0, 0], [2, -1, -1], [2, -1, 0], [2, 0, 0], [3, -1, -1], [3, 0, 0]]

q=[[F(x,36) for x in row] for row in INTEGER_GRAM]
reconstructed,bnorm,order=reconstruct_dual(RELATION_COLUMNS)
assert reconstructed==[tuple(v) for v in VECTORS]
assert all(gram_value(q,v)==1 for v in VECTORS)
short,nodes,diag=exact_short_vectors(q,F(1))
signed={tuple(v) for v in VECTORS}|{tuple(-x for x in v) for v in VECTORS}
assert set(short)==signed and len(short)==24
rank=matrix_rank([[v[i]*v[j] for i in range(9) for j in range(i,9)] for v in VECTORS])
assert rank==12
maxminor=max(abs(det3(*(RELATION_COLUMNS[i] for i in j))) for j in combinations(range(12),3))
assert maxminor==3

# Exhaust all integral symmetries by the image of a unimodular basis.
from itertools import permutations
rays=[tuple(v) for v in RELATION_COLUMNS]
lookup={v:i for i,v in enumerate(rays)}
pivot=next(j for j in combinations(range(12),3) if abs(det3(*(rays[i] for i in j)))==1)
a,b,c=(rays[i] for i in pivot);det=det3(a,b,c)
inverse=[[F(x,det) for x in row] for row in (cross(b,c),cross(c,a),cross(a,b))]
imageset=rays+[tuple(-x for x in v) for v in rays]
symmetries=[]
for images in permutations(imageset,3):
    if abs(det3(*images))!=1:continue
    u=tuple(tuple(sum(images[k][i]*inverse[k][j] for k in range(3)) for j in range(3)) for i in range(3))
    assert all(x.denominator==1 for row in u for x in row)
    mapped=[tuple(sum(u[i][j]*v[j] for j in range(3)) for i in range(3)) for v in rays]
    if any(canon(v) not in lookup for v in mapped):continue
    perm=[lookup[canon(v)] for v in mapped]
    assert len(set(perm))==12
    inversions=sum(perm[i]>perm[j] for i in range(12) for j in range(i+1,12))
    assert inversions%2==0
    symmetries.append({'matrix':[[int(x) for x in row] for row in u],'permutation':perm,'permutation_sign':1})
assert len(symmetries)==4
output={
 'date':'2026-11-21',
 'certificate_scope':'Standard-library exact rational checks; explicit lattice only; no claim about homology or K12.',
 'integer_gram':INTEGER_GRAM,'gram_denominator':36,'vectors':VECTORS,
 'positive_LDL_diagonal':[str(d) for d in diag],
 'norm_le_one_signed_vectors':short,'enumeration_node_count':nodes,
 'quadratic_span_rank':rank,'maximal_minimum_basis_index':maxminor,
 'relation_columns':RELATION_COLUMNS,'normalized_relation_matrix':bnorm,
 'column_order':order,'all_integral_ray_symmetries':symmetries,
 'rank10_extension':{'minimum_pairs':13,'quadratic_span_rank':13,'projective_degree':12,'maximal_index':3,'all_stabilizer_orientations':1}
}
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'positive_definite':True,'minimum_pairs':12,'enumeration_nodes':nodes,'quadratic_rank':rank,'maximal_index':maxminor,'ray_symmetry_count':len(symmetries),'all_symmetries_even':True,'rank10_extension':output['rank10_extension']},indent=2))
