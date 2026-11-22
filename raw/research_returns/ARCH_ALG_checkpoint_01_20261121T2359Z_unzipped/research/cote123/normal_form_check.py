"""Exact finite check of CC-AP04-05; not a proof for arbitrary n.
All arithmetic is in Z/n; enumeration includes all ordered flags modulo K_n.
"""
from itertools import permutations
from math import gcd, factorial
import json

def canonical(p, s, n, units):
    candidates=[]
    for a in units:
        q=tuple((a*(x-p[0]))%n for x in p)
        ai=pow(a,-1,n)
        t=tuple((ai*(x-s[0]))%n for x in s)
        candidates.append((q,t))
    return min(candidates)

rows=[]
for n in range(2,8):
    units=[a for a in range(1,n) if gcd(a,n)==1]
    orders=[(0,)+t for t in permutations(range(1,n))]
    p_reps=[p for p in orders if p==min(tuple(a*x%n for x in p) for a in units)]
    count=fixed=0
    for p in p_reps:
        for s in orders:
            count+=1
            ptheta=p[::-1]
            stheta=tuple((-x)%n for x in s[::-1])
            if canonical(ptheta,stheta,n,units)==(p,s):
                fixed+=1
    assert count==factorial(n)**2//(n*n*len(units))
    if n%2:
        assert fixed==0
    elif n>=4:
        assert fixed>0
    rows.append({'n':n,'inner_classes':count,'fixed_by_inverse_transpose':fixed,'out_group':'trivial' if n==2 else 'C2'})
print(json.dumps(rows,indent=2))
