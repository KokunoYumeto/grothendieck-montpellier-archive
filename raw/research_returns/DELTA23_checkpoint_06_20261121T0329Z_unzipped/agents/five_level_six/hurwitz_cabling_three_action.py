#!/usr/bin/env python3
"""Exact full B3 covariance extension of the prescribed raw cabling action.

This is a finite necessary-condition certificate, not a GT realization.
The full first-pair value is reconstructed from C28 and the marked raw
isomorphism, rather than chosen by an arbitrary word representative.
"""
from pathlib import Path
import json,pickle,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
PENT=HERE.parent/'pentagon';CHAR=HERE.parent/'characters'
def pp(a):return Permutation(np.asarray(a).tolist())
def power(a,n):
    if n<0:return power(np.argsort(a),-n)
    out=np.arange(len(a))
    while n:
        if n&1:out=out[a]
        a=a[a];n//=2
    return out

def run():
    start=time.monotonic()
    raw=np.load(ROOT/'records/hurwitz_product_fixed_cover.npz')
    invt=np.load(CHAR/'records/affine216_marked_pair_kernels.npz')
    mt=invt['multiplication'];iv=invt['inverse'];elements=invt['elements']
    assert np.array_equal(elements,raw['group_elements'])
    cab=np.load(HERE/'hurwitz_cabling_partition.npz')
    initial=cab['merged_tuples'];triples=[tuple(map(int,t))for t in initial]
    index={t:j for j,t in enumerate(triples)}
    def move(t,j):
        out=list(t);u,v=t[j:j+2]
        out[j]=int(mt[mt[u,v],iv[u]]);out[j+1]=u
        return tuple(out)
    for t in triples:
        for j in range(2):
            q=move(t,j)
            if q not in index:index[q]=len(triples);triples.append(q)
    ts=np.array(triples,dtype=np.int16);n=len(ts);I=np.arange(n);m=len(initial)
    A,B=[np.array([index[move(t,j)]for t in triples])for j in range(2)]
    assert np.array_equal(A[B[A]],B[A[B]])
    x=A[A];y=B[B];z=np.argsort(x[y]);Z=power(A[B],3)
    assert n==3*m
    # The three sectors keep track of the distinguished merged entry.
    trans=[I,A,B[A]];sectors=[t[:m]for t in trans]
    assert len(np.unique(np.concatenate(sectors)))==n
    assert all(np.all(g[:m]<m)for g in[x,y,Z,B])
    x0=x[:m];y0=y[:m];z0=z[:m]
    # Literal pure conjugations, with the central powers exhibited.
    Ai=np.argsort(A);BA=B[A];BAi=np.argsort(BA)
    desired=[(x,y),(x,np.argsort(x)[z[x]]),(y,y[z[np.argsort(y)]])]
    conjugation_central_powers=[]
    for T,(u,v)in zip(trans,desired):
        Ti=np.argsort(T);pair=[Ti[x[T]],Ti[y[T]]];ks=[]
        for got,want in zip(pair,[u,v]):
            match=[k for k in range(12)if np.array_equal(got,want[power(Z,k)])]
            assert match
            ks.append(match[0])
        conjugation_central_powers.append(ks)
    # The old mixed marking is (C^2,Z3), whereas the cabled first
    # pair is (Z3,C^2), up to the commuting/fiber-trivial A_old^2.
    oa,ob,oc=raw['generators'];os=oa[ob[oa]]
    ox=oc[oc];oy=os[os];oz=np.argsort(ox[oy])
    merge=cab['merge_map'];assert np.array_equal(merge[oy],x0[merge])
    assert np.array_equal(merge[ox],y0[merge])
    args,state=pickle.load(open(HERE/'hurwitz_full_mixed_groups_state.pkl','rb'))[0]
    M=PermutationGroup(args);M.__dict__.update(state)
    memo={M.generators[0]:ox,M.generators[1]:oz}
    memo.update({p**-1:np.argsort(q)for p,q in list(memo.items())})
    def theta_raw(p):
        if p.is_identity:return np.arange(8064)
        if p in memo:return memo[p]
        if p in M._strong_gens_slp:word=M._strong_gens_slp[p]
        elif p**-1 in M._strong_gens_slp:return np.argsort(theta_raw(p**-1))
        else:word=M.generator_product(p,original=False)
        out=np.arange(8064)
        for q in word:out=out[theta_raw(q)]
        memo[p]=out;memo[p**-1]=np.argsort(out)
        return out
    def descend(g):
        out=np.full(m,-1,dtype=int)
        for a,b in zip(merge,merge[g]):
            assert out[a]<0 or out[a]==b
            out[a]=b
        assert len(set(out))==m
        return out
    data=np.load(PENT/'hurwitz_raw_survivor_covariance.npz')
    rows=[];saved={'triples':ts,'generators':np.array([A,B]),'sectors':np.array(sectors),
                   'central_conjugation_powers':np.array(conjugation_central_powers)}
    for no,(ii,jj)in enumerate(cab['labels']):
        i,j=int(ii),int(jj);R=data[f'R_{i}_{j}'];rbase=R[::6]//6
        assert np.array_equal(R//6,rbase[np.arange(8064)//6])
        tr=theta_raw(pp(rbase));old_b=tr[np.argsort(R)]
        # a=f(x,y)=R^-1, t=f(x,z)=x f(old_y,old_z) x^-1.
        a=descend(np.argsort(R));t=x0[descend(old_b)[np.argsort(x0)]]
        b=t[np.argsort(a)]
        local_values=[a,np.argsort(x0)[t[x0]],y0[b[np.argsort(y0)]]]
        F=np.full(n,-1,dtype=int)
        for T,sec,val in zip(trans,sectors,local_values):F[sec]=T[val]
        assert len(set(F))==n
        # Check the full positive and negative gentle cycles in this
        # representation, including its nontrivial central twist.
        S=A[B[A]];r=A[B]
        swap=np.array_equal(S[F[np.argsort(S)]],np.argsort(F))
        F_yz=np.argsort(r)[F[r]]
        # r^-1 cyclically permutes (x,y,z) only up to central powers.
        found=False
        for cyc in[r,np.argsort(r)]:
            ci=np.argsort(cyc)
            if all(any(np.array_equal(cyc[u[ci]],v[power(Z,k)])for k in range(12))
                   for u,v in[(x,y),(y,z),(z,x)]):
                fyz=cyc[F[ci]];cyc2=cyc[cyc];fzx=cyc2[F[np.argsort(cyc2)]]
                found=True;break
        assert found
        pos=np.array_equal(fzx[fyz[F]],I)
        neg=np.array_equal(fzx[np.argsort(z)[fyz[np.argsort(y)[F[np.argsort(x)]]]]],I)
        assert swap and pos and neg
        Bnew=np.argsort(F)[B[F]]
        V=np.full(n,-1,dtype=int);V[:m]=np.argsort(cab['inverse_action'][no]);queue=list(range(m));ok=True
        for q in queue:
            for g,h in[(A,A),(B,Bnew)]:
                q2=int(g[q]);v2=int(h[V[q]])
                if V[q2]<0:V[q2]=v2;queue.append(q2)
                elif V[q2]!=v2:ok=False;break
            if not ok:break
        ok=bool(ok and np.all(V>=0)and len(set(V))==n)
        row={'label':[i,j],'full_B3_covariance_extension':ok,
             'full_first_f_two_three_negative_cycles':True}
        if ok:
            assert np.array_equal(V[A],A[V])and np.array_equal(V[B],Bnew[V])
            assert np.array_equal(V[Z],Z[V])
            saved[f'V_{i}_{j}']=V;saved[f'F_{i}_{j}']=F
        rows.append(row);print(row,flush=True)
    np.savez_compressed(HERE/'hurwitz_cabling_three_action.npz',**saved)
    out={'statement':'D23.F43 probe','degree':n,'initial_merged_degree':m,
         'conjugation_central_powers':conjugation_central_powers,'cases':rows,
         'elapsed_seconds':time.monotonic()-start,
         'scope':'Unique prescribed full B3 covariance extension from the cabled subset and exact C28 same-f values. No GT realization is asserted; the actual E0 last-meridian value table is a further constraint.'}
    (HERE/'hurwitz_cabling_three_action.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':run()
