#!/usr/bin/env python3
"""Exact independent torus-character check of G-007, no external packages."""
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations
from pathlib import Path
import csv

def parts3(N):
    for a in range(N, (N+2)//3-1, -1):
        for b in range(min(a,N-a), (N-a+1)//2-1, -1):
            c=N-a-b
            if 0<=c<=b<=a:
                yield (a,b,c)

def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

PERMS=[(p,parity(p)) for p in permutations(range(3))]
RHO=(2,1,0)

def highest(ch,lam):
    return sum(s*ch[tuple(lam[i]+RHO[i]-RHO[p[i]] for i in range(3))] for p,s in PERMS)

def form(n,lam):
    a,b,c=lam
    lo=max(c,2*n-a)
    hi=min(b,2*n-b,n)
    K=hi-lo+1
    assert K>=1
    d2=0 if K%2==0 else (-1)**lo
    res=((a+2)%3,(b+1)%3,c%3)
    d3=0 if len(set(res))<3 else parity(tuple(RHO.index(x) for x in res))
    B=(K+3*d2+2*d3,K-3*d2+2*d3,K-d3)
    D=(6,6,3)
    assert all(v>=0 and v%d==0 for v,d in zip(B,D))
    return tuple(v//d for v,d in zip(B,D))

def chen(n,lam):
    K=min(lam[0]-lam[1],lam[1]-lam[2])+1
    low=K//6
    up=(K+5)//6
    sym=up if K%6 in (0,4) or K%6 in (1,3,5) and lam[1]%2==0 else low
    ext=up if K%6 in (0,4) or K%6 in (1,3,5) and lam[1]%2==1 else low
    std=(K+1)//3
    return sym,ext,std

def count_character(weights,iterator):
    out=Counter()
    for items in iterator:
        w=tuple(sum(weights[j][i] for j in items) for i in range(3))
        out[w]+=1
    return out

def run():
    rows=[]
    for n in range(1,13):
        w=[(a,b,n-a-b) for a in range(n+1) for b in range(n-a+1)]
        cs=count_character(w,combinations_with_replacement(range(len(w)),3))
        ce=count_character(w,combinations(range(len(w)),3))
        tensor=Counter()
        for x in w:
            for y in w:
                for z in w:
                    tensor[tuple(x[i]+y[i]+z[i] for i in range(3))]+=1
        cstd=Counter()
        for weight,value in tensor.items():
            a=value-cs[weight]-ce[weight]
            assert a>=0 and a%2==0
            cstd[weight]=a//2
        for lam in parts3(3*n):
            observed=tuple(highest(c,lam) for c in (cs,ce,cstd))
            predicted=form(n,lam)
            assert observed==predicted==chen(n,lam),(n,lam,observed,predicted,chen(n,lam))
            rows.append((n,','.join(map(str,lam)),*observed,'PASS'))
        print('Direct monomial characters checked n=',n,flush=True)
    comparisons=0
    for n in range(1,101):
        for lam in parts3(3*n):
            assert form(n,lam)==chen(n,lam),(n,lam,form(n,lam),chen(n,lam))
            comparisons+=1
    output=Path(__file__).with_name('DEGREE_THREE_CERTIFICATES.tsv')
    with output.open('w') as f:
        wr=csv.writer(f,delimiter='\t')
        wr.writerow(['n','lambda','outer_3','outer_111','outer_21','status'])
        wr.writerows(rows)
    print('PASS',len(rows),'direct character comparisons;',comparisons,'comparisons to Chen formula')

if __name__=='__main__':
    run()
