#!/usr/bin/env python3
"""Cross-orbit ordinary-word compatibility of all last-meridian gentle shadows."""
from pathlib import Path
import itertools,json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;CHAR=HERE.parent/'characters'
def pp(g):return Permutation(g.tolist())
def run():
    start=time.monotonic()
    invt=np.load(CHAR/'records/affine216_marked_pair_kernels.npz')
    meta=json.loads((CHAR/'records/affine216_marked_pair_kernels.json').read_text())
    ex=np.load(CHAR/'records/affine216_last_gentle_extensions.npz')
    aff=np.load(HERE/'affine216_last_commonword.npz')['affine_permutations']
    iv=invt['inverse'];index={tuple(map(int,g)):i for i,g in enumerate(invt['elements'])}
    # All surviving original eight-kernel values are identity, hence have
    # the same seven extension caches. Derive them from a passing row.
    first=int(ex['passing_input_indices'][0]);caches=ex['case_orbit_cache_indices'][first]
    assert all(np.array_equal(ex['case_orbit_cache_indices'][i],caches)for i in ex['passing_input_indices'])
    blocks=[ex[f'orbit_{c}_kernels']for c in caches]
    opts=[ex[f'orbit_{c}_assignments']for c in caches]
    kids=np.concatenate(blocks);assert len(kids)==24 and len(set(kids))==24
    pairs=[meta['kernels'][k]['pair']for k in kids]
    cx,cy=meta['cubic_detector_pair'];pairs.extend([[cx,cy],[cy,cx]])
    pairs=np.array(pairs);known=index[(1,1,1,0,0,1)]
    joint=lambda vals:np.concatenate([9*k+aff[g]for k,g in enumerate(vals)])
    G=PermutationGroup([pp(joint(pairs[:,j]))for j in range(2)]);go=int(G.order())
    print('degree',G.degree,'order',go,flush=True)
    D=G.derived_subgroup();do=int(D.order());print('derived',do,flush=True)
    passed=[];tried=0
    for choices in itertools.product(*[range(len(a))for a in opts]):
        tried+=1;values=np.concatenate([a[i]for a,i in zip(opts,choices)])
        target=joint(np.r_[values,known,iv[known]])
        if D.contains(pp(target)):passed.append(values)
    out={'statement':'D23.F41 expanded E0 commonword computation','kernel_ids':list(map(int,kids)),
         'degree':G.degree,'joint_order':go,'derived_order':do,'tested':tried,'passed':len(passed),
         'elapsed_seconds':time.monotonic()-start,
         'scope':'Cross-orbit common ordinary commutator realization of all24 last-kernel gentle shadow values and both literal cubic orientations; no actual gentle lift.'}
    np.savez_compressed(HERE/'affine216_last_full_s3_commonword.npz',passed=np.array(passed),
        pairs=pairs,kernel_ids=kids,generators=np.array([g.array_form for g in G.generators]),
        derived_generators=np.array([g.array_form for g in D.generators]))
    (HERE/'affine216_last_full_s3_commonword.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
