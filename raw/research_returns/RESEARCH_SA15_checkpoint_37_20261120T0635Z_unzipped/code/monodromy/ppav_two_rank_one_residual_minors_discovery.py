# Exact source of the executed inline residual-minor discovery at18:34UTC.
from pathlib import Path
import json,sympy as s,itertools
p=Path('RESEARCH_SA15_work/agents/monodromy/outputs/ppav_two_rank_one_polar_uniform_lie.json');d=json.loads(p.read_text());a,b,c=s.symbols('a b c')
M=s.Matrix([[sum(a**e[0]*b**e[1]*c**e[2] for e in v) for v in row] for row in d['remaining_matrix']]);print(M)
polys=[]
for rows in itertools.combinations(range(8),4):
 f=s.Poly(M[list(rows),:].det(),a,b,modulus=2).as_expr()
 if f:polys.append(f)
print('nonzero minors',len(polys))
print('gcd',s.gcd_list(polys));print('unique factors',set(str(s.factor(p,modulus=2)) for p in polys if len(p.free_symbols)<=1))
print(s.groebner(polys,a,b,modulus=2))
