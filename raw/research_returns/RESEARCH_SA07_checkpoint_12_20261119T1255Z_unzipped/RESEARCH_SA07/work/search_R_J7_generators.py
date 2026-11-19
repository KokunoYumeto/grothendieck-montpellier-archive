#!/usr/bin/env python3
"""Work-only search for six actual J7 H-isotypical detector vectors."""
from itertools import combinations
from functools import lru_cache
from random import Random
from time import perf_counter
import json
from pathlib import Path

G=5;letters=tuple(range(2*G));prime=1009;started=perf_counter()

def pair(x,y):
    return (1 if x%2==0 else -1) if x//2==y//2 and x!=y else 0

def addterm(out,w,c):
    if c:
        out[w]=out.get(w,0)+c
        if not out[w]:del out[w]

def johnson(t):
    D=[{} for _ in letters]
    for i,x in enumerate(t):
        y,z=t[(i+1)%3],t[(i+2)%3]
        c=pair(x^1,x)
        addterm(D[x^1],(y,z),c);addterm(D[x^1],(z,y),-c)
    return D

def act(D,P,out,sign):
    for word,c in P.items():
        for i,x in enumerate(word):
            for tail,d in D[x].items():
                addterm(out,word[:i]+tail+word[i+1:],sign*c*d)

def bracket(D,E):
    out=[]
    for x in letters:
        Q={};act(D,E[x],Q,1);act(E,D[x],Q,-1);out.append(Q)
    return out

def matchings(items):
    if not items:yield ();return
    a=items[0]
    for j in range(1,len(items)):
        for rest in matchings(items[1:j]+items[j+1:]):yield ((a,items[j]),)+rest

chords=list(matchings(tuple(range(8))));index={m:i for i,m in enumerate(chords)}

@lru_cache(maxsize=300000)
def contractions(word):
    def visit(items,pairs,sgn):
        if not items:
            yield index[tuple(pairs)],sgn;return
        i=items[0]
        for k in range(1,len(items)):
            j=items[k];c=pair(word[i],word[j])
            if c:yield from visit(items[1:k]+items[k+1:],pairs+[(i,j)],sgn*c)
    return tuple(visit(tuple(range(8)),[],1))

def detector(D):
    out=[0]*105
    for x in letters:
        first=x^1;sign=-1 if x%2==0 else 1
        for tail,c in D[x].items():
            if tail[-1]!=0:continue
            word=(first,)+tail[:-1]
            for i,v in contractions(word):out[i]+=sign*c*v
    return out

rterms=[(-2,((0,1),(2,4),(3,6),(5,7))),
 (2,((0,1),(2,5),(3,6),(4,7))),
 (2,((0,1),(2,5),(3,7),(4,6))),
 (2,((0,1),(2,6),(3,5),(4,7))),
 (1,((0,2),(1,5),(3,6),(4,7)))]

basis=[];witness=[]
def independent(row):
    v=[x%prime for x in row]
    for pivot,u in basis:
        c=v[pivot]
        if c:v=[(a-c*b)%prime for a,b in zip(v,u)]
    nz=next((i for i,c in enumerate(v) if c),None)
    if nz is None:return False
    inv=pow(v[nz],-1,prime);v=[x*inv%prime for x in v]
    basis.append((nz,v));return True

rng=Random(20261119)
for trial in range(2000):
    # Ten matched input pairs and one surviving output a.
    pairs=[rng.randrange(G) for _ in range(10)]
    pool=[0]+[x for h in pairs for x in (2*h,2*h+1)]
    rng.shuffle(pool)
    triples=[tuple(pool[i:i+3]) for i in range(0,21,3)]
    if any(len(set(t))<3 for t in triples):continue
    D=johnson(triples[0])
    for t in triples[1:]:
        D=bracket(D,johnson(t))
        if not any(D):break
    if not any(D):continue
    K=detector(D)
    if not any(K):continue
    rv=sum(c*K[index[m]] for c,m in rterms)
    assert rv==0,('R_FAILURE',trial,triples,rv)
    if independent(K):
        witness.append(dict(trial=trial,triples=triples,detector=K,terms=sum(map(len,D)),R=rv))
        print('INDEPENDENT',len(witness),'TRIAL',trial,'TERMS',sum(map(len,D)),flush=True)
        print('TRIPLES',triples,flush=True)
        print('DETECTOR',K,flush=True)
        if len(witness)==6:break
else:print('EXHAUSTED',flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(witness,indent=2)+'\n')
print('RANK',len(witness),'ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'),flush=True)
