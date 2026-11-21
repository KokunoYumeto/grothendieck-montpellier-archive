"""Independent exact check of Severn 2610.00387v2 Appendix A printed blocks.

This checks the printed linear algebra only, not the derivation from a cover.
Source: weil-qsqrt3-v1.5.tex, Appendix A, X_1,...,X_17.
"""
from pathlib import Path
import json
import itertools
import sympy as s
w=s.Symbol('w')
Q=s.Rational
def red(x): return s.rem(s.Poly(s.expand(x),w,domain=s.QQ),s.Poly(w*w+w+1,w)).as_expr()
def conj(x): return red(s.sympify(x).subs(w,-1-w))
def rm(M): return M.applyfunc(red)
def adj(M): return M.T.applyfunc(conj)
def mat(rows): return s.Matrix([[red(s.sympify(x)) for x in row] for row in rows])
X=[]
X.append(mat([[2,Q(1,3)-w/3,Q(1,3)+2*w/3,-w],[2+w,2,0,2+w],[-1-2*w,0,2,-1+w],[1+w,Q(1,3)-w/3,-Q(2,3)-w/3,2]]))
X.append(mat([[2,-2*w,-Q(2,3)+2*w/3,2-2*w],[6+6*w,6,-4-2*w,12+6*w],[-4-2*w,-2+2*w,2,-6],[4+2*w,2-2*w,-2,6]]))
X.append(mat([[0,0,0,0],[0,3,-w,3+3*w],[0,1+w,3,3*w],[0,-w,-1-w,3]]))
X.append(mat([[0,0,0,0],[0,2,0,2+w],[0,0,2,-1+w],[0,Q(1,3)-w/3,-Q(2,3)-w/3,2]]))
X.append(mat([[0,0,0,0],[0,0,0,0],[0,0,4,-2+2*w],[0,0,-Q(4,3)-2*w/3,3]]))
X.append(mat([[0,0,0,0],[0,0,0,0],[0,0,2,0],[0,0,0,0]]))
X.append(mat([[0,0,0,0],[0,0,0,0],[0,0,2,-1+w],[0,0,-Q(2,3)-w/3,2]]))
X.append(mat([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,2]]))
X.append(mat([[2,2,-Q(4,3)-2*w/3,2],[6,6,-4-2*w,6],[-2+2*w,-2+2*w,2,-2+2*w],[2,2,-Q(4,3)-2*w/3,2]]))
X.append(mat([[3,2-w,-2-w,3],[9+3*w,8,-5-4*w,9+3*w],[-3+3*w,-1+4*w,3,-3+3*w],[3,2-w,-2-w,3]]))
X.append(mat([[5,Q(4,3)-7*w/3,-Q(4,3)+w/3,3-2*w],[11+7*w,8,-5-3*w,11+4*w],[-5-w,-2+3*w,4,-5+2*w],[5+2*w,Q(7,3)-4*w/3,-Q(7,3)-2*w/3,5]]))
X.append(mat([[7,Q(2,3)-11*w/3,-Q(2,3)+5*w/3,3-4*w],[13+11*w,9,-5-2*w,13+5*w],[-7-5*w,-3+2*w,5,-7+w],[7+4*w,Q(8,3)-5*w/3,-Q(8,3)-w/3,7]]))
X.append(mat([[5,Q(4,3)-7*w/3,-Q(1,3)+4*w/3,3-2*w],[11+7*w,8,-3,11+4*w],[-5-4*w,-3,3,-5-w],[5+2*w,Q(7,3)-4*w/3,-Q(4,3)+w/3,5]]))
X.append(mat([[2,Q(4,3)-4*w/3,-Q(4,3)-2*w/3,2],[8+4*w,8,-4-4*w,8+4*w],[-2+2*w,4*w,2,-2+2*w],[2,Q(4,3)-4*w/3,-Q(4,3)-2*w/3,2]]))
X.append(mat([[0,0,0,0],[0,2,-2-2*w,4+2*w],[0,2*w,2,-2+2*w],[0,Q(2,3)-2*w/3,-Q(4,3)-2*w/3,2]]))
X.append(mat([[2,-w,Q(1,3)+2*w/3,1-w],[3+3*w,3,-2-w,6+3*w],[-1-2*w,-1+w,2,-3],[2+w,1-w,-1,3]]))
X.append(mat([[2,Q(2,3)-2*w/3,0,2],[4+2*w,2,0,4+2*w],[0,0,0,0],[2,Q(2,3)-2*w/3,0,2]]))

D=s.diag(-3,-1,-1,-3)
expected=[4,1,3,3,2,1,2,1,1,2,4,4,4,1,1,2,1]
records=[]
for j,A in enumerate(X,1):
    B=rm(D*A)
    herm=rm(B-adj(B))==s.zeros(4)
    minors=[]
    for k in range(1,5):
        for I in itertools.combinations(range(4),k):
            minors.append(red((-B).extract(I,I).det()))
    assert all(not c.has(w) for c in minors)
    nsem=herm and all(c>=0 for c in minors)
    rank=max([0]+[k for k in range(1,5) if any(red(B.extract(I,J).det())!=0 for I in itertools.combinations(range(4),k) for J in itertools.combinations(range(4),k))])
    records.append({'j':j,'Hermitian':herm,'negative_semidefinite':bool(nsem),'rank_K':rank,'printed_rank':expected[j-1]})
cols=[]
for A in X:
    v=[]
    for z in A:
        zz=s.Poly(z,w)
        v.extend([zz.nth(0),zz.nth(1)])
    cols.append(s.Matrix(v))
rankQ=s.Matrix.hstack(*cols).rank()
sumB=rm(sum((D*A for A in X),s.zeros(4)))
leading=[red((-sumB)[:k,:k].det()) for k in range(1,5)]
result={'source':'Severn 2610.00387v2 Appendix A (version 1.5)','scope':'Printed blocks only; no geometric derivation checked by this script.',
        'blocks':records,'rank_over_Q':rankQ,'expected_rank_over_Q':16,
        'negative_sum_leading_principal_minors':[str(x) for x in leading],
        'sum_negative_definite':all(x>0 for x in leading)}
result['printed_checks_pass']=all(r['Hermitian'] and r['negative_semidefinite'] and r['rank_K']==r['printed_rank'] for r in records) and rankQ==16 and result['sum_negative_definite']
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
