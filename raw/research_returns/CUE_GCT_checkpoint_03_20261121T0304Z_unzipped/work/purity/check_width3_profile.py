"""Exact finite check of the sharp width-three interval-profile example."""
import json
from pathlib import Path
import sympy as s

x=s.symbols('x1:5')
P=s.diag(1,1,0)
I=s.eye(3)
def E(i,j):
    a=s.zeros(3)
    a[i-1,j-1]=1
    return a
A=[P+x[0]*E(3,1), I+x[1]*E(1,3), P+x[2]*E(3,2), I+x[3]*E(2,3)]
row=s.Matrix([[0,0,1]])
for a in A:
    row=row*a
row=row.applyfunc(s.expand)
expected=s.Matrix([[x[0],x[0]*x[1]*x[2],s.prod(x)]])
assert row==expected
intervals=[]
for left in range(4):
    Q=s.eye(3)
    for right in range(left,4):
        Q=(Q*A[right]).applyfunc(s.expand)
        constant=Q.subs({v:0 for v in x})
        generic=Q.rank()
        at_zero=constant.rank()
        assert generic==at_zero and generic in (2,3)
        intervals.append({'left':left+1,'right':right+1,'rank':generic,
                          'determinant':str(s.factor(Q.det())),
                          'top_left_minor':str(s.factor(Q[:2,:2].det()))})
coeff={}
for col in range(3):
    for alpha,value in s.Poly(row[col],*x).terms():
        coeff.setdefault(alpha,[0,0,0])[col]=value
low=[v for alpha,v in coeff.items() if sum(a>0 for a in alpha)<=3]
rank_low=s.Matrix(low).rank()
rank_all=s.Matrix(list(coeff.values())).rank()
assert rank_low==2 and rank_all==3
result={'scope':'One exact symbolic sharpness example; not a proof by finite testing.',
        'row':[str(v) for v in row], 'intervals':intervals,
        'rank_support_at_most_3':rank_low, 'full_coefficient_rank':rank_all,
        'passed':True}
Path(__file__).with_name('width3_profile_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'passed':True,'intervals':len(intervals),
                  'rank_support_at_most_3':rank_low,'full_coefficient_rank':rank_all}))
