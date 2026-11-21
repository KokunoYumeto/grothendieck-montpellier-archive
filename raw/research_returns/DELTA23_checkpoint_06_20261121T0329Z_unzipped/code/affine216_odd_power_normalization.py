#!/usr/bin/env python3
"""Actual GT odd-power consequences for the normalized θ=0 finite residues."""
from pathlib import Path
import json,time
import numpy as np
from affine216_universal_constraints import solve
from affine216_universal_group import rref
WORK=Path(__file__).resolve().parents[1];CHAR=WORK/'agents/characters/records'

def main():
    start=time.monotonic();d=np.load(CHAR/'affine216_marked_pair_kernels.npz');meta=json.loads((CHAR/'affine216_marked_pair_kernels.json').read_text());mt,iv,els=[d[k]for k in('multiplication','inverse','elements')]
    index={tuple(map(int,e)):j for j,e in enumerate(els)};trans=np.array([[index[(u,v,1,0,0,1)]for v in range(3)]for u in range(3)])
    s=np.load(WORK/'records/affine216_universal_constraints.npz');q=np.load(WORK/'records/affine216_recursive_raw_constraints.npz');au=np.load(WORK/'records/affine216_residue_automorphisms.npz')
    base,coeff=s['all_pair_baseline_elements'],s['all_pair_coefficients'];pt,null=q['point_0'],q['null_0'];params=au['allowed_0'];assert len(params)==7776
    assert np.all(els[base[0],2:]==[1,0,0,1])
    bs=(els[base[0],:2]+np.einsum('abij,j->abi',coeff,pt))%3;cf=np.einsum('abij,jk->abik',coeff,null)%3
    pairs=np.array([r['pair']for r in meta['kernels']]);a,b=pairs.T;C=cf[a,b];v0=bs[a,b]
    _,piv=rref(C.reshape(292,9).T);assert len(piv)==9;M=C.reshape(292,9)[piv]
    Mi=np.column_stack([solve(M,np.eye(9,dtype=np.int16)[:,j])[0]for j in range(9)]);assert np.array_equal(M@Mi%3,np.eye(9))
    pows=3**np.arange(9,dtype=np.int64);codes=params@pows;allowed={int(c):i for i,c in enumerate(codes)}
    def powers(thetas,stages):
        totals={k:[]for k in stages}
        for starti in range(0,len(thetas),128):
            pp=thetas[starti:starti+128];bb=np.repeat(b[None,:],len(pp),axis=0);aa=np.broadcast_to(a,bb.shape);out=np.zeros((*bb.shape,2),dtype=np.int16)
            for k in range(1,max(stages)+1):
                w=(bs[aa,bb]+np.einsum('nrjd,nd->nrj',cf[aa,bb],pp))%3
                f=trans[w[:,:,0],w[:,:,1]];out=(out+w)%3
                bb=mt[mt[iv[f],bb],f]
                if k in totals:totals[k].append(out.copy())
        return{k:np.concatenate(v)for k,v in totals.items()}
    result=powers(params,[3,9]);rows=[];saved={'allowed_parameters':params,'coordinate_pivot_rows':piv,'coordinate_inverse':Mi}
    for exponent,values in result.items():
        theta=(values.reshape(len(params),292)[:,piv]-v0.reshape(292)[piv])@Mi.T%3
        expect=(v0[None,:,:]+np.einsum('rjd,nd->nrj',C,theta))%3
        infamily=np.all(values==expect,axis=(1,2));dest=np.array([allowed.get(int(c),-1)for c in theta@pows])
        dest[~infamily]=-1
        saved[f'power_{exponent}_destination']=dest
        good=dest>=0;rows.append({'power':exponent,'inputs':len(params),'remain_in_allowed_family':int(good.sum()),'distinct_outputs':len(set(map(int,dest[good])))})
        print(rows[-1],flush=True)
    images=np.unique(saved['power_9_destination']);images=images[images>=0];p2=powers(params[images],[2,4,8]);orders=[]
    for j in range(len(images)):
        order=next((e for e in(2,4,8)if np.all(p2[e][j]==0)),None);orders.append(order)
    saved['ninth_power_image_indices']=images;saved['ninth_power_image_parameters']=params[images];saved['ninth_power_image_orders']=np.array([0 if e is None else e for e in orders])
    np.savez_compressed(WORK/'records/affine216_odd_power_normalization.npz',**saved)
    out={'cases':rows,'ninth_power_images':len(images),'ninth_power_order_counts':{str(k):orders.count(k)for k in sorted(set(orders),key=str)},
         'elapsed_seconds':time.monotonic()-start,'scope':'Exact GT composition on the complete146-kernel word tables. For actual normalized θ0 elements, an odd power must remain in the same forced raw-action family; finite residues are not asserted to lift.'}
    (WORK/'records/affine216_odd_power_normalization.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
