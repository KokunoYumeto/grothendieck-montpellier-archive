#!/usr/bin/env python3
"""Independent automorphism count using literal E0 conjugations on basis vectors."""
from pathlib import Path
import itertools,json,time
import numpy as np
HERE=Path(__file__).resolve().parent;WORK=HERE.parents[1];CHAR=HERE.parent/'characters'

def run():
    start=time.monotonic();d=np.load(CHAR/'records/affine216_marked_pair_kernels.npz')
    mt,iv,els=[d[k]for k in['multiplication','inverse','elements']]
    u=np.load(WORK/'records/affine216_universal_constraints.npz')
    r=np.load(WORK/'records/affine216_recursive_raw_constraints.npz')
    auto=np.load(WORK/'records/affine216_residue_automorphisms.npz')
    base,coeff=u['all_pair_baseline_elements'],u['all_pair_coefficients']
    linear=np.flatnonzero(np.all(els[:,:2]==0,axis=1));assert len(linear)==24
    aa,bb=np.meshgrid(linear,linear,indexing='ij');a=aa.ravel();b=bb.ravel()
    shifts=np.r_[b+72,b+24];inputs=np.r_[a,a]
    assert np.all(els[shifts[:576],:2]==[1,0])and np.all(els[shifts[576:],:2]==[0,1])
    params=np.array(list(itertools.product(range(3),repeat=9)),dtype=np.int16)
    rows=[];saved={}
    for case in[0,1]:
        p=r[f'point_{case}'];N=r[f'null_{case}']
        fc=coeff[inputs,shifts]
        fv=(els[base[case,inputs,shifts],:2]+np.einsum('nij,j->ni',fc,p))%3
        cf=np.einsum('nij,jk->nik',fc,N)%3
        constantM=base[case,inputs,shifts]%24;keep=[]
        for starti in range(0,len(params),256):
            par=params[starti:starti+256]
            trans=(fv[None,:,:]+np.einsum('dij,nj->ndi',cf,par))%3
            f=(3*trans[:,:,0]+trans[:,:,1])*24+constantM[None,:]
            conjugated=mt[mt[iv[f],shifts[None,:]],f]
            v=els[conjugated,:2].reshape(len(par),2,576,2).transpose(0,2,3,1)
            determinant=(v[:,:,0,0]*v[:,:,1,1]-v[:,:,0,1]*v[:,:,1,0])%3
            keep.extend(np.all(determinant!=0,axis=1).tolist())
        passing=params[np.array(keep)];assert len(passing)==7776
        assert np.array_equal(passing,auto[f'allowed_{case}'])
        saved[f'allowed_{case}']=passing
        rows.append({'linear_case':case,'tested':len(params),'all576_translation_fibers_bijective':len(passing),
                     'exactly_matches_analytic_polynomial_filter':True})
        print(rows[-1],flush=True)
    np.savez_compressed(HERE/'affine216_automorphism_replay.npz',**saved)
    out={'statement':'independent universal E0 automorphism replay','cases':rows,'elapsed_seconds':time.monotonic()-start,
         'method':'Literal f inverse b f evaluations at both translation basis vectors, for all576 linear input pairs and every19683 parameter value. Universal word-translation linearity makes these exact fiber-bijectivity tests.',
         'scope':'Uses the already checked two affine9-dimensional raw-action fibers. Does not assert actual GT lifting.'}
    (HERE/'affine216_automorphism_replay.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
