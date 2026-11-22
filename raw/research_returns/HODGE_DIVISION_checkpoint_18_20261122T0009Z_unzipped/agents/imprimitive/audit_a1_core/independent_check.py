#!/usr/bin/env python3
"""Independent exact Fourier reconstruction for D-BI-21.

Uses this reviewer's earlier integer-polynomial implementation, not the
author's GAP or Ramanujan code, and selects restrictions by exact row match.
"""
from pathlib import Path
import hashlib,importlib.util,json,time
from fractions import Fraction

BASE=Path(__file__).resolve().parent
OWN=BASE.parent
src=OWN/'sporadic/verify_quarter_bound.py'
spec=importlib.util.spec_from_file_location('reviewer_cyclotomic',src)
cyc=importlib.util.module_from_spec(spec);spec.loader.exec_module(cyc)
P=OWN.parent/'g34_eightfolds/bireflection/a1/a1_character_inputs.json'
raw=P.read_bytes();sha=hashlib.sha256(raw).hexdigest()
assert sha=='5ed905449e1f6f64f3eb18b27a213fc5c72e0731dbd591670166e8763ad7fc88'
data=json.loads(raw);tables={t['name']:t for t in data['tables']}
inventory=json.loads((OWN/'sporadic/small_l2_table_inventory.json').read_text())
expected={g['cover'] for g in inventory['groups']}
for g in inventory['groups']:
    for ext in g['cyclic_extensions']:
        expected.update([ext['core'],ext['extension']])
        assert tables[ext['extension']]['fusion']==ext['fusion']
assert set(tables)==expected and len(tables)==33
chars={n:[[cyc.key(z) for z in c] for c in t['characters']] for n,t in tables.items()}
started=time.monotonic();rows=entries=0;exceptions=[];minimum=Fraction(1)
details=[]
for name,t in tables.items():
    assert 'origin: ATLAS of finite groups' in t['information']
    allc=chars[name]
    assert len(allc)==len(t['sizes'])==len(t['orders'])
    assert sum(c[0]**2 for c in allc)==sum(t['sizes'])==t['order']
    selected=[]
    for i,c in enumerate(allc):
        if c[0]<=1:continue
        if 'core' in t:
            restriction=tuple(c[j-1] for j in t['fusion'])
            if restriction not in {tuple(u) for u in chars[t['core']]}:continue
        selected.append(i)
    record={'table':name,'selected_rows':[i+1 for i in selected],'minimum_nu_over_degree':[]}
    for i in selected:
        c=allc[i];degree=c[0];ratios=[];rows+=1
        for j,z in enumerate(c):
            if cyc.squared_norm(z)==(degree*degree,):continue
            multiplicities=cyc.cyclic_multiplicities(t,c,j)
            nu=degree-max(multiplicities);entries+=1
            ratios.append(Fraction(nu,degree));minimum=min(minimum,ratios[-1])
            assert 5*nu>=degree
            if 4*nu<degree:
                exceptions.append({'table':name,'row':i+1,'class':j+1,'degree':degree,
                                   'order':t['orders'][j],'nu':nu,'multiplicities_zero_first':multiplicities})
        record['minimum_nu_over_degree'].append(str(min(ratios)))
    details.append(record)
assert rows==654 and entries==18922 and len(exceptions)==4
assert {(x['table'],x['row'],x['class'],x['degree'],x['nu']) for x in exceptions}=={
 ('6.A6.2_1',3,20,5,1),('6.A6.2_1',4,20,5,1),
 ('6.A6.2_1',5,21,5,1),('6.A6.2_1',6,21,5,1)}
restrictions=[]
for x in exceptions:
    t=tables[x['table']];c=chars[x['table']][x['row']-1]
    rest=[c[j-1] for j in t['fusion']];core=tables[t['core']]
    matches=[i+1 for i,u in enumerate(chars[t['core']]) if u==rest]
    assert len(matches)==1
    assert all(rest[j]==5 for j,size in enumerate(core['sizes']) if size==1)
    restrictions.extend(matches)
assert restrictions==[2,2,3,3]
proof=OWN.parent/'g34_eightfolds/bireflection/a1_core_section.tex'
out={'status':'PASS','method':'independent exact cyclotomic polynomial Fourier on every nonscalar entry; pointwise irreducible restriction selection',
     'author_code_imported':False,'tables':33,'rows':rows,'entries':entries,
     'minimum_ratio':str(minimum),'quarter_exceptions':exceptions,'exception_core_rows':restrictions,
     'input_sha256':sha,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
     'seconds':round(time.monotonic()-started,3),'complete_rows':details}
(BASE/'independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='complete_rows'}))
