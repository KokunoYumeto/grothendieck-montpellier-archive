#!/usr/bin/env python3
"""Exact finite certificate pi_3(D_2^{4,1}(Z)) = Z/2."""
from pathlib import Path
source=Path('SA08_work/code/D_tail_integral_horizontal.py').read_text()
exec(compile(source.split('\nrows=[]\n')[0], 'D_tail_integral_horizontal.py','exec'))
from itertools import combinations
from math import gcd
ds={n:differential(4,n,2) for n in range(1,5)}
for n in range(2,5):assert ds[n-1]*ds[n]==sp.zeros(ds[n-1].rows,ds[n].cols)
A=ds[4];assert A.shape==(12,4)
g4=0;minor_count=0
for I in combinations(range(12),4):
    g4=gcd(g4,abs(int(A.extract(I,range(4)).det())));minor_count+=1
assert g4==2
unit3=None
for I in combinations(range(12),3):
    for J in combinations(range(4),3):
        det=int(A.extract(I,J).det())
        if abs(det)==1:unit3={'rows':I,'columns':J,'determinant':det};break
    if unit3:break
assert unit3
B=ds[3]
columns=B.rref()[1]
assert len(columns)==8
rows=B[:,columns].T.rref()[1]
det8=int(B.extract(rows,columns).det());assert det8!=0
# rank B >=8 by this minor and <=8 because A has rank4 and BA=0.
out={'statement':'pi_3(D_2^{4,1}(Z))=Z/2',
     'normalized_bases':{n:[{'multidegree':a,'basis':M.tolist(),'offset':o} for a,M,o in basis(4,n,2)[0]] for n in range(1,5)},
     'differentials':{n:ds[n].tolist() for n in ds},
     'd4_four_minors_checked':minor_count,'d4_four_minor_gcd':g4,
     'd4_unit_three_minor':unit3,
     'd3_rank_eight_minor':{'rows':rows,'columns':columns,'determinant':det8},
     'proof':'The d4 Smith factors are 1,1,1,2 by the determinantal divisors. Since rank(d3)=8, H3 has free rank 12-8-4=0. Its torsion is that of coker(d4), namely Z/2, because its quotient im(d3) is free.',
     'elapsed_seconds':time.perf_counter()-started}
def conv(x):
    if isinstance(x,sp.Integer):return int(x)
    raise TypeError(type(x))
Path('SA08_work/logs/D_tail_H3_certificate.json').write_text(json.dumps(out,indent=2,default=conv)+'\n')
print(json.dumps({'det4_gcd':g4,'unit3':unit3,'rank8_minor':det8,'elapsed_seconds':out['elapsed_seconds']}))
