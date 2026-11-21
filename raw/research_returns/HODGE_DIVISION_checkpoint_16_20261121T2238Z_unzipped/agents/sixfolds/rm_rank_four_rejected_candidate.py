from pathlib import Path
from datetime import datetime,timezone
import json
# In A=C[x,y,z,w]/(x²+yz,y²,z²,w²), the two relevant tuples are:
# P+12=P-12=4xy, P+14=2yw+2zw, P-14=2yw-2zw.
# y²=0 removes the shared-index product; xyzw is a nonzero basis monomial.
plus12=minus12=4
plus14_zw=2
minus14_zw=-2
coefficient=plus12*minus14_zw-minus12*plus14_zw
assert coefficient==-16
out={'status':'REJECTED_CANDIDATE_CONFIRMED','completed_utc':datetime.now(timezone.utc).isoformat(),'candidate_relations':['x²+yz','y²','z²','w²'],'ordered_cross_minor':['12','14'],'nonzero_socle_coefficient':coefficient,'reason':'Already fails the previous scalar companion consequence; not a strict witness.','refined_statement':'SF-E840 uses x²+yw and checks all36 scalar cross minors.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
