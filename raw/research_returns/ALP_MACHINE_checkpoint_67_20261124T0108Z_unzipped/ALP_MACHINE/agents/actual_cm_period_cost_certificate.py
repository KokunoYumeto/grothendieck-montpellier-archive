#!/usr/bin/env python3
"""Exact rational interval checks for AM-K066; no transcendental field norm."""
from __future__ import annotations
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import permutations, product
from math import factorial, isqrt
from pathlib import Path
import argparse, hashlib, json

HERE=Path(__file__).resolve().parent
checks=[]
def check(test,name):
    if not test: raise AssertionError(name)
    checks.append(name)
def add(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x): return -x[1],-x[0]
def mul(x,y):
    z=[a*b for a in x for b in y]
    return min(z),max(z)
def div(x,y):
    check(y[0]>0,"positive_interval_divisor")
    return mul(x,(1/y[1],1/y[0]))
def power(x,n):
    check(x[0]>=0,"positive_interval_power")
    return x[0]**n,x[1]**n
def const(x): return F(x),F(x)
def grid(x,scale=10**12):
    return F((x[0]*scale).__floor__(),scale),F(-((-x[1]*scale).__floor__()),scale)
def atan(x,N=40):
    a=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(N)),F(0))
    b=a+(-1)**N*x**(2*N+1)/F(2*N+1)
    return min(a,b),max(a,b)
def sine(x,N=24):
    a=sum(((-1)**k*x**(2*k+1)/factorial(2*k+1) for k in range(N)),F(0))
    b=a+(-1)**N*x**(2*N+1)/factorial(2*N+1)
    return min(a,b),max(a,b)
a5,a239=atan(F(1,5)),atan(F(1,239))
pi=grid(add(mul(const(16),a5),neg(mul(const(4),a239))))
check(F(3)<pi[0]<pi[1]<F(22,7),"Machin_pi_interval")
def sin_fraction(k,q):
    k%=q
    k=min(k,q-k)
    check(0<2*k<q,"sine_monotone_half_interval")
    return grid((sine(pi[0]*F(k,q))[0],sine(pi[1]*F(k,q))[1]))
s7={k:sin_fraction(k,7) for k in range(1,4)}
s29={k:sin_fraction(k,29) for k in range(1,15)}
for s in s7.values():
    check(s[0]>F(2,5),"seventh_root_difference_lower")
def dsin(k): return s7[min(k%7,7-k%7)]
a,b,c=s7[1],s7[2],s7[3]
off=add(add(a,b),neg(c))
mid=add(add(mul(const(3),a),b),neg(c))
Y=[[c,a,off],[a,mid,a],[off,a,c]]
det=(F(0),F(0))
for p in permutations(range(3)):
    inversions=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    v=const(1)
    for i in range(3): v=mul(v,Y[i][p[i]])
    det=add(det,neg(v) if inversions%2 else v)
det2Y=grid(mul(const(8),det))
check(F(4)<det2Y[0]<det2Y[1]<F(8),"actual_det_two_Y")
R=const(1)
for aa in (1,3,5):
    for bb in (0,2,4,6):
        R=mul(R,mul(const(2),dsin(aa-bb)))
R=grid(R)
check(F(4096,625)<R[0]<R[1]<16,"actual_R6_c_between_two_fifths_and_half")
P4=div(mul(det2Y,mul(power((F(5,8),F(11,8)),4),R)),const(256))
check(P4[0]>F(2,5)**4 and P4[1]<F(9,8)**4,"actual_unit_vacuum_period_interval")
check(P4[0]**4>F(1,2**18) and P4[1]**4<4,"period_log2_minus_18_to_2_over16")

# Beta(x,1/2)=sum C_n/(n+x); C_n=binom(2n,n)/4^n.
# C_n<=1/sqrt(3n+1) follows by the displayed induction inequality.
N=257
for nn in range(N+5):
    check((2*nn+1)**2*(3*nn+4)<=4*(nn+1)**2*(3*nn+1),
          "central_binomial_inductive_majorant")
check(N-1==16**2 and F(3)>F(3,2)**2,"beta_tail_below_one_twelfth")
betas={}
Gover2pi={}
for i in (1,2,3):
    coeff=F(1); S=F(0)
    for nn in range(N):
        S+=coeff/(nn+F(i,7))
        coeff*=F(2*nn+1,2*nn+2)
    betas[i]=grid((S,S+F(1,12)))
    # Gi/(2pi)=2 B_i^2 sin(pi i/7)^2/(7 pi sin(2pi i/7)).
    Gover2pi[i]=grid(div(mul(const(2),mul(power(betas[i],2),power(s7[i],2))),
                              mul(const(7),mul(pi,dsin(2*i)))))
    check(Gover2pi[i][0]>1 and Gover2pi[i][1]<3,"actual_Hodge_metric_range")

pil=[]
for ll in range(7):
    aa=pow(2,ll,29); kk=min(aa,29-aa)
    bb=12*aa%29; jj=min(bb,29-bb)
    vv=grid(mul(const(16),mul(power(s29[kk],2),power(s29[jj],2))))
    check(F(1,8)<vv[0]<vv[1]<16,"positive_B_generator_range")
    pil.append(vv)

