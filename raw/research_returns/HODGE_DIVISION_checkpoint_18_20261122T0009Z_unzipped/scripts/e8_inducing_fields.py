"""Exact necessary E8 larger-field profiles. No tuple existence is certified."""
from pathlib import Path
from fractions import Fraction
from math import gcd,lcm
import json,hashlib
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
inp=ROOT/'research/e8_class_exploration.json'
data=json.loads(inp.read_text())
x=S.Symbol('x');H=S.Matrix(data['cartan']);I=S.eye(8)
gens=[I-I[:,j]*H[j,:] for j in range(8)]
rows=[]
for d,expected_index,expected_name in [(8,21,'D_8(a_3)'),(12,32,'E_8(a_3)')]:
    target=S.Poly(S.cyclotomic_poly(d,x)**2,x)
    matches=[c for c in data['classes'] if S.Poly(S.sympify(c['characteristic_polynomial']),x)==target]
    assert len(matches)==1
    c=matches[0];assert c['index']==expected_index and c['name']==expected_name
    w=I
    for j in c['word']:w=w*gens[j-1]
    assert w==S.Matrix(c['matrix']) and w.T*H*w==H
    assert w.charpoly(x).as_poly()==target and w**d==I
    assert all(w**(d//p)!=I for p in S.factorint(d))
    primitive=[a for a in range(d) if gcd(a,d)==1]
    phases=[]
    for a in primitive:
        spec=sorted([Fraction((a+b)%d,d) for b in primitive for _ in range(2)])
        rank=sum(q!=0 for q in spec); age=sum(spec)
        assert rank==6
        order=lcm(*(q.denominator for q in spec))
        for eps in [0,d//2]:
            a2=(-a+eps)%d
            spec2=sorted([Fraction((a2+b)%d,d) for b in primitive for _ in range(2)])
            assert sum(spec2)+age==6
        assert (age==3 and order==4) if d==8 else (age in [Fraction(8,3),Fraction(10,3)] and order==6)
        phases.append({'phase':str(Fraction(a,d)),'spectrum':[str(q) for q in spec],
                       'moving_rank':rank,'age':str(age),'inertia_order':order})
    rows.append({'scalar_order':d,'class_index':c['index'],'class_name':c['name'],
                 'class_size':c['class_size'],'real_factor_order':d,'characteristic_polynomial':str(target.as_expr()),'phases':phases})
out={'status':'PASS','input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),
     'rows':rows,'branch_moving_sum':10+6+6,'coefficient_degree':8,
     'signature':[3,3],'tuple_existence_checked':False,'dominance_checked':False,
     'scope':'Written proof supplies the all-scalar and larger-field exhaustion; complete class list is published input.'}
(ROOT/'research/e8_inducing_fields_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'classes':[r['class_name'] for r in rows],
                 'phase_checks':sum(len(r['phases']) for r in rows),'signature':out['signature']}))
