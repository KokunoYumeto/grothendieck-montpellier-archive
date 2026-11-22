"""Exact small-field flags illustrating the two false degree-one source cases.

The geometric identification with final flag fibres is the separately checked
Ekdahl--van der Geer Section7 and Corollary8.4. This finite program checks the
actual line counts at p=2, not the geometric specialization argument.
"""
from pathlib import Path
import json, time
start=time.perf_counter()
def mul4(a,b):
    c=0
    for i in range(2):
        if (b>>i)&1:c^=a<<i
    if c&4:c^=7
    return c
def sq4(a):return mul4(a,a)
lines2=[(1,0),(0,1),(1,1)]
assert len(set(lines2))==3
ordinary=[v for v in lines2 if v==tuple(x*x for x in v)]
mixed=[v for v in lines2 if (v[0],0)==v]
nilpotent=[v for v in lines2 if (v[1],0)==(0,0)]
lines4=[(1,z) for z in range(4)]+[(0,1)]
hermitian=[v for v in lines4
           if mul4(sq4(v[0]),v[0])^mul4(sq4(v[1]),v[1])==0]
assert len(ordinary)==3 and len(mixed)==len(nilpotent)==1
assert hermitian==[(1,1),(1,2),(1,3)]
out={'status':'PASS','prime':2,
     'ordinary_F2_rational_lines':ordinary,'ordinary_degree':len(ordinary),
     'mixed_required_toral_line':mixed,'mixed_degree':len(mixed),
     'nilpotent_rank_one_kernel_line':nilpotent,'p_rank_zero_a_one_degree':len(nilpotent),
     'F4_polynomial':'z^2+z+1','superspecial_hermitian_isotropic_lines':hermitian,
     'superspecial_degree':len(hermitian),
     'source_correction':'Example12.2 p624 cannot assign degree1 to all four final covers: at p2 the ordinary and superspecial fibres have3 flags. Only the two middle degree1 cases are used.',
     'scope':'Finite line counts only; primary flag-fibre identifications and all monodromy conclusions are separate proofs.',
     'runtime_seconds':time.perf_counter()-start}
dest=Path(__file__).resolve().parents[1]/'outputs/ppav_flag_degree_source_correction.json'
assert not dest.exists()
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
