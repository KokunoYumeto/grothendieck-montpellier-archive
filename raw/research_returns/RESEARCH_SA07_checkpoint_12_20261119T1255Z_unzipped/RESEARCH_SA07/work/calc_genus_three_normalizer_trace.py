"""Exact exploratory ES trace of brackets with degree-one geometric derivations.

No arithmetic assertion is made until the source map to the completed
geometric Johnson image has been proved in the written audit.
"""
from pathlib import Path
from itertools import combinations
from time import perf_counter
from fractions import Fraction
started=perf_counter()
source=Path('/workspace/scratch/f6dbb6638732/output/RESEARCH_SA07/code/check_genus_two_tangent_space.py').read_text()
ns={};exec(source[:source.index('six, eight =')],ns)
add,scale,bracket,multiply=[ns[x] for x in ['add','scale','bracket','multiply']]
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
pr,pc=ns['pivot_minor'](matrix,101)
print('RANK_MOD101:',len(pr))
print('SELECTED_ROWS:',[keys[i] for i in pr])
print('SELECTED_COLUMNS:',pc)
minor=[[matrix[i][j] for j in pc] for i in pr]
print('MINOR_ENTRIES:',minor)
print('MINOR_DET_MOD101:',ns['determinant_mod'](minor,101))
if len(pr)<6:
    import sympy as sp
    print('EXACT_KERNEL:',[list(v) for v in sp.Matrix(matrix).nullspace()])
print('LIMIT: source comparison with completed geometric monodromy is a separate unclosed gate.')
print('ACTUAL_WALL_SECONDS:',format(perf_counter()-started,'.9f'))
