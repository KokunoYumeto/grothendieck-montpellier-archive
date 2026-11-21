#!/usr/bin/env python3
"""Exact character dimensions and symmetrized flag-minor candidates."""
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import permutations, combinations
from pathlib import Path
from math import gcd, comb
from fractions import Fraction
import csv
import json

HERE=Path(__file__).resolve().parent
P4=list(permutations(range(4)))

def sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p))
                     for j in range(i+1,len(p)))

SIGNS=[sign(p) for p in P4]

@lru_cache(None)
def compositions(n,k):
    if k==1:
        return ((n,),)
    return tuple((i,)+z for i in range(n+1)
                 for z in compositions(n-i,k-1))

def partitions(n,k,cap=None):
    if k==0:
        if n==0:
            yield ()
        return
    if cap is None: cap=n
    for i in range(min(cap,n),-1,-1):
        if i*k<n: break
        for z in partitions(n-i,k-1,i):
            yield (i,)+z

def sym_char(outer,inner,rank=4):
    weights=compositions(inner,rank)
    h=[{(0,)*rank:1}]
    for i in range(1,outer+1):
        d=defaultdict(int)
        for k in range(1,i+1):
            for x,c in h[i-k].items():
                for y in weights:
                    d[tuple(x[j]+k*y[j] for j in range(rank))]+=c
        assert all(v%i==0 for v in d.values())
        h.append({x:v//i for x,v in d.items()})
    return h[-1]

def schur_mult(weightchar,lam):
    rho=(3,2,1,0)
    ans=0
    for p,sg in zip(P4,SIGNS):
        w=tuple(lam[i]+rho[i]-rho[p[i]] for i in range(4))
        if min(w)>=0:
            ans+=sg*weightchar.get(w,0)
    assert ans>=0
    return ans

def all_schur(outer,inner):
    c=sym_char(outer,inner)
    ans={}
    for lam in partitions(outer*inner,4):
        m=schur_mult(c,lam)
        if m:
            ans[lam]=m
    return ans

def interlaces(lam,mu):
    return all(lam[i]>=mu[i]>=lam[i+1] for i in range(3)) and lam[3]>=mu[3]>=0

MINORS=[s for size in range(1,5) for s in combinations(range(4),size)]
MINOR_INDEX={s:i for i,s in enumerate(MINORS)}
PERM_MINOR=[]
for p in P4:
    z=[]
    for I in MINORS:
        J=tuple(p[i] for i in I)
        z.append((MINOR_INDEX[tuple(sorted(J))],sign(J)))
    PERM_MINOR.append(z)

def tableaux(lam,b):
    # The interlacing sequence records cells with entries at most j.
    for z in partitions(3*b,3,lam[0]):
        mu3=z+(0,)
        if not interlaces(lam,mu3): continue
        for w in partitions(2*b,2,mu3[0]):
            mu2=w+(0,0)
            if not interlaces(mu3,mu2): continue
            mu1=(b,0,0,0)
            if not interlaces(mu2,mu1): continue
            shapes=[(0,0,0,0),mu1,mu2,mu3,lam]
            rows=[]
            for r in range(4):
                row=[]
                for letter in range(1,5):
                    row += [letter-1]*(shapes[letter][r]-shapes[letter-1][r])
                rows.append(row)
            counts=[0]*15
            for col in range(lam[0]):
                I=tuple(rows[r][col] for r in range(4) if col<len(rows[r]))
                assert len(set(I))==len(I) and I==tuple(sorted(I))
                counts[MINOR_INDEX[I]]+=1
            yield tuple(counts)

def sym_orbit(counts):
    d=defaultdict(int)
    for pm in PERM_MINOR:
        nc=[0]*15
        sg=1
        for i,m in enumerate(counts):
            j,sg0=pm[i]
            nc[j]+=m
            if m%2: sg*=sg0
        d[tuple(nc)]+=sg
    d={k:v for k,v in d.items() if v}
    if not d: return ()
    g=0
    for v in d.values(): g=gcd(g,abs(v))
    items=sorted(d.items())
    if items[0][1]<0: g=-g
    return tuple((c,v//g) for c,v in items)

def make_case(L,b):
    r=4
    sm=all_schur(r,b)
    dm=all_schur(r,b-L)
    def dimension(lam):
        z=Fraction(1)
        for i in range(4):
            for j in range(i+1,4):
                z*=Fraction(lam[i]-lam[j]+j-i,j-i)
        assert z.denominator==1
        return z.numerator
    expected=comb(comb(b+3,3)+3,4)
    assert sum(m*dimension(lam) for lam,m in sm.items())==expected
    rows=[]
    data=[]
    for lam,m in sorted(sm.items(),reverse=True):
        target=sum(v for beta,v in dm.items() if interlaces(lam,beta))
        cand=sorted(set(sym_orbit(c) for c in tableaux(lam,b)))
        cand=[o for o in cand if o]
        rows.append(dict(partition=",".join(map(str,lam)),source_multiplicity=m,
                         target_multiplicity=target,candidate_count=len(cand),
                         forced_kernel_lower_bound=max(0,m-target)))
        data.append((lam,m,cand))
    out=HERE/f"POLARIZATION_R4_L{L}_B{b}"
    with out.with_suffix(".tsv").open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter="\t")
        w.writeheader();w.writerows(rows)
    # Simple integer format for the independent modular evaluator.
    with out.with_suffix(".input").open("w") as f:
        print(L,b,len(data),file=f)
        for lam,m,cand in data:
            print(*lam,m,len(cand),file=f)
            for orbit in cand:
                print(len(orbit),file=f)
                for counts,c in orbit:
                    print(c,*counts,file=f)
    print(dict(L=L,b=b,constituents=len(sm),highest_dimension=sum(sm.values()),
               representation_dimension=expected,
               max_mult=max(sm.values()),candidate_count=sum(x["candidate_count"] for x in rows),
               max_candidates=max(x["candidate_count"] for x in rows),
               forced_kernel=sum(x["forced_kernel_lower_bound"] for x in rows)))

if __name__=="__main__":
    import sys
    if len(sys.argv)==3:
        make_case(int(sys.argv[1]),int(sys.argv[2]))
    else:
        make_case(1,3)
        make_case(2,7)
