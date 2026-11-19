"""Exploratory exact CM-weight degree-six tangent-space calculation."""
from functools import lru_cache
from itertools import product
from time import perf_counter
import json
import sympy as s

started = perf_counter()


def add(a,b):
    c=dict(a)
    for w,k in b.items():
        c[w]=c.get(w,0)+k
        if not c[w]: del c[w]
    return c


def scale(a,k): return {w:k*c for w,c in a.items() if k*c}


def mul(a,b):
    c={}
    for u,j in a.items():
        for v,k in b.items(): c[u+v]=c.get(u+v,0)+j*k
    return {w:k for w,k in c.items() if k}


def br(a,b): return add(mul(a,b),scale(mul(b,a),-1))


def lyn(w): return all(w<w[i:] for i in range(1,len(w)))


@lru_cache(None)
def std(w):
    if len(w)==1:return {w:1}
    i=next(i for i in range(1,len(w)) if lyn(w[i:]))
    return br(std(w[:i]),std(w[i:]))


def lw(n):return [''.join(w) for w in product('abcd',repeat=n) if lyn(''.join(w))]


L6=lw(6); L8=lw(8)
B={i:[w for w in L6 if tuple(w.count(ch) for ch in 'abcd')==(i,i,3-i,3-i)] for i in range(4)}
print('Balanced L6 dimensions:',{i:len(x) for i,x in B.items()},flush=True)
letters={ch:{ch:1} for ch in 'abcd'}
all_kernels=[]
for n in range(5):
    rows=[w for w in L8 if tuple(w.count(ch) for ch in 'abcd')==(n,n,4-n,4-n)]
    labels=[]; images=[]; cols=[]
    for ch in 'abcd':
        degree=n-1 if ch in 'ab' else n
        for w in B.get(degree,[]):
            image=br(std(w),letters[ch])
            if ch=='a':out=br(image,letters['b'])
            elif ch=='b':out=br(letters['a'],image)
            elif ch=='c':out=br(image,letters['d'])
            else:out=br(letters['c'],image)
            labels.append((ch,w));images.append(image);cols.append([out.get(v,0) for v in rows])
    M=s.Matrix(len(rows),len(cols),lambda i,j:cols[j][i])
    kernel=M.nullspace()
    print('BLOCK',n,'shape',M.shape,'nullity',len(kernel),'wall',perf_counter()-started,flush=True)
    for number,vector in enumerate(kernel):
        result={ch:{} for ch in 'abcd'}
        coefficients=[]
        for coefficient,(ch,w),image in zip(vector,labels,images):
            if coefficient:
                result[ch]=add(result[ch],scale(image,coefficient))
                coefficients.append((ch,w,str(coefficient)))
        assert not add(add(br(result['a'],letters['b']),br(letters['a'],result['b'])),
                       add(br(result['c'],letters['d']),br(letters['c'],result['d'])))
        all_kernels.append((n,result,coefficients))
        print('BASIS',n,number,coefficients,flush=True)


@lru_cache(None)
def normal_word(w):
    i=w.find('dc')
    if i<0:return {w:1}
    return add(add(normal_word(w[:i]+'ab'+w[i+2:]),scale(normal_word(w[:i]+'ba'+w[i+2:]),-1)),
               normal_word(w[:i]+'cd'+w[i+2:]))


def normal(poly):
    out={}
    for w,c in poly.items():out=add(out,scale(normal_word(w),c))
    return out


closed=[]
for index,(n,result,coefficients) in enumerate(all_kernels):
    out={ch:normal(poly) for ch,poly in result.items()}
    closed.append(out)
    print('CLOSED_IMAGE',index,'block',n,'sizes',{ch:len(poly) for ch,poly in out.items()},flush=True)
print('TOTAL_NULLITY',len(all_kernels),flush=True)
print('ACTUAL_WALL_SECONDS:',format(perf_counter()-started,'.9f'),flush=True)
