#!/usr/bin/env python3
"""Independent HOS11--12 finite algebra; author proof/checker read, none imported."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
from collections import Counter
from flint import nmod_mat
import hashlib,json,time
start=time.perf_counter();out={'status':'PASS'}
def M(a):return nmod_mat(a,3)
def eye(n):return M([[int(i==j) for j in range(n)] for i in range(n)])
def col(v):return M([[x] for x in v])
def tv(v,c,J):return eye(len(v))+int(c)*col(v)*(col(v).transpose()*J)
def pair(v,w,J):return int((col(v).transpose()*J*col(w))[0,0])
I2=eye(2);J2=M([[0,1],[2,0]])
groups=0; comms=Counter();zero=0
for v in product(range(3),repeat=4):
 h=M([v[:2],v[2:]]);mu=int(h.det())
 if not mu:continue
 groups+=1
 assert h.transpose()*J2*h==mu*J2
 seen=False
 for x in product(range(3),repeat=2):
  hx=tuple(int(y) for y in h*col(x));b=pair(x,hx,J2)
  if b==0:continue
  seen=True
  for c in (1,2):
   tx=tv(x,c,J2);k=h*tx*h.inv()*tx.inv()
   assert k==tv(hx,c*pow(mu,-1,3),J2)*tv(x,-c,J2)
   assert int(k[0,0]+k[1,1])==(2+pow(mu,-1,3))%3
   assert k**(2 if mu==1 else 3)==2*I2
   comms[mu]+=1
 if not seen:
  zero+=1;assert h[0,1]==h[1,0]==0 and h[0,0]==h[1,1]
assert groups==48 and sum(comms.values())==576 and zero==2
out['all_GSp2_3']={'matrices':groups,'scalar_cases':zero,'commutator_cases':dict(comms)}

# Enumerate EVERY self-adjoint4D matrix by enumerating all alternating J*h.
J4=M([[0,0,1,0],[0,0,0,1],[2,0,0,0],[0,2,0,0]])
I4=eye(4);Z4=M([[0]*4 for _ in range(4)])
positions=list(combinations(range(4),2));types=0;cases=0
for values in product(range(3),repeat=6):
 a=[[0]*4 for _ in range(4)]
 for (i,j),v in zip(positions,values):a[i][j]=v;a[j][i]=-v%3
 h=J4.inv()*M(a)
 assert h.transpose()*J4==J4*h
 if h*h!=2*I4:continue
 types+=1
 assert h.transpose()*J4*h==2*J4
 for x in product(range(3),repeat=4):
  if not any(x):continue
  hx=tuple(int(y) for y in h*col(x))
  assert pair(x,hx,J4)==0
  assert any((x[i]*hx[j]-x[j]*hx[i])%3 for i,j in positions)
  for c in (1,2):
   tx=tv(x,c,J4);k=h*tx*h.inv()*tx.inv();N=k-I4
   assert N==-c*(col(x)*col(x).transpose()*J4+col(hx)*col(hx).transpose()*J4)
   assert N*N==Z4 and k**3==I4
   assert any(int(N[i,r]*N[j,s]-N[i,s]*N[j,r]) for i,j in positions for r,s in positions)
   cases+=1
assert types>0 and cases==160*types
out['all_selfadjoint_4D']={'tested_selfadjoint_matrices':3**6,
 'nonsquare_involutive_matrices':types,'vector_parameter_cases':cases}

# Direct matrix-entry exponent check for every Weyl translation/multiplication
# on function spaces F3^2 and F3^3, not a symbolic simplification of the text.
phase_cases=0;carriers=[]
for m in (2,3):
 vectors=list(product(range(3),repeat=m))
 for c,psi in product((1,2),repeat=2):
  f=lambda u:(-2*c*(u[0]*u[0]+u[1]*u[1]))%3
  counts=Counter(psi*f(u)%3 for u in vectors)
  assert [counts[z] for z in range(3)]==[3**(m-2),4*3**(m-2),4*3**(m-2)]
  for x in vectors:
   for y in vectors:
    gy=tuple((y[j]+c*x[j])%3 if j<2 else y[j] for j in range(m))
    for u in vectors:
     shifted=tuple((u[j]+x[j])%3 for j in range(m))
     left=f(u)+sum(y[j]*u[j]+2*x[j]*y[j] for j in range(m))-f(shifted)
     right=sum(gy[j]*u[j]+2*x[j]*gy[j] for j in range(m))
     assert psi*(left-right)%3==0
     phase_cases+=1
  carriers.append({'m':m,'c':c,'psi':psi,'counts':dict(counts)})
out['direct_Weyl_conjugation']={'exact_entry_exponent_checks':phase_cases,'carriers':carriers}
# Independent circular-convolution derivation of(1,4,4).
v=[1,2,0];v2=[sum(v[i]*v[(j-i)%3] for i in range(3)) for j in range(3)]
assert v2==[1,4,4]
delta=(1-F(1,27))/8
assert delta==F(13,108)
assert F(5,36)>delta and F(2,9)>delta
assert F(2,3)*(1-F(1,9))==F(16,27)>F(5,9)
assert delta<F(31,250)<F(1,4)
assert 6/(10*delta-1)==F(324,11)<30
ceil=lambda a:(a.numerator+a.denominator-1)//a.denominator
endpoints=[]
for e in range(27,30):
 lhs=2*e+6;rhs=2*ceil(F(e,2))+10*ceil(delta*e)
 assert rhs>lhs
 endpoints.append([e,lhs,rhs])
out['support_and_budget']={'delta':str(delta),'continuous_degree_ceiling':'324/11',
 'minimum_factor_degree':27,'endpoints':endpoints}
p=Path('HODGE_DIVISION_work/agents/g34_eightfolds/bireflection/higher_odd_symplectic_three_section.tex')
out['proof_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
assert out['proof_sha256']=='43d9154af45a2042e1cbbd5a0f536a7f932e0cad351e29e980a1ca5b3d65dae9'
out['seconds']=time.perf_counter()-start
Path(__file__).with_name('independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
