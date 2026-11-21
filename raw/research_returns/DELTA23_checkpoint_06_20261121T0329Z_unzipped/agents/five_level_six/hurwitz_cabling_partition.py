#!/usr/bin/env python3
"""Exact raw first-strand-cabling partition and the induced nine actions."""
from pathlib import Path
import json,numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];CHAR=HERE.parent/'characters';PENT=HERE.parent/'pentagon'
def run():
    raw=np.load(ROOT/'records/hurwitz_product_fixed_cover.npz')
    d=np.load(CHAR/'records/affine216_marked_pair_kernels.npz');mt=d['multiplication'];t=raw['tuples']
    merged=np.stack([mt[t[:,0],t[:,1]],t[:,2],t[:,3]],axis=1)
    unique,labels=np.unique(merged,axis=0,return_inverse=True)
    V=np.load(PENT/'hurwitz_raw_survivor_covariance.npz');rows=[];maps=[]
    for i in [1,53,61]:
        for j in range(3):
            v=V[f'V_{i}_{j}'];vi=np.argsort(v);image=np.full(len(unique),-1)
            for a,b in zip(labels,labels[vi]):
                assert image[a]<0 or image[a]==b
                image[a]=b
            assert len(set(image))==len(unique)
            rows.append({'label':[i,j],'passes':True});maps.append(image)
    sizes,counts=np.unique(np.bincount(labels),return_counts=True)
    assert len(unique)==1214 and np.array_equal(sizes,[2,3,6,12])and np.array_equal(counts,[6,692,36,480])
    out={'statement':'D23.F42','merged_size':len(unique),'fiber_sizes':sizes.tolist(),
         'fiber_counts':counts.tolist(),'cases':rows,'result':'PASS',
         'scope':'Exact necessary cabling partition only; same-associator action on triples is additional.'}
    np.savez_compressed(HERE/'hurwitz_cabling_partition.npz',merged_tuples=unique,merge_map=labels,
        labels=np.array([r['label']for r in rows]),inverse_action=np.array(maps))
    (HERE/'hurwitz_cabling_partition.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':run()
