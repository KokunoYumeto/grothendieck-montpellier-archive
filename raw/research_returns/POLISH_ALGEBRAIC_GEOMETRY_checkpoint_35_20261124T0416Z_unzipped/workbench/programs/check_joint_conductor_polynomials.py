#!/usr/bin/env python3
"""Root-authored exact coefficient checks, without SymPy or ratio enumeration.

Polynomial coefficients are exact Fractions in ascending order. Universal
signs are certified by translating to a half-line and inspecting coefficients.
This supplements, and does not replace, the surface-theoretic argument.
"""
from fractions import Fraction as F
from math import comb
import json

def trim(a):
    a=list(map(F,a))
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return trim(c)
def scale(a,c):return trim([x*c for x in a])
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return trim(c)
def deriv(a):return trim([i*a[i] for i in range(1,len(a))] or [0])
def compose(a,b):
    c=[F(0)]
    for x in reversed(a):c=add(mul(c,b),[x])
    return c
def value(a,x):return compose(a,[x])[0]
def diff_ratio(n1,d1,n2,d2):return sub(mul(n1,d2),mul(n2,d1))
def positive_after(a,start):
    b=compose(a,[start,1]);assert b[0]>0 and all(x>=0 for x in b),b
    return list(map(str,b))

# Independent coefficient expansions directly from the three stated ratios.
HN=mul([8,12],[-1,1]);HD=[-1,-1,1]
NN=scale(mul([-1,1],[-4,-4,3]),12);ND=mul([0,1],[15,-12,3])
RN=[0,0,12];RD=[-1,-1,1]
out={}
out['h_decreases_g_ge_2']=positive_after(scale(sub(mul(deriv(HN),HD),mul(HN,deriv(HD))),-1),2)
out['n_decreases_g_ge_5']=positive_after(scale(sub(mul(deriv(NN),ND),mul(NN,deriv(ND))),-1),5)
out['n_exceeds_h_g_ge_5']=positive_after(diff_ratio(NN,ND,HN,HD),5)
for ell in [1,2,3,4]:
    G=[1,F(ell,2)]
    delta_n=diff_ratio(compose(NN,G),compose(ND,G),RN,RD)
    delta_h=diff_ratio(compose(HN,G),compose(HD,G),RN,RD)
    out['n_minus_R_cross_coefficients_ell_'+str(ell)]=list(map(str,delta_n))
    if ell==1:out['hyper_row1_positive_s_ge_4']=positive_after(delta_h,4)
    if ell==2:
        out['hyper_row2_negative_s_ge_4']=positive_after(scale(delta_h,-1),4)
        assert value(delta_n,4)<0 and value(delta_n,5)<0
        out['nonhyper_row2_positive_s_ge_6']=positive_after(delta_n,6)
    if ell==3:
        assert all(value(delta_n,s)<0 for s in range(4,20))
        out['nonhyper_row3_positive_s_ge_20']=positive_after(delta_n,20)
    if ell==4:out['all_larger_rows_negative_s_ge_4']=positive_after(scale(delta_n,-1),4)
assert F(18)>F(88,5) and F(840,47)>F(168,11)
assert F(300,19)-F(800,51)==F(100,969)
# Compare cross-multiplied linear inequality, with no division or enumeration.
assert sub(scale([0,300],51),scale([1,19],800))==[-800,100]
assert 109%12==1
out['internal_a6_cross_difference']=[-800,100]
out['noether_degree_residue_mod12']=11
out['status']='PASS'
out['method']='Exact coefficient arithmetic and positive half-line translations; no symbolic library and no bounded ratio search'
print(json.dumps(out,indent=2,sort_keys=True))
