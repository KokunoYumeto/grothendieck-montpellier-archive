#!/usr/bin/env python3
"""Integral regular primitive Coxeter eigenvectors in every exceptional type.

All arithmetic is in Z[z]/Phi_h, with norms computed as exact resultants.
The certificate asserts that every root value is a unit after inverting h.
"""
from pathlib import Path
from itertools import product
import json
import sympy as s
OUT=Path(__file__).resolve().parents[1]/'logs'
z=s.Symbol('z')
for typ in ['G2','F4','E6','E7','E8']:
 data=json.loads((OUT/f'normalizer_{typ}.json').read_text())
 A=s.Matrix(data['cartan']);c=s.Matrix(data['coxeter']);r=A.rows;h=data['h']
 C=c.inv().T;I=s.eye(r);S=[]
 for i in range(r):
  q=I.copy()
  for j in range(r):q[i,j]-=A[i,j]
  S.append(q)
 roots={tuple(I[:,i]) for i in range(r)};todo=list(roots)
 for alpha in todo:
  for q in S:
   beta=tuple(q*s.Matrix(alpha))
   if beta not in roots:roots.add(beta);todo.append(beta)
 phi=s.Poly(s.cyclotomic_poly(h,z),z)
 powers=[I]
 for j in range(1,h):powers.append(powers[-1]*C)
 found=None
 for seed in range(r):
  v=[]
  for i in range(r):
   v.append(s.rem(sum(powers[j][i,seed]*z**((-j)%h) for j in range(h)),phi.as_expr(),z))
  if all(t==0 for t in v):continue
  values=[];bad=False
  for alpha in sorted(roots):
   f=s.rem(sum(alpha[i]*v[i] for i in range(r)),phi.as_expr(),z)
   norm=int(s.resultant(phi.as_expr(),f,z))
   primes=set(s.factorint(abs(norm))) if norm else {0}
   if not primes <= set(s.factorint(h)):
    bad=True;break
   values.append({'root':list(map(int,alpha)),'value':str(f),'norm':norm})
  if not bad:found=(seed,v,values);break
 assert found is not None,(typ,'no certified seed among coordinate vectors')
 seed,v,values=found
 assert all(s.rem(t,phi.as_expr(),z)==0 for t in C*s.Matrix(v)-z*s.Matrix(v))
 cert={'type':typ,'h':h,'cyclotomic_polynomial':str(phi.as_expr()),
       'cocharacter_coxeter':C.tolist(),'seed_index':seed+1,
       'eigenvector':list(map(str,v)),'all_root_values':values}
 (OUT/f'primitive_eigenvector_{typ}.json').write_text(json.dumps(cert,indent=2,default=int))
 print(typ,'h',h,'seed',seed+1,'vector',v,
       'distinct absolute norms',sorted({abs(x['norm']) for x in values}),
       'all root values are units over Z[1/h,zeta_h]')
