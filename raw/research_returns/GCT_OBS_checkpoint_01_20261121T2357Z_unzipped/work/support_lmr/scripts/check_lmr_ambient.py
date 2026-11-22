#!/usr/bin/env python3
"""Exact <h_12[h_3],s_(19,7,2,2,2,2,2)> using only Python stdlib.

Newton's recurrence constructs h_d[h_3] in the power-sum basis:
 d*h_d[h_3] = sum_(i=1)^d h_(d-i)[h_3]*(p_i^3+3*p_i*p_(2i)+2*p_(3i))/6.
Murnaghan--Nakayama is implemented by beta-number moves. No stored numerical
multiplicities or external character table are used.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import factorial
from pathlib import Path
import argparse, json, time


def plethysm(d):
    h=[{():Fraction(1)}]
    for k in range(1,d+1):
        current=defaultdict(Fraction)
        for i in range(1,k+1):
            for cycles,c in h[k-i].items():
                for extra,m in (((i,i,i),1),((2*i,i),3),((3*i,),2)):
                    current[tuple(sorted(cycles+extra,reverse=True))]+=c*Fraction(m,6*k)
        h.append(dict(current))
        assert sum(current.values())==1
    return h[d]


@lru_cache(None)
def character(shape,cycles):
    if not cycles: return int(not shape)
    k=cycles[0]; length=len(shape)
    beads=tuple(shape[i]+length-i-1 for i in range(length))
    answer=0
    for b in beads:
        target=b-k
        if target<0 or target in beads: continue
        moved=sorted([c for c in beads if c!=b]+[target],reverse=True)
        smaller=tuple(c-length+i+1 for i,c in enumerate(moved) if c-length+i+1)
        crossings=sum(target<c<b for c in beads)
        answer+=(-1)**crossings*character(smaller,cycles[1:])
    return answer


def hook_dimension(shape):
    product=1
    for i,row in enumerate(shape):
        for j in range(row):
            product*=row-j+sum(other>j for other in shape[i+1:])
    return factorial(sum(shape))//product


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output')
    args=ap.parse_args();start=time.monotonic()
    shape=(19,7,2,2,2,2,2); degree=12
    expansion=plethysm(degree)
    value=sum((c*character(shape,t) for t,c in expansion.items()),Fraction())
    dim=hook_dimension(shape)
    assert character(shape,(1,)*36)==dim
    assert value==6
    out=dict(partition=shape,outer_degree=degree,inner_degree=3,
             cycle_types=len(expansion),cycle_index_mass=str(sum(expansion.values())),
             symmetric_group_dimension=dim,ambient_multiplicity=int(value),
             method='Newton plethysm recurrence; exact beta-number Murnaghan--Nakayama',
             elapsed_seconds=time.monotonic()-start,status='PASS')
    if args.output:Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out),flush=True)

if __name__=='__main__': main()
