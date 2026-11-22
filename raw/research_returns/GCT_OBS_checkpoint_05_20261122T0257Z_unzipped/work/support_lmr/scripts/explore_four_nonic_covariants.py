#!/usr/bin/env python3
"""Exact exploratory brackets for six nonics, weight (15,15,12,12).

Every symbol has twelve four-brackets and three two-brackets.  All six
letter degrees are nine.  This file first chooses independent symbols
by polarized evaluations on sums of six ninth powers.  Those ambient
samples are not asserted to be determinants.
"""
import argparse
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations
import json
from pathlib import Path
import random
import time

P=101
ROOT=Path(__file__).resolve().parents[1]
PERMS=list(permutations(range(6)))
BIG=((0,1,2,3),(0,1,4,5),(2,3,4,5))

def parity(a):
    return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))

def automorphisms(symbol):
    reference=Counter(dict(symbol));good=[]
    for pi in PERMS:
        image=Counter();sign=1
        for edge,power in symbol:
            transformed=tuple(pi[i] for i in edge)
            image[tuple(sorted(transformed))]+=power
            sign*=parity(transformed)**power
        if image==reference:
            if sign==-1:return None
            good.append(pi)
    return good

def generate_candidates():
    fours=list(combinations(range(6),4));twos=list(combinations(range(6),2))
    seen=set();result=[];negative=0
    for powers in [(4,4,4),(4,4,3),(4,3,3),(3,3,3)]:
        extra=12-sum(powers)
        for more in combinations_with_replacement([e for e in fours if e not in BIG],extra):
            c=Counter(dict(zip(BIG,powers)));c.update(more)
            residual=[9-sum(p for edge,p in c.items() if i in edge) for i in range(6)]
            if min(residual)<0 or max(residual)>3:continue
            for edges in combinations_with_replacement(twos,3):
                if [sum(i in edge for edge in edges) for i in range(6)]!=residual:continue
                cc=c.copy();cc.update(edges)
                symbol=sorted(cc.items(),key=lambda x:(-len(x[0]),x[0]))
                auts=automorphisms(symbol)
                if auts is None:
                    negative+=1;continue
                canonical=min(tuple(sorted((tuple(sorted(pi[i] for i in e)),p)
                                            for e,p in symbol)) for pi in PERMS)
                if canonical in seen:continue
                seen.add(canonical)
                result.append(dict(symbol=symbol,positive_automorphisms=len(auts),
                                   extra_four_brackets=extra))
    return dict(weight=[15,15,12,12],degree=6,n=9,prime=P,
                candidates=result,negative_automorphism_rejections=negative)

def determinant(matrix):
    a=[list(row) for row in matrix];answer=1
    for j in range(len(a)):
        pivot=next((i for i in range(j,len(a)) if a[i][j]%P),None)
        if pivot is None:return 0
        if pivot!=j:a[pivot],a[j]=a[j],a[pivot];answer=-answer
        value=a[j][j]%P;answer=answer*value%P
        inverse=pow(value,-1,P)
        for i in range(j+1,len(a)):
            scale=a[i][j]*inverse%P
            for k in range(j+1,len(a)):a[i][k]=(a[i][k]-scale*a[j][k])%P
    return answer%P

def polarized_value(symbol,points):
    # Every pair of letters lies in one of the three large four-brackets.
    # Hence all assignments with a repeated point vanish.  The surviving
    # terms for a sum of six ninth powers are precisely these720 permutations.
    brackets={}
    for length in (2,4):
        for edge in combinations(range(6),length):
            brackets[edge]=determinant([[points[i][j] for j in range(length)]
                                       for i in edge])
    total=0
    for pi in PERMS:
        value=1
        for edge,power in symbol:
            ordered=tuple(pi[i] for i in edge)
            value=value*pow(parity(ordered)*brackets[tuple(sorted(ordered))]%P,power,P)%P
            if not value:break
        total+=value
    return total%P

