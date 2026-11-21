#!/usr/bin/env python3
"""Schreier kernel of the full mixed pair's signed24 action, local tests.

The full kernel is an upper bound for actual normalized commutator values.
No sufficiency or profinite lift is claimed.
"""
from pathlib import Path
import json,time,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
ROOT=Path(__file__).resolve().parents[1];PENT=ROOT/'agents/pentagon';FIVE=ROOT/'agents/five_level_six'
def pg(gs):return PermutationGroup([Permutation(g.tolist())for g in gs])
def run():
    start=time.monotonic()
    A,B,C=np.load(PENT/'hurwitz_cubic216_four_13.npz')['generators'].astype(np.int64);Z=A[B[A]];Z=Z[Z]
    sig=np.load(FIVE/'hurwitz_block_correlations.npz')['signed_generators'].astype(np.int64)
    a,b,c=sig;z=a[b[a]];z=z[z]
    gens=[C[C],Z];small=[c[c],z]
    I=np.arange(1344);J=np.arange(24);qs=[J];lifts=[I];idx={J.tobytes():0}
    for q,t in zip(qs,lifts):
        for g,s in zip(gens,small):
            qq=s[q];key=qq.tobytes()
            if key not in idx:idx[key]=len(qs);qs.append(qq);lifts.append(g[t])
    assert len(qs)==144
    kernel=[];seen=set()
    for q,t in zip(qs,lifts):
        for g,s in zip(gens,small):
            j=idx[s[q].tobytes()];v=np.argsort(lifts[j])[g[t]]
            key=v.tobytes()
            if key not in seen and not np.array_equal(v,I):seen.add(key);kernel.append(v)
    block=np.load(PENT/'hurwitz_cubic216_four_13_block0.npz')['block_map']
    trans=np.load(FIVE/'hurwitz_block_correlations.npz')['transversals'];base=np.flatnonzero(block==0)
    assert all(np.array_equal(block[g],block)for g in kernel)
    candidates=np.load(PENT/'hurwitz_global_conjugators.npz')
    result=[];saved={'full_kernel_generators':np.array(kernel)}
    for j in [0,9,11,1]:
        pts=trans[j][base];loc={int(v):i for i,v in enumerate(pts)}
        def restrict(g):return np.array([loc[int(g[v])]for v in pts])
        ks=np.array([restrict(g)for g in kernel]);K=pg(ks)
        order=int(K.order());print('block',j,'kernel local order',order,flush=True)
        saved[f'local_{j}_generators']=ks
        row={'block':j,'local_kernel_order':order}
        if np.all(block[C[pts]]==j):
            c0=restrict(C);orbit=[c0];seen={c0.tobytes()};gs=[]
            for p in K.generators:
                g=np.array(p.array_form);gs.append((g,np.argsort(g)))
            for h in orbit:
                for g,gi in gs:
                    hh=g[h[gi]];key=hh.tobytes()
                    if key not in seen:seen.add(key);orbit.append(hh)
            row['C_conjugacy_orbit_size']=len(orbit)
            for bit in [0,1]:
                surviving=[]
                for i,V in enumerate(candidates[f'mixed72_V_{bit}']):
                    v=restrict(V);target=v[c0[np.argsort(v)]]
                    if target.tobytes()in seen:surviving.append(i)
                row[f'passing_global_indices_a3_{bit}']=surviving
            print({k:(len(v)if isinstance(v,list)else v)for k,v in row.items()},flush=True)
        result.append(row)
    out={'statement':'D23.H5 probe','signed_mixed_order':144,'full_Schreier_generator_count':len(kernel),
         'local_tests':result,'elapsed_seconds':time.monotonic()-start,
         'scope':'Necessary local C conjugacy by the full mixed signed kernel; no word-lift sufficiency asserted.'}
    (ROOT/'records/hurwitz_mixed_signed_kernel.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(ROOT/'records/hurwitz_mixed_signed_kernel.npz',**saved)
if __name__=='__main__':run()
