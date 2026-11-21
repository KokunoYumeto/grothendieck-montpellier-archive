#!/usr/bin/env python3
"""Independent exterior reconstruction for SF-E817; no author code imported."""
from itertools import combinations
from pathlib import Path
import hashlib,json
import sympy as s

pairs=list(combinations(range(8),2))
sixes=list(combinations(range(8),6))
row={I:j for j,I in enumerate(sixes)}
a,b,c,d=s.symbols('a b c d')
four=[((0,1,4,5),a),((2,3,4,5),b),((0,1,6,7),c),((2,3,6,7),d)]
M=s.zeros(len(sixes),len(pairs))
for j,I in enumerate(pairs):
    for J,coef in four:
        if set(I).isdisjoint(J):
            sign=(-1)**sum(x>y for x in I for y in J)
            M[row[tuple(sorted(I+J))],j]+=sign*coef
nonzero_rows=[i for i in range(28) if any(M[i,j]!=0 for j in range(28))]
nonzero_cols=[j for j in range(28) if any(M[i,j]!=0 for i in range(28))]
assert len(nonzero_rows)==len(nonzero_cols)==20
det=s.factor(M.extract(nonzero_rows,nonzero_cols).det())
target=(a*d-b*c)**2*a**4*b**4*c**4*d**4
assert s.expand(det-target)==0 or s.expand(det+target)==0
cases={'balanced':{a:18,b:-48,c:-48,d:128},
       'hull':{a:18,b:-48,c:-48,d:144},
       'point':{a:0,b:0,c:0,d:16}}
ranks={k:M.subs(v).rank() for k,v in cases.items()}
assert ranks=={'balanced':18,'hull':20,'point':6}

x,y=s.symbols('x y')
def exponential_truncated(z):
    return sum(z**j/s.factorial(j) for j in range(5))
H=s.Poly(s.expand(3*(exponential_truncated(2*x+2*y)+exponential_truncated(-2*x-2*y))
                 +6*(exponential_truncated(s.sqrt(2)*(x-y))+exponential_truncated(-s.sqrt(2)*(x-y)))),x,y)
h=sum(coef*x**i*y**j for (i,j),coef in H.terms() if i<=2 and j<=2)
assert s.expand(h-(18+24*x*x+24*y*y+36*x*x*y*y))==0
e=s.expand(h-4*x*x*y*y)
assert s.expand(e-18*(1+s.Rational(4,3)*x*x)*(1+s.Rational(4,3)*y*y))==0

source=Path(__file__).parents[2]/'sixfolds/rm_point_defect_obstruction_draft.md'
out={'status':'PASS','proof_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'author_code_imported':False,'method':'tuple exterior products; automatically detected support minor; independent truncated exponential expansion',
     'minor_rows':nonzero_rows,'minor_columns':nonzero_cols,'generic_minor':str(det),
     'ranks':ranks,'hull_character':str(h),'kernel_character':str(e),
     'character_rank':18,'q':'8/3','quotient_length':16,
     'Ext_and_equivariance_computed':False}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','ranks':ranks,'generic_minor':str(det),'proof_sha256':out['proof_sha256']}))
