#!/usr/bin/env python3
"""Bounded higher-even rectangular probes; no generic/all-degree claim.

Uses the explicitly derived monomial Cartier identities on y²+y=x³.
Every sampled coefficient and rank is retained, including rejected trials.
"""
from pathlib import Path
from time import perf_counter
from random import Random
from itertools import product
import json
start=perf_counter()

def basis(n):
    return [(i,0) for i in range(n//2+1)]+[(i,1) for i in range((n-3)//2+1)]

def one(n):
    B=basis(n); ix={v:i for i,v in enumerate(B)};tab=[]
    for a in B:
        row=[]
        for b in B:
            x,y=a[0]+b[0],a[1]+b[1]
            terms=[(x,y)] if y<2 else [(x,1),(x+3,0)]
            v=0
            for r,e in terms:
                if e:target=((r//2,1) if r%2 else (r//2+1,0))
                else:target=(r//2,0) if r%2 else None
                if target is not None:v ^= 1<<ix[target]
            row.append(v)
        tab.append(row)
    return tab

def rank(cols):
    p={}
    for v in cols:
        while v:
            b=v.bit_length()-1
            if b in p:v ^= p[b]
            else:p[b]=v;break
    return len(p)

def apply(cols,v):
    r=0
    while v:
        bit=v&-v;v ^= bit;r ^= cols[bit.bit_length()-1]
    return r

def probe(n,m,budget=100):
    L,R=one(n),one(m);N=n*m;elem=[]
    for a,b in product(range(n),range(m)):
        row=[]
        for u,v in product(range(n),range(m)):
            c=0
            for i in range(n):
                if not (L[a][u]>>i)&1:continue
                for j in range(m):
                    if (R[b][v]>>j)&1:c ^= 1<<(m*i+j)
            row.append(c)
        elem.append(row)
    seed=202611191147+n*101+m
    rng=Random(seed);trials=[];witness=None
    for attempt in range(budget):
        s=rng.getrandbits(N);C=[0]*N
        for i in range(N):
            if (s>>i)&1:C=[x^y for x,y in zip(C,elem[i])]
        ranks=[rank(C)];T=C
        for _ in range(N):
            T=[apply(C,c) for c in T];r=rank(T);ranks.append(r)
            if r==ranks[-2]:break
        trials.append({'section_bits':s,'iterate_ranks':ranks})
        if ranks[-1]==N-2:
            witness={'section_bits':s,'columns':C,'stable_rank':ranks[-1]};break
    return {'degrees':[n,m],'seed':seed,'budget':budget,'trials':trials,'witness':witness}

cases=[probe(n,3) for n in (6,12,24,48,96)]
out={'status':'COMPLETED_BOUNDED_PROBE','scope':'Finite exact witnesses only; no all-valuation geometric theorem inferred','cases':cases,'elapsed_seconds':perf_counter()-start}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'cases':[{'degrees':c['degrees'],'attempts':len(c['trials']),'witness_rank':None if c['witness'] is None else c['witness']['stable_rank']} for c in cases],'elapsed_seconds':out['elapsed_seconds']},indent=2))
