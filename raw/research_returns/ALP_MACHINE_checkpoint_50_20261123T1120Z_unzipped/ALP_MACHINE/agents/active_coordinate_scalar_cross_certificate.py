#!/usr/bin/env python3
"""AM-K072: active-coordinate column and actual homogeneous-energy bounds."""
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
o=next(x for x in json.loads(gp.read_text())['hosts'] if x['host']=='J56')
e=next(x for x in json.loads(ep.read_text())['hosts'] if x['host']=='J56')
a=f=168;m=164;n=169;s=v=5;H=8192
T=int(r['T']);Q=r['g0']*r['g1'];G=int(o['stabilizer_gcd'])
D0=7**140*29**144*5**84*13**84
ell=int(e['ell_max']);A=2**960;B=2**955
ET=int(e['roles']['top']['E']);EH=int(e['roles']['thick']['E']);EL=int(e['roles']['thin']['E']);R=ET-B
energy_low=(7*a-3)*ell+EL+2
energy_top=A+R-(a+1)*ell+1
ck(energy_top>energy_low>2**494 and energy_top>2**959,'actual_role_energy_floors')
root=828375040
ck(root**f<=T**5,'actual_fifth_support_root_lower')
radius=F(90516,1000)+F(9750,root)
ck(F(90516,1000)**2>H+1,'actual_S_radius_upper')
LQ=log2bounds(Q);LT=log2bounds(T);LD=log2bounds(D0)
W=add(mul(lograt(F(22,7)*f*9543**2),5*f),
      mul(log2bounds(factorial(5*f)),-1),mul(LD,-5))
S={d:add(mul(lograt(F(22,7)*f*radius**2),f*d),
         mul(log2bounds(factorial(f*d)),-1),mul(LD,-d)) for d in range(1,m+1)}
base=add(log2bounds(G),W,log2bounds(2),mul(LQ,-(2*a-1)*(f-1)),
         mul(log2bounds(12),f),(F(f,2),)*2,log2bounds(comb(f,5)))
def bound(d,u,top_count=0):
    assert 1<=d<=m and 1<=u<=5 and 0<=top_count<=f
    powers=2*d*v+10*s+a*v+(a-1)*(v+u)+F(v,2)
    energy=add(mul(log2bounds(energy_top),top_count),
               mul(log2bounds(energy_low),f-top_count))
    return add(base,S[d],log2bounds(comb(m,d)),log2bounds(comb(5,u)),
               mul(LT,powers),mul(lograt(F(H+1,d)),F(a*f,2)),
               mul(log2bounds(H+1),(a-1)*f),mul(energy,F(-1,4)))
rows=[];removed=[]
for u in range(1,6):
    good=[]
    for d in range(1,m+1):
        margin=exact_margin(bound(d,u))
        if margin>=4096:good.append((d,margin));removed.append((u,d,margin))
    ck([d for d,_ in good]==list(range(1,good[-1][0]+1)),'active_support_threshold_no_holes')
    rows.append({'u':u,'t':5-u,'d_max':good[-1][0],
                 'margin_at_d_max':good[-1][1],
                 'next_margin':exact_margin(bound(good[-1][0]+1,u)),
                 'minimum_removed_margin':min(z[1] for z in good)})
ck([x['d_max'] for x in rows]==[162,144,127,109,92],'exact_active_support_thresholds')
ck(len(removed)==634 and len(removed)<2**10,'uniform_removed_cells')
top_margins=[(d,exact_margin(bound(d,1,119))) for d in range(1,m+1)]
ck(min(z[1] for z in top_margins)>=4096,'119_top_labels_remove_all_u1')
ck(exact_margin(bound(m,1,118))<4096,'118_not_enough_for_this_fixed_4096_bound')
ck(len(removed)+2==636 and len(removed)+2<2**10,'conditional_removed_union')

