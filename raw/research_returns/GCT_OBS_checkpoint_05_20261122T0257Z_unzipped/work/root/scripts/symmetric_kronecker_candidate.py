#!/usr/bin/env python3
"""Exact rectangular (symmetric) Kronecker upper bound for the d=6 candidate.
Python standard library, Murnaghan--Nakayama and conjugacy-class summation.
"""
from functools import lru_cache
from math import factorial
from collections import Counter
import argparse
import json
import time


def partitions(n, largest=None):
    if not n:
        yield ()
        return
    for k in range(min(n,largest or n),0,-1):
        for t in partitions(n-k,k):
            yield (k,)+t


@lru_cache(None)
def hooks(shape,k):
    length=len(shape)
    beads=tuple(shape[i]+length-i-1 for i in range(length))
    result=[]
    for b in beads:
        target=b-k
        if target<0 or target in beads:
            continue
        moved=sorted([x for x in beads if x!=b]+[target],reverse=True)
        smaller=tuple(x-length+i+1 for i,x in enumerate(moved) if x-length+i+1)
        result.append((smaller,(-1)**sum(target<x<b for x in beads)))
    return tuple(result)


@lru_cache(maxsize=1000000)
def character(shape,cycles):
    if not cycles:
        return int(not shape)
    if not shape:
        return 0
    if cycles[0] > shape[0]+len(shape)-1:
        return 0
    return sum(sign*character(smaller,cycles[1:]) for smaller,sign in hooks(shape,cycles[0]))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',required=True)
    args=p.parse_args()
    start=time.monotonic()
    lam=(15,13,13,13);rect=(9,)*6;n=sum(lam);fact=factorial(n)
    ordinary=trace=0
    for index,rho in enumerate(partitions(n),1):
        squared=tuple(sorted([k if k%2 else k//2 for k in rho
                              for _ in range(1 if k%2 else 2)],reverse=True))
        c=character(rect,rho)
        t=character(rect,squared)
        if c or t:
            l=character(lam,rho)
            if l:
                z=1
                for k,m in Counter(rho).items():
                    z*=k**m*factorial(m)
                size=fact//z
                ordinary+=size*l*c*c
                trace+=size*l*t
        if index%20000==0:
            print(json.dumps(dict(cycle_types_processed=index,
                 elapsed_seconds=round(time.monotonic()-start,2),
                 character_cache=character.cache_info()._asdict())),flush=True)
    assert ordinary%fact==0 and trace%fact==0
    g=ordinary//fact;t=trace//fact
    assert (g+t)%2==0
    result=dict(partition=lam,rectangle=rect,cycle_types=index,
                ordinary_kronecker=g,symmetric_kronecker=(g+t)//2,
                alternating_kronecker=(g-t)//2,
                transposition_trace=t,elapsed_seconds=round(time.monotonic()-start,3))
    with open(args.output,'w') as f:
        json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result),flush=True)


if __name__=='__main__':main()
