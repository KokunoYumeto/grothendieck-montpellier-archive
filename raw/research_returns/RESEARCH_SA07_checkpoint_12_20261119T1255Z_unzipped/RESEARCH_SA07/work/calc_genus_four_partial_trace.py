#!/usr/bin/env python3
"""Modular discovery calculation for partial symplectic-pair tangencies.

This is work only. Ranks modulo101 and their kernels do not assert rational
arithmetic image membership, a q6 value, or an arithmetic curve quotient.
"""
from functools import lru_cache
from itertools import combinations
from time import perf_counter
from pathlib import Path
import pickle
import sys
import numpy as np

started=perf_counter(); prime=101; genus=4; alphabet='abcdefgh'
constrained=2

def add(a,b):
    out=dict(a)
    for w,c in b.items():
        out[w]=(out.get(w,0)+c)%prime
        if not out[w]:del out[w]
    return out

def scale(a,c):return {w:c*v%prime for w,v in a.items() if c*v%prime}

def mul(a,b):
    out={}
    for w,c in a.items():
        for u,d in b.items():out[w+u]=(out.get(w+u,0)+c*d)%prime
    return {w:c for w,c in out.items() if c}

def bracket(a,b):return add(mul(a,b),scale(mul(b,a),-1))

def lyndon(w):return all(w<w[i:] for i in range(1,len(w)))

@lru_cache(None)
def standard(w):
    if len(w)==1:return {w:1}
    i=next(i for i in range(1,len(w)) if lyndon(w[i:]))
    return bracket(standard(w[:i]),standard(w[i:]))

def words(ds,prefix=''):
    if not any(ds):yield prefix;return
    for i,n in enumerate(ds):
        if n:
            dt=list(ds);dt[i]-=1
            yield from words(tuple(dt),prefix+alphabet[i])

@lru_cache(None)
def basis(ds):return tuple(w for w in words(ds) if lyndon(w))

def nullspace(matrix):
    work=np.array(matrix,dtype=np.int16)%prime
    if work.ndim==1:work=work.reshape((0,0))
    nrows,ncols=work.shape
    rank=0;pivots=[]
    for c in range(ncols):
        found=np.flatnonzero(work[rank:,c])
        if not len(found):continue
        pivot=rank+int(found[0])
        if pivot!=rank:work[[rank,pivot]]=work[[pivot,rank]]
        value=int(work[rank,c]);work[rank,c:]=work[rank,c:]*pow(value,-1,prime)%prime
        rows=np.flatnonzero(work[rank+1:,c])+rank+1
        if len(rows):
            factors=work[rows,c].copy();block=work[rows,c:]
            block-=factors[:,None]*work[rank,c:];block%=prime;work[rows,c:]=block
        pivots.append(c);rank+=1
        if rank==nrows:break
    free=[i for i in range(ncols) if i not in pivots]
    ker=np.zeros((ncols,len(free)),dtype=np.int64)
    for j,i in enumerate(free):ker[i,j]=1
    for row,pivot in reversed(list(enumerate(pivots))):
        ker[pivot,:]=(-work[row,pivot+1:].astype(np.int64)@ker[pivot+1:,:])%prime
    return ker,rank

v={x:{x:1} for x in alphabet}

def act(D,poly):
    out={}
    for w,c in poly.items():
        for i,x in enumerate(w):
            for u,d in D[x].items():
                key=w[:i]+u+w[i+1:]
                out[key]=(out.get(key,0)+c*d)%prime
    return {w:c for w,c in out.items() if c}

def derbracket(D,E):return {x:add(act(D,E[x]),scale(act(E,D[x]),-1)) for x in alphabet}

def pair(x,y):
    i,j=alphabet.index(x),alphabet.index(y)
    return (1 if i%2==0 else -1) if i//2==j//2 and i!=j else 0

@lru_cache(None)
def cyclic(w):return min(w[i:]+w[:i] for i in range(len(w)))

def ES(D):
    out={}
    for i in range(genus):
        for first,poly,sign in [(alphabet[2*i],D[alphabet[2*i+1]],1),
                                (alphabet[2*i+1],D[alphabet[2*i]],-1)]:
            for w,c in poly.items():
                value=sign*c*pair(first,w[0])%prime
                if value:
                    key=cyclic(w[1:]);out[key]=(out.get(key,0)+value)%prime
    return {w:c for w,c in out.items() if c}

def matchings(items):
    if not items:yield ();return
    first=items[0]
    for j in range(1,len(items)):
        rest=items[1:j]+items[j+1:]
        for m in matchings(rest):yield ((first,items[j]),)+m

