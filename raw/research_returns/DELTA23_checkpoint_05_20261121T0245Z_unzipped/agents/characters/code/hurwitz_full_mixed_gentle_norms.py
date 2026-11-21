#!/usr/bin/env python3
"""Full 8064-point induced gentle norms on the exact H7 mixed-word fibers."""
from pathlib import Path
import json,pickle,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_mixed72_s3_core import induced,power
HERE=Path(__file__).resolve().parents[1];ROOT=HERE.parents[1]
PENT=HERE.parent/'pentagon';FIVE=HERE.parent/'five_level_six'

def run():
    start=time.monotonic();state=pickle.loads((FIVE/'hurwitz_full_mixed_groups_state.pkl').read_bytes())
    args,st=state[0];M=PermutationGroup(args);M.__dict__.update(st)
    A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators'];ss=A[B[A]]
    x=C[C];y=ss[ss];z=np.argsort(x[y]);n=1344;I=np.arange(n)
    assert M.order()==40122452017152
    assert np.array_equal(M.generators[0].array_form,x) and np.array_equal(M.generators[1].array_form,y)
    cache={M.generators[0]:x,M.generators[1]:z,Permutation(I.tolist()):I}
    def theta(g):
        if not isinstance(g,Permutation):g=Permutation(g.tolist())
        if g in cache:return cache[g]
        gi=g**-1
        if gi in cache:cache[g]=np.argsort(cache[gi]);return cache[g]
        if g in M._strong_gens_slp:word=M._strong_gens_slp[g]
        elif gi in M._strong_gens_slp:
            cache[g]=np.argsort(theta(gi));return cache[g]
        else:word=M.generator_product(g,original=False)
        first=I.copy();second=I.copy()
        for h in word:
            first=first[np.array(h.array_form)];second=second[theta(h)]
        assert np.array_equal(first,np.array(g.array_form))
        cache[g]=second;return second
    for g in M.strong_gens:
        tg=theta(g)
        assert M.contains(Permutation(tg.tolist()))
        assert np.array_equal(theta(tg),x[np.array(g.array_form)[np.argsort(x)]])
    print('reflection SLP verified',len(M.strong_gens),'strong generators',flush=True)
    s,r,X,Y=induced(x,y);N=6*n;II=np.arange(N);Z=np.argsort(X[Y])
    xi=np.argsort(x);yi=np.argsort(y)
    pairs=[(x,y),(y,x),(y,z),(z,x),(x,xi[z[x]]),(y[z[yi]],y)]
    for j,(u,v)in enumerate(pairs):
        assert np.array_equal(X[n*j:n*(j+1)]-n*j,u)
        assert np.array_equal(Y[n*j:n*(j+1)]-n*j,v)
    ri=np.argsort(r)
    if np.array_equal(r[X[ri]],Y) and np.array_equal(r[Y[ri]],Z):cyc=r
    else:
        assert np.array_equal(ri[X[r]],Y) and np.array_equal(ri[Y[r]],Z);cyc=ri
    cyci=np.argsort(cyc);cyc2=cyc[cyc];cyc2i=np.argsort(cyc2)
    zinv=np.argsort(Z);yinv=np.argsort(Y);xinv=np.argsort(X)
    fibers=np.load(ROOT/'records/hurwitz_solvable_fiber_filter.npz')
    es=np.load(HERE/'records/hurwitz_commonword_centralizer216.npz')['elements']
    te=np.array([theta(e)for e in es]);tr=np.array([theta(g)for g in fibers['R_witnesses']])
    rows=[];accepted=[];indices=[];partial=[]
    for row,(base,g,tg)in enumerate(zip(fibers['base_indices'],fibers['R_witnesses'],tr)):
        counts=[0,0,0];passing=[];m0_indices=[]
        for k,(e,et)in enumerate(zip(es,te)):
            a=g[e];t=tg[et];ai=np.argsort(a);ti=np.argsort(t);b=t[ai];bi=a[ti]
            blocks=[a,ai,b,ti,xi[t[x]],y[bi[yi]]]
            f=np.concatenate([n*j+v for j,v in enumerate(blocks)])
            sf=s[f]
            if not np.array_equal(sf[sf],II):continue
            counts[0]+=1;fr=np.argsort(f)[r]
            if not np.array_equal(fr[fr[fr]],II):continue
            counts[1]+=1;m0_indices.append(k)
            f_yz=cyc[f[cyci]];f_zx=cyc2[f[cyc2i]]
            neg=f_zx[zinv[f_yz[yinv[f[xinv]]]]]
            if not np.array_equal(neg,II):continue
            counts[2]+=1;passing.append(k);accepted.append(a);indices.append((int(base),k));partial.append(row)
        rows.append({'base_index':int(base),'input':216,'two_cycle':counts[0],'both_positive_cycles':counts[1],
                     'negative_three_cycle':counts[2],'passing_element_indices':passing,'positive_element_indices':m0_indices})
        print('base',base,'counts',counts,flush=True)
        (HERE/'records/hurwitz_full_mixed_gentle_norms.json').write_text(json.dumps({
            'statement':'D23.C28 probe','cases':rows,'elapsed_seconds':time.monotonic()-start,
            'scope':'Exact full induced B norm equations; joint S3 derived-image membership is not yet imposed.'},indent=2)+'\n')
    np.savez_compressed(HERE/'records/hurwitz_full_mixed_gentle_norms.npz',base_indices=fibers['base_indices'],
        passing_labels=np.array(indices),passing_R=np.array(accepted),passing_case_rows=np.array(partial),
        theta_centralizer=te,theta_representatives=tr,s=s,r=r,x=X,y=Y)
    print('passing total',len(accepted),'elapsed',time.monotonic()-start,flush=True)

if __name__=='__main__':run()
