#!/usr/bin/env python3
"""Exact new genus-three tangent block and geometric-normalizer trace certificate.

Inputs: six ordered symplectic generators; balanced degree6 conjugators;
all twenty degree1 wedge derivations; contraction K12 and cyclic words.
The lower-support tangent blocks are exactly those certified in F.3.22.
No external package is needed; all polynomials have integer coefficients.
"""
from functools import lru_cache
from itertools import combinations
from time import perf_counter
started=perf_counter()
def add(a, b):
    out = dict(a)
    for word, value in b.items():
        out[word] = out.get(word, 0) + value
        if not out[word]:
            del out[word]
    return out


def scale(a, value):
    return {word: value * coefficient for word, coefficient in a.items()
            if value * coefficient}


def multiply(a, b):
    out = {}
    for first, left in a.items():
        for second, right in b.items():
            word = first + second
            out[word] = out.get(word, 0) + left * right
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def bracket(a, b):
    return add(multiply(a, b), scale(multiply(b, a), -1))


def lyndon(word):
    return all(word < word[index:] for index in range(1, len(word)))


@lru_cache(None)
def standard(word):
    if len(word) == 1:
        return {word: 1}
    split = next(index for index in range(1, len(word)) if lyndon(word[index:]))
    out = bracket(standard(word[:split]), standard(word[split:]))
    assert min(out) == word and out[word] == 1
    return out


