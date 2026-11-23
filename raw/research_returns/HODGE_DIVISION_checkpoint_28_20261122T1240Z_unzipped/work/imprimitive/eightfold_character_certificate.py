#!/usr/bin/env python3
"""HD-N14: universal exact exterior block identities and modular rank checks.
21 November 2026. GPT-6 Astra Pro, inherited effort, /root/imprimitive.
The symbolic part checks all coefficients of all nine independent moments.
"""
from itertools import combinations
from pathlib import Path
from random import Random
import json
N=8

def add(*ps):
 out={}
 for z in ps:
  for m,c in z.items():out[m]=out.get(m,0)+c
 return {m:c for m,c in out.items() if c}
def scale(z,c):return {m:v*c for m,v in z.items() if v*c}
def mul(z,w):
 out={}
 for m,c in z.items():
  for n,d in w.items():
   if m&n:continue
   inv=sum((n&((1<<i)-1)).bit_count() for i in range(2*N) if(m>>i)&1)
   out[m|n]=out.get(m|n,0)+(-1)**inv*c*d
 return {m:c for m,c in out.items() if c}
def wedge(i,z):return mul({1<<i:1},z)
def contract(i,z):return {m^(1<<i):(-1)**((m&((1<<i)-1)).bit_count())*c for m,c in z.items() if(m>>i)&1}
def op(j,z):return wedge(N+j,z) if j<N else contract(j-N,z)
def weight(mask):
 return sum((1 if(i<4 or i>=12) else -1) for i in range(16) if(mask>>i)&1)
H={(1<<i)|(1<<(N+i)):1 for i in range(N)}
powers=[{0:1}]
for j in range(1,N+1):
 z=mul(powers[-1],H);assert all(c%j==0 for c in z.values())
 powers.append({m:c//j for m,c in z.items()})
plus=sum(1<<i for i in range(4))+sum(1<<(N+i) for i in range(4,8))
minus=sum(1<<i for i in range(4,8))+sum(1<<(N+i) for i in range(4))
tp={plus:1};tm={minus:1};t=add(tp,tm)
UA=list(range(4))+list(range(8,12))
UB=list(range(4,8))+list(range(12,16))
# Universal c1 injection: all sixteen Weil columns are distinct monomials.
cols1=[op(j,t) for j in range(16)]
assert all(len(c)==1 for c in cols1)
assert len({next(iter(c)) for c in cols1})==16
assert {weight(next(iter(c))) for c in cols1}=={-7,7}
for j in range(16):
 expected=-1 if j in UA else 1
 assert all(weight(m)==expected for pol in powers for m in op(j,pol))
# The 56 outside columns inject through distinct Weil monomials of weights +-6.
diag=[]
for group,wt in ((UA,6),(UB,-6)):
 for i,j in combinations(group,2):
  c=op(i,op(j,t));assert len(c)==1 and weight(next(iter(c)))==wt
  diag.append({'operators':[i,j],'mask':next(iter(c)),'sign':next(iter(c.values()))})
  assert all(weight(m)==(-2 if group is UA else 2) for pol in powers for m in op(i,op(j,pol)))
assert len({e['mask'] for e in diag})==56
# Check every coefficient of all nine moments in each of the 64 middle columns.
middle=[]
for i in UA:
 for j in UB:
  assert not op(i,op(j,t))
  ia=i%8;jb=j%8
  eta=mul({1<<(N+ia):1},{1<<(N+jb):1})
  deriv=(i>=8)+(j>=8)
  signs=set()
  for k in range(9):
   got=op(i,op(j,powers[k]))
   expect=mul(eta,powers[k-deriv]) if k>=deriv else {}
   assert all(weight(m)==0 for m in got)
   if expect:
    first=next(iter(expect));sign=got.get(first,0)//expect[first]
    assert sign in(-1,1) and got==scale(expect,sign);signs.add(sign)
   else:assert not got
  assert len(signs)==1
  middle.append({'operators':[i,j],'pair':[ia,jb],'derivative':deriv,'sign':signs.pop()})
# Injectivity in every coefficient degree: recover every eta from a complement monomial.
recover=[]
for k in range(7):
 for ia in range(4):
  for jb in range(4,8):
   indices=[u for u in range(8) if u not in(ia,jb)][:k]
   mask=sum(1<<u for u in indices)+sum(1<<(N+u) for u in indices+[ia,jb])
   vals=[]
   for ii in range(4):
    for jj in range(4,8):
     eta=mul({1<<(N+ii):1},{1<<(N+jj):1})
     vals.append(mul(eta,powers[k]).get(mask,0))
   assert sum(v!=0 for v in vals)==1 and vals[ia*4+(jb-4)] in(-1,1)
   recover.append([k,ia,jb,mask,vals[ia*4+(jb-4)]])
# Additional modular checks of the full maps against the universal formula.
p=1009

def mod(z):return {m:c%p for m,c in z.items() if c%p}
def rank(cols):
 piv={}
 for col in cols:
  z=mod(col)
  while z:
   r=min(z);c=z[r]
   if r not in piv:
    piv[r]=mod(scale(z,pow(c,-1,p)));break
   z=mod(add(z,scale(piv[r],-c)))
 return len(piv)

def run(m):
 v=add(*(scale(powers[i],m[i]) for i in range(9)),t)
 col1=[op(j,v) for j in range(16)]
 col2=[op(i,col1[j]) for i,j in combinations(range(16),2)]
 hankel=[{k:m[k+j] for k in range(7)} for j in range(3)]
 rho=rank(hankel);r1=rank(col1);r2=rank(col2)
 assert r1==16 and r2==56+16*rho
 return {'moments':m,'rho':rho,'rank1':r1,'rank2':r2}
examples=[run([0]*9)]
for j in range(9):
 m=[0]*9;m[j]=1;examples.append(run(m))
examples.append(run([1,0,-1,0,1,0,-1,0,1]))
rng=Random(144)
for j in range(10):examples.append(run([rng.randrange(p) for i in range(9)]))
result={'statement':'HD-N14','date':'2026-11-21','author':'GPT-6 Astra Pro; inherited effort; /root/imprimitive',
 'c1_monomial_columns':cols1,'diagonal_columns':diag,'middle_columns':middle,'coefficient_recovery_rows':recover,
 'hankel_moment_indices':[[k,k+1,k+2] for k in range(7)],'exact_rank_formula':'16; 56+16*rank(M_P)',
 'modulus':p,'full_modular_checks':examples,
 'scope':'All exterior block identities and coefficient-recovery entries are exact integers. Full-map numerical ranks are additional modular checks. Ext, trace, isogeny and Fourier statements are proved in the TeX fragment.'}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(result,indent=2)+'\n')
print('Universal coefficient identities PASS: 16 first-order, 56 diagonal, 64 mixed columns; 112 coefficient recoveries.')
print('Full modular checks PASS:',len(examples),'cases; rank set',sorted({e['rank2'] for e in examples}))
print('Saved',out)
