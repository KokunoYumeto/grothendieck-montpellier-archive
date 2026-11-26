"""Independent F2 boundary calculation; reads no projected tensor arrays."""
from pathlib import Path
import hashlib,itertools,json

W=Path(__file__).resolve().parents[1]
ip=W/'outputs/sh_cauchy_spin_sector_f2.json';d=json.loads(ip.read_text())
ports=[[j for j in range(4)if j!=i]for i in range(4)]
cov=[(1,2),(2,4),(6,5),(5,3)]

def target():
    return [(s+i,ports[i].index(j),s+j,ports[j].index(i))
            for s in(0,4)for i in range(4)for j in range(i+1,4)]

def crown(p):
    return [(i,ports[i].index(j),4+p[j],ports[p[j]].index(p[i]))
            for i in range(4)for j in range(4)if i!=j]

def functional(edges):
    ans=0
    for z in d['witness_rows']:
        rows=[(z >> (2*v)) & 3 for v in range(8)]
        for branch in range(256):
            bits=[cov[rows[v]][(branch>>v)&1]for v in range(8)]
            ans^=int(all(((bits[u]>>a)&1)!=((bits[v]>>b)&1)for u,a,v,b in edges))
    return ans

values=[functional(crown(p))for p in itertools.permutations(range(4))]
h=functional(target());assert values==[0]*24 and h==1
out={'status':'PASS independent F2 boundary-coefficient functional',
     'input_sha256':hashlib.sha256(ip.read_bytes()).hexdigest(),
     'witness_rows':d['witness_rows'],'crown_values_mod2':values,'target_value_mod2':h,
     'scope':'cyclic symmetric projector and its complement only; arbitrary noncentral maps remain open'}
p=W/'outputs/sh_cauchy_spin_sector_f2_verified.json';t=p.with_suffix('.json.tmp')
t.write_text(json.dumps(out,separators=(',',':'))+'\n');t.replace(p)
print(json.dumps(out,indent=2))
