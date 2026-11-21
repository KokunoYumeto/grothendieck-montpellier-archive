#!/usr/bin/env python3
"""All E0 gentle and pure-pentagon constraints as exact F3 linear systems.

The universal common-word quotient has a90-dimensional translation kernel
over its characteristic SL2 quotient. For each of the four normalized
linear residues, all word values have fixed linear parts; every cycle or
pentagon equation is therefore affine linear in these90 parameters.
"""
from pathlib import Path
import json,time
import numpy as np
WORK=Path(__file__).resolve().parents[1];CHAR=WORK/'agents/characters/records';PENT=WORK/'agents/pentagon'

def solve(A,b):
    A=np.asarray(A,dtype=np.int16)%3;b=np.asarray(b,dtype=np.int16)%3
    n=A.shape[1];aug=np.c_[A,b];r=0;piv=[]
    for c in range(n):
        nz=np.flatnonzero(aug[r:,c])
        if not len(nz):continue
        j=r+int(nz[0]);aug[[r,j]]=aug[[j,r]];aug[r]=aug[r]*int(aug[r,c])%3
        coeff=aug[:,c].copy();coeff[r]=0;aug=(aug-coeff[:,None]*aug[r])%3
        piv.append(c);r+=1
        if r==len(aug):break
    if np.any(np.all(aug[:,:n]==0,axis=1)&(aug[:,n]!=0)):return None
    pt=np.zeros(n,dtype=np.int16);pt[piv]=aug[:r,n]
    free=[j for j in range(n)if j not in piv];basis=np.zeros((n,len(free)),dtype=np.int16)
    for j,k in enumerate(free):basis[k,j]=1;basis[piv,j]=-aug[:r,k]%3
    return pt,basis,aug[:r]

