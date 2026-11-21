from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import lcm
import json,sys
sys.path.insert(0,'work/theta/outer5/variable_wall')
from chamber_polynomials import CLASSES,SIZES
from generic_twist_upper_polynomials import difference_tuple,serialized
ROOT=Path('work/root')
UPPER=json.loads((ROOT/'GENERIC_TWIST_UPPER_INPUT.json').read_text())['phase_polynomials']
LOWER=json.loads((ROOT/'GENERIC_TWIST_LOWER_A_CHECK.json').read_text())['phase_polynomials']

def add(p,q):
 o=dict(p)
 for e,v in q.items():o[e]=o.get(e,Fraction(0))+v
 return {e:v for e,v in o.items() if v}
def mul(p,q):
 o={}
 for a,v in p.items():
  for b,w in q.items():
   e=tuple(x+y for x,y in zip(a,b));o[e]=o.get(e,Fraction(0))+v*w
 return {e:v for e,v in o.items() if v}
def affine(const,coeff):
 n=len(coeff);o={(0,)*n:Fraction(const)} if const else {}
 for i,v in enumerate(coeff):
  if v:e=[0]*n;e[i]=1;o[tuple(e)]=Fraction(v)
 return o

def build(name,forms,source):
 n=len(next(iter(forms[0])));zero=(0,)*n;raw=LOWER if source=='lower' else UPPER
 @lru_cache(None)
 def power(axis,j):
  out={zero:Fraction(1)}
  for _ in range(j):out=mul(out,forms[axis])
  return out
 @lru_cache(None)
 def mono(e):
  out={zero:Fraction(1)}
  for axis,j in enumerate(e):out=mul(out,power(axis,j))
  return out
 @lru_cache(None)
 def transform(poly):
  out={}
  for e,v in poly:out=add(out,{p:v*w for p,w in mono(e).items()})
  return out
 def value(poly,Z):return sum(v*__import__('math').prod(z**i for z,i in zip(Z,e)) for e,v in poly.items())
 data=[]
 for idx,cycles in enumerate(CLASSES):
  L=lcm(*cycles);row={}
  for phase in product(range(L),repeat=n):
   old=tuple(int(value(p,phase)) for p in forms)
   if source=='lower':key=tuple(v%L for v in old)
   else:
    X,B,K,C=old;key=((C+3*K+10+B+X)%L,(C+3*K+10+B)%L,(C+K+4)%L,C%L)
   p=raw[idx][','.join(map(str,key))]
   out=transform(tuple(sorted((tuple(map(int,e.split(','))),Fraction(*v)) for e,v in p.items())))
   row[phase]=out
  data.append(row)
 identity=data[0][zero];unique=[set(tuple(sorted(p.items())) for p in row.values()) for row in data]
 support=set(e for row in data for p in row.values() for e in p)
 orders=set(o for e in support for o in product(*(range(i+1) for i in e)));orders.discard(zero)
 active=[];margins=[];failed=[]
 for order in sorted(orders):
  first=dict(difference_tuple(tuple(sorted(identity.items())),order));worst={}
  for size,polys in zip(SIZES[1:],unique[1:]):
   bound={}
   for p in polys:
    for e,v in difference_tuple(p,order):bound[e]=max(bound.get(e,0),abs(v))
   for e,v in bound.items():worst[e]=worst.get(e,0)+size*v
  if not first and not worst:continue
  active.append(order);margin={e:first.get(e,0)-worst.get(e,0) for e in first.keys()|worst.keys()}
  bad={e:v for e,v in margin.items() if v<0}
  if bad:failed.append(dict(order=order,negative=serialized(bad)))
  margins.append(dict(order=order,constant=str(margin.get(zero,0)),minimum=str(min(margin.values())),margin=serialized(margin)))
 result={'name':name,'dimension':n,'source':source,'source_coordinate_forms':[serialized(p) for p in forms],
 'phase_keys':'residues of new nonnegative free coordinates',
 'degrees':[max(sum(e) for p in row.values() for e in p) for row in data],
 'negative_identity':serialized({e:v for e,v in identity.items() if v<0}),
 'active_orders':active,'margins':margins,'failed':failed,
 'phase_polynomials':[{','.join(map(str,key)):serialized(p) for key,p in row.items()} for row in data]}
 (ROOT/f'GENERIC_TWIST_BOUNDARY_{name}.json').write_text(json.dumps(result,indent=2)+'\n')
 print(name,json.dumps({'dimension':n,'active':len(active),'negative_identity':result['negative_identity'],'failed':failed,'minimum_constant':str(min(Fraction(v['constant']) for v in margins))}),flush=True)
 return result

if __name__=='__main__':
 for D in range(3):
  forms=[affine(3-D,[1,0,0]),affine(0,[0,1,0]),affine(D-3,[0,0,0]),affine(2,[0,0,1])]
  build('D'+str(D),forms,'lower')
 for R,shift,b0 in ((1,1,2),(2,2,4),(3,1,7)):
  forms=[affine(shift,[1,0]),affine(b0-3*R+2,[0,0]),affine(R-4,[0,0]),affine(2,[0,1])]
  build('R'+str(R)+'a',forms,'upper')
  forms=[affine(0,[1,0,0]),affine(b0+1-3*R+2,[0,1,0]),affine(R-4,[0,0,0]),affine(2,[0,0,1])]
  build('R'+str(R)+'b',forms,'upper')
