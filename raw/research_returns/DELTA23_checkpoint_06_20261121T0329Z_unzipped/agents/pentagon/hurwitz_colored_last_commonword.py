#!/usr/bin/env python3
"""Exact common-word test for the three uniquely determined colored last-pair assignments."""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;CHAR=HERE.parent/'characters';start=time.monotonic()
invt=np.load(CHAR/'records/affine216_marked_pair_kernels.npz');meta=json.loads((CHAR/'records/affine216_marked_pair_kernels.json').read_text())
elements=invt['elements'];d=np.load(HERE/'hurwitz_colored_last_gentle.npz');z=json.loads((HERE/'hurwitz_colored_last_gentle.json').read_text());kids=list(map(int,d['kernel_ids']))
def perm(e):
 u,v,A,B,C,D=map(int,e);return np.array([3*((u+A*(j//3)+B*(j%3))%3)+(v+C*(j//3)+D*(j%3))%3 for j in range(9)])
perms=np.array([perm(e)for e in elements])
x=np.concatenate([9*j+perms[meta['kernels'][k]['pair'][0]]for j,k in enumerate(kids)])
y=np.concatenate([9*j+perms[meta['kernels'][k]['pair'][1]]for j,k in enumerate(kids)])
G=PermutationGroup([Permutation(x.tolist()),Permutation(y.tolist())]);order=int(G.order());print('order',order,flush=True)
D=G.derived_subgroup();do=int(D.order());print('derived',do,'index',order//do,flush=True)
rows=[];targets=[];assignments=[]
for aid in z['passing_assemblies']:
 row=z['cases'][aid];assigned={}
 for cid in row['orbit_cache_ids']:
  ks=d[f'orbit_{cid}_kernel_ids'];vals=d[f'orbit_{cid}_assignments'];cols=[j for j,k in enumerate(ks)if int(k)in kids]
  reduced=np.unique(vals[:,cols],axis=0);assert len(reduced)==1
  assigned.update({int(ks[col]):int(value)for col,value in zip(cols,reduced[0])})
 assert set(assigned)==set(kids)
 gs=np.array([assigned[k]for k in kids]);target=np.concatenate([9*j+perms[e]for j,e in enumerate(gs)])
 inG=G.contains(Permutation(target.tolist()));inD=D.contains(Permutation(target.tolist()))
 rows.append({'assembly':aid,'values':gs.tolist(),'common_word':inG,'common_commutator_word':inD});targets.append(target);assignments.append(gs)
 print(rows[-1],flush=True)
np.savez_compressed(HERE/'hurwitz_colored_last_commonword.npz',generators=[x,y],targets=targets,kernel_ids=kids,assignments=assignments)
(HERE/'hurwitz_colored_last_commonword_state.pkl').write_bytes(pickle.dumps([(G.args,G.__dict__),(D.args,D.__dict__)]))
out={'order':order,'derived_order':do,'derived_index':order//do,'cases':rows,'elapsed_seconds':time.monotonic()-start,'scope':'Exact simultaneous16 marked E0 values in F2-derived image; unprescribed S3 values and full raw colored covariance remain additional.'}
(HERE/'hurwitz_colored_last_commonword.json').write_text(json.dumps(out,indent=2)+'\n')
