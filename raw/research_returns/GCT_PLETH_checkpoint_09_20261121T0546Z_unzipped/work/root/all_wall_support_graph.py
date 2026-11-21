#!/usr/bin/env python3
"""Exact finite support exploration on all proper five-row faces.

Point transitions and every initial segment of a stable-ray transition
are retained. This prevents loss of a diagonal state when two stable
directions interact. The report supplies the exhaustion proof.
"""
from collections import deque
from pathlib import Path
import json
from five_row_cycle_trace import multiplicities,partition_from_gaps,traces

HERE=Path(__file__).resolve().parent

def stable_axes(g,support):
    a,b,c,d=g
    axes=[]
    if 0 in support and a>=3*b+2*c+d:axes.append(0)
    if 3 in support and d>=a+2*b+3*c:axes.append(3)
    return axes

def threshold(g,axis):
    a,b,c,d=g
    return max(1,3*b+2*c+d) if axis==0 else max(1,a+2*b+3*c)

def normalize(g,support):
    axes=stable_axes(g,support)
    if not axes:return tuple(g)
    axis=axes[0];base=threshold(g,axis);out=list(g)
    out[axis]=base+(out[axis]-base)%10
    return tuple(out)

def graph(face):
    support=tuple(face['support'])
    generators=[tuple(v) for v in face['generators']]
    for seed in face['seeds']:
        seed['traces']=traces(partition_from_gaps(seed['gaps']))
    queue=deque(normalize(s['gaps'],support) for s in face['seeds']
                if min(s['multiplicities'])==0)
    seen={};edges=[];ray_edges=[]
    while queue:
        g=queue.popleft()
        if g in seen:continue
        value=multiplicities(partition_from_gaps(g))
        assert min(value)==0
        seen[g]=value
        for h in generators:
            raw=tuple(a+2*b for a,b in zip(g,h))
            tests=[(None,0,0,raw)]
            for axis in stable_axes(g,support):
                cutoff=max(0,(threshold(raw,axis)-raw[axis]+9)//10)
                for q in range(cutoff+1):
                    target=list(raw);target[axis]+=10*q
                    tests.append((axis,q,cutoff,tuple(target)))
            for axis,q,cutoff,target in tests:
                normal=normalize(target,support)
                vals=multiplicities(partition_from_gaps(normal))
                row={'source':g,'generator':h,'raw_target':target,
                     'target':normal,'traces':traces(partition_from_gaps(normal)),
                     'multiplicities':vals,'all_positive':min(vals)>0}
                if axis is None:edges.append(row)
                else:
                    row.update(axis=axis,q=q,cutoff=cutoff)
                    ray_edges.append(row)
                    if q==cutoff:
                        later=list(target);later[axis]+=10
                        assert normalize(later,support)==normal
                        assert axis in stable_axes(target,support)
                if min(vals)==0 and normal not in seen:queue.append(normal)
        if len(seen)>2000:raise RuntimeError(('unclosed exploration',support))
    nodes=[{'gaps':g,'traces':traces(partition_from_gaps(g)),
            'multiplicities':v,'stable_axes':stable_axes(g,support)}
           for g,v in sorted(seen.items())]
    result={'support':support,'generators':generators,'initial_seeds':face['seeds'],
            'nodes':nodes,'edges':edges,'ray_edges':ray_edges,'closed':True}
    print('CLOSED',support,'seeds',len(face['seeds']),'nodes',len(nodes),
          'point edges',len(edges),'ray checks',len(ray_edges),
          'finite',sum(not n['stable_axes'] for n in nodes),
          'ray bases',sum(len(n['stable_axes']) for n in nodes),flush=True)
    return result

def main():
    faces=json.loads((HERE/'FIVE_ROW_FACE_EXPLORATION.json').read_text())
    result={'statement_candidate':'G-031','faces':[]}
    for face in faces:
        result['faces'].append(graph(face))
        (HERE/'ALL_WALL_SUPPORT_GRAPH_WORKING.json').write_text(
            json.dumps(result,indent=2)+'\n')
    result['complete']=True
    result['node_count']=sum(len(f['nodes']) for f in result['faces'])
    result['edge_count']=sum(len(f['edges']) for f in result['faces'])
    result['ray_check_count']=sum(len(f['ray_edges']) for f in result['faces'])
    (HERE/'ALL_WALL_SUPPORT_GRAPH.json').write_text(json.dumps(result,indent=2)+'\n')
    print('ALL CLOSED',result['node_count'],result['edge_count'],result['ray_check_count'],flush=True)

if __name__=='__main__':main()
