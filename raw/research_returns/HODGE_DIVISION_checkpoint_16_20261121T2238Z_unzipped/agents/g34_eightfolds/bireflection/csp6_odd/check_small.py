#!/usr/bin/env python3
"""Separate polynomial-Fourier reconstruction of every small C3 spectrum."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import json,sys,hashlib,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from check_a1_spectra import spectrum,encode
from audit_sporadic_input import abs_square,rational_mean_abs_square

B=Path(__file__).resolve().parent

def main():
    start=time.perf_counter();raw=(B/'small_inputs.json').read_bytes();D=json.loads(raw)
    ts={t['name']:t for t in D['tables']};assert set(ts)=={'2.S6(3)','2.S6(3).2'}
    cs={name:[[encode(x) for x in r] for r in t['characters']] for name,t in ts.items()}
    out={'status':'PASS separate exact Fourier','input_sha256':hashlib.sha256(raw).hexdigest(),
         'rows':0,'spectra':0,'tables':[]}
    for name,t in ts.items():
        chars=cs[name];assert 'origin: ATLAS of finite groups' in t['information']
        assert sum(r[0]**2 for r in chars)==sum(t['sizes'])==t['order']
        if 'core' in t:
            u=ts[t['core']];f=t['fusion'];assert t['order']==2*u['order']
            assert len(f)==len(u['orders']) and [i for i,j in enumerate(f) if j==1]==[0]
            assert all(o==t['orders'][j-1] for o,j in zip(u['orders'],f))
            assert all(sum(s for s,k in zip(u['sizes'],f) if k==j)==t['sizes'][j-1] for j in set(f))
            pm={p['prime']:p['map'] for p in t['power_maps']}
            for p in u['power_maps']:
                assert all(f[k-1]==pm[p['prime']][j-1] for j,k in zip(f,p['map']))
            assert len([r for r in chars if r[0]==1])==2
        else:assert t['extension_information']==['2','2']
        rec={'name':name,'rows':[],'spectra':0}
        for i,r in enumerate(chars):
            a=r[0]
            if a<=1:continue
            if 'core' in t:
                norm=sum(s*rational_mean_abs_square(r[j-1]) for s,j in zip(u['sizes'],f))/u['order']
                assert norm.denominator==1
                if norm!=1:continue
                assert tuple(r[j-1] for j in f) in {tuple(x) for x in cs[t['core']]}
            mins=[]
            for j,z in enumerate(r):
                if abs_square(z)[1]==(a*a,):continue
                ev=spectrum(t,r,j);nu=a-max(ev);assert 4*nu>=a
                mins.append(F(nu,a));out['spectra']+=1;rec['spectra']+=1
            rec['rows'].append({'row':i+1,'degree':a,'minimum_ratio':str(min(mins))});out['rows']+=1
        rec['minimum_degree']=min(x['degree'] for x in rec['rows'])
        rec['minimum_ratio']=str(min(F(x['minimum_ratio']) for x in rec['rows']));out['tables'].append(rec)
    assert (out['rows'],out['spectra'])==(228,31428)
    assert [(len(t['rows']),t['spectra'],t['minimum_degree'],t['minimum_ratio']) for t in out['tables']]==[(140,19460,13,'2/7'),(88,11968,78,'8/21')]
    out['seconds']=round(time.perf_counter()-start,6)
    (B/'small_checked.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='tables'},indent=2))

if __name__=='__main__':main()
