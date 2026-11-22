"""Exact character/Fourier and actual-flag supplement for HD-MT301--03."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import gcd,lcm
from collections import Counter
from functools import lru_cache
import hashlib,itertools,json,time
import sympy as s
ROOT=Path(__file__).resolve().parent
START=time.perf_counter();STAMP=datetime.now(timezone.utc).isoformat()

def partitions(n,top=None):
    if not n:
        yield ();return
    for k in range(min(n,top or n),0,-1):
        for rest in partitions(n-k,k):yield (k,)+rest

@lru_cache(None)
def divs(n):return tuple(int(x) for x in s.divisors(n))
@lru_cache(None)
def phi(n):return int(s.totient(n))
@lru_cache(None)
def mu(n):return int(s.mobius(n))
@lru_cache(None)
def ramanujan(order,k):
    quotient=order//gcd(order,k)
    return mu(quotient)*phi(order)//phi(quotient)

def counts(parts,power):
    result=Counter()
    for length in parts:
        split=gcd(length,power);result[length//split]+=split
    return result

def character(parts,power):
    c=counts(parts,power);f,v=c[1],c[3]
    return f*(f-2)*(f-4)//3-v

def spectrum(parts):
    order=lcm(*parts);ds=divs(order)
    chars={d:character(parts,order//d) for d in ds}
    out={}
    for target in ds:
        numerator=sum(chars[d]*ramanujan(d,order//target) for d in ds)
        assert numerator%order==0
        out[target]=numerator//order
    return out

classes=entries=0;rows=[]
for n in range(15,30):
    a=n*(n-2)*(n-4)//3;A=F(n*n-8*n+8,3);B=F(n*(n-3),3)
    worst=None;witness=None;count=0
    for parts in partitions(n):
        mult=spectrum(parts)
        assert min(mult.values())>=0
        assert sum(phi(d)*m for d,m in mult.items())==a
        assert 3*character(parts,1)>=-n
        index=n-len(parts)
        if index:
            margin=F(a-max(mult.values()))-A*index-B
            assert margin>=0,(n,parts,margin)
            if worst is None or margin<worst:worst,witness=margin,parts
        else:assert mult=={1:a}
        count+=1;entries+=len(mult)
    classes+=count
    rows.append({'n':n,'classes':count,'least_support_margin':str(worst),'witness':witness})

def orbit_counts(points,action):
    remaining=set(points);out=Counter()
    while remaining:
        first=next(iter(remaining));word=first;length=0
        while word in remaining:
            remaining.remove(word);length+=1;word=action(word)
        assert word==first
        out[length]+=1
    return out

actual_cases=actual_points=actual_orbits=0
for n in range(15,21):
    for parts in [(2,)+(1,)*(n-2),(3,)+(1,)*(n-3),(n,),
                  (2,)*(n//2)+(1,)*(n%2),(3,)*(n//3)+(1,)*(n%3)]:
        perm=[];start=0
        for length in parts:
            perm.extend(start+(j+1)%length for j in range(length));start+=length
        flags=[(i,j,k) for i in range(n) for j,k in itertools.combinations(range(n),2) if i not in (j,k)]
        triples=list(itertools.combinations(range(n),3))
        pairs=list(itertools.permutations(range(n),2));letters=list(range(n))
        virtual=Counter()
        actions=[(flags,lambda x:(perm[x[0]],)+tuple(sorted((perm[x[1]],perm[x[2]]))),1),
                 (triples,lambda x:tuple(sorted(perm[i] for i in x)),-1),
                 (pairs,lambda x:(perm[x[0]],perm[x[1]]),-1),
                 (letters,lambda x:perm[x],1)]
        for points,action,sign in actions:
            cycles=orbit_counts(points,action)
            actual_points+=len(points);actual_orbits+=sum(cycles.values())
            for d,c in cycles.items():virtual[d]+=sign*c
        for d,m in spectrum(parts).items():
            assert sum(c for length,c in virtual.items() if length%d==0)==m
        actual_cases+=1

n,f=s.symbols('n f',real=True)
a=n*(n-2)*(n-4)/3;A=(n*n-8*n+8)/3;B=n*(n-3)/3
cf=(n*n+n*f+f*f-6*n-6*f+8)/3
assert s.expand(a-f*(f-2)*(f-4)/3-(n-f)*cf)==0
assert s.expand(f*(f-2)*(f-4)+f-f*(f-3)**2)==0
p=(n-f)*(f*f+(n-6)*f+2*n)-2*n*(n-2)
assert s.expand(p-(-f**3+6*f*f+(n*n-8*n)*f+4*n))==0
assert s.expand(p.subs(f,2)-2*(n-2)*(n-4))==0
assert s.expand(p.subs(f,n-2)-2*(n-4)**2)==0
assert s.expand(2*A*(n-1)+12*B-2*a-(6*n*n-20*n-16)/3)==0
assert s.expand(2*A*(n-1)-2*a+(6*n*n-16*n+16)/3)==0
assert s.expand(18*B-(6*n*n-16*n+16)/3-2-(12*n*n-38*n-22)/3)==0
positive=[A,B-6,a-1-2*(A+B),A+B-n/3,A+B-97,
          (6*n*n-20*n-16)/3-6,(12*n*n-38*n-22)/3,a-B]
x=s.symbols('x',nonnegative=True)
for expr in positive:
    poly=s.Poly(s.expand(expr.subs(n,x+15)),x)
    assert all(c>=0 for c in poly.all_coeffs()) and poly.eval(0)>0

proof=ROOT/'alternating_mixed_three_tail_section.tex'
result={'status':'PASS','started_utc':STAMP,'elapsed_seconds':time.perf_counter()-START,
        'partition_classes':classes,'exact_Fourier_entries':entries,
        'actual_flag_virtual_character_cases':actual_cases,
        'actual_permutation_points':actual_points,'actual_permutation_orbits':actual_orbits,
        'symbolic_identities':8,'universal_shifted_positive_polynomials':len(positive),'rows':rows,
        'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Finite exact cyclic spectra and actual flag/permutation models, plus polynomial identities; universal proofs remain written separately.'}
(ROOT/'alternating_mixed_three_tail_checked.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
