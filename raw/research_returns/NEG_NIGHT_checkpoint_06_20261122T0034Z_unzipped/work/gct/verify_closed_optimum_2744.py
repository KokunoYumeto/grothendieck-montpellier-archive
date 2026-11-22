"""Complete final projection of the NN-G035 mass gate.

Uniform proofs in NN-G036, not bounded support enumeration, justify each
deletion. The actual attainer and its uniqueness are the separate
NN-G033/NN-G034 results, with their independently checked coefficients.
"""
from pathlib import Path
import json
import sympy as sp

source=json.loads(Path('work/gct/mass6_action_refinement_certificate.json').read_text())
rows=source['remaining_rows']
def lowest(r):
    return r['w']==12 and (
        (r['g1'],r['g2'],r['d1'],r['d2'],r['u1'],r['u2'])==(80,96,8,4,6,12)
        or (r['g1'],r['g2'],r['d1'],r['d2'],r['u1'],r['u2'])==(96,80,4,8,12,6)
    )
def reverse(r):
    return (r['w'],r['g1'],r['g2'],r['d1'],r['d2'],r['u1'],r['u2'])==(12,96,80,4,12,12,4)
def last(r):
    return (r['w'],r['g1'],r['g2'],r['s'],r['d1'],r['d2'],r['u1'],r['u2'])==(12,96,96,768,4,4,10,10)
assert len(rows)==4
assert len([r for r in rows if lowest(r)])==2
assert len([r for r in rows if reverse(r)])==1
assert len([r for r in rows if last(r)])==1
assert all(sum((lowest(r),reverse(r),last(r)))==1 for r in rows)
assert sum(len(r['allowed_auxiliary_increment_pairs']) for r in rows)==7
assert 768//4**4==3 and 768%4**4==0
assert all(64-u*v!=0 for u in (6,-2) for v in (6,-2))
D,q=sp.symbols('D q')
psi=D*(D-3)
bound=4*D**2*(D-1)**2
bottoms=[10*D**3*(D-3)**2,2*D**3*(3*D-7)]
central=lambda p:int(sp.expand(p.subs(D,q+2+q**-1)).coeff(q,0))
assert [central(bound)]+[central(p) for p in bottoms]==[144,120,140]
assert sp.expand((3-1)*5*D*psi-D*psi*(3*3+1))==0
H=2*D-5
Gminus=D**2*(3*D-7)
assert sp.expand((H-1)*Gminus-D*psi*(3*H+1))==0
attainer=json.loads(Path('work/gct/dimension_certificate_2744.json').read_text())
assert attainer['total_cancelling_pairs']==2744
assert all(v==0 for v in attainer['failures'].values())
out={
    'incoming_base_rows':4,
    'incoming_auxiliary_increment_pairs':7,
    'root_lowest_two_rows_removed':2,
    'root_reverse_row_removed':1,
    'last_equal_action_row_removed':1,
    'remaining_competitor_base_rows':0,
    'exact_closed_table_minimum':2744,
    'unique_parameter_realization_in_closed_presentation':True,
    'uniqueness_source':'NN-G034, plus NN-G036 forcing every competitive g1=64 row into that class and excluding all other mass rows.',
    'coefficient_check':[144,120,140],
    'scope':'Exact optimum only for the symmetric closed-table presentation. Uniform written proofs justify all degrees; extra-position tables remain open.'
}
Path('work/gct/closed_optimum_2744_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
