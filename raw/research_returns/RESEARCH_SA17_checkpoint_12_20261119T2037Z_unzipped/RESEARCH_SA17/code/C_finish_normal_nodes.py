"""Bounded exact certificate for the dyadic normal-node family.

Symbolic identities are checked for n=2 and n=3..10. The F8[s] calculation
checks all seven nonzero residue units and the three distinct quadratic
primary blocks at n=2. Arbitrary exponents, residue fields, AS irreducibility,
normality and the iff are proved in the accompanying written theorem.
"""
from pathlib import Path
from time import perf_counter
import json
import sympy as sp
start=perf_counter()
x,y,u,w,s,z=sp.symbols('x y u w s z')
C=sp.Matrix([[0,0,-1],[1,0,-1],[0,1,0]])
assert C.charpoly(z).as_expr()==z**3+z+1
runs=[]
for n in range(2,11):
 d=3 if n==2 else 1;I=sp.eye(d)
 a=I+2*C if n==2 else (1+2**(n-1))*I
 L=-w*y*(C*C+C) if n==2 else -w*y*(1+2**(n-2))*I
 T=a.row_join(x*I).col_join(L.row_join(-a))
 P=(x*I).row_join(x*I).col_join((I-a).row_join(-I-a))
 G=sp.groebner([x*y-2**n*u,u*w-1],y,x,u,w)
 assert all(G.reduce(sp.expand(v))[1]==0 for v in T*T-sp.eye(2*d))
 assert all(G.reduce(sp.expand(v))[1]==0 for v in T*P-P*sp.diag(*([1]*d+[-1]*d)))
 assert sp.factor(P.det())==(-2*x)**d
 runs.append({'n':n,'rank':2*d,'involution':True,'free_generic_eigenbasis':True})
# F8 = F2[b]/(b^3+b+1), encoded by three coefficient bits.
def add(a,b):return a^b
def mul(a,b):
 v=0
 while b:
  if b&1:v^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return v
def power(a,n):
 b=1
 while n:
  if n&1:b=mul(b,a)
  a=mul(a,a);n//=2
 return b
def inv(a):assert a;return power(a,6)
def zeros(n,m):return [[0]*m for _ in range(n)]
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def matmul(A,B):
 R=zeros(len(A),len(B[0]))
 for i in range(len(A)):
  for j in range(len(B[0])):
   for h in range(len(B)):R[i][j]^=mul(A[i][h],B[h][j])
 return R
def rref(A):
 A=[r[:] for r in A];piv=[];r=0
 for j in range(len(A[0])):
  h=next((i for i in range(r,len(A)) if A[i][j]),None)
  if h is None:continue
  A[r],A[h]=A[h],A[r];v=inv(A[r][j]);A[r]=[mul(v,a) for a in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][j]:
    v=A[i][j];A[i]=[a^mul(v,b) for a,b in zip(A[i],A[r])]
  piv.append(j);r+=1
  if r==len(A):break
 return A,piv
def null(A):
 R,piv=rref(A);out=[]
 for j in range(len(A[0])):
  if j in piv:continue
  v=[0]*len(A[0]);v[j]=1
  for i,h in enumerate(piv):v[h]=R[i][j]
  out.append(v)
 return out
def inverse(A):
 n=len(A);R,piv=rref([r+e for r,e in zip(A,eye(n))]);assert piv==list(range(n));return [r[n:] for r in R]
def fromcols(cs):return list(map(list,zip(*cs)))
roots=[a for a in range(8) if power(a,3)^a^1==0]
assert roots==[2,4,6]
ds=[mul(a,a)^a for a in roots]
assert len(set(ds))==3 and all(ds)
Cb=[[int(v)%2 for v in row] for row in C.tolist()]
S=fromcols([null([[v^(a if i==j else 0) for j,v in enumerate(row)] for i,row in enumerate(Cb)])[0] for a in roots])
Si=inverse(S)
assert matmul(matmul(Si,Cb),S)==[[roots[i] if i==j else 0 for j in range(3)] for i in range(3)]
# Polynomial entries over F8, low-to-high coefficient lists.
def trim(a):
 a=list(a)
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def pa(a,b):
 r=[0]*max(len(a),len(b))
 for i,v in enumerate(a):r[i]^=v
 for i,v in enumerate(b):r[i]^=v
 return trim(r)
def pm(a,b):
 r=[0]*(len(a)+len(b)-1)
 for i,v in enumerate(a):
  for j,t in enumerate(b):r[i+j]^=mul(v,t)
 return trim(r)
def pmm(A,B):
 R=[[[0] for _ in B[0]] for _ in A]
 for i in range(len(A)):
  for j in range(len(B[0])):
   for h in range(len(B)):R[i][j]=pa(R[i][j],pm(A[i][h],B[h][j]))
 return R
def blockdiag(A):
 n=len(A);return [[A[i%n][j%n] if i//n==j//n else 0 for j in range(2*n)] for i in range(2*n)]
S6=[[[a] for a in row] for row in blockdiag(S)]
Si6=[[[a] for a in row] for row in blockdiag(Si)]
CC=matmul(Cb,Cb);D=[[CC[i][j]^Cb[i][j] for j in range(3)] for i in range(3)]
unit_runs=[]
for unit in range(1,8):
 iu=inv(unit);N=[[[0] for _ in range(6)] for _ in range(6)]
 for i in range(3):
  for j in range(3):
   N[i][j]=[Cb[i][j]];N[i][j+3]=[int(i==j)]
   N[i+3][j]=trim([0,mul(iu,D[i][j])]);N[i+3][j+3]=[Cb[i][j]^int(i==j)]
 P=pmm(pmm(Si6,N),S6)
 for i in range(3):
  for j in range(3):
   assert P[i][j]==[roots[i] if i==j else 0]
   assert P[i][j+3]==[int(i==j)]
   assert P[i+3][j]==(trim([0,mul(iu,ds[i])]) if i==j else [0])
   assert P[i+3][j+3]==[(roots[i]^1) if i==j else 0]
 constants=[(d,mul(iu,d)) for d in ds]
 assert len(set(constants))==3 and all(a[1] for a in constants)
 # Verify each block's characteristic polynomial and annihilator directly.
 for i,beta in enumerate(roots):
  inds=[i,i+3];B=[[P[a][b] for b in inds] for a in inds];B2=pmm(B,B)
  f=[ds[i],mul(iu,ds[i])]
  assert all(pa(pa(B2[a][b],B[a][b]),f if a==b else [0])==[0] for a in range(2) for b in range(2))
 unit_runs.append({'unit':unit,'quadratic_constant_polynomials':constants,'nonzero_linear_coefficients':True,'distinct_primaries':True})
# The explicitly mentioned Z_(2) example xy+8, a=3.
T=sp.Matrix([[3,x],[y,-3]])
assert T*T-sp.eye(2)==(x*y+8)*sp.eye(2)
N=sp.Matrix([[1,1],[1,0]])
assert sp.Poly(N.charpoly(z).as_expr(),z,modulus=2).as_expr()==z*z+z+1
report={'status':'PASS','scope':'Symbolic n=2..10 matrix and eigenbasis identities; exact F8[s] diagonalization and three distinct primary quadratics for all7 residue units; explicit xy+8 example. Nonzero linear pole coefficients are checked, while irreducibility over arbitrary kappa(s), normality, all exponents and the whole iff are written proofs.','symbolic_runs':runs,'residue_cubic_roots':roots,'distinct_nonzero_beta_squared_plus_beta':ds,'residue_unit_runs':unit_runs,'xy_plus8_example':True,'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_normal_nodes.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
