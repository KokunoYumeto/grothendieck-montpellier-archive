#!/usr/bin/env python3
"""Exact one-pair partial tangency with ES7 and MSS2026 R,S constraints.

All kernel generators and trace-image inclusions are checked over the integers.
Modular elimination supplies matching rank lower bounds. Arithmetic q6 maps
and invariant-functional extension are separate written arguments.
"""
from functools import lru_cache
from itertools import combinations
from time import perf_counter
import numpy as np
import sympy as sp
from rs_detector_support import RSDetector

started=perf_counter(); prime=101; alphabet='abcdef'
constrained=1
rs_detector=RSDetector(alphabet)

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
assert len(Ds)==180
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
        commutator=derbracket(D,delta)
        for word,c in ES(commutator).items():column[('ES',name,word)]=c
        rr,ss=rs_detector.derivation(commutator)
        for word,c in rr.items():column[('R',name,word)]=c
        for word,c in ss.items():column[('S',name,word)]=c
    columns.append(column)
    if j%20==0:print('FULL_NORMALIZER_COLUMNS',j,'OF',len(Ds),flush=True)
keys=sorted(set().union(*(set(c) for c in columns)))
trace=np.array([[col.get(key,0) for col in columns] for key in keys],dtype=np.int64)
assert int(np.max(np.abs(trace)))*trace.shape[1]*50 < 2**63
tracekernel,tracerank=nullspace(trace)
independent_rows=nullspace(trace.T,only_pivots=True)
assert len(independent_rows)==tracerank
rref,pivots=sp.Matrix(trace[independent_rows,:].tolist()).rref()
assert len(pivots)==tracerank
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
assert C.shape[1]==tracekernel.shape[1]
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
        rr,ss=rs_detector.derivation(commutator)
        assert not rr and not ss
print('CHECKED_40_ACTUAL_SEVENFOLD_JOHNSON_BRACKETS',flush=True)
omega={}
for x,y in [('a','b'),('c','d'),('e','f')]:omega=add(omega,bracket(v[x],v[y]))
polys=[bracket(omega,bracket(v['d'],bracket(v['c'],bracket(omega,v['b'])))),
       bracket(v['d'],bracket(omega,bracket(v['c'],bracket(omega,v['b']))))]
for poly in polys:
    tensor={}
    for tail,c in poly.items():
        word='a'+tail
        for i in range(8):
            key=word[i:]+word[:i];tensor[key]=tensor.get(key,0)+c
    vector=[0]*105
    for word,c in tensor.items():
        for i,sign in word_contractions(word):vector[i]+=c*sign
    known.append(vector)
J=np.array(known,dtype=np.int64).T
assert nullspace(J)[1]==4
K=np.array([contractions(D) for D in Ds],dtype=np.int64).T
assert int(np.max(np.abs(K)))*K.shape[1]*int(np.max(np.abs(C)))<2**63
values=K@C
print('FULL_NORMALIZER_CONTRACTION_RANK_MOD101',nullspace(values)[1],flush=True)
print('JOINED_TWO_JOHNSON_RANK_MOD101',nullspace(np.column_stack((J[:,:2],values)))[1],flush=True)
from pathlib import Path
import pickle
with Path(__file__).with_suffix('.pickle').open('wb') as file:
    pickle.dump(dict(Ds=Ds,Dlabels=Dlabels,trace_kernel=C,contractions=K,values=values,known=J,trace_rank=tracerank),file)
print('SAVED_EXACT_DATA',flush=True)
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'),flush=True)
raise SystemExit(0)
candidates=[]
for j in range(C.shape[1]):
    if nullspace(np.column_stack((J,values[:,j])))[1]==5:
        candidates.append((len(np.flatnonzero(C[:,j])),j))
assert candidates
_,chosen=min(candidates)
joined=np.column_stack((J,values[:,chosen]))
rows=[]
for i in range(105):
    if nullspace(joined[rows+[i],:])[1]>len(rows):rows.append(i)
    if len(rows)==5:break
minor=[[int(x) for x in joined[i,:]] for i in rows]
def det_int(mat):
    a=[list(r) for r in mat];sgn=1;old=1
    for k in range(len(a)-1):
        pivot=next(i for i in range(k,len(a)) if a[i][k])
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sgn=-sgn
        entry=a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                value=entry*a[i][j]-a[i][k]*a[k][j]
                assert value%old==0;a[i][j]=value//old
            a[i][k]=0
        old=entry
    return sgn*a[-1][-1]
determinant=det_int(minor)
assert determinant
print('EXACT_SUCCESSFUL_TRACE_KERNEL_LIFTS',C.shape[1],'OF133')
print('EXACT_SELECTED_KERNEL_INDEX',chosen)
print('EXACT_SELECTED_BASIS_COEFFICIENTS',[(Dlabels[i],int(C[i,chosen])) for i in np.flatnonzero(C[:,chosen])])
print('CONTRACTION_MINOR_ROWS',rows)
print('CONTRACTION_MINOR_ENTRIES',minor)
print('CONTRACTION_MINOR_DETERMINANT',determinant)
print('PASS: one explicit rational special derivation is tangent to a,b and satisfies all mixed ES7 equations, yet its invariant contraction vector lies outside the span of the two specified Johnson brackets and two specified proper-filling spiders.')
print('SCOPE: this is an exact limitation of these linear equations. The derivation has not been proved to lie in the universal arithmetic image or to normalize the full Johnson image. No arithmetic subgroup or nonzero actual q6 value is asserted.')
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
