"""Exact bounded certificate for the all-rank commuting shallow trace proof.

All nine constant indecomposable types are checked in
F3[pi,epsilon]/(pi²,pi*epsilon,epsilon²). This verifies the finite matrix
identities used by the written all-rank and arbitrary-J argument.
"""
from pathlib import Path
import numpy as np
from itertools import product
from time import perf_counter
import json
exec(Path('code/C_finish_shallow_curvature_probe.py').read_text().split('roots=[')[0])
exec(Path('code/C_finish_modp2_Bockstein.py').read_text().split('def homology(')[0])
start=perf_counter()
def rep(A):
 return (np.array([[redq(x[0]+x[1]) for x in row] for row in A],dtype=np.int64),
         np.array([[redq(x[1]) for x in row] for row in A],dtype=np.int64),
         np.zeros((len(A),len(A[0])),dtype=np.int64))
def em(U):return np.zeros_like(U),np.zeros_like(U),U%3
def aa(A,B):return tuple((a+b)%3 for a,b in zip(A,B))
def an(A):return tuple(-a%3 for a in A)
def am(A,B):return (A[0]@B[0]%3,(A[0]@B[1]+A[1]@B[0])%3,(A[0]@B[2]+A[2]@B[0])%3)
def eq(A,B):return all(np.array_equal(a,b) for a,b in zip(A,B))
def bi(A,B,C,D):return tuple(np.block([[a,b],[c,d]])%3 for a,b,c,d in zip(A,B,C,D))
def ztwist(A):return A[0],(A[1]+A[0])%3,A[2]
def eye(n):return rep(ident(n))
def zr(n):return tuple(np.zeros((n,n),dtype=np.int64) for _ in range(3))
roots=[one,zeta,power(zeta,2)]
base=[]
for i,r in enumerate(roots):base.append((f'character_{i}',mat([[r]]),'line'))
for i,j in ((0,1),(0,2),(1,2)):
 base.append((f'pair_{i}{j}',mat([[roots[i],1],[0,roots[j]]]),'pair'))
Tf=mat([[1,0,0],[1,zeta,0],[add(one,zeta),0,power(zeta,2)]])
Pf=mat([[0,1,pi],[1,0,-1],[add(one,zeta),0,-1]])
Tq=mat([[1,0,0],[0,zeta,0],[neg(add(one,zeta)),neg(zeta),power(zeta,2)]])
Pq=mat([[0,0,1],[pi,1,1],[neg(zeta),0,0]])
Fad=conjugate(Tf,Pf);Qad=conjugate(Tq,Pq)
assert all(Fad[i][2]==(one if i==2 else zero) for i in range(3))
assert all(Qad[2][i]==(one if i==2 else zero) for i in range(3))
base.extend([('full_gluing',Fad,'full'),('sum_zero_plane',Qad,'plane'),
             ('regular',mat([[0,0,1],[1,0,0],[0,1,0]]),'regular')])
runs=[];actions=sequences=gauges=regular=0
for name,T0,kind in base:
 n=len(T0);t0=rep(T0);I=eye(n);O=zr(n)
 assert eq(am(am(t0,t0),t0),I)
 units=[]
 for i in range(n):
  for j in range(n):
   H=np.zeros((n,n),dtype=np.int64);H[i,j]=1;units.append(H)
 D=np.column_stack([(t0[0]@H-H@t0[0]).ravel() for H in units])%3
 C=ker(D,3);dim=C.shape[1]
 Vs=[np.zeros((n,n),dtype=np.int64)]+[(a*C[:,j]).reshape(n,n)%3 for j in range(dim) for a in (1,2)]
 count=seq=gc=rc=0
 for params in product(range(3),repeat=dim):
  U=(C@np.array(params,dtype=np.int64)%3).reshape(n,n);t=aa(t0,em(U))
  assert eq(am(am(t,t),t),I);count+=1
  E=bi(t,I,O,ztwist(t0));I2=eye(2*n)
  assert eq(am(am(E,E),E),I2)
  for V in Vs:
   P=bi(I,O,em(V-U),I);Pi=bi(I,O,em(U-V),I)
   expected=bi(aa(t0,em(V)),I,O,aa(ztwist(t0),em(U-V)))
   assert eq(am(P,Pi),I2) and eq(am(am(Pi,E),P),expected)
   seq+=1
  if kind in ('full','plane'):
   assert np.array_equal(t0[0]-np.eye(3,dtype=np.int64),np.array([[0,1,0],[0,0,0],[0,0,0]]))
   a,b,c,d,e=map(int,(U[0,0],U[0,1],U[0,2],U[2,1],U[2,2]))
   assert np.array_equal(U,np.array([[a,b,c],[0,a,0],[0,d,e]]))
   H=np.zeros((3,3),dtype=np.int64);H[1,1]=b;H[1,2]=c;H[2,0]=-d
   target=np.diag([a,a,e])%3
   P=aa(I,em(-H));Pi=aa(I,em(H))
   assert eq(am(am(Pi,t),P),aa(t0,em(target)));gc+=1
   assert int(np.trace(U))%3==(e-a)%3
   E33=np.diag([0,0,1]);tx=aa(t0,em(E33))
   if kind=='full':assert all(int(tx[h][i,2])==(int(i==2) if h==0 else int(h==2 and i==2)) for h in (0,2) for i in range(3))
   else:assert all(int(tx[h][2,i])==(int(i==2) if h==0 else int(h==2 and i==2)) for h in (0,2) for i in range(3))
  if kind=='pair':
   a,b=int(U[0,0]),int(U[0,1]);assert np.array_equal(U,np.array([[a,b],[0,a]]))
   H=np.diag([0,b]);P=aa(I,em(-H));Pi=aa(I,em(H))
   assert eq(am(am(Pi,t),P),aa(t0,em(np.eye(2,dtype=np.int64)*a)));gc+=1
  if kind=='regular':
   assert np.trace(U)%3==0
   v=(np.array([[1],[0],[0]]),np.zeros((3,1),dtype=np.int64),np.zeros((3,1),dtype=np.int64))
   tv=am(t,v);t2v=am(t,tv)
   B=tuple(np.column_stack((a,b,c)) for a,b,c in zip(v,tv,t2v))
   assert np.array_equal(B[0],np.eye(3,dtype=np.int64)) and not np.any(B[1])
   Binv=aa(I,em(-B[2]))
   assert eq(am(B,Binv),I) and eq(am(t,B),am(B,t0));rc+=1
 actions+=count;sequences+=seq;gauges+=gc;regular+=rc
 runs.append({'type':name,'rank':n,'commutant_dimension':dim,'actions':count,'free_block_sequences':seq,'gauge_reductions':gc,'regular_generator_bases':rc})
report={'status':'PASS','scope':'All nine constant indecomposable cubic lattices; every commuting perturbation over a one-dimensional residue ideal; exact order3/free-block conjugacy identities, all pair and rank3 gauge eliminations, regular-generator trivializations, and exact integral rank3 invariant line/quotient bases. All ranks and arbitrary residue-vector-space ideals are handled by the written block-additivity proof.',
        'runs':runs,'actions':actions,'free_block_sequences':sequences,'gauge_reductions':gauges,'regular_generator_bases':regular,'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_shallow_commuting.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
