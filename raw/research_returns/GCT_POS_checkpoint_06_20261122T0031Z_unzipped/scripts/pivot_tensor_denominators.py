"""Exploratory exact-certified axial vertex pivots, biased toward large 2-part."""
import numpy as np,itertools,math,json,argparse,time
from fractions import Fraction
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--n',type=int,required=True);p.add_argument('--steps',type=int,default=10000);p.add_argument('--out',required=True);p.add_argument('--seed',type=int,default=21112026);a=p.parse_args();n=a.n;r=3*n-2
edges=list(itertools.product(range(n),repeat=3));ei={e:i for i,e in enumerate(edges)}
A=np.zeros((3*n,n**3),dtype=np.int64)
for e,(i,j,k) in enumerate(edges):A[i,e]=A[n+j,e]=A[2*n+k,e]=1
rows=list(range(n))+list(range(n,2*n-1))+list(range(2*n,3*n-1));AA=A[rows];b=np.ones(r)
initial=sorted([ei[e] for i in range(n-1) for e in [(i,i,i+1),(i,i+1,i),(i+1,i,i)]]+[ei[(n-1,n-1,n-1)]])
rng=np.random.default_rng(a.seed);basis=initial.copy();seen=set();best=-1;rec=[];start=time.time();stale=0
for step in range(a.steps):
 B=AA[:,basis];inv=np.linalg.inv(B);det=round(np.linalg.det(B));xx=inv@b
 if min(xx)<1e-9:
  basis=initial.copy();continue
 U=inv@AA;rat=np.divide(xx[:,None],U,out=np.full(U.shape,np.inf),where=U>1e-9);lv=np.argmin(rat,axis=0);theta=rat[lv,np.arange(n**3)]
 candidates=[]
 for j in range(n**3):
  if j in basis:continue
  i=lv[j];dd=round(det*U[i,j]);
  if not dd:continue
  yy=xx-theta[j]*U[:,j];yy[i]=theta[j]
  if min(yy)<1e-8:continue
  nb=basis.copy();nb[i]=j;key=tuple(sorted(nb))
  if key in seen:continue
  den=abs(dd)
  ints=np.rint(yy*den).astype(np.int64)
  if not np.array_equal(AA[:,nb]@ints,np.full(r,den)):continue
  g=math.gcd(den,*list(map(int,ints)));d=den//g;v2=(d&-d).bit_length()-1
  candidates.append((v2+float(rng.gumbel())*0.60,key,d,ints//g))
 if not candidates:
  basis=initial.copy();seen.clear();continue
 _,key,d,ints=max(candidates,key=lambda x:x[0]);basis=list(key);seen.add(key)
 # Reconstruct at sorted basis, not prior column order.
 inv=np.linalg.inv(AA[:,basis]);sol=inv@b;nums=np.rint(sol*d).astype(np.int64)
 assert np.array_equal(AA[:,basis]@nums,np.full(r,d)) and np.all(nums>0)
 v2=(d&-d).bit_length()-1
 if v2>best:
  es=[edges[k] for k in basis];free=all(len(set((e[i],e[j]) for e in es))==len(es) for i,j in [(0,1),(0,2),(1,2)])
  best=v2;entry={'step':step,'v2':v2,'denominator':d,'support':es,'numerators':list(map(int,nums)),'free':free};rec.append(entry)
  print(json.dumps({'n':n,'step':step,'v2':v2,'den':d,'free':free,'seconds':time.time()-start}),flush=True)
  Path(a.out).write_text(json.dumps({'n':n,'steps':step+1,'records':rec,'scope':'exploratory biased simplex pivots; every reported balance exact; not exhaustive'},indent=2))
 if step%1000==999:basis=initial.copy()
Path(a.out).write_text(json.dumps({'n':n,'steps':a.steps,'records':rec,'scope':'exploratory biased simplex pivots; every reported balance exact; not exhaustive','elapsed':time.time()-start},indent=2))
