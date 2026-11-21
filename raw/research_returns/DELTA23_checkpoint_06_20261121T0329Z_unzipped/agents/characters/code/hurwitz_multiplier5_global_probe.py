#!/usr/bin/env python3
"""Necessary global multiplier-five transporters, with orthogonal coordinates."""
from pathlib import Path
import itertools,json,contextlib,io,importlib.util
import numpy as np
from hurwitz_multiplier5_global_seeds import HERE,PENT,FIVE,A,B,C,Z,blocks,bm,qA,qZ,trans,points,loc,local,ort,matpow,linear_equations
from hurwitz_multiplier5_detector import power

def enumerate_hom(N):
 d=len(N)
 # One of each pair M,-M: first nonzero coefficient equals1.
 for first in range(d):
  tails=np.array(list(itertools.product(range(3),repeat=d-first-1)),dtype=int)
  if tails.ndim==1:tails=tails.reshape(1,0)
  for start in range(0,len(tails),2048):
   tt=tails[start:start+2048]
   v=np.repeat(N[first][None,:,:],len(tt),axis=0)
   if len(N)>first+1:v=(v+np.einsum('bi,ijk->bjk',tt,N[first+1:]))%3
   gram=np.einsum('bji,jk,bkl->bil',v,ort.Q,v)%3
   keep=np.all(gram==ort.Q,axis=(1,2))|np.all(gram==2*ort.Q%3,axis=(1,2))
   for M,G in zip(v[keep],gram[keep]):
    yield M, 1 if np.array_equal(G,ort.Q) else 2

def seed_maps(j,p):
 src=[ort.lift_permutation(local(g,j))[0]for g in [p,power(Z,2)]]
 dst=[ort.lift_permutation(local(power(g,5),j))[0]for g in [p,power(Z,2)]]
 cidx={tuple(v):i for i,v in enumerate(ort.coords)}
 mats=[];perms=[];types=[];dims=[]
 for signs in itertools.product([1,2],repeat=2):
  N=ort.nullspace(np.vstack([linear_equations(s,t*e%3)for s,t,e in zip(src,dst,signs)])).reshape(-1,6,6)
  dims.append(len(N))
  for M,mu in enumerate_hom(N):
   perm=np.array([cidx[ort.proj(M@v)]for v in ort.coords],dtype=np.int16)
   assert all(np.array_equal(perm[local(g,j)],local(power(g,5),j)[perm])for g in[p,power(Z,2)])
   mats.append(M);perms.append(perm);types.append([ort.determinant(M),mu])
 assert len({p.tobytes()for p in perms})==len(perms)
 return np.array(mats),np.array(perms),np.array(types),dims

def transports(seed):
 out={seed:(np.arange(1344),np.arange(1344))};queue=[seed]
 for j in queue:
  g,g5=out[j]
  for a,a5,qa in[(A,power(A,5),qA),(Z,power(Z,5),qZ)]:
   k=int(qa[j])
   if k not in out:out[k]=(a[g],a5[g5]);queue.append(k)
 return out

