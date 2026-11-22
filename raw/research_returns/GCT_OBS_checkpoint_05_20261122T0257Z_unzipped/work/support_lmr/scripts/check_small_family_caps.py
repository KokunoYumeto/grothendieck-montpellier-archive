#!/usr/bin/env python3
"""Exact normalization multiplicity caps for two D9 subfamilies; stdlib only.

At lambda=(192,8,8,8), degree24, compute the multiplicity in
 Sym^9(Sym^24 C4)                       (nine linear factors), and
 Sym^3(Sym^24(Sym^3 C4))                (three cubic factors).
These are target upper bounds for coordinate-ring restriction, not actual
restriction ranks. The latter cap exceeds804 and so gives no obstruction to
using three-cubic products for an804-dimensional rank certificate.
"""
import argparse
from itertools import permutations,product
import json
from math import comb
from pathlib import Path
import time

CAPS=(10,9,8)
STATES=[s for s in product(*(range(c+1) for c in CAPS)) if sum(s)<=24]
INDEX={s:i for i,s in enumerate(STATES)}


def weyl(values):
    terms=[]
    for p in permutations(range(4)):
        # rho=(3,2,1,0): alpha_i=8+rho_i-rho_{p(i)}=8+p(i)-i.
        alpha=tuple(8+p[i]-i for i in range(1,4))
        sign=(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        value=values[INDEX[alpha]]
        terms.append(dict(permutation=p,weight=alpha,sign=sign,value=value))
    return sum(t['sign']*t['value'] for t in terms),terms


def unbounded(generators):
    values=[0]*len(STATES);values[INDEX[(0,0,0)]]=1
    for g in generators:
        for dest in STATES:
            source=tuple(a-b for a,b in zip(dest,g))
            if min(source)>=0:
                values[INDEX[dest]]+=values[INDEX[source]]
    return values


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('work/support_lmr/results/small_family_caps.json'))
    args=parser.parse_args();start=time.monotonic()
    # Three cubic factors. At tail degree <=24, each Sym^24(Sym^3 C4)
    # character stabilizes to the free monomial character of the19 nonleading
    # cubic coefficients: the omitted leading coefficient fills outerdegree24.
    cubic=[s for s in STATES if 1<=sum(s)<=3]
    first=unbounded(cubic*3)
    second=unbounded(cubic+[tuple(2*x for x in s) for s in cubic])
    third=unbounded([tuple(3*x for x in s) for s in cubic])
    assert all((a+3*b+2*c)%6==0 for a,b,c in zip(first,second,third))
    character=[(a+3*b+2*c)//6 for a,b,c in zip(first,second,third)]
    cubic_cap,cubic_terms=weyl(character)
    # Nine linear factors. The zero-tail generator fills unused factor slots;
    # the other monomial generators all have multiplicity one.
    values=[[0]*len(STATES) for _ in range(10)]
    for k in range(10):values[k][0]=1
    for g in STATES[1:]:
        transitions=[]
        for dest in STATES:
            source=tuple(a-b for a,b in zip(dest,g))
            if min(source)>=0:transitions.append((INDEX[dest],INDEX[source]))
        for k in range(1,10):
            for i,j in transitions:values[k][i]+=values[k-1][j]
    linear_cap,linear_terms=weyl(values[9])
    assert linear_cap==377 and cubic_cap==699257,(linear_cap,cubic_cap)
    result=dict(lambda_=[192,8,8,8],degree=24,linear_factor_normalization_cap=linear_cap,
                cubic_factor_normalization_cap=cubic_cap,linear_weyl_terms=linear_terms,
                cubic_weyl_terms=cubic_terms,elapsed_seconds=time.monotonic()-start)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if 'terms' not in k}),flush=True)


if __name__=='__main__':main()
