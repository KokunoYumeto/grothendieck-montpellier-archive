"""Exact finite character/threshold supplement to B75; no existence claims."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
from itertools import combinations_with_replacement
import hashlib
import json
import time

started=time.perf_counter()
primes=[p for p in range(5,102) if all(p%d for d in range(2,int(p**0.5)+1))]
counts=Counter()
next_pairs=[]
third_intervals=[]
for p in primes:
    N=p*p-1
    for b1,b2 in combinations_with_replacement(range(1,p+1),2):
        if (b2-b1)%(p-1):
            continue
        assert b1==b2 or (b1,b2)==(1,p)
        for offset in range(p-1):
            c1=(p*b1+(p+1)*offset)%N
            c2=(c1+p*(b2-b1))%N
            assert (c1-p*b1)%(p+1)==0
            assert (c2-p*b2)%(p+1)==0
            assert (c1-p*b1-c2+p*b2)%N==0
            assert (p+1)*(c1-c2)%N==0
            assert {c1,p*c1%N}=={c2,p*c2%N}
            if b1!=b2:
                assert c2==p*c1%N
                counts['unequal_frobenius_character_pairs']+=1
            else:
                assert c1==c2
                counts['equal_character_pairs']+=1
            counts['terminal_compatible_character_pairs']+=1
    # The next pair is only an abstract obstruction to this simple interval
    # argument. No torsion-isomorphic pair is constructed by this record.
    b1,b2=2,p+1
    c1,c2=(p*b1)%N,(p*b2)%N
    assert (b2-b1)%(p-1)==0
    assert (c1-p*b1-c2+p*b2)%N==0
    assert (p+1)*(c1-c2)%N==0
    assert {c1,p*c1%N}!={c2,p*c2%N}
    next_pairs.append({'p':p,'b':[b1,b2],'c':[c1,c2],
                       'special_orbits':[sorted({c1,p*c1%N}),sorted({c2,p*c2%N})],
                       'actual_group_existence_claimed':False})
    counts['next_arithmetic_only_pairs']+=1

    for n in range(3,10):
        threshold=p**(n-1)*(p+1)
        assert threshold%p==0
        assert threshold//p**(n-1)==p+1
        # Exact terminal interval and the last surviving actual level.
        for b in range(1,p+1):
            Dlast=p**(n-1)*b
            assert Dlast<threshold
            assert n-(n-2)==2 and n-(n-2)-1==1
            counts['terminal_integer_and_level_checks']+=1
        if n>=4:
            assert threshold<p**(2*n-3)
            counts['full_monodromy_threshold_checks']+=1
        else:
            assert threshold>p**(2*n-3)
            counts['formal_only_n3_scope_checks']+=1

    first_t=p**3//(p-1)+1
    while first_t%p==0:
        first_t+=1
    last_t=(p**3*(p+1)-1)//(p-1)
    while last_t%p==0:
        last_t-=1
    first,last=(p-1)*first_t,(p-1)*last_t
    assert p**3<first<=last<p**3*(p+1)<p**5
    next_t=last_t+1
    while next_t%p==0:
        next_t+=1
    next_e=(p-1)*next_t
    assert p**3*(p+1)<next_e<p**5
    third_intervals.append({'p':p,'first_permitted_e':first,'last_permitted_e':last,
                            'next_permitted_e':next_e,'next_bounds':[3,4],
                            'exact_next_claimed':False})
    counts['third_index_interval_endpoints']+=1

assert next(x for x in third_intervals if x['p']==5)=={
    'p':5,'first_permitted_e':128,'last_permitted_e':748,
    'next_permitted_e':752,'next_bounds':[3,4],'exact_next_claimed':False}
scope_witness={'p':5,'e':128,'n':3,
               'formal_bound_applies':128<5**2*6,
               'mixed_threshold_excludes_comparison':128<=5**3,
               'full_index_two_asserted':False}
assert scope_witness['formal_bound_applies']
assert not scope_witness['mixed_threshold_excludes_comparison']

out={
    'status':'PASS',
    'scope':'All terminal compatible abstract character pairs for the listed finite primes, exact induction endpoint arithmetic and full/formal scope separation. No formal-group existence, universal theorem, or exact next-interval index is inferred from finite tests.',
    'primes':primes,'n_range':[3,9],
    'counts':dict(sorted(counts.items())),
    'next_arithmetic_only_pairs':next_pairs,
    'third_index_intervals':third_intervals,
    'formal_vs_full_scope_witness':scope_witness,
    'elapsed_seconds':time.perf_counter()-started,
    'actual_utc':datetime.now(timezone.utc).isoformat(),
    'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
