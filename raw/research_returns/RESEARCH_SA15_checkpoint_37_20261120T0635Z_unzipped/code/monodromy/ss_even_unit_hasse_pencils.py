#!/usr/bin/env python3
"""Exact exploratory unit-image determinants in supersingular degree two.

No monodromy or global irreducibility conclusion is inferred.  All arithmetic
is over F2[t], encoded by integers; fraction-free elimination checks every
polynomial division.  A fixed nonzero three-row minor of (s,d1s,d2s) is kept
constant on each pencil, so no denominator is hidden in the quotient matrix.
"""
import itertools,json,random,time
from pathlib import Path
import sympy as sp
started=time.perf_counter()
B=[(0,0),(1,0),(2,0),(3,0),(0,1),(1,1)]; ix={a:i for i,a in enumerate(B)}
n=36
def cp(a,b):
 u,v=a[0]+b[0],a[1]+b[1]
 terms=[(u,v)] if v<2 else [(u,1),(u+3,0)]
 out=0
 for u,v in terms:
  if v: z=(u//2,1) if u%2 else (u//2+1,0)
  elif u%2:z=(u//2,0)
  else:continue
  out^=1<<ix[z]
 return out
def deriv(a):
 u,v=a;out=0
 if u%2:out^=1<<ix[(u-1,v)]
 if v:out^=1<<ix[(u+2,0)]
 return out
one=[[cp(a,b) for b in B] for a in B]
der=[deriv(a) for a in B]
def dbits(s,factor):
 out=0
 for a,b in itertools.product(range(6),repeat=2):
  if not (s>>(6*a+b))&1:continue
  if factor==0:
   for i in range(6):
    if (der[a]>>i)&1:out^=1<<(6*i+b)
  else:
   for j in range(6):
    if (der[b]>>j)&1:out^=1<<(6*a+j)
 return out
def matrix(s):
 out=[[0]*n for _ in range(n)]
 for a,b in itertools.product(range(6),repeat=2):
  if not (s>>(6*a+b))&1:continue
  for u,v in itertools.product(range(6),repeat=2):
   for i,j in itertools.product(range(6),repeat=2):
    if (one[a][u]>>i)&1 and (one[b][v]>>j)&1:out[6*i+j][6*u+v]^=1
 return out
def rref(rows,width):
 rows=rows[:];piv=[];r=0
 for j in range(width):
  z=next((i for i in range(r,len(rows)) if (rows[i]>>j)&1),None)
  if z is None:continue
  rows[r],rows[z]=rows[z],rows[r]
  for i in range(len(rows)):
   if i!=r and (rows[i]>>j)&1:rows[i]^=rows[r]
  piv.append(j);r+=1
 return rows[:r],piv
def pmul(a,b):
 z=0
 while b:
  if b&1:z^=a
  b>>=1;a<<=1
 return z
def pdiv(a,b):
 assert b
 q=0
 while a and a.bit_length()>=b.bit_length():
  e=a.bit_length()-b.bit_length();q^=1<<e;a^=b<<e
 assert a==0
 return q
def psquare(a):return sum(((a>>i)&1)<<(2*i) for i in range(a.bit_length()))
def det(A):
 A=[r[:] for r in A];m=len(A);prev=1
 for k in range(m-1):
  z=next((i for i in range(k,m) if A[i][k]),None)
  if z is None:return 0
  A[k],A[z]=A[z],A[k];pivot=A[k][k]
  for i in range(k+1,m):
   for j in range(k+1,m):A[i][j]=pdiv(pmul(A[i][j],pivot)^pmul(A[i][k],A[k][j]),prev)
   A[i][k]=0
  prev=pivot
 return A[-1][-1]
s0=60944792081
U0=[s0,dbits(s0,0),dbits(s0,1)]
rows0=[sum(((u>>i)&1)<<j for j,u in enumerate(U0)) for i in range(n)]
R=[];seen=[]
for i,row in enumerate(rows0):
 if len(rref(seen+[row],3)[1])>len(R):R.append(i);seen.append(row)
 if len(R)==3:break
assert len(R)==3
# Invert the constant three-row matrix.
aug=[rows0[i]|(1<<(3+j)) for j,i in enumerate(R)]
ar,ap=rref(aug,3);assert ap==[0,1,2]
Pinv=[row>>3 for row in ar]
constraints=[]
for i in R:
 for op in range(3):
  constraints.append(sum((((1<<j) if op==0 else dbits(1<<j,op-1))>>i&1)<<j for j in range(n)))
cr,cpiv=rref(constraints,n)
null=[]
for j in range(n):
 if j in cpiv:continue
 v=1<<j
 for row,p in zip(cr,cpiv):
  if (row>>j)&1:v^=1<<p
 null.append(v)
J=[i for i in range(n) if i not in R]
C0=matrix(s0);rng=random.Random(248681504);records=[];t=sp.Symbol('t')
for trial in range(6):
 s1=0
 for v in null:
  if rng.randrange(2):s1^=v
 U1=[s1,dbits(s1,0),dbits(s1,1)]
 assert all(not ((u>>i)&1) for u in U1 for i in R)
 U=[[((U0[j]>>i)&1)|(((U1[j]>>i)&1)<<1) for j in range(3)] for i in range(n)]
 Un=[[0]*3 for _ in range(n)]
 for i,j in itertools.product(range(n),range(3)):
  for a in range(3):
   if (Pinv[a]>>j)&1:Un[i][j]^=U[i][a]
 assert [[Un[i][j] for j in range(3)] for i in R]==[[int(a==b) for b in range(3)] for a in range(3)]
 C1=matrix(s1);M=[[C0[i][j]|(C1[i][j]<<1) for j in range(n)] for i in range(n)]
 # Independently check the three displayed kernel vectors as polynomials.
 for a in range(3):
  for i in range(n):
   z=0
   for j in range(n):z^=pmul(M[i][j],U[j][a])
   assert z==0
 N=[]
 for i in J:
  row=[]
  for j in J:
   z=M[i][j]
   for a,r in enumerate(R):z^=pmul(psquare(Un[i][a]),M[r][j])
   row.append(z)
  N.append(row)
 h=det(N);assert h&1 and h.bit_length()<=37
 p=sp.Poly(sum(((h>>i)&1)*t**i for i in range(h.bit_length())),t,modulus=2)
 factors=sp.factor_list(p)[1]
 records.append({'trial':trial,'s0_bits':s0,'s1_bits':s1,'pivot_rows':R,'nullspace_dimension':len(null),
  'polynomial_bits':h,'degree':p.degree(),'factors':[{'polynomial':str(f.as_expr()),'degree':f.degree(),'multiplicity':e} for f,e in factors],
  'derivative_gcd_degree':sp.gcd(p,p.diff()).degree(),'squarefree':sp.gcd(p,p.diff()).degree()==0})
out={'status':'PASS','scope':'exploratory six exact degree-two unit-image Hasse pencils; no global geometry inferred',
 'method':'constant kernel minor; root-removed quotient matrix; exact F2[t] Bareiss determinant',
 'records':records,'runtime_seconds':time.perf_counter()-started}
Path(__file__).resolve().parents[1].joinpath('outputs/ss_even_unit_hasse_pencils.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
