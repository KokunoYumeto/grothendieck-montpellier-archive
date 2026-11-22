#!/usr/bin/env python3
"""Independent local-series audit of the parent's globally checked third GF64 contact candidate.

No claim about global smoothness or other singularities is made here.
"""
from pathlib import Path
import itertools,json,time
started=time.perf_counter()
MOD=0x43
def product(a,b):
 z=0
 for j in range(6):
  if (b>>j)&1:z^=a<<j
 for j in range(10,5,-1):
  if (z>>j)&1:z^=MOD<<(j-6)
 return z
def power(a,n):
 out=1
 for _ in range(n):out=product(out,a)
 return out
def reciprocal(a):
 assert a
 return power(a,62)
def plus(*items):
 out=0
 for item in items:out^=item
 return out
def dot(a,b):return plus(*(product(x,y) for x,y in zip(a,b)))
assert all(product(a,reciprocal(a))==1 for a in range(1,64))
def padd(a,b):return [x^y for x,y in zip(a,b)]
def pscale(a,c):return [product(x,c) for x in a]
def pmul(a,b):return [plus(*(product(a[i],b[j]) for i in range(3) for j in range(3) if i+j==n)) for n in range(3)]
def pinv(a):
 b=[reciprocal(a[0]),0,0]
 for n in range(1,3):b[n]=product(b[0],plus(*(product(a[i],b[n-i]) for i in range(1,n+1))))
 assert pmul(a,b)==[1,0,0]
 return b
def pdiv(a,b):return pmul(a,pinv(b))
def const(a):return [a,0,0]
one=const(1)
def yseries(x,y0):
 x3=pmul(pmul(x,x),x)
 y=[y0,x3[1],0];y[2]=x3[2]^product(y[1],y[1])
 assert padd(padd(pmul(y,y),y),x3)==[0,0,0]
 return y
def translate(P,g):
 x,y=P;u,v=g
 lam=pdiv(padd(y,const(v)),padd(x,const(u)))
 nu=padd(y,pmul(lam,x))
 xp=padd(padd(pmul(lam,lam),x),const(u))
 yp=padd(padd(pmul(lam,xp),nu),one)
 assert padd(padd(pmul(yp,yp),yp),pmul(pmul(xp,xp),xp))==[0,0,0]
 return xp,yp
s=[38,14,10,47,47,43,30,4,8]
u=[3,5,56,20,4,38,38,12,0]
P=((17,52),(8,53));Q=((18,35),(19,10));G=((58,59),(0,0))
def eval_scalar(s,P):return dot(s,[product(a,b) for a in (1,*P[0]) for b in (1,*P[1])])
def eval_series(s,P):
 out=[0,0,0]
 for i,a in enumerate((one,*P[0])):
  for j,b in enumerate((one,*P[1])):out=padd(out,pscale(pmul(a,b),s[3*i+j]))
 return out
def gradient(s,P):
 A=[1,*P[0]];B=[1,*P[1]]
 DA=[0,1,product(P[0][0],P[0][0])];DB=[0,1,product(P[1][0],P[1][0])]
 return [dot(s,[product(a,b) for a in DA for b in B]),dot(s,[product(a,b) for a in A for b in DB])]
assert eval_scalar(s,P)==eval_scalar(s,Q)==0
assert gradient(s,P)==gradient(s,Q)==[34,53]
M=[[[0,1,0],[0,0,1],[0,0,0]],[[1,0,0],[0,0,0],[0,0,1]],[[0,0,0],[1,0,0],[0,1,0]]]
A=[[0]*9 for _ in range(9)]
for a,b,i,j,k,l in itertools.product(range(3),repeat=6):
 if M[a][i][j] and M[b][k][l]:A[3*i+k][3*j+l]^=s[3*a+b]
assert [dot(row,u) for row in A]==[product(a,a) for a in s]
assert dot([product(a,a) for a in s],s[::-1])==0
det=plus(*(product(product(s[p[0]],s[3+p[1]]),s[6+p[2]]) for p in itertools.permutations(range(3))))
assert det==43
eta=eval_scalar(u,P)^eval_scalar(u,Q);assert eta==60
velocity=[53,34]
raw=[]
for (x0,y0),v in zip(P,velocity):
 x=[x0,v,0];raw.append((x,yseries(x,y0)))
raw_coefficient=eval_series(s,raw)[2]
correction=product(raw_coefficient,reciprocal(34))
branch=[]
for i,((x0,y0),v) in enumerate(zip(P,velocity)):
 x=[x0,v,correction if i==0 else 0];branch.append((x,yseries(x,y0)))
assert eval_series(s,branch)==[0,0,0]
translated=[translate(branch[i],G[i]) for i in range(2)]
assert tuple((x[0],y[0]) for x,y in translated)==Q
second=eval_series(s,translated)
assert second==[0,0,55]
result={'status':'LOCAL_PASS','coefficient_modulus':MOD,'Cartier_lift_identity':True,
 'determinant':det,'Hasse_cubic':0,'gradient_both':[34,53],
 'eta_difference':eta,'source_curve_series_through_order2':eval_series(s,branch),
 'translated_curve_series_through_order2':second,
 'global_smoothness_checked':False,'other_kernel_collisions_checked':False,
 'elapsed_seconds':time.perf_counter()-started}
path=Path(__file__).resolve().parent.parent/'outputs'/'verify_level3_contact03_local.json'
path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
