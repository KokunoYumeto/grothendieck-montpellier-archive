#!/usr/bin/env python3
"""Exact two-pair partial tangency and geometric contraction-image certificate.

All kernel generators and trace-image inclusions are checked over the integers.
Modular elimination supplies matching rank lower bounds. Arithmetic q6 maps
and invariant-functional extension are separate written arguments.
"""
from functools import lru_cache
from itertools import combinations
from time import perf_counter
import numpy as np

started=perf_counter(); prime=101; alphabet='abcdef'
constrained=2

def add(a,b):
    out=dict(a)
    for w,c in b.items():
        out[w]=out.get(w,0)+c
        if not out[w]:del out[w]
    return out

def scale(a,c):return {w:c*v for w,v in a.items() if c*v}

def mul(a,b):
    out={}
    for w,c in a.items():
        for u,d in b.items():out[w+u]=out.get(w+u,0)+c*d
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
    work=(np.asarray(matrix,dtype=np.int64)%prime).astype(np.int16)
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
                out[key]=out.get(key,0)+c*d
    return {w:c for w,c in out.items() if c}

def derbracket(D,E):return {x:add(act(D,E[x]),scale(act(E,D[x]),-1)) for x in alphabet}

def pair(x,y):
    i,j=alphabet.index(x),alphabet.index(y)
    return (1 if i%2==0 else -1) if i//2==j//2 and i!=j else 0

@lru_cache(None)
def cyclic(w):return min(w[i:]+w[:i] for i in range(len(w)))

def ES(D):
    out={}
    for i in range(3):
        for first,poly,sign in [(alphabet[2*i],D[alphabet[2*i+1]],1),
                                (alphabet[2*i+1],D[alphabet[2*i]],-1)]:
            for w,c in poly.items():
                value=sign*c*pair(first,w[0])
                if value:
                    key=cyclic(w[1:]);out[key]=out.get(key,0)+value
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
    for i in range(3):
        for first,poly,sign in [(alphabet[2*i],D[alphabet[2*i+1]],1),
                                (alphabet[2*i+1],D[alphabet[2*i]],-1)]:
            for word,c in poly.items():
                for j,value in word_contractions(first+word):
                    result[j]=result[j]+sign*c*value
    return result

