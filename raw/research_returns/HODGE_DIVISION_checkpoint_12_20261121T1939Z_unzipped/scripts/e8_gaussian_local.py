"""Exact local moving-space forms for i times all112 Weyl E8 classes.

Depends on authored exact Gaussian arithmetic, and mathematical class-word
data reconstructed by examine_e8_classes.py. No claim about a Hurwitz
period differential is part of this certificate.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd
import json,sys
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'agents/g34_eightfolds/g31'))
import gaussian_exact as M
from check_local_discriminants import inert_parities
data=json.loads((ROOT/'research/e8_class_exploration.json').read_text())
H=[[M.F(a) for a in row] for row in data['cartan']]
rows=[];x=S.Symbol('x')
for item in data['classes']:
    g=[[M.F(0,a) for a in row] for row in item['matrix']]
    assert M.mul(M.mul(M.star(g),H),g)==H
    a=M.sub(M.eye(8),g);cols=M.rref(a)[1];d=len(cols)
    U=M.tr([M.tr(a)[j] for j in cols])
    selected=M.rref(M.tr(U))[1]
    left=M.inv([U[j] for j in selected])
    action=M.mul(left,[M.mul(g,U)[j] for j in selected])
    assert M.mul(U,action)==M.mul(g,U)
    gramdet=M.det(M.mul(M.mul(M.star(U),H),U))
    b=M.det(M.sub(M.eye(d),action))
    assert not gramdet.b and gramdet.a>0 and b
    assert not b.a or not b.b
    positive_q=gramdet.a/(abs(b.a) if b.a else abs(b.b))
    exponents=[]
    for f,mult in item['factors']:
        fp=S.Poly(S.sympify(f),x)
        Ns=[n for n in range(1,61) if S.Poly(S.cyclotomic_poly(n,x),x)==fp]
        assert len(Ns)==1
        n=Ns[0]
        for k in range(n):
            if gcd(k,n)==1:exponents.extend([(Q(k,n)+Q(1,4))%1]*mult)
    assert len(exponents)==8 and sum(v!=0 for v in exponents)==d
    age=sum(exponents,Q(0))
    row={'index':item['index'],'name':item['name'],'moving_rank':d,
         'gramdet':str(gramdet.a),'det_one_minus_moving':b.pair(),
         'positive_local_q':str(positive_q),'inert_odd_valuations':inert_parities(positive_q),
         'eigenvalue_exponents':[str(v) for v in sorted(exponents)],
         'age':str(age),'age_imbalance':str(age-Q(d,2))}
    rows.append(row)
out={'status':'PASS','classes':rows,'nonnorm_classes':[r for r in rows if r['inert_odd_valuations']]}
(ROOT/'research/e8_gaussian_local.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','count':len(rows),'nonnorm_classes':out['nonnorm_classes'],
                  'moving_rank4':[(r['index'],r['name'],r['age_imbalance'],r['positive_local_q']) for r in rows if r['moving_rank']==4]}))
