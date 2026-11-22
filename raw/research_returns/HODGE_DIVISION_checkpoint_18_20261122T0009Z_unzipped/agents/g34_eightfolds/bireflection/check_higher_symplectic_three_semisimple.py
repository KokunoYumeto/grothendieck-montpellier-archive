#!/usr/bin/env python3
"""Exact supplements for HOS20--22; all-dimensional arguments are in TeX."""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
from collections import Counter
import hashlib,json,time,datetime
from flint import nmod_mat

start=time.perf_counter();base=Path(__file__).resolve().parent
proof=base/'higher_odd_symplectic_three_semisimple_section.tex'
def mat(rows):return nmod_mat(rows,3)
def eye(n):return mat([[int(i==j) for j in range(n)] for i in range(n)])
def zero(n):return mat([[0]*n for _ in range(n)])
def block(A,B):
    n,m=A.nrows(),B.nrows();C=zero(n+m)
    for i in range(n):
        for j in range(n):C[i,j]=A[i,j]
    for i in range(m):
        for j in range(m):C[n+i,n+j]=B[i,j]
    return C
def companion(c):
    n=len(c);A=zero(n)
    for i in range(1,n):A[i,i-1]=1
    for i in range(n):A[i,n-1]=-c[i]
    return A
def entries(A):return tuple(int(A[i,j]) for i in range(A.nrows()) for j in range(A.ncols()))

def nullspace(rows):
    A=[list(map(lambda v:int(v)%3,row)) for row in rows]
    n=len(A[0]);piv=[];k=0
    for j in range(n):
        i=next((i for i in range(k,len(A)) if A[i][j]),None)
        if i is None:continue
        A[i],A[k]=A[k],A[i]
        c=A[k][j];A[k]=[(v*c)%3 for v in A[k]]
        for i in range(len(A)):
            if i!=k and A[i][j]:
                c=A[i][j];A[i]=[(x-c*y)%3 for x,y in zip(A[i],A[k])]
        piv.append(j);k+=1
    out=[]
    for j in range(n):
        if j in piv:continue
        v=[0]*n;v[j]=1
        for i,p in enumerate(piv):v[p]=-A[i][j]%3
        out.append(v)
    return out

def invariant_forms(A,alt=False):
    n=A.nrows();coords=[(i,j) for i in range(n) for j in range(i+(1 if alt else 0),n)]
    basis=[];cols=[]
    for i,j in coords:
        B=zero(n);B[i,j]=1;B[j,i]=-1 if alt else 1
        basis.append(B);cols.append(entries(A.transpose()*B*A-B))
    kernels=nullspace(zip(*cols));out=[]
    for c in kernels:
        B=zero(n)
        for v,E in zip(c,basis):B+=E*v
        assert A.transpose()*B*A==B
        out.append(B)
    return out

def rank_disc(B):
    n=B.nrows();A=[[int(B[i,j]) for j in range(n)] for i in range(n)]
    rank=0;disc=1
    for k in range(n):
        u=next((i for i in range(k,n) if A[i][i]),None)
        if u is None:
            ij=next(((i,j) for i in range(k,n) for j in range(i+1,n) if A[i][j]),None)
            if ij is None:break
            i,j=ij;A[i]=[(a+b)%3 for a,b in zip(A[i],A[j])]
            for v in range(n):A[v][i]=(A[v][i]+A[v][j])%3
            u=i
        A[u],A[k]=A[k],A[u]
        for row in A:row[u],row[k]=row[k],row[u]
        d=A[k][k];assert d;disc=disc*d%3;rank+=1
        for j in range(k+1,n):
            c=A[j][k]*d%3
            A[j]=[(x-c*y)%3 for x,y in zip(A[j],A[k])]
            for i in range(n):A[i][j]=(A[i][j]-c*A[i][k])%3
    return rank,disc

A5=companion([1,1,1,1]);assert A5**5==eye(4) and (A5-eye(4)).rank()==4
A13=companion([2,2,0]);assert A13**13==eye(3) and (A13-eye(3)).rank()==3
A41=companion([1,0,1,1,2,1,1,0]);assert A41**41==eye(8) and (A41-eye(8)).rank()==8

# Complete rank/type fractions for the smallest allowed prime, no table input.
totals=Counter();fixed=Counter();coords=[(i,j) for i in range(4) for j in range(i,4)]
for c in product(range(3),repeat=10):
    B=zero(4)
    for (i,j),v in zip(coords,c):B[i,j]=B[j,i]=v
    key=rank_disc(B);totals[key]+=1
    if A5.transpose()*B*A5==B:fixed[key]+=1
for key,total in totals.items():
    if key[0]:assert Q(fixed[key],total)<=Q(1,9)
