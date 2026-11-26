"""Independent exact checker: no LP, graph-search code, or NumPy import."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
inp = ROOT / (sys.argv[1] if len(sys.argv)>1 else 'outputs/sh_lu_preparation_routing.json')
d = json.loads(inp.read_text())
state = json.loads((ROOT / 'inputs/rt_lu_rank_probe.json').read_text())
G = [[int(c) for c in row] for row in state['basis']]
# Enumerate the original support and recover the six words whose pivot
# projections are coordinate vectors.  This does not import or repeat the
# discovery program's Gaussian-elimination implementation.
pivots = [1,2,3,4,8,16]
words = [[sum(((mask >> i) & 1)*G[i][v] for i in range(6)) % 2 for v in range(27)]
         for mask in range(64)]
assert len({tuple(w[p-1]for p in pivots)for w in words}) == 64
R = []
for i in range(6):
    target = [int(j == i)for j in range(6)]
    row = [w for w in words if [w[p-1]for p in pivots] == target]
    assert len(row) == 1;R.append(row[0])
edges = {tuple(sorted((p,v))) for i,p in enumerate(pivots)
         for v in range(1,28) if v not in pivots and R[i][v-1]}
assert len(edges) == 70
if d.get('graph_format') == 'lc_search':
    qpath = ROOT / d['graph_input'];q = json.loads(qpath.read_text())
    assert hashlib.sha256(qpath.read_bytes()).hexdigest() == d['graph_sha256']
    for v in q['local_complementation_sequence_one_based']:
        neighbors = [w for w in range(1,28) if tuple(sorted((v,w))) in edges]
        for i,u in enumerate(neighbors):
            for w in neighbors[i+1:]:
                e=tuple(sorted((u,w)))
                if e in edges:edges.remove(e)
                else:edges.add(e)
assert edges == {tuple(e)for e in d['edges']}
loads = {e:Fraction()for e in edges}
demands = {(u,v):Fraction()for u in range(1,28)for v in range(u+1,28)}
for rec in d['certificate']:
    path = rec['path']; num,den = rec['weight']; x=Fraction(num,den)
    assert num > 0 and den > 0 and len(path) == len(set(path))
    assert all(1 <= v <= 27 for v in path)
    assert 2 <= len(path) <= 5 and path[0] < path[-1]
    demands[path[0],path[-1]] += x
    for u,v in zip(path,path[1:]):
        e=tuple(sorted((u,v)));assert e in edges;loads[e]+=x
assert all(x==Fraction(2,27)for x in demands.values())
assert all(x<=1 for x in loads.values())
out={'status':'PASS independent exact path/capacity verification',
     'certificate_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),
     'paths':len(d['certificate']),'pairs':len(demands),'edges':len(edges),
     'uniform_demand':[2,27],
     'maximum_edge_load':[max(loads.values()).numerator,max(loads.values()).denominator],
     'source_graph_reconstructed':'by enumerating original support and selecting six pivot-coordinate words'}
p=ROOT/(sys.argv[2] if len(sys.argv)>2 else 'outputs/sh_lu_preparation_routing_verified.json');t=p.with_suffix('.json.tmp')
t.write_text(json.dumps(out,separators=(',',':'))+'\n');t.replace(p)
print(json.dumps(out,indent=2))
