#!/usr/bin/env python3
"""Exact finite certificate for the printed KM commutativity-sign error."""
from pathlib import Path
import datetime, itertools, json, time
start=time.perf_counter()
swap=((0,1),(1,0))
det_swap=swap[0][0]*swap[1][1]-swap[0][1]*swap[1][0]
printed=(-1)**(1+1)
koszul=(-1)**(1*1)
assert det_swap==koszul==-1 and printed==1
checks=[]
for a,b,c in itertools.product(range(2),repeat=3):
    lhs=(-1)**(a*(b+c))
    rhs=(-1)**(a*b)*(-1)**(a*c)
    assert lhs==rhs
    checks.append([a,b,c,lhs,rhs])
output={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'swap_determinant':det_swap,'printed_rank1_sign':printed,'correct_rank1_sign':koszul,'koszul_hexagon_parity_cases':checks,'counts':{'rank_two_swap':1,'parity_triples':8},'seconds':time.perf_counter()-start,'scope':'Exact rank-one swap refutes the printed alpha+beta sign; eight parity cases verify the bilinear sign identity only, not the full determinant theorem.'}
target=Path(__file__).with_name('part_c_determinant_sign_output.json')
target.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
