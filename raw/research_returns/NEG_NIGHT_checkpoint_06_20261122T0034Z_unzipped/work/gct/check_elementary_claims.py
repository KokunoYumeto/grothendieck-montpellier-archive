"""Finite checks supplementing, not replacing, the proofs in chapter.tex."""
from pathlib import Path
from math import isqrt
import json

primes=[p for p in range(2,44) if all(p%d for d in range(2,isqrt(p)+1))]
point_counts=[]
for p in primes:
    n=sum((z*z-u*v*v-4*u**4)%p==0 for u in range(p) for v in range(p) for z in range(p))
    assert n==p*p
    point_counts.append({'p':p,'count':n})
indices=[]
for L in range(2,101):
    # The shifted constituent indexed by n mod L has constant p+1-((r+p) mod L).
    pp=next(p for p in range(L) if min(p+1-((r+p)%L) for r in range(L))>=0)
    ss=next(p for p in range(L) if min(1+p+1-((r+p)%L) for r in range(L))>0)
    assert pp==ss==L-2
    assert all(L*(n//L)+1>=1 for n in range(5*L))
    indices.append({'L':L,'positivity_index':pp,'strict_saturation_index':ss})
out={'D5_prime_field_counts':point_counts,'full_support_index_checks':indices,
     'scope':'Computations over listed prime fields and integer parameters only; full proofs cover all finite fields and all L.'}
Path('work/gct/elementary_checks.json').write_text(json.dumps(out,indent=2))
print('D5 prime fields:',len(primes),'all q^2; strict-index families:',len(indices),'all L-2')
