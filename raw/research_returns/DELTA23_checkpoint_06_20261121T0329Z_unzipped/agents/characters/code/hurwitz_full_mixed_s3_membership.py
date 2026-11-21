#!/usr/bin/env python3
"""Full cyclic-three common-word membership for the surviving raw pentagon pairs."""
from pathlib import Path
import pickle,time,json,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from hurwitz_mixed_reflection_map import Reflection
HERE=Path(__file__).resolve().parents[1];ROOT=HERE.parents[1];PENT=HERE.parent/'pentagon'

def run():
    start=time.monotonic();data=np.load(HERE/'records/hurwitz_full_mixed_s3_compact.npz')
    sub=data['subset'];n=len(sub);ix=np.full(1344,-1,dtype=int);ix[sub]=np.arange(n)
    args,st=pickle.loads((HERE/'records/hurwitz_full_mixed_s3_compact_group_state.pkl').read_bytes())
    G=PermutationGroup(args);G.__dict__.update(st);theta=Reflection()
    # By the cyclic-coordinate abelianization proof, a triple in (M')^3
    # is in G' iff it is in G. These three values are in M' by construction.
    raw=np.load(PENT/'hurwitz_raw_pentagon45.npz');base=np.load(ROOT/'records/hurwitz_pentagon45_fibers.npz')
    passed=[];rows=[];targets=[]
    for no,(i,j)in enumerate(raw['labels']):
        if not np.array_equal(raw['pentagon_defects'][no],np.arange(8064)):continue
        a=base[f'R_{i}'][j];t=theta(a);b=t[np.argsort(a)];c=np.argsort(t)
        theta_b=theta.x[a[np.argsort(theta.x)]][np.argsort(t)]
        assert np.array_equal(theta.z[theta_b[np.argsort(theta.z)]],np.argsort(b))
        val=np.concatenate([ix[a[sub]],n+ix[b[sub]],2*n+ix[c[sub]]])
        member=bool(G.contains(Permutation(val.tolist())))
        rows.append({'base_index':int(i),'fiber_index':int(j),'S3_derived_member':member,
                     'third_reflection_graph_consistent':True})
        print(rows[-1],flush=True)
        if member:passed.append((int(i),int(j)));targets.append(val)
    out={'statement':'D23.C28 probe','compact_M_degree':n,'core_order':int(G.order()),'core_derived_order':int(G.order())//144,
        'tested_count':len(rows),'passing_count':len(passed),'cases':rows,'elapsed_seconds':time.monotonic()-start,
        'scope':'Exact full mixed S3 common-word derived membership for raw45 survivors. Profinite lifting and further source constraints remain separate.'}
    (HERE/'records/hurwitz_full_mixed_s3_membership.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'records/hurwitz_full_mixed_s3_membership.npz',passing_labels=np.array(passed),passing_tuples=np.array(targets))
    print(json.dumps(out,indent=2))

if __name__=='__main__':run()
