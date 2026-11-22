#!/usr/bin/env python3
"""Independent exact verifier: rebuild the two degree-two matrices from monomials.
Uses no discovery functions or stored matrices; computes integer characteristic
polynomials then reduces mod2, and gives a literal image witness for the
fixed-quotient obstruction.
"""
import itertools,json,time
from pathlib import Path
import sympy as sp
started=time.perf_counter()
B=[(0,0),(1,0),(2,0),(3,0),(0,1),(1,1)];index={x:i for i,x in enumerate(B)}
def cproduct(a,b):
 exponent=a[0]+b[0];ypower=a[1]+b[1]
 terms=[(exponent,ypower)] if ypower<2 else [(exponent,1),(exponent+3,0)]
 answer={}
 for u,v in terms:
  if v:target=(u//2,1) if u%2 else (u//2+1,0)
  elif u%2:target=(u//2,0)
  else:continue
  j=index[target];answer[j]=answer.get(j,0)^1
 return [j for j,c in answer.items() if c]
def derive(a):
 u,v=a;terms=[]
 if u%2:terms.append((u-1,v))
 if v:terms.append((u+2,0))
 ans=0
 for t in terms:ans^=1<<index[t]
 return ans
one=[[cproduct(a,b) for b in B] for a in B]
def rebuild(s):
 C=sp.zeros(36);lam=0
 for a,b in itertools.product(range(6),repeat=2):
  if not (s>>(6*a+b))&1:continue
  da,db=derive(B[a]),derive(B[b])
  for i,j in itertools.product(range(6),repeat=2):
   if (da>>i)&1 and (db>>j)&1:lam^=1<<(6*i+j)
  for u,v in itertools.product(range(6),repeat=2):
   for i,j in itertools.product(one[a][u],one[b][v]):
    C[6*i+j,6*u+v]=1-int(C[6*i+j,6*u+v])
 return C,lam
def v(bits):return sp.Matrix([(bits>>i)&1 for i in range(36)])
def rank2(M):
 rows=[[int(c)%2 for c in row] for row in M.tolist()];r=0
 for j in range(M.cols):
  pivot=next((i for i in range(r,len(rows)) if rows[i][j]),None)
  if pivot is None:continue
  rows[r],rows[pivot]=rows[pivot],rows[r]
  for i in range(r+1,len(rows)):
   if rows[i][j]:rows[i]=[a^b for a,b in zip(rows[i],rows[r])]
  r+=1
 return r
t=sp.Symbol('T');polys=[];records=[]
for s,lam_expected in [(60944792081,408961052),(1642027529,20508)]:
 C,lam=rebuild(s);assert lam==lam_expected
 assert all(int(z)%2==0 for z in C*v(lam)-v(lam))
 assert rank2(C)==rank2(C*C)==33
 cp=sp.Poly(C.charpoly(t).as_expr(),t,modulus=2)
 bits=sum((int(c)%2)<<m[0] for m,c in cp.terms());polys.append(cp)
 records.append({'section_bits':s,'lambda_bits':lam,'rank_C':33,'rank_C2':33,
                 'integer_charpoly_mod2_bits':bits})
 if s==1642027529:
  mu=34911202640
  assert all(int(z)%2==0 for z in (C-sp.eye(36))*v(mu)-v(lam))
  assert rank2(C-sp.eye(36))==35
  records[-1].update({'image_witness_bits':mu,'rank_C_minus_I':35,
      'literal_equation':'(C-I)*mu=lambda','fixed_space_annihilated_by_lambda':True})
f,rem=sp.div(polys[0],sp.Poly(t**3*(t+1),t,modulus=2));assert rem.is_zero
f_bits=sum((int(c)%2)<<m[0] for m,c in f.terms());assert f_bits==4853921047
coeff,factors=sp.factor_list(f)
assert len(factors)==1 and factors[0][1]==1 and factors[0][0].degree()==32
assert f_bits!=sum(((f_bits>>i)&1)<<(32-i) for i in range(33))
def pmul(a,b):
 z=0
 while b:
  if b&1:z^=a
  a<<=1;b>>=1
 return z
def mod(a):
 while a.bit_length()>32:a^=f_bits<<(a.bit_length()-33)
 return a
def powx(e):
 z,a=1,2
 while e:
  if e&1:z=mod(pmul(z,a))
  a=mod(pmul(a,a));e>>=1
 return z
assert all(65537%j for j in range(2,257))
assert pow(2,32,65537)==1 and pow(2,16,65537)!=1
assert powx((1<<32)-1)==1 and powx(((1<<32)-1)//65537)!=1
out={'status':'PASS','basis':B,'matrix_reconstruction':'independent monomial Cartier and derivative rules',
 'characteristic_polynomial_method':'36x36 integer SymPy charpoly reduced mod2',
 'certificates':records,'kernel_polynomial_bits':f_bits,'kernel_polynomial':str(f.as_expr()),
 'irreducible':True,'nonreciprocal':True,'primitive_prime':65537,
 'runtime_seconds':time.perf_counter()-started}
Path(__file__).resolve().parents[1].joinpath('outputs/verify_supersingular_degree_two_group.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
