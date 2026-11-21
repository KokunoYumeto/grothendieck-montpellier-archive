#!/usr/bin/env python3
"""Independent exact finite reconstruction for HD-AST04--06.

Uses integer cyclic group-ring convolution and three-letter rotation
orbits, not the author's phase-Counter/two-factor-swap implementation.
No author code is imported. The conductor theorem itself is a cited
primary-source input, not something numerically certified here.
"""
from datetime import datetime, timezone
from hashlib import sha256
from math import gcd, lcm
from pathlib import Path
import json
import time

start=time.perf_counter()
proof=Path(__file__).resolve().parents[3]/"research"/"alternating_standard_conductor_section.tex"
assert proof.exists(),str(proof)

def primes(n):
    answer=[]
    d=2
    while d*d<=n:
        if n%d==0:
            answer.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:answer.append(n)
    return answer

def phi(n):
    value=n
    for p in primes(n):value=value//p*(p-1)
    return value

def mu(n):
    out=1
    for p in primes(n):
        if n%(p*p)==0:return 0
        out=-out
    return out

def deleted_cycle_polynomial(lengths):
    order=lcm(*lengths)
    counts=[0]*order
    for d in lengths:
        for j in range(d):counts[j*(order//d)]+=1
    counts[0]-=1
    assert min(counts)>=0
    return order,counts

def convolution(x,y):
    assert len(x)==len(y)
    n=len(x); out=[0]*n
    for i,a in enumerate(x):
        if a:
            for j,b in enumerate(y):
                if b:out[(i+j)%n]+=a*b
    return out

def rotated_cube(order,counts):
    # The weighted three-factor cycle has one-dimensional constant-word
    # orbits and length-three orbits for every remaining basis word.
    ordered=convolution(convolution(counts,counts),counts)
    constants_by_product=[0]*order
    result=[0]*(3*order)
    for j,m in enumerate(counts):
        constants_by_product[(3*j)%order]+=m
        result[(3*j)%(3*order)]+=m
    for product in range(order):
        remainder=ordered[product]-constants_by_product[product]
        assert remainder>=0 and remainder%3==0
        orbits=remainder//3
        for root in range(3):
            result[product+root*order]+=orbits
    return 3*order,result

def rational_trace(order,counts):
    equal={}
    for j,m in enumerate(counts):
        d=order//gcd(order,j)
        if d in equal:assert equal[d]==m
        else:equal[d]=m
    return sum(mu(d)*m for d,m in equal.items())

counts={"selected_deleted_spectra":0,"one_active_in_three_factors":0,
        "three_active_tensor_spectra":0,"weighted_three_cycles":0,
        "scalar_generating_quadruples":0,"prime_cutoff_integers":0}
sharp_fourth_root=[]
def check_operator(order,spectrum,a,e):
    assert sum(spectrum)==e
    rational_trace(order,spectrum)
    squared=[0]*order
    for j,m in enumerate(spectrum):squared[(2*j)%order]+=m
    assert a*rational_trace(order,squared)>=-e
    for j,m in enumerate(spectrum):
        d=order//gcd(order,j)
        assert phi(d)*m<=e
        if 6%d!=0:assert 4*a*m<=(a+1)*e
        if d%8==0:assert 4*m<=e
        for p in primes(d):
            if p!=2:assert (p-1)*m<=e

for n in range(8,25):
    a=n-1;e=a**3
    patterns={(1,)*n,(2,)+(1,)*(n-2)}
    for d in (3,4,5,6,8,12):
        if d<=n:patterns.add((d,)*(n//d)+(1,)*(n%d))
    for lengths in sorted(patterns):
        order,base=deleted_cycle_polynomial(lengths)
        assert sum(base)==a
        counts["selected_deleted_spectra"]+=1
        active=[m*a*a for m in base]
        check_operator(order,active,a,e)
        counts["one_active_in_three_factors"]+=1
        cubed=convolution(convolution(base,base),base)
        check_operator(order,cubed,a,e)
        counts["three_active_tensor_spectra"]+=1
        ro,rs=rotated_cube(order,base)
        check_operator(ro,rs,a,e)
        counts["weighted_three_cycles"]+=1
        if all(d==4 for d in lengths):
            assert 4*a*active[order//4]==(a+1)*e
            sharp_fourth_root.append(n)

for M in (4,8,12,20,28,40):
    for x in range(M):
        for y in range(M):
            for z in range(M):
                w=(-x-y-z)%M
                if gcd(gcd(gcd(x,y),z),M)!=1:continue
                values=(x,y,z,w)
                orders=[M//gcd(v,M) for v in values]
                assert sum(6%d!=0 for d in orders)>=2
                for p in primes(M):
                    assert sum(v%p!=0 for v in values)>=2
                if M%8==0:assert sum(d%8==0 for d in orders)>=2
                counts["scalar_generating_quadruples"]+=1

for a in range(14,19):assert a*(19-a)>12
for a in range(14,20):assert a*(20-a)>12
cutoffs={}
for p in (7,11,19,43,67,163):
    h=p-1
    for a in range(14,5*h):
        assert a*(5*h-a)>3*h
        counts["prime_cutoff_integers"]+=1
    cutoffs[p]=5*h+1
assert [cutoffs[p] for p in (7,11,19,43,67,163)]==[31,51,91,211,331,811]
assert 196*(4*14+28)<= (2*196+6)*(3*14)
assert 196*(3*14+19)> (2*196+6)*(2*14)

out={"status":"PASS","completed_utc":datetime.now(timezone.utc).isoformat(),
     "runtime_seconds":time.perf_counter()-start,
     "proof_sha256":sha256(proof.read_bytes()).hexdigest(),
     "script_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
     "counts":counts,"attained_fourth_root_bound_n":sharp_fourth_root,
     "odd_prime_remaining_n_min":cutoffs,
     "scope":"Finite exact spectra for t=3, scalar quadruples and cutoff arithmetic only; not a computation of the conductor theorem, a universal normalizer proof, or source existence.",
     "author_code_imported":False}
destination=Path(__file__).with_name("independent_checked.json")
destination.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