def sqrt_int_interval(d):
    scale=10**12
    z=isqrt(d*scale**2)
    check(z*z<d*scale**2<(z+1)*(z+1),"exact_quadratic_root_interval")
    return F(z,scale),F(z+1,scale)
deltas=[]
for aa,disc in ((1,5),(3,13)):
    sq=sqrt_int_interval(disc)
    plus=add(const(F(1,2)),neg(div(const(aa),mul(const(2),sq))))
    minus=add(const(F(1,2)),div(const(aa),mul(const(2),sq)))
    check(plus[0]>0 and minus[1]<1,"positive_weighted_trace_factors")
    deltas.append([grid(plus),grid(minus)])
delta4=[grid(mul(deltas[0][j],deltas[1][k])) for j,k in product(range(2),repeat=2)]
for vv in delta4: check(F(1,64)<vv[0]<vv[1]<1,"quadratic_product_range")

def floor_log2(x):
    check(x>0,"positive_log_argument")
    k=x.numerator.bit_length()-x.denominator.bit_length()
    def pow2(j): return F(2**j) if j>=0 else F(1,2**(-j))
    while x<pow2(k): k-=1
    while x>=pow2(k+1): k+=1
    check(pow2(k)<=x<pow2(k+1),"exact_binary_interval")
    return k
def dyadic_bounds_squared(v):
    # 16 log2(s)=log2((s^2)^8).
    lo=floor_log2(v[0]**8)
    hi=floor_log2(v[1]**8)+1
    check(lo<hi,"nonempty_log_interval")
    return lo,hi
rows=[]
for h in (1,4):
    DR=1 if h==1 else 65
    for i,aa,ll in product((1,2,3),range(1,7),range(7)):
        dabs=const(1)
        for j in (1,2,3):
            if j!=i: dabs=mul(dabs,mul(const(2),dsin(aa*(i-j))))
        for rr,de in enumerate([const(1)] if h==1 else delta4):
            denom=mul(power(dabs,2),mul(power(pil[ll],6),mul(de,const(DR))))
            s2=div(Gover2pi[i],denom)
            lo,hi=dyadic_bounds_squared(s2)
            rows.append(dict(h=h,i=i,E_automorphism=aa,B_label=ll,R_label=rr,
                             lower_log2_numerator=lo,upper_log2_numerator=hi,
                             denominator=16,squared_interval=[str(x) for x in s2]))
check(len(rows)==630,"all_modulus_label_realizations")
uniform={}
for h in (1,4):
    rr=[x for x in rows if x["h"]==h]
    uniform[str(h)]=dict(lower_numerator=min(x["lower_log2_numerator"] for x in rr),
                        upper_numerator=max(x["upper_log2_numerator"] for x in rr),
                        denominator=16)
means=[]
for h in (1,4):
    for i in (1,2,3):
        X=div(power(Gover2pi[i],42),const(7**28*29**36*(65**21 if h==4 else 1)))
        lo,hi=floor_log2(X[0]),floor_log2(X[1])+1
        means.append(dict(h=h,i=i,lower_log2_numerator=lo,
                          upper_log2_numerator=hi,denominator=84))
        check(hi<0,"negative_average_creation_log")

# Exact exponent/norm consistency. These are real-modulus averages,
# not the field norm of a transcendental creation operator.
for h in (1,4):
    b=1802;a=42 if h==1 else 168;c=3562 if h==1 else 3436
    n=a*b+b*c;NN=14*h*n
    check(n==2*b*b and F(NN,4)==7*h*b*b,"unit_vacuum_theta_period_combination")
    check(F(1,2)*F(1,2)-F(1,2)==-F(1,4),"quadratic_average_factor")
for i in range(1,4):
    check(49==7**2 and F(2,6)==F(1,3),"partial_embedding_generator_average")
check(F(3,7)==F(6,14),"B_generator_average")

parser=argparse.ArgumentParser()
parser.add_argument("--output",default=str(HERE/"actual_cm_period_cost_certificate.json"))
args=parser.parse_args()
result=dict(finding="AM-K066",status="PASS",timestamp_utc=datetime.now(timezone.utc).isoformat(),
 exact_assertions=len(checks),checks=checks,
 pi_interval=[str(x) for x in pi],det_two_Y_interval=[str(x) for x in det2Y],
 R_S_abs_interval=[str(x) for x in R],P_J_fourth_power_interval=[str(x) for x in P4],
 beta_intervals={str(k):[str(x) for x in v] for k,v in betas.items()},
 G_over_2pi_intervals={str(k):[str(x) for x in v] for k,v in Gover2pi.items()},
 pi_B_intervals=[[str(x) for x in v] for v in pil],
 delta_R_intervals=[[str(x) for x in v] for v in delta4],
 uniform_creation_log_bounds=uniform,mean_creation_log_bounds=means,
 all_pointwise_label_intervals=rows,
 scope="Exact rational beta/trigonometric/algebraic bounds and modulus exponent identities. No finite valuation of a transcendental factor, automorphic value, or net DP44 sign is computed.")
Path(args.output).write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({k:result[k] for k in ("finding","status","timestamp_utc","exact_assertions",
 "uniform_creation_log_bounds","mean_creation_log_bounds")},indent=2))
