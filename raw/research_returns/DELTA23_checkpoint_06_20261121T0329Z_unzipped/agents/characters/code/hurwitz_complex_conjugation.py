#!/usr/bin/env python3
"""Actual complex-conjugation symmetry and the three surviving normal forms."""
from pathlib import Path
import json,numpy as np
from hurwitz_mixed72_partial import propagate
HERE=Path(__file__).resolve().parents[1];ROOT=HERE.parents[1];PENT=HERE.parent/'pentagon'

def run():
    data=np.load(PENT/'hurwitz_cubic216_four_13.npz');gs=data['generators']
    # The det-minus target automorphism takes inverses of the class back to it.
    elems=np.unique(data['tuple_elements'].reshape(-1,6),axis=0);assert len(elems)==36
    target=np.diag([1,2]);keys={tuple(g)for g in elems}
    for g in elems:
        v=g[:2];a=g[2:].reshape(2,2);ai=np.array([[a[1,1],-a[0,1]],[-a[1,0],a[0,0]]])%3
        image=np.r_[target@(-ai@v)%3,(target@ai@target%3).ravel()]
        assert tuple(image)in keys
    inverse=[np.argsort(g)for g in gs];ans=[]
    for image0 in range(1344):
        q=propagate(gs,inverse,[(0,image0)])
        if q is not None:ans.append(q)
    assert len(ans)==1;W=ans[0];Wi=np.argsort(W);assert np.array_equal(W[W],np.arange(1344))
    mp={int(i):int(j)for i,j in zip(data['detector_subset'],data['detector_map'])}
    w=np.array([mp[int(W[next(i for i,j in mp.items()if j==a)])]for a in range(36)])
    assert all(mp[int(W[i])]==int(w[j])for i,j in mp.items())
    tab=json.loads((ROOT/'records/hurwitz36_gt_stability.json').read_text())['candidates']
    fs={tuple(row['f']):row['label']for row in tab if row['simultaneous_conjugators']==1}
    first=[]
    for f,label in fs.items():
        moved=fs[tuple(w[np.array(f)[np.argsort(w)]])]
        assert moved==[(-label[0])%3,label[1]];first.append([label,moved])
    p=np.array([1,2,0,3]);t=np.array([1,2,3,0]);k=np.array([2,1,0,3])
    assert np.array_equal(k[p[k]],np.argsort(p))and np.array_equal(k[t[k]],np.argsort(t))
    raw=np.load(PENT/'hurwitz_raw_pentagon45.npz');fib=np.load(ROOT/'records/hurwitz_pentagon45_fibers.npz')
    vs=np.load(PENT/'hurwitz_global_conjugators.npz')['mixed72_V_1'];items=[]
    for j,(a,b)in enumerate(raw['labels']):
        if np.array_equal(raw['pentagon_defects'][j],np.arange(8064)):
            items.append((int(a),int(b),vs[a],fib[f'R_{a}'][b]))
    def key(v,a):return v.astype(np.int16).tobytes()+a.astype(np.int16).tobytes()
    lookup={key(v,a):(i,j)for i,j,v,a in items};rows=[]
    for i,j,v,a in items:
        dest=lookup[key(W[v[Wi]],W[a[Wi]])];rows.append({'source':[i,j],'target':dest})
    cube_labels={(1,0),(19,0),(23,1),(27,2)}
    cube_action={tuple(v['source']):tuple(v['target'])for v in rows if tuple(v['source'])in cube_labels}
    assert cube_action=={(1,0):(1,0),(19,0):(23,1),(23,1):(19,0),(27,2):(27,2)}
    out={'statement':'D23.C31','class_size':36,'target_det_minus_inverse_class_check':True,
         'intertwiner_count':1,'involution':True,'first36_labels':first,'candidate_action':rows,
         'three_existential_normal_forms':[(1,0),(19,0),(27,2)],'result':'PASS'}
    (HERE/'records/hurwitz_complex_conjugation_probe.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'records/hurwitz_complex_conjugation_probe.npz',intertwiners=np.array(ans),first36=w)
    print(json.dumps(out,indent=2))

if __name__=='__main__':run()
