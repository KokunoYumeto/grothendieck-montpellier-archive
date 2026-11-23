#!/usr/bin/env python3
"""AM-DO-062: exact residual trace and higher-support bounds."""
from __future__ import annotations
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from math import comb
from datetime import datetime,timezone
import sympy as sp

p=argparse.ArgumentParser();p.add_argument('--output',default=str(Path(__file__).with_suffix('.json')))
args=p.parse_args();base=Path(__file__).parent;checks=[]
def ck(v,s):
    if not v:raise AssertionError(s)
    checks.append(s)
def margin(A,B):
    k=B.bit_length()-A.bit_length()
    def lt(j):return (A<<j)<B if j>=0 else A<(B<<(-j))
    while not lt(k):k-=1
    while lt(k+1):k+=1
    ck(lt(k) and not lt(k+1),'strict_binary_margin')
    return k
hp=base/'definite_oscillator_large_t_certificate.json'
gp=base/'definite_oscillator_minimal_denominator_certificate.json'
row=next(x for x in json.loads(hp.read_text())['rows'] if x['host']=='J56')
old=next(x for x in json.loads(gp.read_text())['hosts'] if x['host']=='J56')
a=f=168;n=169;H=8192;m=43;T=int(row['T']);Q=row['g0']*row['g1']
G=int(old['stabilizer_gcd']);G5=98148490017978252769652736000000;K=2*(H+1)
ck(n-126==43 and a-4==164,'actual_residual_dimensions')
B1=F(H+2*m-2)+F(1,H)
B2=F(comb(m-2,2)+1)+(m-2)*(F(H)+F(1,H))+(m-1)*(F(H+m-2)+F(1,H))+comb(m,2)
ck(B1==F(67796993,8192),'residual_first_coefficient_bound')
ck(B2==F(5598265427,8192),'residual_second_coefficient_bound')
ck(B2==(2*m-3)*(F(H)+F(1,H))+3446,'residual_second_bound_simplification')
trace=[]
for s in range(4,10):
    vals=[margin(B.numerator**(2*f)*T**(2*s),B.denominator**(2*f)*Q**(2*(f-1))) for B in (B1,B2)]
    trace.append({'s':s,'e1_margin':vals[0],'e2_margin':vals[1]})
ck([(x['e1_margin'],x['e2_margin']) for x in trace]==[(11135,8995),(9144,7004),(7153,5013),(5162,3022),(3171,1032),(1180,-959)],'all_residual_trace_margins')

