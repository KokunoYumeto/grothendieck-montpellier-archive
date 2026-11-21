#!/usr/bin/env python3
"""Test P32's full38-kernel witnesses on the complete available pure targets."""
from pathlib import Path
import argparse,json,time
import numpy as np
WORK=Path(__file__).resolve().parents[1];CHAR=WORK/'agents/characters';PENT=WORK/'agents/pentagon'

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--linear',action='store_true');args=ap.parse_args()
    start=time.monotonic()
    data=np.load(CHAR/'records/affine216_marked_pair_kernels.npz')
    mt,iv,pk,els=[data[k]for k in ('multiplication','inverse','pair_kernel','elements')]
    one=int(np.flatnonzero(np.all(els==[0,0,1,0,0,1],axis=1))[0]);commute=mt==mt.T
    core=np.load(WORK/'records/sl2_3_gentle_core.npz' if args.linear else PENT/'hurwitz_colored_full_core.npz');kids=list(map(int,core['kernel_ids']))
    inventory=np.load(WORK/'records/affine216_pure_pentagon_inventory.npz');tuples=inventory['tuples'];kernels=inventory['kernels']
    pairpos=np.array([[2,3],[4,0],[1,2],[3,4],[0,1]])
    aa=tuples[:,pairpos[:,0]];bb=tuples[:,pairpos[:,1]]
    tested=np.all(np.isin(kernels,kids)|commute[aa,bb],axis=1)
    used=np.unique(np.stack([aa[tested].ravel(),bb[tested].ravel()],axis=1),axis=0)
    transport={}
    for a,b in used:
        if commute[a,b]:continue
        k=int(pk[a,b]);todo=[one];seen={one}
        for g in todo:
            for h in(a,b):
                q=int(mt[g,h])
                if q not in seen:seen.add(q);todo.append(q)
        fwd=np.full(216,-1,dtype=int);fwd[data[f'kernel_{k}_members']]=todo
        transport[int(a),int(b)]=fwd
    outcomes=[]
    aids=range(len(core['survivors']))if args.linear else(0,86,172)
    for aid in aids:
        vals=dict(zip(kids,core['survivors'][aid]if args.linear else core[f'values_{aid}']));ev=np.full((216,216),-1,dtype=int);ev[commute]=one
        for (a,b),fwd in transport.items():ev[a,b]=fwd[vals[int(pk[a,b])]]
        v=ev[aa[tested],bb[tested]];assert np.all(v>=0)
        product=np.full(len(v),one,dtype=int)
        for j in range(5):product=mt[product,v[:,j]]
        bad=np.flatnonzero(product!=one)
        outcomes.append({'assembly':aid,'tested':len(v),'failures':len(bad),
            'first_failure':None if not len(bad)else tuples[np.flatnonzero(tested)[bad[0]]].tolist()})
    out={'kernel_count':len(kids),'fully_tested':int(tested.sum()),'outcomes':outcomes,
         'elapsed_seconds':time.monotonic()-start,
         'scope':f'Exact pure pentagon checks on every E0 target whose noncommuting pairs belong to the known{len(kids)} kernels. Unknown kernels are not tested.'}
    stem='sl2_3_pure_pentagon'if args.linear else'affine216_pure_pentagon_fullcore'
    (WORK/'records'/f'{stem}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
