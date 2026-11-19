#!/usr/bin/env python3
"""Exact genus-three single-line tangency with the mixed ES7 and R equations.

All kernel generators and trace-image inclusions are checked over the integers.
Modular elimination supplies matching rank lower bounds. Arithmetic q6 maps
and invariant-functional extension are separate written arguments.
"""
from functools import lru_cache
from itertools import combinations
from time import perf_counter
import numpy as np
import sympy as sp

started=perf_counter(); prime=101; alphabet='abcdef'

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

def nullspace(matrix,only_pivots=False):
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
    if only_pivots:return pivots
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

def R_c(D):
    # MSS2026v1 Proposition4.1 p11; indices converted from1-based to0-based.
    terms=[(-2,((0,1),(2,4),(3,6),(5,7))),
           (2,((0,1),(2,5),(3,6),(4,7))),
           (2,((0,1),(2,5),(3,7),(4,6))),
           (2,((0,1),(2,6),(3,5),(4,7))),
           (1,((0,2),(1,5),(3,6),(4,7)))]
    result=0
    for i in range(3):
        for first,poly,sign in [(alphabet[2*i],D[alphabet[2*i+1]],1),
                                (alphabet[2*i+1],D[alphabet[2*i]],-1)]:
            for tail,c in poly.items():
                if tail[-1]!='c':continue
                word=first+tail
                assert len(word)==9
                for coefficient,pairs in terms:
                    value=coefficient
                    for a,b in pairs:value*=pair(word[a],word[b])
                    result+=sign*c*value
    return result

@lru_cache(None)
def right_lie(word):
    if len(word)==1:return {word:1}
    return bracket({word[0]:1},right_lie(word[1:]))

def conjugator_for_b(poly):
    # Solve [B,b]=poly along each finite b^i core b^j coefficient chain.
    if not poly:return {}
    cores=set(word.strip('b') for word in poly)
    assert '' not in cores
    result={}
    for core in cores:
        count=7-len(core)
        assert count>=1
        cumulative=0
        for i in range(count):
            cumulative+=poly.get('b'*i+core+'b'*(count-i),0)
            if cumulative:result['b'*i+core+'b'*(count-1-i)]=cumulative
        assert cumulative+poly.get('b'*count+core,0)==0
    assert bracket(result,v['b'])==poly
    dynkin={}
    for word,c in result.items():dynkin=add(dynkin,scale(right_lie(word),c))
    assert dynkin==scale(result,6)
    return result

Ds=[];Dlabels=[]
for n0 in range(5):
 for n1 in range(5-n0):
    n=(n0,n1,4-n0-n1);ds=tuple(x for c in n for x in (c,c))
    rowwords=basis(ds);cols=[];images=[];specials=[]
    for i,x in enumerate(alphabet):
        if not n[i//2]:continue
        y=alphabet[i^1]
        if i==0:
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
assert len(Ds)==180
print('EXACT_PARTIAL_TANGENT_DIMENSION',len(Ds),flush=True)
for D in Ds:conjugator_for_b(D['b'])
print('EXACT_PAIRED_CONJUGATOR_CHECKS',len(Ds),flush=True)


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
        commutator=derbracket(D,delta)
        for word,c in ES(commutator).items():column[('ES',name,word)]=c
        if name=='abc':
            value=R_c(commutator)
            if value:column[('R',name,'c')]=value
    columns.append(column)
keys=sorted(set().union(*(set(c) for c in columns)))
trace=np.array([[col.get(key,0) for col in columns] for key in keys],dtype=np.int64)
assert int(np.max(np.abs(trace)))*trace.shape[1]*50 < 2**63
tracekernel,tracerank=nullspace(trace)
assert trace.shape==(7977,180)
assert tracerank==48 and tracekernel.shape[1]==132
independent_rows=nullspace(trace.T,only_pivots=True)
assert len(independent_rows)==48
rref,pivots=sp.Matrix(trace[independent_rows,:].tolist()).rref()
assert len(pivots)==48
exact_trace_kernel=[];trace_multipliers=[]
for free in range(trace.shape[1]):
    if free in pivots:continue
    denominator=sp.ilcm(*[sp.denom(rref[i,free]) for i in range(len(pivots))])
    coefficients=np.zeros(trace.shape[1],dtype=np.int64)
    coefficients[free]=int(denominator)
    for i,pivot in enumerate(pivots):coefficients[pivot]=int(-denominator*rref[i,free])
    assert int(np.max(np.abs(trace)))*trace.shape[1]*int(np.max(np.abs(coefficients)))<2**63
    assert np.all(trace@coefficients==0)
    trace_multipliers.append(int(denominator))
    exact_trace_kernel.append(coefficients)
C=np.array(exact_trace_kernel,dtype=np.int64).T
assert np.all(trace@C==0)
assert C.shape[1]==132
print('EXACT_TRACE_SHAPE',trace.shape,'RANK',tracerank,'KERNEL_DIMENSION',C.shape[1])
print('EXACT_TRACE_KERNEL_MULTIPLIERS',trace_multipliers)


programs=[['cdf','cef','aef','def','bef','cde'],['bce','adf','adf','abd','bce','abc']]
known=[]
for program in programs:
    D=deltas[names.index(program[-1])]
    for name in reversed(program[:-1]):D=derbracket(deltas[names.index(name)],D)
    known.append(contractions(D))
    for delta in deltas:
        commutator=derbracket(D,delta)
        assert not ES(commutator)
        assert R_c(commutator)==0

J=np.array(known,dtype=np.int64).T
assert nullspace(J)[1]==2
K=np.array([contractions(D) for D in Ds],dtype=np.int64).T
assert int(np.max(np.abs(K)))*K.shape[1]*int(np.max(np.abs(C)))<2**63
values=K@C
r,s=0,7
a,b,c,e=map(int,(J[r,0],J[r,1],J[s,0],J[s,1]))
determinant=a*e-b*c
assert determinant==-10752
for j in range(values.shape[1]):
    x,y=map(int,(values[r,j],values[s,j]))
    n1=e*x-b*y;n2=-c*x+a*y
    assert all(determinant*int(values[i,j])==n1*int(J[i,0])+n2*int(J[i,1]) for i in range(105))
print('SPECIFIED_EXTRA_ROW: coefficient of c in R([D,delta_abc])')
print('CHECKED_40_ACTUAL_SEVENFOLD_JOHNSON_BRACKETS')
print('EXACT_CONTRACTION_MINOR',[[int(J[i,j]) for j in range(2)] for i in (0,7)])
print('EXACT_CONTRACTION_MINOR_DETERMINANT',determinant)
print('EXACT_105_COORDINATE_INCLUSIONS',values.shape[1])
print('MAXIMUM_EXACT_KERNEL_COEFFICIENT',int(np.max(np.abs(C))))
print('PASS: all single-line balanced special derivations satisfying all mixed ES7 equations and the displayed R equation have complete contraction vectors in the span of two actual J6 brackets.')
print('Arithmetic universal-image maps, invariant extension, and the post-constraint torus projection are separate written proofs. No integral division is asserted.')
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
