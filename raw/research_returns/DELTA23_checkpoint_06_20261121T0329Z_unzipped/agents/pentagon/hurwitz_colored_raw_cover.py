#!/usr/bin/env python3
"""Literal fixed-product colored5376 Hurwitz cover, degree32256."""
from pathlib import Path
import json,time
import numpy as np
HERE=Path(__file__).resolve().parent
start=time.monotonic()
invt=np.load(HERE.parent/'characters/records/affine216_marked_pair_kernels.npz')
mt,iv,els=invt['multiplication'],invt['inverse'],invt['elements']
ix={tuple(map(int,a)):i for i,a in enumerate(els)};one=ix[(0,0,1,0,0,1)]
base=np.load(HERE/'hurwitz_colored_inverse_orbit_12.npz')
tuples=np.array([[ix[tuple(map(int,g))]for g in row]for row in base['tuple_elements']])
products=np.full(len(tuples),one,dtype=int)
for j in range(4):products=mt[products,tuples[:,j]]
p=int(products[0]);powers=[one]
for j in range(1,6):powers.append(int(mt[powers[-1],p]))
assert len(set(powers))==6 and mt[powers[-1],p]==one
centralizer=np.flatnonzero(mt[:,p]==mt[p,:]);assert set(centralizer)==set(powers)
conj=mt[mt[np.arange(216)[:,None],np.arange(216)[None,:]],iv[:,None]]
transport={a:int(np.where(conj[:,a]==p)[0][0])for a in set(products)}
raw=[]
for row,prod in zip(tuples,products):
 t=conj[transport[int(prod)],row]
 raw.extend(conj[h,t]for h in powers)
raw=np.array(raw,dtype=np.int16);index={tuple(map(int,t)):i for i,t in enumerate(raw)}
assert len(raw)==len(index)==32256
prod=np.full(len(raw),one,dtype=int)
for j in range(4):prod=mt[prod,raw[:,j]]
assert np.all(prod==p)
N=len(raw);I=np.arange(N);gs=[]
for j in range(3):
 moved=raw.copy();u,v=raw[:,j],raw[:,j+1]
 moved[:,j]=mt[mt[u,v],iv[u]];moved[:,j+1]=u
 g=np.array([index[tuple(map(int,t))]for t in moved],dtype=np.int32)
 assert len(set(g))==N and np.array_equal(g//6,base['generators'][j,I//6]);gs.append(g)
A,B,C=gs;deck=6*(I//6)+(I%6+1)%6
assert np.array_equal(A[B[A]],B[A[B]]) and np.array_equal(B[C[B]],C[B[C]]) and np.array_equal(A[C],C[A])
w=A[B[C]];assert np.array_equal(w[w[w[w]]],deck)
assert all(np.array_equal(g[deck],deck[g])for g in gs)
sph=np.load(HERE/'hurwitz_spherical_five_orbit.npz');assert np.array_equal(sph['tuples'][1344:,:4],tuples)
oldblock=sph['block_map'][1344:];blockids=np.unique(oldblock);assert len(blockids)==48
blockmap=np.searchsorted(blockids,oldblock)
assert all(np.sum(blockmap==j)==112 for j in range(48))
np.savez_compressed(HERE/'hurwitz_colored_raw_cover.npz',generators=gs,tuples=raw,group_elements=els,product=els[p],
 deck=deck,base_generators=base['generators'],block_map=blockmap,spherical_block_ids=blockids,product_transporters=np.array([transport[int(a)]for a in products]))
out={'base_degree':5376,'raw_degree':32256,'fixed_product':els[p].tolist(),'centralizer_order':6,'blocks':48,'all_braid_relations':True,'full_twist_deck':True,'elapsed_seconds':time.monotonic()-start,'scope':'Exact finite raw colored cover; no GT-lift filter in this construction.'}
(HERE/'hurwitz_colored_raw_cover.json').write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)
