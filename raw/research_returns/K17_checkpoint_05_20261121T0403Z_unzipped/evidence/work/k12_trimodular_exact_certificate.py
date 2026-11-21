"""Exact certificates for two trimodular dual templates.

Record1: a six-term quadratic identity obstructs a complete minimum set.
Record2: rational LDL and exact short-vector enumeration certify a
rank9, 12-pair configuration; the separately archived exhaustive
rank3 symmetry computation certifies the orientation statement.
Floating discovery is used only to propose rational data, all of which
are checked here by exact Fraction arithmetic.
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


base=Path(__file__).parent
discovery=json.loads((base/'k12_trimodular_separation.json').read_text())['results']
symmetry=json.loads((base/'k12_trimodular_extremal_check.json').read_text())['results']

# Exact six-term identity for record1.
r1=discovery[0];target1=r1['dual_vectors']
assert [list(v) for v in reconstruct_dual(symmetry[0]['rays'])[0]]==target1
outside=[x['vector'] for x in r1['inequality_dual']]
weights=[-F(x['coefficient']).limit_denominator(10000) for x in r1['inequality_dual']]
coeff=[-F(x).limit_denominator(10000) for x in r1['equality_dual']]
assert len(outside)==6 and all(w==F(1,6) for w in weights)
assert sum(weights)==sum(coeff)==1
assert all(w>0 for w in weights)
assert all(any(v) and canon(v) not in {canon(t) for t in target1} for v in outside)
assert all(sum(w*quad(v)[i][j] for w,v in zip(weights,outside))==sum(w*quad(v)[i][j] for w,v in zip(coeff,target1)) for i in range(9) for j in range(9))

# Exact Gram form, positivity, and all vectors of norm<=1 for record2.
r2=discovery[1];target2=[tuple(v) for v in r2['dual_vectors']]
reconstructed,bnorm,order=reconstruct_dual(symmetry[1]['rays'])
assert reconstructed==target2
assert max(abs(det3(*(symmetry[1]['rays'][i] for i in j))) for j in combinations(range(12),3))==3
q=[[F(x).limit_denominator(10000) for x in row] for row in r2['gram']]
assert all(q[i][j]==q[j][i] for i in range(9) for j in range(9))
assert all(gram_value(q,v)==1 for v in target2)
short,nodes,diag=exact_short_vectors(q,F(1))
signed_targets={tuple(v) for v in target2}|{tuple(-x for x in v) for v in target2}
assert set(short)==signed_targets and len(short)==24
denom=lcm(*(x.denominator for row in q for x in row))
integer_gram=[[int(denom*x) for x in row] for row in q]
qr=matrix_rank([[v[i]*v[j] for i in range(9) for j in range(i,9)] for v in target2])
assert qr==12
assert len(symmetry[1]['all_integral_symmetry_matrices'])==4
assert symmetry[1]['all_symmetry_pair_permutation_signs']==[1,1,1,1]

out={
 'date':'2026-11-21',
 'scope':'Exact rational matrix identity, LDL positivity, and complete norm<=1 enumeration. Symmetry exhaustion is checked by k12_trimodular_extremal_check.py; no complete higher-dimensional Voronoi enumeration.',
 'record1':{
  'target_vectors':target1,'outside_vectors':outside,
  'outside_weights':[str(x) for x in weights],
  'target_coefficients':[str(x) for x in coeff],
  'quadratic_identity_verified':True,
  'consequence':'At least one additional vector has norm<=1 whenever every target vector has norm1; the twelve-pair list cannot be the complete minimum set.'
 },
 'record2':{
  'vectors':target2,'integer_gram':integer_gram,'gram_denominator':denom,
  'original_relation_columns':symmetry[1]['rays'],
  'relation_matrix_in_target_order':bnorm,'target_order_in_original_columns':order,
  'maximal_minimum_basis_index':3,
  'positive_LDL_diagonal':[str(x) for x in diag],
  'exact_enumeration_node_count':nodes,
  'signed_minimum_vector_count':len(short),'all_norm_le_one_vectors':short,
  'quadratic_span_rank':qr,
  'dual_ray_symmetry_matrices':symmetry[1]['all_integral_symmetry_matrices'],
  'dual_ray_symmetry_permutation_signs':symmetry[1]['all_symmetry_pair_permutation_signs'],
  'consequence':'A rank9 minimum-generated twelve-pair cell with only orientation-preserving ray symmetries; adding an orthogonal unit vector gives a rank10 projective degree12 cell.'
 }
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'record1_identity':True,'record2':{k:v for k,v in out['record2'].items() if k not in ['vectors','integer_gram','all_norm_le_one_vectors']}},indent=2))
