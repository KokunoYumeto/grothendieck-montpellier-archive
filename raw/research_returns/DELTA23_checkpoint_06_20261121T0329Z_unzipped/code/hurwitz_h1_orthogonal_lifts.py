#!/usr/bin/env python3
"""Exact local projective-similitude lifts of the canonical degree36 action.

The detector map is recovered intrinsically from minimal block systems of
the unique B3 orbits of degrees108 and324. No GT coordinate deletion is
assumed. Every projective linear lift is exhausted by its six basis images.
"""
from pathlib import Path
import contextlib, importlib.util, io, itertools, json, time
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup

ROOT=Path(__file__).resolve().parents[1]
PENT=ROOT/'agents/pentagon'; FIVE=ROOT/'agents/five_level_six'
CHAR=ROOT/'agents/characters'
spec=importlib.util.spec_from_file_location('orth112',CHAR/'code/hurwitz_orthogonal112.py')
orth=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(orth)

def partition_equal(a,b):
    forward={}; backward={}
    for x,y in zip(a,b):
        if x in forward and forward[x]!=y:return False
        if y in backward and backward[y]!=x:return False
        forward[x]=y;backward[y]=x
    return True

def partition_join(parts):
    parent=list(range(len(parts[0])))
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for part in parts:
        heads={}
        for i,v in enumerate(part):
            if v in heads:parent[find(i)]=find(heads[v])
            else:heads[v]=i
    return [find(i)for i in range(len(parent))]

def run():
    start=time.monotonic()
    d=np.load(PENT/'hurwitz_cubic216_four_13.npz'); A,B,C=d['generators']
    bs=np.load(PENT/'hurwitz_cubic216_four_13_block0.npz'); block=bs['block_map']
    trans=np.load(FIVE/'hurwitz_block_correlations.npz')['transversals']
    base=orth.base; coords=orth.coords; Q=orth.Q
    cindex={tuple(v):i for i,v in enumerate(coords)}
    detector={int(v):int(w)for v,w in zip(d['detector_subset'],d['detector_map'])}
    seen=set();orbits=[]
    for v in range(len(A)):
        if v in seen:continue
        orbit=[v];seen.add(v)
        for x in orbit:
            for g in [A,B]:
                y=int(g[x])
                if y not in seen:seen.add(y);orbit.append(y)
        orbits.append(orbit)
    assert sorted(map(len,orbits))==[4,8,8,12,80,108,160,160,240,240,324]
    canonical=[]
    for size in [108,324]:
        orbit=next(o for o in orbits if len(o)==size)
        loc={v:i for i,v in enumerate(orbit)}
        G=PermutationGroup([Permutation([loc[int(g[v])]for v in orbit])for g in [A,B]])
        systems=G.minimal_blocks(randomized=False)
        target=[detector[v]for v in orbit]
        assert len(systems)==(1 if size==108 else 4)
        joined=partition_join(systems)
        assert partition_equal(joined,target)
        canonical.append({'orbit_degree':size,'image_order':int(G.order()),
                          'minimal_system_degrees':[len(set(s))for s in systems],
                          'join_degree':len(set(joined)),'join_is_detector':True})

    h1=json.loads((ROOT/'records/hurwitz36_gt_stability.json').read_text())
    cases=[];saved={}
    for a3 in [0,1]:
        passing=[v for v in h1['candidates']if v['label']==[0,a3] and v['simultaneous_conjugators']==1]
        assert len(passing)==1
        theta=np.array(passing[0]['conjugator_example'])
        for j in range(12):
            points=trans[j][base]
            assert np.all(block[points]==j)
            labels=np.array([detector.get(int(v),-1)for v in points])
            if not np.any(labels>=0):continue
            assert sum(labels>=0)==108 and len(set(labels[labels>=0]))==36
            ids=[]
            for i in np.flatnonzero(labels>=0):
                if orth.rank(coords[ids+[int(i)]])>len(ids):ids.append(int(i))
                if len(ids)==6:break
            assert len(ids)==6
            V=coords[ids].T; Vi=orth.inverse(V); gram=V.T@Q@V%3
            choices=[]
            for k,i in enumerate(ids):
                images=np.flatnonzero(labels==theta[labels[i]])
                assert len(images)==3
                choices.append([coords[t]*s%3 for t in images for s in ([1]if k==0 else [1,2])])
            matrices=[];perms=[];signs=[];raw_count=0
            for mu in [1,2]:
                def search(columns):
                    k=len(columns)
                    if k==6:
                        yield np.array(columns).T
                        return
                    for v in choices[k]:
                        if all(int(u@Q@v%3)==int(mu*gram[t,k]%3)for t,u in enumerate(columns)):
                            yield from search(columns+[v])
                for W in search([]):
                    M=W@Vi%3
                    if orth.rank(M)!=6:continue
                    assert np.array_equal(M.T@Q@M%3,mu*Q%3)
                    raw_count+=1
                    perm=np.array([cindex[orth.proj(M@v)]for v in coords])
                    if any(labels[perm[i]]!=theta[labels[i]]for i in np.flatnonzero(labels>=0)):continue
                    assert len(set(map(int,perm)))==112
                    matrices.append(M);perms.append(perm);signs.append((orth.determinant(M),mu))
            counts={str(s):signs.count(s)for s in sorted(set(signs))}
            cases.append({'rho':0,'a3':a3,'block':j,'basis_point_indices':ids,
                          'basis_compatible_similitudes':raw_count,'full_lift_count':len(perms),
                          'determinant_multiplier_counts':counts})
            saved[f'case_{a3}_{j}_matrices']=np.array(matrices)
            saved[f'case_{a3}_{j}_permutations']=np.array(perms)
            print(cases[-1],flush=True)
    out={'statement':'D23.H3','canonical_detector_partitions':canonical,'cases':cases,
         'scope':'Exact finite lift constraints; full-GT H1 and block-normalizer hypotheses are proved separately.',
         'elapsed_seconds':time.monotonic()-start,'result':'PASS'}
    (ROOT/'records/hurwitz_h1_orthogonal_lifts.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(ROOT/'records/hurwitz_h1_orthogonal_lifts.npz',**saved)
    return out

if __name__=='__main__':run()
