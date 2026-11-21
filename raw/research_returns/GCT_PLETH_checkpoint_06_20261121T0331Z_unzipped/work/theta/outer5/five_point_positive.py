#!/usr/bin/env python3
"""T039: an oracle-free positive formula for a higher-flag outer-five family.

The family is lambda=(d+2a+3,d+a+2,d+a,d+a,d), n=d+a+1.
Each returned tag represents nonnegative integer solutions of
2*x2+3*x3+4*x4+5*x5=R.  Repeated tags are deliberately distinguished.
"""
from functools import lru_cache
from itertools import product
import argparse
import json

LABELS=((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))
TAGS={
    (5,):(0,),
    (4,1):(1,2,3,4),
    (3,2):(2,3,4,5,6),
    (3,1,1):(3,4,5,5,6,7),
    (2,2,1):(4,5,6,7,8),
    (2,1,1,1):(6,7,8,9),
    (1,1,1,1,1):(10,),
}
# U=[3,2]. Every list below contains the actual irreducible summands of U*rho.
TENSOR={
    (5,):((3,2),),
    (4,1):((4,1),(3,2),(3,1,1),(2,2,1)),
    (3,2):((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1)),
    (3,1,1):((4,1),(3,2),(3,1,1),(3,1,1),(2,2,1),(2,1,1,1)),
    (2,2,1):((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1)),
    (2,1,1,1):((2,1,1,1),(2,2,1),(3,1,1),(3,2)),
    (1,1,1,1,1):((2,2,1),),
}

def transpose(lam):
    return tuple(sum(v>=j for v in lam) for j in range(1,max(lam,default=0)+1))

def polytope_tags(a,d,mu):
    if type(a) is not int or type(d) is not int or min(a,d)<0:
        raise ValueError("a and d must be nonnegative integers")
    mu=tuple(mu)
    if mu not in LABELS:
        raise ValueError("outer partition must be a partition of five")
    nu=transpose(mu) if (a+d)%2 else mu
    result=[]
    for rho in LABELS:
        for copy,label in enumerate(TENSOR[rho]):
            if label!=nu:continue
            for tableau,degree in enumerate(TAGS[rho]):
                result.append(dict(sector="quadrics",rho=list(rho),copy=copy,
                                   tableau=tableau,degree=degree,R=a-degree))
    for tableau,degree in enumerate(TAGS[nu]):
        result.append(dict(sector="cohomology",rho=list(nu),copy=0,
                           tableau=tableau,degree=degree,R=a-1-degree))
    assert len(result)==6*len(TAGS[nu])<=36
    return result

@lru_cache(None)
def count_coins(R):
    if R<0:return 0
    values=[1]+[0]*R
    for denomination in (2,3,4,5):
        for r in range(denomination,R+1):values[r]+=values[r-denomination]
    return values[R]

def coefficient(a,d,mu):
    return sum(count_coins(tag["R"]) for tag in polytope_tags(a,d,mu))

def witnesses(a,d,mu):
    for tag in polytope_tags(a,d,mu):
        R=tag["R"]
        if R<0:continue
        for x5 in range(R//5+1):
            for x4 in range((R-5*x5)//4+1):
                for x3 in range((R-5*x5-4*x4)//3+1):
                    remaining=R-5*x5-4*x4-3*x3
                    if remaining%2==0:
                        yield tag,(remaining//2,x3,x4,x5)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a",type=int,required=True)
    parser.add_argument("--d",type=int,required=True)
    parser.add_argument("--outer",default="5")
    parser.add_argument("--polytopes",action="store_true")
    args=parser.parse_args()
    mu=tuple(map(int,args.outer.split(",")))
    a,d=args.a,args.d
    tags=polytope_tags(a,d,mu)
    result={"a":a,"d":d,"outer":list(mu),"inner":d+a+1,
            "output":[d+2*a+3,d+a+2,d+a,d+a,d],
            "coefficient":coefficient(a,d,mu),"number_of_tags":len(tags)}
    if args.polytopes:
        result["polytopes"]=[dict(tag,variables=["x2","x3","x4","x5"],
                                   equality_coefficients=[2,3,4,5],
                                   nonnegative=True) for tag in tags]
    print(json.dumps(result,indent=2))

if __name__=="__main__":main()
