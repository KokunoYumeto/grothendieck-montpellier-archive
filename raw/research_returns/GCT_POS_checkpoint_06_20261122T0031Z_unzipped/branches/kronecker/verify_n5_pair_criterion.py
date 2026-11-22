"""Exact combinatorial hypotheses for K-012/K-013 on all 77 records."""
from collections import Counter
from pathlib import Path
import json

root=Path(__file__).resolve().parent
records=json.loads((root/'n5_type_analysis.json').read_text())
patterns=Counter();edge_counts=Counter();antipodal_free=[]
for record in records:
    pairs=[];pair_counts=[]
    for weights in record['W']:
        values=[v for v in range(8) if v in weights and v+8 in weights]
        assert len(values)<=1
        pair_counts.append(len(values))
        pairs.append(set() if not values else {weights.index(values[0]),weights.index(values[0]+8)})
    patterns[tuple(sorted(pair_counts))]+=1
    if 0 in pair_counts:
        antipodal_free.append(record['index'])
    else:
        count=sum(sum(e[a] in pairs[a] for a in range(3))==1 for e in record['chosen_support'])
        assert count>0
        edge_counts[count]+=1
assert patterns==Counter({(0,0,0):2,(0,0,1):8,(0,1,1):3,(1,1,1):64})
assert edge_counts==Counter({3:3,4:7,5:34,6:14,7:6})
assert antipodal_free==[1,25,38,39,40,41,42,43,50,51,67,68,73]
print('PASS all77 single-pair hypotheses')
print('antipodal-free',antipodal_free)
print('pair patterns',dict(patterns))
print('one-pair edges',dict(edge_counts))
