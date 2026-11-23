#!/usr/bin/env python3
"""Exact diagnostics for AM-DO-060. Does not enumerate the rational short sum."""
from __future__ import annotations
import argparse, json, hashlib
from datetime import datetime, timezone
from pathlib import Path
from math import comb, gcd, prod
from fractions import Fraction as F
from itertools import combinations
import sympy as sp

p=argparse.ArgumentParser()
p.add_argument('--output', default=str(Path(__file__).with_suffix('.json')))
args=p.parse_args(); base=Path(__file__).parent; checks=[]
def ck(v,s):
    if not v: raise AssertionError(s)
    checks.append(s)
def strict_log(A,B):
    k=B.bit_length()-A.bit_length()
    def lt(j): return (A<<j)<B if j>=0 else A<(B<<(-j))
    while not lt(k): k-=1
    while lt(k+1): k+=1
    ck(lt(k) and not lt(k+1),'exact_binary_margin')
    return k
def gl(q,n): return q**(n*(n-1)//2)*prod(q**i-1 for i in range(1,n+1))
hosts=json.loads((base/'definite_oscillator_large_t_certificate.json').read_text())['rows']
old=json.loads((base/'definite_oscillator_minimal_denominator_certificate.json').read_text())['hosts']
out=[]
for row in hosts:
    a,f=row['a'],row['f']; n=a+1; T=int(row['T']); Q=row['g0']*row['g1']; H=8192
    G=int(next(z for z in old if z['host']==row['host'])['stabilizer_gcd'])
    G5=gcd(gl(row['g0'],5),gl(row['g1'],5))
    ck(a-4>5 and n>6,'positive_block_rank_gap')
    ck(all(q%28==1 and q>28 and q-1>10*f for q in (row['g0'],row['g1'])),'root_and_compact_fibre_injection')
    ck(4*f*2**2<min(row['g0'],row['g1'])**(a-1),'two_green_corrections_below_two')
    margins={'generic':{},'rank1':{},'rank2':{},'coefficient':{}}
    for s in (1,2,3):
        K=comb(f,s)*(T-1)**(2*s)*2**s
        A=K*G*(2*H+1)**(2*f*n)*T**(2*n*s)*2*(2*H)**(a*f)
        B=(T-2)**s*Q**(a*(f-1))
        margins['generic'][str(s)]=strict_log(A,B)
        A=K*G5*(2*H+1)**(10*f)*T**(10*s)*2*(H+1)**(a*f)*T**(2*a*s)
        B=(T-2)**s*Q**(a*(f-1))
        margins['rank1'][str(s)]=strict_log(A,B)
        A=K*G*(2*H+1)**(2*f*n)*T**(2*n*s)*2*(H+1)**(a*f)*(2*(H+1))**((a-1)*f)*T**(2*s*(2*a-1))
        B=(T-2)**s*Q**((2*a-1)*(f-1))
        margins['rank2'][str(s)]=strict_log(A,B)
        margins['coefficient'][str(s)]=[
            strict_log((comb(6,j)*(H+1)**j)**(2*f)*T**(4*s),Q**(2*(f-1))) for j in (1,2,3)]
    if row['host']=='J56':
        ck(margins['generic']['2']==101552,'generic_two_place_bound')
        ck(margins['rank1']['2']==890221,'rank_one_two_place_bound')
        ck(margins['rank2']['2']==362973,'rank_two_two_place_bound')
        ck(margins['coefficient']['2']==[10271,5459,951],'three_coefficient_two_place_margins')
        ck(margins['coefficient']['3'][:2]==[6289,1477],'two_coefficient_three_place_margins')
        ck(margins['generic']['3']<0 and margins['rank2']['3']<0,'higher_remainder_retained')
        ck(3*2**101550<2**101552,'combined_two_place_margin')
        ck(G5==98148490017978252769652736000000,'exact_rank_five_gcd')
    else:
        ck(margins['generic']['2']<0,'J14_scope_not_promoted')
    out.append({'host':row['host'],'a':a,'f':f,'H':H,'G5':str(G5),'G5_bits':G5.bit_length(),'margins':margins})

# Exact local pencil/exterior identities. The canonical plane is supported
# on five coordinates; the remaining positive block is unchanged.
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def mm(A,B): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def det(A):
    if len(A)==0:return F(1)
    if len(A)==1:return A[0][0]
    return sum((-1)**j*A[0][j]*det([r[:j]+r[j+1:] for r in A[1:]]) for j in range(len(A)))
def extentry(A,I,J):return det([[A[i][j] for j in J] for i in I])
local_cases=0; exterior_checks=0
for q in (3,5,7):
  n=7; z=[F(1),F(2),F(),F(),F(),F(),F(1)]
  v=[F(1),F(),F(),F(),F(),F(),F(-1)]
  ck(sum(x*y for x,y in zip(z,v))==0,'rank_one_nilpotent_plane')
  for c,d in ((0,1),(1,0),(1,2),(2,1),(2,2)):
    hc=eye(n);hd=eye(n);hi=eye(n)
    for i in range(n):
      for j in range(n):
        hc[i][j]+=F(c,q)*z[i]*v[j]
        hd[i][j]+=F(d,q)*z[i]*v[j]
        hi[i][j]-=F(c,q)*z[i]*v[j]
    ck(mm(hc,hi)==eye(n),'exact_pencil_inverse')
    for variant in range(3):
      k=eye(n)
      if variant==0:k[0][6]=F(1)
      elif variant==1:k[4][0]=F(1);k[6][5]=F(1)
      else:k[0],k[6]=k[6],k[0]
      g=mm(mm(hd,k),hi);local_cases+=1
      ck(all(g[i][j]==k[i][j] for i in (4,5) for j in (4,5)),'integral_large_positive_block')
      for j in (1,2,3):
        inds=list(combinations(range(n),j))
        # All principal entries and a deterministic off-diagonal sample.
        pairs=[(I,I) for I in inds]+[(inds[i],inds[(3*i+1)%len(inds)]) for i in range(len(inds))]
        for I,J in pairs:
          val=extentry(g,I,J)
          ck((q*q*val).denominator==1,'exterior_pole_at_most_two');exterior_checks+=1
      N=[[g[i][j]-F(i==j) for j in range(n)] for i in range(n)]
      NN=mm(N,N);tr=sum(N[i][i] for i in range(n))
      for i in range(n):
        for j in range(n):
          rhs=sum(N[i][j]*N[k0][k0]-N[i][k0]*N[k0][j] for k0 in range(n))
          ck(rhs==N[i][j]*tr-NN[i][j],'square_from_exterior_minors')
          ck((q*q*rhs).denominator==1,'trace_corrected_square_pole')

# Unit signature-one unipotents in a Euclidean-orthonormal Witt basis.
unipotent_cases=0
for m in (1,2,4):
  size=m+2;J=sp.zeros(size);J[0,size-1]=J[size-1,0]=1
  for i in range(1,size-1):J[i,i]=1
  for seed in range(6):
    vv=sp.Matrix([((seed+i)%3)-1+sp.I*((2*seed+i)%3-1) for i in range(m)])
    if seed==0:vv=sp.zeros(m,1)
    vv2=sp.simplify((vv.conjugate().T*vv)[0])
    for tt in (-2,0,3):
      h=sp.eye(size)
      for i in range(m):h[0,i+1]=-sp.conjugate(vv[i]);h[i+1,size-1]=vv[i]
      h[0,size-1]=-vv2/2+sp.I*tt;N=h-sp.eye(size)
      ck(sp.simplify(h.conjugate().T*J*h-J)==sp.zeros(size),'exact_signature_one_unipotent')
      ck(N**3==sp.zeros(size),'cube_zero')
      rk=N.rank();ck(rk in (0,1,2),'rank_at_most_two')
      ck((rk==2)==(vv2!=0),'rank_two_square_nonzero')
      ck(sp.simplify(vv2**2)<=sp.simplify(4*h[0,size-1]*sp.conjugate(h[0,size-1])),'linear_square_norm_bound')
      ck(sp.simplify(N**2-sp.Matrix(size,size,lambda i,j:-vv2 if (i,j)==(0,size-1) else 0))==sp.zeros(size),'exact_square_block')
      unipotent_cases+=1

# Exact degree-six reciprocity identity and the two-trace reduction.
x,c=sp.symbols('x c',real=True)
P=(x-1)**6+c*x**3
ck(sp.expand(x**6*P.subs(x,1/x)-P)==0,'degree_six_reciprocity')
ck(sp.expand(P/x**3-(x+1/x-2)**3-c)==0,'residual_cubic_identity')
for c0 in (-27,-8,-1,1,8,27):
    w=sp.symbols('w')
    disc=sp.discriminant(w**3+c0,w)
    ck(disc==-27*c0*c0<0,'two_nonreal_residual_w_roots')
for n in (7,10,43,169):
  # Number of Jordan blocks is n-rank(N), independent of block sizes.
  for q in (3,5,113):
    den=prod(q**j-1 for j in range(1,n))
    for rk in (1,2):
      num=prod(q**j-1 for j in range(1,n-rk))
      ck(F(num,den)==F(1,prod(q**j-1 for j in range(n-rk,n))),'exact_green_rank_ratio')

report={'finding':'AM-DO-060','status':'PASS','timestamp_utc':datetime.now(timezone.utc).isoformat(),
 'exact_assertions':len(checks),'local_pencil_cases':local_cases,'exterior_checks':exterior_checks,
 'unipotent_cases':unipotent_cases,'hosts':out,'checks':checks,
 'scope':'Exact arithmetic margins, local pencil/exterior and signature-one unipotent diagnostics. No enumeration or evaluation of the actual rational remainder; no Lean.'}
Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ('finding','status','timestamp_utc','exact_assertions','local_pencil_cases','exterior_checks','unipotent_cases','hosts')},indent=2))
