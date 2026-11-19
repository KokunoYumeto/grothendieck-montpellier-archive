#!/usr/bin/env python3
"""Exact finite checks used in D.1, D.2, D.3, E.4 and E.5.
These certify displayed arithmetic, not the invoked Honda--Tate theorem.
"""
from fractions import Fraction
from itertools import product
from math import gcd
from time import perf_counter

start=perf_counter()
def mul(z,w):
    a,b=z;c,d=w
    return a*c-b*d,a*d+b*c
def conj(z):return z[0],-z[1]
def norm(z):return mul(z,conj(z))[0]
def div_exact(z,w):
    a,b=mul(z,conj(w));n=norm(w)
    return (a//n,b//n) if a%n==0 and b%n==0 else None
def val(z,w):
    k=0
    while (t:=div_exact(z,w)) is not None:
        z=t;k+=1
    return k
pi=(2,1);lam=mul((5,0),mul(pi,pi));q=(25,0)
print('D.1 Gaussian example')
print('pi =',pi,'lambda =',lam,'Norm(lambda) =',norm(lam))
print('v_pi(lambda),v_pibar(lambda) =',val(lam,pi),val(lam,conj(pi)))
print('normalized slopes =',Fraction(val(lam,pi),val(q,pi)),Fraction(val(lam,conj(pi)),val(q,conj(pi))))
print('Polarizations on basis (q, lambda/q):',[(1,a) for a in (0,1)])
print('Slope parity demands a(2f)=1; every F2 hom has a(2f)=0: no extension.')
print('\nD.2 rational odd-weight example')
print('Norm(1+4i) =',1+16,'Norm(3+2sqrt(-2)) =',9+8)
P=[(a,1-a,t) for a,t in product((0,1),repeat=2)]
print('polarizations on (x,y,t):',P)
print('Q-automorphism orbits:',[sorted(x for x in P if x[2]==t) for t in (0,1)])
print('\nD.3 uniform local denominator family')
for p in (2,3,5,7,11):
    for r in (3,4,5,6,7):
        # alpha^2=alpha-p. Work in Z[alpha].
        def mm(z,w):
            a,b=z;c,d=w
            return a*c-p*b*d,a*d+b*c+b*d
        a=(0,1);ab=(1,-1);z=(1,0)
        for _ in range(r-1):z=mm(z,a)
        z=mm(z,ab)
        cz=(z[0]+z[1],-z[1]);nz=mm(z,cz)
        assert nz==(p**r,0)
        assert z[1]!=0
        order=r//gcd(r,1)
        print(f'p={p}; r={r}; pi={z[0]}+({z[1]})*alpha; norm={nz[0]}; slopes={(Fraction(r-1,r),Fraction(1,r))}; invariant_order={order}')
print('\nE.4 finite-field prime-to-p orders')
for p,q0 in ((2,2),(2,4),(3,3),(3,9),(5,5),(5,25)):
    for n in (-3,-2,-1,1,2,3):
        order=q0**abs(n)-1
        assert gcd(order,p)==1
        print(f'q={q0}; n={n}; H1_order={order}; p_primary=0')
print('\nE.5 elliptic fibres over F5, y^2=x^3+a*x+1')
for a in (0,1):
    pts=[(x,y) for x,y in product(range(5),repeat=2) if (y*y-x*x*x-a*x-1)%5==0]
    N=len(pts)+1;trace=6-N;disc=(-16*(4*a**3+27))%5
    assert disc!=0
    print(f'a={a}; discriminant_mod5={disc}; points={pts} plus infinity; cardinality={N}; trace={trace}; Newton_slopes={"(1/2,1/2)" if trace%5==0 else "(0,1)"}')
print('\nE.6 local Artin quadratic quotient')
for ell in (3,5):
    roots=[x for x in range(ell) if (x*x+1)%ell==0]
    print(f'ell={ell}; roots of x^2+1 mod ell={roots}; torsor_trivial={bool(roots)}')
    if roots:
        assert all((2*x)%ell!=0 for x in roots)
print(f'Elapsed seconds: {perf_counter()-start:.6f}')
