#!/usr/bin/env python3
"""Peer reconstruction: restriction inner products plus polynomial Fourier.

Reads only the original numerical input, not the author's selected rows or
scan output.  Reuses this reviewer's previously reviewed cyclotomic helper.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm
from functools import lru_cache
import hashlib,importlib.util,json,time
import sympy as sp

BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('owncyc',BASE.parent/'sporadic/verify_quarter_bound.py')
cyc=importlib.util.module_from_spec(spec);spec.loader.exec_module(cyc)
INPUT=BASE.parent.parent/'g34_eightfolds/bireflection/linear_weil/linear_weil_inputs.json'
NAMES=['3.L3(4)','3.L3(4).2_1','3.L3(4).2_2','3.L3(4).2_3','3.L3(4).3','3.L3(4).6']

def coefficients(z):return (1,(z,)) if isinstance(z,int) else z

@lru_cache(None)
def ramanujan(n,k):
    d=n//gcd(n,k)
    return int(sp.mobius(d))*int(sp.totient(n))//int(sp.totient(d))

@lru_cache(None)
def trace_product(a,b):
    na,aa=coefficients(a);nb,bb=coefficients(b);n=lcm(na,nb)
    value=sum(x*y*ramanujan(n,(i*(n//na)-j*(n//nb))%n)
              for i,x in enumerate(aa) if x for j,y in enumerate(bb) if y)
    return F(value,int(sp.totient(n)))

def main():
    start=time.monotonic();raw=INPUT.read_bytes();data=json.loads(raw)
    ts={t['name']:t for t in data['tables']};assert set(ts)==set(NAMES)
    assert data['simple_extension_info']==['(3x4^2)','D12']
    chars={n:[[cyc.key(z) for z in r] for r in t['characters']] for n,t in ts.items()}
    core=ts[NAMES[0]];targets=[r for r in chars[NAMES[0]] if r[0]==21]
    assert len(targets)==2
    out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
         'method':'independent restriction inner products and integer-polynomial Fourier',
         'tables':[],'rows':0,'spectra':0}
    for name in NAMES:
        t=ts[name];assert 'origin: ATLAS of finite groups' in t['information']
        cs=chars[name];assert len(cs)==len(t['orders'])==len(t['sizes'])
        assert sum(t['sizes'])==sum(c[0]**2 for c in cs)==t['order']
        fusion=t.get('fusion',list(range(1,len(core['orders'])+1)))
        assert len(fusion)==len(core['orders'])
        if name!=NAMES[0]:
            assert t['core']==NAMES[0]
            assert [i for i,j in enumerate(fusion) if j==1]==[0]
            assert all(o==t['orders'][j-1] for o,j in zip(core['orders'],fusion))
            assert all(sum(s for s,k in zip(core['sizes'],fusion) if k==j)==t['sizes'][j-1] for j in set(fusion))
            pm={p['prime']:p['map'] for p in t['power_maps']}
            for p in core['power_maps']:
                assert all(fusion[k-1]==pm[p['prime']][j-1] for j,k in zip(fusion,p['map']))
            quotient=t['order']//core['order'];linear=[c for c in cs if c[0]==1]
            assert len(linear)==quotient
            assert any(any(any(m==1 and t['orders'][j]//gcd(k,t['orders'][j])==quotient
                               for k,m in enumerate(cyc.cyclic_multiplicities(t,c,j)))
                           for j in range(len(c))) for c in linear)
        rr={'name':name,'selected_rows':[],'spectra':0,'row_results':[]}
        for i,c in enumerate(cs):
            if c[0]!=21:continue
            ips=[sum(s*trace_product(c[j-1],z) for s,j,z in zip(core['sizes'],fusion,target))/core['order'] for target in targets]
            assert all(a.denominator==1 and a>=0 for a in ips)
            if 1 not in ips:continue
            assert sum(ips)==1
            rr['selected_rows'].append(i+1);out['rows']+=1
            minimum=21;minimizers=[]
            for j,z in enumerate(c):
                if cyc.squared_norm(z)==(441,):continue
                ms=cyc.cyclic_multiplicities(t,c,j);nu=21-max(ms)
                assert nu>=8
                if nu<minimum:minimum=nu;minimizers=[]
                if nu==minimum:minimizers.append({'class':j+1,'order':t['orders'][j],'multiplicities':ms})
                rr['spectra']+=1;out['spectra']+=1
            assert minimum==8
            rr['row_results'].append({'row':i+1,'min_nu':minimum,'minimizers':minimizers})
        out['tables'].append(rr)
    assert [r['selected_rows'] for r in out['tables']]==[[17,18],[27,28,29,30],[],[],list(range(25,31)),list(range(31,43))]
    assert out['rows']==24 and out['spectra']==1288
    out['seconds']=round(time.monotonic()-start,3)
    (BASE/'independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='tables'}))

if __name__=='__main__':main()
