"""Certificate with A11=x1; no higher-degree ambient equality is inferred."""
from pathlib import Path
from random import Random
from datetime import datetime,timezone
import json
source=Path(__file__).with_name('check_per3_binary_transverse_jacobian.py');ns={'__file__':str(source)}
exec(source.read_text().split('r=7;p=1000003;')[0],ns)
r=7;prime=1000003;rng=Random(250526);trials=[]
for trial in range(5):
 A=[[[rng.randint(-4,4) for k in range(r)] for j in range(3)] for i in range(3)];A[0][0]=[1,0,0,0,0,0,0]
 target,J=ns['jacobian'](A,r);reduced=[row[7:] for row in J];rank,cols,det=ns['echelon'](reduced,prime)
 result={'trial':trial,'rank':rank,'target_dimension':len(target),'source_columns':56};trials.append(result)
 if rank==len(target):
  output={'date_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root/verify_new_jets; GPT-6 Astra Pro; effort not exposed','run':'GCT_KRON_20261120','scope':'Only the base degree3 projected permanent coefficient map is certified here; no ambient equality after padding is inferred.','prime':prime,'status':'FULL RANK','fixed_entry':'A11=x1','pencil_coefficients':A,'target_monomials':target,'pivot_source_columns':[c+7 for c in cols],'selected_minor_mod_prime':det,'Jacobian':J,'trials':trials}
  p=source.with_name('per3_fixed_entry_transverse_certificate.json');p.write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(result));break
else:raise AssertionError('No full rank witness found')
