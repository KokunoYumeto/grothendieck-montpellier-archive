#!/usr/bin/env python3
"""Exact sixty-block local normalizer and cross-sector socle witnesses.

The huge full group is never enumerated.  Explicit words in its block kernel
have squares in S^60.  Different local orders rule out simple diagonal factors.
"""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup

HERE=Path(__file__).resolve().parent
PENT=HERE.parent/'pentagon'

def grp(gs):return PermutationGroup([Permutation(g.tolist())for g in gs])
def inv(g):return np.argsort(g)
def power(g,n):
    out=np.arange(len(g));a=g
    while n:
        if n&1:out=out[a]
        n//=2
        if n:a=a[a]
    return out
def order(g):return int(Permutation(g.tolist()).order())

def run():
    start=time.monotonic()
    d=np.load(PENT/'hurwitz_spherical_five_orbit.npz')
    gs=d['generators'];qs=d['block_generators'];bm=d['block_map'];I=np.arange(6720)
    H=grp(np.load(HERE/'hurwitz_block_stabilizer.npz')['stabilizer_compact'])
    S=H.derived_subgroup();assert H.order()==6531840 and S.order()==3265920
    assert S.derived_subgroup().order()==S.order()
    base=np.flatnonzero(bm==0);assert len(base)==112
    loc=np.full(6720,-1,dtype=int);loc[base]=np.arange(112)
    ts={0:I};words={0:[]};todo=[0]
    for b in todo:
        for j,(g,q)in enumerate(zip(gs,qs)):
            c=int(q[b])
            if c not in ts:ts[c]=g[ts[b]];words[c]=[j+1]+words[b];todo.append(c)
    assert len(todo)==60
    its={b:inv(t)for b,t in ts.items()}
    transitions=[]
    for b in range(60):
        for j,(g,q)in enumerate(zip(gs,qs)):
            c=int(q[b]);p=loc[its[c][g[ts[b][base]]]]
            assert np.all(p>=0)and H.contains(Permutation(p.tolist()))
            transitions.append(p)
    print('all240 transitions lie in H',flush=True)
    Q=grp(qs);qo=int(Q.order());orbs=sorted([sorted(o)for o in Q.stabilizer(0).orbits()],key=lambda o:(len(o),o))
    assert [len(o)for o in orbs]==[1,2,9,48]
    pureq=np.array([bm[g[np.array([np.flatnonzero(bm==b)[0]for b in range(60)])]]for g in d['pure_generators']])
    Qp=grp(pureq);qpo=int(Qp.order());assert qo==120*qpo
    assert qo==18807399383040 and qpo==156728328192
    Qold=grp(np.load(PENT/'hurwitz_cubic216_four_13_block0.npz')['generators'])
    assert int(Qold.order())==216
    for q in pureq:
        for k in range(5):
            assert Qold.contains(Permutation((q[12*k:12*k+12]-12*k).tolist()))
    print('block orders',qo,qpo,'orbit sizes',list(map(len,orbs)),flush=True)
    reps=[o[0]for o in orbs if o!=[0]]
    witnesses={};rng=np.random.default_rng(2356720)
    letters=list(gs)+[inv(g)for g in gs]
    qletters=list(qs)+[inv(g)for g in qs]
    for attempt in range(2000):
        w=np.arange(6720);q=np.arange(60)
        word=rng.integers(0,8,size=16).tolist()
        for a in word:w=w[letters[a]];q=q[qletters[a]]
        e=order(q);u=power(w,2*e)
        assert np.array_equal(bm[u],bm)
        normalized=np.array([loc[its[b][u[ts[b][base]]]]for b in range(60)])
        # Kernel coordinates lie in H, and squaring kills H/S=C2.
        assert all(S.contains(Permutation(p.tolist()))for p in normalized)
        oo=[order(normalized[b])for b in [0]+reps]
        for j,b in enumerate(reps,1):
            if b not in witnesses and oo[j]!=oo[0]:
                witnesses[b]={'word':[a+1 if a<4 else -(a-3)for a in word],
                    'block_order':e,'full_power':2*e,'pair':[0,b],
                    'local_orders':[oo[0],oo[j]],'attempt':attempt}
                print('witness',witnesses[b],flush=True)
        if len(witnesses)==3:break
    assert len(witnesses)==3
    co=np.load(PENT/'hurwitz_order5_cochains.npz')
    cochain_checks=[]
    for label,k in zip(co['labels'],co['cochains']):
        assert np.array_equal(bm[k],bm)
        locals_=[loc[its[b][k[ts[b][base]]]]for b in range(60)]
        assert all(S.contains(Permutation(p.tolist()))for p in locals_)
        cochain_checks.append([int(a)for a in label])
    assert len(cochain_checks)==18
    out={'statement':'D23.F39','block_count':60,'block_size':112,
         'local_group_order':int(H.order()),'local_simple_order':int(S.order()),
         'full_block_order':qo,'pure_block_order':qpo,
         'point_stabilizer_orbits':orbs,'transition_count':len(transitions),
         'all_transitions_in_H':True,'witnesses':list(witnesses.values()),
         'pure_blocks_embed_in_five_old_solvable_quotients':True,
         'all18_cochains_in_local_socle':cochain_checks,
         'result':'PASS','elapsed_seconds':time.monotonic()-start,
         'scope':'Exact local normalization and three cross-factor order witnesses; simple-product conclusion uses C23 simplicity and the proof in hurwitz_spherical_socle.tex.'}
    (HERE/'hurwitz_spherical_socle.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'hurwitz_spherical_socle.npz',
        transversals=np.array([ts[b]for b in range(60)]),
        local_transitions=np.array(transitions),base=base,
        simple_generators=np.array([g.array_form for g in S.generators]),
        pure_block_generators=pureq)
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':run()
