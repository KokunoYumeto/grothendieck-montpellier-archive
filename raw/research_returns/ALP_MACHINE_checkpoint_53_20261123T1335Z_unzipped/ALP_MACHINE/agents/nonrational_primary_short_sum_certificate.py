#!/usr/bin/env python3
"""AM-K067: exact finite-character and actual-host threshold certificate.

This does not enumerate the actual rational short sum or evaluate its signs.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
from math import comb, gcd, prod
from pathlib import Path
import hashlib
import json

parser=argparse.ArgumentParser()
parser.add_argument("--output",default=str(Path(__file__).with_suffix(".json")))
args=parser.parse_args()
base=Path(__file__).parent
checks=[]
def ck(value,label):
    if not value:
        raise AssertionError(label)
    checks.append(label)

def strict_binary_margin(A,B):
    assert A>0 and B>0
    k=B.bit_length()-A.bit_length()
    def lt(j):
        return (A<<j)<B if j>=0 else A<(B<<(-j))
    while not lt(k): k-=1
    while lt(k+1): k+=1
    ck(lt(k) and not lt(k+1),"strict_binary_margin")
    return k

host_path=base/"definite_oscillator_large_t_certificate.json"
old_path=base/"definite_oscillator_minimal_denominator_certificate.json"
hosts=json.loads(host_path.read_text())["rows"]
old=json.loads(old_path.read_text())["hosts"]
output=[]
for row in hosts:
    a,f=row["a"],row["f"]
    n=a+1; H=8192; T=int(row["T"])
    g0,g1=row["g0"],row["g1"]; qmin=min(g0,g1); Q=g0*g1
    G=int(next(x for x in old if x["host"]==row["host"])["stabilizer_gcd"])
    d0=43 if n==43 else 13
    divisors=[d for d in range(2,n+1) if n%d==0]
    E0=n*(n-1)//2-d0*(n//d0)*(n//d0-1)//2-a
    ck(divisors==([43] if n==43 else [13,169]),"actual_primary_degrees")
    ck(2*(f-1)*2<qmin-1,"one_global_euler_factor_below_two")
    ck(a-4>5 and n-6>0,"scalar_block_excludes_nonrational_primary")
    ck(gcd(n,28)==1,"unique_central_determinant_normalization")
    ck([gcd(n,q-1) for q in (g0,g1)]==([1,1] if n==43 else [13,13]),
       "actual_residual_scalar_orders")
    if n==169:
        ck(n%28==1,"J56_determinant_normalizer_is_delta")
    for d in divisors:
        m=n//d
        Ad=n*(n-1)//2-d*m*(m-1)//2
        ck(2*d*Ad==n*n*(d-1),"primary_exponent_identity")
        ck(Ad-a>=E0,"minimal_extra_exponent")
        # The degree169 factor is dominated by the degree13 factor.
        if d!=d0:
            ck(d*qmin**E0<=d0*qmin**(Ad-a),"primary_degree_uniform_domination")
        for r in range(1,min(82,a)+1):
            L=r*n-r*(r+1)//2
            if n==169:
                ck(Ad>L and 2*d<=3**(Ad-L),"high_rank_green_comparison")
    Cnum=2*G*(2*H+1)**(2*f*n)*(2*H)**(a*f)
    Cden=Q**(a*(f-1))
    m0=strict_binary_margin(Cnum,Cden)
    md=strict_binary_margin(d0,qmin**E0)
    bits=T.bit_length()
    slope=2+(2*n+1)*bits
    ck(T<2**bits,"strict_T_binary_bound")
    ck((T-1)**2<2*T*(T-2),"pencil_factor_upper_bound")
    thresholds=[]
    for s in range(1,f+1):
        target=4096-m0+f+slope*s
        k=max(1,(target+md-1)//md)
        exponent=m0-f-slope*s+md*k
        ck(exponent>=4096,"complete_stratum_threshold")
        if k>1:
            ck(m0-f-slope*s+md*(k-1)<4096,"coarse_threshold_minimal")
        ck(comb(f,s)<=2**f,"binomial_count_bound")
        thresholds.append({"s":s,"K_s":k,"available":k<=2*(f-1),
                           "guaranteed_binary_margin":exponent,
                           "remaining_scalar_primary_minimum":max(0,2*(f-1)-k+1)})
    exact=[]
    cases=[(1,5),(2,10),(3,14),(17,78),(18,82)] if n==43 else [(3,1),(4,2)]
    for s,k in cases:
        A=Cnum*comb(f,s)*(T-1)**(2*s)*2**s*T**(2*n*s)*d0**k
        B=Cden*(T-2)**s*qmin**(E0*k)
        M=strict_binary_margin(A,B)
        exact.append({"s":s,"nonrational_count_at_least":k,"binary_margin":M})
    if n==169:
        ck((m0,md,bits,slope)==(776478,447357,996,337646),"J56_exact_constants")
        ck(exact[0]["binary_margin"]==211449,"entire_s3_nonrational_subset")
        ck(exact[1]["binary_margin"]==321345,"J56_s4_two_primary_bound")
        ck(all(t["available"] for t in thresholds),"J56_all_s_thresholds_available")
        ck(thresholds[2]["K_s"]==1 and thresholds[-1]["K_s"]==126,
           "J56_endpoint_thresholds")
        ck(f<2**8,"all_J56_removed_strata_below_2^-4088")
    else:
        ck((m0,md,bits,slope)==(496,19055,1001,87089),"J14_exact_constants")
        ck([x["binary_margin"] for x in exact]==[8702,16909,6061,6662,-4182],
           "J14_exact_selected_margins")
        ck(max(t["s"] for t in thresholds if t["available"])==17,"J14_available_s_range")
        ck(thresholds[16]["K_s"]==78 and thresholds[17]["K_s"]==83,
           "J14_threshold_boundary")
        ck(17<2**5,"all_J14_removed_strata_below_2^-4091")
    output.append({"host":row["host"],"a":a,"f":f,"n":n,"H":H,
                   "d0":d0,"extra_exponent":E0,"C_binary_margin":m0,
                   "delta_binary_margin":md,"T_binary_bits":bits,"slope":slope,
                   "thresholds":thresholds,"exact_selected_bounds":exact})

# Small exact Green maxima: no floating point and no particular regular
# character chosen. These verify the modulus envelope used in the proof.
green_cases=0
for n in range(3,19):
    for d in range(1,n+1):
        if n%d: continue
        m=n//d
        for q in (3,5,7):
            den=prod(q**j-1 for j in range(1,n))
            for t in range(1,m+1):
                if d==1 and t==n: continue  # scalar value, handled separately
                R=F(d*prod(q**(d*j)-1 for j in range(1,t)),den)
                if d==1:
                    ck(R<=F(1,q**(n-1)-1),"scalar_primary_nonscalar_ratio")
                else:
                    A=n*(n-1)//2-d*m*(m-1)//2
                    ck(R< F(2*d,q**A),"nonrational_primary_ratio")
                green_cases+=1

# Existing error components plus the new disjoint removal still fit the
# unchanged error budget; including the optional E12 plane is harmless.
error=F(1,2**1999)+F(1,2**104546)+F(1,2**101550)+F(1,2**4088)+F(1,2**21414)
ck(error<F(1,2**1998),"unchanged_complete_error_budget")

report={"finding":"AM-K067","status":"PASS",
        "timestamp_utc":datetime.now(timezone.utc).isoformat(),
        "exact_assertions":len(checks),"green_cases":green_cases,
        "input_sha256":{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                        for p in (host_path,old_path)},
        "hosts":output,"checks":checks,
        "scope":"Exact Green envelopes, host integers and complete-count thresholds. No rational short-sum enumeration, actual character phase evaluation, global Mram nonvanishing or Lean build."}
Path(args.output).write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps({k:report[k] for k in ("finding","status","timestamp_utc","exact_assertions","green_cases")},indent=2))
for row in output:
    print(json.dumps({k:row[k] for k in ("host","extra_exponent","C_binary_margin","delta_binary_margin","slope","exact_selected_bounds")},indent=2))

