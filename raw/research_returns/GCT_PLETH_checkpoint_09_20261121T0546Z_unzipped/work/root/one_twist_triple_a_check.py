from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from itertools import product,combinations
from math import comb,lcm
import json,sys
import sympy as sp
sys.path.insert(0,'work/theta/outer5/variable_wall')
from chamber_polynomials import difference,serialized,permutation,restricted_cycles,CLASSES,SIZES
RAW=json.loads(Path('work/root/ONE_TWIST_UPPER_INPUT.json').read_text())['phase_polynomials']

def add(p,q):
 out=dict(p)
 for e,c in q.items():out[e]=out.get(e,Fraction(0))+c
 return {e:c for e,c in out.items() if c}
def mul(p,q):
 out={}
 for a,c in p.items():
  for b,d in q.items():
   e=tuple(x+y for x,y in zip(a,b));out[e]=out.get(e,Fraction(0))+c*d
 return {e:c for e,c in out.items() if c}
FORMS=({(1,0,0):1,(0,1,0):1},{(0,1,0):-1,(0,0,0):-2},{(0,1,0):1,(0,0,1):1,(0,0,0):4})
@lru_cache(None)
def power(axis,n):
 out={(0,0,0):1}
 for _ in range(n):out=mul(out,FORMS[axis])
 return out
@lru_cache(None)
def mono(e):
 return mul(mul(power(0,e[0]),power(1,e[1])),power(2,e[2]))
def transform(poly):
 out={}
 for key,value in poly.items():
  e=tuple(map(int,key.split(',')));c=Fraction(*value)
  out=add(out,{p:c*v for p,v in mono(e).items()})
 return out

@lru_cache(None)
def triple_data(cycles):
 p=permutation(cycles);out=[]
 for selected in combinations(range(5),3):
  if set(p[i] for i in selected)!=set(selected):continue
  eta=restricted_cycles(p,selected)
  rest=restricted_cycles(p,set(range(5))-set(selected))
  epsilon=1 if rest==(1,1) else -1
  out.append((eta,epsilon,(-1)**len(eta)))
 return tuple(out)

@lru_cache(None)
def tail_poly(eta,epsilon,L,res):
 cap=res+L*5;values=[1]+[0]*cap
 for ell in eta:
  for sign in (1,epsilon**ell):
   for n in range(ell,cap+1):values[n]+=sign*values[n-ell]
 t=sp.Symbol('t');q=sp.Symbol('q')
 expr=sp.interpolate([(i,values[res+L*i]) for i in range(6)],q).subs(q,(t-res)/L).expand()
 return {(0,int(e[0]),0):Fraction(int(c.p),int(c.q)) for e,c in sp.Poly(expr,t).terms() if c}

all_data=[]
for idx,cycles in enumerate(CLASSES):
 L=lcm(*cycles);data={}
 for xr,tr,kr in product(range(L),repeat=3):
  ar=(3*tr+16+3*kr+xr)%L;br=(2*tr+16+3*kr)%L;kres=(tr+7+kr)%L
  out=transform(RAW[idx][f'{ar},{br},{kres}'])
  for eta,epsilon,orientation in triple_data(cycles):
   sign=orientation*epsilon**((xr+tr+kres)%2)*(eta.count(1)-1)
   out=add(out,{e:sign*c for e,c in tail_poly(eta,epsilon,L,tr).items()})
  data[(xr,tr,kr)]=out
 all_data.append(data)
 print('class',cycles,'phases',len(data),'degree',max(sum(e) for p in data.values() for e in p),flush=True)
identity=all_data[0][(0,0,0)];badidentity={p:c for p,c in identity.items() if c<0}
margins=[];negative=[];active=[]
for order in product(range(4),range(6),range(6)):
 if not 0<sum(order)<=5:continue
 ident=difference(identity,order);bounds={}
 for size,phases in zip(SIZES[1:],all_data[1:]):
  worst={}
  for poly in phases.values():
   for p,v in difference(poly,order).items():worst[p]=max(worst.get(p,0),abs(v))
  for p,v in worst.items():bounds[p]=bounds.get(p,0)+size*v
 if not ident and not bounds:continue
 active.append(order)
 margin={p:ident.get(p,0)-bounds.get(p,0) for p in set(ident)|set(bounds)}
 bad={p:c for p,c in margin.items() if c<0}
 if bad:negative.append({'order':order,'negative':serialized(bad)})
 margins.append({'order':order,'constant_margin':str(margin.get((0,0,0),0)),'minimum':str(min(margin.values())),'margin':serialized(margin)})
out={'parameter_map':'c=1,t=B,k=t+7+K,x=t+X,b=3k-5-t','negative_identity':serialized(badidentity),'active_orders':active,'margins':margins,'negative_margins':negative,'phase_polynomials':[{','.join(map(str,phase)):serialized(poly) for phase,poly in data.items()} for data in all_data]}
Path('work/root/ONE_TWIST_TRIPLE_A_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'active':len(active),'negative_identity':out['negative_identity'],'negative':negative,'minimum_constant':min(Fraction(x['constant_margin']) for x in margins)},default=str))