def pivot_minor(matrix, modulus):
    work = [[entry % modulus for entry in row] for row in matrix]
    origins = list(range(len(work)))
    selected_rows, selected_columns = [], []
    rank = 0
    for column in range(len(work[0])):
        pivot = next((index for index in range(rank, len(work)) if work[index][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        origins[rank], origins[pivot] = origins[pivot], origins[rank]
        selected_rows.append(origins[rank])
        selected_columns.append(column)
        inverse = pow(work[rank][column], -1, modulus)
        work[rank] = [entry * inverse % modulus for entry in work[rank]]
        for index in range(rank + 1, len(work)):
            factor = work[index][column]
            if factor:
                work[index] = [(left - factor * right) % modulus
                               for left, right in zip(work[index], work[rank])]
        rank += 1
        if rank == len(work):
            break
    return selected_rows, selected_columns


def determinant_mod(matrix, modulus):
    work = [[entry % modulus for entry in row] for row in matrix]
    determinant = 1
    for column in range(len(work)):
        pivot = next((index for index in range(column, len(work)) if work[index][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        entry = work[column][column]
        determinant = determinant * entry % modulus
        inverse = pow(entry, -1, modulus)
        for index in range(column + 1, len(work)):
            factor = work[index][column] * inverse % modulus
            for j in range(column + 1, len(work)):
                work[index][j] = (work[index][j] - factor * work[column][j]) % modulus
    return determinant % modulus


alphabet='abcdef'

def words(degrees,prefix=''):
    if not any(degrees):
        yield prefix
    else:
        for i,n in enumerate(degrees):
            if n:
                ds=list(degrees);ds[i]-=1
                yield from words(tuple(ds),prefix+alphabet[i])

def basis(degrees):
    return [w for w in words(degrees) if lyndon(w)]

n=(2,1,1)
degrees=tuple(x for count in n for x in (count,count))
rows=basis(degrees)
letters={x:{x:1} for x in alphabet}
labels=[];polys=[]
for i,x in enumerate(alphabet):
    deg=list(n);deg[i//2]-=1
    ds=tuple(v for v in deg for _ in range(2))
    for word in basis(ds):
        image=bracket(standard(word),letters[x])
        y=alphabet[i^1]
        polynomial=bracket(image,letters[y]) if i%2==0 else bracket(letters[y],image)
        labels.append((x,word));polys.append(polynomial)
matrix=[[p.get(w,0) for p in polys] for w in rows]
print('BLOCK',n,'SHAPE',len(rows),len(labels))
pr,pc=pivot_minor(matrix,101)
det=determinant_mod([[matrix[i][j] for j in pc] for i in pr],101)
print('RANK_MOD101',len(pr),'NULLITY_UPPER_OVER_Q',len(labels)-len(pr),'MINOR',det)
z=[bracket(letters[alphabet[2*i]],letters[alphabet[2*i+1]]) for i in range(3)]
x,y,z3=z
A=[add(bracket(y,bracket(x,z3)),bracket(z3,bracket(x,y))),
   scale(bracket(x,bracket(x,z3)),-1),scale(bracket(x,bracket(x,y)),-1)]
special={}
for ai,zi in zip(A,z): special=add(special,bracket(ai,zi))
assert not special
images={letter:bracket(A[i//2],letters[letter]) for i,letter in enumerate(alphabet)}
assert all(images.values())
print('EXACT_KERNEL: A1=[z2,[z1,z3]]+[z3,[z1,z2]], A2=-[z1,[z1,z3]], A3=-[z1,[z1,z2]]; both generators of each handle share Ai.')
assert len(pr)==359 and len(labels)==360 and det
print('PASS: the new block has rational nullity exactly1; three permutations and the three two-handle blocks give total dimension6.')

# A concrete map out of the proper-surface Lie quotient detects a two-handle
# tangent derivation that vanished after filling in genus2.
v={c:{c:1} for c in 'xyz'}
sub={'a':v['x'],'b':v['y'],'c':v['x'],'d':v['z'],
     'e':v['x'],'f':scale(add(v['y'],v['z']),-1)}
zs=[bracket(sub[alphabet[2*i]],sub[alphabet[2*i+1]]) for i in range(3)]
assert not add(add(zs[0],zs[1]),zs[2])
detect=bracket(bracket(zs[1],bracket(zs[0],zs[1])),sub['a'])
assert detect
print('PROPER_QUOTIENT_DETECTOR: a,c,e map to x; b maps to y; d maps to z; f maps to -y-z. The surface relation maps to0.')
print('D12(a) NONZERO_WORD',min(detect),'COEFFICIENT',detect[min(detect)])
print('LIMIT: no nonzero q6 value, universal-image membership, or arithmetic normalizer is inferred.')

alphabet='abcdef';v={x:{x:1} for x in alphabet}
z=[bracket(v[alphabet[2*i]],v[alphabet[2*i+1]]) for i in range(3)]

def pair(x,y):
    i,j=alphabet.index(x),alphabet.index(y)
    return (1 if i%2==0 else -1) if i//2==j//2 and i!=j else 0

def tangent(aa):
    return {letter:bracket(aa[i//2],v[letter]) for i,letter in enumerate(alphabet)}

Ds=[];labels=[]
for i,j in combinations(range(3),2):
    aa=[{}, {}, {}]
    c=bracket(z[i],z[j])
    aa[i]=bracket(z[j],c);aa[j]=scale(bracket(z[i],c),-1)
    Ds.append(tangent(aa));labels.append('pair'+str(i+1)+str(j+1))
for i in range(3):
    j,k=[x for x in range(3) if x!=i]
    aa=[{}, {}, {}]
    aa[i]=add(bracket(z[j],bracket(z[i],z[k])),bracket(z[k],bracket(z[i],z[j])))
    aa[j]=scale(bracket(z[i],bracket(z[i],z[k])),-1)
    aa[k]=scale(bracket(z[i],bracket(z[i],z[j])),-1)
    Ds.append(tangent(aa));labels.append('triple_repeated'+str(i+1))

def act(D,poly):
    out={}
    for word,c in poly.items():
        for i,x in enumerate(word):
            for middle,d in D[x].items():
                key=word[:i]+middle+word[i+1:]
                out[key]=out.get(key,0)+c*d
    return {w:c for w,c in out.items() if c}

def derivation_bracket(D,E):
    return {x:add(act(D,E[x]),scale(act(E,D[x]),-1)) for x in alphabet}

def ES(D):
    # H-dual tensor is sum x_i tensor D(y_i)-y_i tensor D(x_i).
    out={}
    for i in range(3):
        for first,tail,sgn in [(alphabet[2*i],D[alphabet[2*i+1]],1),
                               (alphabet[2*i+1],D[alphabet[2*i]],-1)]:
            for word,c in tail.items():
                val=sgn*c*pair(first,word[0])
                if val:
                    rest=word[1:]
                    key=min(rest[j:]+rest[:j] for j in range(len(rest)))
                    out[key]=out.get(key,0)+val
    return {w:c for w,c in out.items() if c}

columns=[{} for _ in Ds]
for triple in combinations(alphabet,3):
    a,b,c=triple
    delta={x:add(add(scale(bracket(v[b],v[c]),pair(x,a)),
                       scale(bracket(v[c],v[a]),pair(x,b))),
                    scale(bracket(v[a],v[b]),pair(x,c))) for x in alphabet}
    assert not add(add(act(delta,z[0]),act(delta,z[1])),act(delta,z[2]))
    for j,D in enumerate(Ds):
        result=ES(derivation_bracket(D,delta))
        for word,value in result.items():columns[j][(''.join(triple),word)]=value
keys=sorted(set().union(*(set(c) for c in columns)))
matrix=[[column.get(key,0) for column in columns] for key in keys]
print('INPUT: six complete genus3 balanced tangent basis derivations; twenty degree1 symplectic derivations; ES contraction K12 followed by cyclic coinvariants.')
print('COLUMNS:',labels)
print('SHAPE:',len(keys),len(Ds))
pr,pc=pivot_minor(matrix,101)
print('RANK_MOD101:',len(pr))
print('SELECTED_ROWS:',[keys[i] for i in pr])
print('SELECTED_COLUMNS:',pc)
minor=[[matrix[i][j] for j in pc] for i in pr]
print('MINOR_ENTRIES:',minor)
print('MINOR_DET_MOD101:',determinant_mod(minor,101))
assert len(pr)==4 and columns[3]==columns[4]==columns[5]
assert minor==[[-1,0,0,0],[0,-1,0,1],[0,0,1,-1],[-1,0,0,1]]
print('PASS: exact rank4 and kernel span(T2-T1,T3-T1); displayed integer minor has determinant1.')
print('PASS: handle permutations exchange T1,T2,T3, so every Sp-invariant linear functional annihilates this kernel.')
print('SCOPE: the geometric-normalizer/relative-completion comparison and actual q6 map are written proofs; no arithmetic subgroup is constructed by this program.')
print('ACTUAL_WALL_SECONDS:',format(perf_counter()-started,'.9f'))
