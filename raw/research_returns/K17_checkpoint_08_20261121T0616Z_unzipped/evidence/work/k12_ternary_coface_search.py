"""Discovery of rays fixed by an odd reflection on every full-rank facet."""
from pathlib import Path
from itertools import combinations,product
from math import gcd
from functools import reduce
import json,numpy as np
forms=json.loads(Path('work/k12_ternary_glue_form_data.json').read_text());out=[]
def canon(v):
 v=tuple(map(int,v));g=reduce(gcd,(abs(x)for x in v))
 if not g:return None
 v=tuple(x//g for x in v)
 return v if next(x for x in v if x)>0 else tuple(-x for x in v)
for f in forms:
 B=f['gale_columns'];V=np.asarray(f['Lmin_vectors'],dtype=np.int64);c=f['colors'];AB=np.asarray(f['ambient_basis_numerator'],dtype=np.int64);W=np.asarray(f['minimum_vectors'],dtype=np.int64)
 facets=[]
 for i,bi in enumerate(B):
  if not any(bi):continue
  k=next(k for k,x in enumerate(bi)if x);witnesses={}
  for a,b in combinations([j for j in range(13)if j!=i],2):
   for e in [-1,1]:
    diff=[B[a][l]-e*B[b][l]for l in range(3)]
    if diff[k]%bi[k]:continue
    t=diff[k]//bi[k]
    if diff!=[t*x for x in bi]or(c[a]-e*c[b]-t*c[i])%3:continue
    vals=[0]*13;vals[a]=1;vals[b]=-e;vals[i]=-t;phi=vals[:10]
    assert all(sum(phi[l]*int(V[j,l])for l in range(10))==vals[j]for j in range(13))
    phiamb=tuple(int(x)for x in np.asarray(phi)@AB);key=canon(phiamb)
    witnesses.setdefault(key,{'deleted':i,'a':a,'b':b,'sign':e,'phi_Lmin':phi,'phi_ambient_numerator':phiamb})
  assert witnesses
  facets.append(list(witnesses.values()))
 candidates=set()
 for count in range(1,5):
  for support in combinations(range(10),count):
   for signs in product([-1,1],repeat=count-1):
    v=[0]*10;v[support[0]]=1
    for j,e in zip(support[1:],signs):v[j]=e
    candidates.add(tuple(v))
 for a,b in combinations(range(13),2):
  for e in [-1,1]:
   v=canon(W[a]+e*W[b])
   if v:candidates.add(v)
 old={canon(v)for v in W};candidates=sorted(candidates-old);C=np.asarray(candidates,dtype=np.int64)
 good=np.ones(len(C),dtype=bool)
 for i,b in enumerate(B):
  if not any(b):
   assert i<10
   good&=(C@AB[i,:]==0)
 for ws in facets:
  P=np.asarray([w['phi_ambient_numerator']for w in ws],dtype=np.int64)
  good&=np.any(C@P.T==0,axis=1)
 found=C[good];Q=np.asarray(f['integer_gram'],dtype=float)/f['gram_denominator']
 norms=np.einsum('bi,ij,bj->b',found,Q,found)if len(found)else[]
 order=np.argsort(norms)[:80];entries=[]
 for k in order:
  v=found[k];selected=[]
  for ws in facets:selected.append(next(w for w in ws if sum(x*int(y)for x,y in zip(w['phi_ambient_numerator'],v))==0))
  entries.append({'vector':v.tolist(),'old_norm':float(norms[k]),'facet_reflections':selected})
 item={'record':f['record'],'orbit':f['orbit'],'facet_reflection_counts':[len(w)for w in facets],'small_fixed_rays':int(len(found)),'candidates':entries};out.append(item)
 print(f['record'],f['orbit'],[len(w)for w in facets],len(found),[round(x['old_norm'],3)for x in entries[:3]],flush=True)
Path('work/k12_ternary_coface_search.json').write_text(json.dumps(out,indent=2)+'\n')
