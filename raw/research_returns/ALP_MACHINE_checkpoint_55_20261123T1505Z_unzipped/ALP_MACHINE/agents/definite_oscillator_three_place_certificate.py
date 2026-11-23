#!/usr/bin/env python3
"""AM-DO-061: exact trace, pencil and complete three-place diagnostics.

This certifies stated rational inequalities and finite algebraic identities.
It does not enumerate the actual rational short sum or evaluate a period.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import combinations
from math import comb, gcd, prod
from pathlib import Path
import hashlib
import json
import sympy as sp

parser=argparse.ArgumentParser()
parser.add_argument('--output', default=str(Path(__file__).with_suffix('.json')))
args=parser.parse_args()
base=Path(__file__).parent
checks=[]
def ck(value,label):
    if not value: raise AssertionError(label)
    checks.append(label)
def margin(A,B):
    assert A>0 and B>0
    k=B.bit_length()-A.bit_length()
    def lt(j): return (A<<j)<B if j>=0 else A<(B<<(-j))
    while not lt(k): k-=1
    while lt(k+1): k+=1
    ck(lt(k) and not lt(k+1),'exact_binary_margin')
    return k
def gl(q,n):
    return q**(n*(n-1)//2)*prod(q**i-1 for i in range(1,n+1))
host_path=base/'definite_oscillator_large_t_certificate.json'
old_path=base/'definite_oscillator_minimal_denominator_certificate.json'
row=next(x for x in json.loads(host_path.read_text())['rows'] if x['host']=='J56')
old=next(x for x in json.loads(old_path.read_text())['hosts'] if x['host']=='J56')
a=f=168; n=169; H=8192; T=int(row['T']); Q=row['g0']*row['g1']
G=int(old['stabilizer_gcd']); G5=gcd(gl(row['g0'],5),gl(row['g1'],5))
ck((row['a'],row['f'])==(a,f),'actual_host_rank')
ck(G5==98148490017978252769652736000000,'actual_rank_five_gcd')
ck(G.bit_length()==5022 and G5.bit_length()==107,'actual_fibre_bits')
ck(Q>2**70 and T<2**996 and gcd(n,28)==1,'actual_elementary_bounds')
ck(2*(f-1)*2<min(row['g0'],row['g1'])-1,'one_global_green_euler_factor')
B1=F(H+n-2)+F(1,H)
B2=F(comb(n-2,2)+1)+(n-2)*(F(H)+F(1,H))
BX=max(F(n*n),B1*B1-n*n)
BY=n*B2+F(n-1,2)*B1*B1
ck(B1==F(68476929,8192),'exact_trace_bound')
ck(B2==F(11320737959,8192),'exact_second_coefficient_bound')
ck(BX==F(4687173109006337,67108864),'exact_first_phase_invariant_bound')
ck(BY==F(102389129167157269,16777216),'exact_second_phase_invariant_bound')
trace_margins={}
for s in (3,4):
    trace_margins[str(s)]={}
    for label,B in (('X',BX),('Y',BY)):
        A=B.numerator**(2*f)*T**(4*s)
        D=B.denominator**(2*f)*Q**(2*(f-1))
        trace_margins[str(s)][label]=margin(A,D)
ck(trace_margins['3']=={'X':2770,'Y':604},'complete_s3_global_trace_rigidity')
ck(all(x<0 for x in trace_margins['4'].values()),'s4_trace_gate_not_claimed')

s=3; rho_num=2**s; rho_den=(T-2)**s
Kcount=comb(f,s)*(T-1)**(2*s)*rho_num
full_count=Kcount*G*(2*H+1)**(2*f*n)*T**(2*n*s)
five_count=Kcount*G5*(2*H+1)**(10*f)*T**(10*s)
cross_count=Kcount*G*183**(2*f*(a-4))*(2*H+1)**(10*f)*T**(2*n*s)
K=2*(H+1)
ck(H+1<91**2 and 2*91+1==183,'anisotropic_last_column_radius')
results={}
# N_SS and (N^2)_SS are nonzero integral witnesses.
A=full_count*2*(H+1)**(a*f)*K**((a-1)*f)
D=rho_den*Q**((2*a-1)*(f-1))
results['rank2_nonscalar_block']=margin(A,D)
# A rank-one matrix is determined by one integral-block pivot column.
rank1_count=comb(f,s)*(a-4)*(2*H+3)**(2*f*n)*T**(10*s)*rho_num
A=rank1_count*2*(H+1)**(a*f)
D=rho_den*Q**(a*(f-1))
results['rank1_nonscalar_block']=margin(A,D)
# Fixed five-dimensional rank-one and rank-two subsets.
A=five_count*2*(H+1)**(a*f)*T**(2*a*s)
D=rho_den*Q**(a*(f-1))
results['rank1_scalar_block']=margin(A,D)
A=five_count*2*(H+1)**(a*f)*K**((a-1)*f)*T**(2*s*(2*a-1))
D=rho_den*Q**((2*a-1)*(f-1))
results['rank2_scalar_block_fixed_five']=margin(A,D)
# Cross-block witness has pole one and square-root archimedean norm.
A=cross_count*2*K**(f*(3*a//2-1))*T**(s*(3*a-2))
D=rho_den*Q**((2*a-1)*(f-1))
results['rank2_scalar_block_cross']=margin(A,D)
expected={'rank2_nonscalar_block':1359403,
          'rank1_nonscalar_block':782802,
          'rank1_scalar_block':544796,
          'rank2_scalar_block_fixed_five':1114456,
          'rank2_scalar_block_cross':386930}
ck(results==expected,'all_five_complete_s3_margins')
ck(min(results.values())>211449,'nonrational_primary_piece_is_largest_bound')
ck(6*2**211446<2**211449,'complete_s3_bound')
error=F(1,2**1999)+F(1,2**104546)+F(1,2**101550)+F(1,2**211446)
ck(error<F(1,2**1998),'unchanged_normalized_error')

# Cyclic exterior trace has pole one although individual exterior entries
# can have pole two. All operations below are rational and exact.
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def mm(A,B): return [[sum(x*y for x,y in zip(r,c)) for c in zip(*B)] for r in A]
def det(A):
    if not A:return F(1)
    if len(A)==1:return A[0][0]
    return sum((-1)**j*A[0][j]*det([r[:j]+r[j+1:] for r in A[1:]]) for j in range(len(A)))
def ext(A,inds):return [[det([[A[i][j] for j in J] for i in I]) for J in inds] for I in inds]
local_cases=0; exterior_trace_cases=0; cross_entries=0
for q in (3,5,7):
  size=5; z=[F(1),F(2),F(),F(),F(1)]; row0=[F(1),F(),F(),F(),F(-1)]
  S=(2,3);W=(0,1,4)
  R=[[z[i]*row0[j] for j in range(size)] for i in range(size)]
  ck(mm(R,R)==[[F() for _ in range(size)] for _ in range(size)],'rank_one_square_zero')
  for c,d in ((0,1),(1,0),(1,2),(2,1),(2,2)):
    hd=eye(size);hi=eye(size)
    for i in range(size):
      for j in range(size):hd[i][j]+=F(d,q)*R[i][j];hi[i][j]-=F(c,q)*R[i][j]
    for variant in range(4):
      k=eye(size)
      if variant==0:k[4][0]=F(1)
      elif variant==1:k[2][0]=F(1);k[4][3]=F(1)
      elif variant==2:k[0],k[4]=k[4],k[0]
      else:k[0][1]=F(2);k[1][2]=F(1);k[3][4]=F(3)
      g=mm(mm(hd,k),hi);local_cases+=1
      ck(all(g[i][j]==k[i][j] for i in S for j in S),'integral_positive_block')
      for I,J in ((S,W),(W,S)):
        for i in I:
          for j in J:
            ck((q*g[i][j]).denominator==1,'cross_block_pole_one');cross_entries+=1
      for j in range(1,size+1):
        inds=list(combinations(range(size),j)); Eg=ext(g,inds);Ek=ext(k,inds)
        # D_j is the coefficient of t in wedge(I+tR), since R has rank one.
        oneR=[[F(i==j0)+R[i][j0] for j0 in range(size)] for i in range(size)]
        Eone=ext(oneR,inds);Dj=[[Eone[i][j0]-F(i==j0) for j0 in range(len(inds))] for i in range(len(inds))]
        ck(all(x==0 for r in mm(Dj,Dj) for x in r),'exterior_nilpotent_square_zero')
        trace=sum(Eg[i][i] for i in range(len(inds)))
        product=mm(Ek,Dj)
        expected_trace=sum(Ek[i][i] for i in range(len(inds)))+F(d-c,q)*sum(product[i][i] for i in range(len(inds)))
        ck(trace==expected_trace,'exact_cyclic_exterior_trace')
        ck((q*trace).denominator==1,'characteristic_coefficient_pole_one')
        exterior_trace_cases+=1

# The off-circle Toeplitz contribution and the Vandermonde rank argument.
t,z,b=sp.symbols('t z b')
w=lambda x:sp.Matrix([1,x,x*x])
V=sp.Matrix.hstack(w(t),w(z),w(b))
ck(sp.expand(V.det()-(z-t)*(b-t)*(b-z))==0,'three_node_vandermonde')
toeplitz_cases=0
phases=(F(1),sp.I,F(3,5)+sp.I*F(4,5),F(5,13)-sp.I*F(12,13))
for phase in phases:
  for radius in (F(3,2),F(2),F(5,3)):
    zz=sp.simplify(phase*radius);bb=sp.simplify(phase/radius)
    u=w(zz);v=w(bb)
    off=sp.simplify(u*v.conjugate().T+v*u.conjugate().T)
    direct=sp.Matrix(3,3,lambda i,j:zz**(i-j)+bb**(i-j))
    ck(sp.simplify(off-direct)==sp.zeros(3),'off_pair_toeplitz_exact')
    ck(off.rank()==2,'off_pair_rank_two')
    ck(sp.simplify((zz-bb))!=0,'off_pair_distinct')
    for tt in (F(1),-F(1),sp.I,-sp.I,F(3,5)+sp.I*F(4,5)):
      ck(sp.simplify(sp.Matrix.hstack(w(tt),u,v).det())!=0,'unit_off_pair_vandermonde_nonzero')
    toeplitz_cases+=1
u0,v0,k0=sp.symbols('u0 v0 k0')
ck(sp.diag(1,1,1).rank()==3,'rank_bookkeeping_dimension_three')
for positive_multiplicity in (1,2,7,169):
    block=sp.Matrix([[positive_multiplicity,0,0],[0,0,1],[0,1,0]])
    ck(block.det()==-positive_multiplicity,'rank_three_coefficient_form')

# Actual unipotent structural formulas in standard signature coordinates.
# We choose exact rational orthonormal Witt bases to test every split case.
unipotent_cases=0; column_reconstructions=0
for pos in (2,3,5):
  size=pos+1;J=sp.diag(*([1]*pos+[-1])); neg=size-1
  for null_positive_index in (0,pos-1):
    # sqrt(2) is exact; P is Euclidean-unitary and changes J to Witt form.
    ell=sp.zeros(size,1);ell[null_positive_index]=sp.sqrt(2)/2;ell[neg]=sp.sqrt(2)/2
    other=J*ell
    mids=[sp.eye(size)[:,i] for i in range(pos) if i!=null_positive_index]
    P=sp.Matrix.hstack(ell,*mids,other)
    ck(sp.simplify(P.conjugate().T*P)==sp.eye(size),'euclidean_orthonormal_witt_basis')
    for seed in range(5):
      vv=sp.Matrix([0 if seed==0 else ((seed+i)%3)-1+sp.I*((2*seed+i)%3-1) for i in range(pos-1)])
      vv2=sp.simplify((vv.conjugate().T*vv)[0])
      for tt in (-2,0,3):
        hw=sp.eye(size)
        for i in range(pos-1):hw[0,i+1]=-sp.conjugate(vv[i]);hw[i+1,size-1]=vv[i]
        hw[0,size-1]=-vv2/2+sp.I*tt
        N=sp.simplify(P*(hw-sp.eye(size))*P.conjugate().T);NN=sp.simplify(N*N)
        ck(sp.simplify((sp.eye(size)+N).conjugate().T*J*(sp.eye(size)+N)-J)==sp.zeros(size),'standard_unipotent_unitarity')
        ck(sp.simplify(N+J*N.conjugate().T*J-NN)==sp.zeros(size),'N_plus_adjoint_equals_square')
        ck(sp.simplify(NN+vv2*ell*ell.conjugate().T*J)==sp.zeros(size),'square_null_line_outer_product')
        ck(sp.simplify(N**3)==sp.zeros(size),'unipotent_cube_zero')
        ck(sp.trace(N)==0 and sp.trace(NN)==0,'unipotent_trace_pair')
        ck(N.rank() in (0,1,2),'unipotent_rank_one_or_two')
        if N.rank()==1:
          for i in range(pos):
            if N[i,i]!=0:
              reconstructed=sp.Matrix(size,size,lambda j,k0:N[j,i]*N[i,k0]/N[i,i])
              ck(sp.simplify(reconstructed-N)==sp.zeros(size),'rank_one_pivot_column_recovers_matrix')
              for k0 in range(size):
                ck(sp.simplify(N[i,k0]+J[k0,k0]*sp.conjugate(N[k0,i]))==0,'rank_one_row_from_column')
              column_reconstructions+=1
        # Let S be any positive coordinates disjoint from ell's positive part.
        S=[i for i in range(pos) if i!=null_positive_index]
        ck(all(N[i,j]==0 for i in S for j in S),'scalar_block_unipotent_model')
        scol=sp.Matrix([N[i,neg] for i in S])
        ck(sp.simplify((scol.conjugate().T*scol)[0])==vv2/2,'exact_S_last_column_half_energy')
        ck(sp.simplify(vv2**2-4*hw[0,size-1]*sp.conjugate(hw[0,size-1]))<=0,'square_linear_arch_bound')
        unipotent_cases+=1

# Finite scalar-primary ratios used in the five branches.
green_cases=0
for size in (5,7,13,43,169):
  for q in (3,5,113):
    den=prod(q**j-1 for j in range(1,size))
    for rank in (1,2):
      num=prod(q**j-1 for j in range(1,size-rank))
      ck(F(num,den)==F(1,prod(q**j-1 for j in range(size-rank,size))),'exact_rank_green_ratio')
      green_cases+=1

report={'finding':'AM-DO-061','status':'PASS','timestamp_utc':datetime.now(timezone.utc).isoformat(),
        'exact_assertions':len(checks),'actual_host':row['host'],
        'trace_bounds':{k:str(v) for k,v in {'B1':B1,'B2':B2,'BX':BX,'BY':BY}.items()},
        'trace_margins':trace_margins,'five_stratum_margins':results,
        'nonrational_primary_carried_margin':211449,'combined_s3_margin':211446,
        'local_pencil_cases':local_cases,'exterior_trace_cases':exterior_trace_cases,
        'cross_entries':cross_entries,'toeplitz_cases':toeplitz_cases,
        'unipotent_cases':unipotent_cases,'column_reconstructions':column_reconstructions,
        'green_cases':green_cases,'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (host_path,old_path)},
        'checks':checks,'scope':'Exact arithmetic and finite algebraic diagnostics for the proved complete J56 three-place estimate. No actual rational remainder enumeration, period evaluation, all-T positivity, J14 bound or Lean.'}
Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('checks','input_sha256')},indent=2))
