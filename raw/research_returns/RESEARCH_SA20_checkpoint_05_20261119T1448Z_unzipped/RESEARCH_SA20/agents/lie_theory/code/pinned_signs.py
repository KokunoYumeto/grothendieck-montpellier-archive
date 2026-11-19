#!/usr/bin/env python3
"""Exact pinned diagram signs, using the root-lattice Chevalley cocycle.
For simply laced Cartan A let epsilon(alpha_i,alpha_j) be -1 on the
diagonal and for i>j adjacent, and +1 otherwise.  Extend bimultiplicatively.
Every positive-root decomposition is checked; then every nonzero root
bracket is checked. This does not infer E6 from smaller examples.
"""
from itertools import product
import numpy as np
from coxeter_normalizers import cartan

def check(name,A,perm):
    n=len(A);I=np.eye(n,dtype=np.int64);S=[]
    for i in range(n):
        z=I.copy();z[i]-=A[i];S.append(z)
    R={tuple(map(int,I[:,i])) for i in range(n)};todo=list(R)
    for a in todo:
        for z in S:
            b=tuple(map(int,z@a))
            if b not in R:R.add(b);todo.append(b)
    def eps(a,b):
        e=sum(a[i]*b[i] for i in range(n))+sum(a[i]*b[j] for i in range(n) for j in range(i) if A[i,j]==-1)
        return (-1)**(e%2)
    def sigma(a):
        b=[0]*n
        for i,j in enumerate(perm):b[j]=a[i]
        return tuple(b)
    E=[tuple(map(int,I[:,i])) for i in range(n)]
    eta={e:1 for e in E}
    for a in sorted((a for a in R if min(a)>=0),key=sum):
        if a in eta:continue
        values=[]
        for e in E:
            b=tuple(x-y for x,y in zip(a,e))
            if b in eta:values.append(eta[b]*eps(sigma(b),sigma(e))*eps(b,e))
        assert values and len(set(values))==1
        eta[a]=values[0]
    for a in list(eta):eta[tuple(-x for x in a)]=eta[a]
    brackets=0
    for a,b in product(R,repeat=2):
        q=tuple(x+y for x,y in zip(a,b))
        if q in R:
            assert eps(a,b)*eta[q]==eta[a]*eta[b]*eps(sigma(a),sigma(b));brackets+=1
    theta=max(R,key=sum)
    print(name,'roots=',len(R),'highest=',theta,'permutation=',tuple(i+1 for i in perm),
          'highest-root sign=',eta[theta],'all root brackets checked=',brackets)

if __name__=='__main__':
    for n in range(2,10):
        A=2*np.eye(n,dtype=np.int64)
        for i in range(n-1):A[i,i+1]=A[i+1,i]=-1
        check('A'+str(n),A,list(reversed(range(n))))
    for n in range(4,9):
        A=2*np.eye(n,dtype=np.int64)
        for i in range(n-2):A[i,i+1]=A[i+1,i]=-1
        A[n-3,n-1]=A[n-1,n-3]=-1
        p=list(range(n));p[-2:]=p[-2:][::-1];check('D'+str(n),A,p)
        if n==4:check('D4-triality',A,[2,1,3,0])
    check('E6',cartan('E6'),[5,1,4,3,2,0])
