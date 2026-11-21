#!/usr/bin/env python3
"""Exact labeled-graph intertwining of the eighteen finite source actions."""
from pathlib import Path
import json,pickle,sys,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];CHAR=HERE.parent/'characters'
sys.path.insert(0,str(CHAR/'code'))
from hurwitz_mixed72_s3_core import induced
from hurwitz_mixed_reflection_map import Reflection

def propagate(source,target,start,image):
    n=len(source[0]);f=np.full(n,-1,dtype=int);inv=np.full(n,-1,dtype=int)
    f[start]=image;inv[image]=start;queue=[start]
    for u in queue:
        v=int(f[u])
        for p,q in zip(source,target):
            a,b=int(p[u]),int(q[v])
            if f[a]>=0:
                if f[a]!=b:return None
            elif inv[b]>=0:return None
            else:f[a]=b;inv[b]=a;queue.append(a)
    return f

start=time.monotonic();data=np.load(CHAR/'records/hurwitz_full_mixed_s3_compact.npz')
sub=data['subset'];n=len(sub);ix=np.full(1344,-1,dtype=int);ix[sub]=np.arange(n)
x,y=data['x'],data['y'];s,r,X,Y=induced(x,y);I=np.arange(len(s));theta=Reflection()
args,st=pickle.loads((HERE/'hurwitz_mixed_source_group_state.pkl').read_bytes())
G=PermutationGroup(args);G.__dict__.update(st);orbits=[sorted(o)for o in G.orbits()]
assert np.array_equal(G.generators[0].array_form,s)
assert np.array_equal(G.generators[1].array_form,r)
if '--rebuild' in sys.argv:
    rebuilt=PermutationGroup([Permutation(s.tolist()),Permutation(r.tolist())])
    assert rebuilt.order()==G.order()
    G=rebuilt
ca,cs=pickle.loads((CHAR/'records/hurwitz_full_mixed_s3_compact_group_state.pkl').read_bytes())
cyclic=PermutationGroup(ca);cyclic.__dict__.update(cs)
da,ds=pickle.loads((CHAR/'records/hurwitz_full_mixed_s3_compact_derived_state.pkl').read_bytes())
derived=PermutationGroup(da);derived.__dict__.update(ds)
selected=np.r_[np.arange(n),2*n+np.arange(n),3*n+np.arange(n)]
selected_index=np.full(6*n,-1,dtype=int);selected_index[selected]=np.arange(3*n)
assert all(np.array_equal(selected_index[q[selected]],g.array_form)for q,g in zip([X,Y],cyclic.generators))
assert G.order()==6*cyclic.order() and cyclic.order()==144*derived.order()
base=np.load(ROOT/'records/hurwitz_pentagon45_fibers.npz')
labels=np.load(CHAR/'records/hurwitz_full_mixed_s3_membership.npz')['passing_labels']
rows=[];Fs=[];Ts=[];all_new=[];tau=s[r];powers=[I]
while True:
    p=tau[powers[-1]]
    if np.array_equal(p,I):break
    powers.append(p)
for i,j in labels:
    a0=base[f'R_{i}'][j];t0=theta(a0);a,t=ix[a0[sub]],ix[t0[sub]]
    ai,ti,xi,yi=np.argsort(a),np.argsort(t),np.argsort(x),np.argsort(y)
    bs=[a,ai,t[ai],ti,xi[t[x]],y[a[ti[yi]]]]
    f=np.concatenate([k*n+b for k,b in enumerate(bs)]);sf=s[f];fr=np.argsort(f)[r]
    assert np.array_equal(sf[sf],I) and np.array_equal(fr[fr[fr]],I)
    T=np.full(len(s),-1,dtype=int);local=[]
    for orb in orbits:
        found=None
        for w in orb:
            tr=propagate([s,r],[sf,fr],orb[0],w)
            if tr is not None and np.all(tr[orb]>=0):found=tr;break
        local.append(found is not None)
        if found is not None:T[orb]=found[orb]
    yes=all(local)
    if yes:
        assert len(set(T))==len(T)
        assert np.array_equal(T[s],sf[T]) and np.array_equal(T[r],fr[T])
    inner=bool(yes and G.contains(Permutation(T.tolist())))
    pure=bool(inner and np.array_equal(T//n,I//n))
    derived_pure=bool(pure and derived.contains(Permutation(selected_index[T[selected]].tolist())))
    row={'candidate':int(i),'fiber_index':int(j),'same_orbit_intertwiners':local,
         'full_intertwiner':yes,'intertwiner_in_source_image':inner,'intertwiner_in_pure_image':pure,
         'intertwiner_in_derived_pure_image':derived_pure}
    rows.append(row);Fs.append(f);Ts.append(T);all_new.append(sf)
    print(row,'elapsed',time.monotonic()-start,flush=True)
np.savez_compressed(HERE/'hurwitz_mixed_source_intertwiners.npz',s=s,r=r,x=X,y=Y,
                    labels=labels,f=Fs,intertwiners=Ts)
classes=[];covered=set()
for i,sf in enumerate(all_new):
    if i in covered:continue
    cl=[]
    for j,t in enumerate(all_new):
        for k,p in enumerate(powers):
            if np.array_equal(p[sf[np.argsort(p)]],t):cl.append([j,k]);covered.add(j);break
    classes.append(cl)
out={'source_order':int(G.order()),'source_degree':len(s),'source_orbit_degrees':list(map(len,orbits)),
     'cases':rows,'tau_conjugacy_classes':classes,'tau_order':len(powers),
     'explicit_pure_frame_labels':[[row['candidate'],row['fiber_index']]for row in rows if row['intertwiner_in_pure_image']],
     'explicit_derived_pure_frame_labels':[[row['candidate'],row['fiber_index']]for row in rows if row['intertwiner_in_derived_pure_image']],
     'elapsed_seconds':time.monotonic()-start,
     'scope':'Explicit finite permutation intertwiners prove surjectivity when present. No pre-assumed kernel invariance or profinite realization.'}
(HERE/'hurwitz_mixed_source_intertwiners.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='cases'},indent=2),flush=True)
