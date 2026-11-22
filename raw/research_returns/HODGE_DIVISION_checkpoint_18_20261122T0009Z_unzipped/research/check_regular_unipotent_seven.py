"""Actual truncated-ring norm counts for the proposed Spin block refinement."""
from datetime import datetime,timezone
from pathlib import Path
from itertools import product
import json,time,hashlib
R=Path(__file__).resolve().parent
start=time.perf_counter();stamp=datetime.now(timezone.utc).isoformat()
def mul(a,b,q):
    return tuple(sum(a[i]*b[j-i] for i in range(j+1))%q for j in range(7))
def add(a,b,q):return tuple((x+y)%q for x,y in zip(a,b))
one=(1,0,0,0,0,0,0)
rows=[]
for q in (3,5):
    sigma_x=(0,)+tuple(((-1)**j)%q for j in range(1,7))
    powers=[one]
    for j in range(6):powers.append(mul(powers[-1],sigma_x,q))
    def sigma(a):
        out=(0,)*7
        for coefficient,power in zip(a,powers):
            out=add(out,tuple(coefficient*x%q for x in power),q)
        return out
    fixed=norm_one=0;norm_image=set()
    for tail in product(range(q),repeat=6):
        a=(1,)+tail;sa=sigma(a)
        assert sigma(sa)==a
        fixed+=sa==a
        norm=mul(a,sa,q)
        assert sigma(norm)==norm
        norm_one+=norm==one
        norm_image.add(norm)
    assert fixed==norm_one==len(norm_image)==q**3
    rows.append({'q':q,'unipotent_units':q**6,'fixed_units':fixed,
                 'norm_image':len(norm_image),'unipotent_norm_one':norm_one,
                 'orthogonal_centralizer_order':2*norm_one,
                 'special_orthogonal_centralizer_order':norm_one})
result={'status':'PASS','started_utc':stamp,'elapsed_seconds':time.perf_counter()-start,
        'rows':rows,'scope':'Finite exact rings F3[x]/x7 and F5[x]/x7. Universal odd-q norm-map count is a separate written argument; no character classification is inferred.',
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'regular_unipotent_seven_checked.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
