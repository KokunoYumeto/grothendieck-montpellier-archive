"""Exact finite-field exploration in the nonconcurrent full-torus chart.

Any actual point is a certificate.  Failure to find points is not a theorem.
"""
from pathlib import Path
from datetime import datetime,timezone
from itertools import product
import json,time
start=time.perf_counter()
root=Path(__file__).resolve().parents[3]
table=json.loads((root/'outputs/root_Moore_Fermat_fulltorus_normalized_coefficients.json').read_text())
all_records=[]
for bits,modulus in [(3,0b1011),(6,0b1000011)]:
    q=1<<bits
    def mul(a,b):
        r=0
        while b:
            if b&1:r^=a
            b>>=1;a<<=1
            if a&q:a^=modulus
        return r
    mt=[[mul(a,b) for b in range(q)] for a in range(q)]
    def power(a,n):
        r=1
        while n:
            if n&1:r=mt[r][a]
            a=mt[a][a];n>>=1
        return r
    assert all(power(a,q-1)==1 for a in range(1,q))
    inv=[0]+[power(a,q-2) for a in range(1,q)]
    cubes=[power(a,3) for a in range(q)]
    roots={a:[] for a in range(q)}
    for a in range(1,q):roots[cubes[a]].append(a)
    counts={'parameter_pairs':0,'root_choices':0,'nonzero_I1_denominator':0,
            'I2_pass':0,'I3_pass':0,'I4_pass':0,'all_67_coefficients_pass':0}
    survivors=[]
    for a,b in product(range(1,q),repeat=2):
        ur,vr,wr,tr=roots[1^cubes[a]],roots[cubes[a]^cubes[b]],roots[1^cubes[b]],roots[1^cubes[a]^cubes[b]]
        if not all((ur,vr,wr,tr)):continue
        counts['parameter_pairs']+=1
        for u,v,w,t in product(ur,vr,wr,tr):
            counts['root_choices']+=1
            r=mt[b][v]^mt[w][t]
            if not r:continue
            counts['nonzero_I1_denominator']+=1
            d=mt[mt[a][u]][inv[r]]
            assert d
            if mt[b][w]^mt[d][mt[a][t]^mt[u][v]]:continue
            counts['I2_pass']+=1
            if mt[v][t]^mt[d][mt[a][b]^mt[u][w]]:continue
            counts['I3_pass']+=1
            if mt[d][d]^mt[mt[b][u]][t]^mt[mt[a][v]][w]:continue
            counts['I4_pass']+=1
            c=[1,a,u,b,d,v,w,t,d]
            cp=[[power(value,j) for j in range(10)] for value in c]
            values=[]
            for item in table:
                val=0
                for exponent in item['terms']:
                    term=1
                    for i,e in enumerate(exponent):term=mt[term][cp[i][e]]
                    val^=term
                values.append(val)
            if not any(values):counts['all_67_coefficients_pass']+=1
            survivors.append({'c':c,'nonzero_coefficients':[(i,val) for i,val in enumerate(values) if val]})
    all_records.append({'field_size':q,'binary_modulus':modulus,'counts':counts,'five_cubic_survivors':survivors})
out={'status':'EXACT_FINITE_PROBE_COMPLETE','actual_utc':datetime.now(timezone.utc).isoformat(),
     'runtime_seconds':time.perf_counter()-start,'records':all_records,
     'scope':'Only F8 and F64 points in the normalized full-torus chart were tested. No emptiness, ideal-radical or geometric conclusion is inferred from absence of points.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('status','actual_utc','runtime_seconds')},indent=2))
for record in all_records:print(json.dumps({'field_size':record['field_size'],'counts':record['counts'],'first_survivor':record['five_cubic_survivors'][:1]},indent=2))
