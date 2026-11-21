#!/usr/bin/env python3
"""Exact exploration of the support graph on gaps (g1,g2,g3,0)>0."""
from pathlib import Path
from collections import deque
import json
from five_row_cycle_trace import multiplicities,partition_from_gaps,traces

HERE=Path(__file__).resolve().parent
face=next(f for f in json.loads((HERE/'FIVE_ROW_FACE_EXPLORATION.json').read_text())
          if f['support']==[0,1,2])
generators=[tuple(v) for v in face['generators']]
for seed in face['seeds']:
    seed['traces']=traces(partition_from_gaps(seed['gaps']))

def normalize(g):
    a,b,c,_=g;threshold=3*b+2*c
    if a<threshold:return tuple(g)
    first=threshold+(a-threshold)%10
    return (first,b,c,0)

queue=deque(normalize(s['gaps']) for s in face['seeds'] if min(s['multiplicities'])==0)
seen={};edges=[]
while queue:
    g=queue.popleft()
    if g in seen:continue
    values=multiplicities(partition_from_gaps(g))
    assert min(values)==0,(g,values)
    seen[g]=values
    for v in generators:
        original=tuple(a+2*b for a,b in zip(g,v));target=normalize(original)
        actual=multiplicities(partition_from_gaps(target))
        row={'source':g,'generator':v,'raw_target':original,'target':target,
             'traces':traces(partition_from_gaps(target)),
             'multiplicities':actual,'all_positive':min(actual)>0}
        edges.append(row)
        if min(actual)==0 and target not in seen:queue.append(target)
    if len(seen)>1000:raise RuntimeError('exploration did not close within1000 nodes')
    if len(seen)%10==0:print('nodes',len(seen),'queue',len(queue),flush=True)
nodes=[{'gaps':g,'traces':traces(partition_from_gaps(g)),
        'multiplicities':v,'stable_ray':g[0]>=3*g[1]+2*g[2]}
       for g,v in sorted(seen.items())]
result={'support':face['support'],'generators':generators,'initial_seeds':face['seeds'],
        'nodes':nodes,'edges':edges,'closed':True}
(HERE/'THREE_ROW_SUPPORT_GRAPH.json').write_text(json.dumps(result,indent=2)+'\n')
print('CLOSED',len(nodes),'nodes',len(edges),'edges','stable rays',sum(n['stable_ray'] for n in nodes))
for n in nodes:print(n)
