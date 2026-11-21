#!/usr/bin/env python3
"""Exact independent reconstruction from retained complete tables, no GAP scan."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import hashlib,json,sys,time

BASE=Path(__file__).resolve().parent;ROOT=BASE.parents[1]
sys.path.insert(0,str(ROOT/'agents/g34_eightfolds/bireflection'))
from check_a1_spectra import spectrum,encode
from check_unitary_weil import equal
from audit_sporadic_input import abs_square

def main():
    start=time.monotonic();raw=(BASE/'small_inputs.json').read_bytes();data=json.loads(raw)
    ts={t['name']:t for t in data['tables']};assert len(ts)==len(data['tables'])==47
    chars={n:[[encode(v) for v in row] for row in t['characters']] for n,t in ts.items()}
    out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
         'method':'exact polynomial restriction matching, full Fourier spectra, normal fusions and cyclic quotient checks; no GAP scan imported',
         'tables':[],'rows':0,'spectra':0,'normal_fusions':0}
    for name,t in ts.items():
        cs=chars[name];cn=t.get('core',name);core=ts[cn];cc=chars[cn]
        assert len(cs)==len(t['orders'])==len(t['sizes'])
        assert sum(t['sizes'])==sum(c[0]**2 for c in cs)==t['order']
        assert t['sizes'][0]==t['orders'][0]==1
        fus=t.get('fusion',list(range(1,len(cc)+1)))
        if 'core' in t:
            assert len(fus)==len(cc) and [i for i,j in enumerate(fus) if j==1]==[0]
            assert all(o==t['orders'][j-1] for o,j in zip(core['orders'],fus))
            assert all(sum(s for s,k in zip(core['sizes'],fus) if k==j)==t['sizes'][j-1] for j in set(fus))
            pms={r['prime']:r['map'] for r in t['power_maps']}
            for pm in core['power_maps']:
                assert all(fus[k-1]==pms[pm['prime']][j-1] for j,k in zip(fus,pm['map']))
            d=t['order']//core['order'];linear=[c for c in cs if c[0]==1]
            assert d in (2,3,4,6) and len(linear)==d
            assert all(all(equal(c[j-1],1) for j in fus) for c in linear)
            assert any(any(any(v==1 and t['orders'][j]//gcd(t['orders'][j],k)==d
                               for k,v in enumerate(spectrum(t,c,j)))
                           for j in range(len(c))) for c in linear)
            out['normal_fusions']+=1
        core_by_degree={}
        for k,c in enumerate(cc):core_by_degree.setdefault(c[0],[]).append(k)
        selected=[i for i,c in enumerate(cs) if c[0]>1 and any(
            all(equal(c[j-1],v) for j,v in zip(fus,cc[k])) for k in core_by_degree.get(c[0],[]))]
        rr={'name':name,'selected_rows':[i+1 for i in selected],'spectra':0,'row_bounds':[]}
        for i in selected:
            c=cs[i];a=c[0];nus=[]
            for j,z in enumerate(c):
                if abs_square(z)[1]==(a*a,):continue
                ms=spectrum(t,c,j)
                assert all(isinstance(x,int) and x>=0 for x in ms) and sum(ms)==a
                nu=a-max(ms);assert 4*nu>=a,(name,i+1,j+1,a,nu)
                nus.append(nu)
            assert nus
            rr['row_bounds'].append({'row':i+1,'degree':a,'min_nu':min(nus),'min_ratio':str(F(min(nus),a)),'spectra':len(nus)})
            rr['spectra']+=len(nus)
        assert selected
        rr['minimum_degree']=min(cs[i][0] for i in selected)
        rr['minimum_ratio']=str(min(F(row['min_nu'],row['degree']) for row in rr['row_bounds']))
        assert rr['minimum_degree']>=6
        out['rows']+=len(selected);out['spectra']+=rr['spectra'];out['tables'].append(rr)
    # Universal-cover row6 is allowed by the coarse e<=6 budget, but exact
    # integral quarter-support gives 12*ceil(6/4)=24>18. Every tensor has >=36.
    assert 12*2>2*6+6 and 6*6>24
    assert min(t['minimum_degree'] for t in out['tables'])==6
    assert all(F(t['minimum_ratio'])>=F(1,4) for t in out['tables'])
    out['seconds']=round(time.monotonic()-start,6)
    (BASE/'small_checked.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='tables'},indent=2))
    print(json.dumps([{k:t[k] for k in ('name','minimum_degree','minimum_ratio','spectra')} for t in out['tables']],indent=2))

if __name__=='__main__':main()
