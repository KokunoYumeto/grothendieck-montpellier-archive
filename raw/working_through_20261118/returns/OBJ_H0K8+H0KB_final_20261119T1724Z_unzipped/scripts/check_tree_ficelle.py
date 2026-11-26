"""Finite-grid check of V's continuous finite-tree counterexample.

Order is computed from the original component-ficelle connectedness condition,
then compared with V1. This is a check of the classification/order formula on
a finite grid, not a certificate for density or the infinite G axioms.
"""
from itertools import combinations
main=set(range(13)); hair=set(range(13,18)); v=4; a=0; b=12; p=17
vertices=main|hair
edges={frozenset((i,i+1)) for i in range(12)}
edges|={frozenset((v,13))}|{frozenset((i,i+1)) for i in range(13,17)}
neighbors={x:{next(iter(e-{x})) for e in edges if x in e} for x in vertices}
def components(V):
 left=set(V);ans=[]
 while left:
  root=next(iter(left));left.remove(root);part={root};stack=[root]
  while stack:
   x=stack.pop()
   for y in neighbors[x]&left:
    left.remove(y);part.add(y);stack.append(y)
  ans.append(part)
 return ans
internal=sorted(vertices-{a,b})
cuts=[]
for mask in range(1,1<<len(internal)):
 C=frozenset(x for i,x in enumerate(internal) if mask>>i&1)
 parts=components(vertices-C)
 if len(parts)==2 and not any({a,b}<=part for part in parts):cuts.append(C)
def classification(C):
 M=C&main;H=C&hair
 if not M:return False
 if M!=set(range(min(M),max(M)+1)):return False
 if H and H!=set(range(min(H),p+1)):return False
 return v not in M or H==hair
assert all(classification(C) for C in cuts)
expected=[]
for l in range(1,12):
 for r in range(l,12):
  for start in [None,*range(13,18)]:
   C=frozenset(set(range(l,r+1))|(set() if start is None else set(range(start,p+1))))
   if classification(C):expected.append(C)
assert set(expected)==set(cuts)
A=frozenset({a});B=frozenset({b});L=[A,*cuts,B]
left_component={}
for D in cuts:
 left_component[D]=next(x for x in components(vertices-D) if a in x)|set(D)
def direct(C,D):
 if C==D:return False
 if C==A or D==B:return True
 if C==B or D==A or C&D:return False
 K=left_component[D]
 if not C<=K:return False
 parts=components(K-set(C))
 apart=next(x for x in parts if a in x)
 return not (apart&D) and all(part&D for part in parts if part is not apart)
def formula(C,D):
 if C==D:return False
 if C==A or D==B:return True
 if C==B or D==A:return False
 ch=bool(C&hair);dh=bool(D&hair)
 if ch and dh:return False
 r=max(C&main);l=min(D&main)
 if ch:return max(r,v)<l
 if dh:return r<min(l,v)
 return r<l
relations={(C,D):direct(C,D) for C in L for D in L}
assert all(relations[C,D]==formula(C,D) for C in L for D in L)
samples=[frozenset({9}|set(range(13,18))),
         frozenset({9}|set(range(16,18))),
         frozenset(set(range(4,10))|hair)]
def cones(D):
 return ({C for C in L if relations[C,D]},{C for C in L if relations[D,C]})
assert len(set(samples))==3
assert cones(samples[0])==cones(samples[1])==cones(samples[2])
K=frozenset({6})
pred,succ=cones(samples[0]);pk,sk=cones(K)
assert pred<=pk and succ<=sk and not K<=samples[0]
print('Finite tree: 13 main vertices, branch at 4, 5 additional hair vertices.')
print('Valid internal grid cuts:',len(cuts),'plus 2 ends.')
print('All global cut sets match the interval/terminal-hair classification.')
print('Direct relative-component order comparisons:',len(L)**2,'all agree with V1.')
print('Two distinct terminal-hair cuts and their connected filled hull have identical strict cones.')
print('Their strict predecessor count:',len(pred),'strict successor count:',len(succ))
print('A bare interior point also passes the specialization-cone inclusion test without being a subset.')
print('PASS. Continuous density/local filtering are proved in V, not inferred from this grid.')
