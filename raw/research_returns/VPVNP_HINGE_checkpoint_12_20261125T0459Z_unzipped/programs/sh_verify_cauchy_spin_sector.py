"""Independent boundary-coefficient verifier for the r4 sector obstruction.

Does not read the discovery program's projected arrays, use internal-edge
enumeration, or import symbolic/numerical linear algebra.
"""
from pathlib import Path
import hashlib,itertools,json

W=Path(__file__).resolve().parents[1]
ip=W/'outputs/sh_cauchy_spin_sector_probe.json';data=json.loads(ip.read_text())
weights=[1,1,2,2,1,1,2,2]
assert data['local_weights']==weights
rows=data['witness_rows'];coefs=data['witness_coefficients']
assert len(rows)==len(coefs)
ports=[[j for j in range(4)if j!=i]for i in range(4)]

def local(mask,index,branch):
    choices=([(1,1),(2,-1)],[(2,1),(4,-1)])
    x,c=choices[index][branch]
    return (7-x if mask==2 else x),c

def edges_target():
    return [(s+i,ports[i].index(j),s+j,ports[j].index(i))
            for s in(0,4)for i in range(4)for j in range(i+1,4)]

def edges_crown(p):
    return [(i,ports[i].index(j),4+p[j],ports[p[j]].index(p[i]))
            for i in range(4)for j in range(4)if i!=j]

def coordinate(edges,z):
    total=0
    for branch in range(256):
        boundary=[];coefficient=1
        for v in range(8):
            bitmask,c=local(weights[v],(z>>v)&1,(branch>>v)&1)
            boundary.append(bitmask);coefficient*=c
        for u,a,v,b in edges:
            x=(boundary[u]>>a)&1;y=(boundary[v]>>b)&1
            if x==y:coefficient=0;break
            if x:coefficient=-coefficient
        total+=coefficient
    return total

def functional(edges):
    return sum(c*coordinate(edges,z)for z,c in zip(rows,coefs)if c)

values=[functional(edges_crown(p))for p in itertools.permutations(range(4))]
target=functional(edges_target())
assert values==[0]*24 and target==16
out={'status':'PASS independent integer boundary-coefficient witness',
     'input_sha256':hashlib.sha256(ip.read_bytes()).hexdigest(),
     'nonzero_witness_rows':sum(c != 0 for c in coefs),
     'crown_functional_values':values,'target_functional_value':target,
     'field_scope':'central Sym3/complement projector ansatz excluded in characteristic zero or characteristic>3; no F2 conclusion from this witness'}
p=W/'outputs/sh_cauchy_spin_sector_verified.json';tmp=p.with_suffix('.json.tmp')
tmp.write_text(json.dumps(out,separators=(',',':'))+'\n');tmp.replace(p)
print(json.dumps(out,indent=2))
