#!/usr/bin/env python3
"""Exhaust the216 canonical colored raw lifts against the actual last-meridian formula and gentle identities."""
from pathlib import Path
import itertools,json,time
import numpy as np
HERE=Path(__file__).resolve().parent;CHAR=HERE.parent/'characters';start=time.monotonic()
invt=np.load(CHAR/'records/affine216_marked_pair_kernels.npz');meta=json.loads((CHAR/'records/affine216_marked_pair_kernels.json').read_text())
mt,iv,pk,nielsen=[invt[k]for k in['multiplication','inverse','pair_kernel','nielsen']];elements=invt['elements']
index={tuple(map(int,e)):i for i,e in enumerate(elements)};one=index[(0,0,1,0,0,1)]
raw=np.load(HERE/'hurwitz_colored_raw_cover.npz');lifts=np.load(HERE/'hurwitz_colored_raw_last_pair.npz')
liftmeta=json.loads((HERE/'hurwitz_colored_raw_last_pair.json').read_text())
last=raw['tuples'][:,3];N=len(last);I=np.arange(N);blocks=raw['block_map'];V=lifts['base_V'];Vi=np.argsort(V)
blockshift=lifts['block_potential'];phase=lifts['canonical_phase']
p=index[tuple(map(int,raw['product']))];a=int(iv[p]);bs=np.unique(last);kids=sorted(set(map(int,pk[a,bs])))

def members(x,y):
 todo=[one];seen={one}
 for g in todo:
  for h in(x,y):
   q=int(mt[g,h])
   if q not in seen:seen.add(q);todo.append(q)
 return np.array(todo,dtype=int)
def derived(x,y,mem):
 c=int(mt[mt[mt[x,y],iv[x]],iv[y]]);gens=np.unique(mt[mt[mem,c],iv[mem]])
 todo=[one];seen={one}
 for g in todo:
  for h in gens:
   q=int(mt[g,h])
   if q not in seen:seen.add(q);todo.append(q)
 return np.array(sorted(todo),dtype=int)
mapcache={};dercache={}
def mapping(x,y):
 key=int(x),int(y)
 if key not in mapcache:
  k=int(pk[key]);can=invt[f'kernel_{k}_members'];new=members(*key);assert len(can)==len(new)
  fwd=np.full(216,-1,dtype=int);back=fwd.copy();fwd[can]=new;back[new]=can;mapcache[key]=k,fwd,back
 return mapcache[key]
def canonical_derived(k):
 if k not in dercache:
  x,y=meta['kernels'][k]['pair'];dercache[k]=derived(x,y,invt[f'kernel_{k}_members'])
 return dercache[k]
models={};saved={'kernel_ids':np.array(kids)}
for k in kids:
 der=canonical_derived(k);these=np.array([int(b)for b in bs if pk[a,b]==k]);images=[]
 for b in these:
  _,fwd,_=mapping(a,b);f=fwd[der];assert min(f)>=0;images.append(mt[mt[iv[f],b],f])
 models[k]=these,der,np.stack(images,axis=1)
 saved[f'kernel_{k}_derived']=der
orbits=[];seen=set()
for k in kids:
 if k in seen:continue
 todo=[k]
 for q in todo:
  for z in nielsen[q]:
   if int(z)not in todo:todo.append(int(z))
 todo.sort();orbits.append(todo);seen.update(todo)
cache={};cache_rows=[]
def extensions(orbit,allowed):
 sig=tuple((k,tuple(map(int,allowed[k])))for k in orbit if k in allowed);key=tuple(orbit),sig
 if key in cache:return cache[key]
 base=min((k for k in orbit if k in allowed),key=lambda k:len(allowed[k]));x,y=meta['kernels'][base]['pair'];z=int(iv[mt[x,y]])
 directed=[(x,y),(y,z),(z,x),(y,x),(z,y),(x,z)];maps=[mapping(*q)for q in directed];assert set(q[0]for q in maps)==set(orbit)
 found=[]
 for g0 in allowed[base]:
  for g1 in canonical_derived(base):
   g2=int(iv[mt[g1,g0]]);vals=[g0,g1,g2,iv[g0],iv[g1],iv[g2]];assign={};valid=True
   for(k,_,back),value in zip(maps,vals):
    q=int(back[value]);assert q>=0
    if(k in assign and assign[k]!=q)or(k in allowed and q not in allowed[k]):valid=False;break
    assign[k]=q
   if not valid:continue
   def ev(x,y):
    k,fwd,_=mapping(x,y);q=int(fwd[assign[k]]);assert q>=0;return q
   for k in orbit:
    xx,yy=meta['kernels'][k]['pair'];zz=int(iv[mt[xx,yy]])
    fxy=ev(xx,yy);fyx=ev(yy,xx);fyz=ev(yy,zz);fzx=ev(zz,xx)
    if mt[fyx,fxy]!=one or mt[mt[fzx,fyz],fxy]!=one:valid=False;break
    neg=one
    for q in(fzx,iv[zz],fyz,iv[yy],fxy,iv[xx]):neg=int(mt[neg,q])
    if neg!=one:valid=False;break
   if valid:found.append(tuple(assign[k]for k in orbit))
 found=sorted(set(found));cid=len(cache_rows);cache[key]=cid
 cache_rows.append({'orbit':orbit,'given':[(k,list(v))for k,v in sig],'extension_count':len(found)})
 saved[f'orbit_{cid}_kernel_ids']=np.array(orbit);saved[f'orbit_{cid}_assignments']=np.array(found,dtype=int).reshape(-1,len(orbit))
 return cid
