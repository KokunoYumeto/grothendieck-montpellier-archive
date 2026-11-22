#!/usr/bin/env python3
"""Covered odd-C2 core/outer spectra, with explicit limited coverage."""
from pathlib import Path
from fractions import Fraction
import hashlib
import importlib.util
import json
import time

BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('reviewed_exact_cyclotomic',BASE.parent/'sporadic/verify_quarter_bound.py')
cyc=importlib.util.module_from_spec(spec);spec.loader.exec_module(cyc)
raw=(BASE/'character_inputs.json').read_bytes()
data=json.loads(raw);tabs={t['name']:t for t in data['tables']}
assert set(tabs)=={'2.S4(5)','2.S4(5).2','S4(7)','S4(7).2','S4(9)','S4(9).2_1','S4(9).2_2','S4(9).2_3'}
chars={n:[[cyc.key(z) for z in row] for row in t['characters']] for n,t in tabs.items()}
start=time.monotonic();records=[];failures=[];count=0
for name,t in tabs.items():
    assert len(t['characters'])==len(t['orders'])==len(t['sizes'])
    assert sum(c[0]**2 for c in chars[name])==sum(t['sizes'])==t['order']
    if 'S4(5)' in name:
        assert 'origin: ATLAS of finite groups' in t['information']
    else:
        assert 'Dixon' in t['information']
    if 'fusion' in t:
        core=tabs[t['core']];f=t['fusion']
        assert t['order']==2*core['order'] and len(f)==len(core['orders'])
        assert sum(t['sizes'][j-1] for j in set(f))==core['order']
        assert all(core['orders'][j]==t['orders'][f[j]-1] for j in range(len(f)))
        for power in core['power_maps']:
            target=next(v['map'] for v in t['power_maps'] if v['prime']==power['prime'])
            assert all(f[power['map'][j]-1]==target[f[j]-1] for j in range(len(f)))
    for i,c in enumerate(chars[name]):
        a=c[0]
        if a==1:continue
        core_row=i+1
        if 'fusion' in t:
            rest=tuple(c[j-1] for j in t['fusion'])
            matches=[k+1 for k,u in enumerate(chars[t['core']]) if tuple(u)==rest]
            if not matches:continue
            assert len(matches)==1;core_row=matches[0]
        minimum=Fraction(1);witnesses=[];entries=0
        for j,z in enumerate(c):
            if cyc.squared_norm(z)==(a*a,):continue
            ms=cyc.cyclic_multiplicities(t,c,j);nu=a-max(ms);count+=1;entries+=1
            ratio=Fraction(nu,a)
            witness={'class':j+1,'class_name':t['class_names'][j],'order':t['orders'][j],
                     'nu':nu,'multiplicities_zero_first':ms}
            if ratio<minimum:minimum=ratio;witnesses=[]
            if ratio==minimum:witnesses.append(witness)
            if 4*nu<a:failures.append({'table':name,'row':i+1,'core_row':core_row,'degree':a,**witness})
        records.append({'table':name,'row':i+1,'core_row':core_row,'degree':a,
                        'minimum_ratio':str(minimum),'witnesses':witnesses,
                        'nonscalar_entries':entries,'indicator':t['frobenius_schur'][i]})
out={'status':'PASS' if not failures else 'COUNTEREXAMPLES TO QUARTER BOUND',
     'input_sha256':hashlib.sha256(raw).hexdigest(),
     'method':'Reviewed exact cyclotomic-polynomial Fourier on every nonscalar entry; full irreducible-restriction matching',
     'helper_sha256':hashlib.sha256((BASE.parent/'sporadic/verify_quarter_bound.py').read_bytes()).hexdigest(),
     'selected_rows':len(records),'nonscalar_entries':count,'quarter_failures':failures,
     'minimum_by_core':{core:str(min(Fraction(r['minimum_ratio']) for r in records if tabs[r['table']]['core']==core)) for core in {t['core'] for t in tabs.values()}},
     'degree_minima':{core:min(c[0] for c in chars[core] if c[0]>1) for core in {t['core'] for t in tabs.values()}},
     'records':records,'seconds':round(time.monotonic()-start,6),
     'coverage':data['coverage']}
assert len(records)==485 and count==37502 and not failures
(BASE/'check_spectra.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
