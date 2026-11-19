#!/usr/bin/env python3
"""Exact F2 matrices for hyperplane permutations and independent quadric swaps.
Columns are bit vectors in the exterior basis of W=<e_1,...,e_(d-1)>,
with e_0=sum e_i.  The mathematical derivation is retained in the TeX notes.
This program computes linear invariants, never infers a group classification
from its order without a proof.
"""
from itertools import combinations
from collections import deque
import json, time

def gf2_rank(rows):
    piv={}
    for v in rows:
        while v:
            j=v.bit_length()-1
            if j in piv: v ^= piv[j]
            else:
                piv[j]=v
                break
    return len(piv)

def gf2_nullspace(rows,m):
    piv={}
    for v in rows:
        while v:
            j=v.bit_length()-1
            if j in piv: v ^= piv[j]
            else:
                piv[j]=v
                break
    free=[j for j in range(m) if j not in piv]
    out=[]
    for j in free:
        v=1<<j
        for h in sorted(piv):
            if (piv[h]&v).bit_count()%2: v ^= 1<<h
        out.append(v)
    return out

def apply(cols,v):
    out=0
    while v:
        bit=v&-v
        out ^= cols[bit.bit_length()-1]
        v ^= bit
    return out

def transpose(cols):
    rows=[0]*len(cols)
    for j,v in enumerate(cols):
        while v:
            bit=v&-v
            rows[bit.bit_length()-1] |= 1<<j
            v ^= bit
    return rows

def generators(n,d):
    basis=list(combinations(range(1,d),n))
    ix={s:i for i,s in enumerate(basis)}
    h=len(basis); identity=[1<<j for j in range(h)]
    perms=[]
    for a in range(d-1):
        cols=[]
        for s in basis:
            if a==0:
                if 1 not in s: cols.append(1<<ix[s])
                else:
                    rest=set(s)-{1}; v=0
                    for k in range(1,d):
                        if k not in rest:
                            v ^= 1<<ix[tuple(sorted(rest|{k}))]
                    cols.append(v)
            else:
                t=tuple(sorted(a+1 if k==a else a if k==a+1 else k for k in s))
                cols.append(1<<ix[t])
        perms.append(cols)
    swaps=[]
    for I in combinations(range(2,d),n-1):
        cols=identity[:]; v=0
        for k in range(2,d):
            if k not in I: v ^= 1<<ix[tuple(sorted(I+(k,)))]
        j=ix[(1,)+I]; cols[j]^=v
        swaps.append(cols)
    return basis,perms,swaps

def invariants(n,d):
    basis,perms,swaps=generators(n,d); h=len(basis); gens=perms+swaps
    fixed_rows=[]; image_cols=[]
    for cols in gens:
        diff=[v^(1<<j) for j,v in enumerate(cols)]
        fixed_rows+=transpose(diff)
        image_cols+=diff
    product=[1<<j for j in range(h)]
    for cols in swaps: product=[apply(cols,v) for v in product]
    assert product==perms[0]
    assert all(gf2_rank([v^(1<<j) for j,v in enumerate(cols)])==1 for cols in swaps)
    assert all([apply(cols,v) for v in cols]==[1<<j for j in range(h)] for cols in swaps)
    fixed=gf2_nullspace(fixed_rows,h)
    cofixed=gf2_nullspace(image_cols,h)
    return {'n':n,'d':d,'rank':h,'swap_count':len(swaps),
            'fixed_dimension':len(fixed),'fixed_covector_dimension':len(cofixed),
            'fixed_vectors':fixed,'fixed_covectors':cofixed,
            'swaps_rank_one':True,'swap_product_is_transposition':True}

def vector_orbits(n,d):
    basis,perms,swaps=generators(n,d); h=len(basis)
    if h>20: return None
    gens=perms+swaps
    seen=bytearray(1<<h); sizes=[]
    for v in range(1,1<<h):
        if seen[v]: continue
        seen[v]=1; q=deque([v]); size=0
        while q:
            w=q.popleft();size+=1
            for g in gens:
                z=apply(g,w)
                if not seen[z]:seen[z]=1;q.append(z)
        sizes.append(size)
    return sizes

if __name__=='__main__':
    start=time.monotonic()
    rows=[invariants(n,d) for n in range(2,7) for d in range(n+2,min(n+6,11))]
    for row in rows:
        if row['rank']<=15: row['nonzero_vector_orbits']=vector_orbits(row['n'],row['d'])
    print(json.dumps({'elapsed_seconds':time.monotonic()-start,'results':rows},indent=2))
