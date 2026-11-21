#!/usr/bin/env python3
"""Necessary actual-GT mixed-pair covariance with four known block maps."""
from pathlib import Path
import json, time
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup

HERE = Path(__file__).resolve().parents[1]
PENT = HERE.parent / 'pentagon'

def orbits(gs):
    seen = set(); out = []
    for a in range(len(gs[0])):
        if a in seen: continue
        todo = [a]; seen.add(a)
        for v in todo:
            for g in gs:
                w = int(g[v])
                if w not in seen: seen.add(w); todo.append(w)
        out.append(np.array(todo, dtype=int))
    return sorted(out, key=len)

def propagate(src, tgt, known):
    """Unique equivariant map forced by specified images; return None if absent."""
    n = len(src[0]); out = np.full(n, -1, dtype=int)
    inv = np.full(n, -1, dtype=int); todo = []
    for a,b in known:
        if out[a] not in [-1,b] or inv[b] not in [-1,a]: return None
        if out[a] == -1: todo.append(int(a))
        out[a] = b; inv[b] = a
    for a in todo:
        b = out[a]
        for g,h in zip(src,tgt):
            aa,bb = int(g[a]),int(h[b])
            if out[aa] not in [-1,bb] or inv[bb] not in [-1,aa]: return None
            if out[aa] == -1:
                todo.append(aa); out[aa] = bb; inv[bb] = aa
    assert np.all(out >= 0), 'Source is transitive and known set nonempty'
    return out

def run():
    start=time.monotonic()
    d=np.load(PENT/'hurwitz_cubic216_four_13.npz')
    A,B,C=d['generators']; s=A[B[A]]; global_pair=np.array([C[C],s[s]])
    oo=orbits(global_pair)
    bm=np.load(PENT/'hurwitz_cubic216_four_13_block0.npz')['block_map']
    p21=np.load(PENT/'hurwitz_first_four_block_lifts.npz'); subset=p21['subset']
    part={}
    for bit,key in [(0,'V_0_0_0'),(1,'V_1_0_2')]:
        vv=np.full(1344,-1,dtype=int);vv[subset]=subset[p21[key]];part[bit]=vv
    results=[]; saved={}
    for component in [9,10]:
        orb=oo[component]; ix={int(v):i for i,v in enumerate(orb)}
        pair=np.array([[ix[int(g[v])]for v in orb]for g in global_pair])
        assert np.array_equal(pair,np.load(PENT/f'hurwitz_cubic216_four_13_pair34_component{component}.npz')['generators'])
        x,y=pair; marked=[[1,2,0,3],[1,2,3,0]]
        joint=PermutationGroup([Permutation(g.tolist()+[72+j for j in h])for g,h in zip(pair,marked)])
        assert joint.order()==995328
        der=joint.derived_subgroup(); assert der.order()==82944
        known={bit:np.array([(i,ix[int(vv[v])])for i,v in enumerate(orb)if vv[v]>=0])for bit,vv in part.items()}
        assert np.array_equal(known[0],known[1]) and len(known[0])==24
        assert np.all(known[0][:,0]==known[0][:,1])
        kept=[]; tkept=[]; qcounts={}; total=0
        for pp in der.generate_schreier_sims():
            rr=np.array(pp.array_form,dtype=int); q=tuple((rr[72:]-72).tolist())
            qcounts[q]=qcounts.get(q,0)+1
            if q != (0,1,2,3):continue
            total+=1; r=rr[:72]; newx=r[x[np.argsort(r)]]
            t=propagate(pair,[newx,y],known[0])
            if t is not None:
                assert np.all(bm[orb[t]]==bm[orb])
                assert np.array_equal(t[x],newx[t]) and np.array_equal(t[y],y[t])
                kept.append(r);tkept.append(t)
        unique=sorted({tuple(t)for t in tkept})
        print('component',component,'marked identity',total,'covariance',len(kept),'unique V',len(unique),flush=True)
        saved[f'component_{component}_orbit']=orb
        saved[f'component_{component}_pair']=pair
        saved[f'component_{component}_known']=known[0]
        saved[f'component_{component}_R']=np.array(kept)
        saved[f'component_{component}_V']=np.array(tkept)
        saved[f'component_{component}_unique_V']=np.array(unique)
        results.append({'component':component,'degree':72,'block_counts':{str(int(b)):int(np.sum(bm[orb]==b))for b in np.unique(bm[orb])},
            'known_points':24,'known_map_identity_for_both_cubic_states':True,
            'derived_order':82944,'marked_S4_identity_candidates':total,
            'partial_covariance_candidates':len(kept),'unique_V':len(unique),
            'V_orders':[int(Permutation(list(t)).order())for t in unique]})
    np.savez_compressed(HERE/'records/hurwitz_mixed72_partial.npz',**saved)
    out={'statement':'D23.C25 probe','cases':results,'elapsed_seconds':time.monotonic()-start,
        'scope':'Necessary pair covariance with exact rho=0,a2=0 residue. Does not yet impose all gentle cycles or full 1344 action.','result':'PASS'}
    (HERE/'records/hurwitz_mixed72_partial.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':run()
