"""Reproduce the finite search that found the A16 example; not a moduli classification."""
from pathlib import Path
import json
import construct_theta15 as g

found=[];tested=0;models=0
for lead in range(1,8):
 for pole in range(1,8):
  for a in range(8):
   for c in (0,1):
    models+=1
    f=[0,lead,0,a,c,pole];g.f=f
    points=[(x,y) for x in range(1,8) for y in range(8)
            if g.mul(y,y)^g.mul(g.mul(x,x),y)==g.peval(f,x)]
    for x,y in points:
     tested+=1
     cert=g.torsion_function(x,y,15)
     if cert and not g.torsion_function(x,y,5):
      found.append(dict(f=f,point=[x,y],certificate=cert))
assert models==784 and tested==5488 and len(found)==84
result=dict(models=models,tested_nonbranch_rational_points=tested,
            field='F2[z]/(z^3+z+1)',exact_order15_instances=len(found),found=found,
            exact_order_scope='Nonzero classes; order3 excluded by nonordinary genus-two RR; order5 checked by Taylor system.',
            limitations='Models and points can be isomorphic or conjugate; no moduli classification or universal claim.')
Path(__file__).with_name('theta15_search_result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='found'},indent=2))