def run():
 saved={};rows=[]
 for j,p in[(0,A),(1,power(A,3))]:
  mats,perms,types,dims=seed_maps(j,p)
  saved[f'matrices_{j}']=mats;saved[f'permutations_{j}']=perms;saved[f'types_{j}']=types
  row={'seed':j,'hom_dimensions':dims,'local_PGO_count':len(perms),'types':{str(list(map(int,t))):int(np.sum(np.all(types==t,axis=1)))for t in np.unique(types,axis=0)}}
  rows.append(row);print(row,flush=True)
 # Known local lifts must have one common determinant/multiplier coset.
 inp=np.load(HERE/'records/hurwitz_multiplier5_four_blocks.npz');subset=inp['subset']
 mixed=np.load(PENT/'hurwitz_global_conjugators.npz')['mixed72_V_1'][1]
 observed=[]; known_maps=[]
 for no in inp['first448_pass_indices']:
  for widx,w448 in enumerate(inp[f'W448_{no}']):
   W=np.full(1344,-1,dtype=int);W[subset]=subset[w448]
   typ=[]
   for j in[7,8,10,11]:
    k=int(bm[W[points[j][0]]]);p=loc[k,W[points[j]]]
    M,mu=ort.lift_permutation(p);typ.append([ort.determinant(M),mu])
   assert all(t==typ[0]for t in typ)
   assert np.array_equal(W[A[subset]],power(A,5)[W[subset]])
   assert np.array_equal(W[Z[subset]],power(Z,5)[W[subset]])
   assert np.array_equal(W[mixed[subset]],mixed[W[subset]])
   known_maps.append(W[subset])
   observed.append({'detector':int(no),'lift':widx,'type':typ[0]})
 print('known types',sorted(set(tuple(r['type'])for r in observed)),flush=True)
 saved['known_labels']=np.array([[r['detector'],r['lift'],*r['type']]for r in observed])
 saved['known_subset']=subset
 saved['known_maps']=np.array(known_maps)
 assert len({v.tobytes()for v in known_maps})==36
 # Centralization of the remaining mixed V is blockwise and transport-compatible,
 # because mixed V itself commutes A andZ. For a seed-target shift g, the
 # relevant intertwiner is g^5 followed by a self-seed map.
 central=[]; assembly_counts=[]
 for j in[0,1]:
  T=transports(j);vals=saved[f'permutations_{j}'];types=saved[f'types_{j}']
  orbit_subset=np.flatnonzero(np.isin(bm,list(T)))
  partial_maps=[]; partial_labels=[]
  vj=loc[j,mixed[points[j]]]
  for k,(g,g5)in T.items():
   target=int(bm[g5[points[j][0]]])
   assert len(set(map(int,bm[g5[points[j]]])))==1
   vk=loc[target,mixed[points[target]]]
   carry=loc[target,g5[points[j]]]
   for typ in set(tuple(r['type'])for r in observed):
    chosen=np.flatnonzero(np.all(types==typ,axis=1))
    passing=[int(i)for i in chosen if np.array_equal(carry[vals[i][vj]],vk[carry[vals[i]]])]
    central.append({'seed':j,'target':target,'type':list(typ),'total':len(chosen),'centralizing':len(passing)})
    saved[f'centralizing_{j}_{target}_{typ[0]}_{typ[1]}']=np.array(passing)
    for i in chosen:
     W=np.full(1344,-1,dtype=int)
     image=g5[points[j]][vals[i]]
     for h,h5 in T.values():W[h[points[j]]]=h5[image]
     assert np.all(W[orbit_subset]>=0)
     assert len(set(map(int,W[orbit_subset])))==len(orbit_subset)
     assert np.array_equal(W[A[orbit_subset]],power(A,5)[W[orbit_subset]])
     assert np.array_equal(W[Z[orbit_subset]],power(Z,5)[W[orbit_subset]])
     assert np.array_equal(W[mixed[orbit_subset]],mixed[W[orbit_subset]])
     partial_maps.append(W[orbit_subset]);partial_labels.append([target,int(i)])
  assert len({v.tobytes()for v in partial_maps})==len(partial_maps)
  saved[f'partial_subset_{j}']=orbit_subset
  saved[f'partial_maps_{j}']=np.array(partial_maps)
  saved[f'partial_labels_{j}']=np.array(partial_labels)
  assembly_counts.append(len(partial_maps))
 print('seed centralization',central,flush=True)
 np.savez_compressed(HERE/'records/hurwitz_multiplier5_global_probe.npz',**saved)
 assert assembly_counts==[72,96]
 out={'multiplier_mod12':5,'seed_maps':rows,'known_four_block_types':observed,'mixed_centralization':central,
      'partial_assembly_counts':assembly_counts+[len(known_maps)],
      'global_assemblies':int(np.prod(assembly_counts)*len(known_maps)),
      'all_partial_assemblies_exactly_verified_for_A5_Z5_and_mixed_centralization':True,
      'scope':'Complete local PGO seed maps for A,Z power5; common determinant/multiplier type from known four-block action. All248832 relaxed global assemblies commute the remaining mixed V. Global normalizer and full f covariance are not asserted.'}
 (HERE/'records/hurwitz_multiplier5_global_probe.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
