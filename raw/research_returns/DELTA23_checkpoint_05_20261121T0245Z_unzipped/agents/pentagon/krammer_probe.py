#!/usr/bin/env python3
"""Exact finite Krammer probes, DELTA23. Formula: Bigelow math/0204057 §4.2."""
import itertools,json,pathlib,time
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup

def matrices(n,q,t,p=3):
    pairs=list(itertools.combinations(range(1,n+1),2)); idx={v:j for j,v in enumerate(pairs)}
    out=[]
    for i in range(1,n):
        a=np.zeros((len(pairs),len(pairs)),dtype=np.int64)
        for col,(j,k) in enumerate(pairs):
            def term(u,v,c):a[idx[u,v],col]+=c
            if i not in (j-1,j,k-1,k):term(j,k,1)
            elif i==j-1:
                term(i,k,q);term(i,j,q*q-q);term(j,k,1-q)
            elif i==j and i!=k-1:term(j+1,k,1)
            elif i==k-1 and i!=j:
                term(j,i,q);term(j,k,1-q);term(i,k,(1-q)*q*t)
            elif i==k:term(j,k+1,1)
            elif i==j and i==k-1:term(j,k,-t*q*q)
            else:raise AssertionError((i,j,k))
        out.append(a%p)
    for i in range(n-1):
        for j in range(i+1,n-1):
            if j==i+1:assert np.array_equal(out[i]@out[j]@out[i]%p,out[j]@out[i]@out[j]%p)
            else:assert np.array_equal(out[i]@out[j]%p,out[j]@out[i]%p)
    return out

def mp(a,n,p=3):
    out=np.eye(len(a),dtype=np.int64)
    while n:
        if n&1:out=out@a%p
        a=a@a%p;n//=2
    return out

def perm_rep(gs,p=3,projective=False):
    d=len(gs[0]);vs=[]
    for v in itertools.product(range(p),repeat=d):
        if not any(v):continue
        if projective and next(x for x in v if x)!=1:continue
        vs.append(v)
    vi={v:j for j,v in enumerate(vs)};ps=[]
    for g in gs:
        row=[]
        for v in vs:
            w=tuple(int(x) for x in (g@v%p))
            if projective:
                z=pow(next(x for x in w if x),-1,p);w=tuple(x*z%p for x in w)
            row.append(vi[w])
        ps.append(Permutation(row))
    return ps

def main():
    rows=[]
    for q,t in [(1,1),(1,2),(2,1),(2,2)]:
        gs=matrices(4,q,t)
        c=gs[0]@gs[1]@gs[2]%3
        z=mp(c,4)
        ps=perm_rep(gs)
        t0=time.monotonic()
        g=PermutationGroup(ps);order=int(g.order())
        b3=PermutationGroup(ps[:2]);o3=int(b3.order())
        p3=PermutationGroup([ps[0]**2,ps[1]**2]);op3=int(p3.order())
        # Composition reversal is immaterial for these palindromic words.
        x=[ps[0]**2,ps[1]**2,ps[2]**2,(ps[0]*ps[1]*ps[0])**2,(ps[2]*ps[1]*ps[2])**2]
        pairdata=[]
        for u,v in [(0,1),(1,2),(2,3),(3,4),(4,0)]:
            pg=PermutationGroup([x[u],x[v]]);ds=pg.derived_series()
            pairdata.append({'pair':[u+1,v+1],'derived_orders':[int(z.order()) for z in ds],'second_derived_nilpotent':bool(ds[min(2,len(ds)-1)].is_nilpotent)})
        row={'q':q,'t':t,'order_B4':order,'order_B3':o3,'order_adjacent_square_pair':op3,'pairdata':pairdata,'z4_identity':bool(np.array_equal(z,np.eye(6,dtype=np.int64))),'elapsed_seconds':time.monotonic()-t0,'generators':[g.tolist() for g in gs]}
        rows.append(row);print(json.dumps(row),flush=True)
    pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':main()
