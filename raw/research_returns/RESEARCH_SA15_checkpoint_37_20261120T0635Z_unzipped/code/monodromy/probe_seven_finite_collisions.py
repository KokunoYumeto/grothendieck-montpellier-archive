"""Bounded finite-parameter collision elimination; no universal claim."""
from pathlib import Path
import datetime,hashlib,json,signal,time,traceback
from sympy import Poly,symbols
from sympy.polys.agca.extensions import MonogenicFiniteExtension
from sympy.polys.rings import ring
from sympy.polys.groebnertools import groebner
from gf16_exact_domain import K16,F16,verify_field

start=time.perf_counter()
root=Path(__file__).resolve().parent.parent
source=root/'outputs/probe_seven_finite_mumford.json'
data=json.loads(source.read_text())
result={'status':'RUNNING'}
def timeout(*unused):
    raise TimeoutError('Collision elimination exceeded 60 seconds')
signal.signal(signal.SIGALRM,timeout);signal.alarm(60)
try:
    field_checks=verify_field()
    K=K16
    vals=[F16(n) for n in range(16)]
    R,q,p=ring('q,p',K,order='lex')
    def build(rows,var):
        return sum((var**e*vals[c] for e,c in rows),R.zero)
    polynomials=[]
    for name in ('ell','constant','nu'):
        f=data['sparse_integer_coordinates'][name]
        numerator=build(f['numerator'],p)*build(f['denominator'],q)+build(f['numerator'],q)*build(f['denominator'],p)
        quotient,remainder=numerator.div([p+q]);assert not remainder
        polynomials.append(quotient[0])
    print(json.dumps({'stage':'input','total_degrees':[max(map(sum,f.keys())) for f in polynomials],'term_counts':[len(f) for f in polynomials]}),flush=True)
    G=groebner(polynomials,R,method='f5b')
    print(json.dumps({'stage':'first_groebner','basis_size':len(G),'degrees':[[g.degree(q),g.degree(p)] for g in G]}),flush=True)
    eliminant=next(g for g in G if g.degree(q)==0)
    Z=build(data['sparse_integer_coordinates']['Z']['numerator'],p)
    clean=eliminant
    while True:
        h=clean.gcd(Z)
        if h.degree(p)<=0:break
        clean=clean.exquo(h)
    G2=groebner(G+[clean],R,method='f5b')
    result={
        'status':'COMPLETED_FINITE_ELIMINATION',
        'field_checks':field_checks,
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'choice_r_z_t_beta_w':data['choice_r_z_t_beta_w'],
        'raw_basis':[str(g) for g in G],
        'clean_basis':[str(g) for g in G2],
        'raw_eliminant_degree':eliminant.degree(p),
        'clean_eliminant_degree':clean.degree(p),
        'scope':'A single finite-parameter rational-coordinate collision elimination; no uniform theta nodality or monodromy inference.',
    }
except Exception:
    result={'status':'EXPLORATORY_FAILURE','traceback':traceback.format_exc()}
finally:
    signal.alarm(0)
    result['actual_timestamp_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    result['runtime_seconds']=time.perf_counter()-start
    (root/'outputs/probe_seven_finite_collisions.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
