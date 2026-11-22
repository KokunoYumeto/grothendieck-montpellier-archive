#!/usr/bin/env python3
"""Exact finite supplement for D-ATT01--03.

Cycle spectra are rebuilt directly from the deleted permutation spectrum,
using its exterior and symmetric squares. This is supplemental; no finite
scan is used for the all-n theorem or the actual period factorization.
"""
from pathlib import Path
from collections import Counter, defaultdict
from itertools import combinations_with_replacement
from fractions import Fraction as F
from math import gcd,lcm
import datetime,hashlib,json,re,time

start=time.perf_counter();base=Path(__file__).resolve().parent
proof=base/'alternating_two_tail_section.tex';tex=proof.read_text()
assert tex.count(r'\[')==tex.count(r'\]')
assert re.findall(r'\\tag\{([^}]+)\}',tex)==['ATT.'+str(i) for i in range(1,18)]

def partitions(n,m=1):
    if n==0:yield ()
    for k in range(m,n+1):
        for rest in partitions(n-k,k):yield (k,)+rest

def mobius(n):
    ans=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;ans=-ans
            if n%p==0:return 0
        p+=1
    return -ans if n>1 else ans

def phi(n):
    x=n;p=2;ans=n
    while p*p<=x:
        if x%p==0:
            ans=ans//p*(p-1)
            while x%p==0:x//=p
        p+=1
    if x>1:ans=ans//x*(x-1)
    return ans

