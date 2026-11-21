#!/usr/bin/env python3
"""Independent residual, matrix and binary-rank verifier for A39 pointing.

Imports no producer arithmetic. Uses polynomial-product/long-reduction field
multiplication, Newton series inversion and binary powering, then an F2
block-matrix rank check rather than F256 elimination. The geometric proof
identifies the certified matrix with a complete Riemann--Roch space.
"""
from pathlib import Path
import hashlib,json
P=Path(__file__).with_name('produce_A39_pointed_certificate.json')
D=json.loads(P.read_text());N=128
assert D['field_modulus']==0x11b and D['series_precision']==N

def fm(a,b):
 p=0
 for i in range(8):
  if b>>i&1:p^=a<<i
 for j in range(14,7,-1):
  if p>>j&1:p^=0x11b<<(j-8)
 return p
M=[[fm(a,b) for b in range(256)] for a in range(256)]
I=[0]+[next(b for b in range(1,256) if M[a][b]==1) for a in range(1,256)]
def trim(p):
 p=list(p)
 while p and not p[-1]:p.pop()
 return p

def pa(a,b):
 c=list(a)+[0]*max(0,len(b)-len(a))
 for i,x in enumerate(b):c[i]^=x
 return trim(c)

def pm(a,b):
 c=[0]*max(0,len(a)+len(b)-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):c[i+j]^=M[x][y]
 return trim(c)

def pd(a,b):
 a=trim(a);b=trim(b);q=[0]*max(0,len(a)-len(b)+1)
 while a and len(a)>=len(b):
  j=len(a)-len(b);c=M[a[-1]][I[b[-1]]];q[j]=c
  for i,x in enumerate(b):a[i+j]^=M[c][x]
  a=trim(a)
 return trim(q),a

def pgcd(a,b):
 while b:a,b=b,pd(a,b)[1]
 return [M[x][I[a[-1]]] for x in a]

def pp(a,n):
 r=[1]
 while n:
  if n&1:r=pm(r,a)
  a=pm(a,a);n//=2
 return r

