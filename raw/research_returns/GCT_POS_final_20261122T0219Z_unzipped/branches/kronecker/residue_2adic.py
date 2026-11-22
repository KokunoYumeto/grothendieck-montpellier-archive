"""Exact ramified 2-adic valuations of the already certified n=5 residues.

This is a diagnostic of cancellation, not an all-dimensional theorem.
For pi=1-zeta_16, v_pi(2)=8.  If a=sum b_j*pi^j, 0<=j<8,
the nonzero terms have distinct valuations modulo8, so the minimum is exact.
"""
from fractions import Fraction as F
from math import comb
from collections import Counter
from pathlib import Path
import json

root=Path(__file__).resolve().parent
data=json.loads((root/'n5_residue_verified.json').read_text())

def v2(n):
    n=abs(n)
    assert n
    return (n&-n).bit_length()-1

def valuation(a):
    a=list(map(F,a))
    b=[(-1)**j*sum(a[i]*comb(i,j) for i in range(j,8)) for j in range(8)]
    return min(j+8*(v2(x.numerator)-v2(x.denominator)) for j,x in enumerate(b) if x)

out=[]
for row in data['locals']:
    j=row['index'];m=row['ordered_factor_multiplicity']
    v=valuation(row['local_coefficient_basis'])
    out.append({'index':j,'local_valuation':v,'multiplicity':m,
                'weighted_valuation':v+8*v2(m)})
chain=next(row for row in data['locals'] if row['ordered_factor_multiplicity']==1)
rest=[F(a)-F(b) for a,b in zip(data['residue_basis'],chain['local_coefficient_basis'])]
minimum=min(row['weighted_valuation'] for row in out)
result={'scope':'Exact diagnostic of the K-014 residue; no extrapolation in n',
        'normalization':'pi=1-zeta16; v_pi(2)=8',
        'total_valuation':valuation(data['residue_basis']),
        'chain_index':chain['index'],
        'chain_valuation':valuation(chain['local_coefficient_basis']),
        'nonchain_total_valuation':valuation(rest),
        'minimum_weighted_valuation':minimum,
        'minimum_weighted_indices':[row['index'] for row in out if row['weighted_valuation']==minimum],
        'weighted_histogram':dict(Counter(row['weighted_valuation'] for row in out)),
        'rows':out}
assert (result['total_valuation'],result['chain_valuation'],result['nonchain_total_valuation'])==(-117,-99,-117)
assert result['minimum_weighted_indices']==[3,4,5,6]
(root/'residue_2adic.json').write_text(json.dumps(result,indent=2))
print('PASS exact n5 valuations: total -117, chain -99, nonchain -117; weighted minimum -123 at3,4,5,6')
