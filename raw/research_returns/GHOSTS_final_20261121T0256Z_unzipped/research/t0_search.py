"""Search only: low-degree ordinary E^4 cycles; negative output is not proof."""
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from collections import Counter

def ka(x,y):return x[0]+y[0],x[1]+y[1]
def kn(x):return -x[0],-x[1]
def km(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]
def norm(x):return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def det(h):return ka(km(h[0],h[3]),kn(km(h[1],h[2])))
def add(*xs):
 d={}
 for x in xs:
  for a,v in x.items():d[a]=d.get(a,0)+v
 return {a:v for a,v in d.items() if v}
def scale(c,x):return {a:c*v for a,v in x.items() if c*v}
def wedge(x,y):
 d={}
 for a,c in x.items():
  for b,e in y.items():
   if set(a)&set(b):continue
   k=tuple(sorted(a+b));s=(-1)**sum(i>j for i in a for j in b)
   d[k]=d.get(k,0)+s*c*e
 return {a:v for a,v in d.items() if v}
def form(i):return {(i,):1}
def cmforms(q,k):
 a,b=q;u,v=form(2*k),form(2*k+1)
 return add(scale(a,u),scale(-b,v)),add(scale(b,u),scale(a-b,v))
basis=list(combinations(range(8),4))
def graph(h,inputs=(0,1)):
 outputs=[j for j in range(4) if j not in inputs]
 z={():1}
 for row,k in enumerate(outputs):
  pu,pv={},{}
  for col,i in enumerate(inputs):
   u,v=cmforms(h[2*row+col],i);pu=add(pu,u);pv=add(pv,v)
  z=wedge(z,add(form(2*k),scale(-1,pu)))
  z=wedge(z,add(form(2*k+1),scale(-1,pv)))
 return tuple(z.get(b,0) for b in basis)
def va(x,y):return tuple(a+b for a,b in zip(x,y))
def vs(x,y):return tuple(a-b for a,b in zip(x,y))
zero=(0,)*70
units=[q for q in product(range(-1,2),repeat=2) if norm(q)==1]
small=[(0,0)]+units
extra={}
for inputs in combinations(range(4),2):
 for h in product(small,repeat=4):
  D=2*(1+sum(map(norm,h))+norm(det(h)))
  if D<=6:
   v=graph(h,inputs)
   extra[v]=(D,inputs,h)
print('Extra irreducible counts:',Counter(x[0] for x in extra.values()),flush=True)
e2=[(v,data) for v,data in extra.items() if data[0]==2]
e4=[(v,data) for v,data in extra.items() if data[0]==4]
e6=[(v,data) for v,data in extra.items() if data[0]==6]
extras={0:{zero:[]},2:{v:[data] for v,data in e2},4:{v:[data] for v,data in e4},6:{v:[data] for v,data in e6}}
for (v,a),(w,b) in combinations_with_replacement(e2,2):extras[4][va(v,w)]=[a,b]
for (v,a),(w,b),(x,c) in combinations_with_replacement(e2,3):extras[6][va(va(v,w),x)]=[a,b,c]
for (v,a),(w,b) in product(e2,e4):extras[6][va(v,w)]=[a,b]
print('Extra cycle counts:',{D:len(vs) for D,vs in extras.items()},flush=True)
entries=[q for q in product(range(-2,3),repeat=2) if norm(q)<=5]
graphs={}
for h in product(entries,repeat=4):
 T=sum(map(norm,h))
 if T<=5 and norm(det(h))==1:
  D=2*(2+T);graphs[h]=(D,graph(h))
print('Dominant graph counts:',Counter(v[0] for v in graphs.values()),flush=True)
I=((1,0),(0,0),(0,0),(1,0));mI=tuple(kn(x) for x in I)
O=((0,1),(0,0),(0,0),(0,1));mO=tuple(kn(x) for x in O)
tstar=vs(va(graph(I),graph(mI)),va(graph(O),graph(mO)))
assert all(x%2==0 for x in tstar)
t0=tuple(x//2 for x in tstar)
for degree in [8,10,12,14]:
 cycles={}
 for h,(D,g) in graphs.items():
  if degree-D not in extras:continue
  for ex,data in extras[degree-D].items():
   cycles[va(g,ex)]=(h,data)
 print('Effective candidates degree',degree,':',len(cycles),flush=True)
 for v,data in cycles.items():
  target=vs(v,t0)
  if target in cycles:
   print('FOUND degree',degree,'plus',data,'minus',cycles[target],flush=True)
   raise SystemExit(0)
 print('No equality at degree',degree,flush=True)
