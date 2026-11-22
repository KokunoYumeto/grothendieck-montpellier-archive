#!/usr/bin/env python3
"""Exact finite auxiliary checks for B49; no model-existence assertion.

The p-series coefficients are reconstructed from f([p]T)=p f(T),
where f=T+(u/p)T^p+(1/p+u^(p+1)/p^2)T^(p^2)+O(T^(p^3)).
We retain all coefficients through degree p^2 using the mu_(p-1)
grading, independently of the valuation lemma's arithmetic.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd, lcm
import json,time
import sympy as S
start=time.perf_counter()
u=S.symbols('u')

def mul(a,b,N):
 out=[S.Integer(0)]*(N+1)
 for i,x in enumerate(a):
  if x==0:continue
  for j,y in enumerate(b):
   if i+j>N:break
   if y!=0:out[i+j]+=x*y
 return [S.expand(x) for x in out]
def power(a,p,N):
 r=[S.Integer(1)]+[S.Integer(0)]*N
 for _ in range(p):r=mul(r,a,N)
 return r
coefficient_rows=[]
for p in (2,3,5,7,11):
 # [p](T)=T H(T^(p-1)); H determined up to degree p+1.
 H=[S.Integer(p)]
 l2=S.Rational(1,p)+u**(p+1)/p**2
 for k in range(1,p+2):
  rhs=(u if k==1 else 0)+((p-p**(p*p))*l2 if k==p+1 else 0)
  ck=S.expand(rhs-S.Rational(1,p)*u*power(H,p,k-1)[k-1])
  assert all(c.q==1 for c in S.Poly(ck,u).all_coeffs())
  H.append(ck)
 assert S.expand(H[1]-(1-p**(p-1))*u)==0
 for k in range(2,p+1):assert H[k].subs(u,0)==0
 assert H[p+1].subs(u,0)==1-p**(p*p-1)
 P=power(H,p,p)
 lhs=H[:]
 for k in range(1,p+2):lhs[k]=S.expand(lhs[k]+u*P[k-1]/p)
 lhs[p+1]=S.expand(lhs[p+1]+l2*p**(p*p))
 rhs=[S.Integer(p),u]+[S.Integer(0)]*(p-1)+[p*l2]
 assert len(lhs)==len(rhs)
 assert all(S.expand(x-y)==0 for x,y in zip(lhs,rhs))
 coefficient_rows.append({'p':p,'through_degree':p*p,'nonlinear_terms':len(H)-1,'integral':True,'identity':True,'p_coefficient':str(H[1]),'p_squared_constant':str(H[-1].subs(u,0))})

primes=(2,3,5,7,11,13,17,19,23,29,31,37,41,43)
valuation_rows=[];valuation_cases=0
for p in primes:
 bound=(p-1)*(p*p-1)
 count=0;admissible=0
 for A in range(1,p):
  for b in range(1,p*p-p*A):
   Z=b+p*A
   assert 1<=A and Z<=p*p-1
   a=b+(p-1)*Z
   assert a==p*(b+(p-1)*A)
   assert a%p==0
   assert (p*p-p)*Z>b
   if a<=bound:
    assert a+A>Z and p*p*A>Z
    assert b<a
    admissible+=1
   count+=1
 valuation_cases+=count
 valuation_rows.append({'p':p,'cancellation_configurations':count,'within_absolute_bound':admissible,'prime_to_p_absolute_indices':0})

tame_rows=[];degree_cases=0;determinant_cases=0
for p in primes:
 if p<5:continue
 n=p*p-1
 div=[d for d in range(1,n+1) if n%d==0]
 for a in div:
  assert a%p!=0
  assert (p-1)*a<=(p-1)*(p*p-1)<(p-1)*p*p
  for b in div:
   m=lcm(a,b);assert n%m==0
   assert m%p!=0
   degree_cases+=1
 mod=p*p
 for delta in range(-2,3):
  for residue in range(1,p):
   epsilon=pow(residue,p,mod)
   assert pow(epsilon,p-1,mod)==1
   equality=pow(1+p,delta,mod)*epsilon%mod==1
   assert equality==(delta==0 and residue==1)
   determinant_cases+=1
 tame_rows.append({'p':p,'possible_joint_degrees':div,'p_squared_remaining_joint_degrees':[m for m in div if m>p],'p_cubed_sufficiency_bound':True})
result={'status':'PASS','scope':'Exact finite coefficient/cancellation/degree/determinant checks only; no formal-model existence or least-index evaluation.','coefficient_rows':coefficient_rows,'valuation_rows':valuation_rows,'valuation_cases':valuation_cases,'tame_rows':tame_rows,'joint_degree_cases':degree_cases,'determinant_cases':determinant_cases,'elapsed_seconds':time.perf_counter()-start}
out=Path(__file__).with_suffix('.output.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
