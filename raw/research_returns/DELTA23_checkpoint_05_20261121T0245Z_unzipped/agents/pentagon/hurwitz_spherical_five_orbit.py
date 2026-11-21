#!/usr/bin/env python3
"""Glue the1344 and5376 sectors into the spherical6720-point Nielsen orbit."""
from pathlib import Path
import itertools,json,time,os
import numpy as np
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]

def run():
    start=time.monotonic()
    els=[tuple(map(int,a))for a in np.load(ROOT/'records/hurwitz_product_fixed_cover.npz')['group_elements']]
    ix={a:i for i,a in enumerate(els)};one=ix[(0,0,1,0,0,1)]
    def multiply(a,b):
        u,v,A,B,C,D=a;x,y,E,F,G,H=b
        return((u+A*x+B*y)%3,(v+C*x+D*y)%3,(A*E+B*G)%3,(A*F+B*H)%3,(C*E+D*G)%3,(C*F+D*H)%3)
    mt=np.array([[ix[multiply(a,b)]for b in els]for a in els],dtype=np.int16)
    iv=np.array([next(j for j in range(216)if mt[i,j]==one)for i in range(216)],dtype=np.int16)
    conj=np.array([[mt[mt[g,a],iv[g]]for a in range(216)]for g in range(216)],dtype=np.int16)
    seed=ix[(0,0,2,1,0,2)];plus=sorted(set(map(int,conj[:,seed])));minus=sorted(set(map(int,conj[:,iv[seed]])))
    type_of={a:t for t,c in enumerate([plus,minus])for a in c}
    centers=[];trans=[]
    for c in[plus,minus]:
        centers.append(np.where(conj[:,c[0]]==c[0])[0]);trans.append({a:int(np.where(conj[:,a]==c[0])[0][0])for a in c})
    def canonical(t):
        typ=type_of[int(t[0])];g=trans[typ][int(t[0])];u=conj[g,t]
        return min(tuple(map(int,row))for row in conj[centers[typ][:,None],u[None,:]])
    original=np.load(HERE/'hurwitz_cubic216_four_13.npz')
    colored=np.load(HERE/'hurwitz_colored_inverse_orbit_12.npz')
    tuples=[]
    for data in[original,colored]:
        for row in data['tuple_elements']:
            t=[ix[tuple(map(int,a))]for a in row];prod=one
            for a in t:prod=int(mt[prod,a])
            t.append(int(iv[prod]));canon=canonical(np.array(t))
            assert canon==tuple(t)
            assert sum(type_of[g]for g in t)==1
            tuples.append(t)
    tuples=np.array(tuples,dtype=np.int16);index={tuple(map(int,t)):i for i,t in enumerate(tuples)}
    assert len(index)==len(tuples)==6720
    colors=np.array([next(j for j,g in enumerate(t)if type_of[int(g)]==1)for t in tuples])
    assert np.all(colors[:1344]==4) and all(np.sum(colors==j)==1344 for j in range(5))
    gs=[]
    for j in range(4):
        moved=tuples.copy();u=tuples[:,j];v=tuples[:,j+1]
        moved[:,j]=mt[mt[u,v],iv[u]];moved[:,j+1]=u
        p=np.array([index[canonical(t)]for t in moved]);assert len(set(p))==6720;gs.append(p)
    A,B,C,D=gs;I=np.arange(6720)
    for j in range(3):assert np.array_equal(gs[j][gs[j+1][gs[j]]],gs[j+1][gs[j][gs[j+1]]])
    for j in range(4):
        for k in range(j+2,4):assert np.array_equal(gs[j][gs[k]],gs[k][gs[j]])
    delta=A[B[C[D]]];twist=I.copy()
    for k in range(5):twist=delta[twist]
    assert np.array_equal(twist,I)
    assert np.array_equal(A[B[C[D[D[C[B[A]]]]]]],I)
    assert all(np.array_equal(g[:1344],q)for g,q in zip(gs[:3],original['generators']))
    assert all(np.array_equal(g[1344:]-1344,q)for g,q in zip(gs[:3],colored['generators']))
    s=A[B[A]];t=C[B[C]];X=np.array([A[A],B[B],C[C],s[s],t[t]])
    assert np.array_equal(X[3],D[D])
    reverse=D[C[B[A]]];rho=reverse[reverse];ri=np.argsort(rho)
    rotations=[]
    for x in X:
        z=rho[x[ri]];matches=[j for j,y in enumerate(X)if np.array_equal(z,y)]
        assert len(matches)==1;rotations.append(matches[0])
    assert rotations==[3,4,0,1,2]
    q=I.copy()
    for j in range(5):q=rho[q]
    assert np.array_equal(q,I)
    sectors=[np.arange(1344)]
    for j in range(1,5):sectors.append(rho[sectors[-1]])
    assert len(set(np.concatenate(sectors)))==6720
    # The projection to the five color positions is the literal S5 action.
    color_gens=[]
    for p in gs:
        cg=[]
        for j in range(5):
            values=set(map(int,colors[p[colors==j]]));assert len(values)==1;cg.append(values.pop())
        color_gens.append(cg)
    pure=[];pure_labels=[]
    for i in range(4):
        for j in range(i+1,5):
            h=I.copy()
            for k in range(j-1,i,-1):h=h[gs[k]]
            p=h[gs[i][gs[i][np.argsort(h)]]]
            assert np.array_equal(colors[p],colors)
            pure.append(p);pure_labels.append([i+1,j+1])
    old_block=np.load(HERE/'hurwitz_cubic216_four_13_block0.npz')['block_map']
    block60=np.full(6720,-1,dtype=int)
    for k,sector in enumerate(sectors):block60[sector]=12*k+old_block
    block_gens=[]
    for p in gs:
        q=[]
        for j in range(60):
            values=set(map(int,block60[p[block60==j]]));assert len(values)==1;q.append(values.pop())
        block_gens.append(q)
    out={'degree':6720,'sector_degrees':[1344]*5,'color_generators':color_gens,
         'all_Artin_relations':True,'spherical_relation':True,'full_twist_identity':True,
         'original1344_literal_restriction':True,'colored5376_literal_restriction':True,
         'rho_word':'(sigma4 sigma3 sigma2 sigma1)^2','rho_order':5,
         'rho_twist_permutation_zero_based':rotations,'elapsed_seconds':time.monotonic()-start,
         'scope':'Literal finite full five-puncture action; no pure order-five frame result yet.'}
    temporary=HERE/f'hurwitz_spherical_five_orbit.{os.getpid()}.tmp.npz'
    np.savez_compressed(temporary,generators=gs,tuples=tuples,
        group_elements=els,colors=colors,X=X,rho=rho,rho_sectors=sectors,
        pure_generators=pure,pure_labels=pure_labels,block_map=block60,block_generators=block_gens)
    temporary.replace(HERE/'hurwitz_spherical_five_orbit.npz')
    (HERE/'hurwitz_spherical_five_orbit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':run()
