#!/usr/bin/env python3
"""Exact finite arithmetic for B50; no remaining-pair existence claim."""
from pathlib import Path
from math import gcd
import json,time
start=time.perf_counter()
primes=(2,3,5,7,11,13,17,19,23,29,31,37,41,43)
log_cases=0;boundary_rows=[]
for p in primes:
 for a in range(1,p*p):
  q=min(a+1,p+1,p*p)
  assert (p-1)*q>=a
  J=(a+p-2)//(p-1)
  assert q>=J and a>=J
  log_floor=0;next_power=p
  for n in range(1,1001):
   if n==next_power:log_floor+=1;next_power*=p
   assert (p-1)*log_floor<=n-1
   assert n*q-a*log_floor>=q
   log_cases+=1
 a=p*p-1;q=min(a+1,p+1,p*p)
 assert q==p+1 and q*(p-1)==a
 boundary_rows.append({'p':p,'a':a,'q1':q,'J_exponent':q,'boundary_included':True})

def trim(poly,p):
 poly=[x%p for x in poly]
 while poly and poly[-1]==0:poly.pop()
 return poly

def rem(a,b,p):
 a=trim(a,p);b=trim(b,p)
 while len(a)>=len(b) and a:
  c=a[-1]*pow(b[-1],-1,p)%p;k=len(a)-len(b)
  for j,x in enumerate(b):a[j+k]=(a[j+k]-c*x)%p
  a=trim(a,p)
 return a

def pgcd(a,b,p):
 while b:a,b=b,rem(a,b,p)
 c=pow(a[-1],-1,p)
 return [(c*x)%p for x in a]

spectral_rows=[];crt_cases=0;normalization_cases=0
for p in primes:
 if p<5:continue
 d=next(i for i in range(2,p) if pow(i,(p-1)//2,p)==p-1)
 def mul(x,y):return ((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
 def power(x,n):
  ans=(1,0)
  while n:
   if n&1:ans=mul(ans,x)
   x=mul(x,x);n//=2
  return ans
 N=p*p-1;prime_factors=[];z=N;l=2
 while l*l<=z:
  if z%l==0:
   prime_factors.append(l)
   while z%l==0:z//=l
  l+=1
 if z>1:prime_factors.append(z)
 g=next((i,j) for i in range(p) for j in range(p) if (i,j)!=(0,0) and all(power((i,j),N//q)!=(1,0) for q in prime_factors))
 h=power(g,p-1)
 assert power(h,p+1)==(1,0)
 polys=[];roots=[]
 for e in range(p+1):
  x=power(h,e);y=power(x,p)
  assert mul(x,y)==(1,0)
  roots.append(frozenset((x,y)))
  poly=[-x[0],1] if x==y else [1,-(x[0]+y[0]),1]
  polys.append(trim(poly,p))
 for i in range(p+1):
  for j in range(i+1,p+1):
   if roots[i]!=roots[j]:
    assert not roots[i].intersection(roots[j])
    assert pgcd(polys[i],polys[j],p)==[1]
    crt_cases+=1
 odd=p+1
 while odd%2==0:odd//=2
 expected={N//d for d in range(1,odd+1) if odd%d==0}
 actual=set()
 for c in range(N):
  if gcd(c,p-1)==1:
   divisor=gcd(c,N)
   assert divisor%2==1 and (p+1)%divisor==0
   actual.add(N//divisor);normalization_cases+=1
 assert actual==expected
 assert min(actual)>p+1
 spectral_rows.append({'p':p,'irreducible_quadratic_parameter':d,'norm_one_projector_checks':True,'normalized_remaining_joint_degrees':sorted(actual)})
assert next(x for x in spectral_rows if x['p']==5)['normalized_remaining_joint_degrees']==[8,24]
assert next(x for x in spectral_rows if x['p']==7)['normalized_remaining_joint_degrees']==[48]
out={'status':'PASS','scope':'Closed coefficientwise logarithm inequalities and finite tame-spectrum arithmetic; no formal-group realization or remaining-pair existence claim.','logarithm_cases':log_cases,'crt_spectral_pairs':crt_cases,'primitive_norm_exponents':normalization_cases,'boundary_rows':boundary_rows,'spectral_rows':spectral_rows,'elapsed_seconds':time.perf_counter()-start}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
