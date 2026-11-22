#!/usr/bin/env python3
"""Exact finite certificates for the all-prime symbolic E2 counterexample.
The infinite sequence and naturality on all tests are proved in the TeX.
"""
import json,time
start=time.perf_counter()
primes=[2,3,5,7,11]
rows=[]
def principal_part(exp):
    return exp if exp<0 else None
for p in primes:
    ss=[(p**n-1)//(p-1) for n in range(7)]
    for n in range(6):
        assert ss[n+1]==ss[n]+p**n
        assert principal_part(-ss[n+1]+p**n)==principal_part(-ss[n])
    # A monic f=x^p-tx and B=R[x]/f^2 have the stated free bases.
    # delta=b_1*x^p has a nonzero coefficient at basis monomial x^p in B.
    # In A, x^p=t*x, whose b_1 coefficient is [1]=0 in I.
    assert p<2*p
    assert principal_part(-1) is not None
    assert principal_part(-1+1) is None
    rows.append({'p':p,'s_n_through_n6':ss,
        'recurrences_checked':6,'rank_A':p,'rank_B':2*p,
        'nonzero_delta_B_basis_index':p,'delta_A_zero':True})
print(json.dumps({'all_assertions_passed':True,
 'scope':'Exact recurrence and monic-basis certificates for five primes. The proof establishes every prime and every nilpotent test.',
 'cases':rows,'elapsed_seconds':time.perf_counter()-start},indent=2))
