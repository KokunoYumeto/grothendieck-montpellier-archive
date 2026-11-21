#!/usr/bin/env python3
"""T041: oracle-free positive formula for the five-point hook-bundle family."""
from functools import lru_cache
from math import comb
import argparse,json
from five_point_positive import LABELS,TENSOR,transpose

FOUR={
    (5,):(4,6,13),
    (4,1):(2,3,3,4,4,4,5,5,5,6,6,7),
    (3,2):(2,3,3,4,4,4,5,5,5,6,6,6,7,7,8),
    (3,1,1):(1,2,3,3,4,4,5,5,5,6,6,6,7,7,7,8,8,9),
    (2,2,1):(2,3,4,4,5,5,5,6,6,6,7,7,8,8,9),
    (2,1,1,1):(3,4,4,5,5,6,6,7,7,8,9,10),
    (1,1,1,1,1):(6,7,8),
}
THREE={(5,):(5,6,7)}

@lru_cache(None)
def coins(weights,R):
    if R<0:return 0
    values=[1]+[0]*R
    for weight in weights:
        for i in range(weight,R+1):values[i]+=values[i-weight]
    return values[R]

def tags(a,d,mu):
    if type(a) is not int or type(d) is not int or a<1 or d<0:
        raise ValueError('a must be positive and d nonnegative')
    mu=tuple(mu)
    if mu not in LABELS:raise ValueError('outer must be a partition of five')
    nu=transpose(mu) if (a+d)%2 else mu
    answer=[]
    for rho in LABELS:
        for copy,label in enumerate(TENSOR[rho]):
            if label!=nu:continue
            for weights,shifts in (((2,3,4,5),FOUR[rho]),((2,3,5),THREE.get(rho,()))):
                for index,shift in enumerate(shifts):
                    answer.append(dict(rho=list(rho),copy=copy,tag=index,
                                       weights=list(weights),shift=shift,R=a-shift))
    assert len(answer)<=90
    return answer

def coefficient(a,d,mu):
    return sum(coins(tuple(tag['weights']),tag['R']) for tag in tags(a,d,mu))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--a',required=True,type=int)
    parser.add_argument('--d',required=True,type=int)
    parser.add_argument('--outer',default='5')
    parser.add_argument('--polytopes',action='store_true')
    args=parser.parse_args();a,d=args.a,args.d
    mu=tuple(map(int,args.outer.split(',')))
    result=dict(a=a,d=d,outer=list(mu),inner=d+a+1,
                output=[d+2*a+4,d+a+2,d+a,d+a-1,d],
                coefficient=coefficient(a,d,mu))
    if args.polytopes:result['polytopes']=tags(a,d,mu)
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
