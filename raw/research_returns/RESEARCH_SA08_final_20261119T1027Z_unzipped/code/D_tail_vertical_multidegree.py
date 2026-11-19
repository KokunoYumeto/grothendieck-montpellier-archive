#!/usr/bin/env python3
"""Integral H2 lattice checks for D_N in two variables, T-multidegree zero."""
from math import comb,factorial,gcd
from pathlib import Path
import json,time
start=time.perf_counter()
def multi(n,aa):
    if min(aa)<0 or sum(aa)!=n:return 0
    v=factorial(n)
    for a in aa:v//=factorial(a)
    return v
rows=[]
for N in [2,3,4]:
 for alpha in range(1,13):
  for beta in range(1,13-alpha):
   w=alpha+beta
   if w<N:continue
   E=0
   for a in range(alpha+1):
    for b in range(beta+1):
     if a+b!=0 and a+b<N:continue
     if w-a-b<N:continue
     u=comb(alpha-1,a)*comb(beta,b) if a<alpha else 0
     v=comb(alpha,a)*comb(beta-1,b) if b<beta else 0
     E=gcd(E,v-u)
   G=0
   for a0 in range(alpha+1):
    for b0 in range(beta+1):
     if a0+b0!=0 and a0+b0<N:continue
     for a1 in range(alpha-a0+1):
      for b1 in range(beta-b0+1):
       a2=alpha-a0-a1;b2=beta-b0-b1
       if a1+b1<N or a2+b2<N:continue
       u=multi(alpha-1,(a0,a1-1,a2))*multi(beta-1,(b0,b1,b2-1))
       v=multi(alpha-1,(a0,a1,a2-1))*multi(beta-1,(b0,b1-1,b2))
       G=gcd(G,u-v)
   assert (not E) or G and E%G==0
   quotient=E//G if G else 1
   rows.append({'N':N,'alpha':alpha,'beta':beta,'dD1_index':E,
                'D2_index':G,'H2_order':quotient})
out={'cases':rows,'elapsed_seconds':time.perf_counter()-start,'description':__doc__}
Path('SA08_work/logs/D_tail_vertical_multidegree.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'cases':len(rows),'elapsed_seconds':out['elapsed_seconds'],
                  'nonzero':[r for r in rows if r['H2_order']!=1]}))
