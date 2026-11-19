#!/usr/bin/env python3
"""Retained bounded sparse-family experiment, not an all-integer proof."""
from pathlib import Path
from time import perf_counter
import json
started=perf_counter()
# Reuse only the previously retained pure arithmetic definitions, with no run
# or output side effects; the full source dependency is retained beside this.
source=Path(__file__).with_name('ss_higher_even_rectangular_probe.py').read_text()
namespace={}
exec(compile(source.split('cases=[probe(')[0],'<retained-pure-definitions>','exec'),namespace)
basis,one,rank,apply=(namespace[x] for x in ('basis','one','rank','apply'))

def matrix(n,terms):
    B=basis(n);index={v:i for i,v in enumerate(B)};L,R=one(n),one(3)
    s=0
    for x,y,j in terms:s ^= 1<<(3*index[(x,y)]+j)
    C=[]
    for u in range(n):
        for v in range(3):
            c=0
            for a in range(n):
                for b in range(3):
                    if not (s>>(3*a+b))&1:continue
                    for i in range(n):
                        if not (L[a][u]>>i)&1:continue
                        for j in range(3):
                            if (R[b][v]>>j)&1:c ^= 1<<(3*i+j)
            C.append(c)
    ranks=[rank(C)];T=C
    for _ in range(3*n):
        T=[apply(C,c) for c in T];ranks.append(rank(T))
        if ranks[-1]==ranks[-2]:break
    return {'section_bits':s,'ranks':ranks}

out=[]
for q in (3,6,12,24,48):
    families=[
      [(q,0,0),(q-1,0,0),(0,0,1),(0,1,1),(q-2,1,1),(1,0,2),(q-1,0,2)],
      [(q,0,0),(q-1,0,0),(0,0,1),(0,1,1),(q-2,1,1),(q-2,0,2),(q-1,0,2)],
      [(q,0,0),(1,0,0),(0,0,1),(0,1,1),(q-2,1,1),(1,0,2),(q-1,0,2)],
    ]
    for i,terms in enumerate(families):
        out.append({'q':q,'family':i,'terms':terms,**matrix(2*q,terms)})
result={'scope':'Bounded sparse probes only; no uniform theorem','trials':out,'elapsed_seconds':perf_counter()-started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'elapsed_seconds':result['elapsed_seconds'],'trials':[{'q':r['q'],'family':r['family'],'ranks':r['ranks']} for r in out]},indent=2))
