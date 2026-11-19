#!/usr/bin/env python3
"""GF(2) checks for the cocycle simplicial model K(F_2,n).

Compare Z^n(Delta^k) -> Z^n(boundary Delta^k), the kth matching map.
Finite verification only; the all-degree argument is recorded in the paper.
"""
from itertools import combinations
from time import perf_counter
import json

start = perf_counter()

def rank(rows):
    piv = {}
    for r in rows:
        while r:
            i=r.bit_length()-1
            if i in piv: r ^= piv[i]
            else:
                piv[i]=r
                break
    return len(piv)

def null_basis(rows,ncols):
    piv={}
    for r in rows:
        while r:
            i=r.bit_length()-1
            if i in piv: r ^= piv[i]
            else: piv[i]=r; break
    free=[i for i in range(ncols) if i not in piv]
    basis=[]
    for f in free:
        x=1<<f
        for p in sorted(piv):
            if (piv[p]&x).bit_count()%2: x ^= 1<<p
        assert all((r&x).bit_count()%2==0 for r in rows)
        basis.append(x)
    return basis

def cocycles(k,n,boundary):
    verts=tuple(range(k+1))
    cells=list(combinations(verts,n+1)) if n<=k else []
    if boundary: cells=[c for c in cells if len(c)<k+1]
    index={c:i for i,c in enumerate(cells)}
    larger=list(combinations(verts,n+2)) if n+1<=k else []
    if boundary: larger=[c for c in larger if len(c)<k+1]
    rows=[]
    for s in larger:
        r=0
        for f in combinations(s,n+1): r ^= 1<<index[f]
        rows.append(r)
    return cells,null_basis(rows,len(cells))

rows=[]
for n in range(1,5):
    for k in range(0,8):
        full,basis=cocycles(k,n,False)
        boundary,bbasis=cocycles(k,n,True)
        fidx={c:i for i,c in enumerate(full)}
        projected=[]
        for b in basis:
            z=0
            for j,c in enumerate(boundary):
                if b & (1<<fidx[c]): z |= 1<<j
            projected.append(z)
        image_dim=rank(projected)
        target_dim=len(bbasis)
        is_surj=image_dim==target_dim
        assert is_surj==(k!=n+1)
        rows.append({"n":n,"degree_k":k,"domain_dim":len(basis),"target_dim":target_dim,"image_dim":image_dim,"surjective":is_surj})
for n in range(1,5):
    bad=[r for r in rows if r["n"]==n and not r["surjective"]]
    print("K(F2,%d): unique failed degree %d; domain/image dimension %d, target dimension %d"%(n,bad[0]["degree_k"],bad[0]["image_dim"],bad[0]["target_dim"]))
print("ALL_ROWS",json.dumps(rows,sort_keys=True))
print("COUNTS",json.dumps({"comparisons":len(rows),"n_range":[1,4],"k_range":[0,7],"runtime_seconds":round(perf_counter()-start,6)},sort_keys=True))
