#!/usr/bin/env python3
"""Exact binary identification search, with every finite coefficient case retained.

E: y^2+y=x^3+x; sections of 5O are 1,x,y,x^2,xy.
No geometric smoothness or surface realization is inferred by this program.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import time

t0 = time.perf_counter()

def pmul(a,b):
    out=0
    while b:
        if b&1: out ^= a
        b >>= 1
        a <<= 1
    return out

def add(a,b): return (a[0]^b[0],a[1]^b[1])
def mul(a,b):
    # y^2=y+x^3+x
    bd=pmul(a[1],b[1])
    return (pmul(a[0],b[0])^pmul(bd,0b1010),pmul(a[0],b[1])^pmul(a[1],b[0])^bd)
def square(a): return mul(a,a)

basis=[(1,0),(2,0),(0,1),(4,0),(0,2)]
Tcols=[0b10101,0b01111,0b01000,0b00101,0b00110]
def T(v):
    out=0
    for i,c in enumerate(Tcols):
        if v>>i&1: out ^= c
    return out
def aspoly(v):
    out=(0,0)
    for i,b in enumerate(basis):
        if v>>i&1: out=add(out,b)
    return out
def rank(vs):
    piv={}
    for v in vs:
        while v:
            k=v.bit_length()-1
            if k in piv: v ^= piv[k]
            else:
                piv[k]=v
                break
    return len(piv)

assert all(T(T(T(T(T(1<<i)))))==1<<i for i in range(5))
cases=[]
success=[]
for v in range(1,32):
    orbit=[v]
    for _ in range(4): orbit.append(T(orbit[-1]))
    fs=list(map(aspoly,orbit))
    values=[]
    for i in range(5):
        values.append(add(square(fs[i]),add(mul(fs[(i-1)%5],fs[(i+1)%5]),mul(fs[(i-2)%5],fs[(i+2)%5]))))
    item={'seed':v,'orbit':orbit,'rank':rank(orbit),'Pfaffian_remainders':values}
    cases.append(item)
    if item['rank']==5 and all(z==(0,0) for z in values): success.append(item)

fP=(2,0b11)
fminus=(1,0b11)
assert mul(fP,fminus)==(1<<5,0)
out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-t0,'ring':'F2[x,y]/(y^2+y+x^3+x)','basis':['1','x','y','x^2','xy'],'theta_T_columns_binary':Tcols,'T_fifth_power_identity':True,'fP_fminus_equals_x5':True,'all_cases':cases,'successful_cyclic_bases':success,'successful_count':len(success),'scope':'Exact quotient-ring identities and finite binary change-of-basis search only; no surface Cartier realization.'}
dest=Path(__file__).with_suffix('.output.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'successful_count':len(success),'successful_cyclic_bases':success,'runtime_seconds':out['runtime_seconds']}))
