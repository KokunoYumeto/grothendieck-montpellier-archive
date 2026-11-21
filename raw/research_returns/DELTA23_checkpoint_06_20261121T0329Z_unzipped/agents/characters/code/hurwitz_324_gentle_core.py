#!/usr/bin/env python3
"""Exact necessary gentle cycle constraints in the S3 core of the (3,2,4) S4 pair.
The induction uses right permutation products, as recorded by C11. No actual
profinite lifting or full-pentagon conclusion is drawn from a finite candidate.
"""
from pathlib import Path
import json,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parents[1]
data=json.loads((HERE/'records/induced_s4_324.json').read_text())
s=np.array(data['s']);r=np.array(data['r']);x=np.array(data['x']);y=np.array(data['y'])
p=np.array([1,2,0,3]);t=np.array([1,2,3,0]);v=np.array([3,1,2,0])
def pm(a,b):return b[a]
def pw(a,n):
    if n<0:return pw(np.argsort(a),-n)
    out=np.arange(len(a))
    for _ in range(n):out=pm(out,a)
    return out
join=[np.r_[g,24+h]for g,h in [(x,p),(y,t)]]
F=PermutationGroup([Permutation(g.tolist())for g in join]);D=F.derived_subgroup()
assert F.order()==442368 and D.order()==110592
st=time.monotonic()
arr=np.array([g.array_form for g in D.generate_schreier_sims()],dtype=np.int16)
fs=arr[:,:24];I=np.arange(24)
def batchpm(a,b):
    if a.ndim==1:return b[:,a]
    if b.ndim==1:return b[a]
    return np.take_along_axis(b,a,axis=1)
sf=fs[:,s]
mask2=np.all(batchpm(sf,sf)==I,axis=1)
invf=np.argsort(fs,axis=1);fr=r[invf]
mask3=np.all(batchpm(batchpm(fr,fr),fr)==I,axis=1)
take=np.flatnonzero(mask2&mask3);sel=arr[take];fs=sel[:,:24]
ri=np.argsort(r);r2=pm(r,r);r2i=np.argsort(r2)
B=ri[fs[:,r]];C=r2i[fs[:,r2]]
z=np.argsort(pm(x,y))
prod=batchpm(batchpm(batchpm(batchpm(batchpm(C,np.argsort(z)),B),np.argsort(y)),fs),np.argsort(x))
neg=np.all(prod==I,axis=1);final=sel[neg]
d=pm(v,np.array([0,2,1,3])) # (14)(23)
lookup0={tuple(pm(pw(t,2*e),pw(p,a))):(a,e)for a in range(3)for e in range(2)}
lookup1={tuple(pm(pw(d,e),pw(p,a))):(a,e)for a in range(3)for e in range(2)}
counts={};outside=[]
for row in final:
    f0=tuple(int(j)-24 for j in row[24:]);f1=tuple(int(j)for j in row[:4])
    if f0 not in lookup0 or f1 not in lookup1:
        outside.append([f0,f1]);continue
    a0,e0=lookup0[f0];a1,e1=lookup1[f1]
    key=f'{a0},{e0};{a1},{e1}'
    counts[key]=counts.get(key,0)+1
# Exact transitive-action intertwiner search.  It either constructs a
# permutation conjugating both generators or exhausts all 24 images of 0.
def intertwiners(old,new):
    ans=[]
    for image0 in range(24):
        trans=np.full(24,-1,dtype=int);trans[0]=image0;todo=[0];ok=True
        for i in todo:
            for u,v in zip(old,new):
                k=int(u[i]);j=int(v[trans[i]])
                if trans[k]<0:trans[k]=j;todo.append(k)
                elif trans[k]!=j:ok=False;break
            if not ok:break
        if ok and len(set(trans))==24:
            assert all(np.array_equal(trans[u],v[trans])for u,v in zip(old,new))
            ans.append(trans)
    return ans
normalizers=[]
for row in final:
    f=row[:24];images=[pm(s,f),pm(np.argsort(f),r)]
    normalizers.append(intertwiners([s,r],images))
assert all(normalizers)
# Pure-frame conjugacy orbits in the finite core, not only permutation
# normalizers outside the image group.
def pure_class(seed):
    gens=[x,y,np.argsort(x),np.argsort(y)]
    out=[seed];seen={seed.tobytes()}
    for h in out:
        for g in gens:
            w=pm(pm(g,h),np.argsort(g));key=w.tobytes()
            if key not in seen:seen.add(key);out.append(w)
    return seen
sclass=pure_class(s);rclass=pure_class(r)
assert all(pm(s,row[:24]).astype(s.dtype).tobytes()in sclass for row in final)
assert all(pm(np.argsort(row[:24]),r).astype(r.dtype).tobytes()in rclass for row in final)
out={'statement':'D23.C22 finite necessary stage','source':'S3 induction of x=(123),y=(14); right permutation convention',
     'F_order':int(F.order()),'F_derived_order':int(D.order()),'two_cycle_count':int(mask2.sum()),
     'three_cycle_count':int(mask3.sum()),'both_cycle_count':int(len(sel)),
     'negative_three_cycle_count':int(len(final)),
     'joint_344_324_residue_counts':counts,'outside_six_state_templates':len(outside),
     'all_candidates_finite_automorphism_covariance':True,
     'normalizer_counts':[len(v)for v in normalizers],
     'pure_s_frame_class_size':len(sclass),'pure_r_frame_class_size':len(rclass),
     'all_candidates_have_both_pure_frames':True,
     'elapsed_seconds':time.monotonic()-st,
     'scope':'All finite two/three-cycle constraints, m=-1, permutation covariance and pure frame conjugacy pass. No actual profinite lift or full pentagon is inferred.'}
(HERE/'records/hurwitz_324_gentle_core.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(HERE/'records/hurwitz_324_gentle_candidates.npz',candidates=final,
                    covariance=np.array([v[0]for v in normalizers]))
print(json.dumps(out,indent=2))
