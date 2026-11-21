#!/usr/bin/env python3
"""Exact finite supplements for E837, not a replacement for its all-size proof."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from datetime import datetime,timezone
import time,json,hashlib
start=time.perf_counter();checks=[]
def ck(name,c,scope):
 assert c,name
 checks.append({'name':name,'PASS':True,'scope':scope})
vertices=set(range(4));edges=list(combinations(range(4),2));four=[]
for chosen in combinations(edges,4):
 omitted=[e for e in edges if e not in chosen]
 covered=set().union(*(set(e) for e in omitted))
 ck('omitted_endpoints_'+str(len(four)),len(covered)>=3,'Exact four-edge combinatorics used after dimension equality; no matrix-size sampling.')
 four.append({'chosen':chosen,'omitted':omitted,'covered_vertices':len(covered)})
small=[]
for n in range(4):
 for es in combinations(edges,n):
  disjoint=[(a,b) for a,b in combinations(es,2) if not set(a)&set(b)]
  assert len(disjoint)<=1
  small.append({'edges':es,'complementary_pairs':len(disjoint)})
ck('all_small_support_graphs',len(small)==42,'All subsets of the six edges of size at most three, each with at most one complementary pair.')
# Squarefree polynomial arithmetic in A; a polynomial is mask -> rational coefficient.
def add(a,b):
 r=dict(a)
 for m,c in b.items():r[m]=r.get(m,F(0))+c
 return {m:c for m,c in r.items() if c}
def scale(a,c):return {m:v*c for m,v in a.items() if v*c}
def mul(a,b):
 r={}
 for m,c in a.items():
  for n,d in b.items():
   if not m&n:r[m|n]=r.get(m|n,F(0))+c*d
 return {m:c for m,c in r.items() if c}
def sub(a,b):return add(a,scale(b,-1))
one={0:F(1)};zero={};u=[{1<<i:F(1)} for i in range(4)]
pvals=[1,1,1,F(3,5),F(8,5),1];qvals=[1,2,3,F(9,5),F(16,5),1]
def anti(vals):
 M=[[{} for j in range(4)] for i in range(4)]
 for (i,j),v in zip(edges,vals):M[i][j]={0:F(v)};M[j][i]={0:-F(v)}
 return M
p=anti(pvals);q=anti(qvals)
# Actual nonlinear parameter change from ell: u1=ell1+ell2*ell3, others unchanged.
# Its inverse is ell1=u1-u2*u3, so this derivative matrix is exact in u coordinates.
H=[[dict(one) if i==j else {} for j in range(4)] for i in range(4)]
H[0][1]=u[2];H[0][2]=u[1]
def transpose(M):return [list(row) for row in zip(*M)]
def mm(A,B):
 return [[sum_poly(mul(A[i][k],B[k][j]) for k in range(4)) for j in range(4)] for i in range(4)]
def sum_poly(xs):
 z={}
 for a in xs:z=add(z,a)
 return z
pp=mm(mm(H,p),transpose(H));qq=mm(mm(H,q),transpose(H))
P={e:scale(mul(mul(u[e[0]],u[e[1]]),pp[e[0]][e[1]]),4) for e in edges}
Q={e:scale(mul(mul(u[e[0]],u[e[1]]),qq[e[0]][e[1]]),4) for e in edges}
count=0
for a in edges:
 for b in edges:
  ck('nonlinear_cross_'+str(count),not sub(mul(P[a],Q[b]),mul(Q[a],P[b])),'Actual triangular nonlinear parameter change of the integrable boundary; scalar cross minors still do not settle the module question.')
  count+=1
ratios=[F(p)/(F(p)+F(q)) for p,q in zip(pvals,qvals)]
ck('pencil_lambda_one_has_six_unit_coefficients',all(F(p)+F(q) for p,q in zip(pvals,qvals)),'Constant terms of all six transformed bracket factors are nonzero; the factors are units in A.')
ck('forced_constant_matrix_ratios_are_incompatible',len(set(ratios))==3,'After the proved matrix lemma forces pencil invertibility, the six degree-two equations demand three different scalar constant matrices.')
def sign(perm):return (-1)**sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
mixed={}
for a in edges:
 for b in edges:
  if not set(a)&set(b):mixed=add(mixed,scale(mul(P[a],Q[b]),sign(a+b)))
ck('nonlinear_mixed_wedge_socle_unchanged',mixed=={15:-F(64,5)},'Actual triangular coordinate change has Jacobian determinant one; exact quotient calculation confirms its nonzero mixed top coefficient.')
out={'status':'PASS','finished_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-start,'checks':checks,'check_count':len(checks),'four_edge_graphs':15,'small_support_graphs':42,'ordered_nonlinear_cross_minors':36,'constant_matrix_ratios':[str(t) for t in ratios],'nonlinear_mixed_socle':{str(m):str(c) for m,c in mixed.items()},'scope':'Exact finite graph and quotient-polynomial supplements. The universal filtered-matrix lemma, unit-pivot reduction, actual-module equations and global semiregularity interface are proofs, not asserted to follow from this finite run.','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('rm_square_artin_matrix_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2))
