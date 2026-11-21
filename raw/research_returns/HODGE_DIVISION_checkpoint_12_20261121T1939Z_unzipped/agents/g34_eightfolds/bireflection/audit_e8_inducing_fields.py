"""Independent exact local check for HD-E8IF1; no tuple/rank assertion."""
from pathlib import Path
from fractions import Fraction
from math import gcd,lcm
import hashlib,json
import sympy as s

HERE=Path(__file__).resolve().parent
SRC=HERE.parents[2]/'research'/'e8_class_exploration.json'
data=json.loads(SRC.read_text())
H=s.Matrix(data['cartan']);one=s.eye(8);x=s.Symbol('x')
gens=[]
for j in range(8):
    a=s.eye(8)
    for k in range(8):a[j,k]-=H[j,k]
    assert a*a==one and a.T*H*a==H
    gens.append(a)
matches={8:[],12:[]}
for c in data['classes']:
    a=one
    for j in c['word']:a=a*gens[j-1]
    assert a==s.Matrix(c['matrix']) and a.T*H*a==H
    cp=a.charpoly(x).as_expr().expand()
    assert cp==s.sympify(c['characteristic_polynomial']).expand()
    for d in matches:
        if cp==s.expand(s.cyclotomic_poly(d,x)**2):matches[d].append(c)
checks=[]
for d,idx,name,size in [(8,21,'D_8(a_3)',3628800),(12,32,'E_8(a_3)',2419200)]:
    assert len(matches[d])==1
    c=matches[d][0]
    assert (c['index'],c['name'],c['class_size'])==(idx,name,size)
    exps=[Fraction(b,d) for b in range(d) if gcd(b,d)==1]
    for a in exps:
        spec=sorted([(a+b)%1 for b in exps for _ in range(2)])
        assert sum(v!=0 for v in spec)==6
        for sign in [0,Fraction(1,2)]:
            other=sorted([(-a+sign+b)%1 for b in exps for _ in range(2)])
            assert sum(spec)+sum(other)==6
        order=lcm(*(v.denominator for v in spec))
        assert order==(4 if d==8 else 6)
        checks.append({'d':d,'phase':str(a),'spectrum':[str(v) for v in spec],
                       'age':str(sum(spec)),'order':order})
out={'status':'PASS','all_class_words_reconstructed':len(data['classes']),
     'scalar_phase_checks':len(checks),'checks':checks,
     'source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
     'scope':'Complete class list is published/CHEVIE input; exact reconstruction and spectra independently checked; no tuple existence or period rank inferred.'}
(HERE/'audit_e8_inducing_fields.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','all_class_words_reconstructed','scalar_phase_checks']}))
