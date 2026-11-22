#!/usr/bin/env python3
"""Independent ss degree-three monomial matrix and finite-group certificate."""
from pathlib import Path
import itertools,json,time,math
import sympy as sp
started=time.perf_counter();m=9;n=81
B=[(i,0) for i in range(5)]+[(i,1) for i in range(4)];ix={v:i for i,v in enumerate(B)}
def coeff(a,b):
 u=a[0]+b[0];v=a[1]+b[1];terms=[(u,v)] if v<2 else [(u,1),(u+3,0)];ans={}
 for i,j in terms:
  if j:q=(i//2,1) if i%2 else (i//2+1,0)
  elif i%2:q=(i//2,0)
  else:continue
  k=ix[q];ans[k]=ans.get(k,0)^1
 return [k for k,z in ans.items() if z]
one=[[coeff(a,b) for b in B] for a in B]
s=1726640724722881915971767;C=sp.zeros(n)
for a,b in itertools.product(range(m),repeat=2):
 if not s>>(m*a+b)&1:continue
 for u,v in itertools.product(range(m),repeat=2):
  for i,j in itertools.product(one[a][u],one[b][v]):
   C[m*i+j,m*u+v]=1-int(C[m*i+j,m*u+v])
def rank2(M):
 rows=[[int(z)%2 for z in row] for row in M.tolist()];r=0
 for j in range(M.cols):
  pivot=next((i for i in range(r,len(rows)) if rows[i][j]),None)
  if pivot is None:continue
  rows[r],rows[pivot]=rows[pivot],rows[r]
  for i in range(r+1,len(rows)):
   if rows[i][j]:rows[i]=[a^b for a,b in zip(rows[i],rows[r])]
  r+=1
 return r
assert rank2(C)==rank2(C*C)==80
v=sp.Matrix([(s>>j)&1 for j in range(n)])
assert all(int(z)%2==0 for z in C*v)
T=sp.Symbol('T');cp=sp.Poly(C.charpoly(T).as_expr(),T,modulus=2)
f,rem=sp.div(cp,sp.Poly(T,T,modulus=2));assert rem.is_zero
bits=sum((int(c)%2)<<a[0] for a,c in f.terms());assert bits==1489954141958205319760151
assert bits!=sum(((bits>>j)&1)<<(80-j) for j in range(81))
def mul(a,b):
 z=0
 while b:
  if b&1:z^=a
  a<<=1;b>>=1
 return z
def mod(a,b=bits):
 while a and a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
 return a
def gcd(a,b):
 while b:a,b=b,mod(a,b)
 return a
z=2
for j in range(1,81):
 z=mod(mul(z,z))
 if j in (16,40):assert gcd(bits,z^2)==1
assert z==2
ell=4278255361
assert all(ell%d for d in range(2,math.isqrt(ell)+1))
assert pow(2,80,ell)==1 and pow(2,40,ell)!=1 and pow(2,16,ell)!=1
def xp(e):
 r,a=1,2
 while e:
  if e&1:r=mod(mul(r,a))
  a=mod(mul(a,a));e>>=1
 return r
assert xp((1<<80)-1)==1 and xp(((1<<80)-1)//ell)!=1
out={'status':'PASS','degree':3,'section_bits':s,'basis':B,'rank_C':80,'rank_C2':80,
 'polynomial_bits':bits,'primitive_prime':ell,'irreducible':True,'nonreciprocal':True,
 'independent_matrix_and_integer_charpoly':True,'runtime_seconds':time.perf_counter()-started}
Path(__file__).resolve().parents[1].joinpath('outputs/verify_supersingular_degree_three_group.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
