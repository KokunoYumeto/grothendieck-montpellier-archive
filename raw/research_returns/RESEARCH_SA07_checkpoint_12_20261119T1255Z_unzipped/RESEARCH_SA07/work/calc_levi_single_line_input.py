#!/usr/bin/env python3
"""Exact decorated-tensor input for the Levi-invariant single-line problem.

This work program constructs the input space only. It makes no assertion
about the still uncomputed mixed-normalizer matrix or arithmetic q6.
"""
from itertools import combinations
from functools import lru_cache
from pathlib import Path
from time import perf_counter
from math import lcm
import pickle
import numpy as np
import sympy as sp

started=perf_counter();P=101;AA=-1;BB=-2

def pairings(items):
    if not items:yield ();return
    a=items[0]
    for j in range(1,len(items)):
        for rest in pairings(items[1:j]+items[j+1:]):yield ((a,items[j]),)+rest

def diagrams(n,acount,bcount):
    positions=tuple(range(n))
    for apos in combinations(positions,acount):
        rem=tuple(i for i in positions if i not in apos)
        for bpos in combinations(rem,bcount):
            other=tuple(i for i in rem if i not in bpos)
            for pairs in pairings(other):
                key=[None]*n
                for i in apos:key[i]=AA
                for i in bpos:key[i]=BB
                for label,(i,j) in enumerate(pairs):key[i]=key[j]=label
                yield tuple(key)

@lru_cache(None)
def permute(key,order):
    inverse={old:new for new,old in enumerate(order)};sign=1
    for label in set(key):
        if label<0:continue
        first,second=[i for i,x in enumerate(key) if x==label]
        if inverse[first]>inverse[second]:sign=-sign
    labels={};result=[]
    for i in order:
        x=key[i]
        if x<0:result.append(x)
        else:
            if x not in labels:labels[x]=len(labels)
            result.append(labels[x])
    return tuple(result),sign

def add(a,b,scale=1):
    out=dict(a)
    for key,c in b.items():
        out[key]=out.get(key,0)+scale*c
        if not out[key]:del out[key]
    return out

@lru_cache(None)
def dynkin_orders(n):
    if n==1:return (((0,),1),)
    out=[]
    for tail,c in dynkin_orders(n-1):
        shifted=tuple(i+1 for i in tail)
        out.append(((0,)+shifted,c));out.append((shifted+(0,),-c))
    return tuple(out)

def apply_orders(poly,orders):
    result={}
    for key,c in poly.items():
        for order,d in orders:
            new,sign=permute(key,order)
            result[new]=result.get(new,0)+c*d*sign
    return {key:c for key,c in result.items() if c}

def cyclic(poly):
    n=len(next(iter(poly))) if poly else 8
    return apply_orders(poly,tuple((tuple(range(i,n))+tuple(range(i)),1) for i in range(n)))

def dynkin(poly,head=0):
    if not poly:return {}
    n=len(next(iter(poly)))
    orders=tuple((tuple(range(head))+tuple(i+head for i in order),c) for order,c in dynkin_orders(n-head))
    return apply_orders(poly,orders)

def mod_pivots(matrix):
    A=(np.asarray(matrix,dtype=np.int64)%P).astype(np.int16)
    nr,nc=A.shape;r=0;pivots=[]
    for j in range(nc):
        rows=np.flatnonzero(A[r:,j])
        if not len(rows):continue
        i=r+int(rows[0]);A[[r,i]]=A[[i,r]]
        A[r,j:]=A[r,j:]*pow(int(A[r,j]),-1,P)%P
        targets=np.flatnonzero(A[r+1:,j])+r+1
        if len(targets):
            block=A[targets,j:];block-=A[targets,j,None]*A[r,j:];block%=P;A[targets,j:]=block
        pivots.append(j);r+=1
        if r==nr:break
    return pivots

def matrix_columns(columns):
    keys=sorted(set().union(*(set(c) for c in columns)))
    return np.array([[c.get(key,0) for c in columns] for key in keys],dtype=np.int64).reshape((len(keys),len(columns))),keys