chords=list(matchings(tuple(range(8))))
assert len(chords)==105

@lru_cache(None)
def word_contractions(word):
    result=[]
    for i,chord in enumerate(chords):
        value=1
        for a,b in chord:
            value*=pair(word[a],word[b])
            if not value:break
        if value:result.append((i,value))
    return result

def contractions(D):
    result=[0]*105
    for i in range(genus):
        for first,poly,sign in [(alphabet[2*i],D[alphabet[2*i+1]],1),
                                (alphabet[2*i+1],D[alphabet[2*i]],-1)]:
            for word,c in poly.items():
                for j,value in word_contractions(first+word):
                    result[j]=(result[j]+sign*c*value)%prime
    return result

def compositions(total,count):
    if count==1:
        yield (total,);return
    for first in range(total+1):
        for tail in compositions(total-first,count-1):yield (first,)+tail

Ds=[];Dlabels=[]
for n in compositions(4,genus):
    ds=tuple(x for c in n for x in (c,c))
    rowwords=basis(ds);cols=[];images=[];specials=[]
    for i,x in enumerate(alphabet):
        if not n[i//2]:continue
        y=alphabet[i^1]
        if i//2<constrained:
            deg=list(ds);deg[i]-=1;deg[i^1]-=1
            for w in basis(tuple(deg)):
                image=bracket(standard(w),v[x])
                cols.append((x,w));images.append(image)
                specials.append(bracket(image,v[y]) if i%2==0 else bracket(v[y],image))
        else:
            deg=list(ds);deg[i^1]-=1
            for w in basis(tuple(deg)):
                image=standard(w)
                cols.append((x,w));images.append(image)
                specials.append(bracket(image,v[y]) if i%2==0 else bracket(v[y],image))
    matrix=np.array([[poly.get(w,0) for poly in specials] for w in rowwords],dtype=np.int16)
    ker,rank=nullspace(matrix)
    print('BLOCK',n,'SHAPE',matrix.shape,'RANK_MOD101',rank,'NULLITY',ker.shape[1],flush=True)
    for j in range(ker.shape[1]):
        D={x:{} for x in alphabet}
        for i in np.flatnonzero(ker[:,j]):
            letter=cols[i][0];D[letter]=add(D[letter],scale(images[i],int(ker[i,j])))
        check={}
        for i in range(genus):
            x,y=alphabet[2*i:2*i+2]
            check=add(check,add(bracket(D[x],v[y]),bracket(v[x],D[y])))
        assert not check
        Ds.append(D);Dlabels.append((n,j))
print('PARTIAL_TANGENT_DIMENSION_MOD101',len(Ds),flush=True)

deltas=[]
for triple in combinations(alphabet,3):
    a,b,c=triple
    delta={x:add(add(scale(bracket(v[b],v[c]),pair(x,a)),
                       scale(bracket(v[c],v[a]),pair(x,b))),
                       scale(bracket(v[a],v[b]),pair(x,c))) for x in alphabet}
    deltas.append((''.join(triple),delta))
columns=[]
for j,D in enumerate(Ds):
    column={}
    for name,delta in deltas:
        for word,c in ES(derbracket(D,delta)).items():column[(name,word)]=c
    columns.append(column)
    if j%20==0:print('TRACE_COLUMNS',j,'OF',len(Ds),flush=True)
keys=sorted(set().union(*(set(c) for c in columns)))
trace=np.array([[col.get(key,0) for col in columns] for key in keys],dtype=np.int16)
tracekernel,tracerank=nullspace(trace)
K=np.array([contractions(D) for D in Ds],dtype=np.int64).T
onker=K@tracekernel%prime
_,contractionrank=nullspace(onker)
print('TRACE_SHAPE',trace.shape,'RANK_MOD101',tracerank,'KERNEL_DIMENSION',tracekernel.shape[1])
print('ALL105_CONTRACTIONS_ON_TRACE_KERNEL_RANK_MOD101',contractionrank)
destination=Path(__file__).with_name('partial_trace_genus4_pairs'+str(constrained)+'.pickle')
with destination.open('wb') as f:
    pickle.dump(dict(prime=prime,constrained=constrained,Ds=Ds,Dlabels=Dlabels,
                     tracekernel=tracekernel,contractions=K,onker=onker,
                     chord_patterns=chords,trace_rank=tracerank),f)
print('SAVED',destination.name)
print('WORK ONLY: no rational-kernel equality or universal arithmetic q6 compatibility inferred.')
print('ACTUAL_WALL_SECONDS',perf_counter()-started)
