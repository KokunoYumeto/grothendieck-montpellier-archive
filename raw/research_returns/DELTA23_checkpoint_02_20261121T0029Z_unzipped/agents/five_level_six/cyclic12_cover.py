#!/usr/bin/env python3
"""Pure braid homology of the cyclic12 sphere cover with weights9,9,10,4,4.

Exact cellular chains of the degree12 cover of a four-petal rose, followed by
filling all lifted peripheral circles. No guessed braid matrices are used.
"""
from pathlib import Path
import json,itertools
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parent
N=12
WEIGHTS=[9,9,10,4]

def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def wi(w):return tuple(-x for x in w[::-1])
def wp(w,n):return red((w if n>=0 else wi(w))*abs(n))
def sub(w,a):
    out=()
    for x in w:out=red(out+(a[x-1] if x>0 else wi(a[-x-1])))
    return out
def comp(a,b):return [sub(w,a) for w in b]
IDENTITY=[(j+1,) for j in range(4)]
def sigma(j):
    out=IDENTITY.copy()
    if j>0:
        out[j-1]=(j,j+1,-j);out[j]=(j,)
    else:
        j=-j;out[j-1]=(j+1,);out[j]=(-j-1,j,j+1)
    return out
def braid(w):
    out=IDENTITY.copy()
    for j in w:out=comp(out,sigma(j))
    return out
def shift(v,n):return np.concatenate([np.roll(v[j*N:(j+1)*N],n) for j in range(4)])
def chain(w):
    out=np.zeros(4*N,dtype=np.int64);g=0
    for j in w:
        if j>0:
            out[(j-1)*N+g]+=1;g=(g+WEIGHTS[j-1])%N
        else:
            j=-j;g=(g-WEIGHTS[j-1])%N;out[(j-1)*N+g]-=1
    return out,g
def chainmap(a):
    cols=[]
    for j,w in enumerate(a):
        v,g=chain(w);assert g==WEIGHTS[j]%N
        cols.extend(shift(v,k) for k in range(N))
    return np.array(cols,dtype=np.int64).T
def rref(A,p):
    a=A.copy()%p;row=0;pivs=[]
    for c in range(a.shape[1]):
        pivot=next((k for k in range(row,len(a)) if a[k,c]),None)
        if pivot is None:continue
        a[[row,pivot]]=a[[pivot,row]]
        a[row]=a[row]*pow(int(a[row,c]),-1,p)%p
        for k in range(len(a)):
            if k!=row and a[k,c]:a[k]=(a[k]-a[k,c]*a[row])%p
        pivs.append(c);row+=1
        if row==len(a):break
    return a,pivs
def null(A,p):
    a,pivs=rref(A,p);n=a.shape[1];free=[j for j in range(n) if j not in pivs];out=[]
    for j in free:
        v=np.zeros(n,dtype=np.int64);v[j]=1
        for r,c in enumerate(pivs):v[c]=-a[r,j]%p
        out.append(v)
    return np.array(out,dtype=np.int64).T
def inv(A,p):
    a,pivs=rref(np.concatenate([A,np.eye(len(A),dtype=np.int64)],axis=1),p)
    assert pivs[:len(A)]==list(range(len(A)))
    return a[:,len(A):]
def coordinates(B,p):
    _,rows=rref(B.T,p);rows=rows[:B.shape[1]]
    assert len(rows)==B.shape[1]
    return rows,inv(B[rows,:],p)
def restrict(T,B,p):
    rows,left=coordinates(B,p);m=left@T[rows,:]@B%p
    assert np.array_equal(T@B%p,B@m%p)
    return m
def mp(a,n,p):
    out=np.eye(len(a),dtype=np.int64)
    while n:
        if n&1:out=out@a%p
        a=a@a%p;n//=2
    return out
def orbit_perms(gs,p):
    d=len(gs[0]);vs=[];seen={};rows=[[] for _ in gs]
    for v in np.eye(d,dtype=np.int64):
        k=tuple(v)
        if k not in seen:seen[k]=len(vs);vs.append(v)
    for v in vs:
        for j,g in enumerate(gs):
            w=g@v%p;k=tuple(w)
            if k not in seen:seen[k]=len(vs);vs.append(w)
            rows[j].append(seen[k])
    return [Permutation(r) for r in rows],len(vs)

