#!/usr/bin/env python3
"""Integral certificates for the regraded divided-power bar disk closure."""
from math import comb
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import json,time
started=time.perf_counter();checks=0

@lru_cache(None)
def basis(m,n):
    if n==0:return ((m,),)
    if m<n:return ()
    return tuple((a,)+v for a in range(m-n+1) for v in positive(m-a,n))

@lru_cache(None)
def positive(m,n):
    if n==0:return ((),) if m==0 else ()
    return tuple((a,)+v for a in range(1,m-n+2) for v in positive(m-a,n-1))

def clean(x):return {a:c for a,c in x.items() if c}
def add(*terms):
    out=defaultdict(int)
    for c,v in terms:
        for a,b in v.items():out[a]+=c*b
    return clean(out)
def differential(a):
    if len(a)==1:return {}
    out=defaultdict(int)
    out[(a[0]+a[1],)+a[2:]]+=comb(a[0]+a[1],a[0])
    for i in range(1,len(a)-1):
        out[a[:i]+(a[i]+a[i+1],)+a[i+2:]]+=(-1)**i*comb(a[i]+a[i+1],a[i])
    return clean(out)
def contraction(a):return {(0,)+a:1} if a[0]>0 else {}
def apply(f,v):return add(*[(c,f(a)) for a,c in v.items()])

@lru_cache(None)
def shuffle(u,v):
    if not u:return {v:1}
    if not v:return {u:1}
    out=defaultdict(int)
    for w,c in shuffle(u[1:],v).items():out[(u[0],)+w]+=c
    for w,c in shuffle(u,v[1:]).items():out[(v[0],)+w]+=(-1)**len(u)*c
    return clean(out)
def multiply(a,b):
    c=comb(a[0]+b[0],a[0])
    return {(a[0]+b[0],)+w:c*z for w,z in shuffle(a[1:],b[1:]).items()}
def product_vec(u,v):return add(*[(a*b,multiply(x,y)) for x,a in u.items() for y,b in v.items()])

matrices={}
for m in range(1,9):
    matrices[m]={}
    for n in range(m+1):
        B=basis(m,n)
        assert len(B)==comb(m,n);checks+=1
        for a in B:
            assert not apply(differential,differential(a));checks+=1
            assert add((1,apply(differential,contraction(a))),(1,apply(contraction,differential(a))))=={a:1};checks+=1
        if n:
            target=basis(m,n-1)
            matrices[m][n]={'source_basis':B,'target_basis':target,
                            'differential':[[differential(a).get(b,0) for a in B] for b in target]}

by_arity={m:sum((list(basis(m,n)) for n in range(m+1)),[]) for m in range(1,7)}
for a in range(1,7):
 for b in range(1,7-a):
  for x in by_arity[a]:
   for y in by_arity[b]:
    n=len(x)-1
    lhs=apply(differential,multiply(x,y))
    rhs=add((1,product_vec(differential(x),{y:1})),((-1)**n,product_vec({x:1},differential(y))))
    assert lhs==rhs;checks+=1
    assert multiply(x,y)=={z:(-1)**(n*(len(y)-1))*c for z,c in multiply(y,x).items()};checks+=1

divided=[]
for m in range(1,5):
 for x in by_arity[m]:
    square=multiply(x,x)
    if (len(x)-1)%2:
        assert not square;checks+=1
    else:
        assert all(c%2==0 for c in square.values());checks+=1
        g={z:c//2 for z,c in square.items()}
        assert apply(differential,g)==product_vec({x:1},differential(x));checks+=1
        divided.append({'input':x,'gamma2':[(z,c) for z,c in g.items()]})

x=(0,1);y=(1,);z=(0,2);v=(0,1,1)
assert differential(x)=={y:1};checks+=1
assert differential(z)=={(2,):1};checks+=1
assert differential(v)=={(1,1):1,(0,2):-2};checks+=1
out={'statement':'Integral regraded bar closure; explicit contraction and low products',
     'checks':checks,'matrices':matrices,'divided_square_checks':divided,
     'arity2':{'x':x,'y':y,'z':z,'v':v,'dx':list(differential(x).items()),
               'dz':list(differential(z).items()),'dv':list(differential(v).items())},
     'elapsed_seconds':time.perf_counter()-started}
Path('SA08_work/logs/D_bar_closure_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks':checks,'elapsed_seconds':out['elapsed_seconds']}))
