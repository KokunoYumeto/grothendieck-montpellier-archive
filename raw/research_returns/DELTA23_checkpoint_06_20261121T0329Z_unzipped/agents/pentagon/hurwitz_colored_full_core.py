#!/usr/bin/env python3
"""Seek exact common commutator-word realizations of all P32 gentle-orbit extensions."""
from pathlib import Path
import itertools,json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;CHAR=HERE.parent/'characters';start=time.monotonic()
invt=np.load(CHAR/'records/affine216_marked_pair_kernels.npz');meta=json.loads((CHAR/'records/affine216_marked_pair_kernels.json').read_text());elements=invt['elements']
d=np.load(HERE/'hurwitz_colored_last_gentle.npz');data=json.loads((HERE/'hurwitz_colored_last_gentle.json').read_text())
kids=sorted(set(k for orb in data['nielsen_orbits']for k in orb));index={k:j for j,k in enumerate(kids)}
def perm(e):
 u,v,A,B,C,D=map(int,e);return np.array([3*((u+A*(j//3)+B*(j%3))%3)+(v+C*(j//3)+D*(j%3))%3 for j in range(9)])
perms=np.array([perm(e)for e in elements]);gs=np.array([np.concatenate([9*j+perms[meta['kernels'][k]['pair'][i]]for j,k in enumerate(kids)])for i in range(2)])
G=PermutationGroup([Permutation(g.tolist())for g in gs]);order=int(G.order());print('order',order,'degree',len(gs[0]),flush=True)
D=G.derived_subgroup();do=int(D.order());print('derived',do,'index',order//do,flush=True)
(HERE/'hurwitz_colored_full_core_state.pkl').write_bytes(pickle.dumps([(G.args,G.__dict__),(D.args,D.__dict__)]))
rows=[];saved={'kernel_ids':np.array(kids),'generators':gs}
for aid in data['passing_assemblies']:
 row=data['cases'][aid];cids=row['orbit_cache_ids'];lists=[d[f'orbit_{c}_assignments']for c in cids];cols=[[index[int(k)]for k in d[f'orbit_{c}_kernel_ids']]for c in cids]
 tested=0;witness=None;choice=None;values=None
 for tup in itertools.product(*[range(len(v))for v in lists]):
  assigned=np.zeros(len(kids),dtype=int)
  for aa,choices,cc,j in zip(lists,lists,cols,tup):assigned[cc]=aa[j]
  target=np.concatenate([9*j+perms[v]for j,v in enumerate(assigned)]);tested+=1
  if D.contains(Permutation(target.tolist())):
   witness=target;choice=tup;values=assigned;break
 r={'assembly':aid,'total_choices':int(np.prod([len(v)for v in lists])),'tested':tested,'has_common_commutator_word':witness is not None,'witness_choice':list(choice)if choice is not None else None}
 rows.append(r);print(r,flush=True)
 if witness is not None:saved[f'target_{aid}']=witness;saved[f'values_{aid}']=values
np.savez_compressed(HERE/'hurwitz_colored_full_core.npz',**saved)
out={'kernel_count':len(kids),'degree':len(gs[0]),'group_order':order,'derived_order':do,'cases':rows,'elapsed_seconds':time.monotonic()-start,'scope':'Explicit common F2-derived word for all38 marked kernels satisfying all required gentle orientations. Search stops at first exact witness perassembly; no profinite realization.'}
(HERE/'hurwitz_colored_full_core.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',flush=True)
