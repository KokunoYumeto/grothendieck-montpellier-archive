#!/usr/bin/env python3
"""Reviewer's complete independent five-table Suzuki/Ree reconstruction."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,importlib.util,json,time

BASE=Path(__file__).resolve().parent;OWN=BASE.parent
spec=importlib.util.spec_from_file_location('reviewer_cyc',OWN/'sporadic/verify_quarter_bound.py')
cyc=importlib.util.module_from_spec(spec);spec.loader.exec_module(cyc)
P=OWN.parent/'g34_eightfolds/bireflection/twisted_lie/twisted_character_inputs.json'
raw=P.read_bytes();assert hashlib.sha256(raw).hexdigest()=='10dd43bccf28471f0c8725086666385aba1dc9970fe9d53bd1478e9ad6a1637b'
ts={t['name']:t for t in json.loads(raw)['tables']}
assert set(ts)=={'2^2.Sz(8)','2^2.Sz(8).3','R(27)',"2F4(2)'",'2F4(8)'}
cs={n:[[cyc.key(z) for z in row] for row in t['characters']] for n,t in ts.items()}
start=time.monotonic();out={'status':'PASS','method':'independent integer-polynomial Fourier and pointwise restriction matching; original input coefficient L1 bounds','author_code_imported':False,'input_sha256':hashlib.sha256(raw).hexdigest(),'tables':[],'rows':0,'spectra':0,'trace_bounds':0}
for name,t in ts.items():
    assert len(cs[name])==len(t['sizes'])==len(t['orders'])
    assert all(len(c)==len(cs[name]) for c in cs[name])
    assert sum(c[0]**2 for c in cs[name])==sum(t['sizes'])==t['order']
    if name=='2F4(8)':assert 'source: Gunter Malle' in t['information']
    else:assert 'origin: ATLAS of finite groups' in t['information']
    rs=[]
    for i,c in enumerate(cs[name]):
        if c[0]==1:continue
        if 'core' in t and tuple(c[j-1] for j in t['fusion']) not in {tuple(u) for u in cs[t['core']]}:continue
        rs.append(i)
    rec={'name':name,'rows':[i+1 for i in rs],'minimum_degree':min(cs[name][i][0] for i in rs),'entries':0,'bound':None}
    vals=[]
    for i in rs:
        c=cs[name][i];a=c[0]
        for j,z in enumerate(c):
            if cyc.squared_norm(z)==(a*a,):continue
            rec['entries']+=1
            if 'Sz(8)' in name:
                ms=cyc.cyclic_multiplicities(t,c,j);nu=a-max(ms)
                assert 7*nu>=3*a;vals.append(F(nu,a));out['spectra']+=1
            else:
                l1=abs(z) if isinstance(z,int) else sum(abs(v) for v in z[1])
                assert 4*l1<=a;vals.append(F(l1,a));out['trace_bounds']+=1
    rec['bound']=str(min(vals) if 'Sz(8)' in name else max(vals));out['rows']+=len(rs);out['tables'].append(rec)
assert [r['minimum_degree'] for r in out['tables']]==[14,14,703,26,64638]
assert [r['bound'] for r in out['tables']]==['3/7','3/7','26/703','3/13','449/32319']
assert out['rows']==213 and out['spectra']==1330 and out['trace_bounds']==14141
assert 12*F(23,128)-2==F(5,32) and 6/F(5,32)==F(192,5)
assert 14**2>F(192,5) and 124>F(192,5) and 26>24
proof=OWN.parent/'g34_eightfolds/bireflection/twisted_lie_section.tex'
out['proof_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest();out['seconds']=round(time.monotonic()-start,3)
(BASE/'independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
