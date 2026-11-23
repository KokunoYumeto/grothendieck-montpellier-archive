#!/usr/bin/env python3
"""Exact diagnostics for AM-DO-058; not an enumeration of S_T."""
from __future__ import annotations
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from itertools import product
from math import comb, gcd
from pathlib import Path
import argparse, hashlib, json

parser=argparse.ArgumentParser()
parser.add_argument('--output',default=str(Path(__file__).with_suffix('.json')))
args=parser.parse_args()
base=Path(__file__).parent
rows=json.loads((base/'definite_oscillator_large_t_certificate.json').read_text())['rows']
checks=0; counts=Counter()
def check(cond,label):
 global checks
 if not cond: raise AssertionError(label)
 checks+=1; counts[label.split(':')[0]]+=1

def gl_order(q,n):
 result=q**(n*(n-1)//2); qi=1
 for _ in range(n):
  qi*=q; result*=qi-1
 return result

def strict_inverse_log2(numerator,denominator):
 # Largest integer k such that numerator/denominator < 2^(-k).
 k=denominator.bit_length()-numerator.bit_length()
 def lt(j):return (numerator<<j)<denominator if j>=0 else numerator<(denominator<<(-j))
 while not lt(k): k-=1
 while lt(k+1): k+=1
 check(lt(k),'binary_bounds:strict')
 check(not lt(k+1),'binary_bounds:next_fails')
 return k

host_results=[]
for row in rows:
 a,f=int(row['a']),int(row['f']); n=a+1
 q0,q1=int(row['g0']),int(row['g1']); T=int(row['T']); Q=q0*q1
 H=2**(13 if row['host']=='J14' else 15)
 o0,o1=gl_order(q0,n),gl_order(q1,n); S=gcd(o0,o1)
 for q in (q0,q1):
  check(q-1>2*f*n,'torsion_reduction:cyclotomic_degree')
 check(o0%S==0 and o1%S==0,'stabilizer:gcd_divides_both')
 check(S.bit_length()==(814 if a==42 else 5022),'stabilizer:exact_bits')
 check(q0!=T and q1!=T,'host_primes:distinct_from_T')
 char_rows=[]
 for e in range(21):
  A=2*(2*H)**(a*f)*T**(a*e//2)
  B=Q**(a*(f-1))
  k=strict_inverse_log2(A,B)
  char_rows.append({'e':e,'strict_inverse_log2':k})
  check(a*e%2==0,'character:integer_exponent')
 # The full e=2 stratum: s=1, one denominator pattern per selected place.
 A=4*f*(T-1)**2*S*(2*H)**(a*f)*(2*H+1)**(2*f*n)*T**(a+2*n)
 B=(T-2)*Q**(a*(f-1))
 k=strict_inverse_log2(A,B)
 check(k==(101768 if a==168 else -128606),'minimal_stratum:exact_margin')
 if a==168:
  check((A<<100000)<B,'minimal_stratum:J56_weak_100000')
 else:
  check(A>B,'minimal_stratum:J14_not_controlled')
 host_results.append({'host':row['host'],'a':a,'f':f,'n':n,'H':H,'g0':q0,'g1':q1,
  'T_bits':T.bit_length(),'gl_order_bits':[o0.bit_length(),o1.bit_length()],
  'stabilizer_gcd':str(S),'stabilizer_gcd_bits':S.bit_length(),
  'stabilizer_gcd_sha256':hashlib.sha256(str(S).encode()).hexdigest(),
  'pointwise_character_bounds':char_rows,
  'minimal_stratum_numerator_bits':A.bit_length(),
  'minimal_stratum_denominator_bits':B.bit_length(),
  'minimal_stratum_strict_inverse_log2':k})

# Exact count of denominator patterns: each nonintegral relative place has
# (d_P,d_barP) in {1,2}^2. Weight e gives binomial(2s,e-2s).
for s in range(1,7):
 hist=Counter(sum(x) for x in product((1,2),repeat=2*s))
 for e in range(0,4*s+2):
  expected=comb(2*s,e-2*s) if 0<=e-2*s<=2*s else 0
  check(hist[e]==expected,'denominator_patterns:binomial')
 check(sum(hist.values())==4**s,'denominator_patterns:total')

# Elementary exact packing simplification with rational t representing
# T^(e/(2f)): 1+2Ht <= (2H+1)t for t>=1.
for H in (1,2,8,8192,32768):
 for t in (Fraction(1),Fraction(3,2),Fraction(2),Fraction(11,3),Fraction(29)):
  check(1+2*H*t<=(2*H+1)*t,'packing:radius_simplification')
for f in range(1,9):
 for n in range(1,9):
  check(Fraction(2*f*n,2*f)==n,'packing:ideal_exponent')

# Actual rational elementary matrices: g=u_d k u_c^-1 maps L_c to L_d.
# Its selected/conjugate pole pair is read from g and g^-1.
def eye(n):return [[Fraction(i==j) for j in range(n)] for i in range(n)]
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B))] for i in range(len(A))]
def inv(A):
 n=len(A); M=[list(A[i])+eye(n)[i] for i in range(n)]
 for j in range(n):
  p=next(i for i in range(j,n) if M[i][j]); M[j],M[p]=M[p],M[j]
  v=M[j][j];M[j]=[x/v for x in M[j]]
  for i in range(n):
   if i!=j:
    v=M[i][j];M[i]=[x-v*y for x,y in zip(M[i],M[j])]
 return [row[n:] for row in M]
