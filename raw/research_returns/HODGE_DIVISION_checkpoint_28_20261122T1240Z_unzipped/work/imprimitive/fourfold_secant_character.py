#!/usr/bin/env python3
"""Exact exterior-algebra certificate for HD-N11 (not a semiregularity test).
21 November 2026. GPT-6 Astra Pro, inherited effort, /root/imprimitive.
Variables 0..3 are holomorphic x_i; 4..7 are antiholomorphic y_i.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as S

a,b,d,s=S.symbols('a b d s')

def clean(p):
 return {m:S.expand(c) for m,c in p.items() if S.expand(c)!=0}
def add(*ps):
 out={}
 for p in ps:
  for m,c in p.items():out[m]=out.get(m,0)+c
 return clean(out)
def scale(p,c):return clean({m:c*v for m,v in p.items()})
def mul(p,q):
 out={}
 for m,c in p.items():
  for n,e in q.items():
   if m&n:continue
   inv=sum((n&((1<<i)-1)).bit_count() for i in range(8) if (m>>i)&1)
   out[m|n]=out.get(m|n,0)+(-1)**inv*c*e
 return clean(out)
def unit(i):return {1<<i:S.Integer(1)}
def wedge(i,p):return mul(unit(i),p)
def contract(i,p):
 return clean({m^(1<<i):(-1)**((m&((1<<i)-1)).bit_count())*c for m,c in p.items() if (m>>i)&1})
def op(j,p):return wedge(4+j,p) if j<4 else contract(j-4,p)
def exp(p):
 out={0:S.Integer(1)};q=out
 for k in range(1,5):q=mul(q,p);out=add(out,scale(q,S.Rational(1,S.factorial(k))))
 return out
H=add(*(mul(unit(i),unit(4+i)) for i in range(4)))
v=add(scale(exp(scale(H,s)),a+b*s),scale(exp(scale(H,-s)),a-b*s))
def dspecial(p):
 out={}
 for m,c in p.items():
  pol=S.Poly(c,s);z=0
  for (k,),coef in pol.terms():
   assert k%2==0
   z+=coef*(-d)**(k//2)
  out[m]=S.expand(z)
 return clean(out)
v=dspecial(v)
rows1=[m for m in range(256) if (m&15).bit_count()-(m>>4).bit_count()==-1]
rows2=[m for m in range(256) if (m&15).bit_count()-(m>>4).bit_count()==-2]
cols1=[op(j,v) for j in range(8)]
pairs=list(combinations(range(8),2))
cols2=[op(i,op(j,v)) for i,j in pairs]
M1=S.Matrix([[p.get(m,0) for p in cols1] for m in rows1])
M2=S.Matrix([[p.get(m,0) for p in cols2] for m in rows2])
# Choose independent rows/columns at a=b=d=1, then evaluate the exact minors.
def pivot_minor(M):
 sample=M.subs({a:1,b:1,d:1})
 ci=list(sample.rref()[1]);ri=list(sample[:,ci].T.rref()[1])
 return ri,ci,S.factor(M.extract(ri,ci).det(method='domain-ge'))
r1,c1,minor1=pivot_minor(M1)
r2,c2,minor2=pivot_minor(M2)
assert len(c1)==8 and len(c2)==12
norm=a*a+d*b*b
assert S.simplify(minor1/(d**4*norm**4)).is_nonzero
assert S.simplify(minor2/(d**6*norm**6)).is_nonzero
# The upper bound is verified universally in graph coordinates over Q(a,b,s).
vs={m:S.expand(c.subs(d,-s*s)) for m,c in v.items()}
def graph(i,sgn,p):return add(contract(i,p),scale(wedge(4+i,p),sgn*s))
mixed=[]
for i in range(4):
 for j in range(4):
  z=graph(i,1,graph(j,-1,vs));assert not z;mixed.append([i,j])
# The ordinary Riemann--Roch top coefficient; H^4/4! has orientation +1.
vd={m:(-1)**(m.bit_count()//2)*c for m,c in v.items()}
chi=S.factor(mul(v,vd).get(255,0))
assert S.expand(chi-32*d*d*norm)==0
samples=[]
for dd in [1,2,3,7,11,19,43,67,163]:
 for aa,bb in [(1,0),(0,1),(1,1)]:
  sub={a:aa,b:bb,d:dd}
  rank1=M1.subs(sub).rank();rank2=M2.subs(sub).rank()
  assert rank1==8 and rank2==12
  samples.append({'d':dd,'a':aa,'b':bb,'rank1':rank1,'rank2':rank2,'chi':int(chi.subs(sub))})
result={'statement':'HD-N11','date':'2026-11-21','author':'GPT-6 Astra Pro; inherited effort; /root/imprimitive',
 'matrices':{'c1_shape':list(M1.shape),'c2_shape':list(M2.shape)},
 'c1_minor':str(minor1),'c1_rows':r1,'c1_columns':c1,
 'c2_minor':str(minor2),'c2_rows':r2,'c2_columns':c2,
 'mixed_graph_pairs_zero':mixed,'euler_pairing':str(chi),'samples':samples,
 'scope':'Exact universal exterior and Euler certificate only; categorical trace, finite actions and semiregularity contradiction are proved in the TeX fragment.'}
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(result,indent=2)+'\n')
print('c1 rank8 exact minor:',minor1)
print('c2 rank12 exact minor:',minor2)
print('16 mixed graph columns vanish identically; Euler pairing:',chi)
print('27 exact field/character samples PASS; JSON:',p)