definitions=[
 ('rank2_nonscalar',G*(2*H+1)**(2*f*n)*2*(H+1)**(a*f)*K**((a-1)*f),Q**((2*a-1)*(f-1)),2*n,True),
 ('rank1_nonscalar',(a-4)*(2*H+3)**(2*f*n)*2*(H+1)**(a*f),Q**(a*(f-1)),10,False),
 ('rank1_scalar',G5*(2*H+1)**(10*f)*2*(H+1)**(a*f),Q**(a*(f-1)),10+2*a,True),
 ('rank2_scalar_five',G5*(2*H+1)**(10*f)*2*(H+1)**(a*f)*K**((a-1)*f),Q**((2*a-1)*(f-1)),10+2*(2*a-1),True),
 ('rank2_scalar_cross',G*183**(2*f*(a-4))*(2*H+1)**(10*f)*2*K**(f*(3*a//2-1)),Q**((2*a-1)*(f-1)),2*n+3*a-2,True)]
expected={4:[1021942,773837,199371,436554,-450244],5:[684481,764872,-146054,-241349,-1287416],6:[347021,755907,-491478,-919250,-2124589],7:[9560,746942,-836902,-1597152,-2961762],8:[-327900,737978,-1182326,-2275054,-3798934]}
rows=[];removed=[]
for s in range(4,9):
    bounds={}
    for label,C,D,e,pencil in definitions:
        A=C*comb(f,s)*2**s*T**(e*s)
        if pencil:A*=(T-1)**(2*s)
        B=D*(T-2)**s
        M=margin(A,B);bounds[label]=M
        if (label=='rank2_nonscalar' and s<=7) or label=='rank1_nonscalar' or (s==4 and label in ('rank1_scalar','rank2_scalar_five')):
            removed.append((s,label,M))
    ck(list(bounds.values())==expected[s],'exact_higher_support_bounds')
    rows.append({'s':s,'strict_binary_margins':bounds})
ck(len(removed)==11 and min(x[2] for x in removed)==9560,'eleven_disjoint_removed_subsets')
ck(11*2**9556<2**9560,'combined_higher_support_bound')
error=F(1,2**1999)+F(1,2**104546)+F(1,2**101550)+F(1,2**211446)+F(1,2**1307182)+F(1,2**9556)
ck(error<F(1,2**1998),'retained_error_budget')

# Exact characteristic-coefficient translation and identity padding.
translation_cases=0
for r in range(2,10):
  for seed in range(4):
    A=sp.Matrix(r,r,lambda i,j:(3*i+2*j+seed)%5-2)
    N=A-sp.eye(r)
    e2=lambda X:(sp.trace(X)**2-sp.trace(X*X))/2
    ck(sp.trace(N)==sp.trace(A)-r,'first_coefficient_translation')
    ck(e2(N)==e2(A)-(r-1)*sp.trace(A)+comb(r,2),'second_coefficient_translation')
    padded=sp.diag(A,sp.eye(11-r));Np=padded-sp.eye(11)
    ck(sp.trace(Np)==sp.trace(N) and e2(Np)==e2(N),'positive_identity_padding')
    translation_cases+=1

# Trace zero of a globally unipotent matrix improves an unequal-pencil
# entry pole, but an equal-pencil example really retains a double pole.
pencil_cases=0
for q in (3,5,7,11):
    z=sp.Matrix([1,0,0]);row0=sp.Matrix([[0,0,1]]);R=z*row0
    I=sp.eye(3)
    for c,d in ((0,1),(1,0),(1,2),(2,1)):
        hd=I+sp.Rational(d,q)*R;hc=I+sp.Rational(c,q)*R
        # Choose an integral upper-unipotent k. The resulting g is still
        # upper unipotent, and unequal labels really introduce pole one.
        for u,v,w in ((q,0,0),(0,q,0),(q,q,q),(0,0,q*q)):
            N=sp.Matrix([[0,u,w],[0,0,v],[0,0,0]])
            k=I+N;g=hd*k*hc.inv()
            qkz=(row0*k*z)[0]
            ck(sp.trace(g)==3 and (g-I)**3==sp.zeros(3),'unequal_pencil_global_unipotent_model')
            ck(sp.trace(g)==sp.trace(k)+sp.Rational(d-c,q)*qkz,'unequal_pencil_trace_identity')
            ck(int(qkz)%q==0,'unequal_pencil_double_pole_coefficient_divisible')
            ck(all((q*x).q==1 for x in g),'unequal_pencil_full_pole_one')
            ck(any(x.q==q for x in g),'unequal_pencil_genuine_simple_pole')
            pencil_cases+=1
    # Equal-pencil conjugation of a length-three nilpotent can have pole2.
    h=I+sp.Rational(1,q)*R
    N=sp.Matrix([[0,0,0],[1,0,0],[1,1,0]])
    g=h*(I+N)*h.inv()
    ck(sp.trace(g)==3 and (g-I)**3==sp.zeros(3),'equal_pencil_unipotent')
    ck(any(x.q==q*q for x in g),'equal_pencil_pole_two_retained')
ck(pencil_cases==64,'nonvacuous_unequal_pencil_cases')

report={'finding':'AM-DO-062','status':'PASS','timestamp_utc':datetime.now(timezone.utc).isoformat(),
        'exact_assertions':len(checks),'residual_dimension':m,'B1':str(B1),'B2':str(B2),
        'trace_margins':trace,'stratum_margins':rows,'removed_subsets':removed,
        'combined_removed_margin':9556,'translation_cases':translation_cases,'pencil_cases':pencil_cases,
        'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (hp,gp)},'checks':checks,
        'scope':'Exact residual trace bounds, eleven disjoint higher-support estimates and local pencil diagnostics. No complete four-place bound, all-T sign, period or Lean.'}
Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('checks','input_sha256')},indent=2))
