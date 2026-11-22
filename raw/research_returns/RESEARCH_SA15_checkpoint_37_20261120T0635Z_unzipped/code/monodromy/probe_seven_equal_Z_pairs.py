"""Finite diagnostic for collision pairs with equal residual Z."""
from pathlib import Path
import json,datetime
from sympy.polys.rings import ring
from gf16_exact_domain import K16,F16
r=Path(__file__).resolve().parent.parent
g=json.loads((r/'outputs/verify_seven_finite_collision_graph.json').read_text())
c=json.loads((r/'outputs/probe_seven_finite_mumford.json').read_text())
R,p=ring('p',K16)
build=lambda rows:sum((p**e*F16(v) for e,v in rows),R.zero)
P=build(g['sparse_eliminant']);q=build(g['sparse_partner'])
Z=build(c['sparse_integer_coordinates']['Z']['numerator'])/F16(c['sparse_integer_coordinates']['Z']['denominator'][0][1])
red=lambda f:f.div([P])[1]
zq=sum((red(q**e[0])*v for e,v in Z.items()),R.zero)
h=P.gcd(red(Z+zq))
result={'status':'COMPLETED_DIAGNOSTIC','equal_Z_collision_degree':h.degree(p),'polynomial':str(h),'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(r/'outputs/probe_seven_equal_Z_pairs.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
