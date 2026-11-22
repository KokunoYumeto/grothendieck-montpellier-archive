"""Independent exact supplement to conditional HD-ALT10; no author imports."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from math import factorial, prod, comb
import hashlib
import json
import time

start = time.perf_counter()
here = Path(__file__).resolve().parent
proof = here.parents[2]/'research/alternating_four_tail_integer_cutoffs_section.tex'
expected = '3bcc1ca3a7e59f91cb9e46618d5fb8d05244a503a588c69610960e364485b75a'
assert hashlib.sha256(proof.read_bytes()).hexdigest() == expected

# Direct substitution simplifies the inner quadratic to n-17.
# Expand the remaining two cubic products by integer coefficient convolution.
def multiply(a,b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c

first = [5*x for x in multiply(multiply([0,1],[-3,1]),[-17,1])]
second = [Q(3,2)*x for x in multiply(multiply([3,1],[-1,1]),[-2,1])]
polynomial = [a-b for a,b in zip(first,second)]
assert polynomial == [Q(-9),Q(531,2),Q(-100),Q(7,2)]
shifted = [sum(polynomial[j]*comb(j,i)*36**(j-i)
               for j in range(i,4)) for i in range(4)]
assert shifted == [Q(43245),Q(13347,2),Q(278),Q(7,2)]
assert all(x > 0 for x in shifted)

# Endpoint numerator as a polynomial in m, with n=4m-2.
left = [4*x for x in multiply([0,1],[-7,4])]
right = multiply([-3,4],[-4,4])
assert [a-b for a,b in zip(left,right)] == [-12,0,0]
assert 3*35**2 > 5*27**2
assert 3*19**2 < 5*15**2

count = 0
for h in range(2,163):
    m = 5*h
    for n in range(36,20*h-2):
        d = (n-1)*(n-2)
        assert 5*n*(n-3)*(4*m*(n-5)-d) > 6*m*d
        count += 1
    n = 20*h-2
    assert 4*m*(n-5) < (n-1)*(n-2)
    assert 3*n*n < 5*(n-8)**2
    # Also consistent with ALT08's conductor-dependent sharper shape.
    assert 4*m*(n-4) < n*n

def hook(lam):
    terms = []
    for i,length in enumerate(lam):
        for j in range(length):
            terms.append(length-j+sum(t>j for t in lam[i+1:]))
    degree, remainder = divmod(factorial(sum(lam)),prod(terms))
    assert not remainder
    return degree

rows = []
for radicand,h in [(1,2),(2,4),(7,6),(11,10),(19,18),(43,42),(67,66),(163,162)]:
    n = 20*h-2
    a = hook((n-4,4))
    assert a == comb(n,4)-comb(n,3) == n*(n-1)*(n-2)*(n-7)//24
    assert Q(a)-Q(n*(n-3),2) == Q(n*(n+1)*(n*n-11*n+22),24) > 0
    beta = Q(4*(n-5),(n-1)*(n-2))
    assert beta-Q(1,5*h) == -Q(12,5*h*(n-1)*(n-2))
    rows.append({'radicand':radicand,'h':h,'n':n,'actual_hook_degree':a,
                 'beta':str(beta),'endpoint_difference':str(beta-Q(1,5*h))})

out = {'status':'PASS conditional on the stated k>=4 premises',
       'completed_utc':datetime.now(timezone.utc).isoformat(),
       'runtime_seconds':time.perf_counter()-start,
       'proof_sha256':expected,
       'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'rejected_integer_pairs':count,'h_grid':[2,162],
       'substituted_cubic_ascending':list(map(str,polynomial)),
       'shifted_positive_cubic_ascending':list(map(str,shifted)),
       'field_rows':rows,
       'scope':'Independent algebra/arithmetic for the derived cutoff; does not approve pending three-box exclusions, produce a source, or count as independent movement.'}
(here/'independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
