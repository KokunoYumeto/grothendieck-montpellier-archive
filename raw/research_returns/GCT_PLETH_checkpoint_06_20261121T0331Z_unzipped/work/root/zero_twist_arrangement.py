#!/usr/bin/env python3
"""Exact G027 rank-two first-wall character for every ideal order."""
from functools import lru_cache
from itertools import combinations
from collections import defaultdict
from first_power_zero_twist import PERMS,cycle_type,complete_values
from five_row_cycle_trace import LABELS,SIZES,CHARS,multiplicities

@lru_cache(None)
def normal_schur(cycles,k):
    polynomial={(0,0):1}
    for ell in cycles:
        factor=[(ell*i,ell*(t-i)) for t in range(k) for i in range(t+1)]
        following=defaultdict(int)
        for (a,b),coefficient in polynomial.items():
            for c,d in factor:following[(a+c,b+d)]+=coefficient
        polynomial=dict(following)
    answer=[]
    degree_bound=sum(cycles)*(k-1)
    for degree in range(degree_bound+1):
        for q in range(degree//2+1):
            p=degree-q
            value=polynomial.get((p,q),0)-polynomial.get((p+1,q-1),0)
            if value:answer.append(((p,q),value))
    return tuple(sorted(answer))

@lru_cache(None)
def skew(cycles,a,b,p,q):
    if p>a or q>b:return 0
    h=complete_values(cycles,a-q+1)
    def value(index):
        return h[index] if 0<=index<len(h) else 0
    return value(a-p)*value(b-q)-value(a-q+1)*value(b-p-1)

@lru_cache(None)
def terms(class_index,k):
    permutation=PERMS[class_index];answer=[]
    for size in range(4):
        for selected in combinations(range(5),size):
            if set(permutation[i] for i in selected)!=set(selected):continue
            chosen=cycle_type(permutation,selected)
            complement=cycle_type(permutation,[i for i in range(5) if i not in selected])
            sign=(-1)**len(chosen)
            for rho,value in normal_schur(chosen,k):
                answer.append((sign*value,complement,rho))
    return tuple(answer)

def traces(x,b,k):
    a=b+x
    return tuple(sum(value*skew(cycles,a,b,*rho) for value,cycles,rho in terms(g,k)) for g in range(7))

def coefficients(x,b,k):
    values=traces(x,b,k);answer=[]
    for row in CHARS:
        numerator=sum(s*c*v for s,c,v in zip(SIZES,row,values))
        assert numerator%120==0,(x,b,k,numerator)
        answer.append(numerator//120)
    return tuple(answer)

if __name__=='__main__':
    count=0
    for k in (1,2,3):
        for b in range(10):
            for x in range(10):
                if 2*b+x<5*k:continue
                lam=(3*b+2*x-5*k,b+x,b+x,x,0)
                expected=multiplicities(lam)
                value=coefficients(x,b,k)
                if (b+x)%2:value=value[::-1]
                assert value==expected,(x,b,k,lam,value,expected)
                count+=7
    print('PASS',count,'actual multiplicities')