def pad(a,n=N):return list(a[:n])+[0]*max(0,n-len(a))
def add(a,b,n=N):return [x^y for x,y in zip(pad(a,n),pad(b,n))]
def times(a,b,n=N):return pad(pm(a[:n],b[:n])[:n],n)
def scalar(a,c,n=N):return [M[c][x] for x in pad(a,n)]
def shifted(a,n,limit=N):return pad(([0]*n+list(a))[:limit],limit)
def square(a,n=N):
 c=[0]*n
 for i,x in enumerate(a[:(n+1)//2]):c[2*i]=M[x][x]
 return c

def inverse(a,n=N):
 assert a[0];b=[I[a[0]]];precision=1
 while precision<n:
  precision=min(2*precision,n)
  b=times(a,square(b,precision),precision)
 assert times(a,b,n)==[1]+[0]*(n-1)
 return pad(b,n)

cache={}
def power(a,e,n=N):
 key=(tuple(a),e,n)
 if key in cache:return cache[key]
 if e<0:r=power(inverse(a,n),-e,n)
 else:
  r=[1]+[0]*(n-1);b=pad(a,n);q=e
  while q:
   if q&1:r=times(r,b,n)
   b=square(b,n);q//=2
 cache[key]=r
 return r

def evaluate(p,x,n=N):
 r=[0]*n
 for c in reversed(p):r=times(r,x,n);r[0]^=c
 return r

u=D['u'];U=D['Delta_U'];v0=D['Delta_V'];h=D['h'];f=D['f'];A=D['Kummer_A'];B=D['Kummer_B']
assert u==188 and U==[224,80,1] and v0==[180,59]
assert pa(pa(pm(A,A),pm(pm(A,B),h)),pm(pm(B,B),f))==pp(U,5)
assert not pd(pa(A,pm(B,v0)),U)[1]
assert pgcd(U,pm(B,h))==[1]
assert U[1]!=0
assert D['zeta5']==12 and pp([12],5)==[1]
y=D['Y_lift_Delta_mod_U4'];U4=pp(U,4)
assert not pd(pa(pa(pm(y,y),pm(h,y)),f),U4)[1]
assert pd(y,U)[1]==v0
ybar=pa(y,h)
a=D['series_a_W'];Z=D['series_Z_W'];Xq=D['series_X_Q'];zq=D['series_z_Q']
assert all(len(x)==N for x in (a,Z,Xq,zq))
one=[1]+[0]*(N-1);zero=[0]*N
assert a[0]==I[u] and Z[0]==1 and Xq[0]==0 and zq[0]==92
S=shifted(a,2)
assert add(add(one,add(scalar(a,u),shifted(a,1))),add(shifted(power(a,3),4),scalar(shifted(power(a,5),8),u)))==zero
rhs=zero[:]
for j,c in enumerate(A):rhs=add(rhs,scalar(power(S,5-j),c))
for j,c in enumerate(B):rhs=add(rhs,scalar(shifted(power(S,2-j),1),c))
assert power(Z,5)==rhs
assert add(shifted(one,2),shifted(power(Xq,2),1))==evaluate(f,Xq)
assert power(zq,5)==add(evaluate(A,Xq),shifted(evaluate(B,Xq),1))
Ubar=add(add(one,scalar(S,80)),scalar(power(S,2),224));Uq=evaluate(U,Xq)

basis=[]
for i in range(5):
 Ui=pp(U,i);yb=pd(ybar,Ui)[1]
 for j in range(17-i):basis.append({'i':i,'A':[0]*j+Ui,'B':[]})
 for j in range(14+i):basis.append({'i':i,'A':pd([0]*j+yb,Ui)[1],'B':[0]*j+[1]})
assert basis==D['basis_L_32_piW'] and len(basis)==155

commonW={i:times(power(Z,i),power(Ubar,-i)) for i in range(5)}
commonQ={i:times(power(zq,i),power(Uq,-i)) for i in range(5)}

def local(term,m):
 i=term['i'];aa=term['A'];bb=term['B'];w=zero[:];q=zero[:]
 assert not pd(pa(aa,pm(bb,ybar)),pp(U,i))[1]
 assert len(aa)-1<=(m+2*i)//2 and len(bb)-1<=(m+2*i-5)//2
 for j,c in enumerate(aa):
  w=add(w,scalar(shifted(times(commonW[i],power(a,i-j)),m+2*i-2*j),c))
  q=add(q,scalar(times(commonQ[i],power(Xq,j)),c))
 for j,c in enumerate(bb):
  w=add(w,scalar(shifted(times(commonW[i],power(a,i-j-3)),m+2*i-5-2*j),c))
  q=add(q,scalar(shifted(times(commonQ[i],power(Xq,j)),1),c))
 return w,q

columns=[]
for term in basis:
 w,q=local(term,32);columns.append(w[:32]+q[:128])
matrix=[[column[i] for column in columns] for i in range(160)]
assert matrix==D['constraint_matrix_Rt']
# Expand multiplication by each field coefficient into an8x8 F2 block.
blocks=[]
for c in range(256):
 rows=[0]*8
 for j in range(8):
  image=M[c][1<<j]
  for i in range(8):
   if image>>i&1:rows[i]|=1<<j
 blocks.append(rows)
pivots={}
for row in matrix:
 binary=[0]*8
 for j,c in enumerate(row):
  for i in range(8):binary[i]|=blocks[c][i]<<(8*j)
 for value in binary:
  while value:
   pivot=value.bit_length()-1
   if pivot in pivots:value^=pivots[pivot]
   else:pivots[pivot]=value;break
assert len(pivots)==1240
ws=zero[:];qs=zero[:]
for term in D['Rs_function']:
 w,q=local(term,2);ws=add(ws,scalar(w,term['scalar']));qs=add(qs,scalar(q,term['scalar']))
assert ws[:6]==[0]*6 and ws[6]==189 and qs[:4]==[0]*4 and qs[4]==189
assert ws[:10]==D['Rs_function_t2_times_at_P'] and qs[:8]==D['Rs_function_at_Q']
result={'certificate_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'all_curve_norm_and_opposite_branch_identities':True,
        'all_local_series_residuals_to_precision128':True,
        'complete_basis_and_matrix_reconstructed':True,
        'binary_matrix_shape':[1280,1240],'binary_rank':len(pivots),
        'rank_over_F256':len(pivots)//8,'positive_Rs_function_checked':True,
        'scope':'Independent finite arithmetic verification, not formal verification. Geometric completeness and class inference require the accompanying mathematical proof.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2))