def independent_rows(rows):
    echelon={};selected=[]
    for i,row in enumerate(rows):
        a=list(row)
        for pivot,b in sorted(echelon.items()):
            scale=a[pivot]
            if scale:a=[(x-scale*y)%P for x,y in zip(a,b)]
        pivot=next((j for j,x in enumerate(a) if x),None)
        if pivot is None:continue
        inverse=pow(a[pivot],-1,P)
        echelon[pivot]=[x*inverse%P for x in a];selected.append(i)
    return selected

def extra_candidates(data):
    """Add successively less concentrated brackets only as they are needed."""
    fours=[e for e in combinations(range(6),4) if e not in BIG]
    twos=list(combinations(range(6),2));by_degree={}
    for edges in combinations_with_replacement(twos,3):
        degree=tuple(sum(i in e for e in edges) for i in range(6))
        by_degree.setdefault(degree,[]).append(edges)
    seen={tuple((tuple(e),p) for e,p in r['symbol']) for r in data['candidates']}
    for powers in [(3,3,2),(4,2,2),(3,2,2),(2,2,2)]:
        more_list=list(combinations_with_replacement(fours,12-sum(powers)))
        # Repeated extra brackets usually make the final coefficient joins cheaper.
        more_list.sort(key=lambda more:(len(set(more)),tuple(-n for n in sorted(Counter(more).values(),reverse=True)),more))
        for more in more_list:
            c=Counter(dict(zip(BIG,powers)));c.update(more)
            residual=tuple(9-sum(p for edge,p in c.items() if i in edge) for i in range(6))
            for edges in by_degree.get(residual,()):
                cc=c.copy();cc.update(edges)
                symbol=tuple(sorted(cc.items(),key=lambda x:(-len(x[0]),x[0])))
                if symbol in seen:continue
                seen.add(symbol);auts=automorphisms(symbol)
                if auts is None:continue
                yield dict(symbol=symbol,positive_automorphisms=len(auts),
                           extra_four_brackets=12-sum(powers))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--regenerate',action='store_true')
    ap.add_argument('--samples',type=int,default=12)
    args=ap.parse_args();start=time.monotonic()
    path=ROOT/'results/four_nonic_candidates.json'
    if args.regenerate or not path.exists():
        data=generate_candidates();path.write_text(json.dumps(data,indent=2)+'\n')
    else:data=json.loads(path.read_text())
    randomizer=random.Random(202611220217)
    points=[[[randomizer.randrange(P) for _ in range(4)] for _ in range(6)]
            for _ in range(args.samples)]
    rows=[];selected=[]
    for i,record in enumerate(data['candidates']):
        symbol=[(tuple(e),p) for e,p in record['symbol']]
        assert [sum(p for edge,p in symbol if k in edge) for k in range(6)]==[9]*6
        assert sum(p for edge,p in symbol if len(edge)==4)==12
        assert sum(p for edge,p in symbol if len(edge)==2)==3
        rows.append([polarized_value(symbol,x) for x in points])
        selected=independent_rows(rows)
        print(json.dumps(dict(candidate=i,rank=len(selected),values=rows[-1],
                              seconds=round(time.monotonic()-start,3))),flush=True)
        if len(selected)==4:break
    if len(selected)<4:
        for record in extra_candidates(data):
            i=len(data['candidates']);data['candidates'].append(record)
            symbol=record['symbol']
            rows.append([polarized_value(symbol,x) for x in points])
            selected=independent_rows(rows)
            print(json.dumps(dict(candidate=i,rank=len(selected),values=rows[-1],
                                  seconds=round(time.monotonic()-start,3))),flush=True)
            if len(selected)==4:break
        path.write_text(json.dumps(data,indent=2)+'\n')
    output=dict(status='AMBIENT_SELECTION_ONLY',prime=P,weight=[15,15,12,12],
                selected=selected,points=points,evaluation_rows=rows,
                symbols=[data['candidates'][i]['symbol'] for i in selected],
                rank=len(selected),seconds=time.monotonic()-start)
    (ROOT/'results/four_nonic_ambient_selection.json').write_text(json.dumps(output,indent=2)+'\n')

if __name__=='__main__':main()
