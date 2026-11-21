from pathlib import Path
import sys,json
from fractions import Fraction
from math import comb
from itertools import product
sys.path.insert(0,'work/theta/outer5/variable_wall')
from chamber_polynomials import difference,serialized,SIZES
p=Path('work/root/VARIABLE_WALL_INITIAL_INPUT.json')
s=json.loads(p.read_text())
def change(raw):
 out={}
 for power,value in raw.items():
  i,j,k=map(int,power.split(','));coef=Fraction(*value)
  for ell in range(i+1):
   for m in range(i-ell+1):
    e=(ell,j,k+m)
    c=coef*comb(i,ell)*comb(i-ell,m)*(-1)**m*(-2)**(i-ell-m)
    out[e]=out.get(e,Fraction(0))+c
 return {e:c for e,c in out.items() if c}
data=[{phase:change(poly) for phase,poly in cls.items()} for cls in s['phase_polynomials']]
identity=data[0]['0,0,0'];negative=[];margins=[];active=[]
for order in product(range(4),range(5),range(6)):
 if not 0<sum(order)<=5:continue
 ident=difference(identity,order);bounds={}
 for size,phases in zip(SIZES[1:],data[1:]):
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
out={'coordinate_change':'X_old=X-K-2; k=K+3,b=3k-2+B,x=X','negative_identity':serialized({p:v for p,v in identity.items() if v<0}),'active_orders':active,'margins':margins,'negative_margins':negative,'phase_polynomials':[{phase:serialized(poly) for phase,poly in cls.items()} for cls in data]}
Path('work/root/VARIABLE_WALL_ENLARGEMENT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'active':len(active),'negative_identity':out['negative_identity'],'negative':negative,'minimum_constant':min(Fraction(x['constant_margin']) for x in margins)},default=str))
