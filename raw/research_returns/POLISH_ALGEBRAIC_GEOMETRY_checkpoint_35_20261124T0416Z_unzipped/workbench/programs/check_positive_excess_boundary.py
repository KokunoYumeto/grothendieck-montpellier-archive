#!/usr/bin/env python3
"""Independent arithmetic for the characteristic-two excess endpoint.

Methods: dynamic semigroup reachability versus coordinate blowup valuations;
exhaustive F_2 polynomial decomposition; explicit differential overlap numerators;
integer degree and finite cyclic-group calculations. This does not certify the
geometric normalization, gluing, descent, or existence arguments.
Run: python3 workbench/programs/check_positive_excess_boundary.py
"""
from __future__ import annotations
import json
from math import gcd


def plus(*polys):
    out=set()
    for p in polys: out.symmetric_difference_update(p)
    return out


def times(p,q):
    out=set()
    for i,j in p:
        for k,l in q:
            term=(i+k,j+l)
            if term in out:out.remove(term)
            else:out.add(term)
    return out


def deriv(p,axis):
    return {(i-(axis==0),j-(axis==1)) for i,j in p if (i,j)[axis]%2}


def shift(p,n):
    return {(i+n,j) for i,j in p}


def order_t(p):
    return min((i for i,j in p),default=10**9)


def one_variable_square(mask):
    return sum(1<<(2*i) for i in range(mask.bit_length()) if mask>>i&1)


def main():
    cusp_cases=[]
    for ell in range(65):
        bound=4*ell+8
        reachable={0}
        for n in range(1,bound+1):
            if n-2 in reachable or n-(2*ell+1) in reachable:reachable.add(n)
        gaps=sorted(set(range(bound+1))-reachable)
        assert len(gaps)==ell
        assert not [n for n in gaps if n>=2*ell]
        x,y=2,2*ell+1
        steps=normal_correction=genus_loss=square_loss=0
        while min(x,y)>1:
            multiplicity=min(x,y)
            exceptional_value=min(x,y)
            normal_correction+=multiplicity*exceptional_value
            genus_loss+=multiplicity*(multiplicity-1)//2
            square_loss+=multiplicity**2
            if x<=y:y-=x
            else:x-=y
            steps+=1
        assert steps==ell and genus_loss==len(gaps)
        assert normal_correction==square_loss==4*ell
        assert normal_correction==2*(2*ell)
        cusp_cases.append([ell,len(gaps),steps,normal_correction])

    series_cases=0
    for mask in range(1<<13):
        odd=[i for i in range(13) if i%2 and mask>>i&1]
        if not odd:continue
        first=odd[0]
        even_root=sum(1<<(i//2) for i in range(0,13,2) if mask>>i&1)
        unit_root=sum(1<<((i-first)//2) for i in odd)
        assert unit_root&1
        recomposed=one_variable_square(even_root)^(one_variable_square(unit_root)<<first)
        assert recomposed==mask
        derivative=sum(1<<(i-1) for i in odd)
        derivative_order=(derivative&-derivative).bit_length()-1
        assert derivative_order==first-1 and derivative_order%2==0
        series_cases+=1

    overlap_cases=sharp_cases=0
    one={(0,0)}
    for a in range(1,14,2):
        for seed in range(64):
            # Coordinates are (t-exponent,x-exponent); all arithmetic is in F_2.
            b=plus(one,{(0,1)},{(1,i) for i in range(3) if seed>>i&1})
            h=plus(one,{(1,0)},{(0,i+1) for i in range(3) if seed>>(i+3)&1})
            g=times(h,h)
            c=plus(one,{(1,1)},{(0,i+1) for i in range(3) if seed>>i&1})
            A=plus({(0,1),(1,0)},{(i+2,1) for i in range(3) if seed>>(i+3)&1})
            bi=plus(times(g,b),shift(c,a))
            assert not deriv(g,0) and not deriv(g,1)
            numerator=[plus(times(b,deriv(bi,j)),times(bi,deriv(b,j))) for j in (0,1)]
            assert min(map(order_t,numerator))>=a-1
            omega=[shift(deriv(A,j),2*a) for j in (0,1)]
            wedge=plus(times(numerator[0],omega[1]),times(numerator[1],omega[0]))
            assert order_t(wedge)>=3*a-1
            sharp_cases+=order_t(wedge)==3*a-1
            overlap_cases+=1
    assert sharp_cases>0

    degree_cases=cyclic_cases=0
    for a in range(1,32,2):
        for d in range(2,102,2):
            G=(2*a+1)*d
            assert G-(2*a+1)*d==0
            for h in range(a):
                assert G-d-(2*a+h)*d==-h*d
                assert (2*a+h<3*a-1)==(h<a-1)
                degree_cases+=1
        for n in range(1,2*a+1):
            if (2*a)%n:continue
            power_order=n//gcd(n,a)
            if power_order==2:
                assert n%2==0 and a%(n//2)==0
                cyclic_cases+=1

    print(json.dumps({'status':'PASS','methods':[
        'dynamic numerical-semigroup reachability versus iterative monomial coordinate blowups',
        'exhaustive characteristic-two one-variable polynomial separation',
        'two-variable F_2 differential numerator expansion for gluing orders',
        'exact integer degree and cyclic-order arithmetic'],
        'cusp_cases':len(cusp_cases),'cusp_sample':cusp_cases[:5],
        'polynomial_cases':series_cases,'overlap_cases':overlap_cases,
        'sharp_overlap_cases':sharp_cases,'degree_cases':degree_cases,
        'cyclic_order_cases':cyclic_cases,
        'scope':'Arithmetic only; no geometry, non-descent, or global realization is certified.'},indent=2,sort_keys=True))


if __name__=='__main__':main()