Ds=[];Dlabels=[]
for n0 in range(5):
 for n1 in range(5-n0):
    n=(n0,n1,4-n0-n1);ds=tuple(x for c in n for x in (c,c))
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
    assert all(abs(c)<32768 for poly in specials for c in poly.values())
    matrix=np.array([[poly.get(w,0) for poly in specials] for w in rowwords],dtype=np.int16)
    ker,rank=nullspace(matrix)
    print('BLOCK',n,'SHAPE',matrix.shape,'RANK_MOD101',rank,'NULLITY',ker.shape[1],flush=True)
    exact_matrix=matrix.astype(np.int64)
    assert int(np.max(np.abs(exact_matrix)))*exact_matrix.shape[1]*50 < 2**63
    kernel_multipliers=[]
    for j in range(ker.shape[1]):
        for multiplier in range(1,51):
            coefficients=(multiplier*ker[:,j]+prime//2)%prime-prime//2
            if np.all(exact_matrix@coefficients==0):
                break
        else:
            raise AssertionError(('Integer kernel lift failed',n,j))
        kernel_multipliers.append(multiplier)
        assert multiplier%prime and np.array_equal(coefficients%prime,multiplier*ker[:,j]%prime)
        D={x:{} for x in alphabet}
        for i in np.flatnonzero(coefficients):
            letter=cols[i][0];D[letter]=add(D[letter],scale(images[i],int(coefficients[i])))
        check={}
        for i in range(3):
            x,y=alphabet[2*i:2*i+2]
            check=add(check,add(bracket(D[x],v[y]),bracket(v[x],D[y])))
        assert not check
        Ds.append(D);Dlabels.append((n,j))
    print('EXACT_INTEGER_KERNEL_MULTIPLIERS',n,kernel_multipliers,flush=True)
assert len(Ds)==31
print('EXACT_PARTIAL_TANGENT_DIMENSION',len(Ds),flush=True)


deltas=[];names=[]
for triple in combinations(alphabet,3):
    a,b,c=triple
    delta={x:add(add(scale(bracket(v[b],v[c]),pair(x,a)),
                       scale(bracket(v[c],v[a]),pair(x,b))),
                       scale(bracket(v[a],v[b]),pair(x,c))) for x in alphabet}
    names.append(''.join(triple));deltas.append(delta)
columns=[]
for j,D in enumerate(Ds):
    column={}
    for name,delta in zip(names,deltas):
        for word,c in ES(derbracket(D,delta)).items():column[(name,word)]=c
    columns.append(column)
keys=sorted(set().union(*(set(c) for c in columns)))
trace=np.array([[col.get(key,0) for col in columns] for key in keys],dtype=np.int64)
assert int(np.max(np.abs(trace)))*trace.shape[1]*50 < 2**63
tracekernel,tracerank=nullspace(trace)
assert tracerank==15 and tracekernel.shape[1]==16
exact_trace_kernel=[];trace_multipliers=[]
for j in range(tracekernel.shape[1]):
    for multiplier in range(1,51):
        coefficients=(multiplier*tracekernel[:,j]+prime//2)%prime-prime//2
        if np.all(trace@coefficients==0):break
    else:raise AssertionError(('Exact trace kernel lift failed',j))
    trace_multipliers.append(multiplier)
    exact_trace_kernel.append(coefficients)
C=np.array(exact_trace_kernel,dtype=np.int64).T
assert np.all(trace@C==0)
print('EXACT_TRACE_SHAPE',trace.shape,'RANK',tracerank,'KERNEL_DIMENSION',C.shape[1])
print('EXACT_TRACE_KERNEL_MULTIPLIERS',trace_multipliers)

# Two literal nested brackets in the degree-one Johnson image. Every delta
# below is the actual image of a wedge of three homology generators.
programs=[['cdf','cef','aef','def','bef','cde'],
          ['bce','adf','adf','abd','bce','abc']]
geometry=[]
for program in programs:
    D=deltas[names.index(program[-1])]
    for name in reversed(program[:-1]):D=derbracket(deltas[names.index(name)],D)
    geometry.append(contractions(D))
J=np.array(geometry,dtype=np.int64).T
pivot=next((i,j,int(J[i,0])*int(J[j,1])-int(J[i,1])*int(J[j,0]))
           for i in range(105) for j in range(i+1,105)
           if int(J[i,0])*int(J[j,1])-int(J[i,1])*int(J[j,0]))
r,s,det=pivot
K=np.array([contractions(D) for D in Ds],dtype=np.int64).T
assert int(np.max(np.abs(K)))*K.shape[1]*int(np.max(np.abs(C))) < 2**63
values=K@C
certificates=[]
for j in range(values.shape[1]):
    first=int(values[r,j])*int(J[s,1])-int(values[s,j])*int(J[r,1])
    second=int(J[r,0])*int(values[s,j])-int(J[s,0])*int(values[r,j])
    assert abs(det)*int(np.max(np.abs(values[:,j]))) < 2**63
    assert (abs(first)+abs(second))*int(np.max(np.abs(J))) < 2**63
    assert np.array_equal(det*values[:,j],first*J[:,0]+second*J[:,1])
    certificates.append((first,second,det))
print('GEOMETRIC_NESTED_BRACKETS',programs)
print('GEOMETRIC_CONTRACTION_INDEPENDENCE_MINOR',pivot)
print('GEOMETRIC_CONTRACTION_MINOR_ENTRIES',J[[r,s],:].tolist())
print('EXACT_GEOMETRIC_IMAGE_COEFFICIENTS',certificates)
print('PASS: every105-contraction vector of the entire16-dimensional partial-tangent ES7 kernel lies in the contraction image of these two actual degree6 Johnson brackets.')
print('SCOPE: the invariant-functional extension, complete invariant contraction span, actual universal arithmetic quotient, and q6 vanishing are proved separately in text.')
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
