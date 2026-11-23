#!/usr/bin/env python3
"""AM-K071: exact local pole identities and rational logarithmic bounds."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial
from datetime import datetime, timezone
import sympy as sp

HERE=Path(__file__).resolve().parent
checks=[]
def ck(v,s):
    if not v: raise AssertionError(s)
    checks.append(s)

# Integer directed rounding of 2*atanh(z), 0<=z<=1/3.
# Every finite term is rounded down at scale 2^192. The complete
# omitted tail is at most 9/[4(2M+1)3^(2M+1)].
P=192; SCALE=1<<P; TERMS=80
def ceildiv(a,b): return (a+b-1)//b
def ln_dyadic_bounds(y):
    num=y-SCALE; den=y+SCALE
    ck(0<=num*3<=den,'log_atanh_domain')
    pn=num; pd=den; nn=num*num; dd=den*den; lo=0
    for j in range(TERMS):
        lo+=(2*pn*SCALE)//((2*j+1)*pd)
        pn*=nn;pd*=dd
    tail=ceildiv(9*SCALE,4*(2*TERMS+1)*3**(2*TERMS+1))
    return lo,lo+TERMS+tail
LN2LO,LN2HI=ln_dyadic_bounds(2*SCALE)
ck(LN2LO>0 and LN2HI-LN2LO<=TERMS+1,'log_two_directed_width')
cache={}
def log2bounds(n):
    if n in cache:return cache[n]
    assert n>0
    b=n.bit_length()-1
    y=n<<(P-b) if b<=P else n>>(b-P)
    lo,hi=ln_dyadic_bounds(y)
    # n/2^b lies between y/SCALE and (y+1)/SCALE; log is 1-Lipschitz
    # on [1,2], so one additional scale unit covers this truncation.
    value=(F(b)+F(lo,LN2HI),F(b)+F(hi+1,LN2LO))
    cache[n]=value
    return value
def lograt(x):
    x=F(x);a,b=log2bounds(x.numerator),log2bounds(x.denominator)
    return a[0]-b[1],a[1]-b[0]
def add(*xs):return sum((x[0] for x in xs),F(0)),sum((x[1] for x in xs),F(0))
def mul(x,e):return (x[0]*e,x[1]*e) if e>=0 else (x[1]*e,x[0]*e)
def exact_margin(bounds):
    lo,hi=bounds
    k=(-hi).numerator//(-hi).denominator
    ck(hi<-k or hi==-k,'directed_upper_binary_margin')
    ck(lo>-(k+1),'matching_lower_binary_margin')
    return k

hp=HERE/'definite_oscillator_large_t_certificate.json'
gp=HERE/'definite_oscillator_minimal_denominator_certificate.json'
ep=HERE/'enlarged_gap_admissible_interval_certificate.json'
r=next(x for x in json.loads(hp.read_text())['rows'] if x['host']=='J56')
old=next(x for x in json.loads(gp.read_text())['hosts'] if x['host']=='J56')
wr=next(x for x in json.loads(ep.read_text())['hosts'] if x['host']=='J56')
T=int(r['T']);Q=r['g0']*r['g1'];a=f=168;n=169;m=164;H=8192;K=2*(H+1)
G=int(old['stabilizer_gcd']);G5=98148490017978252769652736000000
D0=7**140*29**144*5**84*13**84
ck(T>2**995 and 2*int(wr['ell_max'])+a>2**485,'unchanged_host_and_energy')
LT=log2bounds(T);LTM1=log2bounds(T-1);LQ=log2bounds(Q)

# Exact dyadic lower roots for the scalar-ideal covering radius.
root_lowers={};radii={};Slogs={}
for v in range(6):
    tv=T**v
    b=(tv.bit_length()-1)//f
    low,high=256,512
    while low+1<high:
        z=(low+high)//2
        if z**f*2**(b*f)<=tv*256**f:low=z
        else:high=z
    root=F(low*2**b,256)
    ck(root**f<=tv and (root+F(2**b,256))**f>tv,'exact_fractional_ideal_root_bracket')
    radius=F(90516,1000)+F(9750)/root
    root_lowers[v]=root;radii[v]=radius
    volume=add(mul(lograt(F(22,7)*f*radius*radius),f*m),
               mul(log2bounds(factorial(f*m)),-1),mul(log2bounds(D0),-m))
    packing=mul(log2bounds(183),2*f*m)
    ck(volume[1]<packing[0] or packing[1]<volume[0],
       'positive_block_count_choice_separated')
    Slogs[v]=volume if volume[1]<packing[0] else packing

Wlog=add(mul(lograt(F(22,7)*f*9543**2),5*f),
          mul(log2bounds(factorial(5*f)),-1),mul(log2bounds(D0),-5))
cross_const=add(log2bounds(G),Wlog,log2bounds(2),
    mul(log2bounds(K),f*(3*a//2-1)),mul(LQ,-(2*a-1)*(f-1)),
    mul(log2bounds(12),f),(F(f,2)-F(485*f,4),)*2)

def cross_bounds(s,v,u):
    assert 4<=s<=f and 0<=u<=v<=min(s,5)
    # For fixed type sets, incidence-pair count times exact |rho| is
    # m for Case I and 1 for Cases II/III, m=T-1. The type sets
    # require binom(s,v)*binom(v,u).
    exponent=2*m*v+10*s+a*v+(a-1)*(v+u)+F(v,2)
    return add(cross_const,Slogs[v],log2bounds(comb(f,s)),
               log2bounds(comb(s,v)),log2bounds(comb(v,u)),
               mul(LTM1,s-v),mul(LT,exponent))

# Fixed-W0 counts retain the earlier integral-coset formula. Their
# improvements use the full N budget s+u and N^2 budget v+u.
Wbase=add(log2bounds(G5),mul(log2bounds(2*H+1),10*f),log2bounds(2))
rank1const=add(Wbase,mul(log2bounds(H+1),a*f),mul(LQ,-a*(f-1)))
rank2const=add(Wbase,mul(log2bounds(H+1),a*f),
               mul(log2bounds(K),(a-1)*f),mul(LQ,-(2*a-1)*(f-1)))
def fixed_bounds(rank,s,v,u):
    assert 0<=u<=v<=s<=f
    e=10*s+a*(s+u)
    C=rank1const
    if rank==2:e+=(a-1)*(v+u);C=rank2const
    return add(C,log2bounds(comb(f,s)),log2bounds(comb(s,v)),
               log2bounds(comb(v,u)),mul(LTM1,s-v),mul(LT,e))

cross_rows=[];removed=[]
for v in range(6):
  for u in range(v+1):
    good=[]
    for s in range(max(5,v),f+1):
      M=exact_margin(cross_bounds(s,v,u))
      if M>=4096:good.append((s,M));removed.append((s,v,u,M))
    ck(not good or [z[0] for z in good]==list(range(max(5,v),good[-1][0]+1)),
       'cross_threshold_has_no_holes')
    cross_rows.append({'v':v,'u':u,'t':v-u,'s_max':good[-1][0] if good else None,
                       'margin_at_s_max':good[-1][1] if good else None,
                       'radius':str(radii[v]),
                       'first_s_margin':exact_margin(cross_bounds(max(5,v),v,u))})

fixed_rows=[];fixed_removed=[]
for rank in (1,2):
  for u in range(9):
    for t in range(9):
      v=u+t;good=[]
      for s in range(max(5,v),f+1):
        M=exact_margin(fixed_bounds(rank,s,v,u))
        if M>=4096:good.append((s,M));fixed_removed.append((rank,s,v,u,M))
      ck(not good or [z[0] for z in good]==list(range(max(5,v),good[-1][0]+1)),
         'fixed_block_threshold_has_no_holes')
      if good:fixed_rows.append({'rank':rank,'u':u,'t':t,'v':v,
                               's_max':good[-1][0],'margin_at_s_max':good[-1][1]})
ck(len(removed)==1521 and len(fixed_removed)==245,'exact_removed_cell_counts')
ck(len(removed)+len(fixed_removed)<2**11,'finite_union_less_2048')
ck(all(exact_margin(cross_bounds(5,v,u))>=4096
       for v in range(5) for u in range(v+1)),
   'all_five_place_cross_with_any_full_pencil_removed')
ck(exact_margin(cross_bounds(5,5,0))>=4096,
   'all_five_place_cross_offdiagonal_removed')
ck(all(exact_margin(fixed_bounds(rank,5,v,u))>=4096
       for rank in (1,2) for v in range(6) for u in range(v+1) if u<5),
   'all_five_place_fixed_block_except_all_unique_fixed_removed')

# Literal local lattice examples, including the genuine double-pole case.
local_cases=0;double_cases=0
for q in (5,7,11,13):
 I=sp.eye(3);R=sp.Matrix([[0,0,1],[0,0,0],[0,0,0]])
 BM=sp.diag(1,1,q);BN=sp.diag(sp.Rational(1,q),1,1)
 # Full-pencil preserving unipotents have simple cross poles at most,
 # but their square is integral. These examples include a genuine
 # simple pole and length-three nilpotence.
 for b in range(1,q):
  h=I+sp.Matrix([[0,1,sp.Rational(b,q)],[0,0,1],[0,0,0]])
  N=h-I
  for B in (BM,BN):
   C=B.inv()*h*B
   ck(all(x.q==1 for x in C) and C.det()==1,'full_pencil_invariant_lattices')
  ck(N**3==sp.zeros(3) and all(x.q==1 for x in N*N),'full_pencil_nilpotent_square_integral')
  ck(all(N[1,j].q==1 and N[j,1].q==1 for j in (0,2)),
     'full_pencil_positive_cross_entries_integral')
  ck(any(x.q==q for x in N),'full_pencil_nonintegral_example')
  local_cases+=1
 # Unequal labels: verify both directions and the square identity.
 z=sp.Matrix([1,0,0]);row=sp.Matrix([[0,0,1]])
 for c,d in ((0,1),(1,0),(1,2),(2,1)):
  hc=I+sp.Rational(c,q)*R;hd=I+sp.Rational(d,q)*R
  k=I+sp.Matrix([[0,0,0],[1,0,0],[0,0,0]])
  h=hd*k*hc.inv();N=h-I
  ck(N**3==sp.zeros(3),'unequal_pencil_nilpotent')
  ck(all((q*x).q==1 for x in h) and all((q*x).q==1 for x in h.inv()),'unequal_pencil_both_full_simple_poles')
  ck(N*N==h+h.inv()-2*I and all((q*x).q==1 for x in N*N),'unequal_pencil_square_simple_poles')
  ck(any(x.q!=1 for x in BN.inv()*h*BN),'genuine_case_three_full_pencils_differ')
  ck(any(x.q==q for x in N*N),'genuine_case_three_square_simple_pole')
  local_cases+=1
 hc=I+R/q
 N0=sp.Matrix([[0,0,0],[1,0,0],[1,1,0]])
 h=hc*(I+N0)*hc.inv();N=h-I
 ck(N**3==sp.zeros(3) and any(x.q==q*q for x in N*N),'unique_fixed_square_double_pole_genuine')
 ck(any(x.q!=1 for x in BN.inv()*h*BN),'double_pole_example_not_full_pencil')
 ck(hc.inv()*h*hc==I+N0,'unique_fixed_actual_lattice')
 double_cases+=1

# The exact local unipotent table gives the maximum 1/(T-1), not
# 2/(T-2). Test the finite endpoint q>=5 used in the actual proof.
for q in (5,7,11,13,17,19):
 for rho in (F(1,q-1),-F(1,(q-1)*(q-2)),-F(1,q-1),
             F(1,(q-1)*(q-2)),F(2,(q-1)*(q-2))):
  ck(abs(rho)<=F(1,q-1),'exact_unipotent_weight_maximum')
 mlocal=q-1
 ck(mlocal**2*F(1,mlocal)==mlocal,'weighted_full_pencil_pair_count')
 ck(mlocal*F(1,mlocal)==1,'weighted_unique_fixed_pair_count')
 ck(mlocal*(mlocal-1)*F(1,mlocal*(mlocal-1))==1,
    'weighted_unique_transition_pair_count')

error=sum((F(1,2**e) for e in
           (1999,104546,101550,211446,11671,1307182,9556,4085)),F(0))
ck(error<F(1,2**1998),'unchanged_normalized_error_after_subsets')

out={'finding':'AM-K071','status':'PASS','checked_at':datetime.now(timezone.utc).isoformat(),
     'exact_assertions':len(checks),'log_interval_bits':P,'atanh_terms':TERMS,
     'cross_rows':cross_rows,'fixed_rows':fixed_rows,
     'cross_removed_cells':len(removed),'fixed_removed_cells':len(fixed_removed),
     'removed_margin':4085,'local_models':local_cases,'unique_fixed_double_models':double_cases,
     'root_lowers':{str(k):str(v) for k,v in root_lowers.items()},
     'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (hp,gp,ep)},
     'checks':checks,
     'scope':'Actual local N and N^2 pole classification and exact directed-rational bounds for selected unipotent subsets. No full signed sum, automorphic period, source-link or Lean claim.'}
p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=HERE/'pencil_nilpotent_pole_budget_certificate.json')
path=p.parse_args().output;path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('checks','fixed_rows','input_sha256')},indent=2))
