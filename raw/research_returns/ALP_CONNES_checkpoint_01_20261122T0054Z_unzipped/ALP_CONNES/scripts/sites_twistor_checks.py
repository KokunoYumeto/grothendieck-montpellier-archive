"""Exact finite checks for AC-G08, AC-G10 and AC-G12; not general proof certificates."""
import itertools,json
from pathlib import Path

def mul(p,q):
 r={}
 for (i,e),a in p.items():
  for (j,f),b in q.items():
   k=(i+j,(e+f)%2);r[k]=r.get(k,0)+a*b
 return r
P={(0,0):1,(1,0):1,(1,1):1,(2,0):1}
Q={(0,0):1,(1,0):1,(2,0):1}
R=mul(mul(P,P),Q)
ap=[R.get((j,0),0) for j in range(7)]
am=[R.get((j,1),0) for j in range(7)]
d=[a+b for a,b in zip(ap,am)];c=[a-b for a,b in zip(ap,am)]
assert ap==[1,3,7,8,7,3,1] and am==[0,2,4,6,4,2,0]
assert d==[1,5,11,14,11,5,1] and c==[1,1,3,2,3,1,1]
# G(F3) has elements tau=-1, e=0, 1,2.
E=[-1,0,1,2]
def add(a,b):
 if a==-1:return b
 if b==-1:return a
 return (a+b)%3
def prod(a,b):
 if a==-1 or b==-1:return -1
 return a*b%3
ringmaps=[]
for vals in itertools.product(range(3),repeat=4):
 phi=dict(zip(E,vals))
 if phi[-1]!=0 or phi[1]!=1:continue
 if all(phi[add(a,b)]==(phi[a]+phi[b])%3 and phi[prod(a,b)]==phi[a]*phi[b]%3 for a,b in itertools.product(E,repeat=2)):
  ringmaps.append(phi)
assert len(ringmaps)==1
boolmaps=[]
for vals in itertools.product([0,1],repeat=4):
 phi=dict(zip(E,vals))
 if phi[-1]!=0 or phi[1]!=1:continue
 if all(phi[add(a,b)]==max(phi[a],phi[b]) and phi[prod(a,b)]==min(phi[a],phi[b]) for a,b in itertools.product(E,repeat=2)):
  boolmaps.append(phi)
assert len(boolmaps)==1
assert (-1)**2==1 and (-1)*1!=1
out={'AC-G12':{'a_plus':ap,'a_minus':am,'dimensions':d,'inert_traces':c},'AC-G10_F3':{'semiring_elements':4,'ring_maps_to_F3':ringmaps,'maps_to_B':boolmaps},'AC-G08':{'epsilon_even_power':1,'epsilon_times_even_power':-1}}
print(json.dumps(out,indent=2))