assert sum(fixed.values())==9 and fixed[(4,2)]==8

# Every unitriangular congruence in rank4, in each of the two types.
unit_counts=[]
for last in (1,2):
    D=eye(4);D[3,3]=last;seen=set()
    for c in product(range(3),repeat=6):
        L=eye(4)
        for (i,j),v in zip([(i,j) for i in range(4) for j in range(i+1,4)],c):L[i,j]=v
        seen.add(entries(L.transpose()*D*L))
    assert len(seen)==3**6;unit_counts.append(len(seen))

# Binary orthogonal orders are computed from every2x2 matrix.
orders=[]
for D in (mat([[0,1],[1,0]]),eye(2)):
    orders.append(sum(1 for c in product(range(3),repeat=4)
                      if (lambda A:A.rank()==2 and A.transpose()*D*A==D)(mat([c[:2],c[2:]]))))
assert orders==[4,8]

fixed_profiles=[]
for name,A,prime in [('selfreciprocal5_mult1',A5,5),
                     ('paired13',block(A13,A13.inv().transpose()),13),
                     ('selfreciprocal5_mult2',block(A5,A5),5)]:
    n=A.nrows();basis=invariant_forms(A);counts=Counter()
    for c in product(range(3),repeat=len(basis)):
        B=zero(n)
        for v,E in zip(c,basis):B+=E*v
        r=B.rank();counts[r]+=1
        assert r==0 or r>=4 and r%2==0
    assert A**prime==eye(n) and (A-eye(n)).rank()==n
    fixed_profiles.append({'name':name,'dimension':n,'prime':prime,
        'fixed_space_dimension':len(basis),'ranks':dict(sorted(counts.items()))})
assert fixed_profiles[0]['ranks']=={0:1,4:8}
assert fixed_profiles[1]['ranks']=={0:1,6:26}
assert fixed_profiles[2]['ranks']=={0:1,4:656,8:5904}

# An actual prime41 toral element in natural dimension8. Every commuting
# linear operator is a polynomial because the companion is cyclic.
alts=invariant_forms(A41,True);assert len(alts)==4
J=alts[0];assert J.rank()==8 and A41.transpose()*J*A41==J
powers=[eye(8)]
for i in range(1,8):powers.append(powers[-1]*A41)
centralizer=0;invertible=0
for c in product(range(3),repeat=8):
    T=zero(8)
    for v,E in zip(c,powers):T+=E*v
    assert T*A41==A41*T
    if T.rank()==8:invertible+=1
    isometry=T.transpose()*J*T==J
    assert isometry==(T*(T**81)==eye(8))
    centralizer+=isometry
assert invertible==3**8-1 and centralizer==3**4+1==82

# Stable isotropic pair for the multiplicity-two selfreciprocal case.
H=block(A5,A5.inv().transpose());Js=zero(8)
for i in range(4):Js[i,4+i]=1;Js[4+i,i]=-1
assert H.transpose()*Js*H==Js and H**5==eye(8)
assert H.charpoly()==A5.charpoly()**2
assert (H-eye(8)).rank()==8

# Exact endpoints and universal monotonicity ingredients.
assert Q(4,5)*Q(8,9)*Q(3,8)==Q(4,15)
assert Q(1,2)*(1-Q(10,27))==Q(17,54)>Q(4,15)>Q(2,9)
assert 10<3**4 and 3**2<10 and (3**2+1)**2==10**2
assert 3**4>4**3
assert Q(6)/(12*Q(2,9)-2)==9<27
assert Q(6)/(12*Q(19,104)-2)==Q(156,5)<81
for r in range(4,101,2):assert r*(r-2)>=8

out={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'all_symmetric_rank4_forms':sum(totals.values()),
 'prime5_orbit_fractions':[{'rank':r,'disc':d,'total':v,'fixed':fixed[(r,d)],'fraction':str(Q(fixed[(r,d)],v))} for (r,d),v in sorted(totals.items())],
 'unitriangular_type_counts':unit_counts,'binary_orthogonal_orders':orders,
 'complete_fixed_form_profiles':fixed_profiles,'prime41_polynomial':[1,0,1,1,2,1,1,0,1],
 'prime41_commuting_polynomials':3**8,'prime41_invertible':invertible,'prime41_isometry_centralizer':centralizer,
 'stable_isotropic_witness_natural_dimension':8,'semisimple_support':'4/15','toral_support':'17/54',
 'source_degree_ceilings':['9','156/5'],'elapsed_seconds':time.perf_counter()-start,
 'scope':'Exact finite and symbolic supplements; universal fixed-form, primary multiplicity and source arguments are proved in TeX.'}
(base/'check_higher_symplectic_three_semisimple.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
