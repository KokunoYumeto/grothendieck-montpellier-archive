#!/usr/bin/env python3
"""Exact finite diagnostics for R032; not a global theta computation."""
from pathlib import Path
from itertools import product
from collections import Counter
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json
import sympy as sp
root=Path(__file__).resolve().parents[1]
counts=Counter()
def ck(x,label):
 assert x,label
 counts[label]+=1

def mul(A,B,q):
 return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%q for j in range(len(B[0]))] for i in range(len(A))]
def diag(A,extra):
 n=len(A);out=[[0]*(n+extra) for _ in range(n+extra)]
 for i in range(n):out[i][:n]=A[i][:]
 for i in range(n,n+extra):out[i][i]=1
 return out
def gl2(q):
 for a,b,c,d in product(range(q),repeat=4):
  det=(a*d-b*c)%q
  if det:
   u=pow(det,-1,q)
   yield [[a,b],[c,d]],[[u*d%q,-u*b%q],[-u*c%q,u*a%q]]
def f0(X,r):
 return int(all(X[i][j]==int(i==j) for i in range(len(X)) for j in range(r)))
def f1(X,r,q):
 # t=1. Exact nontrivial residue character on D in F_3^x.
 if any(X[i][j]!=int(i==j) for i in range(r) for j in range(r)):return 0
 if any(X[i][j] for i in range(r,len(X)) for j in range(r)):return 0
 if any(X[i][r] for i in range(r+1,len(X))):return 0
 d=X[r][r]
 if d==0:return 0
 return 1 if d==1 else -1
q=3;r=2
for g,gi in gl2(q):
 for v in product(range(q),repeat=6):
  X=[list(v[2*i:2*i+2]) for i in range(3)]
  Y=mul(mul(diag(gi,1),X,q),g,q)
  ck(f0(X,r)==f0(Y,r),'first G full residue space')
 # Full support plus every one-entry perturbation, including changes outside support.
 for B in product(range(q),repeat=r):
  for d in range(1,q):
   X=[[int(i==j) for j in range(r)]+[B[i]] for i in range(r)]
   X += [[0]*r+[d],[0]*(r+1)]
   samples=[X]
   for i in range(4):
    for j in range(3):
     for z in range(q):
      Z=[row[:] for row in X];Z[i][j]=z;samples.append(Z)
   for Z in samples:
    Y=mul(mul(diag(gi,2),Z,q),diag(g,1),q)
    ck(f1(Z,r,q)==f1(Y,r,q),'second G support character and complement')
# Complete r=t=1 residue space, including all zero-support cases.
for g in range(1,3):
 gi=pow(g,-1,3)
 for v in product(range(3),repeat=6):
  X=[list(v[2*i:2*i+2]) for i in range(3)]
  Y=mul(mul(diag([[gi]],2),X,3),diag([[g]],1),3)
  ck(f1(X,1,3)==f1(Y,1,3),'second G complete rank-one residue space')
# Nontrivial finite character projector and actual unequal class mass algebra.
P=sp.Matrix([[0,1,0],[0,0,1],[1,0,0]])
I=sp.eye(3);E=(2*I-P-P**2)/3
ck(E*E==E and E.T==E,'real central idempotent')
H0=sp.eye(3)/3;H2=sp.diag(*([sp.Rational(1,7)]*3+[sp.Rational(1,11)]*3))
Rho2=sp.diag(P,P);E2=sp.diag(E,E)
for a,b in [(1,2),(2,5),(sp.Rational(1,3),sp.Rational(2,7))]:
 U=(a*I).col_join(b*P)
 D=H0.inv()*U.T*H2
 R=U*(D*U).inv()
 ck(U*P==Rho2*U,'upward finite equivariance')
 ck(D*Rho2==P*D,'weighted adjoint finite equivariance')
 ck(D*R==I,'least inverse identity')
 ck(R*E==E2*R and D*E2==E*D,'same projector inverse with unequal masses')
# Actual field and group-order costs are carried, independently recomputed here.
hosts=[]
for host,n,f,g0,g1 in [('J14',43,42,4615409,5276377),('J56',169,168,22285932761,64072175441)]:
 field_bits=(1+n*(n+1)//2)*(g0.bit_length()+g1.bit_length())
 expected=43562 if host=='J14' else 1019986
 ck(field_bits==expected,'actual relative character field bound')
 vals=[]
 for g in (g0,g1):
  ck(g>n,'actual exponent unipotent prime')
  v=0
  for i in range(1,n+1):
   x=g**i-1
   while x%11==0:x//=11;v+=1
  vals.append(v)
 total=f*sum(vals)
 ck(total==(336 if host=='J14' else 21336),'full projector sufficient eleven denominator')
 hosts.append(dict(host=host,rank=n,additional_field_log2_bound=field_bits,full_group_eleven_valuation=total))
p=root/'research/genuine_projector_vertical_transport.md'
out=dict(finding='AM-R-032',status='PASS',completed_utc=datetime.now(timezone.utc).isoformat(),
 assertions=sum(counts.values()),groups=dict(counts),actual_hosts=hosts,
 proof_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
 scope='Exact finite raw G support/character invariance, weighted finite adjoint and inverse diagnostics, and carried field/order integers. Does not evaluate an automorphic function, class set, terminal period or integral theta inverse.')
(root/'checks/genuine_projector_vertical_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
