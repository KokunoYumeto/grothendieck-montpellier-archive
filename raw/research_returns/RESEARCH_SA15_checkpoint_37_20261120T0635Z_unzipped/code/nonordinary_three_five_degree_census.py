"""Exact finite enumeration of degrees in the proved 3/5 semigroup and its sums.

This verifies only the displayed finite remaining-degree lists; the universal
monodromy proof is the separately audited good-theta norm-step theorem.
"""
from pathlib import Path
import datetime,json,time
start=time.perf_counter();limit=1000
odd=set();a=1
while a<=limit:
 b=a
 while b<=limit:
  odd.add(b);b*=5
 a*=3
even={a+b for a in odd for b in odd if a+b<=limit}
unknown_odd=[d for d in range(1,limit+1,2) if d not in odd]
unknown_even=[d for d in range(2,limit+1,2) if d not in even]
assert unknown_odd[0]==7 and unknown_even[0]==22
assert all(d in even for d in range(2,22,2))
result={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'runtime_seconds':time.perf_counter()-start,'inclusive_limit':limit,
 'proved_odd_family':sorted(odd),'proved_even_sum_family':sorted(even),
 'first_twenty_remaining_odd':unknown_odd[:20],
 'first_twenty_remaining_even':unknown_even[:20],
 'scope':'Exact finite arithmetic of the newly proved f0 families only. Remaining means not in these families, not an assertion of a counterexample. Product surfaces were already classified in all degrees. No infinite theorem is inferred from this finite enumeration.'}
w=Path(__file__).resolve().parents[1];out=w/'outputs/nonordinary_three_five_degree_census.json';assert not out.exists()
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
