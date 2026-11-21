"""Exact bounded-edge trace calculation for lambda=r*(4,3,2,1,0)."""
from functools import lru_cache
from math import gcd
from itertools import product
from pathlib import Path
import json

CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
SIZES=(1,10,15,20,20,30,24)
LABELS=('5','41','32','311','221','2111','11111')
CHARS=((1,1,1,1,1,1,1),(4,2,0,1,-1,0,-1),
       (5,1,1,-1,1,-1,0),(6,0,-2,0,0,0,1),
       (5,-1,1,-1,-1,1,0),(4,-2,0,1,1,0,-1),
       (1,-1,1,1,-1,-1,1))

def permutation_sign(values):
    return (-1)**sum(values[i]>values[j] for i in range(len(values))
                     for j in range(i+1,len(values)))

def bounded_count(lengths,r):
    n=len(lengths)
    targets=[]
    for ell in lengths:
        value=r*(5-ell)
        if value%2:return 0
        targets.append(value//2)
    demands=tuple(r*sum(lengths[i+1:])-targets[i] for i in range(n))

    @lru_cache(None)
    def visit(lengths,demands):
        if len(lengths)==1:return int(demands==(0,))
        if demands[0]<0:return 0
        alpha=lengths[0]
        edges=[]
        for beta in lengths[1:]:
            g=gcd(alpha,beta)
            coeff=[1]
            for _ in range(g):
                nxt=[0]*(len(coeff)+r)
                for i,v in enumerate(coeff):
                    for j in range(r+1):nxt[i+j]+=v
                coeff=nxt
            edges.append((beta//g,alpha//g,coeff))
        def distribute(index,remaining,newdemands,weight):
            if index==len(edges):
                return weight*visit(lengths[1:],tuple(newdemands)) if remaining==0 else 0
            outw,inw,coeff=edges[index]
            answer=0
            for j in range(min(len(coeff)-1,remaining//outw)+1):
                if not coeff[j]:continue
                newdemands[index]+=inw*j
                answer+=distribute(index+1,remaining-outw*j,newdemands,weight*coeff[j])
                newdemands[index]-=inw*j
            return answer
        return distribute(0,demands[0],list(demands[1:]),1)
    return visit(tuple(lengths),demands)

@lru_cache(None)
def trace(g,r):
    lengths=CLASSES[g]
    if any(gcd(r+1,ell)>1 for ell in lengths):return 0
    sign=1
    for ell in lengths:
        sign*=permutation_sign(tuple(((r+1)*j)%ell for j in range(ell)))
    return sign*bounded_count(lengths,r)

def multiplicities(r):
    values=[trace(g,r) for g in range(7)]
    result=[]
    for row in CHARS:
        numerator=sum(s*c*v for s,c,v in zip(SIZES,row,values))
        assert numerator%120==0
        result.append(numerator//120)
    return result

if __name__=='__main__':
    for r in range(9):
        print(r,[trace(g,r) for g in range(7)],multiplicities(r),flush=True)