def exact_kernel(matrix):
    rows=mod_pivots(matrix.T)
    if rows:R,pivots=sp.Matrix(matrix[rows,:].tolist()).rref()
    else:R,pivots=sp.zeros(0,matrix.shape[1]),()
    assert len(pivots)==len(rows)
    result=[]
    for free in range(matrix.shape[1]):
        if free in pivots:continue
        denominator=lcm(*[int(sp.denom(R[i,free])) for i in range(len(pivots))])
        v=[0]*matrix.shape[1];v[free]=int(denominator)
        for i,j in enumerate(pivots):v[j]=int(-denominator*R[i,free])
        assert all(sum(int(matrix[i,j])*v[j] for j in range(len(v)))==0 for i in range(matrix.shape[0]))
        result.append(v)
    return result,len(rows)

def linear_combination(columns,coefficients):
    out={}
    for poly,c in zip(columns,coefficients):
        if c:out=add(out,poly,c)
    return out

inputs=[];labels=[]
for m in range(1,5):
    keys=list(diagrams(6,m-1,m-1));index={key:i for i,key in enumerate(keys)}
    allA=[dynkin({key:1}) for key in keys]
    dyn=np.array([[col.get(key,0) for col in allA] for key in keys],dtype=np.int64)
    assert np.array_equal(dyn@dyn,6*dyn)
    rank=int(np.trace(dyn))//6
    selected=mod_pivots(dyn);assert len(selected)==rank
    As=[allA[j] for j in selected]
    tensors=[];equations=[]
    for A in As:
        comm={}
        for key,c in A.items():
            comm=add(comm,{(BB,)+key+(AA,):c,(BB,AA)+key:-c})
        T={key:-c for key,c in cyclic(comm).items()}
        lie=add(dynkin(T,1),T,-7)
        consistency=add({key:c for key,c in T.items() if key[0]==BB},comm,m)
        equations.append({(0,)+key:c for key,c in lie.items()}|{(1,)+key:c for key,c in consistency.items()})
        tensors.append(T)
    E,rows=matrix_columns(equations)
    kernel,erank=exact_kernel(E)
    for j,coeff in enumerate(kernel):
        T=linear_combination(tensors,coeff)
        assert T and dynkin(T,1)=={key:7*c for key,c in T.items()}
        assert cyclic(T)=={key:8*c for key,c in T.items()}
        inputs.append(T);labels.append(('positive',m,j))
    print('POSITIVE_BLOCK',m,'RAW_DIAGRAMS',len(keys),'LIE_PARAMETER_DIM',rank,
          'CONSTRAINT_MATRIX',E.shape,'RANK',erank,'INPUT_DIM',len(kernel),flush=True)

keys=list(diagrams(8,0,0))
allC=[cyclic({key:1}) for key in keys]
C=np.array([[col.get(key,0) for col in allC] for key in keys],dtype=np.int64)
assert np.array_equal(C@C,8*C)
selected=mod_pivots(C);assert len(selected)==int(np.trace(C))//8
Ts=[allC[j] for j in selected]
E,rows=matrix_columns([add(dynkin(T,1),T,-7) for T in Ts])
kernel,rank=exact_kernel(E)
assert len(kernel)==5
for j,coeff in enumerate(kernel):
    T=linear_combination(Ts,coeff)
    assert T and dynkin(T,1)=={key:7*c for key,c in T.items()}
    assert cyclic(T)=={key:8*c for key,c in T.items()}
    inputs.append(T);labels.append(('pure',0,j))
print('PURE_W_BLOCK','CYCLIC_DIM',len(Ts),'CONSTRAINT_MATRIX',E.shape,'RANK',rank,'INPUT_DIM',len(kernel))
print('TOTAL_FORMAL_INPUT_DIM',len(inputs))
with Path(__file__).with_suffix('.pickle').open('wb') as file:
    pickle.dump(dict(inputs=inputs,labels=labels),file)
print('SAVED',Path(__file__).with_suffix('.pickle').name)
print('SCOPE: exact stable input parametrization only; mixed scalar matrix and q6 vanishing are not computed.')
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
