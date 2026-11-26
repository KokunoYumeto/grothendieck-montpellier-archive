#!/usr/bin/env python3
"""Independent exact Harper-layer geometric moment comparisons.

Uses Harper's vertex isoperimetric theorem as stated in Raty2020,
arXiv1806.11061v2, Theorem1 and following paragraph, printedp2.
The dimension-(D-1) section contains one of every antipodal pair.
Two independent distance computations (BFS and pairwise Hamming distance)
are required to agree. All comparisons use rational arithmetic.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
from collections import deque,Counter
import json,sys

cfg=json.loads(Path(sys.argv[1]).read_text());out=[]
for D in cfg['dimensions']:
    d=D-1;size=1<<d;K=(size+2)//3;N=6*D
    order=[]
    for r in range(d+1):
        order.extend(sum(1<<i for i in c) for c in combinations(range(d),r))
    assert len(order)==len(set(order))==size
    H=order[:K];dist=[None]*size;q=deque(H)
    for x in H:dist[x]=0
    while q:
        x=q.popleft()
        for i in range(d):
            y=x^(1<<i)
            if dist[y] is None:dist[y]=dist[x]+1;q.append(y)
    direct=[min((x^h).bit_count() for h in H) for x in range(size)]
    assert direct==dist
    counts=Counter(dist);layers=[counts[i] for i in range(max(dist)+1)]
    assert sum(layers)==size
    # Also check that every closed neighborhood is the expected initial
    # simplicial segment; this is the exact order convention used in source.
    for r in range(max(dist)+1):
        actual={x for x in range(size) if dist[x]<=r}
        assert actual==set(order[:len(actual)])
    lower=Fraction(sum(max(0,N-1-12*r)**2*c for r,c in enumerate(layers)),size)
    upper=Fraction(2809*D*D,144)
    out.append({'D':D,'section_dimension':d,'vertices':size,'high_set_minimum':K,
                'layers':layers,'moment_lower':str(lower),'strict_upper':str(upper),
                'margin':str(lower-upper),'excludes':lower>=upper})
result={'status':'PASS','source':'Raty2020 arXiv1806.11061v2 Theorem1 and following paragraph, printedp2',
        'arithmetic':'exact integers and Fractions','independent_distance_methods':['BFS','exhaustive Hamming distances'],
        'rows':out,'reason':'At least one even profile has kappa>=6D-1 on at leastceil(2^(D-1)/3) section vertices. Its12-Lipschitz extension has at least the listed squared moment by Harper; SH55 gives strict upper2809D²/144.'}
Path(sys.argv[2]).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
