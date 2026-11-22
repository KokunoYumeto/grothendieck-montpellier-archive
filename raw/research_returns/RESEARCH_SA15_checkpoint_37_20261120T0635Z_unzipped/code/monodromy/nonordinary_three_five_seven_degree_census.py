"""Finite arithmetic of the 3/5/7 odd family and sums of two members.

No infinite monodromy theorem is inferred from this enumeration.
"""
from pathlib import Path
import datetime,json,time

start=time.perf_counter();limit=1000
odd=set();a=1
while a<=limit:
    b=a
    while b<=limit:
        c=b
        while c<=limit:
            odd.add(c);c*=7
        b*=5
    a*=3
def is_smooth(n):
    for prime in (3,5,7):
        while n%prime==0:n//=prime
    return n==1
assert odd=={d for d in range(1,limit+1,2) if is_smooth(d)}
even={a+b for a in odd for b in odd if a+b<=limit}
assert even=={d for d in range(2,limit+1,2) if any(a in odd and d-a in odd for a in range(1,d,2))}
missing_odd=[d for d in range(1,limit+1,2) if d not in odd]
missing_even=[d for d in range(2,limit+1,2) if d not in even]
assert missing_odd[0]==11 and missing_even[0]==92
assert all(d in even for d in range(2,92,2))
witnesses={str(d):next([a,d-a] for a in sorted(odd) if d-a in odd) for d in sorted(even)}
result={'status':'PASS_FINITE_ARITHMETIC',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'runtime_seconds':time.perf_counter()-start,'inclusive_limit':limit,
 'odd_three_five_seven_family':sorted(odd),'even_sum_family':sorted(even),
 'even_witnesses':witnesses,
 'first_twenty_degrees_outside_odd_family':missing_odd[:20],
 'first_twenty_degrees_outside_even_family':missing_even[:20],
 'scope':'Exact finite family membership only. Degrees outside the family are unresolved by these theorems, not counterexamples; product surfaces were already classified in every degree.'}
root=Path(__file__).resolve().parent.parent
out=root/'outputs/nonordinary_three_five_seven_degree_census.json'
assert not out.exists()
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
