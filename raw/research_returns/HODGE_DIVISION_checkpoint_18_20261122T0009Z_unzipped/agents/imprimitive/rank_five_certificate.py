#!/usr/bin/env python3
"""Exact scalar-field, spectrum and CW checks for the rank-five reduction.

Published reflection classification and normalizer inputs are not verified
by this script.  It constructs no generating tuple and asserts no dominance.
"""
from pathlib import Path
from fractions import Fraction
from functools import reduce
from math import gcd,prod
import json,sympy as sp

ROOT=Path(__file__).resolve().parent
x=sp.symbols('x')
omega=(-1+sp.sqrt(-3))/2
orders=[1,2,3,4,5,6,8,10,12]
rows=[];degree_two=[]
for d in orders:
    factors=sp.factor_list(sp.cyclotomic_poly(d,x),extension=sp.sqrt(-3))[1]
    ds=[int(sp.degree(f,x)) for f,e in factors]
    assert len(set(ds))==1
    if ds[0]==2:degree_two.append(d)
    rows.append({'scalar_order':d,'factor_degrees_over_Qomega':ds})
assert degree_two==[4,12]
spectral=[]
for d in degree_two:
    mod=sp.Poly(sp.cyclotomic_poly(d,x),x,domain=sp.QQ)
    # x is a primitive scalar root.  The other eigenvalue of w is eps*x^4.
    assert sp.rem(sp.Poly(x**d,x,domain=sp.QQ),mod).is_one
    square_reflection_order=d//gcd(d,10)
    for eps in [1,-1]:
        # Product of (+x^-1)^2,(-x^-1)^2,eps*x^4 is eps.
        assert sp.cancel((x**-1)**2*(-x**-1)**2*(eps*x**4))==eps
        assert sp.expand((eps*x**5)**2)==x**10
        spectral.append({'scalar_order':d,'det_w':eps,'g_last_eigenvalue':f'{eps}*zeta_{d}^5',
                         'order_of_nontrivial_eigenvalue_of_g_squared':square_reflection_order,
                         'allowed_by_G33_order_two_reflections':square_reflection_order==2})
assert all(r['allowed_by_G33_order_two_reflections']==(r['scalar_order']==4) for r in spectral)
degrees=[4,6,10,12,18]
assert prod(degrees)==51840
assert reduce(gcd,degrees)==2
gplus=[Fraction(0),Fraction(0),Fraction(1,2),Fraction(1,2),Fraction(1,4)]
gminus=[Fraction(0),Fraction(0),Fraction(1,2),Fraction(1,2),Fraction(3,4)]
age=10*Fraction(1,2)+sum(gplus)+sum(gminus)
moving=10+sum(q!=0 for q in gplus)+sum(q!=0 for q in gminus)
assert age==8 and moving==16
assert age-5==3 and moving-age-5==3
real_boundary=[]
for ell in [0,2,4]:
    q=(10-ell)//2;h0=(5-ell)//2
    assert q-h0==3
    real_boundary.append({'shortest_reflection_length':ell,'equal_pairs':q,'max_tail_fixed_dimension':h0,'graph_rank_lower':q-h0})
out={'status':'PASS exact field/spectral/CW and real-boundary arithmetic',
     'published_classification_reproved':False,'generating_tuple_constructed':False,'dominance_or_actual_nonsplitness_claimed':False,
     'cyclotomic_cases':rows,'outside_F_orders_before_reflection_test':degree_two,'spectral_cases':spectral,
     'remaining_group_order':2*prod(degrees),'remaining_field':'Q(zeta12)','remaining_non_Eisenstein_quadratic_field':'Q(i)',
     'branch_profile':{'reflections':10,'outside_order_four_rank_three':2,'total_moving':moving,'total_age':str(age),'multiplicities':[3,3]},
     'real_boundary_cases':real_boundary}
(ROOT/'rank_five_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
