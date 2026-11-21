#!/usr/bin/env python3
"""Exhaustive same-word gentle test on every marked SL2(F3) pair."""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
WORK=Path(__file__).resolve().parents[1];R=WORK/'agents/characters/records'

def main():
    start=time.monotonic();data=np.load(R/'affine216_marked_pair_kernels.npz')
    meta=json.loads((R/'affine216_marked_pair_kernels.json').read_text())
    mt,iv,pk,els=[data[k]for k in ('multiplication','inverse','pair_kernel','elements')]
    index={tuple(map(int,e)):i for i,e in enumerate(els)};one=index[(0,0,1,0,0,1)]
    lin=np.flatnonzero(np.all(els[:,:2]==0,axis=1));kids=sorted(set(map(int,pk[np.ix_(lin,lin)].ravel())))
    loc={k:i for i,k in enumerate(kids)}
    perms=np.array([[3*int((u+A*(j//3)+B*(j%3))%3)+int((v+C*(j//3)+D*(j%3))%3)for j in range(9)]for u,v,A,B,C,D in els],dtype=np.int16)
    lookup={p.tobytes():i for i,p in enumerate(perms)}
    gs=[np.concatenate([9*j+perms[meta['kernels'][k]['pair'][i]]for j,k in enumerate(kids)])for i in range(2)]
    G=PermutationGroup([Permutation(g.tolist())for g in gs]);order=int(G.order());D=G.derived_subgroup();do=int(D.order())
    assert order==1179648 and do==8192
    print({'stage':'group','order':order,'derived':do,'kernels':len(kids)},flush=True)
    vals=[]
    for p in D.generate_schreier_sims():
        q=np.array(p.array_form,dtype=np.int16).reshape(len(kids),9)-9*np.arange(len(kids),dtype=np.int16)[:,None]
        vals.append([lookup[v.tobytes()]for v in q])
    vals=np.array(vals,dtype=np.int16);assert len(vals)==8192
    def mapping(a,b):
        k=int(pk[a,b]);todo=[one];seen={one}
        for g in todo:
            for h in(a,b):
                q=int(mt[g,h])
                if q not in seen:seen.add(q);todo.append(q)
        fwd=np.full(216,-1,dtype=int);fwd[data[f'kernel_{k}_members']]=todo
        return loc[k],fwd
    keep=np.ones(len(vals),dtype=bool);stages=[]
    for which in ('duality','positive_cycle','negative_cycle'):
        for k in kids:
            a,b=meta['kernels'][k]['pair'];z=int(iv[mt[a,b]])
            def ev(x,y):
                j,t=mapping(x,y);out=t[vals[:,j]];assert np.all(out>=0);return out
            f=vals[:,loc[k]]
            if which=='duality':good=mt[ev(b,a),f]==one
            elif which=='positive_cycle':good=mt[mt[ev(z,a),ev(b,z)],f]==one
            else:
                q=ev(z,a)
                for v in (iv[z],ev(b,z),iv[b],f,iv[a]):q=mt[q,v]
                good=q==one
            keep &= good
        stages.append({'constraint':which,'remaining':int(keep.sum())})
    cubic=data['cubic_pair'];xx=els[cubic[0]].copy();yy=els[cubic[1]].copy();xx[:2]=0;yy[:2]=0
    a,b=index[tuple(xx)],index[tuple(yy)];j,fwd=mapping(a,b);keep &= fwd[vals[:,j]]==one
    stages.append({'constraint':'normalized_cubic_linear_value_identity','kernel':kids[j],'remaining':int(keep.sum())})
    for k in (37,41):
        if k in loc:
            keep &= vals[:,loc[k]]==one
            stages.append({'constraint':f'known_kernel_{k}_identity','remaining':int(keep.sum())})
    survivors=vals[keep]
    # Canonical case labels, independent of stabilizer-chain enumeration.
    S=np.array([[0,1],[2,0]],dtype=np.int16)
    powers=[np.linalg.matrix_power(S,j)%3 for j in range(4)]
    theta=[next(j for j,M in enumerate(powers)if np.array_equal(els[v[loc[1]],2:].reshape(2,2),M))for v in survivors]
    assert sorted(theta)==[0,1,2,3]
    desired=[0,2,1,3];survivors=survivors[[theta.index(j)for j in desired]]
    out={'group_order':order,'derived_order':do,'kernel_ids':kids,'stages':stages,
         'survivors':len(survivors),'theta_labels':desired,'all_values_identity':bool(np.all(survivors==one)),
         'elapsed_seconds':time.monotonic()-start,
         'scope':'Every ordinary derived word image in the characteristic SL2(F3) quotient, filtered by all actual necessary gentle equations and displayed normalized values. No profinite lift asserted.'}
    np.savez_compressed(WORK/'records/sl2_3_gentle_core.npz',kernel_ids=kids,survivors=survivors,all_derived_values=vals)
    (WORK/'records/sl2_3_gentle_core.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
