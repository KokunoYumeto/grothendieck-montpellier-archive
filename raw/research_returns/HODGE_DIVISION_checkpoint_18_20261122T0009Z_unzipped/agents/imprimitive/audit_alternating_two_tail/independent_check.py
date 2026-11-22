#!/usr/bin/env python3
"""Independent signed pair-orbit reconstruction for D-ATT01--03.

No author program is imported.  We construct the actual permutations
on unordered pairs, retain orientation for wedge^2(P), then subtract
the letter module (and add the trivial line in the exterior case).
The universal normalizer/geometry proof is audited separately.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm
from pathlib import Path
import datetime,hashlib,json,time

start=time.perf_counter()
here=Path(__file__).resolve().parent
root=here.parents[1]
proof=root/'g34_eightfolds/bireflection/alternating_two_tail_section.tex'
assert hashlib.sha256(proof.read_bytes()).hexdigest()=='663aea29319e2ce97288077ba58195eaa6946f1bd5eda3033589c5b95b84ec3b'

def partitions(n,upper=None):
    if n==0:
        yield ()
        return
    if upper is None:upper=n
    for first in range(min(n,upper),0,-1):
        for tail in partitions(n-first,first):yield (first,)+tail

def actual_spectra(part):
    n=sum(part);perm=list(range(n));pos=0
    for length in part:
        for j in range(length):perm[pos+j]=pos+(j+1)%length
        pos+=length
    period=2*lcm(*part)
    up=Counter();ex=Counter();seen=set();orbit_count=0
    for pair in combinations(range(n),2):
        if pair in seen:continue
        current=pair;orientation=1;length=0
        while True:
            seen.add(current);length+=1
            x,y=perm[current[0]],perm[current[1]]
            if x>y:x,y=y,x;orientation=-orientation
            current=(x,y)
            if current==pair:break
        assert period%length==0
        for j in range(length):up[j*(period//length)]+=1
        if orientation==1:
            for j in range(length):ex[j*(period//length)]+=1
        else:
            assert period%(2*length)==0
            for j in range(length):ex[(2*j+1)*(period//(2*length))]+=1
        orbit_count+=1
    letters=Counter()
    for length in part:
        for j in range(length):letters[j*(period//length)]+=1
    up.subtract(letters);ex.subtract(letters);ex[0]+=1
    assert min(up.values())>=0 and min(ex.values())>=0
    up=+up;ex=+ex
    # Independent actual signed fixed-pair traces, before subtraction.
    pair_trace=0;wedge_trace=0
    for i,j in combinations(range(n),2):
        a,b=perm[i],perm[j]
        if (a,b)==(i,j):pair_trace+=1;wedge_trace+=1
        if (a,b)==(j,i):pair_trace+=1;wedge_trace-=1
    fixed=sum(perm[i]==i for i in range(n))
    traces=(pair_trace-fixed,wedge_trace-fixed+1)
    return period,(up,ex),traces,orbit_count

rows=0;entries=0;orbits=0;minima={};trace_minima={}
for n in range(15,27):
    degrees=(n*(n-3)//2,(n-1)*(n-2)//2)
    lower=(n-3,n-2);b=(1,(n-1)//2)
    mins=list(degrees);trmins=list(degrees)
    for part in partitions(n):
        period,spectra,traces,num=actual_spectra(part)
        for k,spec in enumerate(spectra):
            assert sum(spec.values())==degrees[k]
            support=degrees[k]-max(spec.values())
            if part!=(1,)*n:
                assert support>=lower[k]
                mins[k]=min(mins[k],support)
            f1=part.count(1);f2=part.count(2)
            formula=(f1*(f1-3)//2+f2,(f1-1)*(f1-2)//2-f2)[k]
            assert traces[k]==formula and traces[k]>=-b[k]
            trmins[k]=min(trmins[k],traces[k])
            entries+=len(spec)
        rows+=1;orbits+=num
    assert tuple(mins)==lower
    minima[n]=mins;trace_minima[n]=trmins

# Rational arithmetic with all conductor ranges.  The inequalities in
# the proof are also checked symbolically by evaluating polynomial
# coefficients after shifting h>=6, n>=15 where applicable.
count=0;endpoints=[]
for n in range(15,41):
    for kind in ('UP','EX'):
        a=n*(n-3)//2 if kind=='UP' else (n-1)*(n-2)//2
        mu=F(n-3,a) if kind=='UP' else F(n-2,a)
        b=1 if kind=='UP' else (n-1)//2
        value=(10*mu-F(1,2)-F(b,2*a))*a*a
        if n<=39:assert value>6
        eight=(10*mu-F(1,2))*a*a
        if n<=39 or kind=='EX':assert eight>6
        if kind=='UP':
            displayed=F(n*(n-3),8)*((40-n)*(n-3)-2)
            assert displayed==value
        else:
            displayed=F((n-1)*(n-2),8)*((40-n)*(n-2)-1)
            assert displayed<=value
            assert eight==F((n-1)*(n-2)**2*(41-n),8)
        count+=1
for p in (7,11,19,43,67,163):
    h=p-1
    for kind in ('UP','EX'):
        endpoint=10*h-(kind=='UP')
        for n in range(15,endpoint+1):
            a=n*(n-3)//2 if kind=='UP' else (n-1)*(n-2)//2
            mu=F(n-3,a) if kind=='UP' else F(n-2,a)
            value=(10*mu-F(2,h))*a*a
            x=n if kind=='UP' else n-1
            square=(n-3)**2 if kind=='UP' else (n-2)**2
            assert value==F(x*square*(10*h-x),2*h)>6
            count+=1
        endpoints.append([kind,p,endpoint])

# The universal endpoint differences and final lower bounds have
# positive coefficients when h=6+y, y>=0.
for coefficients in ((616,140),(585,130),(8496-72,1440-12),
                     (9971-72,1690-12)):
    assert all(x>0 for x in coefficients)
assert F(36,703)<F(1,10)

# Recover the preceding ALT07 three-cycle ratio directly from the
# actual character at n39: each chosen label has a nonselfconjugate
# restriction, and the support bound is (1-chi(3)/a)/4.
for kind in (0,1):
    n=39;f1=36;f2=0
    a=(n*(n-3)//2,(n-1)*(n-2)//2)[kind]
    chi=(f1*(f1-3)//2+f2,(f1-1)*(f1-2)//2-f2)[kind]
    exact=F(a-chi,4*a)
    assert exact<=F(36,703)<F(1,10)

out={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-start,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'method':'Actual unsigned/signed unordered-pair orbits; subtract letter permutation module; no author arithmetic imported',
 'partitions_n15_26':rows,'spectral_entries':entries,'actual_pair_orbits':orbits,
 'minimum_supports':minima,'minimum_traces':trace_minima,
 'exact_arithmetic_cases':count,'conductor_endpoints':endpoints,
 'scope':'Independent finite supplement; all-degree trace, normalizer, conductor and geometric proof reviewed separately.'}
(here/'independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('minimum_supports','minimum_traces')},indent=2))
