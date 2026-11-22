#!/usr/bin/env python3
"""Exact supplement to ATT07--09; universal and geometric proofs are separate."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations, product
from math import gcd
from pathlib import Path
import json
import time

started=time.perf_counter()
here=Path(__file__).resolve().parent
proof=here/'alternating_two_tail_all_tensors_section.tex'
proof_hash=sha256(proof.read_bytes()).hexdigest()
assert proof_hash in {'90a4a0266b9bf0ac090a420212239639da53a1faa2205018464a11ba3d9278ef', '2e9afd9be79f01ee143291b73619837be11182569bccc0234bfb66d45c73372b'}

def error(a,t):
    return sum(a**gcd(t,j) for j in range(1,t))

error_cases=0
for a in range(4,101):
    for t in range(3,81):
        assert error(a,t)<=2*a**(t-2)
        error_cases+=1
assert all(error(a,3)==2*a and error(a,4)==a*a+2*a for a in range(2,101))

# Actual weighted word orbits.  A rotation takes the last letter to the
# first, with its specified root-of-unity weight.  Each orbit gives the
# roots of its own cyclic characteristic polynomial, with no approximation.
patterns=[(4,1,(0,0,0,0)),(4,4,(0,0,1,1)),(4,5,(0,1,2,3)),
          (4,3,(0,1,1,2)),(5,6,(0,0,1,2,5)),(6,4,(0,0,1,1,2,3))]
orbit_cases=word_count=word_orbits=short_orbits=eigenvalue_checks=0
records=[]
for a,m,alpha in patterns:
    for t in range(3,9 if a==4 else 7):
        L=m*t
        seen=set();spectrum=Counter();observed_error=0;local_orbits=0
        for word in product(range(a),repeat=t):
            if word in seen:continue
            current=word;phase=0;d=0
            while current not in seen:
                seen.add(current);phase+=alpha[current[-1]];d+=1
                current=(current[-1],)+current[:-1]
            assert current==word and t%d==0
            local_orbits+=1
            if d<t:short_orbits+=1
            observed_error+=t-d
            start_phase=((t//d)*phase)%L
            for j in range(d):spectrum[(start_phase+j*(L//d))%L]+=1
        assert len(seen)==a**t and sum(spectrum.values())==a**t
        assert observed_error==error(a,t)
        counts=Counter(v%m for v in alpha)
        convolution=Counter({0:1})
        for _ in range(t):
            new=Counter()
            for u,c in convolution.items():
                for v,d in counts.items():new[(u+v)%m]+=c*d
            convolution=new
        max_product=max(counts.values())
        for k in range(L):
            assert t*spectrum[k]<=convolution[k%m]+observed_error
            assert convolution[k%m]<=a**(t-1)*max_product
            assert t*(a**t-spectrum[k]) >= (t-1)*a**t+a**(t-1)*(a-max_product)-observed_error
            eigenvalue_checks+=1
        if a==4 and m==1 and t==8:
            assert spectrum[1]>0
            identity_eighth_root_multiplicity=spectrum[1]
        records.append({'a':a,'t':t,'phase_order':m,'weights':list(alpha),
                        'words':a**t,'orbits':local_orbits,'R':observed_error,
                        'largest_eigenspace':max(spectrum.values())})
        orbit_cases+=1;word_count+=a**t;word_orbits+=local_orbits

def cycles(p):
    seen=set();out=[]
    for i in range(len(p)):
        if i in seen:continue
        j=i;length=0
        while j not in seen:seen.add(j);j=p[j];length+=1
        assert j==i
        out.append(length)
    return sorted(out)

permutation_cases=0
for n in (2,3):
    choices=list(permutations(range(n)))
    for t in (3,4):
        for x in product(choices,repeat=t):
            actual=[]
            fixed=[]
            for j in range(t):
                for k in range(n):
                    actual.append(((j+1)%t)*n+x[(j+1)%t][k])
                    fixed.append(j*n+x[j][k])
            h=[]
            for k in range(n):
                j=k
                for _ in range(t):j=actual[j]
                assert 0<=j<n
                h.append(j)
            assert cycles(actual)==[t*l for l in cycles(h)]
            assert n*t-len(cycles(actual))==n*(t-1)+n-len(cycles(h))
            assert n*t-len(cycles(fixed))==sum(n-len(cycles(y)) for y in x)
            permutation_cases+=1

arithmetic_cases=active_factor_checks=0
for n in range(15,101):
    for label in ('UP','EX'):
        if label=='UP':a=n*(n-3)//2;d0=n-3;b0=1;kappa=5
        else:a=(n-1)*(n-2)//2;d0=n-2;b0=(n-1)//2;kappa=3
        A=F(n-5,2);B=F(n,4)
        assert a>=90 and 2*d0<=a-1 and b0<=d0 and B<a
        for t in range(3,31):
            e=a**t
            forced_excess=a**(t-1)*(9*d0-F(b0+1,2))
            assert forced_excess>6
            raw=A*(2*n-2)+10*t*B-2*a-F(4,a)
            simplified=(F(5*t,2)-3)*n+kappa-F(4,a)
            assert raw==simplified
            excess=F(a**(t-1),t)*raw
            assert excess>F(3*n*a**(t-1),2)>6
            for active in range(1,t+1):
                I=active*(n-1)
                assert A*I/active+B>=A*I/t+B
                active_factor_checks+=1
            arithmetic_cases+=1

out={'status':'PASS','completed_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-started,'proof_sha256':proof_hash,
     'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'short_error_grid_cases':error_cases,'weighted_cycle_cases':orbit_cases,
     'actual_words':word_count,'actual_word_orbits':word_orbits,
     'short_orbits':short_orbits,'eigenvalue_inequalities':eigenvalue_checks,
     'identity_cycle_primitive_eighth_root_multiplicity':identity_eighth_root_multiplicity,
     'actual_nt_letter_permutation_cases':permutation_cases,
     'source_arithmetic_cases':arithmetic_cases,'active_factor_checks':active_factor_checks,
     'weighted_cycle_records':records,
     'scope':'Exact finite weighted-word spectra, all short-orbit defects, actual imprimitive quotient indices and source-constant arithmetic. No tuple enumeration, universal-bound extrapolation, or geometric existence claim.'}
(here/'alternating_two_tail_all_tensors_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='weighted_cycle_records'},indent=2))
