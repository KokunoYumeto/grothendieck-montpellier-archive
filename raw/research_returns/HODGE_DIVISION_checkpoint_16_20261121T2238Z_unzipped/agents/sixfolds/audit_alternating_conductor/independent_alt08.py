#!/usr/bin/env python3
"""Independent exact supplement for HD-ALT08; no author imports.

Formal polynomials use a tiny integer dictionary implementation.
Young dimensions are reconstructed by individual hook lengths.
Finite inequalities are integer cross-products, with no radical rounding.
"""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from math import factorial, comb
from pathlib import Path
import json
import time

start=time.perf_counter()
root=Path(__file__).resolve().parents[3]
proof=root/'research'/'ordinary_alternating_conductor_section.tex'

def add(*items):
    result={}
    for item in items:
        for key,value in item.items():result[key]=result.get(key,0)+value
    return {key:value for key,value in result.items() if value}
def scale(item,value):return {key:value*coefficient for key,coefficient in item.items() if value*coefficient}
def mul(a,b):
    result={}
    for (i,j),u in a.items():
        for (k,l),v in b.items():
            key=(i+k,j+l);result[key]=result.get(key,0)+u*v
    return {key:value for key,value in result.items() if value}
one={(0,0):1};c={(1,0):1};n={(0,1):1}
den=mul(add(n,scale(one,-1)),add(n,scale(one,-2)))
numerator=mul(mul(c,n),add(n,scale(one,-1),scale(mul(c,n),-1)))
target=mul(c,add(mul(add(scale(one,2),scale(c,-3)),n),scale(one,-2),scale(c,2)))
assert add(numerator,scale(mul(mul(c,add(one,scale(c,-1))),den),-1),scale(target,-1))=={}

def shift_quadratic(coeffs,offset):
    # Coefficients are ordered by increasing degree.
    answer=[0,0,0]
    for i,value in enumerate(coeffs):
        for j in range(i+1):answer[j]+=value*comb(i,j)*offset**(i-j)
    return answer
polynomials={
    'n_squared_minus_3n_minus_6':shift_quadratic([-6,-3,1],15),
    '49n_squared_minus_595n_plus_480':shift_quadratic([480,-595,49],15),
}
assert polynomials=={'n_squared_minus_3n_minus_6':[174,27,1],
                     '49n_squared_minus_595n_plus_480':[2580,875,49]}
assert all(value>0 for values in polynomials.values() for value in values)
assert Fraction(15,256)>Fraction(1,20)

def partitions(total,maximum=None):
    if total==0:
        yield ()
        return
    maximum=min(total,maximum if maximum is not None else total)
    for first in range(maximum,0,-1):
        for rest in partitions(total-first,first):yield (first,)+rest

def hook_degree(shape):
    size=sum(shape);denominator=1
    for i,row in enumerate(shape):
        for j in range(row):
            below=sum(next_row>j for next_row in shape[i+1:])
            denominator*=row-j+below
    assert factorial(size)%denominator==0
    return factorial(size)//denominator

young_checks=0
for nn in range(15,41):
    for k in range(1,(nn-1)//4+1):
        for tail in partitions(k):
            degree=hook_degree((nn-k,)+tail)
            if k==1:assert degree==nn-1
            else:assert degree>=nn*(nn-3)//2
            young_checks+=1

threshold_checks=0
by_h={}
for h in range(4,81):
    count=0
    values=set(range(15,161))|{5*h-1,5*h,5*h+1,10*h+3}
    for nn in sorted(values):
        for k in range(1,(nn-1)//4+1):
            # Since k/n<1/4<1/2, this is precisely k/n>=c_h.
            if 5*h*k*(nn-k)<nn*nn:continue
            e=(nn-1)**2 if k==1 else nn*(nn-3)//2
            left=5*h*e*k*(nn-1-k)
            right=(e+3*h)*(nn-1)*(nn-2)
            assert left>right,(h,nn,k,e,left,right)
            count+=1
    by_h[h]=count;threshold_checks+=count

dimension=hook_degree((94,6))
assert dimension==1116764880
assert dimension==comb(100,6)-comb(100,5)
beta=Fraction(6*93,99*98)
assert beta==Fraction(31,539)
assert beta<Fraction(1,10)
assert beta>Fraction(1,20)+Fraction(3,5*dimension)

result={'status':'PASS','completed_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-start,
        'proof_sha256':sha256(proof.read_bytes()).hexdigest(),
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'formal_difference_identity':True,
        'positive_shifted_coefficients_in_increasing_order':polynomials,
        'hook_dimension_checks':young_checks,
        'integer_threshold_checks':threshold_checks,
        'tested_h':list(range(4,81)),
        'counts_by_h':by_h,
        'strictness_witness':{'shape':[94,6],'hook_degree':dimension,'beta':str(beta)},
        'author_code_imported':False,
        'scope':'Exact universal polynomial identity, finite integer inequalities and finite hook dimensions; no numerical proof of the classification, normalizer, or source existence.'}
Path(__file__).with_name('independent_alt08_checked.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({key:value for key,value in result.items() if key not in {'tested_h','counts_by_h'}},indent=2))
