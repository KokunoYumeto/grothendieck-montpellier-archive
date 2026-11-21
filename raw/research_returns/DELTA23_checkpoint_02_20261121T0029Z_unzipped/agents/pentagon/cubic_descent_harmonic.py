#!/usr/bin/env python3
"""Exact signed harmonic quotient computation for D23.P13."""
import json,pathlib
from collections import deque

# R=(Z/4)[w], w^2+w+1=0, encode a+bw by a+4b.
def add(a,b):return (a%4+b%4)%4+4*((a//4+b//4)%4)
def neg(a):return (-a%4)%4+4*((-(a//4))%4)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 x,y=a%4,a//4;z,t=b%4,b//4
 return (x*z-y*t)%4+4*((x*t+y*z-y*t)%4)
def power(a,n):
 r=1
 for _ in range(n):r=mul(r,a)
 return r
w=4;c=14;assert add(add(mul(w,w),w),1)==0 and mul(sub(1,w),c)==1
units=[power(neg(w),j) for j in range(6)];assert len(set(units))==6
I=(0,1)
def am(a,b):return add(a[0],mul(a[1],b[0])),mul(a[1],b[1])
def ai(a):
 u=next(v for v in units if mul(a[1],v)==1)
 return neg(mul(u,a[0])),u
def ap(a,n):
 if n<0:return ap(ai(a),-n)
 r=I
 for _ in range(n):r=am(r,a)
 return r
s=(c,3);r=(c,w);tau=am(s,r);x=ap(tau,-2);y=am(am(s,x),s)
assert ap(s,2)==ap(r,3)==I
assert tau==(0,neg(w)) and x==(0,w) and y==(1,w)
srs=am(am(s,r),s);assert srs==(neg(mul(w,c)),w)
seen={I};todo=deque([I])
while todo:
 a=todo.popleft()
 for g in [s,r]:
  b=am(a,g)
  if b not in seen:seen.add(b);todo.append(b)
assert len(seen)==96
for k in range(16):
 C=(mul(c,k),1);g=(mul(mul(w,w),mul(c,k)),1)
 f0=am(am(am(am(s,ai(C)),s),g),C)
 assert f0==(k,1)
 for t in [0,3,6,9]:assert am(am(ap(y,-t),f0),ap(x,t))==(k,1)
phases=[]
for rho in range(3):
 for e in range(2):
  phase=mul(power(w,rho),3 if e else 1)
  k=mul(c,sub(1,phase));assert sub(1,mul(sub(1,w),k))==phase
  phases.append({'rho':rho,'a2':e,'phase':phase,'k':k})
assert len({r['phase'] for r in phases})==6
out={'statement':'D23.P13','ring':'Z/4[w],w^2+w+1=0; encode a+4b','s':s,'r':r,'tau':tau,'x':x,'y':y,'srs':srs,'group_order':len(seen),'translation_cases':16,'normalization_checks':64,'six_harmonic_phases':phases,'result':'PASS'}
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