def val(x,q):
 if not x:return 1000
 a,b=abs(x.numerator),x.denominator;v=0
 while a%q==0:a//=q;v+=1
 while b%q==0:b//=q;v-=1
 return v
def pole(A,q):return max(0,-min(val(x,q) for row in A for x in row))
local_hist=Counter()
for n,q in product((2,3,4),(3,5,7)):
 E=eye(n); kernels=[E]
 for i in range(n):
  for j in range(n):
   if i==j:continue
   for z in (-2,-1,1,2):
    K=eye(n);K[i][j]=z;kernels.append(K)
 for shift in range(n):
  kernels.append([[Fraction(j==(i+shift)%n) for j in range(n)] for i in range(n)])
 for c,d,K in product(range(q-1),range(q-1),kernels):
  Uc=eye(n);Ud=eye(n);Uc[0][1]=Fraction(c,q);Ud[0][1]=Fraction(d,q)
  G=mul(mul(Ud,K),inv(Uc));Gi=inv(G)
  dc,db=pole(G,q),pole(Gi,q);e=dc+db
  check(dc<=2 and db<=2,'local_support:pole_two')
  check((dc==0)==(db==0),'local_support:paired_integrality')
  check(e==0 or 2<=e<=4,'local_support:minimal_nonzero')
  if e==2:check(dc==db==1,'local_support:minimal_pair')
  check(mul(mul(inv(Ud),G),Uc)==K,'local_support:exact_isometry_torsor')
  local_hist[f'n{n}_q{q}_e{e}']+=1

out={'finding':'AM-DO-058','status':'PASS','timestamp_utc':datetime.now(timezone.utc).isoformat(),
 'exact_assertions':checks,'categories':dict(counts),'hosts':host_results,
 'local_denominator_histogram':dict(local_hist),
 'scope':'Exact host inequalities, finite group-order gcds, denominator-pattern and local rational-matrix diagnostics. No enumeration of S_T or positivity of its higher-denominator remainder; no Lean.'}
Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'timestamp_utc':out['timestamp_utc'],'exact_assertions':checks,
 'hosts':[{'host':h['host'],'gcd_bits':h['stabilizer_gcd_bits'],'minimal_stratum_strict_inverse_log2':h['minimal_stratum_strict_inverse_log2']} for h in host_results]},indent=2))
