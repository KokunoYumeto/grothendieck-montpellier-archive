#!/usr/bin/env python3
"""Independent HK301--03 supplement: determinant coefficients + Ramanujan Fourier.
No author program, selected spectrum, or arithmetic helper is imported.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import gcd,lcm,isqrt,comb
from time import perf_counter
import hashlib,json
import sympy as s

HERE=Path(__file__).resolve().parent
PROOF=HERE.parent.parent/'g34_eightfolds/bireflection/hook_three_section.tex'

def partitions(n,cap=None):
    if n==0:
        yield ()
        return
    for first in range(min(n,n if cap is None else cap),0,-1):
        for tail in partitions(n-first,first):
            yield (first,)+tail

@lru_cache(None)
def divisors(n):
    small=[d for d in range(1,isqrt(n)+1) if n%d==0]
    return tuple(small+[n//d for d in reversed(small) if d*d!=n])

@lru_cache(None)
def mobius(n):
    sign=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
        p+=1
    return -sign if n>1 else sign

@lru_cache(None)
def phi(n):
    return sum(d*mobius(n//d) for d in divisors(n))

@lru_cache(None)
def ramanujan(n,k):
    return sum(d*mobius(n//d) for d in divisors(gcd(n,k)))

def exterior_cube_trace(parts,power):
    # det(1+t P(x^power))/(1+t), coefficient t^3.
    poly=[1,0,0,0]
    for length in parts:
        copies=gcd(length,power);cycle=length//copies
        if cycle>3:continue
        sign=1 if cycle%2 else -1
        for _ in range(copies):
            for j in range(3,cycle-1,-1):poly[j]+=sign*poly[j-cycle]
    return poly[3]-poly[2]+poly[1]-poly[0]

def main():
    start=perf_counter();classes=orders=character_powers=0;least=None;rows=[]
    for n in range(15,25):
        degree=comb(n-1,3);A=F(n*n-9*n+8,6);B=F(n*n-2*n-1,8);b=F((n-1)**2,8)
        worst=None;witness=None
        for pp in partitions(n):
            L=lcm(*pp);ds=divisors(L)
            chars={k:exterior_cube_trace(pp,L//k) for k in ds}
            assert chars[1]==degree
            multiplicities={}
            for d in ds:
                numerator=sum(chars[k]*ramanujan(k,L//d) for k in ds)
                assert numerator%L==0
                value=numerator//L;assert value>=0
                multiplicities[d]=value;orders+=1
            assert sum(phi(d)*v for d,v in multiplicities.items())==degree
            ch=exterior_cube_trace(pp,1)
            assert sum(mobius(d)*v for d,v in multiplicities.items())==ch
            f,u,v=pp.count(1),pp.count(2),pp.count(3)
            assert ch==F((f-1)*(f-2)*(f-3),6)-(f-1)*u+v
            assert all(value>=-b for value in chars.values())
            index=n-len(pp)
            if index:
                margin=degree-max(multiplicities.values())-A*index-B
                assert margin>=0
                if worst is None or margin<worst:worst,witness=margin,pp
                if least is None or margin<least:least=margin
            else:
                assert multiplicities=={1:degree}
            classes+=1;character_powers+=len(chars)
        rows.append({'n':n,'minimum_margin':str(worst),'witness':witness})

    n,f,x=s.symbols('n f x')
    degree=(n-1)*(n-2)*(n-3)/6
    A=(n*n-9*n+8)/6;B=(n*n-2*n-1)/8;b=(n-1)**2/8
    upper=(f-1)*(f-2)*(f-3)/6+(n-f)/3
    cf=s.cancel((degree-upper)/(n-f))
    c=s.cancel((degree-n/2+1)/n)
    assert s.expand(cf-c-(f*f+(n-6)*f+1)/6)==0
    gap=s.expand(12*((cf-A)*(n-f)/2-b-B))
    assert s.expand(s.diff(gap,f,2)-(12-6*f))==0
    positive=[gap.subs(f,2),gap.subs(f,n-2),
              2*A*(n-1)+12*B-2*degree-6,
              A+B-40,A+B-b,degree-1-2*(A+B),degree-B,
              18*B-2*(n-1)*(2*n-1)/3-2]
    translated=[]
    for e in positive:
        p=s.Poly(s.expand(e.subs(n,x+15)),x)
        assert min(p.all_coeffs())>=0 and p.eval(0)>0
        translated.append(str(p.as_expr()))
    assert s.expand(2*A*(n-1)-2*degree+2*(n-1)*(2*n-1)/3)==0
    proof_hash=hashlib.sha256(PROOF.read_bytes()).hexdigest()
    assert proof_hash=='6f3918af33aa3f23c2c89d4ac445635a64c00bd981a0d7f5557636a7eb5c6130'
    out={'status':'PASS','proof_sha256':proof_hash,'method':'Truncated determinant-polynomial characters and independent divisor/Ramanujan Fourier; no exterior eigenvalue triples or signed-subset code imported.',
         'partition_classes':classes,'primitive_root_order_multiplicities':orders,
         'exact_character_powers':character_powers,'minimum_support_margin':str(least),
         'universal_positive_polynomials':translated,'rows':rows,'seconds':perf_counter()-start}
    (HERE/'independent_checked.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,sort_keys=True))

if __name__=='__main__':main()
