#!/usr/bin/env python3
"""F40 on the complete spherical6720 orbit, using known marked E0 values."""
from pathlib import Path
import json
import numpy as np
HERE=Path(__file__).resolve().parent
CHAR=HERE.parent/'characters'
d=np.load(CHAR/'records/affine216_marked_pair_kernels.npz')
mt,iv,pk=d['multiplication'],d['inverse'],d['pair_kernel']
elements=d['elements'];idx={tuple(map(int,a)):i for i,a in enumerate(elements)};one=idx[(0,0,1,0,0,1)]
sphere=np.load(HERE/'hurwitz_spherical_five_orbit.npz');tuples=sphere['tuples'];colors=sphere['colors']
values=np.load(HERE/'hurwitz_full_spherical_covariance.npz')
assert np.array_equal(elements,sphere['group_elements'])
conj=mt[mt[np.arange(216)[:,None],np.arange(216)[None,:]],iv[:,None]]
def canonical(a,b):
 v=np.array([conj[:,a],conj[:,b]]).T
 j=np.lexsort((v[:,1],v[:,0]))[0]
 return tuple(map(int,v[j]))
def members(a,b):
 seen={one};todo=[one]
 for g in todo:
  for h in(a,b):
   q=int(mt[g,h])
   if q not in seen:seen.add(q);todo.append(q)
 return np.array(todo)
a0,b0=map(int,d['cubic_pair']);kid0=int(pk[a0,b0]);assert kid0==77
position=int(np.where(members(a0,b0)==idx[(1,1,1,0,0,1)])[0][0])
known_zero={37,42,49,58,61,66,73,78}
lookup={}
for a,b in set((int(t[4]),int(t[3]))for t in tuples):
 kid=int(pk[a,b])
 if kid==kid0:f=int(members(a,b)[position])
 elif kid in known_zero:f=one
 else:continue
 lookup[(a,b)]=canonical(a,int(mt[mt[iv[f],b],f]))
selected=[i for i,t in enumerate(tuples)if(int(t[4]),int(t[3]))in lookup]
rows=[]
for label,V in zip(values['labels'],values['conjugators']):
 vi=np.argsort(V);bad=[]
 for i in selected:
  a,b=map(int,tuples[i,[4,3]])
  out=tuples[vi[i]];actual=canonical(int(out[4]),int(out[3]))
  if actual!=lookup[(a,b)]:bad.append(i)
 rows.append({'label':label.tolist(),'tested':len(selected),'failures':len(bad),'failed_kernel_ids':sorted(set(int(pk[tuple(tuples[i,[4,3]])])for i in bad)),'first_failure':bad[0]if bad else None})
 print(rows[-1],flush=True)
allkids,cnt=np.unique(pk[tuples[:,4],tuples[:,3]],return_counts=True)
out={'scope':'Necessary class-level F40 comparison on all6720, using exact normalized cubic value and C34 zero values. No claim on omitted kernels.','cubic_kernel_count':int(np.sum(pk[tuples[:,4],tuples[:,3]]==kid0)), 'kernel_counts':dict(zip(map(str,allkids),map(int,cnt))),'cases':rows}
(HERE/'hurwitz_colored_last_pair.json').write_text(json.dumps(out,indent=2)+'\n')
