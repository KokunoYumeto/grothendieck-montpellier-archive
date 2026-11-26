"""Exact F2 witness for the full four-dimensional local mixed sector."""
from pathlib import Path
import hashlib,json
import numpy as np

W=Path(__file__).resolve().parents[1]
ip=W/'inputs/sh_cauchy_spin_sector_f2.json';cfg=json.loads(ip.read_text())
ap=W/cfg['arrays_input'];data=np.load(ap)
C=np.stack([x.ravel(order='F')for x in data['crowns']])%2
h=data['target'].ravel(order='F')%2
piv={};witness=None
for i in range(len(h)):
    word=sum(int(C[j,i])<<j for j in range(24))|(int(h[i])<<24)
    comb=1<<i
    while word&((1<<24)-1):
        bits=word&((1<<24)-1);p=(bits&-bits).bit_length()-1
        if p in piv:
            row,mask=piv[p];word^=row;comb^=mask
        else:piv[p]=(word,comb);break
    else:
        if word>>24&1:
            witness=[j for j in range(i+1)if comb>>j&1];break
assert witness is not None
assert all(int(sum(C[j,i] for i in witness)) % 2 == 0 for j in range(24))
assert int(sum(h[i]for i in witness))%2==1
out={'status':'PASS exact F2 full-mixed-sector obstruction',
     'input_sha256':hashlib.sha256(ip.read_bytes()).hexdigest(),
     'arrays_sha256':hashlib.sha256(ap.read_bytes()).hexdigest(),
     'coordinate_convention':'z=sum_v(local_row_v*4^v), local rows R1_0,R1_1,R2_0,R2_1',
     'witness_rows':witness,'crown_values_mod2':[0]*24,'target_value_mod2':1,
     'scope':'arbitrary many terms with local central cyclic-symmetric/complement projectors; noncentral multiplicity action not excluded'}
p=W/cfg['output'];t=p.with_suffix('.json.tmp');t.write_text(json.dumps(out,separators=(',',':'))+'\n');t.replace(p)
print(json.dumps(out,indent=2))
