"""Exact finite-field exploration; no conclusion until lifted and checked."""
from itertools import product
from collections import Counter
import json,sys
from pathlib import Path

p=int(sys.argv[1]) if len(sys.argv)>1 else 41
rprime=int(sys.argv[2]) if len(sys.argv)>2 else 11
eps=int(sys.argv[3]) if len(sys.argv)>3 else 1
d=next(i for i in range(2,p) if pow(i,(p-1)//2,p)==p-1)
O=None
zero=(0,0);one=(1,0)
def add(a,b):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def neg(a):return ((-a[0])%p,(-a[1])%p)
def sub(a,b):return add(a,neg(b))
def mul(a,b):return ((a[0]*b[0]+d*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def inv(a):
 u=pow((a[0]*a[0]-d*a[1]*a[1])%p,-1,p)
 return (a[0]*u%p,-a[1]*u%p)
def div(a,b):return mul(a,inv(b))
def scale(n,a):return(n*a[0]%p,n*a[1]%p)
def plus(P,Q):
 if P is None:return Q
 if Q is None:return P
 x,y=P;u,v=Q
 if x==u and add(y,v)==zero:return None
 s=div(sub(v,y),sub(u,x)) if x!=u else div(add(scale(3,mul(x,x)),(-30%p,0)),scale(2,y))
 z=sub(sub(mul(s,s),x),u)
 return z,sub(mul(s,sub(x,z)),y)
def minus(P):return None if P is None else (P[0],neg(P[1]))
def times(n,P):
 R=None
 while n:
  if n&1:R=plus(R,P)
  P=plus(P,P);n//=2
 return R
def frob(P):return None if P is None else ((P[0][0],-P[0][1]%p),(P[1][0],-P[1][1]%p))
elts=list(product(range(p),repeat=2))
squares={}
for y in elts:squares.setdefault(mul(y,y),[]).append(y)
points=[None]
for x in elts:
 f=add(add(mul(mul(x,x),x),scale(-30,x)),(-25%p,0))
 for y in squares.get(f,[]):points.append((x,y))
tors8=[P for P in points if times(8,P) is None]
tors2=[P for P in points if P is not None and times(2,P) is None]
tors11=[P for P in points if P is not None and times(rprime,P) is None and frob(P)==(P if eps==1 else minus(P))]
print('field',p,d,'#E2',len(points),'E[8] rational',len(tors8),'R11',tors11,flush=True)
records=[]
for T in tors2:
 unused=set(P for P in tors8 if times(2,P) is not None and times(2,P)!=T)
 orbs=[]
 while unused:
  U=min(unused)
  orb={U,minus(U),plus(U,T),plus(minus(U),T)}
  unused-=orb
  orbs.append((U,frob(U) in ({U,plus(U,T)} if eps==1 else {minus(U),plus(minus(U),T)})))
 print('T',T,'stable orbits',orbs,flush=True)
 if len(orbs)<3:continue
 for U,sgn in orbs:
  if not sgn:continue
  rest=[V for V,_ in orbs if V!=U]
  for V,W in __import__('itertools').combinations(rest,2):
   vw={V,minus(V),plus(V,T),plus(minus(V),T),W,minus(W),plus(W,T),plus(minus(W),T)}
   if frob(V) not in vw or frob(W) not in vw:continue
   for R in tors11[:3]:
    Ps=[U,plus(U,R),V,W]
    roots=[]
    for P in Ps:roots.extend([P[0],plus(P,T)[0]])
    if len(set(roots))<8:continue
    e=T[0]
    B=add(scale(3,mul(e,e)),(-30%p,0))
    # fixed points of translation on Kummer: (x-e)^2=B.
    poly=[sub(mul(e,e),B),scale(-2,e),one]
    for r in roots:
     out=[zero]*(len(poly)+1)
     for j,c in enumerate(poly):
      out[j]=sub(out[j],mul(r,c));out[j+1]=add(out[j+1],c)
     poly=out
    assert all(c[1]==0 for c in poly)
    coeff=[c[0] for c in poly]
    rec={'degeneration_prime':rprime,'epsilon':eps,'split_T':pow(B[0],(p-1)//2,p)==1,'T':T,'U':U,'V':V,'W':W,'R':R,'poly':coeff}
    records.append(rec)
print('curves',len(records),flush=True)
Path(f'work/C25_candidates_{p}.json').write_text(json.dumps({'prime':p,'nonsquare':d,'curves':records},indent=2))
