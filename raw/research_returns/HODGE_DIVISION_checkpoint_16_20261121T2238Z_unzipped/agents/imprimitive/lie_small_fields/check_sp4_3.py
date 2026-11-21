#!/usr/bin/env python3
"""All scalar-normalizer spectra from the complete Sp4(3) cover tables."""
from pathlib import Path
from fractions import Fraction
import hashlib,importlib.util,json,time

BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('exact_cyclotomic',BASE.parent/'sporadic/verify_quarter_bound.py')
cyc=importlib.util.module_from_spec(spec);spec.loader.exec_module(cyc)
raw=(BASE/'sp4_3_character_inputs.json').read_bytes()
data=json.loads(raw);ts={t['name']:t for t in data['tables']}
assert set(ts)=={'2.U4(2)','2.U4(2).2'}
assert data['simple_metadata']['extension_info']==['2','2']
chars={n:[[cyc.key(z) for z in row] for row in t['characters']] for n,t in ts.items()}
start=time.monotonic();records=[];failures=[];count=0
for name,t in ts.items():
    assert 'origin: ATLAS of finite groups' in t['information']
    assert len(t['characters'])==len(t['orders'])==len(t['sizes'])
    assert sum(c[0]**2 for c in chars[name])==sum(t['sizes'])==t['order']
    for i,c in enumerate(chars[name]):
        a=c[0]
        if a==1:continue
        core_row=i+1
        if 'core' in t:
            rest=tuple(c[j-1] for j in t['fusion'])
            matches=[k+1 for k,u in enumerate(chars[t['core']]) if tuple(u)==rest]
            if not matches:continue
            assert len(matches)==1;core_row=matches[0]
        rec={'table':name,'row':i+1,'core_row':core_row,'degree':a,
             'indicator':t['frobenius_schur'][i],'nonscalar_entries':0,'minimum_ratio':'1','witnesses':[]}
        minimum=Fraction(1)
        for j,z in enumerate(c):
            if cyc.squared_norm(z)==(a*a,):continue
            ms=cyc.cyclic_multiplicities(t,c,j);nu=a-max(ms);count+=1
            rec['nonscalar_entries']+=1
            ratio=Fraction(nu,a)
            witness={'class':j+1,'class_name':t['class_names'][j],'order':t['orders'][j],
                     'nu':nu,'multiplicities_zero_first':ms}
            if ratio<minimum:minimum=ratio;rec['witnesses']=[]
            if ratio==minimum:rec['witnesses'].append(witness)
            if 4*nu<a:failures.append({'table':name,'row':i+1,'core_row':core_row,'degree':a,**witness})
        rec['minimum_ratio']=str(minimum);records.append(rec)
out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
     'method':'exact cyclotomic-polynomial Fourier on every nonscalar entry; full irreducible restriction matching',
     'selected_rows':len(records),'nonscalar_entries':count,'quarter_failures':failures,
     'records':records,'seconds':round(time.monotonic()-start,3)}
assert len(records)==59 and count==1992
assert {(r['table'],r['row'],r['class'],r['degree'],r['nu']) for r in failures}=={
    ('2.U4(2)',2,3,5,1),('2.U4(2)',3,3,5,1),
    ('2.U4(2).2',4,25,6,1),('2.U4(2).2',5,25,6,1)}
for r in records:
    a=r['degree'];bound=Fraction(r['minimum_ratio'])
    assert a>=4
    assert bound>=Fraction(1, a if a in (4,5,6) else 4)
assert [i+1 for i,c in enumerate(chars['2.U4(2)']) if c[0]==6]==[4]
c6=chars['2.U4(2)'][3];t6=ts['2.U4(2)'];p2=next(p['map'] for p in t6['power_maps'] if p['prime']==2)
assert all(isinstance(z,int) for z in c6)
assert sum(s*c6[j-1] for s,j in zip(t6['sizes'],p2))==t6['order']
assert all(c6[j]==6 for j,s in enumerate(t6['sizes']) if s==1)
out['degree_six_indicator_independently_reconstructed']=1
out['degree_six_center_trivial']=True
out['degree_five_quarter_expectation']='REFUTED: class2b has spectrum1+4(-1) in both degree5 rows'
(BASE/'check_sp4_3.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'}))
for r in records:print(r['table'],r['row'],r['core_row'],r['degree'],r['indicator'],r['minimum_ratio'])
