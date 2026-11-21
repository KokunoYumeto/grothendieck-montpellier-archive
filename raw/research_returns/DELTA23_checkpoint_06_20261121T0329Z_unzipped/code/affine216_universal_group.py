#!/usr/bin/env python3
"""Exact relatively free two-generator image in every E0 marking.

Seed the Schreier--Sims chain by the lifted characteristic SL2(F3)
quotient. The remaining kernel consists of affine translations.
"""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
WORK=Path(__file__).resolve().parents[1];R=WORK/'agents/characters/records'
def pp(x):return Permutation(np.asarray(x).tolist())

def rref(v):
    a=np.array(v,dtype=np.int16,copy=True)%3;r=0;piv=[]
    for c in range(a.shape[1]):
        nz=np.flatnonzero(a[r:,c])
        if not len(nz):continue
        j=r+int(nz[0]);a[[r,j]]=a[[j,r]];a[r]=a[r]*int(a[r,c])%3
        for i in range(len(a)):
            if i!=r and a[i,c]:a[i]=(a[i]-a[i,c]*a[r])%3
        piv.append(c);r+=1
        if r==len(a):break
    return a[:r],piv

def main():
    start=time.monotonic();data=np.load(R/'affine216_marked_pair_kernels.npz');meta=json.loads((R/'affine216_marked_pair_kernels.json').read_text());els=data['elements']
    oldkids=list(map(int,np.load(WORK/'records/sl2_3_gentle_core.npz')['kernel_ids']))
    kids=oldkids+[k for k in range(146)if k not in oldkids];prefix=9*len(oldkids);n=9*len(kids)
    perms=np.array([[3*int((u+A*(j//3)+B*(j%3))%3)+int((v+C*(j//3)+D*(j%3))%3)for j in range(9)]for u,v,A,B,C,D in els],dtype=np.int16)
    gens=np.array([np.concatenate([9*j+perms[meta['kernels'][k]['pair'][i]]for j,k in enumerate(kids)])for i in range(2)])
    old=PermutationGroup([pp(g[:prefix])for g in gens]);old._schreier_sims();oo=int(old.order());assert oo==1179648
    memo={}
    for p,g in zip(old.generators,gens):memo[p]=g;memo[p**-1]=np.argsort(g)
    def lift(p):
        if p.is_identity:return np.arange(n)
        if p in memo:return memo[p]
        if p in old._strong_gens_slp:fac=old._strong_gens_slp[p]
        elif p**-1 in old._strong_gens_slp:return np.argsort(lift(p**-1))
        else:fac=old.generator_product(p,original=False)
        out=np.arange(n)
        for q in fac:out=out[lift(q)]
        assert np.array_equal(out[:prefix],p.array_form)
        memo[p]=out;memo[p**-1]=np.argsort(out);return out
    seeds=[pp(lift(p))for p in old.strong_gens];G=PermutationGroup(seeds)
    print({'stage':'building','degree':n,'seeds':len(seeds),'old_base':len(old.base)},flush=True)
    G._schreier_sims(base=old.base);go=int(G.order());print({'stage':'group','order':go,'kernel':go//oo},flush=True)
    assert G.base[:len(old.base)]==old.base
    (WORK/'records/affine216_universal_group_state.pkl').write_bytes(pickle.dumps([(G.args,G.__dict__),(old.args,old.__dict__)]))
    vectors=[];ks=[]
    for p in G.strong_gens:
        if any(p(b)!=b for b in old.base):continue
        arr=np.array(p.array_form,dtype=np.int16);assert np.array_equal(arr[:prefix],np.arange(prefix))
        local=arr.reshape(len(kids),9)-9*np.arange(len(kids),dtype=np.int16)[:,None]
        trans=local[:,0];v=np.c_[trans//3,trans%3]
        expect=np.array([[3*((int(u)+j//3)%3)+(int(vv)+j%3)%3 for j in range(9)]for u,vv in v])
        assert np.array_equal(local,expect)
        vectors.append(v.ravel());ks.append(arr)
    basis,piv=rref(vectors);rank=len(basis);assert go==oo*3**rank
    # Lift each of the four normalized SL2 f-values to an actual same-word
    # E0 image. All these fibers lie in the derived subgroup because both
    # generator orders are12 and the quotient abelianization isC12^2.
    oldvals=np.load(WORK/'records/sl2_3_gentle_core.npz')['survivors'];lifts=[]
    for row in oldvals:
        target=np.concatenate([9*j+perms[v]for j,v in enumerate(row)])
        lifts.append(lift(pp(target)))
    np.savez_compressed(WORK/'records/affine216_universal_group.npz',kernel_ids=kids,generators=gens,
        old_kernel_ids=oldkids,translation_basis=basis,pivots=piv,normalized_f_lifts=lifts,
        strong_generators=np.array([p.array_form for p in G.strong_gens],dtype=np.int16),base=G.base)
    out={'degree':n,'marked_kernels':len(kids),'order':go,'linear_quotient_order':oo,'translation_kernel_order':go//oo,
         'translation_dimension':rank,'normalized_linear_fibers':len(lifts),'elapsed_seconds':time.monotonic()-start,
         'scope':'Exact common-word image and its elementary abelian translation kernel; no fullE0 gentle or pentagon equation has yet been imposed.'}
    (WORK/'records/affine216_universal_group.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
