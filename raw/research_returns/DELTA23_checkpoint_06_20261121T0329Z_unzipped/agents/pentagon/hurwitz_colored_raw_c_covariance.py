#!/usr/bin/env python3
"""Solve full raw C covariance in the product of all certified local R fibers."""
from pathlib import Path
import json,time
import numpy as np
HERE=Path(__file__).resolve().parent;start=time.monotonic()
raw=np.load(HERE/'hurwitz_colored_raw_cover.npz');A,B,C=raw['generators'];N=len(C);I=np.arange(N);n=N//6
baseparts=np.load(HERE/'hurwitz_colored_inverse_12_mixed.npz');rawparts=np.load(HERE/'hurwitz_colored_raw_mixed_projection.npz');fibers=np.load(HERE/'hurwitz_colored_raw_mixed_local.npz')
localmeta=json.loads((HERE/'hurwitz_colored_raw_mixed_local.json').read_text());assert localmeta['passing_assemblies']==[0]
lift=np.load(HERE/'hurwitz_colored_raw_last_pair.npz');gentle=np.load(HERE/'hurwitz_colored_last_gentle.npz');v=lift['base_V'];W=6*v[I//6]+(I%6+gentle['potential_0'][I//6])%6
Cnew=W[C[np.argsort(W)]];c=C[::6]//6;ec=C[::6]%6;cn=Cnew[::6]//6;en=Cnew[::6]%6
phase0=np.zeros(n,dtype=int);r=np.full(n,-1,dtype=int);bases={2:[],3:[]};kernel_dims=[]
def rref(m,p):
 a=np.array(m,dtype=int,copy=True)%p;row=0;cols=[]
 for col in range(a.shape[1]):
  nz=np.flatnonzero(a[row:,col])
  if not len(nz):continue
  j=row+int(nz[0]);a[[row,j]]=a[[j,row]];a[row]=a[row]*pow(int(a[row,col]),-1,p)%p
  coeff=a[:,col].copy();coeff[row]=0;a=(a-coeff[:,None]*a[row][None,:])%p
  cols.append(col);row+=1
  if row==a.shape[0]:break
 return a,cols
for row in localmeta['cases']:
 k=row['component'];sub=baseparts[f'orbit_{k}'];RR=fibers[f'R_0_{k}'];assert len(RR)>0
 rp=RR[:,::6]//6;assert np.all(rp==rp[0]);r[sub]=sub[rp[0]]
 phases=RR[:,::6]%6;phase0[sub]=phases[0];delta=(phases-phases[0])%6
 dims=[]
 for p in[2,3]:
  rr,piv=rref(delta,p);bb=rr[:len(piv)];dims.append(len(bb))
  for u in bb:
   g=np.zeros(n,dtype=int);g[sub]=u;bases[p].append(g)
 assert len(RR)==2**dims[0]*3**dims[1]
 kernel_dims.append({'component':k,'fiber_size':len(RR),'dim2':dims[0],'dim3':dims[1]})
assert min(r)>=0 and np.array_equal(cn[r],r[c])
rhs=(en[r]-ec-phase0[c]+phase0)%6
solutions={};saved={'base_R':r,'reference_phase':phase0,'raw_V':W};outrows=[]
for p in[2,3]:
 bs=np.array(bases[p],dtype=int).reshape(-1,n);mat=(bs[:,c]-bs).T%p;b=rhs%p
 aug,piv=rref(np.c_[mat,b],p);nv=len(bs);valid=nv not in piv
 x=np.zeros(nv,dtype=int);null=[]
 if valid:
  for row,col in enumerate(piv):x[col]=aug[row,nv]
  for free in range(nv):
   if free in piv:continue
   u=np.zeros(nv,dtype=int);u[free]=1
   for row,col in enumerate(piv):u[col]=-aug[row,free]%p
   null.append(u)
  e=(phase0+x@bs)%p;assert np.array_equal((e[c]-e)%p,(en[r]-ec)%p);solutions[p]=e
  saved[f'phase_particular_{p}']=e;saved[f'phase_nullspace_{p}']=np.array([u@bs%p for u in null]).reshape(-1,n)
 saved[f'local_phase_basis_{p}']=bs
 outrows.append({'prime':p,'variables':nv,'rank':len(piv),'consistent':valid,'solution_dimension':len(null)if valid else None})
 print(outrows[-1],flush=True)
valid=len(solutions)==2
if valid:
 e=(3*solutions[2]+4*solutions[3])%6;R=6*r[I//6]+(I%6+e[I//6])%6
 assert np.array_equal(Cnew[R],R[C]);assert len(set(R))==N
 for row in localmeta['cases']:
  k=row['component'];sub=rawparts[f'raw_subset_{k}'];loc=np.full(N,-1,dtype=int);loc[sub]=np.arange(len(sub));part=loc[R[sub]]
  assert any(np.array_equal(part,u)for u in fibers[f'R_0_{k}'])
 saved['raw_R_witness']=R;saved['phase_witness']=e
np.savez_compressed(HERE/'hurwitz_colored_raw_c_covariance.npz',**saved)
out={'all_local_fibers_affine':True,'local_fiber_dimensions':kernel_dims,'linear_systems':outrows,'full_C_covariance_in_local_product':valid,'elapsed_seconds':time.monotonic()-start,
 'scope':'Exact full raw C covariance in product of all local R fibers. Membership in the globally generated raw mixed group and same-word cross-quotient constraints remain additional.'}
(HERE/'hurwitz_colored_raw_c_covariance.json').write_text(json.dumps(out,indent=2)+'\n');print('full_C_covariance',valid,flush=True)
