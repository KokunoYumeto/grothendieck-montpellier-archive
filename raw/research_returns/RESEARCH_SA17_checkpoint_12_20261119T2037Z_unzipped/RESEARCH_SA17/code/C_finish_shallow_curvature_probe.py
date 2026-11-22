"""Bounded exact curvature search; zero detections are not a vanishing theorem.

A=Z_3[zeta_3], pi=zeta_3-1. Test every residual tangent gauge class
on all nine pair-plus-line rank-three baselines and the two rank-three
indecomposable nonregular full-support baselines. The coefficient map is
epsilon -> pi^(m-1), m=3,4,5. Compute all nonzero curvature-primary
cokernel lengths using exact DVR row/column elimination and graded pieces.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
from time import perf_counter
import json
import sympy as sp
start=perf_counter()

def el(a=0,b=0):return F(a),F(b)
zero=el();one=el(1);zeta=el(0,1);pi=el(-1,1)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=x;c,d=y
 return a*c-b*d,a*d+b*c-b*d
def inv(x):
 a,b=x;n=a*a-a*b+b*b
 assert n
 return (a-b)/n,-b/n
def div(x,y):return mul(x,inv(y))
def power(x,n):
 if n<0:return power(inv(x),-n)
 out=one
 while n:
  if n&1:out=mul(out,x)
  x=mul(x,x);n//=2
 return out
def v3(a):
 if not a:return 10000
 a=F(a);n,d=abs(a.numerator),a.denominator;v=0
 while n%3==0:n//=3;v+=1
 while d%3==0:d//=3;v-=1
 return v
def redq(a):
 a=F(a);assert a.denominator%3
 return a.numerator*pow(a.denominator,-1,3)%3
def valuation(x):
 if x==zero:return 10000
 a,b=x;v=min(v3(a),v3(b));u=F(3)**(-v)
 return 2*v+int((redq(a*u)+redq(b*u))%3==0)
def residue(x):
 assert valuation(x)>=0
 return (redq(x[0])+redq(x[1]))%3
def ident(n):return [[one if i==j else zero for j in range(n)] for i in range(n)]
def mat(rows):return [[x if isinstance(x,tuple) else el(x) for x in row] for row in rows]
def mm(A,B):
 return [[sumel(mul(A[i][k],B[k][j]) for k in range(len(B)))
          for j in range(len(B[0]))] for i in range(len(A))]
def sumel(xs):
 out=zero
 for x in xs:out=add(out,x)
 return out
def ma(A,B):return [[add(x,y) for x,y in zip(a,b)] for a,b in zip(A,B)]
def mn(A):return [[neg(x) for x in row] for row in A]
def scale(A,x):return [[mul(x,y) for y in row] for row in A]
def mi(A):
 n=len(A);B=[r[:] for r in A];P=ident(n)
 for j in range(n):
  h=next(i for i in range(j,n) if B[i][j]!=zero)
  B[j],B[h]=B[h],B[j];P[j],P[h]=P[h],P[j]
  q=inv(B[j][j]);B[j]=[mul(q,x) for x in B[j]];P[j]=[mul(q,x) for x in P[j]]
  for i in range(n):
   if i==j:continue
   c=B[i][j];B[i]=[sub(x,mul(c,y)) for x,y in zip(B[i],B[j])]
   P[i]=[sub(x,mul(c,y)) for x,y in zip(P[i],P[j])]
 assert B==ident(n)
 return P
def conjugate(A,P):return mm(mm(mi(P),A),P)

zz=sp.symbols('z')
@lru_cache(None)
def factors(flat,n):
 if not n:return ()
 M=sp.Matrix(n,n,flat)
 pol=sp.Poly(M.charpoly(zz).as_expr(),zz,modulus=3)
 return tuple((tuple(int(c)%3 for c in q.all_coeffs()),int(e))
              for q,e in sp.factor_list(pol)[1])

def smith_curvature(D,C,m):
 """Diagonalize D by integral DVR bases; apply row conjugacies to C."""
 D=[r[:] for r in D];C=[r[:] for r in C];n=len(D);vs=[]
 for k in range(n):
  v,i,j=min((valuation(D[i][j]),i,j) for i in range(k,n) for j in range(k,n))
  if v>=10000:vs.extend([10000]*(n-k));break
  assert v>=0
  if i!=k:
   D[k],D[i]=D[i],D[k];C[k],C[i]=C[i],C[k]
   for r in C:r[k],r[i]=r[i],r[k]
  if j!=k:
   for r in D:r[k],r[j]=r[j],r[k]
  piv=power(pi,v);unit=div(piv,D[k][k]);assert valuation(unit)==0
  D[k]=[mul(unit,x) for x in D[k]]
  C[k]=[mul(unit,x) for x in C[k]]
  iu=inv(unit)
  for r in C:r[k]=mul(r[k],iu)
  for i in range(k+1,n):
   c=div(D[i][k],piv);assert valuation(c)>=0
   D[i]=[sub(x,mul(c,y)) for x,y in zip(D[i],D[k])]
   C[i]=[sub(x,mul(c,y)) for x,y in zip(C[i],C[k])]
   for r in C:r[k]=add(r[k],mul(c,r[i]))
  for j in range(k+1,n):
   c=div(D[k][j],piv);assert valuation(c)>=0
   for r in D:r[j]=sub(r[j],mul(c,r[k]))
  vs.append(v)
 assert all(D[i][j]==zero for i in range(n) for j in range(n) if i!=j)
 assert all(valuation(x)>=0 for row in C for x in row)
 lengths={}
 for j in range(m):
  inds=[i for i,v in enumerate(vs) if v>j]
  M=tuple(residue(C[i][h]) for i in inds for h in inds)
  for q,e in factors(M,len(inds)):lengths[q]=lengths.get(q,0)+e
 return vs,lengths

roots=[one,zeta,power(zeta,2)]
baselines=[]
for i,j in ((0,1),(0,2),(1,2)):
 for h in range(3):
  baselines.append((f'L_{i}{j}+L_{h}',mat([[roots[i],1,0],[0,roots[j],0],[0,0,roots[h]]])))
Tfull=mat([[1,0,0],[1,zeta,0],[add(one,zeta),0,power(zeta,2)]])
Pfull=mat([[0,1,0],[1,0,1],[2,0,0]])
TQ=mat([[1,0,0],[0,zeta,0],[neg(add(one,zeta)),neg(zeta),power(zeta,2)]])
PQ=mat([[0,1,1],[0,0,1],[1,0,0]])
baselines.extend([('L_012',conjugate(Tfull,Pfull)),('Q',conjugate(TQ,PQ))])
I=ident(3);N=[[0,1,0],[0,0,0],[0,0,0]]
runs=[];nonzero=[];total=0
for name,T0 in baselines:
 assert mm(mm(T0,T0),T0)==I
 assert [[(residue(T0[i][j])-int(i==j))%3 for j in range(3)] for i in range(3)]==N
 detections=0;nonzero_curvatures=0
 for S,A,B,C0 in product(range(3),repeat=4):
  U=mat([[0,0,0],[0,S,A],[B,0,C0]])
  tangent=ma(ma(mm(mm(T0,T0),U),mm(mm(T0,U),T0)),mm(mm(U,T0),T0))
  assert all(valuation(x)>=1 for row in tangent for x in row)
  for m in (3,4,5):
   T=ma(T0,scale(U,power(pi,m-1)))
   cube=ma(mm(mm(T,T),T),mn(I))
   assert all(valuation(x)>=m for row in cube for x in row)
   Cur=scale(cube,power(pi,-m))
   D=ma(T,mn(I))
   assert mm(Cur,D)==mm(D,Cur)
   vals,lengths=smith_curvature(D,Cur,m);total+=1
   relevant={str(q):length for q,length in lengths.items() if q!=(1,0)}
   if relevant:nonzero_curvatures+=1
   bad={q:v%m for q,v in relevant.items() if v%m}
   if bad:
    detections+=1
    nonzero.append({'baseline':name,'parameters':[S,A,B,C0],'m':m,'smith_exponents':vals,'lengths':relevant,'nonzero_residues':bad})
 runs.append({'baseline':name,'tangent_gauge_classes':81,'truncations':[3,4,5],
              'nonzero_primary_cases':nonzero_curvatures,'detected_cases':detections})
 print(name,'done; detections',detections,flush=True)
report={'status':'BOUNDED SEARCH COMPLETE','scope':'Every one of81 tangent gauge classes for each of11 rank3 baselines, three target truncations. Exact Q(zeta3) arithmetic and integral pi-Smith transformations, all curvature-primary graded lengths. A zero result does not prove the representations vanish or that the shallow ring is positive.',
        'runs':runs,'actual_truncated_actions':total,'detections':nonzero,
        'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_shallow_curvature_probe.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
