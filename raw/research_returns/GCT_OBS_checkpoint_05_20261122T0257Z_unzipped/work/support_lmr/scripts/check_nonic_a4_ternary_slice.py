#!/usr/bin/env python3
"""Polarized exact restrictions of four nonic covariants to x2^2 G7.

G7 is an arbitrary ternary form in x0,x1,x3.  The already established
ternary determinant theorem puts this whole family in D9.  This checker
computes coefficients of products of six scalar parameters after
G7=sum t_i*(v_i dot (x0,x1,x3))^7.  A full four-row rank therefore
certifies independence on D9.  Python standard library only.
"""
import argparse
from collections import Counter
from itertools import combinations,permutations
import json
from math import factorial
from pathlib import Path
import random
import time
from explore_four_nonic_covariants import determinant,parity,automorphisms,independent_rows

P=101
ROOT=Path(__file__).resolve().parents[1]
STEP=[3**i for i in range(6)]
TARGET=3**6-1
AVAILABLE=[[i for i in range(6) if state//STEP[i]%3<2] for state in range(3**6)]
PERMS=list(permutations(range(6)))

def linear_product_coefficient(factors):
    """Coefficient of z0^2...z5^2 in12 explicit linear factors."""
    current={0:1}
    for factor in factors:
        following={}
        for state,value in current.items():
            for i in AVAILABLE[state]:
                coefficient=factor[i]
                if coefficient:
                    dest=state+STEP[i]
                    following[dest]=(following.get(dest,0)+value*coefficient)%P
        current={state:value for state,value in following.items() if value}
        if not current:return 0
    return current.get(TARGET,0)

def polarized_value(symbol,points):
    triple={edge:determinant([points[i] for i in edge])
            for edge in combinations(range(6),3)}
    pair={edge:(points[edge[0]][0]*points[edge[1]][1]
                -points[edge[0]][1]*points[edge[1]][0])%P
          for edge in combinations(range(6),2)}
    total=0;nonzero=0
    for pi in PERMS:
        factor=1
        for edge,power in symbol:
            if len(edge)!=2:continue
            transformed=tuple(pi[i] for i in edge)
            value=parity(transformed)*pair[tuple(sorted(transformed))]%P
            factor=factor*pow(value,power,P)%P
        if not factor:continue
        factors=[]
        for edge,power in symbol:
            if len(edge)!=4:continue
            linear=[0]*6
            for position,letter in enumerate(edge):
                others=tuple(pi[i] for i in edge if i!=letter)
                # Expand the fourth-coordinate determinant in column x2.
                linear[letter]=((-1)**(position+2)*parity(others)
                                *triple[tuple(sorted(others))])%P
            factors.extend([linear]*power)
        value=linear_product_coefficient(factors)
        total=(total+factor*value)%P
        nonzero+=bool(value)
    return total,nonzero

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--samples',type=int,default=6)
    ap.add_argument('--symbol',type=int,choices=range(4))
    args=ap.parse_args();start=time.monotonic()
    data=json.loads((ROOT/'results/four_nonic_ambient_selection.json').read_text())
    symbols=[[(tuple(edge),power) for edge,power in symbol] for symbol in data['symbols']]
    assert len(symbols)==4
    for symbol in symbols:
        assert all(sum(power for edge,power in symbol if i in edge)==9 for i in range(6))
        assert sum(power for edge,power in symbol if len(edge)==4)==12
        assert sum(power for edge,power in symbol if len(edge)==2)==3
    rng=random.Random(202611220224)
    samples=[[[rng.randrange(P) for _ in range(3)] for _ in range(6)]
             for _ in range(args.samples)]
    directory=ROOT/'results/four_nonic_ternary_slice';directory.mkdir(exist_ok=True)
    rows=[]
    for i,symbol in enumerate(symbols):
        row=[]
        for j,points in enumerate(samples):
            cache=directory/f's{i}_p{j}.json'
            if args.symbol is not None and args.symbol!=i and not cache.exists():
                row.append(None);continue
            if cache.exists():
                record=json.loads(cache.read_text())
                assert record['symbol']==data['symbols'][i] and record['points']==points
            else:
                began=time.monotonic()
                value,nonzero=polarized_value(symbol,points)
                record=dict(symbol=data['symbols'][i],points=points,value=value,
                            nonzero_ordered_terms=nonzero,
                            seconds=time.monotonic()-began)
                temporary=cache.with_suffix('.tmp')
                temporary.write_text(json.dumps(record,indent=2)+'\n');temporary.replace(cache)
            row.append(record['value'])
            print(json.dumps(dict(symbol=i,sample=j,value=row[-1],seconds=record['seconds'])),flush=True)
        rows.append(row)
    if all(x is not None for row in rows for x in row):
        rank=len(independent_rows(rows))
        result=dict(status='RANK_COMPUTED',prime=P,shape=[4,args.samples],
                    matrix=rows,rank=rank,samples=samples,symbols=data['symbols'],
                    common_differential_factor=pow(2*factorial(7),6,P),
                    seconds=time.monotonic()-start)
        (directory/'result.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({k:v for k,v in result.items() if k not in ('samples','symbols')}),flush=True)

if __name__=='__main__':main()
