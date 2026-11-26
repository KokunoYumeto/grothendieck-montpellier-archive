"""Exact universal rank certificates: unit minors and vanishing larger minors."""
from pathlib import Path
from itertools import combinations,product
import json,hashlib
import sympy as sp
W=Path(__file__).resolve().parents[1]
p=W/'inputs/rt_universal_rank_witness.json';d=json.loads(p.read_text())
A=sp.diag(1,0,0);B=sp.diag(0,1,0)
C,R,S=map(sp.Matrix,(d['C'],d['R'],d['S']))
points=[(x*A+y*B if z==0 else C+x*R+y*S)
        for z in range(2)for y in range(2)for x in range(2)]
cert=[]
for i,j in combinations(range(8),2):
    X=points[i]-points[j];rank=d['rank_by_xor_label'][i^j]
    unit=None;larger=0
    for rows in combinations(range(3),rank):
        for cols in combinations(range(3),rank):
            determinant=int(X.extract(rows,cols).det())
            if abs(determinant)==1 and unit is None:
                unit={'rows':rows,'columns':cols,'determinant':determinant}
    assert unit is not None
    for rows in combinations(range(3),rank+1):
        for cols in combinations(range(3),rank+1):
            assert X.extract(rows,cols).det()==0;larger+=1
    cert.append({'pair':[i,j],'rank':rank,'unit_minor':unit,'larger_minors_checked_zero':larger})
u,v,x,y=sp.symbols('u v x y')
X=C+x*R+y*S-u*A-v*B
expected=u+x-2*u*x-v-y+2*v*y
assert sp.expand(X.det()-expected)==0
assert sp.expand(X.extract([0,2],[0,2]).det()-(1-2*y))==0
out={'status':'PASS over every field','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'matrices':[[list(map(int,row))for row in P.tolist()]for P in points],
     'cross_determinant':str(expected),'fixed_cross_minor':'1-2*y',
     'pair_certificates':cert,'unordered_pairs_checked':28,
     'interpretation':'Unit minors survive every characteristic; all larger minors vanish as integers.'}
(W/'outputs/rt_universal_rank_witness.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in('matrices','pair_certificates')},indent=2))
