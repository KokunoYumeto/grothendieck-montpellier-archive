#!/usr/bin/env python3
"""Exact reconstruction of every spectrum in the finite ordinary A_n scan.

This driver imports the previously independently authored integer-polynomial
arithmetic, not GAP's character selection or eigenvalue routine. Character
tables and generic labels remain explicitly identified GAP inputs.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib, importlib.util, json, time

BASE=Path(__file__).resolve().parent
ROOT=BASE.parent
spec=importlib.util.spec_from_file_location('exact_cyclotomic',ROOT/'agents/imprimitive/sporadic/verify_quarter_bound.py')
cyc=importlib.util.module_from_spec(spec);spec.loader.exec_module(cyc)
raw=(BASE/'alternating_small_inputs.json').read_bytes()
data=json.loads(raw);tables={t['name']:t for t in data['tables']}
assert set(tables)=={f'{kind}({n})' for n in range(8,15) for kind in ('Alt','Sym')}
chars={name:[[cyc.key(z) for z in c] for c in t['characters']] for name,t in tables.items()}
scan=json.loads((BASE/'alternating_small_scan.json').read_text())
scan={t['name']:t for t in scan['tables']}
start=time.monotonic();rows=entries=0;records=[];small=[];nonreal=[]

def is_real(z):
    if isinstance(z,int):return True
    n,c=z;v=list(c);inv=[0]*n
    for j,a in enumerate(c):inv[-j%n]+=a
    return (cyc.fmpz_poly(v)-cyc.fmpz_poly(inv))%cyc.phi(n)==0

for name,t in tables.items():
    n=t['n'];cc=chars[name];nr=len(cc)
    assert len(t['sizes'])==len(t['orders'])==nr
    assert all(len(c)==nr for c in cc)
    assert sum(c[0]**2 for c in cc)==sum(t['sizes'])==t['order']
    if name.startswith('Sym'):assert all(is_real(z) for c in cc for z in c)
    assert t['information']==f'computed using generic character table for {"alternating" if name.startswith("Alt") else "symmetric"} groups'
    chosen=[]
    for i,c in enumerate(cc):
        if c[0]<=1:continue
        if 'core' in t:
            rest=tuple(c[j-1] for j in t['fusion'])
            if rest not in {tuple(u) for u in chars[t['core']]}:continue
        chosen.append(i)
    assert [i+1 for i in chosen]==[r['row'] for r in scan[name]['rows']]
    if 'core' in t:
        core=tables[t['core']];fus=[j-1 for j in t['fusion']]
        assert t['order']==2*core['order'] and fus[0]==0
        assert all(core['orders'][i]==t['orders'][j] for i,j in enumerate(fus))
        assert [i for i,j in enumerate(fus) if j==0]==[0]
        for j in set(fus):assert sum(core['sizes'][i] for i,k in enumerate(fus) if k==j)==t['sizes'][j]
        pm={p['prime']:p['map'] for p in t['power_maps']}
        for p in core['power_maps']:
            assert all(fus[k-1]==pm[p['prime']][fus[i]]-1 for i,k in enumerate(p['map']))
    rtable={'name':name,'rows':[]}
    for i in chosen:
        c=cc[i];a=c[0];minimum=F(1);worst=[];rows+=1
        for j,z in enumerate(c):
            if cyc.squared_norm(z)==(a*a,):continue
            m=cyc.cyclic_multiplicities(t,c,j);nu=a-max(m);ratio=F(nu,a);entries+=1
            if ratio<minimum:minimum=ratio;worst=[]
            if ratio==minimum:worst.append({'class':j+1,'nu':nu,'multiplicities_zero_first':m})
        author=next(r for r in scan[name]['rows'] if r['row']==i+1)
        assert str(minimum)==author['min_ratio']
        # GAP orders Fourier multiplicities by eigenvalues zeta,...,1.
        byclass={r['class']:r for r in author['worst']}
        assert set(byclass)=={r['class'] for r in worst}
        for r in worst:
            am=byclass[r['class']]['multiplicities'];assert r['multiplicities_zero_first']==am[-1:]+am[:-1]
        standard=a==n-1
        if standard:assert t['character_parameters'][i][1] in ([n-1,1],[2]+[1]*(n-2))
        if not standard:
            assert a>=14 and minimum>=F(1,7)
            if name.startswith('Alt'):assert minimum>=F(1,5)
        if a<=15:small.append({'name':name,'row':i+1,'degree':a,'standard':standard,'ratio':str(minimum),'parameter':t['character_parameters'][i]})
        if name.startswith('Alt') and not all(is_real(z) for z in c):
            assert a>15 and not standard
            nonreal.append({'name':name,'row':i+1,'degree':a})
        if not standard and a==14:
            assert n==8 and minimum>=F(1,4)
            assert t['character_parameters'][i][1] in ([4,4],[2,2,2,2])
        if standard:assert minimum>=F(1,n-1)
        rtable['rows'].append({'row':i+1,'degree':a,'parameter':t['character_parameters'][i],
                             'minimum_ratio':str(minimum),'standard':standard,'worst':worst})
    records.append(rtable)
assert rows==682 and entries==49650
assert [(x['name'],x['degree']) for x in small if not x['standard']]==[('Alt(8)',14),('Sym(8)',14),('Sym(8)',14)]
tensor_bounds=[{'n':n,'factor_degree':n-1,'degree_upper':str(F(6*(n-1),11-n)),'two_factor_minimum':(n-1)**2} for n in (8,9,10)]
assert all(F(x['degree_upper'])<x['two_factor_minimum'] for x in tensor_bounds)
out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
 'scope':'all14 complete generic character inputs, independent row selection, seven fusions and all49650 spectra; published generic algorithm/group identification retained',
 'tables':len(tables),'rows':rows,'nonscalar_entries':entries,'small_rows':small,'nonreal_core_rows':nonreal,
 'standard_tensor_bounds':tensor_bounds,'complete_rows':records,'seconds':round(time.monotonic()-start,3)}
(BASE/'alternating_small_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('complete_rows','small_rows','nonreal_core_rows')}))
