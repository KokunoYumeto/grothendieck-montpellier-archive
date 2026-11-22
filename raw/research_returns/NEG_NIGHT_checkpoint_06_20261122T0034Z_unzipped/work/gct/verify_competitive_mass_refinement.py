"""Finite projection and exact polynomial identities for the NN-G036 addendum.
Uniform irreducibility, divisibility and parity exclusions are written proofs.
"""
from pathlib import Path
import json
import sympy as sp

source=json.loads(Path('work/gct/closed_mass_gate_2744_certificate.json').read_text())
def newly_excluded(r):
    return ((r['w']==8 and (r['g1'],r['d1'],r['u1']) in [(72,6,4),(80,8,4)])
            or (r['w']==10 and r['g1']==r['g2']==80)
            or (r['w']==8 and r['g1']==r['g2']==96)
            or (r['w']==10 and sorted([r['g1'],r['g2']])==[76,100]))
previous=[r for r in source['bases'] if r['g1']>64]
removed=[r for r in previous if newly_excluded(r)]
rows=[r for r in previous if not newly_excluded(r)]
assert len(previous)==38 and len(removed)==12 and len(rows)==26
assert sum(len(r['allowed_auxiliary_increment_pairs']) for r in rows)==42
triples=sorted({(r['g1'],r['d1'],r['u1']) for r in rows})
assert len(triples)==15 and min(r['score_min'] for r in rows)==2572

D,q,a,b,c,d=sp.symbols('D q a b c d')
T1=D-2;T2=D**2-4*D+2;T3=D**3-6*D**2+9*D-2
T4=D**4-8*D**3+20*D**2-16*D+2
W=2*D**2-7*D+4;psi=D*(D-3);H=W*(D-1)-psi
V=d+a*T1+b*T2+c*T3
A=sp.expand((D**2*H-D*(D-1)*V).subs(D,q+2+q**-1))
observed=[sp.expand(A.coeff(q,k).subs(d,26-2*a-2*b-2*c)) for k in range(4)]
expected=[-44+2*a+6*b+8*c,-24+a+3*b+5*c,14-a-2*b-c,24-a-3*b-4*c]
assert observed==expected
assert sp.expand(A.coeff(q,5))==2-c

N=sp.expand(D*(D+2)*(D**2-3*D+1))
assert N.subs(D,2)==-8
assert sp.rem(T3,T1,D)==0
assert sp.rem(N,T2,D)==16*D-10
assert sp.expand(N-T4)==7*D**3-25*D**2+18*D-2

out={'previous_base_rows':38,'newly_excluded_base_rows':12,
     'remaining_base_rows':26,'remaining_auxiliary_increment_pairs':42,
     'remaining_first_cell_mass_triples':triples,
     'necessary_closed_table_score_lower_bound':2572,'actual_upper_bound':2744,
     'mass80_auxiliary_coefficient_identities':[str(x) for x in observed],
     'asymmetric_divisibility_checks':{'N_at_2':-8,'remainder_mod_T2':'16*D - 10',
                                      'N_minus_T4':'7*D**3 - 25*D**2 + 18*D - 2'},
     'remaining_rows':rows,
     'scope':'Complete finite projection plus exact coefficient identities only. The addendum proves every arbitrary-degree exclusion; surviving mass data are not asserted realizable.'}
Path('work/gct/competitive_mass_refinement_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='remaining_rows'},indent=2))
