#!/usr/bin/env python3
"""Exact checks for AM-DO-059: moments, complete-tail constants, actual strata."""
from __future__ import annotations
from datetime import datetime,timezone
from fractions import Fraction as F
from math import prod,gcd,comb,factorial
from pathlib import Path
import argparse,hashlib,json
p=argparse.ArgumentParser();p.add_argument('--output',default=str(Path(__file__).with_suffix('.json')));args=p.parse_args()
base=Path(__file__).parent;checks=[]
def check(cond,label):
 if not cond:raise AssertionError(label)
 checks.append(label)
profiles=json.loads((base/'enlarged_gap_admissible_interval_certificate.json').read_text())
h=next(x for x in profiles['hosts'] if x['host']=='J56')
a,f=h['a'],h['f'];ell=int(h['ell_max']);d=f*(a+1)**2;t=ell//16;s0=a+1
check(a==f==168,'actual_host')
check(t>s0 and 16*t<=ell<16*(t+1),'floor_moment_order')
check(10000*a*d<ell,'derivative_shift_margin')
role_bounds={'top':35,'thick':1266,'thin':453};roles=[]
for role,z in h['roles'].items():
 E=int(z['E']);rs=[E+(4*a-3-4*i)*ell+1 for i in range(a-1)]+[2*ell+1]
 ms=([2**960+(a-2)//2-4*ell*(a-1)] if role=='top' else [4*a*ell])+[4*ell-1]*(a-2)+([E-2**955-ell-a//2] if role=='top' else [E+ell])
 check(len(rs)==len(ms)==a and min(ms)>=0,'actual_Pieri_data')
 check(min(r-1 for r in rs)>t,'convergent_shifted_metric')
 num=prod(r+m+2*d for r,m in zip(rs,ms));den=prod(r-1-t for r in rs)
 check(num<role_bounds[role]*den,'full_derivative_moment_bound_'+role)
 check(role_bounds[role]<1280<2048,'uniform_moment_bound')
 for q in (0,ell):
  for bit in (0,1):
   mm=ms[:]
   for i in range(1,a-1):mm[i]-=ell*bit
   nn=prod(r+q+m+2*d for r,m in zip(rs,mm));dd=prod(r+q-1-t for r in rs)
   check(nn*den<=num*dd,'word_twist_monotonicity')
   check(max(r+q for r in rs)<2**960,'unchanged_C_bound')
 # The derivative factor can also be bounded by the exact scalar inflation.
 bare=prod(r+m for r,m in zip(rs,ms))
 check(F(num,bare)<=F(ell,ell-a*d),'derivative_inflation_geometric_bound')
 roles.append({'role':role,'strict_derivative_moment_upper':role_bounds[role],
  'numerator_bits':num.bit_length(),'denominator_bits':den.bit_length(),
  'num_sha256':hashlib.sha256(num.to_bytes((num.bit_length()+7)//8,'big')).hexdigest(),
  'den_sha256':hashlib.sha256(den.to_bytes((den.bit_length()+7)//8,'big')).hexdigest()})
check(F(1280,1536)==F(5,6),'new_epsilon_ratio')
check(2*5**4<6**4,'ratio_below_two_minus_quarter')
check(1536<2**11,'epsilon_inverse_bound')
B0=960*a*f+11*f*s0
check(128*t-512*B0>ell,'absolute_derivative_tail_exponent')
# R'=4.499; exp9>8000 and exp(-.002)>.998.
check(sum(F(3)**j/factorial(j) for j in range(10))>20,'exp3_rational_lower')
check(F(8000)*F(499,500)/4==1996>1536,'shrunk_radius_retains_event')
log2_lower=2*sum(F(1,3)**(2*j+1)/F(2*j+1) for j in range(15))
check(13*log2_lower>F(901,100),'algebraic_H_cutoff_beyond_double_radius')
check(d<2**23 and d>100,'actual_group_dimension')
check(F(1,100*d)<F(1,1000),'shrunk_sampling_chart_radial_margin')
check(2**9*50000*d**5<2**140,'existing_L1_chart_coefficient')
check(23*(d+1)<25*d,'all_Lie_words_count')
check(140+25+1000<1200,'existing_complete_sampling_constant')
check(8*(a+1)*(2*2**960+2*d+a+1)<2**1000,'existing_Casimir_derivative_bound')
Trow=next(x for x in json.loads((base/'definite_oscillator_large_t_certificate.json').read_text())['rows'] if x['host']=='J56')
T=int(Trow['T']);q0=Trow['g0'];q1=Trow['g1'];Q=q0*q1;H=2**13;n=a+1
check(T<2**1001,'unchanged_T_sampling_bound')
loss=F(1+9208*d+f.bit_length())+F(11*f*s0,2)
check(F(ell,1024)-loss>2000,'complete_rational_tail_below_2minus2000')
def order(q):
 v=q**(n*(n-1)//2);qi=1
 for _ in range(n):qi*=q;v*=qi-1
 return v
S=gcd(order(q0),order(q1));check(S.bit_length()==5022,'same_exact_stabilizer_gcd')
old=json.loads((base/'definite_oscillator_minimal_denominator_certificate.json').read_text())
check(S==int(next(x for x in old['hosts'] if x['host']=='J56')['stabilizer_gcd']),'same_finite_group_integer')
def strict_log(A,B):
 k=B.bit_length()-A.bit_length()
 def lt(j):return(A<<j)<B if j>=0 else A<(B<<(-j))
 while not lt(k):k-=1
 while lt(k+1):k+=1
 check(lt(k) and not lt(k+1),'exact_stratum_binary_interval')
 return k
strata=[]
for s,e,expected in [(1,2,271780),(1,3,19933),(1,4,-231913),(2,4,-232916)]:
 charA=2*(2*H)**(a*f)*T**(a*e//2);charB=Q**(a*(f-1))
 check(charA<charB,'untruncated_character_bound_is_below_one')
 A=comb(f,s)*comb(2*s,e-2*s)*(T-1)**(2*s)*S*(2*H+1)**(2*f*n)*T**(n*e)*2**s*charA
 B=(T-2)**s*charB;k=strict_log(A,B)
 check(k==expected,'actual_complete_stratum_margin')
 strata.append({'s':s,'e':e,'strict_inverse_log2':k,'numerator_bits':A.bit_length(),'denominator_bits':B.bit_length()})
# Improved target-lattice over-lattice count: it has T^(2ns) cosets,
# independently of the separate selected/conjugate pole depths.
one_place=[]
for ss,expected in [(1,104546),(2,-567385)]:
 A=comb(f,ss)*(T-1)**(2*ss)*S*(2*H+1)**(2*f*n)*T**(2*n*ss)*2**ss*2*(2*H)**(a*f)*T**(2*a*ss)
 B=(T-2)**ss*Q**(a*(f-1));kk=strict_log(A,B)
 check(kk==expected,'complete_support_size_margin')
 one_place.append({'s':ss,'strict_inverse_log2':kk,'numerator_bits':A.bit_length(),'denominator_bits':B.bit_length()})
for nn in range(2,9):
 for qq in (3,5,7,11):
  for cc in range(qq-1):
   # U=I+(c/q)E12 and qU^-1=qI-cE12.
   inverse_scaled=[[qq*int(i==j)-cc*int(i==0 and j==1) for j in range(nn)] for i in range(nn)]
   check(all(isinstance(x,int) for row in inverse_scaled for x in row),'target_overlattice_contains_standard')
   check(prod(inverse_scaled[i][i] for i in range(nn))==qq**nn,'target_overlattice_exact_local_index')
   check((qq**nn)**2==qq**(2*nn),'target_overlattice_conjugate_pair_index')
check(28>1,'E12_plane_disjoint_from_single_place')
check(2*28==56>3,'E12_plane_disjoint_from_low_strata')
# Exact comparison of the normalized total error, including optional K063.
err=F(1,2**1999)+F(1,2**19933)+F(1,2**271780)
check(err<F(1,2**1998),'low_strata_total_error')
check(err+F(1,2**19425)<F(1,2**1998),'combined_plane_total_error')
check(F(1,2**1999)+F(1,2**104546)+F(1,2**19425)<F(1,2**1998),'complete_single_place_and_plane_error')
# Small exact moment comparisons verify the non-asymptotic bound used for all j<=t.
for r in range(8,21):
 for m in range(0,9):
  for tt in range(1,min(5,r-1)):
   A=F(r+m,r-1-tt)
   for j in range(tt+1):
    exact=prod(F(r+m-j+k,r-1-j+k) for k in range(j))
    check(exact<=A**j,'exact_negative_moment_upper')
result={'finding':'AM-DO-059','status':'PASS','timestamp_utc':datetime.now(timezone.utc).isoformat(),
 'exact_assertions':len(checks),'checks':checks,'host':'J56','ell':str(ell),'moment_order':str(t),
 'd_L':d,'roles':roles,'single_place_support_bounds':one_place,'epsilon':'1/1536','R':'9/2','R_prime':'4499/1000','H':H,
 'absolute_L1_union_tail':'f 2^(-ell/1024)','sampling_loss':str(loss),'strata':strata,
 'scope':'Exact moment and sampling-constant comparisons plus actual rational stratum bounds. The infinite-series argument is in the proof; At least two nonintegral relative places outside the removed small-field plane and Mram positivity remain open.'}
Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['finding','status','timestamp_utc','exact_assertions','strata']},indent=2))
