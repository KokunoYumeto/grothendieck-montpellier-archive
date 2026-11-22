"""Reconstruct the twenty explicit polarized five-self-isogeny kernels.

Reads the retained theta-packet census without modifying it. The algebraic
isogeny interpretation is proved separately; this exact check identifies
all kernel subspaces with the twenty geometrically good census planes.
"""
from pathlib import Path
from itertools import product
import json,time,datetime,hashlib
start=time.perf_counter(); root=Path(__file__).resolve().parent.parent
base=root/'outputs/nonordinary_five_theta_packet_probe.json'
old=base.read_bytes(); data=json.loads(old)
modulus=data['field_modulus']
def mul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&16:a^=modulus
    return z
def power(a,n):
    z=1
    while n:
        if n&1:z=mul(z,a)
        a=mul(a,a);n>>=1
    return z
points=[None]+[tuple(x) for x in data['curve_points'][1:]]
vec=[tuple(x) for x in data['curve_torsion_vectors']]
pointvec=dict(zip(points,vec)); basis=data['chosen_basis_indices']; J=data['symplectic_matrix']
def add(u,v):return tuple((x+y)%5 for x,y in zip(u,v))
def scale(c,u):return tuple(c*x%5 for x in u)
def encode(u):return sum(x*5**i for i,x in enumerate(u))
def matvec(M,u):return tuple(sum(M[i][j]*u[j] for j in range(4))%5 for i in range(4))
def span(u,v):return tuple(sorted(encode(add(scale(a,u),scale(b,v))) for a,b in product(range(5),repeat=2)))
good={span(*record['basis']) for record in data['lagrangians'] if record['good_nodal']}
records=[]; actual=set()
for alpha in range(1,16):
    r=power(alpha,5)
    if r in (0,1):continue
    assert power(r,2)^r==1
    for beta in range(16):
        if power(beta,2)^beta!=r:continue
        def image(P):
            if P is None:return None
            x,y=P
            return (x^alpha,y^mul(power(alpha,8),power(x,2))^mul(power(alpha,4),x)^beta)
        assert all(image(P) in pointvec for P in points)
        assert all(image(image(P))==(None if P is None else (P[0],P[1]^1)) for P in points)
        cols=[pointvec[image(points[j])] for j in basis]
        G=[[cols[j][i] for j in range(4)] for i in range(4)]
        assert all(matvec(G,u)==pointvec[image(P)] for P,u in zip(points,vec))
        assert all(matvec(G,matvec(G,u))==scale(4,u) for u in vec)
        assert all(sum(G[a][i]*J[a][b]*G[b][j] for a,b in product(range(4),repeat=2))%5==J[i][j] for i,j in product(range(4),repeat=2))
        K=tuple(sorted(encode(u) for u in product(range(5),repeat=4) if add(scale(2,u),matvec(G,u))==(0,0,0,0)))
        assert len(K)==25 and K in good
        actual.add(K); records.append({'alpha':alpha,'beta':beta,'matrix':G,'kernel':K})
assert len(records)==20 and len(actual)==20 and actual==good
assert base.read_bytes()==old
result={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'base_output_sha256':hashlib.sha256(old).hexdigest(),'automorphism_count':len(records),'distinct_kernel_count':len(actual),'equals_all_twenty_good_kernels':actual==good,'records':records,'scope':'Exact automorphism actions on the reconstructed J[5] symplectic space and equality of their kernels with the retained nodal census. Polarized endomorphism and geometric packet-exhaustion arguments are separate.'}
out=root/'outputs/nonordinary_five_theta_self_isogenies.json';out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
