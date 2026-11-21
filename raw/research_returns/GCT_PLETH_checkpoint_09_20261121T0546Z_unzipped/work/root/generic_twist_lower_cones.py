from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from itertools import product,combinations
from math import lcm
import json,sys
import sympy as sp
sys.path.insert(0,'work/theta/outer5/variable_wall')
from chamber_polynomials import permutation,restricted_cycles,CLASSES,SIZES
from generic_twist_upper_polynomials import difference_tuple,serialized
RAW=json.loads(Path('work/root/GENERIC_TWIST_UPPER_INPUT.json').read_text())['phase_polynomials']
ZERO=(0,0,0,0)

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

@lru_cache(None)
def triple_data(cycles):
 p=permutation(cycles);out=[]
 for selected in combinations(range(5),3):
  if set(p[i] for i in selected)!=set(selected):continue
  eta=restricted_cycles(p,selected)
  rest=restricted_cycles(p,set(range(5))-set(selected))
  out.append((eta,1 if rest==(1,1) else -1,(-1)**len(eta)))
 return tuple(out)

@lru_cache(None)
def tail_poly(eta,epsilon,L,res):
 cap=res+L*5;values=[1]+[0]*cap
 for ell in eta:
  for sign in (1,epsilon**ell):
   for n in range(ell,cap+1):values[n]+=sign*values[n-ell]
 t,q=sp.symbols('t q')
 expr=sp.interpolate([(i,values[res+L*i]) for i in range(6)],q).subs(q,(t-res)/L).expand()
 return {(0,int(e[0]),0,0):Fraction(int(c.p),int(c.q)) for e,c in sp.Poly(expr,t).terms() if c}

@lru_cache(None)
def standard_h(eta,cr):
 if eta==(1,1,1):return {ZERO:Fraction(1),(0,0,0,1):Fraction(1)}
 if eta==(2,1):return {ZERO:Fraction(1)} if cr%2==0 else {}
 assert eta==(3,),eta
 v=(1,-1,0)[cr%3]
 return {ZERO:Fraction(v)} if v else {}

@lru_cache(None)
def tail_power(n):
 out={ZERO:Fraction(1)}
 for _ in range(n):out=mul(out,{(1,0,0,0):1,(0,1,0,0):1,ZERO:1})
 return out

def changed_tail(poly):
 out={}
 for e,c in poly.items():out=add(out,{p:c*v for p,v in tail_power(e[1]).items()})
 return out

def build(branch):
 if branch=='A':
  forms=({(1,0,0,0):1,(0,1,0,0):1},{(0,1,0,0):-1,ZERO:-1},{(0,1,0,0):1,(0,0,1,0):1,ZERO:2},{(0,0,0,1):1})
 else:
  forms=({(1,0,0,0):1},{(1,0,0,0):-1,(0,1,0,0):-1,ZERO:-2},{(1,0,0,0):1,(0,1,0,0):2,(0,0,1,0):1,ZERO:4},{(0,0,0,1):1})
 @lru_cache(None)
 def power(axis,n):
  out={ZERO:Fraction(1)}
  for _ in range(n):out=mul(out,forms[axis])
  return out
 @lru_cache(None)
 def mono(e):
  out={ZERO:Fraction(1)}
  for axis,n in enumerate(e):out=mul(out,power(axis,n))
  return out
 @lru_cache(None)
 def transform(pairs):
  out={}
  for e,c in pairs:out=add(out,{p:c*v for p,v in mono(e).items()})
  return out
 data=[]
 for idx,cycles in enumerate(CLASSES):
  L=lcm(*cycles);row={}
  for xr,sr,kr,cr in product(range(L),repeat=4):
   if branch=='A':
    x=xr+sr;R=sr+6+kr;b=cr+2*sr+15+3*kr
   else:
    x=xr;R=xr+2*sr+8+kr;b=cr+2*xr+5*sr+20+3*kr
   a=b+x;k=cr+R
   raw=RAW[idx][','.join(str(v%L) for v in (a,b,k,cr))]
   pairs=tuple(sorted((tuple(map(int,e.split(','))),Fraction(*v)) for e,v in raw.items()))
   out=dict(transform(pairs))
   for eta,epsilon,orientation in triple_data(cycles):
    if branch=='A':correction=tail_poly(eta,epsilon,L,sr)
    else:
     correction=changed_tail(tail_poly(eta,epsilon,L,(xr+sr+1)%L))
     correction=add(correction,{e:-v for e,v in tail_poly(eta,epsilon,L,sr).items()})
    correction=mul(correction,standard_h(eta,cr))
    sign=orientation*epsilon**((x+R-1)%2)
    out=add(out,{e:sign*v for e,v in correction.items()})
   row[(xr,sr,kr,cr)]=out
  data.append(row)
  print(branch,'class',cycles,'phases',len(row),'degree',max(sum(e) for p in row.values() for e in p),flush=True)
 identity=data[0][ZERO]
 unique=[set(tuple(sorted(p.items())) for p in row.values()) for row in data]
 support=set(p for row in data for poly in row.values() for p in poly)
 orders=set(order for p in support for order in product(*(range(v+1) for v in p)));orders.discard(ZERO)
 active=[];margins=[];failed=[]
 for order in sorted(orders):
  first=dict(difference_tuple(tuple(sorted(identity.items())),order));worst={}
  for size,polys in zip(SIZES[1:],unique[1:]):
   bound={}
   for poly in polys:
    for p,v in difference_tuple(poly,order):bound[p]=max(bound.get(p,0),abs(v))
   for p,v in bound.items():worst[p]=worst.get(p,0)+size*v
  if not first and not worst:continue
  active.append(order)
  margin={p:first.get(p,0)-worst.get(p,0) for p in first.keys()|worst.keys()}
  bad={p:v for p,v in margin.items() if v<0}
  if bad:failed.append({'order':order,'negative':serialized(bad)})
  margins.append({'order':order,'constant':str(margin.get(ZERO,0)),'minimum':str(min(margin.values())),'margin':serialized(margin)})
 result={'branch':branch,'coordinates':('X,T,K,C' if branch=='A' else 'X,S,K,C'),
 'parameter_map':('c=C,k=C+T+6+K,x=T+X,b=C+2T+15+3K' if branch=='A' else 'c=C,k=C+X+2S+8+K,x=X,b=C+2X+5S+20+3K'),
 'phase_keys':'residues of the four cone coordinates, not physical a,b,k,c',
 'degrees':[max(sum(e) for p in row.values() for e in p) for row in data],
 'separate_degrees':[max(e[j] for row in data for p in row.values() for e in p) for j in range(4)],
 'unique_phase_counts':list(map(len,unique)),
 'negative_identity':serialized({p:v for p,v in identity.items() if v<0}),
 'active_orders':active,'margins':margins,'failed':failed,
 'phase_polynomials':[{','.join(map(str,key)):serialized(poly) for key,poly in row.items()} for row in data]}
 Path(f'work/root/GENERIC_TWIST_LOWER_{branch}_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
 print(branch,json.dumps({'active':len(active),'failed':failed,'negative_identity':result['negative_identity'],'minimum_constant':str(min(Fraction(v['constant']) for v in margins))}),flush=True)
 return result
if __name__=='__main__':
 for branch in ('A','B'):build(branch)
