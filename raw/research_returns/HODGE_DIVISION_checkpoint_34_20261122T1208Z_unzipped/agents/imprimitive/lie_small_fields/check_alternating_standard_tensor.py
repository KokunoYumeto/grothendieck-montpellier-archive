#!/usr/bin/env python3
"""Exact finite endpoints and all quadratic standard-wreath spectra."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from functools import lru_cache
import hashlib,json,time

BASE=Path(__file__).resolve().parent

def partitions(n,minimum=1):
    if n==0:
        yield ()
        return
    for k in range(minimum,n+1):
        for tail in partitions(n-k,k):yield (k,)+tail

def std_spectrum(partition):
    c=Counter()
    for k in partition:
        for j in range(k):c[F(j,k)]+=1
    c[F(0)]-=1
    assert min(c.values())>=0
    return {r:m for r,m in c.items() if m}

@lru_cache(None)
def add_phase(r,s):return (r+s)%1

def tensor(c,d):
    out=Counter()
    for r,m in c.items():
        for s,k in d.items():out[add_phase(r,s)]+=m*k
    return out

def swap(c):
    roots=[r for r,m in c.items() for _ in range(m)]
    out=Counter(roots)
    for i,r in enumerate(roots):
        for s in roots[i+1:]:
            out[(r+s)/2%1]+=1
            out[((r+s)/2+F(1,2))%1]+=1
    return out

def check(c,a,e):
    assert sum(c.values())==e
    for r,m in c.items():
        assert m>=0 and c.get((-r)%1,0)==m
        if r not in (F(0),F(1,2)):assert 3*a*m<=(a+1)*e

start=time.monotonic();rows=[];total_pairs=total_swaps=0
for n in range(8,15):
    a=n-1;e=a*a;parts=list(partitions(n));spectra=[std_spectrum(p) for p in parts]
    for c in spectra:check(c,a,a)
    pairs=0;max_nonreal=0
    for i,c in enumerate(spectra):
        for d in spectra[i:]:
            s=tensor(c,d);check(s,a,e);pairs+=1
            max_nonreal=max([max_nonreal]+[m for r,m in s.items() if r not in (F(0),F(1,2))])
    for c in spectra:
        s=swap(c);check(s,a,e)
        assert 4*(e-max(s.values()))>=e
    upper=F(9*a,14-a);assert a*a>upper
    rows.append({'n':n,'a':a,'partitions':len(parts),'unordered_tensor_pairs':pairs,
                 'swap_types':len(parts),'maximum_nonreal_multiplicity_tensor':max_nonreal,
                 'two_factor_degree':e,'necessary_upper_degree':str(upper)})
    total_pairs+=pairs;total_swaps+=len(parts)
out={'status':'PASS','method':'exact rational roots from permutation cycles; all unordered two-factor spectra and weighted swaps; rational endpoint inequalities',
     'range':[8,14],'tensor_pair_types':total_pairs,'swap_types':total_swaps,'cases':rows,
     'proof_for_arbitrary_t':'the every-power trace inequality in D-AST01; no extrapolation from finite spectra',
     'seconds':round(time.monotonic()-start,3)}
out['proof_sha256']=hashlib.sha256((BASE/'alternating_standard_tensor_section.tex').read_bytes()).hexdigest()
(BASE/'check_alternating_standard_tensor.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
