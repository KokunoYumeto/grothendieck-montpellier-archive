#!/usr/bin/env python3
"""Impose the exact same-f κ4 recursion on the two forced raw actions.

Input: the complete affine solution families of the universal E0 quotient.
This file is a computational probe until F44's source proof is checked.
"""
from pathlib import Path
import json,time,sys
import numpy as np
from affine216_universal_constraints import solve
WORK=Path(__file__).resolve().parents[1];CHAR=WORK/'agents/characters/records';PENT=WORK/'agents/pentagon'

def main():
    start=time.monotonic();d=np.load(CHAR/'affine216_marked_pair_kernels.npz');mt,iv,els=[d[k]for k in('multiplication','inverse','elements')]
    src=np.load(WORK/'records/affine216_universal_constraints.npz');base,coeff=src['all_pair_baseline_elements'],src['all_pair_coefficients']
    orig=np.load(WORK/'records/hurwitz_product_fixed_cover.npz');Vs=np.load(PENT/'hurwitz_raw_survivor_covariance.npz')
    assert np.array_equal(orig['group_elements'],els)
    colored=np.load(PENT/'hurwitz_colored_raw_cover.npz');lifts=np.load(PENT/'hurwitz_colored_last_gentle.npz')
    V=np.load(PENT/'hurwitz_colored_raw_last_pair.npz')['base_V'];I=np.arange(32256)
    W=6*V[I//6]+(I%6+lifts['potential_0'][I//6])%6
    sources=[('original8064',orig['tuples'],Vs['V_1_0']),('colored32256',colored['tuples'],W)]
    def product(a,b):
        v,M,C=a;w,N,B=b
        return((v+np.einsum('nij,nj->ni',M,w))%3,np.einsum('nij,njk->nik',M,N)%3,(C+np.einsum('nij,njk->nik',M,B))%3)
    def inverse(a):
        v,M,C=a;Q=np.empty_like(M);Q[:,0,0]=M[:,1,1];Q[:,0,1]=-M[:,0,1];Q[:,1,0]=-M[:,1,0];Q[:,1,1]=M[:,0,0];Q%=3
        return(-np.einsum('nij,nj->ni',Q,v)%3,Q,-np.einsum('nij,njk->nik',Q,C)%3)
    def conjugate(a,b):return product(product(a,b),inverse(a))
    rows=[];saved={}
    for case in range(4):
        if f'point_{case}'not in src.files:continue
        pt=src[f'point_{case}'];null=src[f'null_{case}'];dim=null.shape[1]
        bs=(els[base[case],:2]+np.einsum('abij,j->abi',coeff,pt))%3
        cf=np.einsum('abij,jk->abik',coeff,null)%3
        acc=np.empty((0,dim+1),dtype=np.int16);row={'linear_case':case,'initial_dimension':dim,'source_results':[]};okay=True
        for name,tuples,rawV in sources:
            n=len(tuples);target=els[tuples[np.argsort(rawV)]]
            def constant(g):return(els[g,:2],els[g,2:].reshape(n,2,2),np.zeros((n,2,dim),dtype=np.int16))
            def f(a,b):
                v=base[case,a,b]
                return(bs[a,b],els[v,2:].reshape(n,2,2),cf[a,b])
            prefix=tuples[:,0].copy();out=[constant(prefix)]
            for k in range(1,tuples.shape[1]):
                g=tuples[:,k];D=mt[prefix,g];F=f(iv[D],g);J=f(prefix,g);Fi=inverse(F);c=product(Fi,J)
                out=[conjugate(c,h)for h in out]+[conjugate(Fi,constant(g))]
                prefix=D
            value=np.stack([v for v,M,C in out],axis=1);mats=np.stack([M for v,M,C in out],axis=1);cs=np.stack([C for v,M,C in out],axis=1)
            bad=np.flatnonzero(np.any(mats.reshape(n,4,4)!=target[:,:,2:],axis=(1,2)))
            sr={'source':name,'tuples':n,'linear_part_failures':len(bad)}
            if len(bad):
                sr['first_linear_failure']=int(bad[0]);okay=False;row['source_results'].append(sr);break
            A=cs.reshape(8*n,dim);b=(target[:,:,:2]-value).ravel()%3
            combined=np.concatenate([acc,np.c_[A,b]]);sol=solve(combined[:,:dim],combined[:,dim]);sr['consistent']=sol is not None
            if sol is None:okay=False;row['source_results'].append(sr);break
            cpt,cn,acc=sol;sr['remaining_dimension']=cn.shape[1];row['source_results'].append(sr)
        row['both_forced_raw_actions_compatible']=okay
        if okay:
            fp=(pt+null@cpt)%3;fn=null@cn%3
            row['final_dimension']=fn.shape[1];row['solution_count']=int(3**fn.shape[1]);saved[f'point_{case}']=fp;saved[f'null_{case}']=fn
        rows.append(row);print(row,flush=True)
    np.savez_compressed(WORK/'records/affine216_recursive_raw_constraints.npz',**saved)
    result={'cases':rows,'elapsed_seconds':time.monotonic()-start,
        'scope':'Exact affine constraints from ψκ4=T∘V^-1 on all8064original and32256colored raw tuples, using the F44 recursion. This does not test larger braid quotient common words or construct an actual GT element.'}
    (WORK/'records/affine216_recursive_raw_constraints.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
