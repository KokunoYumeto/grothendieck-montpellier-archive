"""Exact finite p=2,3+2 parabolic supplement; not a geometric realization."""
from pathlib import Path
from itertools import product
from datetime import datetime, timezone
import json, time

started=time.perf_counter()
def rank(rows,n):
    basis=[0]*n
    count=0
    for row in rows:
        while row:
            j=row.bit_length()-1
            if basis[j]: row ^= basis[j]
            else:
                basis[j]=row
                count+=1
                break
    return count

def action(rows,v):
    return sum(((row & v).bit_count() & 1)<<i for i,row in enumerate(rows))

def transpose(rows,n):
    return tuple(sum(((rows[i]>>j)&1)<<i for i in range(n)) for j in range(n))

gl3=[rows for rows in product(range(8),repeat=3) if rank(rows,3)==3]
gl2=[rows for rows in product(range(4),repeat=2) if rank(rows,2)==2]
assert len(gl3)==168 and len(gl2)==6
members=set()
for A in gl3:
    for D in gl2:
        for B in range(64):
            rows=tuple(A[i] | (((B>>(2*i))&3)<<3) for i in range(3))
            rows += tuple(row<<3 for row in D)
            assert rank(rows,5)==5
            assert rows[3]&7==0 and rows[4]&7==0
            members.add(rows)
assert len(members)==168*6*64==64512
gl5_order=1
for i in range(5): gl5_order*=32-(1<<i)
assert gl5_order==9999360 and len(members)<gl5_order

identity=tuple(1<<i for i in range(5))
generators=[]
for i in range(5):
    for j in range(5):
        if i==j or (i>=3 and j<3): continue
        rows=list(identity)
        rows[i]^=1<<j
        rows=tuple(rows)
        assert rows in members
        assert rank(tuple(rows[k]^identity[k] for k in range(5)),5)==1
        generators.append(rows)
assert len(generators)==14
fixed=[v for v in range(32) if all(action(g,v)==v for g in generators)]
fixed_dual=[v for v in range(32) if all(action(transpose(g,5),v)==v for g in generators)]
assert fixed==[0] and fixed_dual==[0]
large_block={A+tuple(row<<3 for row in (1,2)) for A in gl3}
assert len(large_block)==168 and large_block<=members
escape=list(identity)
escape[3]^=1
assert tuple(escape) not in members and action(tuple(escape),1)&24

out={
 'status':'PASS',
 'actual_utc':datetime.now(timezone.utc).isoformat(),
 'runtime_seconds':time.perf_counter()-started,
 'parameters':{'p':2,'r':3,'s':2,'d':5},
 'counts':{'GL3':len(gl3),'GL2':len(gl2),'all_parabolic_members':len(members),
           'GL5_order':gl5_order,'elementary_generators':len(generators),
           'large_GL3_block':len(large_block)},
 'fixed_vectors':fixed,'fixed_covectors':fixed_dual,
 'proper_invariant_subspace_dimension':3,
 'scope':'All 64512 finite matrices have rank5 and preserve the first3 coordinates. Elementary generators leave only zero fixed in the natural and dual modules. The full GL3 natural block is present and a displayed invertible matrix outside the parabolic proves properness. No geometric realization or infinite p-adic density is inferred from this finite check; those scopes are separated in the written proof.'}
output=Path(__file__).resolve().parents[1]/'outputs/rational_residual_parabolic.json'
assert not output.exists()
output.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
