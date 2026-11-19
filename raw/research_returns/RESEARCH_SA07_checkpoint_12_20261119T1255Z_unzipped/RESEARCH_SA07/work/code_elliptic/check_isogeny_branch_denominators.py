#!/usr/bin/env python3
"""Exact primitive cyclic-line enumeration and denominator sums for note50."""
import datetime, hashlib, json, pathlib, time
from collections import Counter
from fractions import Fraction
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
tick=time.perf_counter()
def vp(a,p,n):
    if a==0:return n
    v=0
    while a%p==0:a//=p;v+=1
    return v
def expected(p,n):
    return {0:p**n,**{m:(p-1)*p**(n-m-1) for m in range(1,n)},n:1}
def total_sum(p,n):
    r=n//2
    return 2*(p**r-1)//(p-1) if n%2==0 else ((p+1)*p**r-2)//(p-1)
records=[]
# Enumerate every primitive vector; quotient by actual unit scaling.
for p,maxn in [(3,4),(5,3),(7,3)]:
    for n in range(1,maxn+1):
        q=p**n
        lines=set()
        for a in range(q):
            for b in range(q):
                if b%p:
                    ib=pow(b,-1,q);lines.add((a*ib%q,1))
                elif a%p:
                    ia=pow(a,-1,q);lines.add((1,b*ia%q))
        counts=Counter()
        for a,b in lines:
            # Directly count intersection with the first-axis subgroup.
            order=sum(1 for k in range(q) if k*b%q==0)
            m=vp(order,p,n)
            assert order==p**m
            counts[m]+=1
        assert dict(counts)==expected(p,n)
        D=(p+1)*p**(n-1)
        assert len(lines)==D
        S=sum(counts[m]*max(0,2*m-n) for m in counts)
        assert S==total_sum(p,n)
        # Fractional b occurs at ramified completions; test exact values too.
        for b0 in [Fraction(0),Fraction(1,2),Fraction(1),Fraction(5,3)]:
            negative=sum(counts[m]*max(Fraction(0),2*m-n-b0) for m in counts)
            assert 0<=negative<=S
        records.append({'p':p,'n':n,'counts':dict(sorted(counts.items())),
                        'total':D,'denominator_sum_b0':S,'mean_b0':str(Fraction(S,D))})
# Check both closed parity formulas against their finite geometric sums.
for p in [2,3,5,7,11,101]:
    for n in range(1,101):
        S=sum(c*max(0,2*m-n) for m,c in expected(p,n).items())
        assert S==total_sum(p,n)
record={'start_utc':start,'elapsed_seconds':time.perf_counter()-tick,
        'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        'input':'all primitive vectors for p=3,n<=4; p=5,7,n<=3; geometric sums p=2,3,5,7,11,101,n<=100',
        'enumeration':records,'geometric_sum_checks':600,
        'scope':'finite exact checks; arbitrary n formulas proved in work note50','status':'PASS'}
print(json.dumps(record,indent=2))
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
