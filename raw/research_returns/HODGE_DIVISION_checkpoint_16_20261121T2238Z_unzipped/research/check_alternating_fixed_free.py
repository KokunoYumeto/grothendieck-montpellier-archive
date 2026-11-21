#!/usr/bin/env python3
"""Exact supplements for ALT07, not a substitute for the universal proof."""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
from fractions import Fraction as F
from math import factorial,comb,prod
import sympy as s
import json,hashlib,time
start=time.perf_counter();root=Path(__file__).resolve().parent
n,k,c,x=s.symbols('n k c x')
beta=k*(n-1-k)/((n-1)*(n-2))
assert s.simplify(beta.subs(k,c*n)-c*(1-c)-c*((2-3*c)*n-2+2*c)/((n-1)*(n-2)))==0
assert s.simplify(s.diff(beta,k)-(n-1-2*k)/((n-1)*(n-2)))==0
assert s.expand((n*n-11*n-8).subs(n,15+x))==x*x+19*x+52
assert s.expand((n*n-8*n+8).subs(n,15+x))==x*x+22*x+113
assert s.expand((13*n*n-151*n+48).subs(n,15+x))==13*x*x+239*x+708
assert s.factor((13*n-16)*(n-3)-96*n)==13*n*n-151*n+48
# Exact radical-threshold comparisons, with no floating point premise.
assert F(3,5)<F(4,5)**2 and F(3,5)>F(3,4)**2
assert (2*F(22,25)-1)**2<F(3,5) # .88 is below the new long-row threshold.

def partitions(n,cap=None):
 if n==0:
  yield ();return
 for v in range(min(n,cap or n),0,-1):
  for rest in partitions(n-v,v):yield (v,)+rest

def degree(shape):
 n=sum(shape);hooks=[]
 for i,row in enumerate(shape):
  for j in range(row):hooks.append(row-j+sum(r>j for r in shape[i+1:]))
 h=prod(hooks);assert factorial(n)%h==0;return factorial(n)//h

@lru_cache(None)
def domino_character(shape):
 if not shape:return 1
 answer=0
 for i,a in enumerate(shape):
  nxt=shape[i+1] if i+1<len(shape) else 0
  if a>=2 and a-2>=nxt:
   p=list(shape);p[i]-=2;p=tuple(z for z in p if z)
   answer+=domino_character(p)
  if i+1<len(shape) and a==nxt and a-1>=(shape[i+2] if i+2<len(shape) else 0):
   p=list(shape);p[i]-=1;p[i+1]-=1;p=tuple(z for z in p if z)
   answer-=domino_character(p)
 return answer

assert domino_character((2,))==1 and domino_character((1,1))==-1
assert domino_character((2,2))==2 and domino_character((3,1))==-1
rows=[];tot=0;long_count=0
for nn in range(16,25,2):
 mm=nn//2;count=0;long=0
 for shape in partitions(nn):
  aa=degree(shape);ch=domino_character(shape)
  assert ch*ch*factorial(nn)<=factorial(mm)**2*4**mm*aa
  if F(3*nn,4)<shape[0]<nn-1:
   kk=nn-shape[0];assert aa>=F(nn*(nn-3),2)>4*(nn+1)
   assert 4*ch*ch<aa*aa
   bb=F(kk*(nn-1-kk),(nn-1)*(nn-2));assert bb<F(1,4)
   long+=1
  count+=1
 assert 4**mm<=comb(nn,mm)*(nn+1)
 rows.append({'n':nn,'partitions':count,'nonstandard_long_shapes':long})
 tot+=count;long_count+=long

nn=100;kk=12
T=F(nn*(nn-1),2)-kk*(nn-kk+1)
S0=F((nn-kk-1)*(nn-kk)*(2*nn-2*kk-1),6)
V=4*(T*T+nn*(nn-1)-3*S0)/F(nn*(nn-1)*(nn-2)*(nn-3))
bb=F(kk*(nn-1-kk),(nn-1)*(nn-2))
old=min(F(1,4),bb,(1-V)/4)
aa=comb(nn,kk)-comb(nn,kk-1)
assert old==F(1519571,15684900)<F(1,10)
assert bb==F(58,539)>F(1,10)+F(3,5*aa)
assert aa==908791246463100
out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-start,'proof_sha256':hashlib.sha256((root/'ordinary_alternating_fixed_free_section.tex').read_bytes()).hexdigest(),'symbolic_checks':['exact beta difference','monotonicity derivative','all three shifted positivity polynomials','cross-multiplied degree correction','rational radical brackets'],'domino_character_method':'Exact signed horizontal/vertical rim-domino recursion with hook-length degree','finite_rows':rows,'total_partitions':tot,'nonstandard_long_shapes':long_count,'witness':{'n':nn,'shape':[88,12],'degree':aa,'old_delta':str(old),'new_beta':str(bb)},'scope':'Universal proof is in TeX. Finite Fomin-Lulov/domino and exact polynomial checks supplement it; no character-table extrapolation or TeX compilation.'}
(root/'alternating_fixed_free_checked.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
