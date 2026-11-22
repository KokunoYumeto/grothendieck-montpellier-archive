"""Exact coefficient relations on the six-coordinate support x!=0."""
from pathlib import Path
from collections import Counter
from itertools import product
from datetime import datetime,timezone
import json,time,hashlib
start=time.perf_counter()
dependency=Path(__file__).with_name('post_CP30_Moore_full_coefficients.output.json')
data=json.loads(dependency.read_text())
support=tuple(range(3,9));mask=sum(1<<i for i in support)
relations={}
for x,cs in data['coefficients'].items():
    terms=[]
    for value in cs:
        c=int(value,16);exps=tuple((c>>(4*i))&15 for i in range(9))
        if any(exps[i] for i in range(3)):continue
        terms.append(tuple(exps[i] for i in support))
    if not terms:continue
    common=tuple(min(t[i] for t in terms) for i in range(6))
    relation=tuple(sorted(tuple(t[i]-common[i] for i in range(6)) for t in terms))
    relations.setdefault(relation,{'x':x,'common':common})
ordered=sorted(relations,key=lambda r:(sum(r[0]),len(r),r))
out={'status':'EXACT_SIX_SUPPORT_RELATIONS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-start,'support':support,
     'unique_relation_count':len(ordered),
     'degree_term_counts':dict(Counter(str((sum(r[0]),len(r))) for r in ordered)),
     'relations':[{'terms':r,'witness':relations[r]} for r in ordered],
     'dependency_sha256':hashlib.sha256(dependency.read_bytes()).hexdigest(),
     'scope':'Each relation is an actual determinant coefficient divided by its common monomial, invertible on this support torus. No radical computation or classification inferred.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','actual_utc','runtime_seconds','unique_relation_count','degree_term_counts')}))
print(json.dumps(out['relations'][:20]))
