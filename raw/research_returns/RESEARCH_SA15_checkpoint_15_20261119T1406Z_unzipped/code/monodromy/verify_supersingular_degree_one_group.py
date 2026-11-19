#!/usr/bin/env python3
"""Independent verifier for the two stated ss E x E degree-one certificates.

The Frobenius polynomial is checked through an integer 27x27 characteristic
polynomial after restricting F8 scalars to F2, rather than the discovery
program's subset-determinant calculation.
"""
import itertools,json,time
from pathlib import Path
import sympy as sp
started=time.perf_counter()
def mul(a,b):
 c=0
 while b:
  if b&1:c^=a
  a<<=1;b>>=1
  if a&8:a^=11
 return c
assert all(mul(a,b) for a in range(1,8) for b in range(1,8))
def sq(a):return mul(a,a)
def dot(a,b):
 c=0
 for x,y in zip(a,b):c^=mul(x,y)
 return c
def matmul(A,B):return [[dot(row,col) for col in zip(*B)] for row in A]
def rank(A):
 A=[r[:] for r in A];r=0
 for j in range(len(A[0])):
  at=next((i for i in range(r,len(A)) if A[i][j]),None)
  if at is None:continue
  A[r],A[at]=A[at],A[r]
  inv=next(v for v in range(1,8) if mul(v,A[r][j])==1)
  A[r]=[mul(inv,a) for a in A[r]]
  for i in range(len(A)):
   if i!=r and A[i][j]:
    c=A[i][j];A[i]=[a^mul(c,b) for a,b in zip(A[i],A[r])]
  r+=1
 return r
# C(1*1)=C(x*x)=C(y*y)=0, C(1*x)=1,
# C(1*y)=x, C(x*y)=y; symmetric product table.
table={(0,1):0,(1,0):0,(0,2):1,(2,0):1,(1,2):2,(2,1):2}
def matrix(s):
 M=[[0]*9 for _ in range(9)]
 for a,b in itertools.product(range(3),repeat=2):
  for i,j in itertools.product(range(3),repeat=2):
   if (a,i) in table and (b,j) in table:
    M[3*table[a,i]+table[b,j]][3*i+j]^=s[3*a+b]
 return [list(row) for row in zip(*M)]
def frob3(A):
 A2=[[sq(a) for a in row] for row in A]
 A4=[[sq(a) for a in row] for row in A2]
 return matmul(matmul(A,A2),A4)
def determinant3(s):
 z=0
 for p in itertools.permutations(range(3)):
  z^=mul(mul(s[p[0]],s[3+p[1]]),s[6+p[2]])
 return z
def Q(s):return dot([sq(v) for v in s],s[::-1])
def prem(a,b):
 while a and a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
 return a
def pmul(a,b):
 z=0
 while b:
  if b&1:z^=a
  b>>=1;a<<=1
 return z
def pgcd(a,b):
 while b:a,b=b,prem(a,b)
 return a
f=419
x=2
for _ in range(8):x=prem(pmul(x,x),f)
assert x==2
x=2
for _ in range(4):x=prem(pmul(x,x),f)
assert pgcd(f,x^2)==1
rev=sum(((f>>i)&1)<<(8-i) for i in range(9))
assert rev!=f
assert all(pow(2,j,17)!=1 for j in range(1,8)) and pow(2,8,17)==1

s=[6,7,0,5,4,1,6,0,4]
A=matrix(s);B=frob3(A)
assert determinant3(s)!=0 and Q(s)!=0
assert rank(B)==8
# Since B^[2]=A^[2] A^[4] A is a cyclic permutation of A A^[2] A^[4],
# its characteristic polynomial equals that of B. Therefore cp_B is in F2[T].
# Restriction of scalars cubes cp_B. Equality of these monic cubes uniquely
# determines cp_B in the polynomial domain; no norm-descent ambiguity remains.
# Entry a acts by multiplication by a on basis1,alpha,alpha^2.
C=sp.zeros(27)
for i,j in itertools.product(range(9),repeat=2):
 for c in range(3):
  z=mul(B[i][j],1<<c)
  for r in range(3):C[3*i+r,3*j+c]=(z>>r)&1
t=sp.Symbol('T');cp=C.charpoly(t).as_expr()
actual=sum((int(c)%2)<<i[0] for i,c in sp.Poly(cp,t).terms())
expected=pmul(pmul(f<<1,f<<1),f<<1)
assert actual==expected

s0=[0,6,4,5,5,5,3,3,4];delta=[1]+[0]*8
A0=matrix(s0);B0=frob3(A0)
power=B0
for _ in range(8):power=matmul(power,B0)
assert rank(A0)==8 and rank(power)==7
assert determinant3(s0)!=0 and Q(s0)==0
u=[sq(sq(c)) for c in s0[::-1]];usq=[sq(c) for c in u]
assert u==[2,7,7,3,3,3,2,4,0]
assert dot(s0,u)==0 and all(dot(row,usq)==0 for row in A0)
v=[dot(row,usq) for row in matrix(delta)]
assert v==[0,0,0,0,4,3,0,5,5]
assert rank([u,v])==2
assert dot([sq(c) for c in s0[::-1]],delta)==6
out={'field':'F2[alpha]/(alpha^3+alpha+1)',
 'ordinary_section':s,'determinant_cubic_value':determinant3(s),'Hermitian_cubic_value':Q(s),
 'relative_Frobenius_polynomial_bits':f,'relative_Frobenius_polynomial':'T^8+T^7+T^5+T+1',
 'irreducible':True,'nonreciprocal':True,'primitive_prime':17,
 'independent_characteristic_polynomial_method':'27x27 integer matrix, reduction mod2, equals (T*f(T))^3',
 'local_section':s0,'local_direction':delta,'local_determinant_cubic_value':determinant3(s0),
 'local_Hermitian_cubic_value':Q(s0),'local_Hermitian_derivative':6,
 'local_full_linearized_rank':8,'local_full_semilinear_stable_rank':7,
 'local_kernel':u,'local_Frobenius_derivative':v,'kernel_derivative_rank':2,
 'all_assertions_passed':True,'runtime_seconds':time.perf_counter()-started}
dest=Path(__file__).resolve().parents[1]/'outputs'/'verify_supersingular_degree_one_group.json'
dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
