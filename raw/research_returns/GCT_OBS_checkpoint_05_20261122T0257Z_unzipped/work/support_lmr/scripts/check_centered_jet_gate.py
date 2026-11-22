#!/usr/bin/env python3
"""Two exact character counts for the finite 804-dimensional (8,9) gate.

First: det^8 in Sym(Sym^2 C^3 + ... + Sym^8 C^3), using GL_3 Weyl
alternation. Second: S_(192,8,8,8) in Sym^24(Sym^9 C^4), using GL_4
Weyl alternation directly. Because all target tail sums are <=24, each
monomial in the three nonfirst variables extends uniquely to outer
polynomial degree24 by adding the pure first-coordinate coefficient.
Only Python's standard library is used. No determinant-side evaluation
rank is claimed by this checker.
"""
from functools import lru_cache
from itertools import permutations,product
from pathlib import Path
import argparse,json,time


@lru_cache(None)
def weight_count(cap,lowest,highest):
    states=list(product(*(range(x+1) for x in cap)))
    index={s:i for i,s in enumerate(states)}
    values=[0]*len(states);values[0]=1
    for generator in states:
        if not lowest<=sum(generator)<=highest:continue
        for dest in states:
            if all(x>=y for x,y in zip(dest,generator)):
                source=tuple(x-y for x,y in zip(dest,generator))
                values[index[dest]]+=values[index[source]]
    return values[-1]


def sign(p):
    # rho is decreasing; its identity permutation is the decreasing tuple.
    return (-1)**sum(p[i]<p[j] for i in range(len(p)) for j in range(i+1,len(p)))


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output')
    args=ap.parse_args();start=time.monotonic()
    centered=[];total=0;rho=(2,1,0)
    for p in permutations(rho):
        target=tuple(8+rho[i]-p[i] for i in range(3))
        value=weight_count(tuple(sorted(target,reverse=True)),2,8)
        total+=sign(p)*value
        centered.append(dict(sign=sign(p),target=target,weight_dimension=value))
    assert total==804
    direct=[];second=0;rho=(3,2,1,0);shape=(192,8,8,8)
    for p in permutations(rho):
        target=tuple(shape[i]+rho[i]-p[i] for i in range(4))
        assert sum(target[1:])<=24
        value=weight_count(tuple(sorted(target[1:],reverse=True)),1,9)
        second+=sign(p)*value
        direct.append(dict(sign=sign(p),target=target,weight_dimension=value))
    assert second==total
    out=dict(status='PASS',partition=shape,outer_degree=24,inner_degree=9,
             centered_dimension=total,direct_plethysm_multiplicity=second,
             centered_weyl_terms=centered,direct_weyl_terms=direct,
             remaining_gate='Rank of the 804-dimensional highest-weight evaluation space on D_(9,4); padded multiplicity is 804 by the proved support/projection argument.',
             elapsed_seconds=time.monotonic()-start)
    if args.output:Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if not k.endswith('weyl_terms')}),flush=True)

if __name__=='__main__':main()