def rational_trace(spec,L):
    orbits=defaultdict(dict)
    for k,v in spec.items():
        if v:orbits[L//gcd(k,L)][k]=v
    ans=0
    for order,d in orbits.items():
        vals=set(d.values());assert len(vals)==1 and len(d)==phi(order)
        ans+=next(iter(vals))*mobius(order)
    return ans

def spectra(parts):
    n=sum(parts);L=lcm(*parts)
    p=Counter(j*(L//k) for k in parts for j in range(k))
    u=list(p.elements());u.remove(0)
    ex=Counter((x+y)%L for i,x in enumerate(u) for y in u[i+1:])
    sy=Counter((x+y)%L for i,x in enumerate(u) for y in u[i:])
    up=sy.copy();up.subtract(p)
    assert min(up.values())>=0
    up=+up
    assert sum(ex.values())==(n-1)*(n-2)//2
    assert sum(up.values())==n*(n-3)//2
    return L,up,ex

rows=0;entries=0;transpositions=[];minima={};trace_minima={}
for n in range(15,27):
    amin={'UP':n*(n-3)//2,'EX':(n-1)*(n-2)//2}
    minimum={'UP':amin['UP'],'EX':amin['EX']};trmin=minimum.copy()
    for parts in partitions(n):
        L,up,ex=spectra(parts);f1=parts.count(1);f2=parts.count(2)
        formula={'UP':f1*(f1-3)//2+f2,'EX':(f1-1)*(f1-2)//2-f2}
        for kind,spec in [('UP',up),('EX',ex)]:
            a=amin[kind];chi=rational_trace(spec,L)
            assert chi==formula[kind]
            b=1 if kind=='UP' else (n-1)//2
            assert chi>=-b
            trmin[kind]=min(trmin[kind],chi)
            if parts!=(1,)*n:
                support=a-max(spec.values())
                lower=n-3 if kind=='UP' else n-2
                assert support>=lower
                minimum[kind]=min(minimum[kind],support)
            entries+=len(spec)
        rows+=1
    assert minimum=={'UP':n-3,'EX':n-2}
    minima[n]=minimum;trace_minima[n]=trmin

def tensor_spec(S,L,T,M):
    N=lcm(L,M);out=Counter()
    for x,v in S.items():
        for y,w in T.items():out[(x*(N//L)+y*(N//M))%N]+=v*w
    return N,out

def swap_spec(S,L):
    out=Counter();items=list(S.items())
    # Constant words; each unordered nonconstant word yields its two
    # square-root eigenvalues, as an actual weighted two-cycle.
    for i,(x,v) in enumerate(items):
        out[(2*x)%(2*L)]+=v
        m=v*(v-1)//2
        out[(2*x)%(2*L)]+=m;out[(2*x+L)%(2*L)]+=m
        for y,w in items[i+1:]:
            out[(x+y)%(2*L)]+=v*w;out[(x+y+L)%(2*L)]+=v*w
    return 2*L,+out

tensor_cases=0;power_checks=0;phase_checks=0
for n in (15,16,19,20,39,40):
    cycletypes=[(1,)*n,(1,)*(n-2)+(2,), (1,)*(n-3)+(3,),
                (1,)*(n-4)+(2,2),(1,)*(n-4)+(4,), (n,),
                ((1,) if n%2 else ())+ (2,)*(n//2)]
    for kind in ('UP','EX'):
        a=n*(n-3)//2 if kind=='UP' else (n-1)*(n-2)//2
        b=1 if kind=='UP' else (n-1)//2;c=F(b,a);mu=F(2,n if kind=='UP' else n-1)
        base_specs=[(L,up if kind=='UP' else ex) for L,up,ex in map(spectra,cycletypes)]
        tests=[swap_spec(S,L) for L,S in base_specs]
        tests += [tensor_spec(S,L,T,M) for L,S in base_specs for M,T in base_specs]
        for N,spec in tests:
            assert sum(spec.values())==a*a
            if max(spec.values())<a*a:assert a*a-max(spec.values())>=mu*a*a
            else:assert spec==Counter({0:a*a})
            for k,v in spec.items():
                order=N//gcd(k,N)
                assert phi(order)*v<=a*a
                if 6%order:assert 4*v<= (1+c)*a*a
                if order%8==0:assert 4*v<=a*a
                phase_checks+=1
            for r in range(N):
                power=Counter()
                for k,v in spec.items():power[(r*k)%N]+=v
                tr=rational_trace(power,N)
                assert tr>=-b*a
                power_checks+=1
            tensor_cases+=1

arithmetic=[]
for kind in ('UP','EX'):
    for n in range(15,41):
        a=n*(n-3)//2 if kind=='UP' else (n-1)*(n-2)//2
        b=1 if kind=='UP' else (n-1)//2
        mu=F(2,n if kind=='UP' else n-1)
        ordinary=(10*mu-F(1,2)-F(b,2*a))*a*a
        eight=(10*mu-F(1,2))*a*a
        if n<=39:assert ordinary>6
        if n<=39 or kind=='EX':assert eight>6
        arithmetic.append({'kind':kind,'n':n,'ordinary_coefficient_times_a2':str(ordinary),
                           'conductor8_coefficient_times_a2':str(eight)})

field_ranges=[]
for p in (7,11,19,43,67,163):
    h=p-1
    for kind in ('UP','EX'):
        endpoint=10*h-1 if kind=='UP' else 10*h
        for n in range(15,endpoint+1):
            a=n*(n-3)//2 if kind=='UP' else (n-1)*(n-2)//2
            mu=F(2,n if kind=='UP' else n-1)
            assert (10*mu-F(2,h))*a*a>6
        # At the next integer the coefficient itself vanishes; no
        # extension of this inequality-only range is claimed.
        assert 10*F(2,endpoint+1 if kind=='UP' else endpoint)-F(2,h)==0
        field_ranges.append({'kind':kind,'p':p,'last_excluded_n':endpoint})

# Universal endpoint inequalities in h>=6, represented as shifted
# linear polynomials with positive coefficients.
assert (140*6-224)>0 and (130*6-195)>0
assert 144*(10*6-1)>12*6 and 169*(10*6-1)>12*6
assert 144*10>12 and 169*10>12
assert F(36,703)<F(1,10)
out={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-start,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'all_cycle_types_n15_26':rows,'spectral_entries':entries,'exact_minima':minima,'minimum_traces':trace_minima,
 'actual_tensor_and_swap_cases':tensor_cases,'all_power_trace_checks':power_checks,
 'scalar_eigenvalue_checks':phase_checks,'finite_range_arithmetic':arithmetic,
 'prime_conductor_ranges':field_ranges,
 'scope':'Exact finite spectra, actual tensor swaps and arithmetic only; all-degree inequalities, full normalizers, field containment and period factorization proved in TeX.'}
(base/'alternating_two_tail_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('finite_range_arithmetic','exact_minima','minimum_traces')},indent=2))
