#!/usr/bin/env python3
"""Independent six-letter word realization of the twelve Levi inputs.

Checks the scalar diagram evaluator at s=2 without using its loop or
gluing implementations. No mixed-matrix completeness claim is made.
"""
from datetime import datetime, timezone
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
from time import perf_counter
import json
import pickle

HERE=Path(__file__).resolve().parent
WORK=HERE.parent
START=datetime.now(timezone.utc).isoformat(); t0=perf_counter()
INPUT=WORK/'calc_levi_single_line_input.pickle'
EXPECTED=WORK/'calc_levi_scalar_rows.pickle'
source=pickle.loads(INPUT.read_bytes())
expected=pickle.loads(EXPECTED.read_bytes())
alphabet='abcdef'; out=[]

def report(*args):
    line=' '.join(map(str,args)); out.append(line); print(line,flush=True)

def add(a,b,scale=1):
    result=dict(a)
    for word,c in b.items():
        result[word]=result.get(word,0)+scale*c
        if not result[word]:del result[word]
    return result

def mul(a,b):
    result={}
    for x,c in a.items():
        for y,d in b.items():result[x+y]=result.get(x+y,0)+c*d
    return {w:c for w,c in result.items() if c}

def bracket(a,b):return add(mul(a,b),mul(b,a),-1)

def pair(x,y):
    i,j=alphabet.index(x),alphabet.index(y)
    return (1 if i%2==0 else -1) if i//2==j//2 and i!=j else 0

@lru_cache(None)
def expand(key):
    edge_labels=sorted({x for x in key if x>=0})
    positions=[tuple(i for i,x in enumerate(key) if x==label) for label in edge_labels]
    result={}
    # Each edge is the literal cd-dc+ef-fe, with four choices.
    for terms in product((('c','d',1),('d','c',-1),('e','f',1),('f','e',-1)),repeat=len(positions)):
        letters=[alphabet[-x-1] if x<0 else None for x in key]; coefficient=1
        for (i,j),(x,y,c) in zip(positions,terms):
            letters[i],letters[j]=x,y;coefficient*=c
        word=''.join(letters);result[word]=result.get(word,0)+coefficient
    return {w:c for w,c in result.items() if c}

def to_derivation(T):
    D={x:{} for x in alphabet}
    for word,c in T.items():
        i=alphabet.index(word[0]);image=alphabet[i^1]
        sign=1 if i%2==0 else -1
        D[image]=add(D[image],{word[1:]:sign*c})
    reconstructed={}
    for i in range(0,6,2):
        x,y=alphabet[i:i+2]
        reconstructed=add(reconstructed,{x+w:c for w,c in D[y].items()})
        reconstructed=add(reconstructed,{y+w:-c for w,c in D[x].items()})
    assert reconstructed==T
    return D

def act(D,poly):
    result={}
    for word,c in poly.items():
        for i,x in enumerate(word):
            for replacement,d in D[x].items():
                key=word[:i]+replacement+word[i+1:]
                result[key]=result.get(key,0)+c*d
    return {w:c for w,c in result.items() if c}

def derbracket(D,E):return {x:add(act(D,E[x]),act(E,D[x]),-1) for x in alphabet}

v={x:{x:1} for x in alphabet}
def delta(triple):
    a,b,c=triple
    return {x:add(add({w:pair(x,a)*n for w,n in bracket(v[b],v[c]).items()},
                          {w:pair(x,b)*n for w,n in bracket(v[c],v[a]).items()}),
                          {w:pair(x,c)*n for w,n in bracket(v[a],v[b]).items()}) for x in alphabet}

def matchings(items):
    if not items:yield ();return
    a=items[0]
    for j in range(1,len(items)):
        for rest in matchings(items[1:j]+items[j+1:]):yield ((a,items[j]),)+rest

all_matches=list(matchings(tuple(range(8))))
detector=[all_matches[i] for i in (0,1,2,7,13)]
def K5(T):
    values=[]
    for pairs in detector:
        total=0
        for word,c in T.items():
            value=c
            for i,j in pairs:
                value*=pair(word[i],word[j])
                if not value:break
            total+=value
        values.append(total)
    return values

# Exact MSS2026 p.11, independently applied to expanded length-nine words.
rterms=((-2,((0,1),(2,4),(3,6),(5,7))),
         ( 2,((0,1),(2,5),(3,6),(4,7))),
         ( 2,((0,1),(2,5),(3,7),(4,6))),
         ( 2,((0,1),(2,6),(3,5),(4,7))),
         ( 1,((0,2),(1,5),(3,6),(4,7))))
@lru_cache(maxsize=300000)
def rword(word):
    result=0
    for coefficient,pairs in rterms:
        value=coefficient
        for i,j in pairs:
            value*=pair(word[i],word[j])
            if not value:break
        result+=value
    return result

def Rcoordinate(D,output):
    total=0
    for i in range(0,6,2):
        for first,image,sign in ((alphabet[i],D[alphabet[i+1]],1),
                                  (alphabet[i+1],D[alphabet[i]],-1)):
            for tail,c in image.items():
                if tail[-1]==output:total+=sign*c*rword(first+tail)
    return total

tests=(('abx','abc','c'),('axy','acd','a'),('xyu','cde','e'))
deltas={name:delta(triple) for name,triple,_ in tests}
s=expected['s']; r_names=expected['names']
all_K=[];all_R=[]
for j,(formal,label) in enumerate(zip(source['inputs'],source['labels'])):
    T={}
    for key,c in formal.items():T=add(T,expand(key),c)
    D=to_derivation(T)
    # Specialness checked literally on the three-generator symplectic sum.
    omega={}
    for i in range(0,6,2):omega=add(omega,bracket(v[alphabet[i]],v[alphabet[i+1]]))
    assert not act(D,omega)
    k=K5(T)
    want_k=[int(expected['K'][i,j].subs(s,2)) for i in range(5)]
    assert k==want_k,('K',j,k,want_k)
    rr=[]
    for name,_,output in tests:
        value=Rcoordinate(derbracket(D,deltas[name]),output)
        index=r_names.index('R_'+name)
        want=int(expected['rows'][index][j].subs(s,2))
        assert value==want,('R',j,name,value,want)
        rr.append(value)
    all_K.append(k);all_R.append(rr)
    report('INPUT',j,label,'WORDS',len(T),'K5',k,'R3',rr,'PASS')
elapsed=perf_counter()-t0
report('PASS: all60 K coordinates and36 R coordinates agree at s=2')
report('ACTUAL_WALL_SECONDS',f'{elapsed:.9f}')
report('SCOPE: concrete signs and composition only; no mixed-kernel completeness claim')
(HERE/'check_levi_scalar_word_realization.out').write_text('\n'.join(out)+'\n')
(HERE/'check_levi_scalar_word_realization.json').write_text(json.dumps(dict(
    start_utc=START,wall_seconds=elapsed,exit_code=0,
    input_sha256=sha256(INPUT.read_bytes()).hexdigest(),
    scalar_output_sha256=sha256(EXPECTED.read_bytes()).hexdigest(),
    scalar_program_sha256=sha256((WORK/'calc_levi_scalar_rows.py').read_bytes()).hexdigest(),
    parameter_s=2,alphabet=alphabet,K_columns=all_K,R_columns=all_R),indent=2)+'\n')