def run():
    assert braid((1,2,1))==braid((2,1,2))
    assert braid((2,3,2))==braid((3,2,3))
    assert braid((1,3))==braid((3,1))
    boundary_word=(1,2,3,4)
    assert braid((1,2,3)*4)==[red(boundary_word+(j+1,)+wi(boundary_word)) for j in range(4)]
    boundary=np.zeros((N,4*N),dtype=np.int64)
    deck=np.zeros((4*N,4*N),dtype=np.int64)
    for j,w in enumerate(WEIGHTS):
        for g in range(N):
            boundary[(g+w)%N,j*N+g]+=1;boundary[g,j*N+g]-=1
            deck[j*N+(g+1)%N,j*N+g]=1
    fills=[]
    for j,w in enumerate(WEIGHTS):
        d=int(np.gcd(w,N));v,g=chain((j+1,)*(N//d));assert g==0
        fills.extend(shift(v,k) for k in range(d))
    d=int(np.gcd(sum(WEIGHTS),N));v,g=chain((1,2,3,4)*(N//d));assert g==0
    fills.extend(shift(v,k) for k in range(d))
    fills=np.array(fills,dtype=np.int64).T
    assert np.array_equal(boundary@fills,np.zeros((N,16),dtype=np.int64))
    words=[(1,1),(2,2),(3,3),(1,2,1)*2,(3,2,3)*2]
    chainmaps=[chainmap(braid(w)) for w in words]
    fulltwist=chainmap(braid((1,2,3)*4))
    out={'branch_weights':[9,9,10,4,4],'degree':12,'genus':11,'fields':{}}
    for p in [2,3]:
        cycles=null(boundary,p)
        _,fpiv=rref(fills,p);rel=fills[:,fpiv]%p
        combined=np.concatenate([rel,cycles],axis=1)
        _,cpiv=rref(combined,p);B=combined[:,cpiv]%p
        assert cycles.shape[1]==37 and rel.shape[1]==15 and B.shape[1]==37
        rows,left=coordinates(B,p);h=B[:,15:]
        def hom(T):
            whole=left@T[rows,:]@B%p
            assert np.array_equal(T@B%p,B@whole%p)
            assert not np.any(whole[15:,:15])
            return whole[15:,15:]
        Ts=[hom(t) for t in chainmaps];D=hom(deck);Z=hom(fulltwist)
        assert np.array_equal(Z,mp(D,8,p))
        assert np.array_equal(mp(D,12,p),np.eye(22,dtype=np.int64))
        assert all(np.array_equal(T@D%p,D@T%p) for T in Ts)
        # Normalizing link12 kills the full twist. It has no effect on a
        # commutator-word evaluation because the deck action is central.
        normalized=[mp(D,4,p)@T%p if j in [0,3] else T for j,T in enumerate(Ts)]
        I=np.eye(22,dtype=np.int64)
        pol=(D@D+D+I)%p if p==2 else (D@D+I)%p
        eig=null(pol,p)
        eis=[restrict(T,eig,p) for T in normalized]
        de=restrict(D,eig,p)
        rankdim=eig.shape[1]
        erows=[]
        for j in range(5):
            gs=[eis[j],eis[(j+1)%5]]
            perms,degree=orbit_perms(gs,p)
            G=PermutationGroup(perms)
            derived=[int(g.order()) for g in G.derived_series()]
            erows.append({'pair':[j+1,(j+1)%5+1],'orbit_degree':degree,'derived_orders':derived})
        row={'compact_homology_dimension':22,'semisimple_kernel_dimension_over_Fp':rankdim,
             'deck_semisimple_matrix':de.tolist(),'semisimple_pair_data':erows,
             'semisimple_generators':[g.tolist() for g in eis]}
        socle=[{'factor':'T^2+T+1' if p==2 else 'T^2+1','dimension':rankdim,'pair_derived_orders':[r['derived_orders'] for r in erows]}]
        other_polys={'T-1':D-I}
        if p==3:other_polys['T+1']=D+I
        for name,poly in other_polys.items():
            b0=null(poly,p);g0=[restrict(T,b0,p) for T in normalized];series=[]
            for j in range(5):
                ps,_=orbit_perms([g0[j],g0[(j+1)%5]],p)
                series.append([int(h.order()) for h in PermutationGroup(ps).derived_series()])
            socle.append({'factor':name,'dimension':b0.shape[1],'pair_derived_orders':series})
        assert all(len(series)<=3 for block in socle for series in block['pair_derived_orders'])
        row['all_deck_socle_factor_data']=socle
        out['fields'][str(p)]=row
        np.savez_compressed(HERE/f'cyclic12_cover_mod{p}.npz',generators=np.array(normalized),deck=D,semisimple_basis=eig,semisimple_generators=np.array(eis),semisimple_deck=de)
        print(json.dumps({'p':p,'dimension':rankdim,'pairs':erows}),flush=True)
        (HERE/'cyclic12_cover.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS compact filling dimensions, pure braid action, central twist and deck checks',flush=True)
if __name__=='__main__':run()
