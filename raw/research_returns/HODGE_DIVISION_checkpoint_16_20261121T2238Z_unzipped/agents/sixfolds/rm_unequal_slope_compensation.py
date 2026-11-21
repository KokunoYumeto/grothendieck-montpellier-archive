#!/usr/bin/env python3
"""Exact positive integral hull compensation for the unequal-slope test.

This constructs a split bundle's character, not a semiregular object.
"""
from pathlib import Path
from itertools import product
from functools import reduce
from math import lcm
import json
import sympy as s

root=Path(__file__).resolve().parent
u=s.sqrt(2)
q=s.Rational(1,2)
scaleD=3
signs=list(product((-1,1),repeat=4))


def coeff(v):
    return s.Matrix([s.prod(v[i] for i in range(4) if (mask>>i)&1)
                     for mask in range(16)])


def mult(a,b):
    out=[s.S.Zero]*16
    for i in range(16):
        for j in range(16):
            if not i&j:
                out[i|j]+=a[i]*b[j]
    return s.Matrix([s.simplify(x) for x in out])


target=s.zeros(16,1);target[0]=1;target[3]=target[12]=-q;target[15]=q*q
mh=s.zeros(16,1);mh[0]=1
for mask in range(16):
    if mask.bit_count()==3:mh[mask]=-12*scaleD**3
mh[15]=96*scaleD**4
mhres=2*coeff([-scaleD]*4)-2*coeff([-3*scaleD]*4)+coeff([-4*scaleD]*4)
assert mh==mhres
inverse=s.zeros(16,1);inverse[0]=1
for mask in range(1,16):inverse[mask]=-mh[mask]
assert mult(mh,inverse)==s.eye(16)[:,0]
hull=mult(target,inverse)


def nearest(v):
    # Exact floor in the real quadratic field; half-integer ties do not arise
    # in the nonrational entries. Rational entries here are integral.
    return int(s.floor(v+s.Rational(1,2)))


trials=[]
found=None
for R in (4,8,16,32,64,128):
    divisors=[];columns=[]
    for eps in signs:
        v=[R*x for x in eps]
        a=nearest(sum(v)/s.Integer(4))
        b=nearest((v[0]+v[1]-v[2]-v[3])/(4*u))
        c=nearest((v[0]-v[1]+v[2]-v[3])/s.Integer(4))
        d=nearest((v[0]-v[1]-v[2]+v[3])/(4*u))
        lam=[a+b*u+c+d*u,a+b*u-c-d*u,
             a-b*u+c-d*u,a-b*u-c+d*u]
        divisors.append([a,b,c,d])
        columns.append(coeff(lam))
    M=s.Matrix.hstack(*columns)
    if M.det()==0:
        trials.append({'scale':R,'result':'singular character matrix'});continue
    weights=[s.simplify(x) for x in M.inv()*hull]
    assert all(x.is_Rational for x in weights)
    assert M*s.Matrix(weights)==hull
    positive=all(x>0 for x in weights)
    trials.append({'scale':R,'positive':bool(positive),'minimum_weight':str(min(weights))})
    if not positive:continue
    r=reduce(lcm,(int(x.q) for x in weights),1)
    multiplicities=[int(r*x) for x in weights]
    assert sum(multiplicities)==r and all(n>0 for n in multiplicities)
    actual=M*s.Matrix(multiplicities)
    assert actual==r*hull
    assert mult(actual,mh)==r*target
    found={'scale':R,'rank':r,'q':str(q),'divisor_basis':['theta','theta_U','theta_S','theta_US'],
           'summands':[{'coefficients':v,'multiplicity':n,'normalized_weight':str(w)}
                       for v,n,w in zip(divisors,multiplicities,weights)],
           'normalized_hull_character_subset_coefficients':[str(x) for x in hull],
           'unit_modification_character_subset_coefficients':[str(x) for x in mh],
           'full_balanced_target_subset_coefficients':[str(x) for x in target]}
    break
assert found is not None
out={'result':'PASS','construction':found,'trials':trials,
     'limits':'The hull is a split direct sum of actual integral-divisor line bundles. This is not a semiregular seed, and no finite action or nonsplit hull is constructed.'}
(root/'rm_unequal_slope_compensation_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'result':'PASS','scale':found['scale'],'rank':found['rank'],'trials':trials},indent=2))
