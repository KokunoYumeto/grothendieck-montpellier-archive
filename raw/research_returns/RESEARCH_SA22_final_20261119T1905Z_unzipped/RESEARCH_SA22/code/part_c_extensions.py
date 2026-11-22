#!/usr/bin/env python3
"""Exhaustive certificates for the two nonisomorphic two-torsion extensions of C2."""
from itertools import product
from collections import Counter
from pathlib import Path
import json,time
def conv(f,g,mul):
 out=[0]*len(f)
 for i,a in enumerate(f):
  for j,b in enumerate(g): out[mul(i,j)]+=a*b
 return out

def indicator(a,n): return [int(i in a) for i in range(n)]

def cone_coefficients(v,chain):
 prev=set(); levels=[]
 for a in chain:
  values={v[x] for x in set(a)-prev}
  if len(values)!=1: return None
  levels.append(next(iter(values)));prev=set(a)
 coeff=[levels[i]-(levels[i+1] if i+1<len(levels) else 0) for i in range(len(levels))]
 if min(coeff)<0:return None
 assert v==[sum(c*int(x in a) for c,a in zip(coeff,chain)) for x in range(len(v))]
 return coeff
start=time.perf_counter(); out=[]
G={0,1}
for name,E,mul,rho,inc,families in [
 ('C4',list(range(4)),lambda x,y:(x+y)%4,lambda x:x%2,lambda t:2*t,
  {0:[{0},G],1:[G],2:[{1},G],3:[G]}),
 ('C2xC2',list(product(range(2),repeat=2)),lambda x,y:((x[0]+y[0])%2,(x[1]+y[1])%2),lambda x:x[0],lambda t:(0,t),
  {(s,t):([{t},G] if s==0 else [G]) for s,t in product(range(2),repeat=2)})]:
 counts=Counter()
 for k in E:
  chain=families[k]
  assert all(a<=b or b<=a for a,b in product(chain,repeat=2)); counts['chains']+=1
  for a in chain:
   assert a=={(rho(k)-x)%2 for x in a};counts['symmetry_atoms']+=1
 for k,l in product(E,repeat=2):
  for a,b in product(families[k],families[l]):
   c=conv(indicator(a,2),indicator(b,2),lambda x,y:(x+y)%2)
   assert cone_coefficients(c,families[mul(k,l)]) is not None
   counts['convolution_pairs']+=1
  assert any(all(a<=b or b<=a for a,b in product(families[k]+[{(x+s)%2 for x in b} for b in families[l]],repeat=2)) for s in G)
  counts['alignment_pairs']+=1
 for t,k in product(G,E):
  assert families[mul(inc(t),k)]==[{(t+x)%2 for x in a} for a in families[k]]
  counts['kernel_equivariance']+=1
 assert {len(a) for chain in families.values() for a in chain}=={1,2}
 out.append({'extension':name,'counts':dict(counts),'all_positive_cardinalities':[1,2]})
result={'results':out,'runtime_seconds':time.perf_counter()-start}
Path(__file__).with_name('part_c_extensions_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2));print('PASS')
