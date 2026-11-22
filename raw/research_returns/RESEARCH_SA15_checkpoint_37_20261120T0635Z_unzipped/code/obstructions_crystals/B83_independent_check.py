"""Exact B83 quotient-lattice, opposite-weight and valuation supplement."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
from itertools import product
from fractions import Fraction
from math import isqrt
import sympy as sp
import json,time

start=time.perf_counter();counts=Counter();weight_rows=[]
P=sp.symbols('p',nonzero=True)
a,b,c,d=sp.symbols('a b c d')
M=sp.Matrix([[a,b],[c,d]])
H1=sp.diag(P,1)*M*sp.diag(1/P,1)
H2=sp.diag(1,P)*M*sp.diag(1,1/P)
assert H1==sp.Matrix([[a,P*b],[c/P,d]])
assert H2==sp.Matrix([[a,b/P],[P*c,d]])
counts['exact_lattice_conjugations']=2
A11,A12,A21,A22,B11,B12,B21,B22=sp.symbols('A11 A12 A21 A22 B11 B12 B21 B22')
subs={a:1+P*A11+P**2*B11,b:P*A12+P**2*B12,
      c:P*A21+P**2*B21,d:1+P*A22+P**2*B22}
Q1=H1.subs(subs).applyfunc(sp.expand)
Q2=H2.subs(subs).applyfunc(sp.expand)
assert Q1.applyfunc(lambda z:z.subs(P,0))==sp.Matrix([[1,0],[A21,1]])
assert Q2.applyfunc(lambda z:z.subs(P,0))==sp.Matrix([[1,A12],[0,1]])
counts['exact_quotient_residual_matrices']=2
E12=(0,1,0,0);E21=(0,0,1,0);I=(1,0,0,1)
def add(X,Y,m):return tuple((x+y)%m for x,y in zip(X,Y))
def scale(a,X,m):return tuple(a*x%m for x in X)
def mul(X,Y,m):return ((X[0]*Y[0]+X[1]*Y[2])%m,(X[0]*Y[1]+X[1]*Y[3])%m,
                       (X[2]*Y[0]+X[3]*Y[2])%m,(X[2]*Y[1]+X[3]*Y[3])%m)
def power(X,n,m):
    z=I
    while n:
        if n&1:z=mul(z,X,m)
        X=mul(X,X,m);n//=2
    return z

primes=[p for p in range(5,102) if all(p%j for j in range(2,isqrt(p)+1))]
for p in primes:
    q=p*p;N=q-1;e=p*(p-1);s=p*N
    for k1,k2 in product(range(1,p-1),repeat=2):
        B1=q*k1;B2=q*k2
        assert e<B1<p*e and e<B2<p*e
        high1=s-B1;low2=B2//p
        high2=s-B2;low1=B1//p
        assert high1==p*(N-p*k1) and low2==p*k2
        assert high2==p*(N-p*k2) and low1==p*k1
        assert N-p*k1>=2*p-1>k2
        assert N-p*k2>=2*p-1>k1
        assert all(z%p!=0 for z in (N-p*k1,N-p*k2,k1,k2))
        assert all(Fraction(z,q).denominator==q for z in (N-p*k1,N-p*k2,k1,k2))
        counts['opposite_actual_quotient_pairs']+=1
    bad=good=0
    for alpha,beta in product(range(1,p),repeat=2):
        if pow(alpha*beta%p,(p-1)//2,p)!=p-1:
            continue
        ratio=alpha*pow(beta,-1,p)%p
        assert pow(ratio,(p-1)//2,p)==p-1
        if p%4==1:
            assert ratio not in (1,p-1)
            assert len({1,ratio,pow(ratio,-1,p)})==3
            good+=1
        else:
            if ratio==p-1:bad+=1
            else:good+=1
        counts['nonsquare_residual_weight_pairs']+=1
    if p%4==3:
        assert bad==p-1
    else:
        assert bad==0
    weight_rows.append({'p':p,'separated_pairs':good,'order_two_exception_pairs':bad})
    modulus=p**3
    g=add(I,scale(p,E12,modulus),modulus)
    h=add(I,scale(p,E21,modulus),modulus)
    gi=add(I,scale(-p,E12,modulus),modulus)
    hi=add(I,scale(-p,E21,modulus),modulus)
    comm=mul(mul(mul(g,h,modulus),gi,modulus),hi,modulus)
    assert comm==add(I,scale(p*p,(1,0,0,-1),modulus),modulus)
    assert power(g,p,modulus)==add(I,scale(p*p,E12,modulus),modulus)
    assert power(h,p,modulus)==add(I,scale(p*p,E21,modulus),modulus)
    counts['literal_commutator_and_power_rows']+=1
    assert all(r1+t>=5 for r1 in range(2,5) for t in range(3,5) if r1<=t)
    counts['dimension_lower_bound_rows']+=1
    for b0 in range(1,e):
        valuation=Fraction(b0,p**4)
        if b0%p:
            assert valuation.denominator==p**4
        else:
            k=b0//p
            assert 1<=k<=p-2 and b0==p*k
            assert valuation.denominator==p**3
        counts['residual_tame_parameter_branches']+=1

out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-start,'counts':dict(counts),
     'weight_rows':weight_rows,
     'scope':'Two symbolic lattice conjugations and residual matrices; every k-pair, every nonsquare '
             'residual eigenvalue pair, exact matrix commutator/power and every tame parameter branch '
             'for primes5..101. The p congruent3mod4 order-two weight exceptions are retained explicitly. '
             'Actual quotient descent and point-field proofs are separate; no existence or full-index claim.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
