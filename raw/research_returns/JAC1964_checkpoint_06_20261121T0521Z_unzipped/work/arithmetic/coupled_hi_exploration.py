"""Noncertified exploration of a formal coupled HI functional; not a proof."""
import numpy as np
rng=np.random.default_rng(1964)
n=6

def herm(z): return (z+z.conj().T)/2

def randh(): return herm(rng.normal(size=(2*n,2*n))+1j*rng.normal(size=(2*n,2*n)))
def tr(z): return np.trace(z).real

def G(M,P):
 R,S,B=M[:n,:n],M[n:,n:],M[:n,n:]
 X,Y,C=P[:n,:n],P[n:,n:],P[:n,n:]
 return tr(R)*tr(Y)+tr(X)*tr(S)-2*np.trace(B@C.conj().T).real

def e3pol(M,P):
 return tr(M)**2*tr(P)-tr(M@M)*tr(P)-2*tr(M)*tr(M@P)+2*tr(M@M@P)

def I0(M,P): return e3pol(M,P)-e3pol(M[:n,:n],P[:n,:n])-e3pol(M[n:,n:],P[n:,n:])

def dpol(A,B):
 # coefficient of t in det(A+tB), divided by 3, exact algebraic polynomial.
 return sum(np.linalg.det(np.column_stack([B[:,j] if k==j else A[:,k] for k in range(3)])) for j in range(3))/3

def IH(M,P):
 B,C=M[:n,n:],P[:n,n:]
 return -6*(-dpol(B[:3,:3],C[:3,:3])+dpol(B[3:,3:],C[3:,3:])).real

mins=[]
for rank in range(2,13):
 max0=-1e99; maxh=-1e99; ratio=1e99; count=0
 for _ in range(300):
  Z=rng.normal(size=(2*n,rank))+1j*rng.normal(size=(2*n,rank))
  P=Z@Z.conj().T; P/=tr(P)
  gp=G(P,P)
  if gp<1e-12: continue
  M=randh(); M-=G(M,P)/gp*P; M/=np.linalg.norm(M)
  a,b=I0(M,P),IH(M,P)
  max0=max(max0,a); maxh=max(maxh,a+0.1*b)
  if abs(b)>1e-12: ratio=min(ratio,-a/abs(b))
  count+=1
 mins.append(dict(rank=rank,count=count,max_even=max0,max_perturbed=maxh,minimum_ratio=ratio))
import json
print(json.dumps({'scope':'NONCERTIFIED random formal-model check only; no positivity theorem', 'results':mins},indent=2))
