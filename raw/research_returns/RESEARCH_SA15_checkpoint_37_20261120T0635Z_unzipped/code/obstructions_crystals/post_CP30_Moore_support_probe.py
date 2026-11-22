"""Exact support exclusions from single determinant coefficient monomials."""
from pathlib import Path
from itertools import product, combinations
from collections import Counter
from datetime import datetime, timezone
import json, time, hashlib

start=time.perf_counter()
dependency=Path(__file__).with_name('post_CP30_Moore_full_coefficients.output.json')
data=json.loads(dependency.read_text())
coeffs=[]
for x,cs in data['coefficients'].items():
    terms=[]
    for value in cs:
        c=int(value,16)
        support=sum(1<<i for i in range(9) if (c>>(4*i))&15)
        terms.append((c,support))
    coeffs.append((int(x,16),terms))
coeffs.sort(key=lambda row:len(row[1]))
points=list(product(range(3),repeat=2));index={v:i for i,v in enumerate(points)}
known={}
for h in points:
    center=index[h];pairs=[];used={center}
    for i,v in enumerate(points):
        if i in used:continue
        j=index[tuple((2*a-b)%3 for a,b in zip(h,v))]
        pairs.append((i,j));used|={i,j}
    assert len(pairs)==4
    for choices in product((0,1),repeat=4):
        support=sum((1<<a)+(1<<b) for choice,(a,b) in zip(choices,pairs) if choice)
        if support:known.setdefault(support,[]).append(center)
survivors=[];excluded=[]
for support in range(1,512):
    witness=None
    for x,cs in coeffs:
        terms=[c for c,t in cs if t & ~support==0]
        if len(terms)==1:
            witness={'x':hex(x),'c':hex(terms[0])};break
    if witness is None:survivors.append(support)
    else:excluded.append({'support':support,'single_monomial_witness':witness})
out={'status':'EXACT_SUPPORT_PROBE_COMPLETE','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-start,'support_count':511,
     'survivor_counts_by_size':dict(sorted(Counter(x.bit_count() for x in survivors).items())),
     'known_counts_by_size':dict(sorted(Counter(x.bit_count() for x in known).items())),
     'surviving_supports':survivors,'known_symmetric_supports':known,
     'outside_known':[x for x in survivors if x not in known],
     'known_missing':[x for x in known if x not in survivors],
     'excluded_supports':excluded,
     'dependency_sha256':hashlib.sha256(dependency.read_bytes()).hexdigest(),
     'scope':'Each recorded excluded support has one exact determinant coefficient consisting of a single nonzero monomial on that torus. Surviving support is necessary only; coefficient ratios remain to be classified. No Clifford or actual Cartier bridge is assumed.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','actual_utc','runtime_seconds','survivor_counts_by_size','known_counts_by_size','outside_known','known_missing')}))
