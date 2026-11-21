"""Exact character of the five-frame subspace-arrangement Schur ideal."""
from functools import lru_cache
from itertools import combinations
from math import comb
from five_row_cycle_trace import SIZES,CHARS,LABELS,multiplicities,trim

PERMS=((0,1,2,3,4),(1,0,2,3,4),(1,0,3,2,4),
       (1,2,0,3,4),(1,2,0,4,3),(1,2,3,0,4),(1,2,3,4,0))

def cycle_type(p,subset):
    left=set(subset);cycles=[]
    while left:
        current=min(left);length=0
        while current in left:
            left.remove(current);length+=1;current=p[current]
        cycles.append(length)
    return tuple(sorted(cycles,reverse=True))

@lru_cache(None)
def complete_values(cycles,limit):
    values=[1]+[0]*limit
    for ell in cycles:
        for degree in range(ell,limit+1):values[degree]+=values[degree-ell]
    return tuple(values[i]-(values[i-1] if i else 0) for i in range(limit+1))

@lru_cache(None)
def two_row(cycles,a,b):
    rank=sum(cycles)-1
    if b and rank<2:return 0
    h=complete_values(cycles,a+1)
    if not b:return h[a]
    return h[a]*h[b]-h[a+1]*h[b-1]

SUBSETS=[]
for p in PERMS:
    terms=[]
    for size in (1,2,3):
        for subset in combinations(range(5),size):
            if set(p[i] for i in subset)!=set(subset):continue
            selected=cycle_type(p,subset)
            remaining=cycle_type(p,tuple(i for i in range(5) if i not in subset))
            orientation=(-1)**(size-len(selected))
            terms.append(((-1)**size*orientation,remaining))
    SUBSETS.append(tuple(terms))

def traces(x,b):
    a=b+x;answer=[]
    for p,terms in zip(PERMS,SUBSETS):
        value=two_row(cycle_type(p,range(5)),a,b)
        value+=sum(sign*two_row(cycles,a,b) for sign,cycles in terms)
        answer.append(value)
    return tuple(answer)

def coefficients(x,b):
    values=traces(x,b);answer=[]
    for row in CHARS:
        numerator=sum(s*c*v for s,c,v in zip(SIZES,row,values))
        assert numerator%120==0,(x,b,values,numerator)
        answer.append(numerator//120)
    return tuple(answer)

if __name__=='__main__':
    checked=0
    for b in range(7):
        for x in range(10):
            if 2*b+x<5:continue
            lam=(3*b+2*x-5,b+x,b+x,x,0)
            actual=multiplicities(lam)
            proposed=coefficients(x,b)
            if (b+x)%2:proposed=proposed[::-1]
            assert actual==proposed,(x,b,lam,actual,proposed)
            checked+=7
    print('PASS',checked,'actual cycle-trace comparisons')
