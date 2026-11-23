#!/usr/bin/env python3
"""AM-DO-067: exact t<=9 trace rigidity with block rank at most one."""
from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from fractions import Fraction as F
from math import comb
from pathlib import Path
import sympy as sp

HERE=Path(__file__).parent; checks=[]
def ck(value,label):
    if not value: raise AssertionError(label)
    checks.append(label)

hp=HERE/'definite_oscillator_large_t_certificate.json'
row=next(x for x in json.loads(hp.read_text())['rows'] if x['host']=='J56')
Q=row['g0']*row['g1']; T=int(row['T']); f=168; n=169; m=164; H=8192
def bounds(k,h):
    h=F(h)
    return (h+2*k-2+1/h,
            (2*k-3)*(h+1/h)+comb(k-2,2)+1+(k-1)*(k-2)+comb(k,2))

rows=[]
for r,k,margin2 in ((0,6,119),(1,7,22)):
    ck(n-(m-r-1)==k,'actual_positive_fixed_complement_dimension')
    b1,b2=bounds(k,H)
    for j,(b,margin) in enumerate(((b1,1184),(b2,margin2)),1):
        lhs=Q**(2*(f-1))*b.denominator**(2*f)
        for t in range(10):
            rhs=b.numerator**(2*f)*T**(2*t)
            ck(lhs>2**margin*rhs,'every_t_le_nine_exact_norm_contradiction')
        ck(lhs<b.numerator**(2*f)*T**20,
           'ten_transition_test_not_claimed')
        rows.append({'r_max':r,'residual_dimension':k,'coefficient':j,
                     'bound':str(b),'t9_inverse_binary_margin_at_least':margin})
ck(bounds(6,H)[1]==9*(H+F(1,H))+42,'exact_scalar_block_second_bound')
ck(bounds(7,H)[1]==11*(H+F(1,H))+62,'exact_rank_one_block_second_bound')
b8=bounds(8,H)[1]
ck(Q**(2*(f-1))*b8.denominator**(2*f)<b8.numerator**(2*f)*T**18,
   'rank_two_block_not_covered_by_this_t9_test')

# The enlarged DO065 counts do not use the value of t once unipotence is
# proved. The newly eligible t=9 subfamily is contained in the same counts.
ck((89-9+1)+(106-9+1)==179 and 179<2**8,
   'new_t9_nonscalar_subset_union')
ck((46-9+1)+(16-10+1)==45 and 179+45==224 and 224<2**8,
   'exact_new_cross_cells_and_complete_new_union')
# DO066 already used the full 2^v bound, so adding t=9 requires no
# increase of that bound or of the number of (s,v) cells.
for v in range(11):
    ck(sum(comb(v,u) for u in range(max(0,v-9),v+1))<=2**v,
       'enlarged_t9_type_sum_same_bound')

# Exact signature-one spectral diagnostics for the carried B1/B2
# estimates and the coefficient translation identity.
models=0
phases=(sp.Integer(1),sp.Integer(-1),sp.I,-sp.I)
for k in range(2,8):
    for R in (1,2,3,5):
        c=sp.Rational(R*R+1,2*R); s=sp.Rational(R*R-1,2*R)
        ck(c*c-s*s==1,'exact_hyperbolic_pair_unitarity')
        for shift in range(4):
            positive=[phases[(i+shift)%4] for i in range(k-2)]
            trh=2*c+sum(positive)
            trh2=2*(c*c+s*s)+sum(z*z for z in positive)
            e2h=sp.expand((trh*trh-trh2)/2)
            e1n=sp.expand(trh-k)
            trn2=sp.expand(trh2-2*trh+k)
            e2n=sp.expand((e1n*e1n-trn2)/2)
            ck(sp.expand(e2n-e2h+(k-1)*trh-comb(k,2))==0,
               'exact_second_coefficient_translation')
            bb=bounds(k,R)
            for value,b in zip((e1n,e2n),bb):
                square=sp.expand(value*sp.conjugate(value))
                ck(square<=sp.Rational(b.numerator,b.denominator)**2,
                   'exact_small_spectral_coefficient_bound')
            models+=1

out={'finding':'AM-DO-067','status':'PASS',
     'timestamp_utc':datetime.now(timezone.utc).isoformat(),
     'exact_assertions':len(checks),'coefficient_norm_rows':rows,
     'new_t9_nonscalar_cells':179,'new_t9_cross_cells':45,
     'new_t9_union_cells':224,'spectral_models':models,
     'checks':checks,'input_sha256':{hp.name:hashlib.sha256(hp.read_bytes()).hexdigest()},
     'scope':'Actual K068 J56 residual with rank(A-I)<=1 and t<=9. No general higher-r t9 or t10 unipotence; absolute sums only at carried eligible cells.'}
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,
 default=HERE/'definite_oscillator_small_block_trace_certificate.json')
path=ap.parse_args().output;path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('checks','input_sha256')},indent=2))
