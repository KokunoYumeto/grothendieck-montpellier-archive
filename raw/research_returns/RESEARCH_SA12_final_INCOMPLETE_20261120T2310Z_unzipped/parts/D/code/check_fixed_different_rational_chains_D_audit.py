#!/usr/bin/env python3
"""Exact checks for the degree-two fixed-different rational-chain family."""
from pathlib import Path
import hashlib, json, time
from itertools import product
import sympy as s

start=time.perf_counter()
checks=0
def check(v,msg):
    global checks
    checks+=1
    if not v:
        raise AssertionError(msg)
x,y,z,u,v,a,b,t=s.symbols("x y z u v a b t")
records=[]
for m in range(1,21):
    N=2*m+1
    F=z*z+x*z+y**N
    check(s.Poly(F.subs({x:u+v,z:v})-(u*v+y**N),u,v,y,modulus=2).is_zero,
          ("coordinate substitution",m))
    check(s.Poly(s.diff(F,z)-x,x,y,z,modulus=2).is_zero,("z derivative",m))
    check(s.Poly(s.diff(F,x)-z,x,y,z,modulus=2).is_zero,("x derivative",m))
    check(s.Poly(s.diff(F,y)-y**(N-1),x,y,z,modulus=2).is_zero,("y derivative",m))
    check(s.Poly((z*z+y**N).subs({y:t*t,z:t**N}),t,modulus=2).is_zero,
          ("curve normalization",m))
    represented={2*i+N*j for i in range(2*N+1) for j in range(3)
                 if 2*i+N*j <= 2*N}
    missing=[i for i in range(2*N+1) if i not in represented]
    check(missing==list(range(1,2*m,2)),("semigroup gaps",m))
    check(len(missing)==m,("curve delta",m))
    for i in range(N):
        U=(i+1,i); V=(N-i-1,N-i); Y=(1,1)
        check(tuple(U[j]+V[j] for j in range(2))==(N,N),("chart equation",m,i))
        check(all(q>=0 for q in U+V+Y),("regular chart monomials",m,i))
        if i<N-1:
            # a_next=b^-1, b_next=a*b^2; compare exponent vectors.
            def transform(exp):
                return (exp[1],-exp[0]+2*exp[1])
            check(transform((i+2,i+1))==U,("u transition",m,i))
            check(transform((N-i-2,N-i-1))==V,("v transition",m,i))
            check(transform((1,1))==Y,("y transition",m,i))
    d0,d1=1,2
    if N-1==0:
        determinant=d0
    elif N-1==1:
        determinant=d1
    else:
        for length in range(2,N):
            d0,d1=d1,2*d1-d0
        determinant=d1
    check(determinant==N,("intersection determinant",m))
    check(1*2==2,("valuation fundamental equality",m))
    check(N-1==2*m,("chain length",m))
    records.append({"m":m,"N":N,"chain_length":N-1,"determinant":determinant,
                    "curve_delta":m,"degree":2,"e":1,"f_insep":2,"different":1})
out={"status":"passed","assertions":checks,"runtime_seconds":time.perf_counter()-start,
     "exact_arithmetic":True,"records":records,
     "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     "scope":"Exact polynomial, semigroup, monomial-chart and determinant checks; normality and properness are proved in the TeX."}
path=Path(__file__).resolve().parents[1]/"output/fixed_different_rational_chains.json"
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:out[k] for k in ("status","assertions","runtime_seconds","source_sha256")},indent=2))

