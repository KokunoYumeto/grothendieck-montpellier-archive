#!/usr/bin/env python3
"""Exact rank-five, field Q(sqrt5) full-character test.

The 120 candidates are the rank-two determinant-fixed matrices in the
prescribed mod5 row/column spaces.  This is a necessary character test,
not an object construction or an all-rank obstruction.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,time
import rm_integral_character_search as ex

start=time.monotonic()
U=[[1,2,0,0],[2,-1,0,0],[0,0,1,2],[0,0,2,-1]]
theta=ex.hermitian_real([[int(i==j)for j in range(4)]for i in range(4)])
eta=ex.hermitian_real(U)
pt=ex.divpow(theta,2);pe=ex.divpow(eta,2)
t={m:F(pt[m],2)+F(pe[m],10)for m in ex.M4}
assert ex.wedge(t,t).get(255)==2
assert all((5*v).denominator==1 for v in t.values())
P=[[1,0],[2,0],[0,1],[0,2]]
tested=0;ch2_ok=0;integral=[];ch3_denominators={}
for a,b,c,d in product(range(5),repeat=4):
    if (a*d-b*c)%5!=3:continue
    tested+=1;K=[[a,b],[c,d]]
    M=[[sum(P[i][s]*K[s][u]*P[j][u]for s in range(2)for u in range(2))%5
        for j in range(4)]for i in range(4)]
    coeff=[M[i][i]for i in range(4)]
    for i,j in ex.combinations(range(4),2):
        coeff.extend([3*(M[i][j]+M[j][i])%5,4*(M[i][j]-M[j][i])%5])
    A=ex.from_coeff(coeff);pa=ex.divpow(A,2)
    if any((F(pa[m],5)-t[m]).denominator!=1 for m in ex.M4):continue
    ch2_ok+=1
    p3=ex.divpow(A,3);at=ex.wedge(ex.divpow(A,1),t)
    den=sorted({(F(p3[ex.mask(ix)],25)-F(at.get(ex.mask(ix),0),5)).denominator for ix in ex.I6})
    key=','.join(map(str,den));ch3_denominators[key]=ch3_denominators.get(key,0)+1
    out=ex.candidate(5,coeff,t,4)
    if out:integral.append(out)
assert tested==120
out={'status':'EXACT FIXED-RANK NECESSARY CHARACTER TEST','field_radicand':5,
     'rank':5,'polarization_product':1,'r_times_q':1,'self_Euler':4,
     'mod5_rank2_candidates':tested,'ch2_integral_candidates':ch2_ok,
     'ch3_denominator_distributions':ch3_denominators,
     'integral_full_characters':integral,'elapsed_seconds':time.monotonic()-start,
     'actual_object_constructed':False,'all_rank_obstruction_claimed':False}
Path(__file__).with_name('rm_field5_character_search_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
