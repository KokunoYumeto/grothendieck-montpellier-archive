#!/usr/bin/env python3
"""Canonical linear raw colored lifts and literal F40 last-pair constraints."""
from pathlib import Path
import itertools,json,time
import numpy as np
HERE=Path(__file__).resolve().parent
start=time.monotonic()
raw=np.load(HERE/'hurwitz_colored_raw_cover.npz');group=raw['group_elements'];tuples=group[raw['tuples']]
blocks=raw['block_map'];deck=raw['deck'];N=len(deck);I=np.arange(N);I2=np.eye(2,dtype=int)
values=np.load(HERE/'hurwitz_full_spherical_covariance.npz')
row=next(k for k,v in enumerate(values['labels'])if np.array_equal(v,[1,0]))
V=values['conjugators'][row,1344:]-1344;assert np.array_equal(blocks[V],blocks)

def rref(a):
 a=np.array(a,dtype=int,copy=True)%3;row=0;piv=[]
 for col in range(a.shape[1]):
  nz=np.flatnonzero(a[row:,col])
  if not len(nz):continue
  j=row+int(nz[0]);a[[row,j]]=a[[j,row]];a[row]=a[row]*int(a[row,col])%3
  for k in range(a.shape[0]):
   if k!=row and a[k,col]:a[k]=(a[k]-a[k,col]*a[row])%3
  piv.append(col);row+=1
  if row==len(a):break
 return a,piv
def rank(a):return len(rref(a)[1])
def inv(a):
 n=len(a);v,piv=rref(np.c_[a,np.eye(n,dtype=int)]);assert piv[:n]==list(range(n));return v[:,n:]
def coordinates(t):
 fixed=[inv(I2-g[2:].reshape(2,2))@g[:2]%3 for g in t]
 return np.concatenate([(v-fixed[3])%3 for v in fixed[:3]])
