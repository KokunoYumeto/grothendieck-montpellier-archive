"""Standalone exact-integer verifier for the five-plane permanent obstruction.

Only Python's standard library is used. Matrices are reconstructed from the
five explicit quadrics. No symbolic nullspace routine, SDP, rank oracle,
floating-point arithmetic, or generator import is used.
"""
from pathlib import Path
from itertools import combinations
import json,math,time

p=Path(__file__).with_name('permanent_apolar_certificate.json')
data=json.loads(p.read_text());A=5;B=9
assert data['A_dimension']==A and data['B_dimension']==B
expected=[[[0,4],[1,3]],[[0,5],[2,3]],[[1,5],[2,4]],[[0,7],[1,6]],[[0,8],[2,6]]]
assert data['slices_edges']==expected
PA=list(combinations(range(A),2));PB=list(combinations(range(B),2))
IA={x:i for i,x in enumerate(PA)};IB={x:i for i,x in enumerate(PB)}
def zero(m,n):return [[0]*n for _ in range(m)]
T=[zero(B,B) for _ in range(A)]
for a,edges in enumerate(expected):
 for i,j in edges:T[a][i][j]=T[a][j][i]=1
U=[[T[r//B][r%B][c] for c in range(B)] for r in range(A*B)]
K=zero(len(PA)*B,A*B)
for i in range(A):
 for a in range(A):
  if i==a:continue
  idx=IA[tuple(sorted((i,a)))];sgn=1 if i<a else -1
  for b in range(B):
   for c in range(B):K[idx*B+b][i*B+c]=sgn*T[a][b][c]
L=zero(*data['left_annihilator_shape'])
assert data['left_annihilator_shape']==[50,90]
for i,j,v in data['left_annihilator_entries']:
 assert L[i][j]==0 and isinstance(v,int)
 L[i][j]=v

def assert_zero_product(M,N):
 assert len(M[0])==len(N)
 for row in M:
  nonzero=[(k,x) for k,x in enumerate(row) if x]
  for j in range(len(N[0])):assert sum(x*N[k][j] for k,x in nonzero)==0
assert_zero_product(L,K)
H=zero(A*len(L),A*B)
for i in range(A):
 for a in range(A):
  if i==a:continue
  idx=IA[tuple(sorted((i,a)))];sgn=1 if i<a else -1
  for l in range(len(L)):
   for b in range(B):H[i*len(L)+l][a*B+b]=sgn*L[l][idx*B+b]
assert data['extra_extension_entry']==[2,0]
E=[row+[1 if r==2*B else 0] for r,row in enumerate(U)]
assert_zero_product(H,E)
R=zero(len(PB)*A,B*10)
for i in range(B):
 for b in range(B):
  if i==b:continue
  idx=IB[tuple(sorted((i,b)))];sgn=1 if i<b else -1
  for a in range(A):
   for k in range(10):R[idx*A+a][i*10+k]=sgn*E[a*B+b][k]

def determinant_bareiss(M):
 M=[row[:] for row in M];n=len(M)
 assert all(len(row)==n for row in M)
 if n==0:return 1
 sign=1;previous=1
 for k in range(n-1):
  pivot=next((i for i in range(k,n) if M[i][k]),None)
  if pivot is None:return 0
  if pivot!=k:M[k],M[pivot]=M[pivot],M[k];sign=-sign
  value=M[k][k]
  for i in range(k+1,n):
   entry=M[i][k]
   for j in range(k+1,n):
    numerator=value*M[i][j]-entry*M[k][j]
    quotient,remainder=divmod(numerator,previous)
    assert remainder==0
    M[i][j]=quotient
   M[i][k]=0
  previous=value
 return sign*M[-1][-1]

start=time.time();dets={}
matrices={'K':K,'L':L,'H':H,'E':E,'R':R}
expected_sizes={'K':40,'L':50,'H':35,'E':10,'R':82}
for name,M in matrices.items():
 cert=data['minor_certificates'][name]
 assert cert['shape']==[len(M),len(M[0])]
 r=cert['rank_minor_size'];assert r==expected_sizes[name]
 rows=cert['rows'];cols=cert['columns']
 assert len(rows)==len(set(rows))==len(cols)==len(set(cols))==r
 sub=[[M[i][j] for j in cols] for i in rows]
 det=determinant_bareiss(sub)
 assert det!=0 and det%data['prime']==cert['determinant_mod_prime']
 # These unit determinants make the obstruction characteristic-free.
 assert abs(det)==1
 dets[name]=det
out={'result':'PASS','integer_minor_sizes':expected_sizes,'integer_minor_determinants':dets,'identities_checked':['L K = 0','H E = 0'],'field_scope':'every field (all selected minors are units)','conclusion':'BR of the five-plane permanent tensor is at least 11 over every algebraically closed field','seconds':time.time()-start}
Path(__file__).with_name('permanent_apolar_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
