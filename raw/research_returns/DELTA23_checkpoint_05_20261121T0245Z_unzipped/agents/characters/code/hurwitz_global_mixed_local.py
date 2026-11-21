#!/usr/bin/env python3
"""Test exact necessary local mixed-pair conjugacy for finite global candidates."""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_mixed72_partial import orbits

HERE=Path(__file__).resolve().parents[1];PENT=HERE.parent/'pentagon'

def cls_targets(gens,x,targets,limit=200000):
    gs=[np.array(g.array_form,dtype=int)for g in gens]
    gi=[np.argsort(g)for g in gs]
    key=lambda a:a.astype(np.int16).tobytes()
    remaining=set(targets); found={}
    todo=[x];seen={key(x)};witness=[np.arange(len(x))]
    for k,a in enumerate(todo):
        ka=key(a)
        if ka in remaining:
            remaining.remove(ka);found[ka]=witness[k]
            if not remaining:return found,len(todo),False
        for g,ig in zip(gs,gi):
            b=g[a[ig]];kb=key(b)
            if kb not in seen:
                seen.add(kb);todo.append(b);witness.append(g[witness[k]])
                if len(todo)>limit:return found,len(todo),True
    return found,len(todo),False

def run():
    start=time.monotonic();raw=np.load(PENT/'hurwitz_cubic216_four_13.npz')
    A,B,C=raw['generators'];s=A[B[A]];pair=[C[C],s[s]];oo=orbits(pair)
    vs=np.load(PENT/'hurwitz_global_conjugators.npz')['mixed72_V_1']
    rows=[];records={};survive=set(range(len(vs)))
    for comp in[3,8,11,12,13,14,15,1,2,4,5,6,7]:
        orb=oo[comp];n=len(orb);ix={int(v):i for i,v in enumerate(orb)}
        gs=np.array([[ix[int(g[v])]for v in orb]for g in pair]);x,y=gs
        H=PermutationGroup([Permutation(g.tolist())for g in gs]);D=H.derived_subgroup()
        print('component',comp,'degree',n,'orders',H.order(),D.order(),flush=True)
        locals=np.array([[ix[int(v[w])]for w in orb]for v in vs])
        tar=np.array([v[x[np.argsort(v)]]for v in locals]);keys=[a.astype(np.int16).tobytes()for a in tar]
        normal=[i for i,v in enumerate(locals)if H.contains(Permutation(tar[i].tolist())) and np.array_equal(v[y],y[v])]
        found,visited,truncated=cls_targets(D.generators,x,set(keys))
        good=[i for i,k in enumerate(keys)if k in found]
        # A partial orbit search cannot reject an as-yet unseen target.
        survive.intersection_update(normal)
        if not truncated: survive.intersection_update(good)
        print('component',comp,'unique targets',len(set(keys)),'normal',len(normal),'conjugacy',len(good),'visited',visited,'truncated',truncated,'survive',len(survive),flush=True)
        rows.append({'component':comp,'degree':n,'group_order':int(H.order()),'derived_order':int(D.order()),
            'normalizer_passes':normal,'local_conjugacy_passes':good,'visited':visited,'truncated':truncated,
            'survivors_after':sorted(survive)})
        records[f'component_{comp}_orbit']=orb;records[f'component_{comp}_pair']=gs
        records[f'component_{comp}_witnesses']=np.array([found[k]for k in sorted(found)])
        records[f'component_{comp}_targets']=np.array([np.frombuffer(k,dtype=np.int16)for k in sorted(found)])
        (HERE/'records/hurwitz_global_mixed_local.json').write_text(json.dumps({'scope':'Necessary independent local conjugacy tests only; common word and full C covariance not yet imposed.','rows':rows,'survivors':sorted(survive),'elapsed_seconds':time.monotonic()-start},indent=2)+'\n')
        np.savez_compressed(HERE/'records/hurwitz_global_mixed_local.npz',**records)
    print('FINAL',sorted(survive),flush=True)

if __name__=='__main__':run()
