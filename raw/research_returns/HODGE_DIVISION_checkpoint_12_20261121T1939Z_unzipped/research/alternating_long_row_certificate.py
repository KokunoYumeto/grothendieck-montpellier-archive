#!/usr/bin/env python3
"""Exact tail-content certificate for HD-ALT05, with all-n proof separate."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,prod
import hashlib,json,time
R=Path(__file__).resolve().parent
def parts(n,cap=None):
    if not n:
        yield ();return
    for x in range(min(n,cap or n),0,-1):
        for tail in parts(n-x,x):yield (x,)+tail
def stats(lam):
    n=sum(lam);c=[j-i for i,w in enumerate(lam) for j in range(w)]
    t=sum(c);s=sum(x*x for x in c)
    col=[sum(w>j for w in lam) for j in range(lam[0])]
    degree=factorial(n)//prod(w-j+col[j]-i-1 for i,w in enumerate(lam) for j in range(w))
    u=F(3*(s-n*(n-1)//2),n*(n-1)*(n-2))
    v=F(4*(t*t+n*(n-1)-3*s),n*(n-1)*(n-2)*(n-3))
    return t,s,degree,u,v
start=time.monotonic();count=0;data=[]
for n in range(15,101):
    number=0;min_degree=None;max_v=F(-100)
    for k in range((n+6)//7,(n-1)//4+1):
        for mu in parts(k):
            lam=(n-k,)+mu;t,s,degree,u,v=stats(lam)
            assert F(n,7)<=k<F(n,4)
            bound=sum(j*j for j in range(1,n-k))+sum(j*j for j in range(1,k+1))
            assert s<=bound
            assert F(n*(n-2*k-1),2)<=t<=n*(n-1)//2-k*(n-k+1)
            assert (1-u)/3>=F(k*(n-1-k),(n-1)*(n-2))>=F(n*(6*n-7),49*(n-1)*(n-2))>F(6,49)>F(5,48)
            assert t<=F(n*(37*n-63),98)
            upper=F((37*n-63)**2,2401*(n-1)*(n-2))+F(4,(n-2)*(n-3))
            assert v<=upper<F(7,12)
            assert min((1-u)/3,(1-v)/4)>=F(5,48)
            assert degree>=F(2*n**3,27)>=250>144
            count+=1;number+=1
            min_degree=min(degree,min_degree or degree);max_v=max(max_v,v)
    data.append(dict(n=n,partitions=number,minimum_degree=min_degree,maximum_v=str(max_v)))
P=lambda n:379*n**3+4386*n*n-145831*n+157290
for x in range(1001):
    assert P(15+x)==379*x**3+21441*x*x+241574*x+235800>0
assert 1+10*F(5,48)-2==F(1,24)
assert 6/F(1,24)==144
t,s,d,u,v=stats((12,3))
assert F(45,4)<12<=F(90,7)
out=dict(status='PASS',partitions=count,range_n=[15,100],cases=data,
         strict_gate_witness=dict(n=15,partition=[12,3],degree=d,u=str(u),v=str(v)),
         positive_translated_polynomial_coefficients=[235800,241574,21441,379],
         inducing_degree_upper_bound=144,factor_degree_lower_bound=250,
         scope='Exact finite tail-content/hook/ratio checks. Universal inequalities and monodromy/period obstruction are proved in full in the TeX; no finite extrapolation.',
         proof_sha256=hashlib.sha256((R/'ordinary_alternating_long_row_obstruction.tex').read_bytes()).hexdigest(),
         seconds=round(time.monotonic()-start,3))
(R/'alternating_long_row_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
