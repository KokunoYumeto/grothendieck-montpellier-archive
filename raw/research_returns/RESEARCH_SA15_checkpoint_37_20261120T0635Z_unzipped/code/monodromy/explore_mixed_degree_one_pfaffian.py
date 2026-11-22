#!/usr/bin/env python3
"""Original executed universal mixed Pfaffian exploration, retained unchanged.
The first stdout was observed at 2026-11-19 14:34 UTC; no group claim.
"""
import sympy as s
from functools import lru_cache
a=s.symbols('a');u=s.symbols('u0:3');v=s.symbols('s0:9');vars=(a,)+v
M=s.Matrix([[u[0],a*u[2],a*u[1]],[u[2],u[1],u[0]],[0,u[2],u[1]+u[2]]]);R=s.Matrix([[1,0,a],[0,0,a],[0,a,a]])
J=s.Matrix([[0,0,1],[0,1,0],[1,0,0]]);S=s.Matrix([[u[1],u[0],0],[u[2],0,u[0]],[0,u[2],u[1]]])
A=s.zeros(9)
for i in range(3):
 for j in range(3):A+=v[3*i+j]*s.kronecker_product(R*M.diff(u[i]),J*S.diff(u[j]))
def md(e):return s.Poly(s.expand(e),*vars,modulus=2).as_expr()
@lru_cache(None)
def pf(t):
 if not t:return s.Integer(1)
 i=t[0];return md(sum(A[i,j]*pf(t[1:k]+t[k+1:]) for k,j in enumerate(t[1:],1)))
p=pf(tuple(range(1,9)))
print('pf0=',s.factor(p,extension=True));print('quotient=',s.Poly(p,*vars,modulus=2).exquo(s.Poly(v[0],*vars,modulus=2)).as_expr())
