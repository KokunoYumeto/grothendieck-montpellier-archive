#!/usr/bin/env python3
"""Exact H9 join with all146 E0 kernels, retaining affine fiber equations."""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_colored_word_evaluator import WordEvaluator,load_group,target_zero
from affine216_prefix_recursion_replay import solve_rows
HERE=Path(__file__).resolve().parent;WORK=HERE.parents[1];CHAR=HERE.parent/'characters'
def pp(a):return Permutation(np.asarray(a).tolist())
def row_basis(rows):
    a=np.asarray(rows,dtype=np.int16).copy()%3;r=0;piv=[]
    for c in range(a.shape[1]):
        nz=np.flatnonzero(a[r:,c])
        if not len(nz):continue
        j=r+int(nz[0]);a[[r,j]]=a[[j,r]];a[r]=a[r]*int(a[r,c])%3
        v=a[:,c].copy();v[r]=0;a=(a-v[:,None]*a[r])%3
        piv.append(c);r+=1
        if r==len(a):break
    return a[:r],piv

def run():
    start=time.monotonic();old=load_group(HERE/'hurwitz_first_full_cyclic_core_state.pkl')
    univ=np.load(WORK/'records/affine216_universal_group.npz')
    states=pickle.load(open(WORK/'records/affine216_universal_group_state.pkl','rb'))
    args,state=states[1];linear=PermutationGroup(args);linear.__dict__.update(state)
    eg=univ['generators'];n=1948+eg.shape[1];prefix=9*len(univ['old_kernel_ids']);qdeg=1948+prefix
    gens=np.array([np.r_[p.array_form,1948+e]for p,e in zip(old.generators,eg)])
    assert all(pp(g).order()==12 for g in gens)
    ev=WordEvaluator(old,gens);seeds=[]
    for p in old.strong_gens:
        q=ev.evaluate(p);assert np.array_equal(q[:1948],p.array_form);seeds.append(pp(q))
    quotient_base=list(old.base)+[1948+b for b in linear.base]
    G=PermutationGroup(seeds)
    print('building',n,'degree',len(seeds),'seeds, quotient base',len(quotient_base),flush=True)
    G._schreier_sims(base=quotient_base);go=int(G.order())
    assert G.base[:len(quotient_base)]==quotient_base
    print('group order',go,'elapsed',time.monotonic()-start,flush=True)
    pickle.dump((list(G.args),G.__dict__),open(HERE/'hurwitz_universal_affine_join_state.pkl','wb'))
    vectors=[];kernelgens=[]
    for p in G.strong_gens:
        if any(p(b)!=b for b in quotient_base):continue
        a=np.array(p.array_form);assert np.array_equal(a[:qdeg],np.arange(qdeg))
        local=(a[1948:]-1948).reshape(146,9)-9*np.arange(146)[:,None]
        v=np.c_[local[:,0]//3,local[:,0]%3]
        expected=3*((v[:,0,None]+np.arange(9)[None,:]//3)%3)+(v[:,1,None]+np.arange(9)[None,:]%3)%3
        assert np.array_equal(local,expected)
        vectors.append(v.ravel());kernelgens.append(a)
    K,piv=row_basis(vectors);rank=len(K);print('translation kernel dimension',rank,flush=True)
    # Exact quotient-lift by the initial segment of the full stabilizer
    # chain. The unexplained tail is deliberately kept arbitrary.
    def quotient_lift(target):
        h=np.r_[target,np.arange(qdeg,n)];out=np.arange(n)
        for j,b in enumerate(quotient_base):
            beta=int(h[b])
            if beta not in G.basic_transversals[j]:return None
            u=np.array(G.basic_transversals[j][beta].array_form)
            h=np.argsort(u)[h];out=out[u]
        if not np.array_equal(h[:qdeg],np.arange(qdeg)):return None
        assert np.array_equal(out[:qdeg],target)
        return out
    invt=np.load(CHAR/'records/affine216_marked_pair_kernels.npz');els=invt['elements']
    meta=json.loads((CHAR/'records/affine216_marked_pair_kernels.json').read_text())
    cs=np.array([meta['kernels'][int(k)]['pair']for k in univ['kernel_ids']]);ca,cb=cs.T
    uc=np.load(WORK/'records/affine216_universal_constraints.npz')
    raw=np.load(WORK/'records/affine216_recursive_raw_constraints.npz')
    coeff=uc['all_pair_coefficients'][ca,cb].reshape(292,90)
    base=uc['all_pair_baseline_elements'];h9target=target_zero()[:1948]
    def reduce(v):
        v=np.asarray(v,dtype=np.int16).copy()%3
        for row,c in zip(K,piv):v=(v-v[:,c,None]*row)%3
        return v
    def affine_permutations(ids):
        es=els[ids];j=np.arange(9)
        return 3*((es[:,0,None]+es[:,2,None]*(j//3)+es[:,3,None]*(j%3))%3)+(es[:,1,None]+es[:,4,None]*(j//3)+es[:,5,None]*(j%3))%3
    rows=[];saved={'generators':gens,'quotient_base':np.array(quotient_base),'kernel_basis':K,
                  'kernel_pivots':np.array(piv),'kernel_ids':univ['kernel_ids']}
    for case in[0,1]:
        qtarget=np.r_[h9target,1948+univ['normalized_f_lifts'][case,:prefix]]
        lift=quotient_lift(qtarget);row={'linear_case':case,'quotient_compatible':lift is not None}
        if lift is None:rows.append(row);print(row,flush=True);continue
        vl=(lift[1948:]-1948).reshape(146,9)-9*np.arange(146)[:,None]
        vl=np.c_[vl[:,0]//3,vl[:,0]%3].ravel()
        point=raw[f'point_{case}'];null=raw[f'null_{case}'];b0=els[base[case,ca,cb],:2].ravel()
        d0=(b0+coeff@point-vl)%3;D=coeff@null%3
        reduced=reduce(np.r_[d0[None,:],D.T]);A=reduced[1:].T;b=-reduced[0]%3
        sol,rr,_=solve_rows(A,b);row.update(raw_parameter_dimension=null.shape[1],additional_rank=rr,
            affine_intersection_nonempty=sol is not None)
        if sol is not None:
            sp,sn=sol;pt=(point+null@sp)%3;nn=null@sn%3
            row['remaining_dimension']=nn.shape[1]
            saved[f'point_{case}']=pt;saved[f'null_{case}']=nn;saved[f'quotient_lift_{case}']=lift
            # Every basis direction and one point is independently sifted
            # in the full3262 image, checking the linear coset computation.
            for parameter in[pt]+[(pt+v)%3 for v in nn.T]:
                bv=(b0+coeff@parameter)%3;ids=(3*bv.reshape(146,2)[:,0]+bv.reshape(146,2)[:,1])*24+base[case,ca,cb]%24
                perm=np.concatenate([9*j+a for j,a in enumerate(affine_permutations(ids))])
                target=np.r_[h9target,1948+perm];assert G.contains(pp(target))
            row['full_group_point_and_basis_checks']='PASS'
        rows.append(row);print(row,flush=True)
    out={'statement':'D23.F45 probe','degree':n,'group_order':go,'translation_kernel_dimension':rank,
         'joint_linear_quotient_order':go//(3**rank),'cases':rows,'elapsed_seconds':time.monotonic()-start,
         'scope':'Exact common ordinary commutator-word intersection with H9 and all146 affine kernels, after full raw source constraints. Order12 source generators and H9 C12 squared abelianization certify derived membership. Actual GT realization is not asserted.'}
    np.savez_compressed(HERE/'hurwitz_universal_affine_join.npz',**saved)
    (HERE/'hurwitz_universal_affine_join.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
