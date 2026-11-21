#!/usr/bin/env python3
"""Exact finite support for HD-ALT04; the all-n argument is in the proof."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial, prod
import hashlib, json, time
ROOT=Path(__file__).resolve().parent

def partitions(n,cap=None):
    if n==0:
        yield ()
    else:
        for x in range(min(n,cap if cap is not None else n),0,-1):
            for rest in partitions(n-x,x):
                yield (x,)+rest

def stats(lam):
    n=sum(lam)
    cols=[sum(w>j for w in lam) for j in range(lam[0])]
    cs=[j-i for i,w in enumerate(lam) for j in range(w)]
    t=sum(cs);s=sum(c*c for c in cs)
    deg=factorial(n)//prod(w-j+cols[j]-i-1 for i,w in enumerate(lam) for j in range(w))
    u=F(3*(s-n*(n-1)//2),n*(n-1)*(n-2))
    v=F(4*(t*t+n*(n-1)-3*s),n*(n-1)*(n-2)*(n-3))
    return t,s,deg,u,v

start=time.monotonic()
total=selected=new=0;records=[]
for n in range(15,37):
    count=extra=0;minhalf=None;maxu=maxv=F(-10)
    for lam in partitions(n):
        total+=1;k=max(lam[0],len(lam))
        if 4*k>3*n:continue
        count+=1;selected+=1
        if k>(n+1)//2:extra+=1;new+=1
        t,s,deg,u,v=stats(lam)
        assert s>=F(t*t,n)
        assert s<=F(k*(2*k-1)*(n-1),6)
        assert abs(t)<=F(n*(k-1),2)-(n-k)<=F(3*n*(n-2),8)
        assert u<=F(k*(2*k-1)-3*n,2*n*(n-2))<=F(9*n-30,16*(n-2))<F(9,16)
        assert v<=F(4*t*t,n*n*(n-1)*(n-2))+F(4,(n-2)*(n-3))
        assert v<=F(9*(n-2),16*(n-1))+F(4,(n-2)*(n-3))<F(9,16)
        assert min((1-u)/3,(1-v)/4)>=F(7,64)
        assert F(deg,2)>=F(n**3,27)>=125>64
        minhalf=min(F(deg,2),minhalf if minhalf is not None else F(deg,2))
        maxu=max(maxu,u);maxv=max(maxv,v)
    records.append(dict(n=n,partitions=count,new_vs_half=extra,
                        min_half_specht_degree=str(minhalf),max_u=str(maxu),max_v=str(maxv)))
p=lambda n:9*n*n-109*n+118
assert p(15)==508
for n in range(15,1001):
    assert p(n+1)-p(n)==18*n-100>0
    assert n-2>F(3*n,4)
assert 1+F(70,64)-2==F(3,32)
assert 6/(F(3,32))==64
t,s,d,u,v=stats((11,4))
assert 8<11<=F(45,4)
output={'status':'PASS','all_partitions_15_to_36':total,
        'three_quarter_partitions':selected,'new_vs_half_partitions':new,
        'cases':records,'strict_gate_witness':{'partition':[11,4],'n':15,'specht_degree':d,'u':str(u),'v':str(v)},
        'polynomial_base':508,'polynomial_forward_difference':'18n-100',
        'degree_upper_bound':64,
        'scope':'Finite exact content/hook/ratio and endpoint checks. Universal all-degree bounds, full normalizers, transitive tensor factors and actual period obstruction are established in the written proof.',
        'proof_sha256':hashlib.sha256((ROOT/'ordinary_alternating_three_quarters.tex').read_bytes()).hexdigest(),
        'seconds':round(time.monotonic()-start,3)}
(ROOT/'alternating_three_quarters_certificate.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k!='cases'}))
