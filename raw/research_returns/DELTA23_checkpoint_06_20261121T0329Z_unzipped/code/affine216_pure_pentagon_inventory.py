#!/usr/bin/env python3
"""All E0 K(0,5) representations, modulo only first-pair AGL symmetry.

The five generators a,b,c,d,e have disjoint-index commutations
[a,c]=[b,d]=[c,e]=[d,a]=[e,b]=1 and the exact LS1997 relation.
No arbitrary five tuples are substituted for group homomorphisms.
"""
from pathlib import Path
import json,time
import numpy as np
WORK=Path(__file__).resolve().parents[1];CHAR=WORK/'agents/characters';PENT=WORK/'agents/pentagon'

def main():
    start=time.monotonic()
    data=np.load(CHAR/'records/affine216_marked_pair_kernels.npz')
    meta=json.loads((CHAR/'records/affine216_marked_pair_kernels.json').read_text())
    mt,iv,pk,els=[data[k]for k in ('multiplication','inverse','pair_kernel','elements')]
    one=int(np.flatnonzero(np.all(els==[0,0,1,0,0,1],axis=1))[0])
    commute=mt==mt.T;cent=[np.flatnonzero(commute[a])for a in range(216)]
    rows=[];counts=[]
    for row in meta['orbits']:
        a,b=row['pair'];ca,cb=cent[a],cent[b]
        cc,ee=np.meshgrid(ca,cb,indexing='ij');mask=commute[cc,ee]
        c,e=cc[mask],ee[mask]
        local=[]
        for d in np.intersect1d(ca,cb):
            q=np.full(len(c),one,dtype=int)
            for val in(e,iv[b],a,iv[c],b,iv[d],c,iv[e],d,iv[a]):q=mt[q,val]
            good=np.flatnonzero(q==one)
            if len(good):local.append(np.stack([np.full(len(good),a),np.full(len(good),b),c[good],np.full(len(good),d),e[good]],axis=1))
        arr=np.concatenate(local) if local else np.empty((0,5),dtype=int)
        rows.append(arr);counts.append({'first_pair_orbit':row['orbit'],'first_pair_kernel':row['kernel'],'number':len(arr)})
    tuples=np.concatenate(rows).astype(np.int16)
    # Source pentagon has these five ordered input pairs.
    pairpos=np.array([[2,3],[4,0],[1,2],[3,4],[0,1]])
    aa=tuples[:,pairpos[:,0]];bb=tuples[:,pairpos[:,1]]
    kernels=pk[aa,bb]
    targets=json.loads((PENT/'hurwitz_colored_last_commonword.json').read_text())['cases']
    kids=list(map(int,np.load(PENT/'hurwitz_colored_last_commonword.npz')['kernel_ids']))
    # Every commuting pair has identity value for a derived word.
    known=np.isin(kernels,kids)|commute[aa,bb]
    tested=np.all(known,axis=1)
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
    for target in targets:
        vals=dict(zip(kids,target['values']));ev=np.full((216,216),-1,dtype=int);ev[commute]=one
        for (a,b),fwd in transport.items():ev[a,b]=fwd[vals[int(pk[a,b])]]
        v=ev[aa[tested],bb[tested]];assert np.all(v>=0)
        product=np.full(len(v),one,dtype=int)
        for j in range(5):product=mt[product,v[:,j]]
        bad=np.flatnonzero(product!=one)
        outcomes.append({'assembly':target['assembly'],'tested':len(v),'failures':len(bad),'first_failure':None if not len(bad)else tuples[np.flatnonzero(tested)[bad[0]]].tolist()})
    np.savez_compressed(WORK/'records/affine216_pure_pentagon_inventory.npz',tuples=tuples,kernels=kernels,known_tested=tested)
    out={'first_pair_ambient_orbits':len(rows),'representatives':len(tuples),'known16_fully_tested':int(tested.sum()),
         'known16_outcomes':outcomes,'counts':counts,'elapsed_seconds':time.monotonic()-start,
         'scope':'Complete E0-valued K(0,5) maps modulo AGL symmetry of the first pair; only the already known16 kernel values are tested.'}
    (WORK/'records/affine216_pure_pentagon_inventory.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items()if k!='counts'},indent=2),flush=True)

if __name__=='__main__':main()
