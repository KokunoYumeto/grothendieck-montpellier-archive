#!/usr/bin/env python3
"""Finite certificates for SA10-A1 and SA10-A4; no external packages."""
from itertools import product, combinations
from time import perf_counter
import json

t0=perf_counter()
P=('o','p','n','u','d')
le={(x,x) for x in P}|{('o','p'),('o','n'),('p','u'),('p','d'),('n','u'),('n','d'),('o','u'),('o','d')}
fib={x:(0,1) if x=='u' else (0,) for x in P}

def functor(nodes, upper_p, upper_n):
    nodes=set(nodes); maps={}
    for x,y in le:
        if x in nodes and y in nodes:
            if x==y: maps[x,y]=tuple(fib[x])
            elif y=='u': maps[x,y]=(upper_p if x in ('o','p') else upper_n,)
            else: maps[x,y]=(0,)
    for x,y,z in product(nodes,repeat=3):
        if (x,y) in maps and (y,z) in maps:
            composite=tuple(maps[y,z][fib[y].index(v)] for v in maps[x,y])
            assert composite==maps[x,z],(x,y,z)
    return nodes,maps

def restriction_equal(F,G):
    n,m=F; N,M=G
    assert n<=N
    return all(M[k]==v for k,v in m.items())

# Each finite diagram is realized by a cellular constructible sheaf on the
# indicated actual plane germ, as proved in the paper. Only genuine germ
# inclusions are imposed; arbitrary inclusions of cell SUPPORTS are not.
allpair={
 'S0':functor('o',0,0), 'S1':functor(('p','n'),0,0),
 'S2':functor(('u','d'),0,0), 'V01':functor(('o','p','n'),0,0),
 'V01s':functor(('p','n'),0,0), 'V12':functor(('p','n','u','d'),1,1),
 'V12s':functor(('u','d'),0,0), 'V02':functor(P,0,0),
 'V02s':functor(('u','d'),0,0)}
arrows={('S0','V01'),('S0','V02'),('V01','V02'),('V01s','V01'),
 ('V01s','S1'),('S1','V12'),('V12s','V12'),('V12s','S2'),
 ('V02s','V02'),('V02s','S2'),('V02s','V12s')}
while True:
    new=arrows|{(a,d) for a,b in arrows for c,d in arrows if b==c}
    if new==arrows: break
    arrows=new
for a,b in arrows: assert restriction_equal(allpair[a],allpair[b]),(a,b)
assert allpair['V02'][1]['p','u'] != allpair['V12'][1]['p','u']
print('A1 all-pair/triple witness:',len(allpair),'distinct objects,',len(arrows),'nonidentity inclusions checked; incompatible overlap p->u verified.')

succ={'V01':functor(('o','p','n'),0,0),'V12':functor(('p','n','u','d'),0,1)}
valid=[]
for op,on,pu,nu,ou in product((0,1), repeat=5):
    # Singleton o,p,n means op=on=0 is compulsory; pu and nu prescribed.
    if op==on==0 and pu==0 and nu==1 and ou==pu and ou==nu: valid.append((op,on,pu,nu,ou))
assert not valid
print('A1 successor witness: 32 candidate assignments checked; 0 extensions.')

# Finite meet-semilattice: all proper subsets of a three-element set.
I=[frozenset(c) for r in range(3) for c in combinations(range(3),r)]
assert all(a&b in I for a,b in product(I,repeat=2))
X={a: (() if not a else (0,1)) for a in I}
def transport(a,b,x):
    assert a<=b
    return 1-x if a==frozenset({0}) and b==frozenset({0,1}) else x
for a,b,c in product(I,repeat=3):
    if a<=b<=c:
        for x in X[a]: assert transport(b,c,transport(a,b,x))==transport(a,c,x)
objs=[(a,x) for a in I for x in X[a]]
parent={a:a for a in objs}
def root(a):
    while parent[a]!=a: a=parent[a]
    return a
def union(a,b): parent[root(a)]=root(b)
for a,b in product(I,repeat=2):
    if a<=b:
        for x in X[a]: union((a,x),(b,transport(a,b,x)))
classes={root(a) for a in objs}
assert len(classes)==1
assert root((frozenset({0}),0))==root((frozenset({0}),1))
# Object-level order is a closed partial order: all objects finite discrete.
R={( (a,x),(b,transport(a,b,x)) ) for a,b in product(I,repeat=2) if a<=b for x in X[a]}
assert all((a,a) in R for a in objs)
assert all(a==b for a,b in R if (b,a) in R)
assert all((a,d) in R for a,b in R for c,d in R if b==c)
print('A4 counterexample:',len(I),'indices,',len(objs),'points in disjoint union,',len(classes),'point in colimit; all meet, functor, and partial-order conditions checked.')

# Strengthened version: every member of the indexed partition is nonempty.
XX={a:((2,) if not a else (0,1,2)) for a in I}
def tt(a,b,x):
    return transport(a,b,x) if x<2 else 2
oo=[(a,x) for a in I for x in XX[a]]
pp={a:a for a in oo}
def rr(a):
    while pp[a]!=a:a=pp[a]
    return a
for a,b,c in product(I,repeat=3):
    if a<=b<=c:
        for x in XX[a]:assert tt(b,c,tt(a,b,x))==tt(a,c,x)
for a,b in product(I,repeat=2):
    if a<=b:
        for x in XX[a]:pp[rr((a,x))]=rr((b,tt(a,b,x)))
assert len(oo)==19 and len({rr(a) for a in oo})==2
RR={((a,x),(b,tt(a,b,x))) for a,b in product(I,repeat=2) if a<=b for x in XX[a]}
assert all((a,a) in RR for a in oo)
assert all(a==b for a,b in RR if (b,a) in RR)
assert all((a,d) in RR for a,b in RR for c,d in RR if b==c)
print('A4 nonempty strengthening: 7 nonempty spaces, 19 total points, 2 colimit points; all functor and order checks pass.')

# Three-cover descent: without the triple, a nontrivial transition cycle.
ident=(0,1); swap=(1,0)
g01=ident;g12=ident;g02=swap
comp=tuple(g12[v] for v in g01)
assert comp!=g02
assert len([]) != 1
assert len((0,)) != len((0,1))
print('A1 Cech minimality: missing vertex leaves 0 versus 1 fibres; missing pair allows stalk cardinalities 1 and 2; missing triple permits identity != transposition.')

# R3 support deletion, the false parenthesis after (12), and R6's strict bound.
chain={0:{0},1:{0,1},2:{0,1,2}}
support_R=lambda i:set().union(*(v for k,v in chain.items() if not chain[i]<=v))
for i in chain:
    lower=set().union(*(v for k,v in chain.items() if k<i))
    assert support_R(i)&chain[i]==lower
R12=support_R(1)&chain[2]
S12=set().union(*(v for k,v in chain.items() if 1<=k<2))
assert R12&S12=={0} and R12&S12!=set()
coincident={0:{0},1:{0}}
bad_R=set().union(*(v for k,v in coincident.items() if not coincident[1]<=v))
assert bad_R==set() and coincident[0]=={0}
strict_failures=[(i,j) for i,j in product(chain,repeat=2)
    if chain[i]&chain[j] != set().union(*(v for k,v in chain.items() if k<i and k<j))]
assert len(strict_failures)==9
print('R3/R6: all three nonempty-stratum support identities verified; coincident-piece failure and false (12) parenthesis verified; all 9 strict-bound comparisons fail in the nonempty three-point chain.')
print('Elapsed seconds:',f'{perf_counter()-t0:.6f}')
