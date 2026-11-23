#!/usr/bin/env python3
"""AM-DO-064: exact partial-monomial ranks and unchanged short-sum bounds."""
from __future__ import annotations
import argparse, hashlib, itertools, json
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial, prod
from datetime import datetime, timezone
import sympy as sp

HERE=Path(__file__).parent
checks=[]
def ck(v,s):
    if not v: raise AssertionError(s)
    checks.append(s)

hp=HERE/'definite_oscillator_large_t_certificate.json'
gp=HERE/'definite_oscillator_minimal_denominator_certificate.json'
host=next(z for z in json.loads(hp.read_text())['rows'] if z['host']=='J56')
old=next(z for z in json.loads(gp.read_text())['hosts'] if z['host']=='J56')
f=a=168;n=169;m=164;H=8192
T=int(host['T']);Q=host['g0']*host['g1'];G=int(old['stabilizer_gcd'])
D0=7**140*29**144*5**84*13**84
NA=sum(comb(m,d)**2*factorial(m-d)*28**(m-d) for d in range(4))
ck(2**1767<NA<2**1768,'exact_total_partial_monomial_count')
ck(G<2**5022,'actual_last_column_fibre_bound')
ck(T>2**995 and T<2**996,'actual_prime_window')
ck(Q**4>2**281,'actual_auxiliary_product_quarter_bit_bound')
ck(2*(T-1)**2<2**997*(T-2),'exact_weighted_pencil_pair_bound')
ck(2**f*D0<1500**f,'actual_root_discriminant_bound')
ck(T**4>2**(23*f),'fractional_scale_for_all_s_ge_four')
ck(m<13**2,'positive_block_sqrt_bound')
ck(F(H**2,2)+F(1,2*H**2)<5793**2,'general_negative_column_radius')
ck(5793+F(13*1500,2*2**23)<5794,'positive_column_covering_radius')
ck(5793+F(5*1500,2)==9543,'five_block_covering_radius')

MS=f*m;MW=5*f
Vnum=(22*f*5794**2)**MS*(22*f*9543**2)**MW
Vden=7**(MS+MW)*factorial(MS)*factorial(MW)*D0**n
ck(Vnum<Vden*2**324076,'rational_archimedean_volume_upper_bound')
ck(Vnum>Vden*2**324075,'strict_volume_exponent_bracket')
ck(f+5022+324076+1==329267,'exact_constant_exponent')
ck(2*n*996+997==337645,'exact_support_exponent')
ck(2*334*33<2**136,'one_global_green_euler_factor')

