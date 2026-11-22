#!/usr/bin/env python3
"""Exact sparse D9 test for four degree-six nonic bracket polynomials.

F=(x0*x1*x2)^2*(x3^3+x0*x1*x2).  The two-brackets use
u=(1,1,1,0), v=(0,0,0,1); complete these by e1,e2 to an SL4 matrix.
This is a translate of the standard highest-weight test.  Its only
possible nonzero coefficient pattern is A^5 E, with A=(2,2,2,3),
E=(3,3,3,0).  Its A^4 E^2 contribution is identically zero because
these two-brackets always contain color3, whereas that pattern has
no excess color3 over the twelve four-brackets.
"""
import argparse
from collections import defaultdict,Counter
from itertools import permutations
import json
from math import factorial,prod
from pathlib import Path
import pickle
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
PEER=ROOT.parent/'quaternary/scripts'
sys.path.insert(0,str(PEER))
import explore_three_nonic_covariants as core
from explore_three_nonic_join import product_groups,coefficient_join

P=101
PAIR_COLORS=((0,3),(1,3),(2,3))
BIG=((0,1,2,3),(0,1,4,5),(2,3,4,5))

def embed(key,edge):
    return sum(((key>>(core.ROWBITS*i))&core.ROWMASK)<<(core.ROWBITS*letter)
               for i,letter in enumerate(edge))

def small_terms(symbol,dp):
    out={0:1}
    for edge,power in symbol:
        if len(edge)!=2:continue
        terms=[]
        for a,b in PAIR_COLORS:
            terms.append(((1<<(core.ROWBITS*edge[0]+core.BITS*a))
                          +(1<<(core.ROWBITS*edge[1]+core.BITS*b)),1))
            terms.append(((1<<(core.ROWBITS*edge[0]+core.BITS*b))
                          +(1<<(core.ROWBITS*edge[1]+core.BITS*a)),-1))
        for _ in range(power):
            nxt=defaultdict(int)
            for key,value in out.items():
                for term,sign in terms:nxt[key+term]+=value*sign
            out={k:v%P for k,v in nxt.items() if v%P}
    required=(1,1,1,3)
    def totals(key):
        return tuple(sum((key>>(core.ROWBITS*i+core.BITS*c))&31 for i in range(6))
                     for c in range(4))
    out={key:value for key,value in out.items() if totals(key)==required}
    for edge,power in symbol:
        if len(edge)!=4 or edge in BIG:continue
        factor=[(embed(key,edge),value) for key,value in dp[power].items()]
        nxt=defaultdict(int)
        for key,value in out.items():
            for term,c in factor:nxt[key+term]+=value*c
        out={k:v%P for k,v in nxt.items() if v%P}
    return [(tuple((key>>(core.ROWBITS*i))&core.ROWMASK for i in range(6)),value)
            for key,value in out.items()]

def grouped_targets(pattern,symbol):
    # Only positive letter automorphisms are used.  Coordinate swaps carry
    # nontrivial signs in this odd two-bracket degree and are not quotiented.
    auts=core.automorphisms(symbol);groups=Counter()
    for target in set(permutations(pattern)):
        groups[min(tuple(target[i] for i in aut) for aut in auts)]+=1
    return sorted(groups.items())

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--symbol',type=int,choices=range(4))
    args=ap.parse_args();start=time.monotonic()
    data=json.loads((ROOT/'results/four_nonic_ambient_selection.json').read_text())
    directory=ROOT/'results/four_nonic_sparse';directory.mkdir(exist_ok=True)
    dp={p:core.det_power(p) for p in (1,2,3,4)}
    A=(2,2,2,3);E=(3,3,3,0);pattern=(A,)*5+(E,)
    results=[]
    for index,raw in enumerate(data['symbols']):
        if args.symbol is not None and index!=args.symbol:continue
        symbol=[(tuple(edge),power) for edge,power in raw];powers=dict(symbol)
        tabfile=directory/f's{index}_tables.pickle'
        if tabfile.exists():
            cached=pickle.loads(tabfile.read_bytes());assert cached['symbol']==raw
            tab=cached['table']
        else:
            tab=list(core.tables(symbol,(0,1),dp));tab[2]=small_terms(symbol,dp)
            temporary=tabfile.with_suffix('.tmp')
            temporary.write_bytes(pickle.dumps(dict(symbol=raw,table=tab),protocol=5))
            temporary.replace(tabfile)
        use_join=max(powers[BIG[0]],powers[BIG[1]])<=3
        outer=product_groups(tab) if use_join else None
        groups=grouped_targets(pattern,symbol)
        print(json.dumps(dict(stage='tables',symbol=index,small=len(tab[2]),groups=len(groups),
                              join=use_join,seconds=time.monotonic()-start)),flush=True)
        total=0;records=[]
        for number,(target,multiplicity) in enumerate(groups):
            cache=directory/f's{index}_g{number}.json'
            if cache.exists():
                record=json.loads(cache.read_text())
                assert record['symbol']==raw and record['target']==[list(x) for x in target]
                assert record['multiplicity']==multiplicity
            else:
                began=time.monotonic()
                if use_join:value,joins,tested=coefficient_join(target,tab,outer)
                else:value,joins=core.coefficient(target,tab);tested=None
                record=dict(symbol=raw,target=target,multiplicity=multiplicity,
                            coefficient=value,joins=joins,tested=tested,
                            seconds=time.monotonic()-began)
                temporary=cache.with_suffix('.tmp')
                temporary.write_text(json.dumps(record,indent=2)+'\n');temporary.replace(cache)
            total=(total+multiplicity*record['coefficient'])%P;records.append(record)
            print(json.dumps(dict(symbol=index,group=number,value=record['coefficient'],
                                  multiplicity=multiplicity,seconds=record['seconds'])),flush=True)
        scale=prod(factorial(a) for m in pattern for a in m)%P
        result=dict(symbol=index,coefficient_sum=total,factorial_factor=scale,
                    differential_value=total*scale%P,ordered_assignments=6)
        (directory/f's{index}_result.json').write_text(json.dumps(result,indent=2)+'\n')
        results.append(result);print(json.dumps(result),flush=True)
    print(json.dumps(dict(results=results,seconds=time.monotonic()-start)),flush=True)

if __name__=='__main__':main()
