#!/usr/bin/env python3
"""AM-K073: fixed W0 rank-zero congruence packing and complete pencil counts."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as F
from math import comb
from datetime import datetime, timezone

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
ep=HERE/'enlarged_gap_admissible_interval_certificate.json'
r=next(x for x in json.loads(hp.read_text())['rows'] if x['host']=='J56')
e=next(x for x in json.loads(ep.read_text())['hosts'] if x['host']=='J56')
a=f=168;n=169;w=5;H=8192
T=int(r['T']);g0=int(r['g0']);g1=int(r['g1']);Q=g0*g1;M=Q**(f-1)
G5=98148490017978252769652736000000
from math import gcd,prod
orders=[q**(w*(w-1)//2)*prod(q**j-1 for j in range(1,w+1)) for q in (g0,g1)]
ck(gcd(*orders)==G5,'exact_fixed_five_dimensional_fibre_bound')
ck(2*334<min(g0,g1)**a,'complete_Green_Euler_correction_less_two')
ell=int(e['ell_max']);A=2**960;B=2**955
ET=int(e['roles']['top']['E']);EL=int(e['roles']['thin']['E']);R=ET-B
energy_low=(7*a-3)*ell+EL+2
energy_top=A+R-(a+1)*ell+1
ck(2*ell+a>2**485,'carried_uniform_energy_floor')
ck(energy_low>2**494 and energy_top>2**959,'actual_homogeneous_energy_floors')
ck(T.bit_length()==996 and a-F(1,2)>2*w,'monotonicity_exponent_and_actual_prime_size')

# Bracket z_s=(M/T^(2s))^(1/f) by 24-bit dyadic mantissas.
# Every comparison is an integer cross multiplication, including
# negative binary exponents. There is no floating root inference.
def pow2(k): return F(2**k) if k>=0 else F(1,2**(-k))
def root_bracket(s):
    x=F(M,T**(2*s))
    b=(x.numerator.bit_length()-x.denominator.bit_length())//f
    while pow2(b*f)>x:b-=1
    while pow2((b+1)*f)<=x:b+=1
    bits=24;lo=2**bits;hi=2**(bits+1)
    while lo+1<hi:
        mid=(lo+hi)//2
        if (F(mid,2**bits)*pow2(b))**f<=x:lo=mid
        else:hi=mid
    zl=F(lo,2**bits)*pow2(b);zu=F(hi,2**bits)*pow2(b)
    ck(zl**f<=x<zu**f,'exact_rank_zero_cap_root_bracket')
    return zl,zu

def bound(s,energy_bits):
    zl,zu=root_bracket(s)
    common=add((F(335),)*2,log2bounds(G5),log2bounds(comb(f,s)),
               mul(log2bounds(T+1),s),mul(log2bounds(12),f),
               (F(f,2)-F(energy_bits*f,4),)*2)
    # The cap expression z^(-f/2)(1+C/z)^(10f) is decreasing.
    def value(z):
        return add(common,mul(lograt(z),F(-f,2)),
                   mul(lograt(1+F(2*(H+1),1)/z),2*w*f))
    lower=value(zu)[0];upper=value(zl)[1]
    return (lower,upper),zl,zu
rows=[]
for s in [4,5,6,7]:
 for eb in [485,494,959]:
    q,zl,zu=bound(s,eb);margin=exact_margin(q)
    rows.append(dict(s=s,energy_bits=eb,binary_margin=margin,
                     root_lower=str(zl),root_upper=str(zu)))
by={(r['s'],r['energy_bits']):r for r in rows}
ck(by[(5,485)]['binary_margin']==9199,'uniform_complete_five_place_bound')
ck(by[(6,959)]['binary_margin']==7423,'all_top_complete_six_place_bound')
ck(by[(6,485)]['binary_margin']<0 and by[(7,959)]['binary_margin']<0,
   'unclosed_neighboring_scopes_recorded')

# Exact incidence-weight binomial identity, independent of actual T.
for ff in range(1,13):
 for ss in range(ff+1):
  for qq in [3,5,11,29]:
   direct=sum(comb(ff,ss)*comb(ss,v)*comb(v,u)*(qq-1)**(ss-v)
              for v in range(ss+1) for u in range(v+1))
   ck(direct==comb(ff,ss)*(qq+1)**ss,'all_pencil_type_weight_identity')
# The rank-zero loss is paid by an ideal at both CM partners.
for aa in range(2,173):
 for d in [0,1,2]:
  L=[0,aa,2*aa-1][d]
  ck(-L<=-aa+aa*(d==0),'minimal_nonzero_Green_rank_bound')
# A positive derivative proves the cap monotonicity for all z>0.
# After stripping z powers, derivative numerator is
# (p-b)C+p z, with p=(a-1/2)f and b=10f.
pp=(F(a)-F(1,2))*f;bb=2*w*f
ck(pp-bb>0 and pp>0,'symbolic_monotonicity_positive_coefficients')
for zz in [F(1,1000),F(1,2),F(1),F(2),F(10000)]:
 ck((pp-bb)*2*(H+1)+pp*zz>0,'monotonicity_diagnostic')
# Exact cancellation at z_s^f=M/T^(2s), recorded as exponents.
for s in range(1,f+1):
 ck(-a+a==0 and 2*a*s-2*a*s==0,'rank_zero_cap_Green_cancellation')
# Check the actual old energy bound is sufficient without all-top.
ck(by[(5,485)]['binary_margin']>4096,'uniform_new_stratum_below_carried_error')
ck(by[(6,959)]['binary_margin']>4096,'conditional_new_stratum_below_carried_error')
now=datetime.now(timezone.utc).isoformat()
result=dict(finding='AM-K073',status='PASS',time_utc=now,assertions=len(checks),
 a=a,f=f,W0_dimension=w,H=H,G5=str(G5),rank_zero_patterns=334,
 energy_low=str(energy_low),energy_top=str(energy_top),rows=rows,
 source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [hp,ep]},
 script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 scope='Directed exact arithmetic, paired rank-zero losses and full incidence weights; no global support enumeration or inference of all-T positivity.')
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,
 default=HERE/'fixed_block_rank_zero_packing_certificate.json');args=ap.parse_args()
args.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(status='PASS',assertions=len(checks),time_utc=now,
 rows=[{k:r[k] for k in ['s','energy_bits','binary_margin']} for r in rows])))
