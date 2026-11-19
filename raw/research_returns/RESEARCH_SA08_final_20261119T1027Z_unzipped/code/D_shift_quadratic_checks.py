#!/usr/bin/env python3
"""Exact normalized quadratic Dold--Kan checks for D-025.

K(Z,r)_n has basis indexed by r-subsets of {1,...,n}, encoding
surjections [n] -> [r].  In normalized quotient chains of Sym^2 or
Gamma^2, a pair survives exactly when its union is {1,...,n}.
This builds the actual integral face matrices, not a recurrence model.
"""
import itertools
import json
from pathlib import Path
import time
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

start=time.perf_counter()
checks=0
def check(c):
    global checks
    assert c
    checks+=1

def basis(r,n):
    if n<r or n>2*r:return []
    ss=list(itertools.combinations(range(1,n+1),r))
    return [(a,b) for j,a in enumerate(ss) for b in ss[j:]
            if set(a)|set(b)==set(range(1,n+1))]

def face(s,n,i):
    if i==0:
        return None if 1 in s else tuple(j-1 for j in s)
    if i==n:
        return None if n in s else s
    if i in s and i+1 in s:return None
    return tuple(j if j<=i else j-1 for j in s)

def differential(kind,r,n):
    src=basis(r,n);dst=basis(r,n-1);ix={v:j for j,v in enumerate(dst)}
    D=sp.zeros(len(dst),len(src))
    for c,(a,b) in enumerate(src):
        for i in range(n+1):
            aa=face(a,n,i);bb=face(b,n,i)
            if aa is None or bb is None:continue
            key=tuple(sorted((aa,bb)))
            if key not in ix:continue
            coefficient=2 if kind=='Gamma' and a!=b and aa==bb else 1
            D[ix[key],c]+=(-1)**i*coefficient
    return D

def gamma_expected(r):
    out={}
    stop=2*r-1 if r%2 else 2*r-2
    for i in range(r,stop+1,2):out[i]={'free_rank':0,'torsion':[2]}
    if r%2==0:out[2*r]={'free_rank':1,'torsion':[]}
    return out

all_data={}
for r in range(1,5):
    for kind in ['Sym','Gamma']:
        ds={n:differential(kind,r,n) for n in range(1,2*r+2)}
        for n in range(2,2*r+2):
            check(ds[n-1]*ds[n]==sp.zeros(ds[n-1].rows,ds[n].cols))
        hom={}
        for n in range(1,2*r+1):
            # ker d_n is a primitive direct summand of the free chain group,
            # hence the torsion of coker d_(n+1) is exactly H_n torsion.
            snf=smith_normal_form(ds[n+1],domain=ZZ)
            torsion=[abs(int(snf[i,i])) for i in range(min(snf.shape))
                     if abs(snf[i,i])>1]
            free=len(basis(r,n))-ds[n].rank()-ds[n+1].rank()
            if free or torsion:hom[n]={'free_rank':free,'torsion':torsion}
        if kind=='Gamma':expected=gamma_expected(r)
        elif r==1:expected={}
        elif r==2:expected={4:{'free_rank':1,'torsion':[]}}
        else:expected={i+4:v for i,v in gamma_expected(r-2).items()}
        check(hom==expected)
        all_data[f'{kind}_KZ{r}']={
            'bases':{str(n):basis(r,n) for n in range(r,2*r+1)},
            'differentials':{str(n):[[int(x) for x in row] for row in ds[n].tolist()]
                             for n in range(r,2*r+1)},
            'homology':hom}

# On Sym^2 K(Z,2), duality identifies the top coalgebra coefficient
# with the square of the weight-one cohomology generator of Gamma(Z[-2]).
D=differential('Sym',2,4)
z=D.nullspace()[0]
den=sp.ilcm(*[x.q for x in z]);z*=den
g=sp.igcd(*[int(x) for x in z]);z/=g
check(all(x.q==1 for x in z))
aw=0
for c,(a,b) in enumerate(basis(2,4)):
    if (a,b)==((1,2),(3,4)):aw+=z[c]
check(abs(aw)==1)
all_data['shift2_product']={'top_cycle':list(map(int,z)),
                            'Alexander_Whitney_coefficient':int(aw),
                            'PD_square_coefficient':2}
out={'assertions':checks,'elapsed_seconds':time.perf_counter()-start,
     'description':__doc__,'cases':all_data}
target=Path('SA08_work/logs/D_shift_quadratic_checks.json')
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'assertions':checks,'elapsed_seconds':out['elapsed_seconds'],
                  'output':str(target)}))
