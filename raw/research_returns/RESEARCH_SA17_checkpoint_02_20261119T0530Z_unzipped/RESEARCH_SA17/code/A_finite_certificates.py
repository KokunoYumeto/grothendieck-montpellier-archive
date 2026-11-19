#!/usr/bin/env python3
"""Finite checks illustrating the infinite-ring NR(b) counterexample.

This does not certify dimension one: that is proved in the paper. It checks
all ring axioms on F_2[t,e]/(t^3,te,e^2), including the nonzero embedded e.
"""
import itertools, json, time
from pathlib import Path

started=time.perf_counter()
p=2
n=3
elements=list(itertools.product(range(p),repeat=n+1))
zero=(0,)*(n+1)
one=(1,)+(0,)*n
t=(0,1,0,0)
eps=(0,0,0,1)
def add(a,b): return tuple((x+y)%p for x,y in zip(a,b))
def mul(a,b):
    c=[0]*(n+1)
    for i in range(n):
        for j in range(n-i): c[i+j]=(c[i+j]+a[i]*b[j])%p
    c[n]=(a[0]*b[n]+a[n]*b[0])%p
    return tuple(c)
assert eps!=zero and mul(eps,eps)==zero and mul(t,eps)==zero
triples=0
for a,b,c in itertools.product(elements,repeat=3):
    assert add(add(a,b),c)==add(a,add(b,c))
    assert mul(mul(a,b),c)==mul(a,mul(b,c))
    assert mul(a,add(b,c))==add(mul(a,b),mul(a,c))
    triples+=1
for a,b in itertools.product(elements,repeat=2):
    assert add(a,b)==add(b,a)
    assert mul(a,b)==mul(b,a)
for a in elements:
    assert mul(a,one)==a and add(a,zero)==a
ann=[a for a in elements if mul(a,eps)==zero]
units=[a for a in elements if any(mul(a,b)==one for b in elements)]
assert len(ann)==8 and all(a[0]==0 for a in ann)
assert len(units)==8 and all(a[0]==1 for a in units)
out={'statement':'A:NR-counterexample','scope':'finite truncation only; the paper proves the complete dimension-one example',
     'ring':'F2[t,e]/(t^3,te,e^2)','elements':len(elements),'triples_checked':triples,
     'annihilator_e':len(ann),'units':len(units),'e_nonzero':eps!=zero,
     'e_squared_zero':mul(eps,eps)==zero,'t_e_zero':mul(t,eps)==zero,
     'seconds':time.perf_counter()-started,'result':'passed'}
path=Path(__file__).resolve().parents[1]/'logs/A_finite_certificates.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
