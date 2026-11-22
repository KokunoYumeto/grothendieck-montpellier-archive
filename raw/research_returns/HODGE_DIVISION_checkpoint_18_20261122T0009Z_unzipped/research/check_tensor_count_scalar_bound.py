"""Exact permutation and weighted-tensor checks for HD-TC01--03."""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
from collections import Counter
from itertools import product
from math import gcd,lcm,comb
import hashlib,json,time
import sympy as s
R=Path(__file__).resolve().parent
start=time.perf_counter();stamp=datetime.now(timezone.utc).isoformat()
def partitions(n,top=None):
    if not n:yield ();return
    for k in range(min(n,top or n),0,-1):
        for pp in partitions(n-k,k):yield (k,)+pp
@lru_cache(None)
def divisors(n):return tuple(map(int,s.divisors(n)))
@lru_cache(None)
def phi(n):return int(s.totient(n))
@lru_cache(None)
def mobius(n):return int(s.mobius(n))
@lru_cache(None)
def ramanujan(d,j):
    r=d//gcd(d,j)
    return mobius(r)*phi(d)//phi(r)
def check_bound(a,pp,mult):
    t=sum(pp);e=a**t;c=len(pp);index=t-c
    maximum=max(mult);left=t*maximum-c*e
    assert left<=0 or left*left<=index*index*e,(a,pp,maximum)
    if index:assert 2*a*(e-maximum)>=(a-1)*e
pure_cases=phase_orders=equalities=0
for t in range(2,25):
 for pp in partitions(t):
  order=lcm(*pp);ds=divisors(order)
  for a in (2,3,5):
    chars={d:a**sum(gcd(k,order//d) for k in pp) for d in ds}
    mult={}
    for target in ds:
        numerator=sum(chars[d]*ramanujan(d,order//target) for d in ds)
        assert numerator%order==0
        mult[target]=numerator//order
    assert min(mult.values())>=0
    assert sum(phi(d)*m for d,m in mult.items())==a**t
    check_bound(a,pp,mult.values())
    left=t*max(mult.values())-len(pp)*a**t
    if left>=0 and left*left==(t-len(pp))**2*a**t:equalities+=1
    pure_cases+=1;phase_orders+=len(mult)
weighted_cases=word_orbits=word_points=0
for t in range(2,8):
 for pp in partitions(t):
  permutation=[];offset=0
  for length in pp:
    permutation.extend(offset+(j+1)%length for j in range(length));offset+=length
  order=lcm(*pp)
  for a in (2,3):
   for p in (3,5):
    grid=p*order;mult=Counter();remaining=set(product(range(a),repeat=t))
    word_points+=len(remaining)
    while remaining:
        first=next(iter(remaining));word=first;length=0;phase=0
        while word in remaining:
            remaining.remove(word);length+=1
            phase+=sum((i+1)*(value+1)**2 for i,value in enumerate(word))
            image=[None]*t
            for i,value in enumerate(word):image[permutation[i]]=value
            word=tuple(image)
        assert word==first and order%length==0
        for j in range(length):mult[(phase*(order//length)+j*(grid//length))%grid]+=1
        word_orbits+=1
    assert sum(mult.values())==a**t
    check_bound(a,pp,mult.values());weighted_cases+=1
for t in range(5,201):assert 2**t>t*t and 2**t>6*t
a=comb(100,4)-comb(100,3)
assert 3*100**2<5*(100-8)**2 and 4*95*10<99*98
assert 2*a>max(4,(5*a+3)//4-1)
proof=R/'tensor_count_scalar_bound_section.tex';text=proof.read_text()
assert '+n+' not in text
assert text.count('\\begin{proof}')==text.count('\\end{proof}')==3
assert text.count('\\[')==text.count('\\]')==12
result={'status':'PASS','started_utc':stamp,'elapsed_seconds':time.perf_counter()-start,
        'pure_tensor_partition_cases':pure_cases,'primitive_phase_order_entries':phase_orders,
        'sharp_bound_equalities':equalities,'actual_weighted_tensor_cases':weighted_cases,
        'actual_weighted_word_points':word_points,'actual_weighted_word_orbits':word_orbits,
        'strictness_profile':{'natural_n':100,'label':[96,4],'factor_degree':a,'old_permitted_t':2*a,'new_max_t':max(4,(5*a+3)//4-1)},
        'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Exact finite spectra, weighted word orbits and elementary arithmetic supplement the universal proofs. No finite Nielsen classification is claimed.'}
(R/'tensor_count_scalar_bound_checked.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
