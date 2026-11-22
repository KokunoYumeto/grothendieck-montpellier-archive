#!/usr/bin/env python3
"""Independent AM-R018 numerical Sizes review; no Lean or prime proof."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import json

ROWS = [
    dict(host="J14", f=42, k=42, d=1760, C=45156049293,
         G=[4615409,5276377],
         T=3710360310942963702130514092646914581678165356491757211050633,
         expected_rmax=55),
    dict(host="J56", f=168, k=168, d=1634, C=40530339687,
         G=[22285932761,64072175441],
         T=3045759889845354427724717877501093821489629367456155582288640401018208099619883018305672886530161,
         expected_rmax=90),
]

def actual_arrays(k,d,C,n):
    u = [F((2*(k-i)+1)*C)+F(1,2) for i in range(k)]
    u[0] += n
    w0 = [u[i]-F(k-1,2)+i for i in range(k)]
    w1 = [x-F(d,2) for x in w0] + [F(k,2)]*d
    w2 = [x-F(d,2) for x in w1] + [F(-4*C)+F(k+d,2)]*d
    arr = [w0,w1,w2]
    for j,w in enumerate(arr):
        assert len(w)==k+j*d
        assert all(x.denominator==1 for x in w)
        assert all(w[i]>=w[i+1] for i in range(len(w)-1))
    return arr

def check(row):
    k,d,C,f,T = [row[x] for x in ["k","d","C","f","T"]]
    S=[2*(k-1)*C+1,(2*k+1)*C+1+d//2,(2*k+5)*C+1+d//2]
    assert S[0]<S[1]<S[2]
    rmax=row["expected_rmax"]
    increments=[0,1,121,11**rmax,121*11**rmax,121*11**(rmax+1)]
    for n in increments:
        for j,w in enumerate(actual_arrays(k,d,C,n)):
            literal_spread=w[0]-w[-1]+len(w)
            assert literal_spread==S[j]+n
    assert all(2*f*k<g-1 for g in row["G"])
    endpoints=[]
    for r in range(rmax+2):
        B=121*11**r
        maximum=S[2]+B
        a_size=(maximum+1)//2
        assert maximum<=2*a_size and 2*(a_size-1)<maximum
        assert 2*f*(k+2*d)+1<4*a_size
        inside=4*a_size<T
        assert inside == (r<=rmax)
        if r in (0,rmax,rmax+1):
            endpoints.append(dict(r=r,B=B,max_spread=maximum,a_size=a_size,
                                  four_a=4*a_size,T_minus_four_a=T-4*a_size,
                                  literal_Sizes_holds=inside))
    # At the next exponent even the least real a=max_spread/2 fails.
    assert 2*(S[2]+121*11**(rmax+1))>=T
    return dict(**row, S=S,N=[k,k+d,k+2*d],tested_increment_arrays=len(increments),
                checked_r_values=rmax+2,endpoints=endpoints,result="PASS")

out={"statement":"Independent AM-R018 Sizes review",
     "checked_utc":datetime.now(timezone.utc).isoformat(),
     "scope":"Source spread includes +N. Exact integer/Fraction weight recurrence and numerical Sizes only. The primality theorem for the supplied T is the parent R017 input.",
     "hosts":[check(row) for row in ROWS],"result":"PASS"}
sharp = []
for host,r,D0,c0,K0,upper,lower in [
    ("J14",55,3504831920337006,350483192023230,899640,F(2,10**45),F(4,10**54)),
    ("J56",90,194467812219985248,19446781221824712,60484032,F(3,10**80),F(1,10**88)),
]:
    degree = 122*11**r+D0
    error_upper = (F(c0)-F(1,10)-F(D0,1220))/degree
    error_lower = (F(1,5)+K0)/degree
    assert error_upper < upper and error_lower < lower
    sharp.append(dict(host=host,r=r,T_r=degree,
                      strict_upper_error_bound=str(upper),
                      strict_lower_error_bound=str(lower),
                      check="exact Fraction comparison PASS"))
out["finite_raw_content_precision"] = sharp
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
