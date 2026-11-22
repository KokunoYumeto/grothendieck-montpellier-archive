#!/usr/bin/env python3
"""Exact algebra supplement for D-HOS11--12, with explicit finite scope."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json,time
import sympy as s

base=Path(__file__).resolve().parent
start=time.perf_counter()
p=3
def eye(d):return tuple(tuple(int(i==j) for j in range(d)) for i in range(d))
def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))%p for j in range(len(b[0]))) for i in range(len(a)))
def add(a,b):return tuple(tuple((x+y)%p for x,y in zip(r,t)) for r,t in zip(a,b))
def scale(a,c):return tuple(tuple(c*x%p for x in r) for r in a)
def trans(a):return tuple(zip(*a))
def mv(a,v):return tuple(sum(x*y for x,y in zip(r,v))%p for r in a)
def power(a,k):
 r=eye(len(a))
 for _ in range(k):r=mul(r,a)
 return r
def rank(a):
 a=[list(r) for r in a];i=0
 for j in range(len(a[0])):
  k=next((k for k in range(i,len(a)) if a[k][j]),None)
  if k is None:continue
  a[i],a[k]=a[k],a[i];t=pow(a[i][j],-1,p);a[i]=[t*x%p for x in a[i]]
  for k in range(len(a)):
   if k!=i:
    t=a[k][j];a[k]=[(x-t*y)%p for x,y in zip(a[k],a[i])]
  i+=1
  if i==len(a):break
 return i
def bv(v,w,j):return sum(x*y for x,y in zip(v,mv(j,w)))%p
def tv(v,c,j):
 r=tuple(sum(v[k]*j[k][l] for k in range(len(v)))%p for l in range(len(v)))
 return add(eye(len(v)),tuple(tuple(c*x*y%p for y in r) for x in v))
j=((0,1),(2,0))
gl=cases=zero=0
for data in product(range(3),repeat=4):
 h=(data[:2],data[2:]);mu=(data[0]*data[3]-data[1]*data[2])%3
 if not mu:continue
 gl+=1
 assert mul(mul(trans(h),j),h)==scale(j,mu)
 nonzero=False
 for v in product(range(3),repeat=2):
  hv=mv(h,v);b=bv(v,hv,j)
  if not b:continue
  nonzero=True
  for c in (1,2):
   k=mul(tv(hv,c*pow(mu,-1,3),j),tv(v,-c,j))
   assert power(k,2 if mu==1 else 3)==scale(eye(2),-1)
   cases+=1
 if not nonzero:
  zero+=1
  assert h[0][1]==h[1][0]==0 and h[0][0]==h[1][1]
assert gl==48 and zero==2

j4=((0,0,1,0),(0,0,0,1),(2,0,0,0),(0,2,0,0))
h=((0,2,0,0),(1,0,0,0),(0,0,0,1),(0,0,2,0))
assert mul(mul(trans(h),j4),h)==scale(j4,-1)
assert mul(trans(h),j4)==mul(j4,h)
assert power(h,2)==scale(eye(4),-1)
selfadjoint=0
for v in product(range(3),repeat=4):
 if not any(v):continue
 hv=mv(h,v)
 assert rank((v,hv))==2 and bv(v,hv,j4)==0
 for c in (1,2):
  k=mul(tv(hv,-c,j4),tv(v,-c,j4))
  n=add(k,scale(eye(4),-1))
  assert rank(n)==2 and mul(n,n)==scale(eye(4),0)
  assert power(k,3)==eye(4)
  selfadjoint+=1
assert selfadjoint==160

# The exact, phase-free Schrödinger conjugation, with unrestricted coordinates.
u=s.symbols('u0:3');x=s.symbols('x0:3');y=s.symbols('y0:3');c=s.symbols('c')
f=lambda v:-c*(v[0]**2+v[1]**2)/2
left=f(u)+sum(y[i]*u[i]+x[i]*y[i]/2 for i in range(3))-f(tuple(u[i]+x[i] for i in range(3)))
yy=tuple(y[i]+c*x[i] if i<2 else y[i] for i in range(3))
right=sum(yy[i]*u[i]+x[i]*yy[i]/2 for i in range(3))
assert s.expand(left-right)==0
carriers=[]
for m in (2,3,4):
 for c,psi in product((1,2),repeat=2):
  counts=[0,0,0]
  for v in product(range(3),repeat=m):counts[(psi*c*(v[0]**2+v[1]**2))%3]+=1
  assert counts==[3**(m-2),4*3**(m-2),4*3**(m-2)]
  assert 1-F(max(counts),3**m)==F(5,9)
  carriers.append({'m':m,'c':c,'central_character':psi,'counts':counts})

delta=F(13,108)
assert (1-F(1,27))/8==delta
assert F(2,9)>delta and F(5,36)>delta
assert F(16,27)>F(5,9) and delta<F(31,250)<F(1,4)
ceiling=F(6)/(10*delta-1)
assert ceiling==F(324,11)<30
ceil=lambda x:-(-x.numerator//x.denominator)
endpoints=[]
for e in (27,28,29):
 lhs=2*e+6;rhs=2*ceil(F(e,2))+10*ceil(delta*e)
 assert ceil(delta*e)==4 and lhs<rhs
 endpoints.append({'degree':e,'Euler_budget':lhs,'forced_cost':rhs})
assert not [e for e in range(27,61) if 2*e+6>=2*ceil(F(e,2))+10*ceil(delta*e)]
tex=base/'higher_odd_symplectic_three_section.tex';txt=tex.read_text()
assert txt.count(r'\[')==txt.count(r'\]')
assert txt.count(r'\begin{proof}')==txt.count(r'\end{proof}')==2
out={'status':'PASS','scope':'exact algebra and finite matrix/carrier witnesses; not a substitute for the universal proof','complete_GSp2_F3':{'matrices':gl,'scalar_zero_form':zero,'vector_parameter_commutators':cases},'nonsquare_self_adjoint_F3_4D_cases':selfadjoint,'symbolic_Schrodinger_conjugation':'PASS','exact_carriers':carriers,'normalizer_support':str(delta),'ESD_degree_ceiling':str(ceiling),'elementary_degree_floor':27,'endpoints':endpoints,'proof_sha256':hashlib.sha256(tex.read_bytes()).hexdigest(),'elapsed_seconds':time.perf_counter()-start}
(base/'check_higher_symplectic_three.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
