"""Exact arithmetic audit of NN-G031, not a substitute for its polynomial proof."""
from fractions import Fraction
from pathlib import Path
import json

cap=11128
pairs=[(u,v) for u in range(4,10,2) for v in range(4,10,2) if u*v<36]
assert pairs==[(4,4),(4,6),(4,8),(6,4),(8,4)]
possible=[]
for d1 in range(4,24,2):
    for d2 in range(4,24-d1,2):
        g1=Fraction(12*(3*d1+2*d2),5)
        g2=Fraction(12*(2*d1+3*d2),5)
        if g1.denominator!=1 or g2.denominator!=1:
            continue
        if g1%48==0 and g2%24==0 and int(g2/24)%2==1:
            possible.append((d1,d2,int(g1),int(g2)))
assert possible==[(4,14,96,120),(16,6,144,120)]
values={
    'u_contains8_mass_lower_bound':20*(240+336),
    'u6_4_at_t16':16*16**2+432*16+1520,
    'u4_6_at_t14':16*14**2+458*14+2696,
    'u4_4_at_t24':str(Fraction(144,25)*24**2+266*24+2336),
    'last_candidate_mass_lower_bound':2880+5280+1200+160+572+784+544,
}
assert all(Fraction(x)>cap for x in values.values())
assert (576-16)//20==28 and (576-16)%40==0
out={'mass_cap':cap,'possible_u_pairs':pairs,
     'u4_4_remaining_scalar_tuples':possible,
     'strict_exclusion_lower_bounds':values,
     'scope':'Arithmetic audit only. Integral-polynomial divisibility and parity exclusions are proved in NN-G031; no global optimum is claimed.'}
Path('work/gct/gluing_mass6_exclusion_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
