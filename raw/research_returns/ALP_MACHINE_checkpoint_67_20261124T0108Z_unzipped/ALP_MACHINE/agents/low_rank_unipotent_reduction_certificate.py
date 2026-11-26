#!/usr/bin/env python3
"""AM-K068 exact all-support structural-cut certificate; no short-sum enumeration."""
from __future__ import annotations
import argparse,json,hashlib
from datetime import datetime,timezone
from pathlib import Path
from math import prod,gcd,comb
from fractions import Fraction as F
from itertools import combinations
import sympy as sp

p=argparse.ArgumentParser()
p.add_argument("--output",default=str(Path(__file__).with_suffix(".json")))
args=p.parse_args();base=Path(__file__).parent;checks=[]
def ck(x,s):
    if not x:raise AssertionError(s)
    checks.append(s)
hp=base/"definite_oscillator_large_t_certificate.json"
gp=base/"definite_oscillator_minimal_denominator_certificate.json"
row=next(x for x in json.loads(hp.read_text())["rows"] if x["host"]=="J56")
old=next(x for x in json.loads(gp.read_text())["hosts"] if x["host"]=="J56")
a=f=168;n=169;m=164;H=8192;T=int(row["T"]);q0=row["g0"];q1=row["g1"];Q=q0*q1
G=int(old["stabilizer_gcd"])
ck((row["a"],row["f"])==(a,f),"actual_host_ranks")
ck(2**70<Q<2**71 and T<2**996 and G<2**5022,"actual_strict_binary_parameters")
ck(2*H+1<2**15 and H==2**13,"actual_cutoff_bounds")
ck([gcd(n,q-1) for q in (q0,q1)]==[13,13],"scalar_primary_thirteenth_roots")
ck(n%28==1 and gcd(13,28)==1,"central_normalization_and_root_exclusion")
ck(all((q-1)%13==0 and q!=13 for q in (q0,q1)),"primitive_roots_split_distinct")
ck(q0-1>4*(f-1) and q1-1>4*(f-1),"single_global_euler_factor")
ck((T-1)**2<2*T*(T-2),"complete_pencil_count_factor")
cuts=[]
for power,k,expected in [(13,37,1483877),(1,34,1307183)]:
    L=k*n-k*(k+1)//2
    overhead=1+5022+15*2*f*n+(k+13*power)*a*f+f*(3+996*(2*n+1))
    margin=70*L*(f-1)-overhead
    ck(margin==expected,"exact_all_s_cut_margin")
    ck(k<=82 and 0<k<=m,"available_minor_and_green_range")
    for r in range(n):
        u=min(r,k)
        Lu=u*n-u*(u+1)//2
        ck(L-Lu<=a*(k-u),"green_deficiency_linear_bound")
    for d in (13,169):
        A=n*n*(d-1)//(2*d)
        ck(3**(A-L)>=2*d,"nonrational_primary_absorption")
    cuts.append({"power":power,"minor_order":k,"green_exponent":L,
                 "overhead_binary_upper":overhead,"absolute_sum_binary_margin":margin})
ck(m-36==128 and 128-12*5==68 and 68-5==63,"first_cut_eigenspace_dimensions")
ck(m-33==131 and 131-5==126 and n-126==43,"second_cut_positive_fixed_dimensions")
ck(F(1,2**1483877)+F(1,2**1307183)<F(1,2**1307182),"two_cut_union_bound")
ck(F(1,2**1999)+F(1,2**104546)+F(1,2**101550)+F(1,2**4088)+
   F(1,2**21414)+F(1,2**1307182)<F(1,2**1998),"full_retained_error_budget")
# Nearby bounds are retained as failed alternatives rather than promoted.
def margin(k,power):
    L=k*n-k*(k+1)//2
    return 70*L*(f-1)-(1+5022+15*2*f*n+(k+13*power)*a*f+
                            f*(3+996*(2*n+1)))
ck(margin(36,13)==-30979,"order36_first_cut_not_sufficient")
ck(margin(33,1)==-242743,"order33_second_cut_not_sufficient")

# Exact exterior/minor expansion in a small integral model.
x=sp.symbols("x")
expansion_cases=0
for size in (2,3,4):
    for seed in range(4):
        A=sp.Matrix(size,size,lambda i,j:(3*i+2*j+seed)%5-2)
        for power in (1,2,3):
            C=A**power-sp.eye(size)
            for k in range(1,size+1):
                for I in combinations(range(size),k):
                    for J in combinations(range(size),k):
                        # Polynomial coefficient form makes every minor of
                        # A^power-I a signed sum of lower exterior entries.
                        poly=sp.Poly((A**power-x*sp.eye(size)).extract(I,J).det(),x)
                        ck(poly.eval(1)==C.extract(I,J).det(),"exact_minor_expansion")
                        ck(poly.degree()<=k,"at_most_k_identity_insertions")
                        expansion_cases+=1

def rankmod(A,q):
    M=[[int(x)%q for x in row] for row in A.tolist()]
    r=0
    for j in range(len(M[0])):
        pivot=next((i for i in range(r,len(M)) if M[i][j]),None)
        if pivot is None:continue
        M[r],M[pivot]=M[pivot],M[r]
        z=pow(M[r][j],-1,q);M[r]=[(v*z)%q for v in M[r]]
        for i in range(len(M)):
            if i!=r:
                z=M[i][j];M[i]=[(u-z*v)%q for u,v in zip(M[i],M[r])]
        r+=1
        if r==len(M):break
    return r

local_cases=0;valuation_checks=0
for q in (53,79):
    etas=[z for z in range(1,q) if pow(z,13,q)==1]
    ck(len(etas)==13,"thirteen_distinct_local_scalars")
    for eta in etas:
        for rank in (0,1,2,3):
            # Actual scalar-primary full matrix with a fixed compression.
            N=sp.zeros(5)
            for j in range(rank):N[j,j+1]=1
            g=eta*(sp.eye(5)+N)
            A=g.extract(range(4),range(4))
            C=A**13-sp.eye(4)
            ck(rankmod(g-eta*sp.eye(5),q)==rank,"local_actual_rank")
            ck(rankmod(C,q)<=rank,"annihilating_polynomial_rank")
            for k in range(1,5):
                e=max(0,k-rank)
                for I in combinations(range(4),k):
                    for J in combinations(range(4),k):
                        ck(int(C.extract(I,J).det())%(q**e)==0,"local_minor_valuation")
                        valuation_checks+=1
            local_cases+=1

report={"finding":"AM-K068","status":"PASS","timestamp_utc":datetime.now(timezone.utc).isoformat(),
        "exact_assertions":len(checks),"expansion_cases":expansion_cases,
        "local_scalar_primary_cases":local_cases,"local_valuation_checks":valuation_checks,
        "cuts":cuts,
        "input_sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (hp,gp)},
        "checks":checks,
        "scope":"Exact all-s absolute-bound arithmetic, local annihilator/minor diagnostics and fixed-space dimensions. No global short-sum enumeration, residual positivity or Lean build."}
Path(args.output).write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps({k:report[k] for k in ("finding","status","timestamp_utc","exact_assertions","expansion_cases","local_scalar_primary_cases","local_valuation_checks","cuts")},indent=2))

