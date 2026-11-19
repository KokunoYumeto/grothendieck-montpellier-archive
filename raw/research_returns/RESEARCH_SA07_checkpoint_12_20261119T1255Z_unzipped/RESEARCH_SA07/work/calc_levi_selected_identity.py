#!/usr/bin/env python3
"""Exact polynomial identity for the seven selected mixed scalar rows."""
from pathlib import Path
source=Path(__file__).with_name('calc_levi_scalar_rows.py').read_text()
exec(compile(source.split('chords=list')[0],'levi_scalar_definitions','exec'))
from sympy.polys.matrices import DomainMatrix
data=pickle.loads(Path(__file__).with_name('calc_levi_scalar_rows.pickle').read_bytes())
K=data['K'];L=sp.Matrix([[-1,4,0,0,0],[1,0,1,0,0],[0,0,0,1,1]]);LK=L*K
rows=list(data['rows']);names=list(data['names'])
chords6=list(pairings(tuple(range(6))))
selected=[('abx',(-1,-2,-3,-4),1),('abx',(-1,-2,-3,-4),2),
          ('axy',(-1,-3,-4,-2),1),('xyu',(-3,-4,-5,-6),1)]
for name,constants,index in selected:
    plans=plans_ES(chords6[index])
    row=[sp.factor(evaluate(T,constants,plans)) for T in inputs]
    rows.append(row);names.append('ES1_'+name+'_'+str(index))
    print('EXACT_ROW',names[-1],row,flush=True)
M=sp.Matrix(rows)
_,pivots=M.subs(s,3).rref();pivots=list(pivots)
assert len(pivots)==7
square=M[:,pivots]
domain_matrix=DomainMatrix.from_Matrix(square).convert_to(sp.QQ.poly_ring(s))
inverse_numerator,denominator=domain_matrix.inv_den()
den=domain_matrix.domain.to_sympy(denominator)
inv=inverse_numerator.to_Matrix()
assert all(sp.expand(x)==0 for x in square*inv-den*sp.eye(7))
numerator=LK[:,pivots]*inv
defect=(numerator*M-den*LK).applyfunc(sp.expand)
print('SELECTED_ROW_NAMES',names,flush=True)
print('PIVOT_COLUMNS',pivots,flush=True)
print('EXACT_DENOMINATOR',sp.factor(den),flush=True)
print('NONZERO_DEFECT_ENTRIES',[(i,j,sp.factor(defect[i,j])) for i in range(3) for j in range(12) if defect[i,j]],flush=True)
if defect==sp.zeros(3,12):
    numerator=numerator.applyfunc(sp.factor)
    print('EXACT_POLYNOMIAL_ROW_IDENTITY_PASSED',flush=True)
    print('NUMERATOR_MATRIX',numerator.tolist(),flush=True)
with Path(__file__).with_suffix('.pickle').open('wb') as file:
    pickle.dump(dict(M=M,K=K,L=L,LK=LK,s=s,names=names,pivots=pivots,denominator=den,numerator=numerator,defect=defect),file)
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
