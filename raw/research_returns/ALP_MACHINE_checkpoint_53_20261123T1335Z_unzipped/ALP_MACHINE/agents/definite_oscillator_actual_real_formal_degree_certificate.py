#!/usr/bin/env python3
"""Exact normalization diagnostics for AM-DO-048; no automorphic evaluation."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial, prod
from pathlib import Path
import json

checks=0
groups=Counter()
def check(ok,group):
    global checks
    assert ok,(group,checks)
    checks+=1
    groups[group]+=1

def weyl(weight):
    return prod((F(weight[i]-weight[j]+j-i,j-i)
                 for i,j in combinations(range(len(weight)),2)),start=F(1))

def vand(h):
    return prod((F(h[i]-h[j],j-i)
                 for i,j in combinations(range(len(h)),2)),start=F(1))

# Arbitrary small dominant minimal types: both formulae and invariances.
for a in range(1,8):
    for jumps in product(range(3),repeat=min(a-1,4)):
        delta=list(jumps)+[1]*max(0,a-1-len(jumps))
        alpha=[sum(delta[i:]) for i in range(a)]
        for gap in (1,2,5):
            beta=alpha[-1]-a-gap
            p=[F(alpha[i])+F(a-2,2)-i for i in range(a)]
            pm=F(beta)+F(a,2)
            h=p+[pm]
            rho=[F(a,2)-i for i in range(a+1)]
            highest=[h[i]-rho[i] for i in range(a+1)]
            c=prod(x-pm for x in p)
            d=weyl(alpha)*c
            check(all(x.denominator==1 for x in highest),"integral HC weight")
            check(all(h[i]>h[i+1] for i in range(a)),"holomorphic chamber")
            check(d==factorial(a)*weyl(highest),"minimal type versus compact dual")
            check(d==factorial(a)*vand(h),"HC root product")
            check(weyl(alpha).denominator==1 and d.denominator==1,"dimension integrality")
            for shift in (-7,3):
                check(vand([x+shift for x in h])==vand(h),"unitary determinant shift")
            check(vand([-x for x in reversed(h)])==vand(h),"contragredient invariance")
            # FD10 is d_alpha/d=1/c, not 1/d for vector-valued evaluation.
            check(weyl(alpha)/d==1/c,"vector versus scalar Schur sum")

# Independent scalar beta integral using integer factorials.
for a in range(1,11):
    for lam in range(a+1,a+15):
        beta_integral=F(factorial(lam-a-1),factorial(lam-1))
        degree=prod(lam-j for j in range(1,a+1))
        check(beta_integral*degree==1,"scalar beta calibration")
        p=[F(a-2,2)-i for i in range(a)]
        pm=-lam+F(a,2)
        check(prod(x-pm for x in p)==degree,"scalar HC calibration")

# Actual-profile factorization in independent small exact Weyl models.
for a,ell,E,q in product((2,4,6,8),(1,3,7),(2,11,31),(0,1,2)):
    p=[4*ell*(a-1-i) for i in range(a-1)]+[-E+ell]
    pm=-E-ell-q
    alpha=[F(p[i])-F(a-2,2)+i for i in range(a)]
    compact=F((4*ell)**((a-1)*(a-2)//2),factorial(a-1))
    compact*=prod(E+(4*j-1)*ell for j in range(1,a))
    c=(2*ell+q)*prod(E+(4*j+1)*ell+q for j in range(1,a))
    check(compact==weyl(alpha),"closed compact factor")
    check(c==prod(x-pm for x in p),"closed noncompact factor")
    check(compact*c==factorial(a)*vand(p+[pm]),"closed full formal degree")

# Use the already certified K044 integers, not floating-point exponentials.
base=Path(__file__).resolve().parent
hosts=json.loads((base/'enlarged_gap_admissible_interval_certificate.json').read_text())['hosts']
tables=[]
for host in hosts:
    a=host['a'];f=host['f']
    emn=host['ell_min'];emx=host['ell_max']
    check(a==f and a in (42,168),"actual ranks")
    check(emx<2**485,"actual ell upper bound")
    for role,entry in host['roles'].items():
        E=entry['E']
        bound={'top':2**955+2**485,'thick':2**495,'thin':2**485}[role]
        check(E<bound,"actual role upper bound")
        for ell in (emn,emx):
            for q in (0,ell):
                p=[4*ell*(a-1-i) for i in range(a-1)]+[-E+ell]
                pm=-E-ell-q
                h=p+[pm]
                check(all(h[i]>h[i+1] for i in range(a)),"actual HC chamber")
                alpha=[p[i]-(a-2)//2+i for i in range(a)]
                beta=pm-a//2
                check(all(alpha[i]>=alpha[i+1] for i in range(a-1)),"actual minimal dominance")
                check(alpha[-1]-beta>a,"actual Nakahama convergence")
                for i in range(a):
                    check(alpha[i]-beta-i-1==p[i]-pm,"actual exact Nakahama shift")
                for i,j in combinations(range(a+1),2):
                    check(0<h[i]-h[j]<2**960,"actual all root differences")
                # Counter identity retains every linear factor without huge products.
                left=Counter(p[i]-pm for i in range(a))
                right=Counter([2*ell+q]+[E+(4*j+1)*ell+q for j in range(1,a)])
                check(left==right,"actual exact noncompact factor list")
                numerator=Counter(p[i]-p[j] for i,j in combinations(range(a),2))
                rhs=Counter(4*ell*(j-i) for i,j in combinations(range(a-1),2))
                rhs.update(E+(4*j-1)*ell for j in range(1,a))
                check(numerator==rhs,"actual exact compact factor list")
    exponent=960*f*a*(a+1)//2
    tables.append({'host':host['host'],'a':a,'f':f,'product_formal_degree_less_than_2_power':exponent})

# Haar rescaling: d'=d/nu and actual test nu/d, including the two-edge energy.
for degree,compact,nu,s0,s1 in product((3,7,20),(1,4),(F(1,3),F(5)),(F(1),F(2)),(F(1),F(3))):
    check(1/(F(degree)/nu)==nu/degree,"Haar reciprocal formal degree")
    check((s0*s1)**2*nu/(degree*compact)==(s0*s1)**2*(nu/degree)/compact,"oscillator test scalar retention")
    check((nu/degree)/compact/(s0*s1)**2==nu/(degree*compact*(s0*s1)**2),"fixed-test multiplicity inverse scalar")

out={'finding':'AM-DO-048','status':'PASS','time_utc':datetime.now(timezone.utc).isoformat(),
     'assertions':checks,'groups':dict(groups),'actual_hosts':tables,
     'scope':'Exact representation/measure normalization diagnostics; no automorphic value or global inverse computation.'}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
