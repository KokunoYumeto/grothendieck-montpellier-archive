#!/usr/bin/env python3
"""Full four-table reconstruction independent of the GAP scan result."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import hashlib,importlib.util,json,time

BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cyc',BASE.parent/'sporadic/verify_quarter_bound.py')
cyc=importlib.util.module_from_spec(spec);spec.loader.exec_module(cyc)
NAMES=['S4(4)','S4(4).2','S4(4).4','2.S6(2)']

def main():
    start=time.monotonic();raw=(BASE/'even_symplectic_small_inputs.json').read_bytes()
    data=json.loads(raw);ts={t['name']:t for t in data['tables']}
    assert set(ts)==set(NAMES)
    assert {m['name']:m['extension_info'] for m in data['metadata']}=={'S4(4)':['','4'],'S6(2)':['2','']}
    cs={n:[[cyc.key(z) for z in c] for c in t['characters']] for n,t in ts.items()}
    out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),'tables':[],'rows':0,'spectra':0}
    for name,n in zip(NAMES,[27,30,30,43]):
        t=ts[name];chars=cs[name]
        assert 'origin: ATLAS of finite groups' in t['information']
        assert len(chars)==len(t['orders'])==len(t['sizes'])==n
        assert sum(c[0]**2 for c in chars)==sum(t['sizes'])==t['order']
        if 'core' in t:
            assert t['core']=='S4(4)';u=ts['S4(4)'];fusion=t['fusion']
            d=2 if name.endswith('.2') else 4
            assert t['order']==d*u['order'] and len(fusion)==len(u['orders'])
            assert [i for i,j in enumerate(fusion) if j==1]==[0]
            assert all(o==t['orders'][j-1] for o,j in zip(u['orders'],fusion))
            assert all(sum(s for s,k in zip(u['sizes'],fusion) if k==j)==t['sizes'][j-1] for j in set(fusion))
            pm={p['prime']:p['map'] for p in t['power_maps']}
            for p in u['power_maps']:
                assert all(fusion[k-1]==pm[p['prime']][j-1] for j,k in zip(fusion,p['map']))
            linear=[c for c in chars if c[0]==1];assert len(linear)==d
            assert any(any(any(m==1 and t['orders'][j]//gcd(k,t['orders'][j])==d
                               for k,m in enumerate(cyc.cyclic_multiplicities(t,c,j)))
                           for j in range(n)) for c in linear)
        rr={'name':name,'selected_rows':[],'row_bounds':[],'spectra':0,'quarter_failures':[]}
        for i,c in enumerate(chars):
            a=c[0]
            if a==1:continue
            if 'core' in t and tuple(c[j-1] for j in t['fusion']) not in {tuple(r) for r in cs['S4(4)']}:continue
            rr['selected_rows'].append(i+1);out['rows']+=1;minimum=F(1)
            for j,z in enumerate(c):
                if cyc.squared_norm(z)==(a*a,):continue
                ms=cyc.cyclic_multiplicities(t,c,j);ratio=F(a-max(ms),a)
                minimum=min(minimum,ratio);out['spectra']+=1;rr['spectra']+=1
            if name!='2.S6(2)':assert minimum>=F(1,3)
            elif a==7:
                assert minimum==F(1,7) and all(isinstance(z,int) for z in c)
                squaremap=next(p['map'] for p in t['power_maps'] if p['prime']==2)
                indicator=F(sum(s*c[j-1] for s,j in zip(t['sizes'],squaremap)),t['order'])
                assert indicator==t['indicators'][i]==1
            else:
                assert minimum>=F(2,9)
                if a==8:assert minimum>=F(1,4)
            if minimum<F(1,4):rr['quarter_failures'].append({'row':i+1,'degree':a,'ratio':str(minimum)})
            rr['row_bounds'].append({'row':i+1,'degree':a,'minimum_ratio':str(minimum)})
        out['tables'].append(rr)
    assert [len(t['selected_rows']) for t in out['tables']]==[26,20,16,42]
    assert [t['spectra'] for t in out['tables']]==[676,580,464,1722]
    assert out['rows']==104 and out['spectra']==3442
    rows=out['tables'][-1]['row_bounds']
    assert [r['degree'] for r in rows if r['degree']<=9]==[7,8]
    assert out['tables'][-1]['quarter_failures']==[
        {'row':2,'degree':7,'ratio':'1/7'},
        {'row':5,'degree':21,'ratio':'5/21'},
        {'row':6,'degree':27,'ratio':'2/9'}]
    assert all(min(r['degree'] for r in t['row_bounds'])==18 for t in out['tables'][:3])
    out['seconds']=round(time.monotonic()-start,3)
    (BASE/'check_even_symplectic_small.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='tables'}))

if __name__=='__main__':main()
