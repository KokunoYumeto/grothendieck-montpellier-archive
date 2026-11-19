#!/usr/bin/env python3
"""Exhaustive finite-field checks for SA06 A.1/A.8; pure Python.

General Weierstrass models are used at p=2,3. For p>3 every
elliptic curve has a short model, and all isomorphisms of short
models are the scaling changes used below. No random sampling.
"""
from itertools import product
from collections import Counter
from math import gcd, isqrt
from pathlib import Path
import json, time

def discriminant(a,p):
    a1,a2,a3,a4,a6=a
    b2=a1*a1+4*a2
    b4=a1*a3+2*a4
    b6=a3*a3+4*a6
    b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    return (-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6)%p

def points(a,p):
    a1,a2,a3,a4,a6=a
    return [(x,y) for x,y in product(range(p),repeat=2)
            if (y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6)%p==0]

def change(a,p,u,r,s,t):
    a1,a2,a3,a4,a6=a
    ns=[a1+2*s,a2-s*a1+3*r-s*s,a3+r*a1+2*t,
        a4-s*a3+2*r*a2-(t+r*s)*a1+3*r*r-2*s*t,
        a6+r*a4+r*r*a2+r**3-t*a3-r*t*a1-t*t]
    return tuple(n*pow(pow(u,w,p),-1,p)%p for n,w in zip(ns,[1,2,3,4,6]))

def small(p):
    models={a for a in product(range(p),repeat=5) if discriminant(a,p)}
    remaining=set(models); out=[]
    while remaining:
        a=min(remaining)
        orbit={change(a,p,u,r,s,t) for u in range(1,p)
               for r,s,t in product(range(p),repeat=3)}
        assert orbit<=models
        trace=p-len(points(a,p))
        assert all(p-len(points(b,p))==trace for b in orbit)
        aut=(p-1)*p**3//len(orbit)
        out.append(dict(model=a,trace=trace,supersingular=trace%p==0,
                        automorphisms_over_Fp=aut,orbit_size=len(orbit)))
        remaining-=orbit
    return dict(p=p,nonsingular_models=len(models),classes=out,
                ss_classes=sum(x['supersingular'] for x in out),
                trace_zero_classes=sum(x['trace']==0 for x in out))

def class_number(D):
    """Primitive reduced positive binary quadratic forms; D<0, D=0,1 mod4."""
    forms=[]
    for a in range(1,isqrt(abs(D)//3)+2):
        for b in range(-a,a+1):
            if (b*b-D)%(4*a):continue
            c=(b*b-D)//(4*a)
            if a>c or gcd(gcd(a,abs(b)),c)!=1:continue
            if (abs(b)==a or a==c) and b<0:continue
            if b*b-4*a*c==D:forms.append((a,b,c))
    return forms

def odd(p):
    models={(a,b) for a,b in product(range(p),repeat=2)
            if (4*a**3+27*b*b)%p}
    remaining=set(models); ss=[]
    while remaining:
        a,b=min(remaining)
        orbit={(a*pow(u,4,p)%p,b*pow(u,6,p)%p) for u in range(1,p)}
        tr=p-len(points((0,0,0,a,b),p))
        if tr%p==0:
            assert tr==0
            j=1728*4*a**3*pow((4*a**3+27*b*b)%p,-1,p)%p
            roots=[x for x in range(p) if (x**3+a*x+b)%p==0]
            ss.append(dict(model=[a,b],trace=tr,j=j,
                           rational_2torsion_roots=roots,
                           maximal_Fp_endring=(p%4==1 or len(roots)==3)))
        remaining-=orbit
    hm4=len(class_number(-4*p)); hm=len(class_number(-p)) if p%4==3 else 0
    assert len(ss)==hm4+hm
    assert len({x['j'] for x in ss})*2==len(ss)
    assert sum(x['maximal_Fp_endring'] for x in ss)==(hm if p%4==3 else hm4)
    return dict(p=p,ss_classes=len(ss),ss_j=len({x['j'] for x in ss}),
                h_minus4p=hm4,h_minusp=hm,maximal_endring_classes=sum(x['maximal_Fp_endring'] for x in ss),
                classes=ss)

def main():
    start=time.perf_counter()
    result={'small_primes':[small(p) for p in [2,3]],
            'odd_primes':[odd(p) for p in [5,7,11,13,17,19,23,29,31,37,43]]}
    a=(0,0,0,1,0); p=7
    result['counterexample_Rmax']={'field':'F_7','model':'y^2=x^3+x',
        'discriminant':discriminant(a,p),'affine_points':points(a,p),
        'points_total':len(points(a,p))+1,'trace':p-len(points(a,p)),
        'rational_2torsion_x':[x for x in range(p) if (x**3+x)%p==0],
        'reason':'Frobenius is not the identity on geometric E[2]; (1+pi)/2 is not an endomorphism.'}
    result['runtime_seconds']=time.perf_counter()-start
    dest=Path(__file__).with_name('check_supersingular_output.json')
    dest.write_text(json.dumps(result,indent=2)+'\n')
    for row in result['small_primes']:
        print('p=',row['p'],'supersingular Fp-classes=',row['ss_classes'],
              'trace-zero=',row['trace_zero_classes'],
              'traces=',Counter(x['trace'] for x in row['classes'] if x['supersingular']))
    for row in result['odd_primes']:
        print('p=',row['p'],'ss=',row['ss_classes'],'j=',row['ss_j'],
              'h(-4p)=',row['h_minus4p'],'h(-p)=',row['h_minusp'],
              'maximal R=',row['maximal_endring_classes'])
    print('counterexample',result['counterexample_Rmax'])
    print('runtime_seconds',result['runtime_seconds'])

if __name__=='__main__':main()
