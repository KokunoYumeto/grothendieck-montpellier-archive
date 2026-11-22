#!/usr/bin/env python3
"""Finite checks for A.401; all-arity closure is proved in the paper.

Universe {0,1,2}; Q={1,2}; T={(0,1),(0,2)}. M_n is the family
of finite intersections of equality, Q and T atoms (plus the empty set).
We exhaust M_n through n=4 and every coordinate projection of each relation.
"""
from itertools import product, combinations
from collections import Counter
import json, time
from pathlib import Path

start=time.perf_counter()
R=range(3)
families={}
tuples={n:list(product(R,repeat=n)) for n in range(5)}
for n, ts in tuples.items():
    full=(1<<len(ts))-1
    atoms=[]
    for i in range(n):
        atoms.append(sum(1<<k for k,t in enumerate(ts) if t[i] in (1,2)))
        for j in range(n):
            atoms.append(sum(1<<k for k,t in enumerate(ts) if t[i]==0 and t[j] in (1,2)))
            atoms.append(sum(1<<k for k,t in enumerate(ts) if t[i]==t[j]))
    family={full,0}
    for a in set(atoms):
        family |= {x&a for x in tuple(family)}
    families[n]=family

checked=0
unique_checked=0
violations=[]
for n, family in families.items():
    ts=tuples[n]
    for rel in family:
        members=[t for k,t in enumerate(ts) if rel>>k&1]
        for k in range(n+1):
            for keep in combinations(range(n),k):
                checked+=1
                fibers=Counter(tuple(t[i] for i in keep) for t in members)
                if max(fibers.values(),default=0)<=1:
                    unique_checked+=1
                    image=sum(1<<j for j,t in enumerate(tuples[k]) if t in fibers)
                    if image not in families[k]:
                        violations.append(dict(n=n,rel=rel,keep=keep))

T={(0,1),(0,2)}
Tmask=sum(1<<k for k,t in enumerate(tuples[2]) if t in T)
assert Tmask in families[2]
assert not violations
assert 1 not in families[1] # bit for singleton {0}
out={
    'universe':[0,1,2], 'Q':[1,2], 'T':sorted(T),
    'family_counts':{n:len(f) for n,f in families.items()},
    'M1_relations':[[tuples[1][k][0] for k in range(3) if rel>>k&1] for rel in sorted(families[1])],
    'coordinate_projections_checked':checked,
    'unique_coordinate_projections_checked':unique_checked,
    'unique_projection_violations':violations,
    'ordinary_projection_of_T':[0],
    'ordinary_projection_missing':True,
    'scope':'Exhaustive arities 0..4; general-arity proof in A.401.',
    'seconds':round(time.perf_counter()-start,6)
}
dest=Path(__file__).resolve().parents[1]/'logs'/'unique_existential.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
