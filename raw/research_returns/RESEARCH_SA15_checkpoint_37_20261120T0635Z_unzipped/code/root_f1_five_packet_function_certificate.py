"""Independent exact F4 norm identity for the explicit two-rank-one five packet."""
from pathlib import Path
import datetime, hashlib, json, time
start=time.perf_counter()
w=Path(__file__).resolve().parents[1]
out=w/'outputs/root_f1_five_packet_function_certificate.json'
assert not out.exists()
def mul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return z
def norm(a):
    a=list(a)
    while a and a[-1]==0:a.pop()
    return a
def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]^=x
    for i,x in enumerate(b):c[i]^=x
    return norm(c)
def pmul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]^=mul(x,y)
    return norm(c)
omega=2
assert mul(omega,omega)^omega^1==0
curve=[0,1,0,1,0,1]      # v^2+z^2*v=z^5+z^3+z
qpoly=[1,1,omega]         # f=v+qpoly
norm_f=add(curve,add(pmul(qpoly,qpoly),pmul([0,0,1],qpoly)))
power=[1]
for unused in range(5):power=pmul(power,[1,1])
assert norm_f==power==[1,1,0,0,1,1]
assert omega^qpoly[0]^qpoly[1]^qpoly[2]==0
assert (omega^1)^qpoly[0]^qpoly[1]^qpoly[2]==1
result={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-start,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'field_modulus':'omega^2+omega+1','original_curve':'y^2+x*y=x^5+x^3+x',
        'Q':[0,0],'P':[1,2],'P_hyperelliptic':[1,3],
        'coordinates':'z=1/x, v=y/x^3',
        'function':'v+omega*z^2+z+1','norm_coefficients_ascending':norm_f,
        'norm':'(z+1)^5','value_at_P':0,'value_at_hyperelliptic_P':1,
        'scope':'Exact polynomial identity and evaluations only. The divisor/polarization interpretation is proved separately.'}
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
