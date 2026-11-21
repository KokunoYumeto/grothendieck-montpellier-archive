#!/usr/bin/env python3
"""Independent checks on full signed exterior matrices and stored certificates.
Constructs full signed exterior generators for n<=4 and checks their exact
block coordinates against the stored generated-order lattice. Independently
checks determinantal-index valuations at p=2,3,5 by rational local elimination.
Does not perform an independent word-closure enumeration or Lean compilation.
"""
from pathlib import Path
import json, math
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form
ROOT=Path(__file__).resolve().parent

def rank_mod(A,p):
    a=[[int(v)%p for v in row] for row in A.tolist()]
    R=len(a);C=len(a[0]) if R else 0;i=0
    for j in range(C):
        q=next((q for q in range(i,R) if a[q][j]),None)
        if q is None: continue
        a[i],a[q]=a[q],a[i]
        inv=pow(a[i][j],-1,p)
        a[i]=[(v*inv)%p for v in a[i]]
        for q in range(i+1,R):
            z=a[q][j]
            if z:a[q]=[(a[q][k]-z*a[i][k])%p for k in range(C)]
        i+=1
        if i==R:break
    return i

def p_adic_index(B,p):
    # Compute determinantal divisor valuation by unimodular pivots in Z_(p).
    a=[[S.Rational(v) for v in row] for row in B.tolist()]
    nr=len(a);nc=len(a[0]); vals=[];i=0
    def valuation(x):
        if x==0:return 10**8
        u=abs(int(x.p));v=abs(int(x.q));r=0
        while u%p==0: r+=1;u//=p
        while v%p==0:r-=1;v//=p
        return r
    while i<nc:
        best=min(((valuation(a[r][c]),r,c) for r in range(i,nr) for c in range(i,nc)),default=None)
        v,r,c=best
        assert v<10**8
        vals.append(v)
        a[i],a[r]=a[r],a[i]
        for row in a:row[i],row[c]=row[c],row[i]
        pivot=a[i][i]
        for r in range(i+1,nr):
            if a[r][i]:
                scale=a[r][i]/pivot
                for c in range(i+1,nc):a[r][c]-=scale*a[i][c]
                a[r][i]=0
        i+=1
    return sum(vals),vals

def exterior_gens(n):
    dim=4**n;L=S.zeros(dim);D=S.zeros(dim)
    # Basis subsets of ordered e1,f1,e2,f2,...; pair insertion has + sign.
    # Still calculate it directly from wedge inversion parity.
    for s in range(dim):
        for a in range(n):
            pair=(1<<(2*a))|(1<<(2*a+1))
            if not(s&pair):
                inv=sum(1 for b in (2*a,2*a+1) for c in range(2*n) if (s>>c)&1 and b>c)
                L[s|pair,s]=(-1)**inv
            if s&pair==pair:
                # i_f i_e removes e then f; each single contraction uses its own parity.
                e=2*a;f=e+1
                inv1=(s&((1<<e)-1)).bit_count()
                t=s^(1<<e)
                inv2=(t&((1<<f)-1)).bit_count()
                D[s^pair,s]=(-1)**(inv1+inv2)
    return L,D,[S.diag(*[int(s.bit_count()==j) for s in range(dim)]) for j in range(2*n+1)]

def extract_blocks(A,n):
    data=[]
    for v in range(n+1):
        # v active pairs, then one e singleton on remaining n-v pairs.
        singles=sum(1<<(2*i) for i in range(v,n))
        indexes=[singles|sum(3<<(2*i) for i in range(v) if t>>i&1) for t in range(2**v)]
        data.extend([A[r,c] for r in indexes for c in indexes])
    return S.Matrix(data)

out=[]
for n in range(1,5):
    L,D,P=exterior_gens(n)
    assert D==L.T
    for kind in ['ordinary','ordinary_pi','divided','divided_pi']:
        rec=json.loads((ROOT/f'order_basis_n{n}_{kind}.json').read_text());B=S.Matrix(rec['basis_rows'])
        vals={}
        for p in [2,3,5]:
            v,vs=p_adic_index(B,p)
            expect=sum(next((k for k in range(100) if d//p**k%p),0) for d in rec['smith_nonzero'])
            assert v==expect,(n,kind,p,v,expect)
            vals[p]=v
        # Primes outside stored index are excluded by an exact full-rank minor
        # of index determinant in the column HNF (checked via Cauchy-Binet SNF
        # producer); this independent local routine checks the nontrivial primes.
        gens=[L,D]
        if 'pi' in kind:gens+=P
        if 'div' in kind:
            gens += [G**r/math.factorial(r) for r in range(2,n+1) for G in [L,D]]
        for G in gens:
            v=extract_blocks(G,n)
            assert hermite_normal_form(S.Matrix.hstack(B,v))==B
        out.append({'n':n,'kind':kind,'local_index_valuations':vals,'signed_full_generator_membership':True})
print(json.dumps(out,indent=2))
(ROOT/'independent_exterior_verification.json').write_text(json.dumps(out,indent=2))
