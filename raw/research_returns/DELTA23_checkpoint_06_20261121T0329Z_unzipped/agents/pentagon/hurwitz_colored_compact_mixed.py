#!/usr/bin/env python3
"""Faithful mixed-orbit compression and full marked S4 test.

A discarded coordinate is always certified by an exact joined-order
equality, first against a smaller retained factor and then the whole union.
"""
from pathlib import Path
import json,pickle,sys,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent
kind=sys.argv[1];no=int(sys.argv[2]);stem=HERE/f'hurwitz_colored_{kind}_{no}_compact_mixed'
start=time.monotonic()
def group(gs):return PermutationGroup([Permutation(g.tolist())for g in gs])
def join(a,b):return b.copy()if a is None else np.array([np.r_[g,len(g)+h]for g,h in zip(a,b)])
source=np.load(HERE/f'hurwitz_colored_{kind}_orbit_{no}.npz');A,B,C=source['generators'];s=A[B[A]]
original=np.array([C[C],s[s]]);N=len(A)
parts=np.load(HERE/f'hurwitz_colored_{kind}_{no}_mixed.npz')
inventory=json.loads((HERE/f'hurwitz_colored_{kind}_{no}_mixed.json').read_text())['cases']
assert np.array_equal(np.sort(np.concatenate([parts[f"orbit_{r['mixed_orbit']}"]for r in inventory])),np.arange(N))
by_id={r['mixed_orbit']:r for r in inventory}
for row in inventory:
    k=row['mixed_orbit'];sub=parts[f'orbit_{k}'];ix=np.full(N,-1,dtype=int);ix[sub]=np.arange(len(sub))
    assert np.array_equal(ix[original[:,sub]],parts[f'pair_{k}'])
current=None;current_order=1;selected=[];history=[];current_group=None
for row in sorted(inventory,key=lambda r:(-r['order'],r['degree'],r['mixed_orbit'])):
    k=row['mixed_orbit'];gs=parts[f'pair_{k}'];factor=None;tested=[]
    for h in sorted(selected,key=lambda v:by_id[v]['degree']):
        if by_id[h]['order']%row['order']:continue
        J=group(join(parts[f'pair_{h}'],gs));jo=int(J.order());tested.append([h,jo])
        if jo==by_id[h]['order']:factor=h;break
    if factor is not None:
        kept=False;order=current_order;method={'factor_through_component':factor,'pair_checks':tested}
    else:
        candidate=join(current,gs);J=group(candidate);order=int(J.order())
        assert order%current_order==0 and order%row['order']==0
        kept=order!=current_order;method={'full_union_join':order,'pair_checks':tested}
        if kept:current,current_order,current_group=candidate,order,J;selected.append(k)
    step={'component':k,'retained':kept,'current_degree':len(current[0]),'current_order':current_order,**method}
    history.append(step);print(step,flush=True)
    out={'kind':kind,'orbit':no,'source_degree':N,'selected_components':selected,
         'current_degree':len(current[0]),'current_order':current_order,'component_tests':history,
         'elapsed_seconds':time.monotonic()-start,'status':'IN_PROGRESS'}
    stem.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
target=np.array([[1,2,0,3],[1,2,3,0]])
J=group(join(current,target));jo=int(J.order());assert jo%current_order==0
out.update({'full_mixed_order':current_order,'joined_markedS4_order':jo,
            'projection_kernel_order':jo//current_order,'retains_markedS4':jo==current_order,
            'faithful_degree':len(current[0]),'elapsed_seconds':time.monotonic()-start,'status':'PASS'})
np.savez_compressed(stem.with_suffix('.npz'),generators=current,target=target,
                    subset=np.concatenate([parts[f'orbit_{k}']for k in selected]))
stem.with_name(stem.name+'_state.pkl').write_bytes(pickle.dumps((current_group.args,current_group.__dict__)))
stem.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k!='component_tests'},indent=2),flush=True)
