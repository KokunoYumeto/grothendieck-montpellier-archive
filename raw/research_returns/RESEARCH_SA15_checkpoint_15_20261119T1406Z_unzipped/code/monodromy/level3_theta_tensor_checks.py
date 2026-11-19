#!/usr/bin/env python3
"""Exact finite algebra for the level-three theta/Cartier symmetrizer.

This verifies the Schrödinger matrices and invariant-tensor index argument;
the relative-Cartier geometric equivariance is proved separately in TeX.
"""
import itertools,json,time
from pathlib import Path
import sympy as sp
started=time.perf_counter()
H=list(itertools.product(range(3),repeat=2));idx={a:i for i,a in enumerate(H)}
def add(a,b):return tuple((u+v)%3 for u,v in zip(a,b))
def sub(a,b):return tuple((u-v)%3 for u,v in zip(a,b))
def dot(a,b):return sum(u*v for u,v in zip(a,b))%3
def mul4(a,b):
 c=0
 while b:
  if b&1:c^=a
  a<<=1;b>>=1
  if a&4:a^=7
 return c
powers=[1,2,3]
checked=0
for central,x,y in itertools.product(range(3),H,H):
 A=[[0]*9 for _ in range(9)]
 for a in H:A[idx[add(a,x)]][idx[a]]=powers[(central+dot(y,a))%3]
 # A^t A^[2]=I is equivalent to A^[2]=A^(-t).
 for i,j in itertools.product(range(9),repeat=2):
  c=0
  for k in range(9):c^=mul4(A[k][i],mul4(A[k][j],A[k][j]))
  assert c==int(i==j)
 checked+=1
assert checked==243
allowed=[q for q in itertools.product(H,repeat=3) if add(add(q[0],q[1]),q[2])==(0,0)]
assert len(allowed)==81
for a,b,c in allowed:
 x=sub(b,a)
 assert (add(a,x),add(b,x),add(c,x))==(b,c,a)
remaining=set(allowed);orbits=[]
while remaining:
 a,b,c=min(remaining);orbit=set()
 for x in H:
  triple=(add(a,x),add(b,x),add(c,x));orbit.add(triple)
  orbit.add((triple[1],triple[0],triple[2]))
 for triple in orbit:
  assert all(tuple(p) in orbit for p in itertools.permutations(triple))
 remaining-=orbit;orbits.append(orbit)
assert len(orbits)==5
assert sorted(map(len,orbits))==[9,18,18,18,18]
orbits.sort(key=lambda o:(len(o),min(o)))
c=sp.symbols('c0:5');s=sp.symbols('s0:9');variables=c+s
def mod2(x):return sp.Poly(sp.expand(x),*variables,modulus=2).as_expr()
T={q:c[i] for i,o in enumerate(orbits) for q in o}
M=sp.Matrix(9,9,lambda k,j:sum(T.get((a,H[j],H[k]),0)*s[idx[a]] for a in H))
assert (M-M.T).applyfunc(mod2)==sp.zeros(9)
assert [mod2(M[i,i]-c[0]*s[i]) for i in range(9)]==[0]*9
assert (M*sp.Matrix(s)-c[0]*sp.Matrix([v*v for v in s])).applyfunc(mod2)==sp.zeros(9,1)
out={'scope':'Finite level3 Schrödinger/tensor algebra, dimension9',
 'finite_Heisenberg_matrices_checked':checked,
 'relative_target_duality':'rho(h)^[2]=rho(h)^(-transpose)',
 'modulation_allowed_triples':len(allowed),
 'translation_and_first_swap_orbit_sizes':list(map(len,orbits)),
 'invariant_first_two_symmetric_tensor_dimension':5,
 'all_five_basis_tensors_fully_symmetric':True,
 'universal_matrix_diagonal':'c0*(s0,...,s8)',
 'universal_beta_diagonal':'c0*s^[2]',
 'all_assertions_passed':True,'runtime_seconds':time.perf_counter()-started}
dest=Path(__file__).resolve().parents[1]/'outputs'/'level3_theta_tensor_checks.json'
dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
