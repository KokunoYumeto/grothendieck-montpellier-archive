#!/usr/bin/env python3
"""Exploratory exact seed support on every equal-row face; no theorem claim."""
from itertools import product, combinations
from pathlib import Path
import json
from five_row_cycle_trace import multiplicities,partition_from_gaps

HERE=Path(__file__).resolve().parent
faces=[]
for cardinality in range(1,4):
    for support in combinations(range(4),cardinality):
        seeds=[]
        for parity in product(range(2),repeat=cardinality):
            base=[0]*4
            for i,p in zip(support,parity):base[i]=2+p
            candidates=[]
            for small in product(range(5),repeat=cardinality):
                if sum(small)>4:continue
                u=[0]*4
                for i,v in zip(support,small):u[i]=v
                if sum((i+1)*(base[i]+2*u[i]) for i in range(4))%5==0:
                    candidates.append(tuple(u))
            minimal=[u for u in candidates if not any(v!=u and all(a<=b for a,b in zip(v,u)) for v in candidates)]
            for u in minimal:
                gaps=tuple(b+2*v for b,v in zip(base,u));lam=partition_from_gaps(gaps)
                seeds.append({'parity':parity,'increment':u,'gaps':gaps,'partition':lam,
                              'inner':sum(lam)//5,'multiplicities':multiplicities(lam)})
        candidates=[]
        for small in product(range(6),repeat=cardinality):
            if not 1<=sum(small)<=5:continue
            u=[0]*4
            for i,v in zip(support,small):u[i]=v
            if sum((i+1)*u[i] for i in range(4))%5==0:candidates.append(tuple(u))
        generators=[u for u in candidates if not any(v!=u and all(a<=b for a,b in zip(v,u)) for v in candidates)]
        face={'support':support,'seeds':seeds,'generators':generators}
        faces.append(face)
        always=[i for i in range(7) if all(s['multiplicities'][i]>0 for s in seeds)]
        all_positive=sum(min(s['multiplicities'])>0 for s in seeds)
        print('face',support,'seeds',len(seeds),'generators',len(generators),
              'always',always,'allpositive',all_positive,flush=True)
(HERE/'FIVE_ROW_FACE_GAP2_EXPLORATION.json').write_text(json.dumps(faces,indent=2)+'\n')
