"""Exact postprocessing of the retained finite norm-seven collision basis.

This is a fixed-parameter certificate check, not a uniform nodality theorem.
"""
from pathlib import Path
import datetime, hashlib, json, time, traceback
from sympy.polys.rings import ring
from gf16_exact_domain import K16, F16, verify_field

start=time.perf_counter()
root=Path(__file__).resolve().parent.parent
result={"status":"RUNNING"}
try:
    field=verify_field()
    source=root/'outputs/probe_seven_finite_collisions.json'
    coordinates=root/'outputs/probe_seven_finite_mumford.json'
    data=json.loads(source.read_text()); coord=json.loads(coordinates.read_text())
    R,q,p=ring('q,p',K16,order='lex')
    env={'p':p,'q':q,**{f'u{i}':F16(i) for i in range(16)}}
    G=[eval(s,{'__builtins__':{}},env) for s in data['clean_basis']]
    assert len(G)==2 and G[0].degree(q)==1 and G[1].degree(q)==0
    partner=G[0]+q; P=G[1]
    assert P.degree(p)==48 and partner.degree(p)==44
    def red(f):return f.div([P])[1]
    def compose(f,at):
        out=R.zero
        for (eq,ep),c in f.items():
            assert not eq
            out+=c*red(at**ep)
        return red(out)
    assert P.gcd(P.diff(p)).degree(p)==0
    assert P.gcd(partner+p).degree(p)==0
    assert red(compose(partner,partner)+p)==0
    assert compose(P,partner)==0
    sparse=coord['sparse_integer_coordinates']
    def build(rows,var=p):return sum((var**e*F16(c) for e,c in rows),R.zero)
    Z=build(sparse['Z']['numerator'])/F16(sparse['Z']['denominator'][0][1])
    assert P.gcd(Z).degree(p)==0
    assert P.gcd(compose(Z,partner)).degree(p)==0
    for name in ('ell','constant','nu'):
        f=sparse[name]; n=build(f['numerator']); d=build(f['denominator'])
        assert P.gcd(d).degree(p)==0
        assert red(n*compose(d,partner)+compose(n,partner)*d)==0
    # The ordinate offset determines the only possible partner y-coordinate.
    f=sparse['eta_minus_y']; ne=build(f['numerator']); de=build(f['denominator'])
    assert P.gcd(de).degree(p)==0
    # Extended Euclid, with all polynomials independent of q.
    aa,bb=P,de;ta,tb=R.zero,R.one
    while bb:
        quotient,remainder=aa.div([bb])
        aa,bb=bb,remainder;ta,tb=tb,ta+quotient[0]*tb
    assert aa.degree(p)==0
    invde=ta/aa[(0,0)]
    assert red(invde*de)==1
    ep=red(ne*invde)
    offset=red(ep+compose(ep,partner))
    r,z,t,beta,w=map(F16,coord['choice_r_z_t_beta_w'])
    a=z*z; b=a+z+1
    assert red(offset**2+offset+a*(p**5+partner**5)+b*(p**3+partner**3))==0
    # Retain sparse coefficients so no string parsing is needed by later checks.
    serial=lambda f:[[e[1],int(c)] for e,c in sorted(f.items(),reverse=True)]
    result={
      'status':'PASS_FIXED_PARAMETER_GRAPH',
      'field_checks':field,
      'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
      'coordinates_sha256':hashlib.sha256(coordinates.read_bytes()).hexdigest(),
      'choice_r_z_t_beta_w':coord['choice_r_z_t_beta_w'],
      'eliminant_degree':48,'partner_degree':44,
      'squarefree':True,'partner_fixed_point_free':True,'partner_involution':True,
      'all_three_coordinates_preserved':True,'ordinate_offset_preserves_curve':True,
      'sparse_eliminant':serial(P),'sparse_partner':serial(partner),'sparse_ordinate_offset':serial(offset),
      'scope':'Postprocessing of one exact finite-parameter Groebner calculation; a complete geometric proof and independent audit are still required.'}
except Exception:
    result={'status':'FAILURE','traceback':traceback.format_exc()}
result['actual_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
result['runtime_seconds']=time.perf_counter()-start
(root/'outputs/verify_seven_finite_collision_graph.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