phase=np.zeros(5376,dtype=int);local=[]
for j in range(48):
 points=np.flatnonzero(blocks==j);rows=np.array([6*int(v)+e for v in points for e in range(6)])
 partitions={}
 for row in rows:partitions.setdefault(tuple(map(int,tuples[row,:,2:].ravel())),[]).append(int(row))
 assert len(partitions)==3 and{len(v)for v in partitions.values()}=={224}
 chosen=np.array(partitions[min(partitions)]);coords=np.array([coordinates(tuples[row])for row in chosen])
 assert len({tuple(v)for v in coords})==224 and rank(coords)==6
 cindex={tuple(v):int(row)for v,row in zip(coords,chosen)}
 bypoint={int(p):[int(i)for i in np.flatnonzero(chosen//6==p)]for p in points};assert{len(v)for v in bypoint.values()}=={2}
 ids=[]
 for i,v in enumerate(coords):
  if rank(coords[ids+[i]])>len(ids):ids.append(i)
  if len(ids)==6:break
 assert len(ids)==6
 assert np.array_equal(np.array([cindex[tuple(-v%3)]for v in coords]),deck[deck[deck[chosen]]])
 images=np.array([coords[bypoint[int(V[int(chosen[i]//6)])][0]]for i in ids]).T
 good=[];ib=inv(coords[ids].T)
 for signs in itertools.product([1,2],repeat=5):
  M=images@np.diag((1,)+signs)@ib%3
  if rank(M)!=6:continue
  moved=coords@M.T%3
  if not all(tuple(v)in cindex for v in moved):continue
  target=np.array([cindex[tuple(v)]for v in moved])
  if np.array_equal(target//6,V[chosen//6]):good.append((M,target))
 assert len(good)==1
 M,target=good[0];mapping={};src,dst=chosen.copy(),target.copy()
 for e in range(3):
  mapping.update(zip(map(int,src),map(int,dst)));src,dst=deck[src],deck[dst]
 assert len(mapping)==672
 pp=np.array([mapping[6*int(p)]%6 for p in points]);phase[points]=pp
 for p,e in zip(points,pp):
  for k in range(6):assert mapping[6*int(p)+k]==6*int(V[p])+(k+int(e))%6
 local.append({'block':j,'points':points,'matrix':M})
W0=6*V[I//6]+(I%6+phase[I//6])%6;assert len(set(W0))==N and np.array_equal(W0[deck],deck[W0])
# Evaluate the required literal last-coordinate images on every known kernel.
invt=np.load(HERE.parent/'characters/records/affine216_marked_pair_kernels.npz')
mt,iv,pk=invt['multiplication'],invt['inverse'],invt['pair_kernel'];assert np.array_equal(group,invt['elements'])
index={tuple(map(int,a)):i for i,a in enumerate(group)};one=index[(0,0,1,0,0,1)];p=index[tuple(map(int,raw['product']))];a=int(iv[p])
def members(x,y):
 todo=[one];seen={one}
 for g in todo:
  for h in(x,y):
   q=int(mt[g,h])
   if q not in seen:seen.add(q);todo.append(q)
 return np.array(todo)
x0,y0=map(int,invt['cubic_pair']);f0=index[(1,1,1,0,0,1)];pos=int(np.where(members(x0,y0)==f0)[0][0])
known_zero={37,42,49,58,61,66,73,78};required={};ker={}
for b in np.unique(raw['tuples'][:,3]):
 b=int(b);k=int(pk[a,b]);ker[b]=k
 if k==77:f=int(members(a,b)[pos])
 elif k in known_zero:f=one
 else:continue
 required[b]=int(mt[mt[iv[f],b],f])
last=raw['tuples'][:,3];known=np.array([int(b)in required for b in last]);target=np.array([required.get(int(b),-1)for b in last])
allowed=[];Wi=np.argsort(W0);di=np.argsort(deck)
for j in range(48):
 rows=np.flatnonzero(blocks[I//6]==j);mask=known[rows];r=rows[mask];good=[];shifted=r.copy()
 for e in range(6):
  actual=last[Wi[shifted]]
  if np.array_equal(actual,target[r]):good.append(e)
  shifted=di[shifted]
 allowed.append(good)
 print({'block':j,'known_points':int(mask.sum()),'allowed_deck_shifts':good},flush=True)
# Raw A and z3 are fixed at multiplier one; solve block potential edges.
A,B,C=raw['generators'];z=A[B[A]];z=z[z]
a0,b0,c0=raw['base_generators'];z0=a0[b0[a0]];z0=z0[z0]
edges=[];valid=True
for q,Q in[(a0,A),(z0,z)]:
 e=Q[::6]%6
 for j in range(48):
  points=local[j]['points'];k=int(blocks[q[points[0]]]);assert np.all(blocks[q[points]]==k)
  rhs=(e[V[points]]-e[points]-phase[q[points]]+phase[points])%6
  if len(set(map(int,rhs)))!=1:valid=False
  else:edges.append((j,k,int(rhs[0])))
components=[];shift=np.full(48,-1,dtype=int)
if valid:
 for st in range(48):
  if shift[st]>=0:continue
  shift[st]=0;queue=[st]
  for j in queue:
   for u,v,e in edges:
    if u==j:k,delta=v,e
    elif v==j:k,delta=u,-e
    else:continue
    value=(int(shift[j])+delta)%6
    if shift[k]<0:shift[k]=value;queue.append(k)
    elif shift[k]!=value:valid=False
  permitted=[t for t in range(6)if all((int(shift[j])+t)%6 in allowed[j]for j in queue)]
  components.append({'blocks':queue,'allowed_component_shifts':permitted})
  if not permitted:valid=False
out={'label':[1,0],'raw_degree':N,'block_count':48,'all_framings_3x224':True,'known_last_entry_kernels':sorted(set(ker[b]for b in required)),
 'known_raw_points':int(known.sum()),'block_allowed_shifts':allowed,'A_z3_potential_consistent':valid,'components':components,
 'elapsed_seconds':time.monotonic()-start,'scope':'Canonical linear deck-equivariant raw lifts, literal F40 on known kernels77 and C34 zeros, and fixed A/z3. Full raw colored covariance and unknown E0 kernels not imposed.'}
np.savez_compressed(HERE/'hurwitz_colored_raw_last_pair.npz',base_V=V,canonical_raw_V=W0,canonical_phase=phase,
 local_matrices=np.array([v['matrix']for v in local]),block_potential=shift,known=known,required_last=target)
(HERE/'hurwitz_colored_raw_last_pair.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
