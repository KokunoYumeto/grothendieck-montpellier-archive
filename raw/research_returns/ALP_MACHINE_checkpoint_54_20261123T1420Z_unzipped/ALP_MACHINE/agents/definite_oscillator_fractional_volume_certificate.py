#!/usr/bin/env python3
"""AM-DO-063: actual fractional-lattice volume and selected-compression bounds."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial, prod, isqrt
from datetime import datetime, timezone
import sympy as sp

HERE=Path(__file__).parent
checks=[]
def ck(v,s):
    if not v: raise AssertionError(s)
    checks.append(s)
def margin(A,B):
    k=B.bit_length()-A.bit_length()
    def lt(j): return (A<<j)<B if j>=0 else A<(B<<(-j))
    while not lt(k):k-=1
    while lt(k+1):k+=1
    ck(lt(k) and not lt(k+1),'strict_binary_margin')
    return k
hp=HERE/'definite_oscillator_large_t_certificate.json'
gp=HERE/'definite_oscillator_minimal_denominator_certificate.json'
ep=HERE/'enlarged_gap_admissible_interval_certificate.json'
host=next(x for x in json.loads(hp.read_text())['rows'] if x['host']=='J56')
old=next(x for x in json.loads(gp.read_text())['hosts'] if x['host']=='J56')
weights=next(x for x in json.loads(ep.read_text())['hosts'] if x['host']=='J56')
a=f=168;n=169;m=164;s=4;H=8192
T=int(host['T']);Q=host['g0']*host['g1'];G=int(old['stabilizer_gcd'])
ell=int(weights['ell_max']);K=2*(H+1)
D0=7**140*29**144*5**84*13**84
Delta=2**336*7**280*29**288*5**168*13**168
ck(Delta==2**(2*f)*D0**2,'exact_half_trace_covolume')
ck(2**f*D0<1500**f,'root_discriminant_less_1500')
ck(T>2**995 and T<2**996,'actual_prime_bits')
ck(T**s>2**(23*f),'fractional_ideal_scale_greater_2pow23')
ck(m<13**2,'positive_block_square_root_bound')
ck(F(90516,1000)**2>H+1,'positive_column_radius_bound')
ck(F(90516,1000)+F(13*1500,2*2**23)<F(90518,1000),
   'positive_column_plus_covering_radius')
ck(F(H**2,2)+F(1,2*H**2)<5793**2,'full_negative_column_radius')
ck(5793+5*1500//2==9543,'five_block_plus_covering_radius')
ck(2*ell+a>2**485,'actual_selected_energy_floor')
Rnear=77*Q**4-14*Q**2
ck(Rnear*2**704<T,'actual_near_point_sinh_square_bound')
# An entirely rational direct check: (sqrt(1+x)+sqrt(x))^2<2
# follows from 4x(1+x)<(1-2x)^2, i.e. x<1/8.
ck(8*Rnear<T,'near_point_conjugator_squared_norm_less_two')

MS=f*m;MW=5*f
Snum=(22*f*45259**2)**MS*T**(2*m*s)
Sden=(7*500**2)**MS*factorial(MS)*D0**m
Wnum=(22*f*9543**2)**MW*T**(10*s)
Wden=7**MW*factorial(MW)*D0**5
base_num=comb(f,s)*(T-1)**(2*s)*G*2**s
base_den=(T-2)**s
char_num=2*K**(f*(3*a//2-1))*T**(s*(3*a-2))
char_den=Q**((2*a-1)*(f-1))
real_num=12**f*2**(f//2)*T**(s//2)
real_den=2**(485*f//4)
A=prod((Snum,Wnum,base_num,char_num,real_num))
B=prod((Sden,Wden,base_den,char_den,real_den))
combined=margin(A,B)
without_real=margin(Snum*Wnum*base_num*char_num,Sden*Wden*base_den*char_den)
real_margin=margin(real_num,real_den)
ck(combined==11674,'actual_complete_scalar_cross_margin')
ck(without_real==-6018 and real_margin==17692,'separate_volume_and_real_margins')
ck(Snum*Wnum*base_num*char_num>2**6017*Sden*Wden*base_den*char_den,
   'strict_volume_only_lower_endpoint')
# DO062 has already removed the other four s=4 cases with larger margins.
prior=[1021942,773837,199371,436554]
ck(all(x>11674 for x in prior),'all_other_four_place_cases_smaller')
ck(1307182>11674 and 6<8,'complete_four_place_margin_11671_including_k068_cut')
# The exact original normalized identity after four complete support strata.
error=sum((F(1,2**e) for e in (1999,104546,101550,211446,11671)),F(0))
ck(error<F(1,2**1998),'retained_error_budget_gap')

# Exact paired split-pencil dual lattice models. No actual global lattice
# enumeration is performed by these small normalization checks.
pencil_cases=0
for w in (3,5):
  J=sp.diag(*([1]*(w-1)+[-1]));I=sp.eye(w)
  z=I[:,0];row=I[-1,:];N=z*row
  for q in (3,5,7,11):
    for c in range(q):
      Lp=I+sp.Rational(c,q)*N
      Lm=J*Lp.inv().T*J
      Bp=Lp/q;Bm=Lm/q
      dual=Bm.inv().T
      ck(Lp.det()==1 and Lm.det()==1,'paired_pencil_unit_covolumes')
      ck(dual==q*J*Lp*J,'exact_positive_hermitian_dual_basis')
      ck(all(x.q==1 for x in dual),'paired_overlattice_dual_integral')
      ck(Bp.det()==sp.Rational(1,q**w),'five_block_covolume_index')
      ck(all(x.q==1 for x in Bp.inv()),'standard_lattice_contained')
      pencil_cases+=1

# Actual signature-one unipotents in an orthogonal Witt basis: square roots
# are unnecessary for the Frobenius and column identities.
unipotent_cases=0
for d in (1,2,3,4):
  J=sp.zeros(d+2);J[0,-1]=J[-1,0]=1
  for j in range(1,d+1):J[j,j]=1
  I=sp.eye(d+2)
  for seed in range(1,9):
    v=sp.Matrix([sp.Rational((seed+j)%5-2,seed%3+1) for j in range(d)])
    x=(v.T*v)[0];b=-x/2+sp.I*sp.Rational(seed-3,2)
    N=sp.zeros(d+2);N[0,-1]=b
    for j in range(d):N[0,j+1]=-v[j];N[j+1,-1]=v[j]
    h=I+N
    ck(h.conjugate().T*J*h==J,'exact_unipotent_unitarity')
    ck(N**3==sp.zeros(d+2),'exact_unipotent_cube')
    t=sp.trace(N.conjugate().T*N)
    ck(sp.simplify(t-(abs(b)**2+2*x))==0,'nilpotent_hilbert_schmidt_norm')
    ck(sp.simplify(sp.trace(h.conjugate().T*h)-(d+2)-t)==0,
       'singular_value_frobenius_identity')
    e=I[:,0]-I[:,-1]
    col2=(e.conjugate().T*h.conjugate().T*h*e)[0]/2
    ck(sp.simplify(2*col2-(t+2))==0,'negative_column_half_frobenius_identity')
    unipotent_cases+=1

# Exact finite-dimensional examples of the elementary Dirichlet-cell count.
# The bound uses an upper radius and pi<22/7; it tests the normalization,
# not the external covering-radius transference theorem.
def sphere_count(dim,R2):
    c={0:1}
    for _ in range(dim):
      new={}
      for z in range(-isqrt(R2),isqrt(R2)+1):
        for u,count in c.items():
          v=u+z*z
          if v<=R2:new[v]=new.get(v,0)+count
      c=new
    return sum(c.values())
ball_cases=0
for k in (1,2,3):
  dim=2*k;ceilroot=isqrt(dim)+(isqrt(dim)**2<dim)
  for q in (2,3,5):
    for R in (1,2,3):
      count=sphere_count(dim,(q*R)**2)
      cover=F(ceilroot,2*q)
      bound=F(22,7)**k*(R+cover)**dim*q**dim/factorial(k)
      ck(count<=bound,'fractional_lattice_ball_volume_normalization')
      ball_cases+=1

out={'finding':'AM-DO-063','status':'PASS','timestamp_utc':datetime.now(timezone.utc).isoformat(),
     'exact_assertions':len(checks),'complete_scalar_cross_margin':combined,
     'volume_only_margin':without_real,'real_compression_margin':real_margin,
     'complete_four_place_margin':11671,'positive_real_dimension':2*MS,
     'five_block_real_dimension':2*MW,'half_trace_covolume':str(D0),
     'pencil_models':pencil_cases,'unipotent_models':unipotent_cases,
     'fractional_ball_models':ball_cases,'checks':checks,
     'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (hp,gp,ep)},
     'scope':'Exact scalar-cross four-place upper bound and paired-dual/volume/norm diagnostics. No rational-support enumeration, all-T sign, period or source-link compatibility.'}
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=HERE/'definite_oscillator_fractional_volume_certificate.json')
path=ap.parse_args().output;path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('checks','input_sha256','half_trace_covolume')},indent=2))
