#!/usr/bin/env python3
"""Independent actual-subset reconstruction for root HD-AT301--03.
No author checker, divisors-from-fixed-points, or exported spectra imported.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
from math import lcm
import hashlib,json,time
import sympy as s
ROOT=Path(__file__).resolve().parent
start=datetime.now(timezone.utc).isoformat();clock=time.perf_counter()
def parts(n,lo=1):
    if n==0:yield ()
    for k in range(lo,n+1):
        for rest in parts(n-k,k):yield (k,)+rest
def divisors(n):return [i for i in range(1,n+1) if n%i==0]
classes=orbits=entries=points=0;worst=None;rows=[]
for n in range(15,27):
    sets={k:list(combinations(range(n),k)) for k in (2,3)}
    indices={k:{sum(1<<i for i in cc):j for j,cc in enumerate(sets[k])} for k in (2,3)}
    a=n*(n-1)*(n-5)//6;A=F(n*n-8*n+3,6);B=F(n*(n-5),6)
    rowmin=None;rowtypes=None
    for pp in parts(n):
        permutation=[];offset=0
        for length in pp:
            permutation.extend(offset+(j+1)%length for j in range(length));offset+=length
        images=[1<<i for i in permutation];cyc={}
        for k in (2,3):
            action=[indices[k][sum(images[i] for i in cc)] for cc in sets[k]]
            seen=bytearray(len(action));cc=Counter()
            for i in range(len(action)):
                if seen[i]:continue
                j=i;length=0
                while not seen[j]:seen[j]=1;length+=1;j=action[j]
                assert j==i
                cc[length]+=1
            cyc[k]=cc;orbits+=sum(cc.values());points+=len(action)
        ds=divisors(lcm(*pp));multip=[]
        for d in ds:
            m=sum(v for k,v in cyc[3].items() if k%d==0)-sum(v for k,v in cyc[2].items() if k%d==0)
            assert m>=0;multip.append((d,m));entries+=1
        assert sum(int(s.totient(d))*m for d,m in multip)==a
        chi=cyc[3][1]-cyc[2][1]
        assert F(chi)>=-F(n,2)
        index=n-len(pp)
        if index:
            nu=a-max(m for d,m in multip);margin=F(nu)-A*index-B
            assert margin>=0,(n,pp,nu,margin)
            if rowmin is None or margin<rowmin:rowmin=margin;rowtypes=pp
            if worst is None or margin<worst:worst=margin
        classes+=1
    rows.append({'n':n,'minimum_margin':str(rowmin),'witness':rowtypes})
n,f,t,x=s.symbols('n f t x')
a=n*(n-1)*(n-5)/6;A=(n*n-8*n+3)/6;B=n*(n-5)/6
cf=(f*f+(n-9)*f+(n-2)*(n-4))/6
upper=f*(f-1)*(f-5)/6+(f-1)*(n-f)/2
assert s.expand(a-upper-(n-f)*cf)==0
c=(n*n-6*n+3)/6
assert s.expand(cf-c-(f*f+(n-9)*f+5)/6)==0
raw=6*((cf-A)*(n-f)/2-n/2-B)*2
# Twelve times the desired margin is the displayed polynomial.
p=(n-f)*(f*f+(n-9)*f+2*n+5)-2*n*(n-2)
assert s.expand(raw-p)==0
assert s.expand(s.diff(p,f,2)-(18-6*f))==0
for endpoint in (2,3,n-2):
    poly=s.Poly(s.expand(p.subs(f,endpoint).subs(n,x+15)),x)
    assert all(v>=0 for v in poly.all_coeffs()) and poly.eval(0)>0
assert s.expand(2*A*(n-1)+12*B-2*a)==n*n-8*n-1
assert s.expand(2*A*(n-1)-2*a+(n-1)**2)==0
for p0 in (a-1-2*(A+B),A+B-n/2,2*n*n-13*n-3,n*n-8*n-7):
    pp=s.Poly(s.expand(p0.subs(n,x+15)),x)
    assert all(v>=0 for v in pp.all_coeffs()) and pp.eval(0)>0
proof=ROOT.parent.parent.parent/'research/alternating_two_row_three_tail_section.tex'
result={'status':'PASS','started_utc':start,'completed_utc':datetime.now(timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-clock,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'all_actual_partition_classes':classes,'actual_subset_orbits':orbits,'actual_subset_points':points,
 'exact_cyclotomic_entries':entries,'minimum_margin':str(worst),'rows':rows,
 'scope':'Actual 2-/3-subset cycles in every class for n15..26, plus independent universal polynomial identities; universal source proof checked separately.'}
(ROOT/'audit_three_row_tail.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
