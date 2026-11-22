"""Exact bounded certificate for the normal dyadic-node comparison kernel.

The all-rank exact-sequence argument and normality/PID claims are proved in
C_finish_normal_kernel_draft.tex. This checks its ring/matrix/primary data and
all admissible rank-one extensions and witness-plus-line extensions over A/4.
"""
from pathlib import Path
from itertools import product
from time import perf_counter
import json
import sympy as sp
start=perf_counter()
# W = (Z/4)[z]/(z^2+z+1); field k=F4 uses a+2b for a+b*alpha.
def wa(x,y): return ((x%4+y%4)%4)+4*((x//4+y//4)%4)
def wn(x): return (-x%4)+4*((-(x//4))%4)
def wm(x,y):
 a,b=x%4,x//4;c,d=y%4,y//4
 return ((a*c-b*d)%4)+4*((a*d+b*c-b*d)%4)
def red(x): return (x%2)+2*((x//4)%2)
def lift(x): return (x%2)+4*(x//2)
def half(x):
 a,b=x%4,x//4
 assert a%2==b%2==0
 return a//2+2*(b//2)
def ka(x,y): return x^y
def km(x,y):
 a,b=x%2,x//2;c,d=y%2,y//2
 return ((a*c+b*d)%2)+2*((a*d+b*c+b*d)%2)
def ki(x):
 assert x
 return km(x,x)
def zero(n,m): return [[0]*m for _ in range(n)]
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def add(A,B,ring=False):
 f=wa if ring else ka
 return [[f(a,b) for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def neg(A): return [[wn(a) for a in ar] for ar in A]
def mm(A,B,ring=False):
 n=len(A);r=len(B);m=len(B[0]) if r else 0
 out=zero(n,m);mul=wm if ring else km;plus=wa if ring else ka
 for i in range(n):
  for j in range(m):
   for h in range(r):out[i][j]=plus(out[i][j],mul(A[i][h],B[h][j]))
 return out
def scale(A,c): return [[km(c,a) for a in ar] for ar in A]
def cols(A): return list(map(list,zip(*A))) if A else []
def fromcols(cs,n): return [[c[i] for c in cs] for i in range(n)]
def rref(A):
 A=[r[:] for r in A];n=len(A);m=len(A[0]) if n else 0;piv=[];r=0
 for j in range(m):
  k=next((i for i in range(r,n) if A[i][j]),None)
  if k is None:continue
  A[r],A[k]=A[k],A[r];iv=ki(A[r][j]);A[r]=[km(iv,a) for a in A[r]]
  for i in range(n):
   if i!=r and A[i][j]:
    c=A[i][j];A[i]=[ka(a,km(c,b)) for a,b in zip(A[i],A[r])]
  piv.append(j);r+=1
  if r==n:break
 return A,piv
def rank(A):return len(rref(A)[1])
def null(A):
 R,piv=rref(A);m=len(A[0]) if A else 0;out=[]
 for j in range(m):
  if j in piv:continue
  v=[0]*m;v[j]=1
  for i,h in enumerate(piv):v[h]=R[i][j]
  out.append(v)
 return out
def coordinates(basis,v):
 n=len(v);m=len(basis)
 if not m:
  assert not any(v);return []
 R,piv=rref([row+[v[i]] for i,row in enumerate(fromcols(basis,n))])
 assert piv==list(range(m))
 assert all(not row[-1] for row in R[m:])
 return [R[i][-1] for i in range(m)]
def bockstein(T):
 n=len(T);D=add(T,neg(eye(n)),True);db=[[red(a) for a in row] for row in D]
 assert mm(db,db)==zero(n,n)
 boundaries=[]
 for c in cols(db):
  if rank(fromcols(boundaries+[c],n))>len(boundaries):boundaries.append(c)
 basis=boundaries[:];hom=[]
 for c in null(db):
  if rank(fromcols(basis+[c],n))>len(basis):basis.append(c);hom.append(c)
 out=[]
 for c in hom:
  dw=mm(D,[[lift(a)] for a in c],True)
  w=[half(row[0]) for row in dw]
  assert mm(db,[[a] for a in w])==zero(n,1)
  out.append(coordinates(basis,w)[len(boundaries):])
 return fromcols(out,len(hom))
def chi(T):
 N=bockstein(T);n=len(N)
 if not n:return 0
 # f(t)=t^2+t+alpha^2, alpha=2 and alpha^2=3.
 fN=add(add(mm(N,N),N),scale(eye(n),3));powf=eye(n)
 for _ in range(n):powf=mm(powf,fN)
 dim=n-rank(powf);assert dim%2==0
 return (dim//2)%2
def extension(A,B,X):
 a=len(A);b=len(B)
 return [A[i]+X[i] for i in range(a)]+[[0]*a+B[i] for i in range(b)]
def inv(T):return mm(T,T,True)==eye(len(T))
# Polynomial identities, independent of a ring substitution.
z,x,y=sp.symbols('z x y');a=1+2*z
T=sp.Matrix([[a,x],[y,-a]]);P=sp.Matrix([[x,x],[1-a,-1-a]])
G=sp.groebner([z*z+z+1,x*y-4],y,x,z)
assert all(G.reduce(sp.expand(e))[1]==0 for e in T*T-sp.eye(2))
assert all(G.reduce(sp.expand(e))[1]==0 for e in T*P-P*sp.diag(1,-1))
assert sp.expand(P.det())==-2*x
# Exact coefficient ring and the specialized witness.
for a,b,c in product(range(16),repeat=3):assert wm(wm(a,b),c)==wm(a,wm(b,c))
za=4;aa=wa(1,wm(2,za))
W=[[aa,2],[wm(2,za),wn(aa)]]
assert inv(W)
N=bockstein(W)
assert N==[[2,1],[2,3]]
assert add(add(mm(N,N),N),scale(eye(2),3))==zero(2,2)
assert all(ka(ka(km(u,u),u),3)!=0 for u in range(4))
assert chi(W)==1
lines=[[[u]] for u in range(16) if wm(u,u)==1]
assert len(lines)==4 and all(chi(L)==0 for L in lines)
# All possible upper blocks, testing every admissible extension in these ranges.
extensions=0;candidates=0;by_shape={}
for A,B in [(A,B) for A in lines for B in lines]+[(W,L) for L in lines]+[(L,W) for L in lines]:
 a,b=len(A),len(B);key=f'{a}+{b}'
 for es in product(range(16),repeat=a*b):
  candidates+=1;X=[list(es[i*b:(i+1)*b]) for i in range(a)];E=extension(A,B,X)
  if not inv(E):continue
  assert chi(E)==(chi(A)+chi(B))%2
  extensions+=1;by_shape[key]=by_shape.get(key,0)+1
# Every field basis change for the Bockstein matrix preserves the primary length.
bases=0
for es in product(range(4),repeat=4):
 S=[list(es[:2]),list(es[2:])]
 if rank(S)<2:continue
 Sinv=fromcols([coordinates(cols(S),c) for c in cols(eye(2))],2)
 N1=mm(mm(Sinv,N),S)
 fN=add(add(mm(N1,N1),N1),scale(eye(2),3))
 assert fN==zero(2,2);bases+=1
assert bases==180
report={'status':'PASS','scope':'Exact defining-ring and generic-eigenbasis identities; all 4096 coefficient-ring associativity triples; specialized nonzero translation-invariant irreducible Bockstein primary; exhaustive line/line and witness/line upper-triangular extensions over A/4; all GL2(F4) basis changes. Normality, generic PID/K0 and arbitrary-rank additivity are written proofs, not inferred from this finite computation.','field':'F4=F2[alpha]/(alpha^2+alpha+1)','bockstein':N,'detecting_polynomial':'t^2+t+alpha^2','chi_witness':1,'rank_one_involutions':len(lines),'extension_candidates':candidates,'admissible_extensions':extensions,'extensions_by_shape':by_shape,'basis_changes':bases,'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_normal_kernel.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