def main():
    start=time.monotonic();d=np.load(CHAR/'affine216_marked_pair_kernels.npz');meta=json.loads((CHAR/'affine216_marked_pair_kernels.json').read_text())
    mt,iv,pk,els,autos=[d[k]for k in ('multiplication','inverse','pair_kernel','elements','ambient_automorphisms')]
    index={tuple(map(int,e)):j for j,e in enumerate(els)};one=index[(0,0,1,0,0,1)];eye=np.eye(2,dtype=np.int16)
    src=np.load(WORK/'records/affine216_universal_group.npz');kids=list(map(int,src['kernel_ids']));loc={k:j for j,k in enumerate(kids)}
    K=src['translation_basis'].reshape(-1,146,2);dim=len(K);assert dim==90
    trans_index=np.array([[index[(u,v,1,0,0,1)]for v in range(3)]for u in range(3)])
    kval=trans_index[K[:,:,0],K[:,:,1]]
    perms=np.array([[3*int((u+A*(j//3)+B*(j%3))%3)+int((v+C*(j//3)+D*(j%3))%3)for j in range(9)]for u,v,A,B,C,D in els],dtype=np.int16)
    plookup={p.tobytes():j for j,p in enumerate(perms)}
    lifts=src['normalized_f_lifts'];fvalues=[]
    for lift in lifts:
        local=(lift.reshape(146,9)-9*np.arange(146)[:,None]).astype(np.int16)
        fvalues.append([plookup[p.tobytes()]for p in local])
    fvalues=np.array(fvalues,dtype=np.int16)
    base=np.full((4,216,216),-1,dtype=np.int16)
    coeff=np.zeros((216,216,2,dim),dtype=np.int16)
    for orbit in meta['orbits']:
        a,b=orbit['pair'];k=orbit['kernel'];j=loc[k];todo=[one];seen={one}
        for g in todo:
            for h in(a,b):
                q=int(mt[g,h])
                if q not in seen:seen.add(q);todo.append(q)
        fwd=np.full(216,-1,dtype=np.int16);fwd[d[f'kernel_{k}_members']]=todo
        fv=fwd[fvalues[:,j]];kv=fwd[kval[:,j]];assert min(fv)>=0 and min(kv)>=0
        assert np.all(els[kv,2:]==[1,0,0,1])
        pairs=np.stack([autos[:,a],autos[:,b]],axis=1)
        unique,where=np.unique(pairs,axis=0,return_index=True);aa,bb=unique.T;aut=autos[where]
        base[:,aa,bb]=aut[:,fv].T
        images=els[aut[:,kv]];assert np.all(images[:,:,2:]==[1,0,0,1])
        coeff[aa,bb]=images[:,:,:2].transpose(0,2,1)
    assert np.min(base)>=0
    print({'stage':'all_pair_evaluations','pairs':216**2,'parameters':dim},flush=True)
    def product(case,terms,cf=coeff,bs=None):
        # terms are ('f',a,b) or ('g',g), with equally-sized index arrays.
        n=len(terms[0][1]);p=cf.shape[-1]
        v=np.zeros((n,2),dtype=np.int16);M=np.repeat(eye[None,:,:],n,axis=0);C=np.zeros((n,2,p),dtype=np.int16)
        for term in terms:
            if term[0]=='f':
                a,b=term[1:];f=base[case,a,b];q=els[f,:2]if bs is None else bs[a,b];N=els[f,2:].reshape(n,2,2);B=cf[a,b]
            else:
                f=term[1];q=els[f,:2];N=els[f,2:].reshape(n,2,2);B=None
            v=(v+np.einsum('nij,nj->ni',M,q))%3
            if B is not None:C=(C+np.einsum('nij,njk->nik',M,B))%3
            M=np.einsum('nij,njk->nik',M,N)%3
        return v,M,C
    can=np.array([k['pair']for k in meta['kernels']],dtype=int);a,b=can.T;z=iv[mt[a,b]]
    constraints=[
        [('f',b,a),('f',a,b)],
        [('f',z,a),('f',b,z),('f',a,b)],
        [('f',z,a),('g',iv[z]),('f',b,z),('g',iv[b]),('f',a,b),('g',iv[a])]]
    anchor=np.load(PENT/'hurwitz_colored_last_commonword.npz');anchor_kids=anchor['kernel_ids'];anchor_vals=anchor['assignments'][0]
    anchor_pairs=np.array([meta['kernels'][int(k)]['pair']for k in anchor_kids]);anchor_a,anchor_b=anchor_pairs.T
    invt=np.load(WORK/'records/affine216_pure_pentagon_inventory.npz');tuples=invt['tuples'];pp=np.array([[2,3],[4,0],[1,2],[3,4],[0,1]])
    outrows=[];saved={'kernel_ids':kids,'translation_basis':K,'all_pair_coefficients':coeff,'all_pair_baseline_elements':base}
    for case in range(4):
        As=[];rhs=[];linear_ok=True
        for terms in constraints:
            v,M,C=product(case,terms)
            if not np.all(M==eye):linear_ok=False;break
            As.append(C.reshape(-1,dim));rhs.append(-v.ravel()%3)
        if linear_ok:
            f=base[case,anchor_a,anchor_b]
            linear_ok=bool(np.array_equal(els[f,2:],els[anchor_vals,2:]))
            As.append(coeff[anchor_a,anchor_b].reshape(-1,dim));rhs.append((els[anchor_vals,:2]-els[f,:2]).ravel()%3)
        sol=solve(np.concatenate(As),np.concatenate(rhs))if linear_ok else None
        row={'linear_case':case,'gentle_and_anchor_consistent':sol is not None}
        if sol is None:outrows.append(row);print(row,flush=True);continue
        point,null,rr=sol;row['gentle_dimension']=null.shape[1]
        print({'stage':'gentle',**row},flush=True)
        bs=(els[base[case],:2]+np.einsum('abij,j->abi',coeff,point))%3
        cf=np.einsum('abij,jk->abik',coeff,null)%3
        # Stream pentagons into an affine system in the surviving parameters.
        d2=null.shape[1];acc=np.empty((0,d2+1),dtype=np.int16);okay=True;processed=0
        for offset in range(0,len(tuples),2048):
            t=tuples[offset:offset+2048];terms=[('f',t[:,i],t[:,j])for i,j in pp]
            v,M,C=product(case,terms,cf=cf,bs=bs)
            if not np.all(M==eye):okay=False;row['linear_pentagon_failure_at']=offset;break
            eq=np.c_[C.reshape(-1,d2),-v.ravel()%3]
            accum=np.concatenate([acc,eq]);ps=solve(accum[:,:d2],accum[:,d2])
            processed+=len(t)
            if ps is None:okay=False;row['first_inconsistent_prefix']=processed;break
            acc=ps[2]
        row['pentagon_consistent']=okay;row['pentagons_processed']=processed
        if okay:
            p2,n2,_=solve(acc[:,:d2],acc[:,d2]);fp=(point+null@p2)%3;fn=null@n2%3
            row['final_dimension']=fn.shape[1];row['solution_count']=int(3**fn.shape[1])
            saved[f'point_{case}']=fp;saved[f'null_{case}']=fn
        outrows.append(row);print(row,flush=True)
    np.savez_compressed(WORK/'records/affine216_universal_constraints.npz',**saved)
    out={'translation_dimension':dim,'cases':outrows,'all_pure_targets':len(tuples),'elapsed_seconds':time.monotonic()-start,
         'scope':'Exact universalE0 common-word fibers, all two/three/m=-1 equations, all16 forced colored anchors, and every E0-valued pureK05 pentagon. The finite automorphism condition and larger braid quotient correlations remain additional.'}
    (WORK/'records/affine216_universal_constraints.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
