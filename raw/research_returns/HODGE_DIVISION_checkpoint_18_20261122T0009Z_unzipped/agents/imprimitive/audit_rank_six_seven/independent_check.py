#!/usr/bin/env python3
"""Independent reconstruction for D-BI16--17; no author code imported."""
from fractions import Fraction as Q
from itertools import product,combinations_with_replacement
from math import prod,lcm
from pathlib import Path
import json,sympy as s
root=Path(__file__).resolve().parent
x=s.symbols('x')
opts=[]
for p in [2,3,5,7]:
    row=[(1,1)];a=1
    while p**(a-1)*(p-1)<=6:
        row.append((p**a,p**(a-1)*(p-1)));a+=1
    opts.append(row)
orders=sorted({prod(v[0] for v in z) for z in product(*opts)
               if prod(v[1] for v in z)<=6})
assert orders==[1,2,3,4,5,6,7,8,9,10,12,14,18]
deg={}
for d in orders:
    fs=s.factor_list(s.cyclotomic_poly(d,x),extension=s.sqrt(-3))[1]
    ds={int(s.degree(p,x)) for p,e in fs};assert len(ds)==1
    deg[d]=next(iter(ds))
assert [d for d in orders if 1<deg[d]<=3]==[4,9,12,18]
profiles=[]
for r in [12,13,14]:
    for a,b in combinations_with_replacement([3,4,5],2):
        k=r-2;t=18-a-b-k
        if t==0:profiles.append((r,a,b,tuple([1]*k)))
        if t==1:profiles.append((r,a,b,tuple([1]*(k-1)+[2])))
        if t==2:
            profiles.extend([(r,a,b,tuple([1]*(k-2)+[2,2])),
                             (r,a,b,tuple([1]*(k-1)+[3]))])
assert len(profiles)==8
pairs=set()
for a,b in combinations_with_replacement([Q(j,6) for j in range(6)],2):
    if (a+b)%1 in [0,Q(1,2)]:
        pairs.add(tuple(sorted(((a+Q(1,4))%1,(b+Q(1,4))%1))))
assert len(pairs)==7
pairs=sorted(pairs)
for a,b in pairs:
    assert lcm(a.denominator,b.denominator,2) in [4,12]
    assert all((2*t)%1 for t in [a,b])
    assert 1+a+b==1+(Q(1,2)-a)%1+(Q(1,2)-b)%1
out={'status':'PASS independent whole-profile arithmetic',
     'all_phi_le_six_orders':orders,'factor_degrees_over_Qomega':deg,
     'rank_profiles':profiles,
     'outside_rank_four_residual_exponents':[[str(a),str(b)] for a,b in pairs],
     'recorded_limit':'Necessary ranks and spectra only; no tuple or class occurrence inferred.'}
(root/'independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS13 exact field cases,8 rank profiles,7 unordered residual pairs; all embedding ages checked.')
