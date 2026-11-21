#!/usr/bin/env python3
"""All prescribed full-sphere f12 values and their wreath-product C5 primitives.

A computed primitive is not yet asserted to belong to the actual pure
finite braid image. That membership is the remaining order-five test.
"""
from pathlib import Path
import json,os,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];FIVE=HERE.parent/'five_level_six'
data=np.load(HERE/'hurwitz_spherical_five_orbit.npz');rho=data['rho'];ri=np.argsort(rho)
sectors=data['rho_sectors'];I=np.arange(6720);old=np.load(HERE/'hurwitz_cubic216_four_13.npz')
A,B,C=old['generators'];D=A[B[C[A[B[A]]]]];di=np.argsort(D)
first=np.load(FIVE/'hurwitz_first_pair_covariance.npz')
values=np.load(ROOT/'records/hurwitz_pentagon45_fibers.npz')
raw=json.loads((HERE/'hurwitz_raw_pentagon45.json').read_text())
labels=[];full_f=[];new_rho=[];primitives=[];rows=[]
stab=np.load(FIVE/'hurwitz_block_stabilizer.npz');base112=stab['base']
trans=np.load(FIVE/'hurwitz_block_correlations.npz')['transversals']
Hlocal=PermutationGroup([Permutation(p.tolist())for p in stab['stabilizer']])
Slocal=Hlocal.derived_subgroup();assert Slocal.order()==3265920
loc=np.full(1344,-1,dtype=int);loc[base112]=np.arange(112)
sector_inverse=[]
for sector in sectors:
    z=np.full(6720,-1,dtype=int);z[sector]=np.arange(1344);sector_inverse.append(z)
for row in raw['cases']:
    if not row['raw_pentagon']:continue
    i,j=row['candidate'],row['R_fiber_index']
    F,R,H=first[f'F_1_{i}'],values[f'R_{i}'][j],values[f'H_{i}'][j]
    edge=[F,D[np.argsort(F)[di]],R,H,D[np.argsort(R)[di]]]
    f=np.full(6720,-1,dtype=int)
    for k,sector in enumerate(sectors):f[sector]=sector[edge[(-3*k)%5]]
    assert len(set(f))==6720
    w=np.argsort(f)[rho];power=I.copy()
    for k in range(5):power=w[power]
    assert np.array_equal(power,I)
    # Solve K W = rho K with K identity on the original1344 sector.
    K=np.full(6720,-1,dtype=int);K[sectors[0]]=sectors[0]
    current=sectors[0]
    for k in range(4):
        K[w[current]]=rho[K[current]];current=w[current]
    assert len(set(K))==6720 and np.array_equal(K[w],rho[K])
    assert np.array_equal(f,rho[np.argsort(K)[ri[K]]])
    assert np.array_equal(data['colors'][K],data['colors'])
    assert np.array_equal(data['block_map'][K],data['block_map'])
    for k,sector in enumerate(sectors):
        p=sector_inverse[k][K[sector]]
        for b in range(12):
            local=loc[np.argsort(trans[b])[p[trans[b][base112]]]]
            assert Slocal.contains(Permutation(local.tolist()))
    labels.append([i,j]);full_f.append(f);new_rho.append(w);primitives.append(K)
    result={'candidate':i,'fiber_index':j,'norm5':True,'color_preserving_primitive':True,
            'all60_blocks_fixed':True,'all60_local_components_in_S':True,
            'actual_pure_image_membership':'not tested here'}
    rows.append(result);print(result,flush=True)
temporary=HERE/f'hurwitz_order5_cochains.{os.getpid()}.tmp.npz'
np.savez_compressed(temporary,labels=labels,f12=full_f,
                    new_rho=new_rho,cochains=primitives,rho=rho)
temporary.replace(HERE/'hurwitz_order5_cochains.npz')
(HERE/'hurwitz_order5_cochains.json').write_text(json.dumps({'cases':rows,'tested':len(rows),
    'scope':'Exact prescribed full6720-point values and cochains in block-preserving symmetric product; membership in actual pure image is additional.'},indent=2)+'\n')
