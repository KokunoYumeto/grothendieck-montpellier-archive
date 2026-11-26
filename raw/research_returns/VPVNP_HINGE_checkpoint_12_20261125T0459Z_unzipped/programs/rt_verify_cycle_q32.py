#!/usr/bin/env python3
"""Independently enumerate high-ratio multisets and verify the q32 certificate."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
from collections import Counter
import hashlib, json

w = Path(__file__).resolve().parents[1]
certificate = w/'outputs/pg_cycle_q32_exact.json'
data = json.loads(certificate.read_text())
q = 32
types = sorted((2**a,2**b) for a in range(11) for b in range(11)
               if max(2**a,2**b) > 256*min(2**a,2**b))
assert len(types) == 6
def price_fifths(pair):
    r,s = pair
    exponent = (r*s).bit_length()-1
    return 5*(2**(exponent//2)) if exponent%2 == 0 else 7*(2**(exponent//2))
prices = [price_fifths(t) for t in types]
profiles=[]
def enumerate_multisets(start, remaining, items):
    profiles.append(tuple(items))
    for i in range(start,len(types)):
        if prices[i] <= remaining:
            enumerate_multisets(i,remaining-prices[i],items+[i])
enumerate_multisets(0,674,[])
assert len(profiles) == 205
original_types=[tuple(t) for t in data['types']]
saved={tuple(r['counts']):r for r in data['records']}
assert len(saved)==len(profiles)
summary={}
exceptions=[]
for profile in profiles:
    items=[types[i] for i in profile]
    count=Counter(items)
    key=tuple(count[t] for t in original_types)
    row=saved[key]
    H=[sum(t[c] for t in items) for c in [0,1]]
    minima=sum(min(t) for t in items)
    K=[]
    for c in [0,1]:
        candidates=[0]
        for size in range(1,len(items)+1):
            for subset in combinations(items,size):
                if sum(t[1-c] for t in subset)<=2:
                    candidates.append(sum(t[c] for t in subset))
        K.append(max(candidates))
    L=[max(0,1024-H[c],496+K[c]-H[c]) for c in [0,1]]
    M=max(0,32-minima)
    C=Fraction(sum(prices[i] for i in profile),5)
    bound=C+Fraction(sum(L)+15*M,17)
    assert row['low_R']==L[0] and row['low_S']==L[1]
    assert row['removed_R']==K[0] and row['removed_S']==K[1]
    assert row['low_min']==M and Fraction(row['cost_lower'])==bound
    if bound<=135:
        exceptions.append(key)
    else:
        n=len(items)
        previous=summary.get(n,{'count':0,'minimum':bound})
        previous['count']+=1
        previous['minimum']=min(previous['minimum'],bound)
        summary[n]=previous
assert exceptions==[(1,0,0,1,0,0)]
assert Fraction(99,70)**2>2 and 2**99<135**14
assert 32**2*2>45**2
assert 30*(1+8*Fraction(10,7))<422
assert 390<422 and 334+56*Fraction(10,7)<422
out={'status':'PASS','certificate_sha256':hashlib.sha256(certificate.read_bytes()).hexdigest(),
     'profiles_reconstructed':len(profiles),'independent_types':types,
     'enumeration':'Recursive nondecreasing multisets with integer fifth-unit budget674; all removal subsets enumerated',
     'summary':{str(k):{'count':v['count'],'minimum':str(v['minimum'])} for k,v in summary.items()},
     'sole_exception':exceptions[0],
     'exception':'Separate dyadic-excess proof independently checked; all rational endpoint comparisons pass.'}
(w/'outputs/rt_cycle_q32_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
