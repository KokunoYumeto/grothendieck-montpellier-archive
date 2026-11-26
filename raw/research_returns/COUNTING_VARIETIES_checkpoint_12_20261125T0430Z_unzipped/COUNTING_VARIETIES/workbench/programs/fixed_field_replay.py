#!/usr/bin/env python3
"""Independent small-instance certificates for fixed-field multiplicities.
Run: python fixed_field_replay.py. Uses Python 3 and SymPy.
"""
from itertools import product
import json
from math import gcd, lcm
import sympy as sp

x=sp.Symbol('x')
def P(expr,p): return sp.Poly(expr,x,modulus=p)
def order(a,n):
    r=1
    for k in range(1,n+1):
        r=r*a%n
        if r==1:return k
    raise AssertionError('no order')
def unit_example(p,ell,q,S):
    N=ell*q
    R=lambda a: sorted({i*i%a for i in range(1,a)})
    C=lambda a,z: -sum(z**i for i in R(a))
    G=lambda a,z: pow(a,-1,p)*sum(z**i for i in range(a))
    cv=P(C(ell,x**q),p); guard=P(G(ell,x**q),p)
    if S==0: tests=[P(1,p)-cv,cv,guard]
    elif S==1: tests=[P(1,p)-cv,guard]
    else: tests=[P(0,p),guard]
    packed=sum((P(x**(ell*j),p)*v for j,v in enumerate(tests)),P(0,p))
    W=(P(1,p)-P(G(q,x**ell),p))*P(C(q,x**ell),p)
    B=P(x**N-1,p)
    A=(P(1,p)-W+W*packed).rem(B)
    J=sp.gcd(A,B).monic()
    K=(ell-1)//2*((q-1)//2); L=lcm(order(p,ell),order(p,q))
    factors=sp.factor_list(J)[1]
    degrees=sorted(f.degree() for f,e in factors for _ in range(e))
    assert J.degree()==K*S and degrees==[L]*(K*S//L)
    assert A.eval(1)%p==1 and gcd(K,p)==1 and K%L==0
    assert sp.gcd(J,J.diff()).degree()==0
    genus=(p-1)*(N-1-J.degree())
    assert (pow(K,-1,p)*(genus+N-1))%p==S%p
    return dict(p=p,ell=ell,q=q,S=S,N=N,K=K,L=L,A_terms=len(A.terms()),
                gcd_degree=J.degree(),factor_degrees=degrees,genus=genus,
                geometric_p_rank=genus,trace_F=0,trace_F_L=(K*S)%p)

def cubic(p):
    count=0
    for a,b,y1,y2,y3,t in product(range(p),repeat=6):
        value=t*t-t-y1*(a*a-a)-y2*(b*b-b)-y3*(1-a)*(1-b)
        count+=(value%p==0)
    expected=p**5+3*p**3
    assert count==expected
    return dict(p=p,count=count,expected=expected)

def binary_full_tag():
    ell,q=17,11;N=ell*q
    R=sorted({i*i%ell for i in range(1,ell)})
    C=P(sum(x**(q*i) for i in R),2)
    G=P(sum(x**(q*i) for i in range(ell)),2)
    E=P(sum(x**(ell*j) for j in range(q)),2)
    packed=P(1,2)+C+P(x**ell,2)*G
    H=E+(P(1,2)+E)*packed;B=P(x**N-1,2)
    T=H**4+P(x,2)*B**2
    J=sp.gcd(H,B).monic()
    assert sp.gcd(T,T.diff()).monic()==J**2
    assert J.degree()==80
    degrees=sorted(f.degree() for f,e in sp.factor_list(J)[1] for _ in range(e))
    assert degrees==[40,40]
    assert H.degree()==363 and T.degree()==1452
    odd=sorted(e[0][0] for e in T.terms() if e[0][0]%2)
    assert odd==[1,375]
    return dict(N=N,K=80,L=40,H_degree=H.degree(),T_degree=T.degree(),
                double_roots=J.degree(),factor_degrees=degrees,odd_exponents=odd)

if __name__=='__main__':
    result=dict(unit_examples=[unit_example(p,e,q,S) for p,e,q in [(2,7,23),(3,11,23)] for S in range(3)],
                binary_full_tag=binary_full_tag(),cubic_examples=[cubic(p) for p in [2,3,5]])
    print(json.dumps(result,indent=2))
