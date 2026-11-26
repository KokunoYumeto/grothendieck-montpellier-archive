#!/usr/bin/env python3
"""Independent exact BFS of Harper initial-segment distance layers."""
from pathlib import Path
from fractions import Fraction
from collections import deque
from itertools import combinations
import json, hashlib, os
base=Path(__file__).resolve().parents[1]
p=base/'inputs/ex_harper_layers_parameters.json'
params=json.loads(p.read_text()); out=[]
for D in params['dimensions']:
 d=D-1; N=1<<d; K=(N+params['terms']-1)//params['terms']
 # Simplicial order: size, then lexicographic order of the increasing tuple.
 order=[sum(1<<i for i in s) for w in range(d+1) for s in combinations(range(d),w)]
 dist=[-1]*N; queue=deque(order[:K])
 for x in queue:dist[x]=0
 while queue:
  x=queue.popleft()
  for i in range(d):
   y=x^(1<<i)
   if dist[y]<0:dist[y]=dist[x]+1;queue.append(y)
 layers=[dist.count(j) for j in range(max(dist)+1)]
 T=params['width']*D-1; lip=2*params['width']
 lower=Fraction(sum(max(0,T-lip*t)**2 for t in dist),N)
 upper=(Fraction(params['upper_coefficient_num'],params['upper_coefficient_den'])*D)**2
 out.append({'D':D,'cube_dimension':d,'high_set_size':K,'layers':layers,
 'lower_moment':str(lower),'strict_cost_upper':str(upper),
 'gap':str(lower-upper),'excludes':lower>upper})
record={'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'method':'Independent combinations-lex initial segment and multi-source hypercube BFS; exact Fraction arithmetic.',
 'results':out}
p=base/'outputs/ex_harper_layers_independent.json'; q=p.with_name(p.name+'.atomic_tmp')
with q.open('w') as f:json.dump(record,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
os.replace(q,p)
print(json.dumps(record,indent=2))
