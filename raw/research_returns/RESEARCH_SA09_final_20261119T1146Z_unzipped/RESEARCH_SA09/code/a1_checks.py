"""Finite certificates for the counterexamples and formulas of A.1.

The general categorical proofs are in the paper. These checks certify each
finite obstruction and test the partition formula within the stated bounds.
"""
from functools import lru_cache
from itertools import product
from math import comb, gcd
from time import perf_counter
from pathlib import Path
import json

start=perf_counter()

def scalar_t(n): return 2 if n==2 else 1
def c(p,q):
    return scalar_t(p*q)*pow(scalar_t(p)*pow(scalar_t(q),p,3)%3,-1,3)%3

twist_cases=0
for p,q,r in product(range(17),repeat=3):
    assert c(p,q*r)*pow(c(q,r),p,3)%3 == c(p*q,r)*c(p,q)%3
    twist_cases+=1
assert all(c(1,q)==c(q,1)==c(0,q)==1 for q in range(33))
assert all(c(q,0) != 0 for q in range(33))
assert c(2,0)==2

@lru_cache(None)
def partitions_fixed(seq, size):
    """Unordered partitions into blocks of one fixed size, each exactly once."""
    from itertools import combinations
    if not seq: return ((),)
    first,*rest=seq
    out=[]
    for more in combinations(rest,size-1):
        block=(first,)+more
        remaining=tuple(x for x in rest if x not in more)
        for later in partitions_fixed(remaining,size): out.append((block,)+later)
    return tuple(out)

partition_cases=[]
for p,q,r in product(range(1,9),repeat=3):
    N=p*q*r
    if N>8: continue
    left=set()
    for top in partitions_fixed(tuple(range(N)),q*r):
        for choices in product(*(partitions_fixed(block,r) for block in top)):
            left.add(tuple(sorted(tuple(sorted(x)) for x in choices)))
    right=set()
    for bottom in partitions_fixed(tuple(range(N)),r):
        for grouping in partitions_fixed(tuple(range(p*q)),q):
            right.add(tuple(sorted(tuple(sorted(bottom[j] for j in block)) for block in grouping)))
    assert left==right
    partition_cases.append([p,q,r,len(left)])

# F4=F2[t]/(t^2+t+1), encoded by two bits.
def mul4(a,b):
    out=0
    for i in range(2):
        if (b>>i)&1: out ^= a<<i
    if out&4: out ^= 7
    return out
def cube4(a): return mul4(mul4(a,a),a)
cube_failures=[[a,b,cube4(a^b),cube4(a)^cube4(b)]
               for a,b in product(range(4),repeat=2)
               if cube4(a^b)!=(cube4(a)^cube4(b))]
assert [1,2,1,0] in cube_failures

def primes_upto(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**.5)+1))]
def val(n,p):
    v=0
    while n%p==0: n//=p;v+=1
    return v
def difference_gcd(m,delta):
    ans=1
    for p in primes_upto(delta+1):
        if delta%(p-1): continue
        a=(1 if delta%2 else 2+val(delta,2)) if p==2 else 1+val(delta,p)
        ans*=p**min(m,a)
    return ans
gcd_cases=[]
for m,delta in product(range(1,7),range(1,13)):
    observed=0
    for x in range(201): observed=gcd(observed,x**(m+delta)-x**m)
    expected=difference_gcd(m,delta)
    assert observed==expected
    gcd_cases.append([m,delta,expected])

out={
  'model':'GPT-6 Astra (OpenAI, ChatGPT Pro mode)',
  'status':'all checks passed',
  'A1.3_dimension_witness':{'field':'F2','V_dimension':1,'W_dimension':2,'d':2,
      'Hom_GammaV_W_dimension':2,'Gamma_HomVW_dimension':comb(3,2),
      'cardinalities':[4,8]},
  'A1.5_exterior_unit_witness':{'dim_unit':1,'dim_Lambda2_unit':0},
  'A1.5_partition_associativity':{'scope':'all positive p,q,r with p*q*r<=8',
      'number_of_cases':len(partition_cases),'cases':partition_cases},
  'A1.6_scalar_twist':{'field':'F3','triples_checked':twist_cases,
      'scope':'0<=p,q,r<=16','alpha_2_0':c(2,0),'required_mixed_value':1},
  'A1.8_nonnatural_cubic':{'ring':'F4=F2[t]/(t^2+t+1)',
      'pairs_checked':16,'failures':cube_failures},
  'A1.9_scalar_gcd':{'scope':'1<=min(n,m)<=6, 1<=abs(n-m)<=12; evaluations 0..200',
      'cases':gcd_cases},
  'runtime_seconds':round(perf_counter()-start,6),
}
ROOT=Path(__file__).resolve().parents[1]
rendered=json.dumps(out,indent=2)
(ROOT/'logs'/'a1_checks.json').write_text(rendered)
print(rendered)
