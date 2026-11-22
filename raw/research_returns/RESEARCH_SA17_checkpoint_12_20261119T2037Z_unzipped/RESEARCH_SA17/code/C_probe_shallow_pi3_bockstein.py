"""Exploratory first-pi Bockstein/curvature computation; no theorem claim."""
from pathlib import Path
from itertools import product
from time import perf_counter
import json
import numpy as np
exec(Path('code/C_finish_shallow_curvature_probe.py').read_text().split('\nroots=[')[0])
start=perf_counter()

def inv3(A):
 A=np.array(A,dtype=np.int64)%3;n=len(A);B=np.eye(n,dtype=np.int64)
 for j in range(n):
  h=next(i for i in range(j,n) if A[i,j])
  A[[j,h]]=A[[h,j]];B[[j,h]]=B[[h,j]]
  u=int(A[j,j]);A[j]=A[j]*u%3;B[j]=B[j]*u%3
  for i in range(n):
   if i!=j:
    u=int(A[i,j]);A[i]=(A[i]-u*A[j])%3;B[i]=(B[i]-u*B[j])%3
 assert np.array_equal(A,np.eye(n,dtype=np.int64))
 return B

def inds(A):
 A=np.array(A,dtype=np.int64)%3;r=0;out=[]
 for j in range(A.shape[1]):
  h=next((i for i in range(r,len(A)) if A[i,j]),None)
  if h is None:continue
  A[[r,h]]=A[[h,r]];A[r]=A[r]*int(A[r,j])%3
  for i in range(len(A)):
   if i!=r:A[i]=(A[i]-int(A[i,j])*A[r])%3
  out.append(j);r+=1
  if r==len(A):break
 return out

def restrict(C,beta):
 cs=inds(beta);X=beta[:,cs]%3;rs=inds(X.T)
 Y=inv3(X[rs,:])@(C@X%3)[rs,:]%3
 assert np.array_equal(X@Y%3,C@X%3)
 return Y

def mix(A,B):
 return [[([A,B][i%2])[i//2][j//2] if i%2==j%2 else zero for j in range(6)] for i in range(6)]
D=mat([[1,0,0],[0,zeta,0],[0,0,power(zeta,2)]])
BL=mat([[0,1,pi],[pi,1,0],[neg(pi),1,0]])
BQ=mat([[0,0,1],[pi,1,F(-1,2)],[pi,-1,F(-1,2)]])
I=ident(6);In=np.eye(6,dtype=np.int64);N=np.zeros((6,6),dtype=np.int64);N[:2,2:4]=np.eye(2,dtype=np.int64)
h0=[0,1,4,5];h1=[2,3,4,5]
TL=conjugate(D,BL);TQ=conjugate(D,BQ)
runs=[]
for name,T0,signs in [('L012_plus_minus',mix(TL,TL),[-1,1,1,-1,1,-1]),('Q_plus_minus',mix(TQ,TQ),[1,-1,-1,1,1,-1]),('L012_plus_Q_plus',mix(TL,TQ),[-1,1,1,-1,1,1]),('L012_plus_Q_minus',mix(TL,TQ),[-1,-1,1,1,1,-1])]:
 sg=np.diag(signs)
 assert mm(mm(mat(sg.tolist()),T0),mat(sg.tolist()))==mm(T0,T0)
 dif=ma(T0,mn(I));norm=ma(ma(I,T0),mm(T0,T0))
 be0=np.array([[residue(div(dif[i][j],pi)) for j in h0] for i in h1],dtype=np.int64)
 be1=np.array([[residue(div(norm[i][j],pi)) for j in h1] for i in h0],dtype=np.int64)
 assert not np.any(be1@be0%3) and not np.any(be0@be1%3)
 assert len(inds(be0))+len(inds(be1))==len(h0)
 def invol(U):return -sg@(In-N)@U@(In-N)@sg%3
 cmap=[];positions=[]
 for i in range(2):
  for j in range(2):
   if signs[2+i]*signs[2+j]==-1:positions.append((2+i,2+j))
   if signs[2+i]*signs[4+j]==-1:positions.append((2+i,4+j))
   if signs[4+i]*signs[2+j]==1:positions.append((4+i,j))
   if signs[4+i]*signs[4+j]==-1:positions.append((4+i,4+j))
 for i,j in positions:
  W=np.zeros((6,6),dtype=np.int64);W[i,j]=1;U=2*(W+invol(W))%3
  assert not np.any(N@U@N%3) and np.array_equal(invol(U),U)
  UA=mat(U.tolist());C=scale(ma(ma(mm(mm(T0,T0),UA),mm(mm(T0,UA),T0)),mm(mm(UA,T0),T0)),inv(pi))
  cmap.append(np.array([[residue(x) for x in row] for row in C],dtype=np.int64))
 detected=[];count=0
 for par in product(range(3),repeat=len(positions)):
  C=sum((c*Q for c,Q in zip(par,cmap)),np.zeros((6,6),dtype=np.int64))%3
  C0=C[np.ix_(h0,h0)];C1=C[np.ix_(h1,h1)]
  assert np.array_equal(C1@be0%3,be0@C0%3) and np.array_equal(C0@be1%3,be1@C1%3)
  A0=restrict(C1,be0);A1=restrict(C0,be1)
  f0=dict(factors(tuple(map(int,A0.flatten())),len(A0)));f1=dict(factors(tuple(map(int,A1.flatten())),len(A1)))
  bad={str(q):(f0.get(q,0)-f1.get(q,0))%3 for q in set(f0)|set(f1) if q!=(1,0) and (f0.get(q,0)-f1.get(q,0))%3}
  if bad:detected.append({'parameters':par,'h_mod3':bad,'beta0_image_curvature':A0.tolist(),'beta1_image_curvature':A1.tolist()})
  count+=1
 runs.append({'baseline':name,'tangent_positions':positions,'actual_S3_first_order_parameters':count,'beta0':be0.tolist(),'beta1':be1.tolist(),'detections':detected})
 print(name,count,'detections',len(detected),flush=True)
report={'status':'BOUNDED EXPLORATORY COMPUTATION','scope':'All fixed-transposition tangent parameters on four rank6 signed L012/Q baselines at pi³. First-pi Bockstein on residue Tate groups and residual cubic curvature on its image spaces. Additivity of h modulo3 over this mixed-characteristic coefficient base is still being proved; detections, if any, are candidate witnesses only.','runs':runs,'runtime_seconds':round(perf_counter()-start,6)}
Path('logs/C_probe_shallow_pi3_bockstein.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'runtime_seconds':report['runtime_seconds'],'counts':[{'baseline':x['baseline'],'parameters':x['actual_S3_first_order_parameters'],'detections':len(x['detections'])} for x in runs]},indent=2))
