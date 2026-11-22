"""Exact exceptional coefficient check and finite audit of all index recipes."""
import sympy as S,json,time
from pathlib import Path
start=time.monotonic();P=S.symbols('P');e=10
G=S.groebner([P**10+3*P**5+3],P,domain=S.QQ)
def red(a):return S.expand(G.reduce(S.expand(a))[1])
def vp3(a):
 a=S.Rational(a);n,d=int(a.p),int(a.q);v=0
 while n%3==0:n//=3;v+=1
 while d%3==0:d//=3;v-=1
 return v
def val(a):return min(e*vp3(c)+k[0] for k,c in S.Poly(red(a),P).terms() if c)
w=P**2;t=1+w;a=-3*t*(t**3+8);b=2*(t**6-20*t**3-8);r=P**4+P**6
coeff=[red(r**3+a*r+b),red(3*r*r+a),red(3*r),S.Integer(1)]
assert [val(c) for c in coeff]==[22,16,14,0]
checks=[]
for ee in range(2,10002,2):
 for m in [3,6,12]:
  if m==3 and ee==2:continue
  exceptions={3:{4,8,10},6:{2,4,6,14},12:{2}}[m]
  if ee in exceptions:continue
  if m==12:rr=1 if (ee+1)%3 else 3
  elif m==6:
   rr=(2 if (ee+2)%3 else 6) if ee%4==0 else (4 if (ee+4)%3 else 8)
  else:
   rr=(4 if (ee+4)%3 else 8) if ee%4==0 else (2 if (ee+2)%3 else 6)
  assert 0<2*rr<ee and (ee+rr)%3
  from math import gcd
  assert 12//gcd(4,ee+rr)==m
  checks.append((ee,m,rr))
out={'exception_e10':{'minimal_polynomial':'P^10+3P^5+3','Hesse_parameter':'1+P^2','translation':'X=P^4+P^6+Z','coefficients':[str(z) for z in coeff],'valuations':[val(z) for z in coeff]},'recipe_audit':{'even_e_through':10000,'count':len(checks),'all_passed':True,'exceptions':{'3':[4,8,10],'6':[2,4,6,14],'12':[2]}},'seconds':time.monotonic()-start}
print(json.dumps(out,indent=2))
