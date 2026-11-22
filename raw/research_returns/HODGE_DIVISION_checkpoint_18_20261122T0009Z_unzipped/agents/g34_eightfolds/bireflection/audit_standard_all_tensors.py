#!/usr/bin/env python3
"""AST10--12 review supplement, distinct from the author's word-orbit code.

The weighted-cycle lemma was previously authored by this reviewer and is
not claimed as an independently originated ingredient.  Here full traces
of actual monomial matrices and exact cyclotomic Fourier projection give a
different numerical reconstruction.  No sibling program/output is imported.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from itertools import combinations, combinations_with_replacement
from math import gcd, lcm
from pathlib import Path
import json
import time
import sympy as sp

started=time.perf_counter()
here=Path(__file__).resolve().parent
proof=here.parent.parent/'imprimitive/standard_all_tensors/standard_all_tensors_section.tex'
proof_hash=sha256(proof.read_bytes()).hexdigest()
assert proof_hash=='571d9d5475dbd1aadb7a68d85d39346f0bea7db6fd04d220ef881ad4e3a5a2a3'
z=sp.symbols('z')
patterns=[(4,(1,2,3)),(5,(1,2,3,4)),(2,(0,0,0,1)),
          (1,(0,0,0,0)),(3,(0,0,1,2))]
matrix_cases=matrix_words=trace_steps=fourier_targets=0
records=[]
for m,alpha in patterns:
    a=len(alpha)
    for t in range(3,7):
        size=a**t;L=m*t
        traces=[Counter() for _ in range(L)]
        for basis in range(size):
            current=basis;phase=0
            for j in range(L):
                if current==basis:traces[j][phase]+=1
                phase=(phase+alpha[current%a])%m
                current=(current%a)*a**(t-1)+current//a
                trace_steps+=1
            assert current==basis and phase==0
        phi=sp.Poly(sp.cyclotomic_poly(L,z),z,domain=sp.ZZ)
        spectrum=[]
        for target in range(L):
            coefficients=[0]*L
            for j,tr in enumerate(traces):
                for phase,count in tr.items():
                    coefficients[(t*phase-target*j)%L]+=count
            remainder=sp.Poly.from_list(coefficients[::-1],z,domain=sp.ZZ).rem(phi)
            assert remainder.is_zero or remainder.degree()==0
            numerator=int(remainder.nth(0));assert numerator%L==0
            multiplicity=numerator//L;assert multiplicity>=0
            spectrum.append(multiplicity);fourier_targets+=1
        assert sum(spectrum)==size
        R=sum(a**gcd(t,j) for j in range(1,t))
        largest_X=max(Counter(alpha).values())
        assert all(t*multiplicity<=a**(t-1)*largest_X+R for multiplicity in spectrum)
        assert all(2*multiplicity<=size+a for multiplicity in spectrum)
        if a>=4:assert R<=2*a**(t-2)
        records.append({'a':a,'t':t,'phase_order':m,'matrix_degree':size,
                        'max_eigenspace':max(spectrum),'R':R})
        matrix_cases+=1;matrix_words+=size

def profile(p):
    L=lcm(*p);values=Counter()
    for cycle in p:
        for j in range(cycle):values[j*(L//cycle)]+=1
    values[0]-=1
    return L,{k:v for k,v in values.items() if v}

tensor_cases=tensor_spectral_entries=0
for n in (15,16):
    a=n-1
    shapes=[tuple([k]+[1]*(n-k)) for k in (1,2,3,4,5,7,n)]
    shapes.append(tuple([2]*(n//2)+[1]*(n%2)))
    inputs=[(n-len(p),*profile(p)) for p in shapes]
    for t in (3,4):
        for selection in combinations_with_replacement(inputs,t):
            indices=[item[0] for item in selection];I=sum(indices)
            L=lcm(*(item[1] for item in selection));multiplicities={0:1}
            for _,denom,values in selection:
                next_counts={}
                for x,c in multiplicities.items():
                    for y,d in values.items():
                        phase=(x+y*(L//denom))%L
                        next_counts[phase]=next_counts.get(phase,0)+c*d
                multiplicities=next_counts
            assert sum(multiplicities.values())==a**t
            if I:
                pairmax=max(indices[i]+indices[j] for i,j in combinations(range(t),2))
                assert t*pairmax>=2*I and pairmax>0
                moving=a**t-max(multiplicities.values())
            else:
                # The proof's exceptional case is an actual nonidentity scalar.
                moving=a**t
            assert 2*t*moving>=a**(t-2)*(2*(n-3)*I+n*t)
            tensor_cases+=1;tensor_spectral_entries+=len(multiplicities)

# Derive the final coefficient after multiplying the rank sum by the
# positive t/a^(t-2); keep the discarded H term explicit.
n,t,H=sp.symbols('n t H',integer=True,positive=True);a=n-1
normalized=2*(t-1)*a*a+(n-3)*(2*a-H)+a*H+5*n*t-2*a-4
excess=sp.expand(normalized-2*t*a*a)
assert excess==2*H+5*n*t-6*n+2
u,v=sp.symbols('u v',nonnegative=True)
assert sp.expand(((5*t-6)*n+2-3*n*t).subs({n:15+u,t:3+v}))==2*u*v+30*v+2
assert sp.cancel(2*(3-1/a)/4+(a-1)/(2*a)+9/a-2)==8/a
endpoint_cases=0
for nn in range(15,101):
    for tt in range(3,41):
        aa=nn-1
        assert aa**(tt-2)*((5*tt-6)*nn+2)>6*tt
        assert 8*aa**(tt-1)>6
        endpoint_cases+=1

out={'status':'PASS','completed_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-started,'proof_sha256':proof_hash,
     'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'direct_trace_matrix_cases':matrix_cases,'matrix_basis_words':matrix_words,
     'direct_matrix_power_steps':trace_steps,'cyclotomic_Fourier_targets':fourier_targets,
     'actual_multifactor_standard_cases':tensor_cases,
     'actual_multifactor_spectral_entries':tensor_spectral_entries,
     'exact_source_endpoint_cases':endpoint_cases,
     'normalized_excess_after_RH':str(excess),'matrix_records':records,
     'scope':'Separate direct-matrix-trace/Fourier and actual standard multi-factor spectral reconstruction. No author imports. Reviewer previously authored the common weighted-cycle lemma; that origin is explicitly retained, not claimed independent.'}
(here/'audit_standard_all_tensors.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='matrix_records'},indent=2))
