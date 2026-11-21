#!/usr/bin/env python3
"""Exact Krammer F9 probes: q=i,t=-i. Source Bigelow math/0204057 §4.2."""
import itertools,json,pathlib,time,contextlib,io
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
with contextlib.redirect_stdout(io.StringIO()):
    import affine_cubic_detector as af

def matrices(n,q,t):
    pairs=list(itertools.combinations(range(1,n+1),2));idx={v:j for j,v in enumerate(pairs)};out=[]
    for i in range(1,n):
        a=np.zeros((len(pairs),len(pairs)),dtype=np.int64)
        for col,(j,k) in enumerate(pairs):
            def term(u,v,c):a[idx[u,v],col]=af.add(int(a[idx[u,v],col]),c)
            if i not in (j-1,j,k-1,k):term(j,k,1)
            elif i==j-1:
                term(i,k,q);term(i,j,af.sub(af.mul(q,q),q));term(j,k,af.sub(1,q))
            elif i==j and i!=k-1:term(j+1,k,1)
            elif i==k-1 and i!=j:
                term(j,i,q);term(j,k,af.sub(1,q));term(i,k,af.mul(af.mul(af.sub(1,q),q),t))
            elif i==k:term(j,k+1,1)
            elif i==j and i==k-1:term(j,k,af.N[af.mul(t,af.mul(q,q))])
            else:raise AssertionError((i,j,k))
        out.append(a)
    return out

def to3(g):
    d=len(g);a=np.zeros((2*d,2*d),dtype=np.int64)
    for i in range(d):
        for j in range(d):
            x=int(g[i,j]);u=x%3;v=x//3
            a[2*i:2*i+2,2*j:2*j+2]=[[u,-v%3],[v,u]]
    return a

def mp(a,n):
    out=np.eye(len(a),dtype=np.int64)
    while n:
        if n&1:out=out@a%3
        a=a@a%3;n//=2
    return out

def orbit_perm(gs,seeds,limit=100000,projective=False):
    """Faithful if the union of seeded orbits spans the full vector space."""
    vs=[];vi={}
    def norm(w):
        w=tuple(map(int,w))
        if projective:
            a=next(x for x in w if x)
            if a==2:w=tuple(-x%3 for x in w)
        return w
    for seed in seeds:
        v=norm(seed)
        if v not in vi:vi[v]=len(vs);vs.append(v)
    cursor=0;rows=[[] for _ in gs]
    while cursor<len(vs):
        v=vs[cursor];cursor+=1
        for j,g in enumerate(gs):
            w=norm(g@v%3)
            if w not in vi:
                vi[w]=len(vs);vs.append(w)
                if len(vs)>limit:raise RuntimeError('orbit limit')
            rows[j].append(vi[w])
    return [Permutation(row) for row in rows],len(vs)

def run():
    out={}
    for n in [3,4]:
        raw=matrices(n,3,6);gs=list(map(to3,raw));d=len(gs[0]);eye=np.eye(d,dtype=np.int64)
        for i in range(n-1):
            for j in range(i+1,n-1):
                if j==i+1:assert np.array_equal(gs[i]@gs[j]@gs[i]%3,gs[j]@gs[i]@gs[j]%3)
                else:assert np.array_equal(gs[i]@gs[j]%3,gs[j]@gs[i]%3)
        prod=eye.copy()
        for g in gs:prod=prod@g%3
        z=mp(prod,n)
        assert np.array_equal(z,(1 if n==3 else 2)*eye%3)
        row={'generators_F9':[g.tolist() for g in raw],'z_scalar':1 if n==3 else 2}
        # B3 restriction has tiny vector orbits; full B4 explored separately.
        ps,degree=orbit_perm(gs[:2],eye,limit=150000)
        g3=PermutationGroup(ps);p3=PermutationGroup([x**2 for x in ps])
        row.update({'B3_orbit_degree':degree,'B3_order':int(g3.order()),'pure_pair_order':int(p3.order()),'pure_pair_derived':[int(h.order()) for h in p3.derived_series()]})
        out[f'B{n}']=row;print(json.dumps(row),flush=True)
    pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')

def pairs():
    raw=matrices(4,3,6);a,b,c=list(map(to3,raw));eye=np.eye(12,dtype=np.int64)
    xs=[mp(a,2),mp(b,2),mp(c,2),mp(a@b@a%3,2),mp(c@b@c%3,2)]
    out=[]
    for u,v in [(0,1),(2,3),(3,4)]:
        t0=time.monotonic();ps,degree=orbit_perm([xs[u],xs[v]],eye,limit=270000,projective=True)
        pg=PermutationGroup(ps);ds=pg.derived_series()
        row={'pair':[u+1,v+1],'degree_projective_F3':degree,'derived_orders':[int(g.order()) for g in ds],'second_derived_nilpotent':bool(ds[min(2,len(ds)-1)].is_nilpotent),'elapsed_seconds':time.monotonic()-t0}
        out.append(row);print(json.dumps(row),flush=True)
        pathlib.Path(__file__).with_name('krammer_f9_pairs.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':run()
