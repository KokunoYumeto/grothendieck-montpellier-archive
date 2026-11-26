"""Independent recursive enumeration and rational-dual audit for q=64."""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter,defaultdict
from itertools import combinations
import json,hashlib

W=Path(__file__).resolve().parents[1]
p=W/'outputs/pg_cycle_q64_simple_exact.json'
source=json.loads(p.read_text())
q=64; cutoff=359
alpha=F(140,99)
def weight(pair):
    n=(pair[0]*pair[1]).bit_length()-1
    return (2**(n//2))*(alpha if n%2 else F(1))
types=[(2**a,2**b) for a in range(13) for b in range(13)
       if weight((2**a,2**b))<cutoff]
high=sorted(t for t in types if max(t)>1024*min(t))
low=sorted(set(types)-set(high))
assert len(high)==6 and len(low)==127
ts=(3,4,7,9)
y=[F(4201,169740),F(4201,169740),F(17,99),F(8,33),F(8,33)]
for v in (F(2,231),F(5,84),F(32,495),F(40,2829)):y += [v,v]
def measures(pair):
    a,b=pair
    return [a,b,min(a,b),min(a,3*b),min(3*a,b)]+[
        v for t in ts for v in (min(a,t*t*b),min(t*t*a,b))]
for pair in low:
    assert sum(a*b for a,b in zip(y,measures(pair)))<=weight(pair)
base=[4096,4096,88,128,128]+[q*t for t in ts for _ in (0,1)]
saved_order=[tuple(pair) for pair in source['high_types']]
saved={tuple(row['counts']):row for row in source['records']}
records=[]

def audit(items,cost):
    columns=[measures(t) for t in items]
    remaining=[max(0,base[i]-sum(c[i] for c in columns)) for i in range(13)]
    # Enumerate every removable subset, rather than special-case singles/pairs.
    for mask in range(1,1<<len(items)):
        removed=[items[i] for i in range(len(items)) if mask>>i&1]
        rest=[items[i] for i in range(len(items)) if not mask>>i&1]
        for big in (0,1):
            small=1-big
            if sum(t[small] for t in removed)>2:continue
            residual=2016
            if len(removed)==1 and removed[0][small]==1:
                R=removed[0][big]
                rho=64 if R==4096 else 2**((R.bit_length()-1)//2)
                residual=4096-rho*(rho+1)//2
            remaining[big]=max(remaining[big],residual-sum(t[big] for t in rest))
    bound=cost+sum(a*b for a,b in zip(y,remaining))
    counts=tuple(items.count(t) for t in saved_order)
    row=saved.pop(counts)
    assert remaining==row['low_bounds']
    assert bound==F(row['cost_lower']) and cost==F(row['high_cost_lower'])
    assert bound>359
    records.append((len(items),bound))

def enumerate_multisets(first,items,cost):
    audit(items,cost)
    for i in range(first,len(high)):
        new=cost+weight(high[i])
        if new<cutoff:enumerate_multisets(i,items+[high[i]],new)
enumerate_multisets(0,[],F(0))
assert len(records)==540 and not saved
minimum=min(bound for _,bound in records)
assert minimum==F(422523176,1089165)>387
assert alpha*alpha<2<F(99,70)**2
assert 2**297<359**35
groups=defaultdict(list)
for k,b in records:groups[k].append(b)
out={'status':'PASS independent full enumeration and dual audit',
     'source_certificate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'high_types':high,'low_types':len(low),'profiles':len(records),
     'minimum_bound':str(minimum),
     'groups':[{'high_terms':k,'count':len(v),'minimum':str(min(v))} for k,v in sorted(groups.items())],
     'threshold_comparison':'sqrt(2)<99/70 and 2^297<359^35',
     'scope':'All dyadic clipped capacity types and all high-resource multisets below359; no numerical solver used.'}
(W/'outputs/rt_cycle_q64_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
