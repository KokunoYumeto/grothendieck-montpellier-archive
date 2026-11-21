#!/usr/bin/env python3
"""Exact finite supplements for HOS17--19; the universal proof is in TeX."""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as F
from math import prod
import hashlib, json, time, datetime
import sympy as s

start=time.perf_counter()
base=Path(__file__).resolve().parent
proof=base/'higher_odd_symplectic_three_involution_section.tex'

def mm(A,B):
    return [[sum(x*y for x,y in zip(row,col))%3 for col in zip(*B)] for row in A]
def tr(A): return list(map(list,zip(*A)))
def ident(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def complex_structure(n):
    A=[[0]*n for _ in range(n)]
    for k in range(0,n,2): A[k][k+1]=2; A[k+1][k]=1
    return A

def rank_discriminant(B):
    """Symmetric congruence elimination over F3, including zero diagonals."""
    A=[row[:] for row in B]; n=len(A); r=0; disc=1
    for k in range(n):
        u=next((i for i in range(k,n) if A[i][i]),None)
        if u is None:
            pair=next(((i,j) for i in range(k,n) for j in range(i+1,n) if A[i][j]),None)
            if pair is None: break
            i,j=pair
            A[i]=[(A[i][v]+A[j][v])%3 for v in range(n)]
            for v in range(n): A[v][i]=(A[v][i]+A[v][j])%3
            assert A[i][i]
            u=i
        if u!=k:
            A[k],A[u]=A[u],A[k]
            for row in A: row[k],row[u]=row[u],row[k]
        d=A[k][k]; disc=disc*d%3; r+=1
        for j in range(k+1,n):
            c=A[j][k]*d%3  # 1 and 2 are their own inverses
            if c:
                A[j]=[(A[j][v]-c*A[k][v])%3 for v in range(n)]
                for v in range(n): A[v][j]=(A[v][j]-c*A[v][k])%3
        assert all(A[k][j]==A[j][k]==0 for j in range(k+1,n))
    return r,disc

def gaussian(n,k,q):
    return F(prod(q**(n-i)-1 for i in range(k)),prod(q**(k-i)-1 for i in range(k)))
def hr(r): return 3**(r*(r-1)//2)*prod(3**j+(-1)**j for j in range(1,r+1))
def sr(r): return F(3**(r*r)*(3**r+(-1)**r)*prod(3**(2*j-1)-1 for j in range(1,r+1)),2)
def rr(r): return F(hr(r),sr(r))

tables=[]
for n in (2,4):
    A=complex_structure(n); coords=[(i,j) for i in range(n) for j in range(i,n)]
    counts=Counter(); fixed=Counter(); pairs=0
    for c in product(range(3),repeat=len(coords)):
        B=[[0]*n for _ in range(n)]
        for (i,j),v in zip(coords,c): B[i][j]=B[j][i]=v
        key=rank_discriminant(B); counts[key]+=1
        C=mm(mm(tr(A),B),A)
        assert mm(mm(tr(A),C),A)==B
        if C==B: fixed[key]+=1
        else: pairs+=1
    assert sum(fixed.values())==3**((n//2)**2)
    assert pairs%2==0
    for (rank,disc),v in fixed.items():
        if rank:
            assert rank%2==0 and disc==1
            r=rank//2
            expected=gaussian(n//2,r,9)*hr(r)
            assert v==expected
            assert counts[(rank,disc)]==gaussian(n,rank,3)*sr(r)
            ratio=F(v,counts[(rank,disc)])
            assert ratio==gaussian(n//2,r,9)/gaussian(n,2*r,3)*rr(r)
            if n>=4: assert ratio<=F(1,39)
    tables.append({'dimension':n,'all_forms':sum(counts.values()),'fixed_forms':sum(fixed.values()),
      'nonfixed_weight_pairs':pairs//2,
      'rank_discriminant':[{'rank':k[0],'disc':k[1],'orbit_size':v,'fixed':fixed[k],
                            'fraction':str(F(fixed[k],v))} for k,v in sorted(counts.items())]})

# Every Hermitian form of dimension three over F9, converted to F3 exactly.
m=3; n=2*m
params=[(i,j) for i in range(m) for j in range(i+1,m)]
hcounts=Counter(); A=complex_structure(n)
for diag in product(range(3),repeat=m):
    for off in product(range(9),repeat=len(params)):
        B=[[0]*n for _ in range(n)]
        for i,d in enumerate(diag): B[2*i][2*i]=B[2*i+1][2*i+1]=d
        for (i,j),v in zip(params,off):
            a,b=v%3,v//3
            block=[[a,b],[-b%3,a]]
            for x in range(2):
                for y in range(2): B[2*i+x][2*j+y]=B[2*j+y][2*i+x]=block[x][y]
        assert mm(mm(tr(A),B),A)==B
        rank,disc=rank_discriminant(B)
        assert rank%2==0 and disc==1
        hcounts[rank//2]+=1
assert sum(hcounts.values())==3**9
for r,v in hcounts.items(): assert v==gaussian(m,r,9)*hr(r)

# Symbolic symplectic embeddings and the exact Siegel conjugation action.
N=4; A=s.Matrix(complex_structure(N)).applyfunc(lambda x:-1 if x==2 else x)
I=s.eye(N); O=s.zeros(N); J=O.row_join(I).col_join((-I).row_join(O))
h=s.diag(A,A.inv().T)
c=s.symbols('c0:10'); C=s.zeros(N)
for (i,j),z in zip([(i,j) for i in range(N) for j in range(i,N)],c): C[i,j]=C[j,i]=z
U=I.row_join(C).col_join(O.row_join(I))
assert h*h==-s.eye(2*N) and h.T*J*h==J
assert s.simplify(h*U*h.inv()-(I.row_join(A*C*A.T).col_join(O.row_join(I))))==s.zeros(2*N)
J2=s.Matrix([[0,1],[-1,0]])
hodd=s.diag(h,J2); Jodd=s.diag(J,J2)
assert hodd*hodd==-s.eye(10) and hodd.T*Jodd*hodd==Jodd

# Exact arithmetic; the decreasing-ratio inequality is proved universally in TeX.
assert rr(1)==F(1,3) and rr(2)==F(1,351)
for r in range(1,31):
    assert rr(r+1)/rr(r)==F(3**r+(-1)**r,3**(r+1)*(3**(2*r+1)-1))<1
assert 3**4>4**3
assert F(1,2)*F(38,39)*F(1,2)==F(19,78)
assert F(1,2)*F(38,39)*F(3,8)==F(19,104)>F(1,6)
assert F(19,78)>F(2,9)
assert 6/(12*F(2,9)-2)==9<27
assert 6/(12*F(19,104)-2)==F(156,5)<81

out={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'all_symmetric_form_tables':tables,
 'all_hermitian_rank_counts_F9_dimension3':dict(sorted(hcounts.items())),
 'hermitian_forms_checked':3**9,'symbolic_natural_dimensions':[8,10],
 'rational_monotonicity_samples':30,'even_support':'19/78','odd_support':'19/104',
 'source_ceiling_even':'9','source_ceiling_odd':'156/5',
 'scope':'Exact finite and symbolic supplement only; universal orbit bound and published branching are proved/read in TeX.',
 'elapsed_seconds':time.perf_counter()-start}
(base/'check_higher_symplectic_three_involution.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
