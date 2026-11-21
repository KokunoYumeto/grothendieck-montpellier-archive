#!/usr/bin/env python3
"""Exact automorphism test on all remaining universal E0 residues.

For the two surviving central SL2 patterns, the transformation of each
fixed linear-part pair is a linear map of its four translation coordinates.
It fixes the first translation. Its remaining2x2 determinant must be nonzero.
"""
from pathlib import Path
import itertools,json,time
import numpy as np
WORK=Path(__file__).resolve().parents[1];CHAR=WORK/'agents/characters/records'

def main():
    start=time.monotonic();d=np.load(CHAR/'affine216_marked_pair_kernels.npz');els=d['elements'];index={tuple(map(int,e)):j for j,e in enumerate(els)}
    u=np.load(WORK/'records/affine216_universal_constraints.npz');raw=np.load(WORK/'records/affine216_recursive_raw_constraints.npz')
    base,coeff=u['all_pair_baseline_elements'],u['all_pair_coefficients'];linear=np.flatnonzero(np.all(els[:,:2]==0,axis=1));assert len(linear)==24
    aa,bb=np.meshgrid(linear,linear,indexing='ij');a=aa.ravel();b=bb.ravel();B=els[b,2:].reshape(-1,2,2);I=np.eye(2,dtype=np.int16)
    shifted=[]
    for delta in((1,0),(0,1)):
        shifted.append(np.array([index[(*delta,*map(int,els[j,2:]))]for j in b]))
    params=np.array(list(itertools.product(range(3),repeat=9)),dtype=np.int16)
    monomials=np.c_[np.ones(len(params),dtype=np.int16),params,*[(params[:,j]*params[:,k])[:,None]for j in range(9)for k in range(j,9)]]%3
    rows=[];saved={'parameter_grid':params}
    for case in (0,1):
        pt=raw[f'point_{case}'];null=raw[f'null_{case}'];assert null.shape==(90,9)
        bs=(els[base[case],:2]+np.einsum('abij,j->abi',coeff,pt))%3;cf=np.einsum('abij,jk->abik',coeff,null)%3
        assert np.all(bs[a,b]==0)and np.all(cf[a,b]==0)
        L=els[base[case,a,b],2:].reshape(-1,2,2)
        assert np.all(np.all(L==I,axis=(1,2))|np.all(L==2*I,axis=(1,2)))
        assert all(np.array_equal(els[base[case,a,sh],2:],L.reshape(-1,4))for sh in shifted)
        K=np.stack([bs[a,sh]for sh in shifted],axis=2)
        KC=np.stack([cf[a,sh]for sh in shifted],axis=2)
        M=(I+np.einsum('nij,njk->nik',B-I,K))%3
        MC=np.einsum('nij,njkl->nikl',B-I,KC)%3
        polys=[]
        for m,c in zip(M,MC):
            co=[int(m[0,0]*m[1,1]-m[0,1]*m[1,0])%3]
            co.extend((m[0,0]*c[1,1]+c[0,0]*m[1,1]-m[0,1]*c[1,0]-c[0,1]*m[1,0])%3)
            for j in range(9):
                for k in range(j,9):
                    q=c[0,0,j]*c[1,1,k]-c[0,1,j]*c[1,0,k]
                    if j!=k:q+=c[0,0,k]*c[1,1,j]-c[0,1,k]*c[1,0,j]
                    co.append(int(q)%3)
            co=np.array(co,dtype=np.int16);nz=np.flatnonzero(co)
            if len(nz):co=co*int(co[nz[0]])%3
            polys.append(co)
        unique=np.unique(polys,axis=0);keep=np.ones(len(params),dtype=bool)
        for p in unique:keep &= (monomials@p)%3!=0
        saved[f'polynomials_{case}']=unique;saved[f'allowed_{case}']=params[keep]
        rows.append({'linear_case':case,'input_residues':len(params),'distinct_nonzero_determinant_conditions':len(unique),'automorphism_residues':int(keep.sum()),'first_parameters':params[keep][:1].tolist()})
        print(rows[-1],flush=True)
    np.savez_compressed(WORK/'records/affine216_residue_automorphisms.npz',**saved)
    out={'linear_part_pairs':576,'cases':rows,'elapsed_seconds':time.monotonic()-start,
         'scope':'Exact bijectivity of precomposition on all46656 E0-valued free pairs, equivalently automorphisms of the universalE0 quotient. Finite automorphism residues are not actual GT elements.'}
    (WORK/'records/affine216_residue_automorphisms.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
