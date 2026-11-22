"""Exploration only: test a proposed half-length invariant over F3[epsilon]/epsilon^2."""
from pathlib import Path
from itertools import product
from time import perf_counter
import numpy as np
import json
exec(Path('code/C_finish_modp2_Bockstein.py').read_text().split('def data(')[0])
start=perf_counter();p=3

def dualpower(T,U,r):
 n=len(T);A=np.eye(n,dtype=np.int64);B=np.zeros((n,n),dtype=np.int64)
 for _ in range(r):A,B=A@T%p,(A@U+B@T)%p
 return A,B

def dat(T,U):
 n=len(T);I=np.eye(n,dtype=np.int64)
 A,B=dualpower(T,U,p)
 if not np.array_equal(A,I) or np.any(B):return None
 N=sum((dualpower(T,U,j)[0] for j in range(p)),np.zeros_like(T))%p
 V=sum((dualpower(T,U,j)[1] for j in range(p)),np.zeros_like(T))%p
 D=(T-I)%p;H0,P0=homology(D,N,p);H1,P1=homology(N,D,p)
 b0=P1@U@H0%p;b1=P0@V@H1%p;z=b1@b0%p
 h=len(z);q=(z-np.eye(h,dtype=np.int64))%p
 dim=h-rank(powm(q,max(h,1),p),p)
 assert dim%2==0
 return {'T':T,'U':U,'primary_dimension':dim,'half_parity':dim//2%2}

T=np.eye(3,dtype=np.int64);T[0,1]=1
U=np.zeros((3,3),dtype=np.int64);U[1,2]=1;U[2,0]=1
M=dat(T,U);assert M['half_parity']==1
lines=[dat(np.eye(1,dtype=np.int64),np.array([[a]],dtype=np.int64)) for a in range(3)]
candidates=valid=0;failures=[]
for A,B in [(M,L) for L in lines]+[(L,M) for L in lines]:
 n,m=len(A['T']),len(B['T']);shape=(n,m)
 for c in product(range(p),repeat=2*n*m):
  candidates+=1;X=np.array(c[:n*m],dtype=np.int64).reshape(shape);Y=np.array(c[n*m:],dtype=np.int64).reshape(shape)
  TT=np.block([[A['T'],X],[np.zeros((m,n),dtype=np.int64),B['T']]])
  UU=np.block([[A['U'],Y],[np.zeros((m,n),dtype=np.int64),B['U']]])
  E=dat(TT,UU)
  if E is None:continue
  valid+=1
  if E['half_parity']!=(A['half_parity']+B['half_parity'])%2:
   failures.append({'A_T':A['T'].tolist(),'A_U':A['U'].tolist(),'B_T':B['T'].tolist(),'B_U':B['U'].tolist(),'X0':X.tolist(),'X1':Y.tolist(),'middle_primary_dimension':E['primary_dimension']})
   break
 if failures:break
# A constructive larger-endpoint counterexample from the cusp lattice.
import sympy as sp
eps=sp.symbols('eps')
K=sp.Matrix([[0,0,eps],[1,0,0],[0,1,0]])
DS=K**2
DR=sp.Matrix([[0,0,eps**2],[1,0,0],[0,1,0]])
IR=sp.Matrix([[1,0,0],[0,0,eps],[0,1,0]])
F1=sp.Matrix([[0,eps,0],[1,0,0],[0,0,1]])
f=F1.col_join(K)
g=IR.row_join(-K)
assert g*f==sp.zeros(3)
Dmid=sp.diag(DR,DS)
assert Dmid*f==f*DS and g*Dmid==DS*g
section=sp.zeros(6,3);section[0,0]=1;section[3,1]=-1;section[1,2]=1
assert g*section==sp.eye(3)
P=f.row_join(section)
assert abs(P.det())==1
tri=P.inv()*Dmid*P
assert tri[:3,:3]==DS and tri[3:,3:]==DS and tri[3:,:3]==sp.zeros(3)
assert DS**3==eps**2*sp.eye(3) and DR**3==eps**2*sp.eye(3)
def coefficients(M):
 return (np.array(M.subs(eps,0).tolist(),dtype=np.int64)%p,
         np.array(M.diff(eps).subs(eps,0).tolist(),dtype=np.int64)%p)
D0,D1=coefficients(DS);R0,R1=coefficients(DR);E0,E1=coefficients(Dmid)
Sdat=dat(np.eye(3,dtype=np.int64)+D0,D1)
Rdat=dat(np.eye(3,dtype=np.int64)+R0,R1)
Edat=dat(np.eye(6,dtype=np.int64)+E0,E1)
assert Sdat['half_parity']==1 and Rdat['half_parity']==0 and Edat['half_parity']==1
X0,X1=coefficients(tri[:3,3:])
failures.append({'kind':'explicit cusp free-split sequence',
 'endpoint_D0':D0.tolist(),'endpoint_D1':D1.tolist(),
 'upper_extension_X0':X0.tolist(),'upper_extension_X1':X1.tolist(),
 'endpoint_half_parities':[1,1],'middle_half_parity':1,
 'basis_determinant':int(P.det()),'middle_is_regular_plus_endpoint':True})
report={'status':'REFUTED proposed half-length invariant',
 'scope':'The small range alone found no counterexample; an explicit larger-endpoint A-free split cusp sequence gives a concrete failure and proves this particular residue rank3 class equals the regular class. No claim for the mixed-characteristic ring.',
 'small_range_candidates':candidates,'small_range_admissible':valid,
 'constructive_failures':failures,'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_finish_residue_torsion_probe.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
