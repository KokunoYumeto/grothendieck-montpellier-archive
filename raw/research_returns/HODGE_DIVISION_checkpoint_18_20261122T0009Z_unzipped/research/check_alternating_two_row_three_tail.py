"""Exact finite supplement to the universal HD-AT301--03 proofs."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from math import comb, gcd, lcm
from collections import Counter
import hashlib, itertools, json, time
import sympy as s

ROOT=Path(__file__).resolve().parent
START=time.perf_counter();STAMP=datetime.now(timezone.utc).isoformat()

def partitions(n, top=None):
    if not n:
        yield ()
        return
    for k in range(min(n, top or n), 1-1, -1):
        for rest in partitions(n-k, k):
            yield (k,)+rest

def fixed_counts(parts, power):
    counts=Counter()
    for length in parts:
        d=gcd(length,power)
        counts[length//d]+=d
    return counts[1],counts[2],counts[3]

def subset_orbits(parts):
    order=lcm(*parts);ds=[int(x) for x in s.divisors(order)]
    c2={};c3={}
    for d in ds:
        f,u,v=fixed_counts(parts,d)
        fixed2=comb(f,2)+u
        fixed3=comb(f,3)+f*u+v
        assert fixed3-fixed2==f*(f-1)*(f-5)//6+(f-1)*u+v
        rem2=fixed2-sum(k*c2[k] for k in c2 if d%k==0)
        rem3=fixed3-sum(k*c3[k] for k in c3 if d%k==0)
        assert rem2%d==rem3%d==0 and min(rem2,rem3)>=0
        c2[d]=rem2//d;c3[d]=rem3//d
    return ds,c2,c3

classes=entries=0;rows=[];global_margin=None
for n in range(15,30):
    a=n*(n-1)*(n-5)//6;A=F(n*n-8*n+3,6);B=F(n*(n-5),6)
    worst=None;worst_type=None;count=0
    for parts in partitions(n):
        index=n-len(parts)
        ds,c2,c3=subset_orbits(parts)
        multiplicities={d:sum(c3[k]-c2[k] for k in ds if k%d==0) for d in ds}
        assert min(multiplicities.values())>=0
        assert sum(int(s.totient(d))*m for d,m in multiplicities.items())==a
        f,u,v=fixed_counts(parts,1)
        char=f*(f-1)*(f-5)//6+(f-1)*u+v
        assert 2*char>=-n
        if index:
            support=a-max(multiplicities.values())
            margin=F(support)-A*index-B
            assert margin>=0,(n,parts,support,A*index+B)
            if worst is None or margin<worst:worst,worst_type=margin,parts
        else:
            assert multiplicities=={1:a}
        count+=1;entries+=len(ds)
    classes+=count
    rows.append({'n':n,'classes':count,'least_support_margin':str(worst),'witness':worst_type})
    if global_margin is None or worst<global_margin:global_margin=worst

# Independent direct subset cycles in selected actual permutations.
direct=0
for n in range(15,21):
    samples=[(2,)+(1,)*(n-2),(3,)+(1,)*(n-3),(n,),
             (2,)*(n//2)+(1,)*(n%2),(3,)*(n//3)+(1,)*(n%3),
             (4,)+(1,)*(n-4)]
    for parts in samples:
        perm=[];start=0
        for length in parts:
            perm.extend(start+(j+1)%length for j in range(length));start+=length
        _,c2,c3=subset_orbits(parts)
        for k,expected in ((2,c2),(3,c3)):
            remaining=set(itertools.combinations(range(n),k));actual=Counter()
            while remaining:
                first=next(iter(remaining));word=first;length=0
                while word in remaining:
                    remaining.remove(word);length+=1
                    word=tuple(sorted(perm[j] for j in word))
                assert word==first
                actual[length]+=1
            assert dict(actual)=={d:c for d,c in expected.items() if c}
            direct+=1

n,f,t=s.symbols('n f t',real=True)
a=n*(n-1)*(n-5)/6;A=(n*n-8*n+3)/6;B=n*(n-5)/6
charupper=f*(f-1)*(f-5)/6+(f-1)*(n-f)/2
cf=(f*f+(n-9)*f+(n-2)*(n-4))/6
assert s.expand(a-charupper-(n-f)*cf)==0
p=(n-f)*(f*f+(n-9)*f+2*n+5)-2*n*(n-2)
assert s.expand(p-(-f**3+9*f*f+(n*n-11*n-5)*f+9*n))==0
assert s.expand(p.subs(f,2)-(2*n*n-13*n+18))==0
assert s.expand(p.subs(f,3)-(3*n*n-24*n+39))==0
assert s.expand(p.subs(f,n-2)-2*(n*n-11*n+27))==0
assert s.expand(2*A*(n-1)+12*B-2*a-(n*n-8*n-1))==0
assert s.expand(2*A*(n-1)-2*a+(n-1)**2)==0
positive=[3*n*n-24*n+39,2*(n*n-11*n+27),2*n*n-13*n+18,
          n*n-8*n-7,2*n*n-13*n-3,a-1-2*(A+B),A+B-n/2]
x=s.symbols('x',nonnegative=True)
for expr in positive:
    poly=s.Poly(s.expand(expr.subs(n,x+15)),x)
    assert all(c>=0 for c in poly.all_coeffs()) and poly.eval(0)>0
for nn in (15,29,59,89,100,149,269,629,989,2429):
    aa=nn*(nn-1)*(nn-5)//6;bb=F(nn*(nn-5),6)
    for tt in range(2,33):
        excess=F(aa**(tt-1),tt)*(10*tt*bb-(nn-1)**2-2)
        assert excess>bb*aa**(tt-1)>6

proof=ROOT/'alternating_two_row_three_tail_section.tex'
result={'status':'PASS','started_utc':STAMP,'elapsed_seconds':time.perf_counter()-START,
        'all_partition_classes':classes,'exact_cyclotomic_multiplicity_entries':entries,
        'direct_actual_subset_cycle_checks':direct,'symbolic_identities':7,
        'universal_shifted_positive_polynomials':len(positive),'tensor_endpoint_cases':310,
        'least_support_margin':str(global_margin),'rows':rows,
        'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Exact finite spectra and polynomial identities supplement the separate universal proof; no source existence or classification inferred.'}
(ROOT/'alternating_two_row_three_tail_checked.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
