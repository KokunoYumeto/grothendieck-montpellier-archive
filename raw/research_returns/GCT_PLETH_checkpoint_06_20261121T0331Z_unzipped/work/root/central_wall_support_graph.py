#!/usr/bin/env python3
"""Exact exploration of the support graph on gaps (g1,g2,0,g4)>0; two proved stable directions."""
from pathlib import Path
from collections import deque
import json
from five_row_cycle_trace import multiplicities,partition_from_gaps,traces

HERE=Path(__file__).resolve().parent
face=next(f for f in json.loads((HERE/'FIVE_ROW_FACE_EXPLORATION.json').read_text())
          if f['support']==[0,1,3])
generators=[tuple(v) for v in face['generators']]
for seed in face['seeds']:
    seed['traces']=traces(partition_from_gaps(seed['gaps']))

def stable_axis(g):
    a,b,_,c=g
    if a>=3*b+c:return 0
    if c>=a+2*b:return 3
    return None

def normalize(g):
    a,b,_,c=g
    if a>=3*b+c:
        threshold=3*b+c
        return (threshold+(a-threshold)%10,b,0,c)
    if c>=a+2*b:
        threshold=a+2*b
        return (a,b,0,threshold+(c-threshold)%10)
    return tuple(g)

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
        'multiplicities':v,'stable_ray':stable_axis(g) is not None,'stable_axis':stable_axis(g)}
       for g,v in sorted(seen.items())]
result={'support':face['support'],'generators':generators,'initial_seeds':face['seeds'],
        'nodes':nodes,'edges':edges,'closed':True}
ray_edges=[]
for node in nodes:
    axis=node['stable_axis']
    if axis is None:continue
    g=tuple(node['gaps'])
    for h in generators:
        raw=tuple(u+2*v for u,v in zip(g,h))
        threshold=3*raw[1]+raw[3] if axis==0 else raw[0]+2*raw[1]
        cutoff=max(0,(threshold-raw[axis]+9)//10)
        for q in range(cutoff+1):
            target=list(raw);target[axis]+=10*q;target=tuple(target)
            normal=normalize(target);value=multiplicities(partition_from_gaps(normal))
            assert min(value)>0 or normal in seen,(g,h,q,target,normal,value)
            if q==cutoff:
                later=list(target);later[axis]+=10
                assert normalize(later)==normal
                assert stable_axis(target)==axis
            ray_edges.append({'source':g,'axis':axis,'generator':h,'q':q,
                              'cutoff':cutoff,'raw_target':target,'target':normal,
                              'traces':traces(partition_from_gaps(normal)),
                              'multiplicities':value,'all_positive':min(value)>0})
result['ray_transition_checks']=ray_edges
result['maximum_ray_cutoff']=max(row['cutoff'] for row in ray_edges)
(HERE/'CENTRAL_WALL_SUPPORT_GRAPH.json').write_text(json.dumps(result,indent=2)+'\n')
print('CLOSED',len(nodes),'nodes',len(edges),'edges','stable rays',sum(n['stable_ray'] for n in nodes))
for n in nodes:print(n)
