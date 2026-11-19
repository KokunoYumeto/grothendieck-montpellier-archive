#!/usr/bin/env python3
"""Exact root certificates for highest marks and Dynkin-parabolic collisions.
Classical infinite families are proved uniformly in the text.  This additionally
prints low-rank examples; all exceptional root systems are exhausted.
"""
import numpy as np
import sympy as s
from coxeter_normalizers import cartan
from itertools import product

def classical(kind,n):
    A=2*np.eye(n,dtype=np.int64)
    for i in range(n-1):A[i,i+1]=A[i+1,i]=-1
    if kind=='B':A[-1,-2]=-2
    if kind=='C':A[-2,-1]=-2
    if kind=='D':
        A[-2,-1]=A[-1,-2]=0;A[-3,-1]=A[-1,-3]=-1
    return A
def run(name,A):
    n=len(A);I=np.eye(n,dtype=np.int64);S=[]
    for i in range(n):
        z=I.copy();z[i]-=A[i];S.append(z)
    R={tuple(map(int,I[:,i])) for i in range(n)};todo=list(R)
    for a in todo:
        for z in S:
            b=tuple(map(int,z@a))
            if b not in R:R.add(b);todo.append(b)
    d=[s.Rational(1)]*n
    for _ in range(n):
        for i,j in product(range(n),repeat=2):
            if i<j and A[i,j]:d[j]=d[i]*s.Rational(int(A[i,j]),int(A[j,i]))
    G=s.diag(*d)*s.Matrix(A)
    theta=max(R,key=sum);v=s.Matrix(theta);length=(v.T*G*v)[0]
    # alpha_i(theta^vee) = 2 (alpha_i,theta)/(theta,theta).
    labels=2*G*v/length
    marks=[0]+[i+1 for i,m in enumerate(theta) if m==1]
    pairs=[]
    for b in R:
        q=tuple(x-y for x,y in zip(theta,b))
        if q not in R:continue
        bv=s.Matrix(b);qv=s.Matrix(q)
        if (bv.T*G*bv)[0]==length and (qv.T*G*qv)[0]==length and (bv.T*G*qv)[0]==-length/2:pairs.append((b,q))
    print(name,'highest marks=',theta,'permitted deletion nodes=',marks)
    if pairs and max(labels)<=1:
        b,q=pairs[0]
        assert min(labels)>=0 and any(labels)
        print('  distinct nilpotent characteristics with same zeros:',list(labels),list(2*labels),'; A2 roots:',b,q)
    elif name[0]=='C' and n>=3:
        H=s.Matrix([1,1]+[0]*(n-2))
        roots=s.zeros(n)
        for i in range(n-1):roots[i,i]=1;roots[i,i+1]=-1
        roots[-1,-1]=2
        lab=roots*H
        print('  symplectic partitions:',[3,3]+[1]*(2*n-6),[2,2]+[1]*(2*n-4),'; labels:',list(2*lab),list(lab))

if __name__=='__main__':
    for kind,n in [('A',2),('B',3),('C',3),('D',4)]:run(kind+str(n),classical(kind,n))
    for kind in ['G2','F4','E6','E7','E8']:run(kind,cartan(kind))