# Anchored associator values: C34 zeros and P10 cubic e=1,rho=0.
zero={37,42,49,58,61,66,73,78};anchor={k:one for k in zero}
x0,y0=map(int,invt['cubic_pair']);_,_,back=mapping(x0,y0);anchor[77]=int(back[index[(1,1,1,0,0,1)]])
components=liftmeta['components']; choices=[c['allowed_component_shifts']for c in components]
rows=[];passing=[];passes_partition=0;passes_fibers=0
for ordinal,ts in enumerate(itertools.product(*choices)):
 shift=blockshift.copy()
 for component,t in zip(components,ts):shift[component['blocks']]=(shift[component['blocks']]+t)%6
 pot=(phase+shift[blocks])%6
 Wi=6*Vi[I//6]+(I%6-pot[Vi[I//6]])%6
 desired=last[Wi];target={};valid=True
 for b in bs:
  out=np.unique(desired[last==b])
  if len(out)!=1:valid=False;break
  target[int(b)]=int(out[0])
 row={'assembly':ordinal,'component_shifts':list(map(int,ts)),'last_partition':valid}
 if not valid:rows.append(row);continue
 passes_partition+=1;allowed={}
 for k,(these,der,pred)in models.items():
  want=np.array([target[int(b)]for b in these]);aa=der[np.all(pred==want,axis=1)]
  if k in anchor:aa=aa[aa==anchor[k]]
  allowed[k]=aa
 row['fiber_sizes']={str(k):len(v)for k,v in allowed.items()};valid=all(len(v)for v in allowed.values())
 row['fibers_nonempty']=valid
 if not valid:rows.append(row);continue
 passes_fibers+=1;cids=[extensions(o,allowed)for o in orbits];counts=[cache_rows[c]['extension_count']for c in cids]
 row['orbit_cache_ids']=cids;row['extension_counts']=counts;row['all_gentle_orbits']=all(counts)
 if all(counts):
  passing.append(ordinal);saved[f'potential_{ordinal}']=pot;saved[f'last_map_{ordinal}']=np.array([target[int(b)]for b in bs])
  for k,v in allowed.items():saved[f'fiber_{ordinal}_{k}']=v
 rows.append(row)
 print({k:v for k,v in row.items()if k!='fiber_sizes'},flush=True)
assert len(rows)==216
# Identity actual-source control: every kernel has the identity value and
# all literal cycle identities hold, independently of the mixed anchors.
for orbit in orbits:
 ids={k:np.array([one])for k in orbit}
 cid=extensions(orbit,ids);assert cache_rows[cid]['extension_count']==1
out={'input_assemblies':len(rows),'passes_last_partition':passes_partition,'passes_derived_fibers':passes_fibers,
 'passes_gentle':len(passing),'passing_assemblies':passing,'kernel_ids':kids,'nielsen_orbits':orbits,
 'identity_cycle_control':'PASS','cases':rows,'cache':cache_rows,'elapsed_seconds':time.monotonic()-start,
 'scope':'Necessary literal colored F40, anchored actual E0 values and every two/three/m=-1 cycle by marked kernel. Cross-orbit common-word and full raw B/C covariance remain additional.'}
np.savez_compressed(HERE/'hurwitz_colored_last_gentle.npz',**saved)
(HERE/'hurwitz_colored_last_gentle.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in['cases','cache']},indent=2),flush=True)