rows=[];cell_count=0
for r in range(1,34):
    L=r*n-r*(r+1)//2
    E0=F(329267)-F(281,4)*167*L
    sr=min(f,int((-4096-E0)//337645))
    ck(E0+337645*sr<=-4096,'threshold_endpoint')
    if sr<f:ck(E0+337645*(sr+1)>-4096,'next_support_not_certified_by_this_bound')
    for s in range(5,sr+1):
        ck(E0+337645*s<=-4096,'every_retained_rank_support_cell')
        cell_count+=1
    rows.append({'r':r,'L_r':L,'R_r':sr})
ck(cell_count==2881,'exact_new_cell_count')
ck(cell_count<2**12,'strict_union_budget_4084')
ck(rows[-1]['R_r']==168 and rows[-2]['R_r']==168,'all_supports_at_ranks_32_33')
ck(F(329267)+337645*168-F(281,4)*167*rows[-2]['L_r']==-197313,
   'uniform_rank32_full_support_margin')

def rank_mod(mat,p):
    A=[[int(x)%p for x in row] for row in mat]
    nr=len(A);nc=len(A[0]) if A else 0;k=0
    for j in range(nc):
        z=next((i for i in range(k,nr) if A[i][j]),None)
        if z is None:continue
        A[k],A[z]=A[z],A[k]
        q=pow(A[k][j],-1,p);A[k]=[(q*x)%p for x in A[k]]
        for i in range(nr):
            if i!=k and A[i][j]:
                q=A[i][j];A[i]=[(x-q*y)%p for x,y in zip(A[i],A[k])]
        k+=1
        if k==nr:break
    return k

def graph_rank(k,edges):
    # edges maps source column to (target row, nonzero integer weight).
    indeg={i:0 for i in range(k)}
    for i,w in edges.values():indeg[i]+=1
    seen=set();r=0;paths=0;nonidentity=0
    for st in range(k):
        if indeg[st] or st in seen:continue
        paths+=1;v=st;length=0
        while v not in seen:
            seen.add(v);length+=1
            if v not in edges:break
            v=edges[v][0]
        r+=length;nonidentity+=length
    for st in range(k):
        if st in seen:continue
        v=st;length=0;weight=1
        while v not in seen:
            seen.add(v);length+=1;v,w=edges[v];weight*=w
        r+=length-(weight==1)
        if length!=1 or weight!=1:nonidentity+=length
    return r,paths,nonidentity

graph_models=0
for k in range(1,5):
  for defect in range(min(3,k)+1):
    z=k-defect
    for cols in itertools.combinations(range(k),z):
      for rows0 in itertools.combinations(range(k),z):
        for rows1 in itertools.permutations(rows0):
          for weights in itertools.product((-1,1),repeat=z):
            edges={j:(i,w) for j,i,w in zip(cols,rows1,weights)}
            A=sp.zeros(k)
            for j,(i,w) in edges.items():A[i,j]=w
            r,paths,supp=graph_rank(k,edges)
            ck(paths==defect,'graph_paths_equal_defect')
            ck((A-sp.eye(k)).rank()==r,'characteristic_zero_cycle_path_rank')
            ck(supp<=2*r,'nonidentity_coordinate_support')
            ck(A.T*A==sp.diag(*[int(j in edges) for j in range(k)]),
               'partial_isometry_defect_gram')
            for p in (3,5,11):
                ck(rank_mod((A-sp.eye(k)).tolist(),p)==r,'finite_rank_preserved_away_weights_order')
            graph_models+=1

# All possible mu28 cycle products at two split primes, with arbitrary
# distributions of edge weights. The rank only depends on their product.
mu_models=0
for p,g in ((29,2),(113,3)):
  ck(pow(g,p-1,p)==1 and all(pow(g,(p-1)//q,p)!=1 for q in sp.factorint(p-1)),
     'primitive_residue_generator')
  root=pow(g,(p-1)//28,p)
  ck(len({pow(root,j,p) for j in range(28)})==28,'mu28_reduction_injective')
  for k in range(1,9):
    for exponent in range(28):
      A=[[0]*k for _ in range(k)]
      exps=[(j*j+3*j+exponent)%28 for j in range(k-1)]
      exps.append((exponent-sum(exps))%28)
      for j,e in enumerate(exps):A[(j+1)%k][j]=pow(root,e,p)
      for j in range(k):A[j][j]=(A[j][j]-1)%p
      ck(rank_mod(A,p)==k-(exponent==0),'all_mu28_weighted_cycle_ranks')
      mu_models+=1
for order in (2,4,7,14,28):
    val=int(sp.cyclotomic_poly(order,sp.Symbol('x')).subs('x',1))
    ck(set(sp.factorint(val)).issubset({2,7}),'cyclotomic_difference_support')

# Defect three is possible under the linear-algebra exception. These
# rational unitary examples are not asserted to pass the actual G tests.
unitary_models=0
for defect in range(4):
  ks=defect+1;total=ks+5
  J=sp.eye(total);J[-1,-1]=-1;I=sp.eye(total)
  u=I[:,0];ell=I[:,ks]+I[:,-1];v=u
  N=-ell*(v.T*J)+v*(ell.T*J)-sp.Rational(1,2)*ell*(ell.T*J)
  h=I+N
  for j in range(defect):
    i=j+1;w=ks+j+1
    R=sp.eye(total);R[i,i]=R[w,w]=0;R[i,w]=1;R[w,i]=-1
    h=R*h
  A=h[:ks,:ks];B=h[ks:,:ks];JW=J[ks:,ks:]
  ck(h.T*J*h==J and h.det()==1,'exact_exception_unitarity_and_determinant')
  ck(A==sp.diag(1,*([0]*defect)),'attained_partial_monomial_defect')
  U=sp.Matrix.hstack(*(A-sp.eye(ks)).nullspace())
  BU=B*U
  ck(BU.rank()==1 and BU.T*JW*BU==sp.zeros(U.cols),
     'actual_nonzero_isotropic_cross_exception')
  ck(BU.T*JW*B==sp.zeros(U.cols,ks),'cross_orthogonality_to_all_BS')
  ck((sp.eye(ks)-A.T*A).rank()==defect,'defect_rank_attained')
  unitary_models+=1

out={'finding':'AM-DO-064','status':'PASS','timestamp_utc':datetime.now(timezone.utc).isoformat(),
     'exact_assertions':len(checks),'partial_monomial_count':str(NA),
     'partial_monomial_count_bits':NA.bit_length(),'constant_volume_exponent':324076,
     'new_cell_count':cell_count,'union_inverse_binary_bound':4084,'thresholds':rows,
     'graph_models':graph_models,'mu28_cycle_models':mu_models,
     'unitary_exception_models':unitary_models,'checks':checks,
     'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (hp,gp)},
     'scope':'Exact classification/rank and rational short-sum upper-bound diagnostics. No enumeration of actual rational correspondences, residual sign, period, or source SizesAt constructor.'}
ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,
    default=HERE/'definite_oscillator_exceptional_partial_monomial_certificate.json')
path=ap.parse_args().output;path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('checks','input_sha256','partial_monomial_count')},indent=2))