# Verify the degree formulas on every interior word count, both
# allowed twist endpoints, and each role; the symbolic dependence
# is affine in the word count and nonnegative twist.
qmax=(a+1)*28*(ell//((a+1)*28))
for role,E in [('top',ET),('thick',EH),('thin',EL)]:
 for w in range(a-1):
  for q in [0,qmax]:
   mids=(a-2)*(4*ell-1)-ell*w
   m0=A+(a-2)//2-4*ell*(a-1) if role=='top' else 4*a*ell
   ma=E-B-ell-a//2 if role=='top' else E+ell
   N=m0+mids+ma
   kappa=2*ell+q+a
   Eexact=A+R-(w+3)*ell+q+1 if role=='top' else (8*a-5-w)*ell+E+q+2
   ck(N+kappa==Eexact,'actual_PB3_PB12_PB13_energy_identity')
   ck(N>=0 and m0>=0 and ma>=0,'actual_selected_nonnegative_degrees')
   ck(Eexact>=(energy_top if role=='top' else energy_low),'all_words_twists_energy_lower')

# Rational Heisenberg models in U(d+1,1) verify the actual last-column
# and square-diagonal normalizations. The unused W0 coordinates may
# be added as identity coordinates.
model_count=0
for d in range(1,7):
 for theta in [0,2,6]:
  z=sp.Matrix([j+1 for j in range(d)])
  z2=int((z.T*z)[0]);size=d+2
  N=sp.zeros(size);b=-z2+sp.I*theta
  for i in range(d):
   N[i,d]=z[i];N[i,d+1]=-z[i]
   N[d,i]=-z[i];N[d+1,i]=-z[i]
  N[d,d]=b/2;N[d,d+1]=-b/2;N[d+1,d]=b/2;N[d+1,d+1]=-b/2
  J=sp.diag(*([1]*(size-1)+[-1]));h=sp.eye(size)+N
  N2=(N*N).applyfunc(sp.simplify)
  ck((h.conjugate().T*J*h-J).applyfunc(sp.simplify)==sp.zeros(size),'unipotent_unitary_model')
  ck(N**3==sp.zeros(size) and N.rank()==2,'rank_two_nilpotence')
  ck(N[:d,:d]==sp.zeros(d),'scalar_positive_compression')
  ck(N2[-1,-1]==z2 and sum(abs(N[i,-1])**2 for i in range(d))==z2,
     'actual_square_diagonal_and_cross_norm')
  ck(N2[-1,-1]==2*sp.re(h[-1,-1])-2,'negative_diagonal_identity')
  model_count+=1

# Exact nonproportional integer instances of generalized Holder.
# Raising f0-th powers removes all radicals; these checks diagnose
# the sharp d factor without substituting for the symbolic proof.
for f0 in range(1,7):
 for d in range(1,8):
  z=[[1+(i+2)*(j+3)+(i*j)%5 for j in range(f0)] for i in range(d)]
  prods=[__import__('math').prod(row) for row in z]
  right=__import__('math').prod(sum(z[i][j]**f0 for i in range(d)) for j in range(f0))
  ck(sum(prods)**f0<=right,'generalized_Holder_integer_diagnostic')
  ck(d**f0*min(prods)**f0<=right,'selected_product_witness_d_factor')

ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,
 default=HERE/'active_coordinate_scalar_cross_certificate.json');args=ap.parse_args()
margin118=exact_margin(bound(m,1,118))
ck(8*2**1999<2**4085,'carried_error_plus_new_union_below_1998')
now=datetime.now(timezone.utc).isoformat()
result={'finding':'AM-K072','status':'PASS','time_utc':now,'assertions':len(checks),
 'host':'J56','support_size':5,'unequal_pencils':5,'a':a,'f':f,'m':m,
 'energy_low':str(energy_low),'energy_top':str(energy_top),
 'uniform_thresholds':rows,'uniform_removed_cells':len(removed),
 'top_count_sufficient':119,'minimum_119_top_margin':min(z[1] for z in top_margins),
 'worst_119_top_d':min(top_margins,key=lambda z:z[1])[0],
 'd164_118_top_margin':margin118,
 'uniform_union_bits':4086,'conditional_union_cells':636,
 'local_models':model_count,
 'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [hp,gp,ep]},
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Exact local normalization and rational upper-bound checks; no global support enumeration, all-T positivity, or literal source admissibility.'}
args.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','assertions':len(checks),'time_utc':now,'rows':rows,
 'minimum_119_top_margin':result['minimum_119_top_margin'],
 'd164_118_top_margin':result['d164_118_top_margin']}))
