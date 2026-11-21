#!/usr/bin/env python3
"""Exact extension of knownV to allfour canonical sphericalGT generator images."""
from pathlib import Path
import io,json,os
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent
def snapshot(name):
    with np.load(io.BytesIO((HERE/name).read_bytes()))as d:return{k:d[k]for k in d.files}
data=snapshot('hurwitz_spherical_five_orbit.npz');a,b,c,e=data['generators']
rho=data['rho'];ri=np.argsort(rho);I=np.arange(6720)
co=snapshot('hurwitz_order5_cochains.npz');old=snapshot('hurwitz_global_conjugators.npz')['mixed72_V_1']
with np.load(io.BytesIO((HERE.parent/'five_level_six/hurwitz_spherical_socle.npz').read_bytes()))as d:
    base=d['base'];transversals=d['transversals'];simple_generators=d['simple_generators']
local_index=np.full(6720,-1,dtype=int);local_index[base]=np.arange(112)
S=PermutationGroup([Permutation(g.tolist())for g in simple_generators]);assert S.order()==3265920
assert np.array_equal(c[b[a[a[b[c]]]]],np.argsort(e[e]))
rows=[];vs=[]
for label,F in zip(co['labels'],co['f12']):
    i,j=map(int,label);R=ri[F[rho]];bn=np.argsort(F)[b[F]];cn=R[c[np.argsort(R)]]
    new=[a,bn,cn,e]
    V=np.full(6720,-1,dtype=int);vi=np.full(6720,-1,dtype=int)
    V[:1344]=old[i];vi[old[i]]=np.arange(1344);queue=list(range(1344));good=True
    for u in queue:
        for x,y in zip(data['generators'],new):
            uu=int(x[u]);vv=int(y[V[u]])
            if V[uu]>=0:
                if V[uu]!=vv:good=False;break
            elif vi[vv]>=0:good=False;break
            else:V[uu]=vv;vi[vv]=uu;queue.append(uu)
        if not good:break
    if good:
        assert len(queue)==6720
        assert all(np.array_equal(V[x],y[V])for x,y in zip(data['generators'],new))
        for t in transversals:
            q=local_index[np.argsort(t)[V[t[base]]]]
            assert min(q)>=0 and S.contains(Permutation(q.tolist()))
    rows.append({'candidate':i,'fiber_index':j,'full_spherical_covariance':good,
                 'derived_pure_socle_membership':good})
    vs.append(V);print(rows[-1],flush=True)
temporary=HERE/f'hurwitz_full_spherical_covariance.{os.getpid()}.tmp.npz'
np.savez_compressed(temporary,labels=co['labels'],conjugators=vs)
temporary.replace(HERE/'hurwitz_full_spherical_covariance.npz')
(HERE/'hurwitz_full_spherical_covariance.json').write_text(json.dumps({'cases':rows,
    'scope':'Literal extension of oldV to all four spherical generator covariance equations and all 1080 local S memberships, hence derived-pure inner implementation by F39; no profinite realization.'},indent=2)+'\n')
