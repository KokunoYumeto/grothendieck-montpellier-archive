#!/usr/bin/env python3
"""Different-method exact corroboration of the characteristic-five example.

Run: python workbench/programs/check_zheng_v1_counterexample.py
The geometric construction and cohomology proof are in the correction records.
"""
from pathlib import Path
from fractions import Fraction
import json

mod, precision = 5, 150
def add(x,y):return [(a+b)%mod for a,b in zip(x,y)]
def mul(x,y):
 z=[0]*precision
 for i,a in enumerate(x):
  if a:
   for j,b in enumerate(y[:precision-i]):
    if b:z[i+j]=(z[i+j]+a*b)%mod
 return z
def power(x,n):
 z=[1]+[0]*(precision-1)
 while n:
  if n&1:z=mul(z,x)
  x=mul(x,x);n//=2
 return z
t=[0,1]+[0]*(precision-2)
t5=power(t,5)
z=t5
iterations=0
while True:
 nxt=add(t5,[-x%mod for x in mul(t,power(z,8))])
 iterations+=1
 if nxt==z:break
 z=nxt
 assert iterations<precision
# From t=y/x² and y⁵-y=x⁹, z=1/x satisfies z+t z⁸=t⁵.
assert add(z,mul(t,power(z,8)))==t5
valuation=lambda c:next(i for i,a in enumerate(c) if a)
dz=[(i*z[i])%mod for i in range(1,precision)]+[0]
assert valuation(z)==5 and valuation(dz)==40
assert valuation(dz)-2*valuation(z)==30
g=1+30//2
assert g==16
count=4
# Compute on the ruled surface first, then transform under degree-six pullback.
KP=(-2,36); branch=(6,-30)
Kpull=tuple(Fraction(KP[i])+Fraction(5,6)*branch[i] for i in range(2))
assert Kpull==(3,11)
K=(6*Kpull[0],Kpull[1]);Z=(1,1)
A=tuple(24*Z[i]-K[i] for i in range(2))
assert K==(18,11) and A==(6,13)
pair=lambda x,y:x[0]*y[0]+x[0]*y[1]+x[1]*y[0]
assert (pair(Z,Z),pair(K,Z),pair(K,K),pair(A,A))==(3,47,720,192)
count+=3
# Independent Euler calculation via six cyclic weights on the ruled surface.
weights=[]
for i in range(6):
 a,b=-i,5*i
 chi=(a+1)*(1-g+b)+Fraction(6*a*(a+1),2)
 assert chi.denominator==1
 weights.append(int(chi));count+=1
assert weights==[-15,0,11,18,21,20] and sum(weights)==55
eC=2-2*g;eP=2*eC;eBranch=2*eC;eX=6*eP-5*eBranch
assert eX==-60 and pair(K,K)+eX==12*sum(weights)
count+=2
# Čech/Serre-duality ranks and degree of the quotient-generated subline.
summands=[]
for i in range(2,6):
 twist=5*i-7; quotient=6*(i-2)
 subline_degree=twist-quotient
 assert subline_degree==5-i
 assert subline_degree>=0
 summands.append(dict(weight=i,rank=i-1,twist=twist,quotient_degree=quotient,subline_degree=subline_degree))
 count+=2
assert summands[-1]['subline_degree']==0
count+=1
out={'status':'PASS','assertions':count,'formal_series_precision':precision,
     'formal_series_iterations':iterations,'ord_z':valuation(z),'ord_dz':valuation(dz),
     'ord_dx':30,'genus':g,'canonical_coefficients':[int(x) for x in K],
     'ample_difference_coefficients':[int(x) for x in A],
     'cyclic_weight_euler_characteristics':weights,'chi_X':sum(weights),'c2_X':eX,
     'nonvanishing_summands':summands,
     'scope':'Arithmetic and local formal-series corroboration only; full smoothness, all-curve ampleness and nonvanishing are proved geometrically in the frozen record'}
(Path(__file__).resolve().parents[1]/'records/ZHENG_V1_COUNTEREXAMPLE_ARITHMETIC.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
