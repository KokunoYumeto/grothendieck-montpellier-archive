#!/usr/bin/env python3
"""Exact balanced S5 traces by Pieri branching and cycle alternants."""
from functools import lru_cache
from itertools import combinations, product
from math import comb
import json
from pathlib import Path

CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
SIZES=(1,10,15,20,20,30,24)
LABELS=('5','41','32','311','221','2111','11111')
CHARS=((1,1,1,1,1,1,1),(4,2,0,1,-1,0,-1),
       (5,1,1,-1,1,-1,0),(6,0,-2,0,0,0,1),
       (5,-1,1,-1,-1,1,0),(4,-2,0,1,1,0,-1),
       (1,-1,1,1,-1,-1,1))

def sign(values):
    return (-1)**sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))

def trim(lam):
    lam=list(lam)
    while lam and lam[-1]==0:lam.pop()
    return tuple(lam)

@lru_cache(None)
def remove_horizontal(lam,n,max_rows):
    """All eta with lam/eta a horizontal n-strip and length <=max_rows."""
    if len(lam)>max_rows+1:return ()
    values=lam+(0,)*(max_rows+1-len(lam))
    target=sum(lam)-n;answer=[]
    if target<0:return ()
    def visit(i,remaining,prefix):
        if i==max_rows:
            if remaining==0:answer.append(trim(prefix))
            return
        lower,upper=values[i+1],values[i]
        for value in range(lower,min(upper,remaining)+1):
            visit(i+1,remaining-value,prefix+(value,))
    visit(0,target,())
    return tuple(answer)

def single_cycle(lam,length):
    if len(lam)>length:return 0
    padded=lam+(0,)*(length-len(lam))
    residues=tuple((padded[i]+length-1-i)%length for i in range(length))
    if len(set(residues))<length:return 0
    return sign(residues)*(-1)**(length*(length-1)//2)

def two_double_cycles(lam,n):
    if len(lam)>4:return 0
    padded=lam+(0,)*(4-len(lam))
    exponents=tuple(padded[i]+3-i for i in range(4))
    even=[v//2 for v in exponents if v%2==0]
    odd=[v//2 for v in exponents if v%2]
    if len(even)!=2 or len(odd)!=2:return 0
    alpha=(even[0]-1,even[1]);beta=(odd[0]-1,odd[1])
    residues=[v%2 for v in exponents]
    epsilon=sign(residues)*(-1)**3
    lower=max(alpha[1],n-beta[0]);upper=min(alpha[0],n-beta[1])
    return epsilon*max(0,upper-lower+1)

def three_two_cycles(lam,n):
    padded=lam+(0,)*(5-len(lam))
    exponents=tuple(padded[i]+4-i for i in range(5));answer=0
    for selected in combinations(range(5),3):
        other=tuple(i for i in range(5) if i not in selected)
        first=[exponents[i] for i in selected];second=[exponents[i] for i in other]
        rfirst=[v%3 for v in first];rsecond=[v%2 for v in second]
        if len(set(rfirst))<3 or len(set(rsecond))<2:continue
        a=(sum(first)-3)//3;b=(sum(second)-1)//2
        epsilon=(-1)**(sum(selected)+3)*sign(rfirst)*(-1)**3*sign(rsecond)*(-1)
        # Expand (T1^2-T2^3)^(-1) in T2^3/T1^2.
        offset=a-n-2
        if offset>=0 and offset%2==0 and b+3*(offset//2)==n:answer+=epsilon
    return answer

@lru_cache(None)
def cycle_trace(lam,n,cycles):
    lam=trim(lam)
    if sum(lam)!=sum(cycles)*n:return 0
    if len(lam)>sum(cycles):return 0
    if len(cycles)==1:return single_cycle(lam,cycles[0])
    if cycles[-1]==1:
        remaining=cycles[:-1]
        return sum(cycle_trace(eta,n,remaining) for eta in remove_horizontal(lam,n,sum(remaining)))
    if cycles==(2,2):return two_double_cycles(lam,n)
    if cycles==(3,2):return three_two_cycles(lam,n)
    raise ValueError(('unsupported cycle type',cycles))

def traces(lam):
    lam=trim(lam)
    if sum(lam)%5:raise ValueError('partition size must be divisible by five')
    n=sum(lam)//5
    return tuple(cycle_trace(lam,n,c) for c in CLASSES)

def multiplicities(lam):
    values=traces(lam);answer=[]
    for row in CHARS:
        total=sum(s*v*c for s,v,c in zip(SIZES,values,row))
        if total%120:raise ArithmeticError((lam,values,total))
        answer.append(total//120)
    return tuple(answer)

def partition_from_gaps(gaps):
    return tuple(sum(gaps[i:]) for i in range(4))+(0,)

def main():
    from staircase_five_positive import trace as staircase_trace
    for r in range(8):
        lam=(4*r,3*r,2*r,r,0)
        actual=traces(lam);expected=tuple(staircase_trace(g,r) for g in range(7))
        assert actual==expected,(r,actual,expected)
        print('staircase PASS',r,multiplicities(lam),flush=True)
    seeds=[]
    for parity in product(range(2),repeat=4):
        candidates=[]
        for gaps in product(*(tuple(v for v in range(2,6) if v%2==p) for p in parity)):
            lam=partition_from_gaps(gaps)
            if sum(lam)%5==0:candidates.append((sum(lam),gaps,lam))
        for _,gaps,lam in sorted(candidates):
            values=multiplicities(lam)
            if min(values)>0:
                item={'parity':parity,'gaps':gaps,'partition':lam,'inner':sum(lam)//5,
                      'traces':traces(lam),'multiplicities':values}
                seeds.append(item);print('seed',item,flush=True);break
        else:print('UNRESOLVED parity',parity,flush=True)
    Path(__file__).with_name('FIVE_ROW_PARITY_SEEDS.json').write_text(json.dumps(seeds,indent=2)+'\n')
    print('found',len(seeds),'parity seeds',flush=True)

if __name__=='__main__':main()
