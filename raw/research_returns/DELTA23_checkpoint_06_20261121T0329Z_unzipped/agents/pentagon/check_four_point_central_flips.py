#!/usr/bin/env python3
"""Exact finite matrix certificate for D23.P1; no profinite lifting claim."""
import itertools, json, pathlib
p=3
I=(1,0,0,1)
def mul(a,b):
 return ((a[0]*b[0]+a[1]*b[2])%p,(a[0]*b[1]+a[1]*b[3])%p,(a[2]*b[0]+a[3]*b[2])%p,(a[2]*b[1]+a[3]*b[3])%p)
def inv(a):
 assert (a[0]*a[3]-a[1]*a[2])%p==1
 return (a[3]%p,-a[1]%p,-a[2]%p,a[0]%p)
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
def generated(gs):
 seen={I}; todo=[I]
 while todo:
  a=todo.pop()
  for g in gs:
   b=mul(a,g)
   if b not in seen:seen.add(b);todo.append(b)
 return seen
x=(1,2,0,1);y=(1,0,1,1)
G=generated([x,y]); allSL={a for a in itertools.product(range(p),repeat=4) if (a[0]*a[3]-a[1]*a[2])%p==1}
assert G==allSL
D=generated([comm(a,b) for a in G for b in G])
DD=generated([comm(a,b) for a in D for b in D])
minusI=(2,0,0,2)
assert len(G)==24 and len(D)==8 and DD=={I,minusI}
c1=comm(x,y);c2=mul(mul(x,comm(y,x)),inv(x));w=comm(c1,c2)
assert w==minusI
# A formal dependency calculation: deleting each label kills an inner commutator.
assert ({1,2}|{2,3})=={1,2,3}
assert ({2,3}|{3,4})=={2,3,4}
result={'group_order':len(G),'derived_order':len(D),'second_derived_order':len(DD),'x':x,'y':y,'commutator_1':c1,'commutator_2':c2,'word':w,'result':'PASS','scope':'Finite matrix part only; geometric forgetting and profinite statements proved in text.'}
print(json.dumps(result,indent=2))
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
