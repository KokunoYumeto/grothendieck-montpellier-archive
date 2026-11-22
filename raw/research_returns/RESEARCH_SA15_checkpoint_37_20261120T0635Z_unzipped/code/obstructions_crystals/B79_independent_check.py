"""Finite exact supplement for B79; no image or formal-pair existence inferred."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from math import isqrt
from itertools import product
from collections import Counter
import time,json
started=time.perf_counter(); counts=Counter(); rows=[]
primes=[p for p in range(5,102) if all(p%d for d in range(2,isqrt(p)+1))]

def matrix_mul(A,B,m):
 return ((A[0]*B[0]+A[1]*B[2])%m,(A[0]*B[1]+A[1]*B[3])%m,
         (A[2]*B[0]+A[3]*B[2])%m,(A[2]*B[1]+A[3]*B[3])%m)

def matrix_power(A,n,m):
 R=(1,0,0,1)
 while n:
  if n&1:R=matrix_mul(R,A,m)
  A=matrix_mul(A,A,m); n//=2
 return R

for p in primes:
 q=p*p; N=q-1; e=p*(p-1); A=p-1
 for r in range(9):
  val=Fraction(e*p**r,q*q)
  assert (val.denominator==1)==(r>=3)
  counts['valuation_denominator_cases']+=1
 assert Fraction(e*p**3,q*q)==A
 assert e*N*p**3==N*q*q*A
 assert e*p**3==q*q*A
 possibilities=[]
 for s in range(5):
  for t in range(5):
   if s+t==3 and 0<s<=t:possibilities.append((s,t))
   counts['layer_dimension_cases']+=1
 assert possibilities==[(1,2)]
 # Every pth matrix binomial coefficient beyond the linear contribution
 # has sufficient p-adic valuation; the p^2B contribution also disappears.
 assert all((pow(p,j)*__import__('math').comb(p,j))%(p**3)==0 for j in range(2,p+1))
 counts['universal_p_power_divisibility_rows']+=1
 b=(q*q-1)*A
 assert b%N==0 and N*q*q*A>q*q*A
 for j in range(A+1,A+41):
  k=j; v=0
  while k%p==0:k//=p;v+=1
  assert j+p**v*b>A+b
  counts['higher_uniformizer_term_checks']+=1
 d=next(x for x in range(2,p) if pow(x,(p-1)//2,p)==p-1)
 def mul(x,y):return ((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
 def power(x,n):
  y=(1,0)
  while n:
   if n&1:y=mul(y,x)
   x=mul(x,x);n//=2
  return y
 one=(1,0); eta=(0,1); fp_eta=power(eta,p)
 assert fp_eta==(0,p-1) and fp_eta!=eta
 for x in product(range(p),repeat=2):
  assert power(x,q*q)==x
  counts['q_squared_field_identities']+=1
  # Testing 1 and eta already refutes every possible scalar Frobenius.
  assert not (mul(x,one)==one and mul(x,eta)==fp_eta)
  counts['frobenius_scalar_candidates']+=1
 rows.append({'p':p,'e':e,'minimal_wild_degree':p**3,'primitive_integral_valuation':A,
              'first_level_integral_valuation':q*q*A,'terminal_lower_break':b,
              'remaining_wild_exponents':list(range(4,9))})

I=(1,0,0,1)
Bs=[(0,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)]
for p in (5,7,11):
 m=p**3
 for A in product(range(p),repeat=4):
  target=tuple((I[j]+p*p*A[j])%m for j in range(4))
  for B in Bs:
   g=tuple((I[j]+p*A[j]+p*p*B[j])%m for j in range(4))
   assert matrix_power(g,p,m)==target
   counts['exact_mod_p3_matrix_power_checks']+=1
out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-started,'counts':dict(counts),'rows':rows,
     'scope':'Exact finite valuation, dimension, full coefficient-divisibility, mod-p3 matrix-power, fixed higher-term and Fq scalar/Frobenius checks. The common-field and formal-group arguments are the written proof; no existence of any larger wild image or different-character pair is asserted.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
