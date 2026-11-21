"""Exact second reconstruction from the complete A7-cover inputs.

This reuses the already reviewed Ramanujan Fourier helper, independently
of GAP's EigenvaluesChar. It is not advertised as a third new algorithm.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, sys, time

B=Path(__file__).resolve().parent
R=B.parents[1]
sys.path.insert(0,str(R/'agents/g34_eightfolds/bireflection'))
from check_a1_spectra import spectrum, encode
from audit_sporadic_input import abs_square, rational_mean_abs_square

def main():
    start=time.perf_counter()
    raw=(B/'inputs.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='185c2a90af296395c33ad8c7c5e839fadba5fffaeda3aacac2d99c8d20c906ab'
    D=json.loads(raw);ts={t['name']:t for t in D['tables']}
    assert set(ts)=={'6.A7','6.A7.2'}
    cs={name:[[encode(z) for z in row] for row in t['characters']] for name,t in ts.items()}
    u=ts['6.A7'];f=ts['6.A7.2']['fusion']
    assert u['extension_information']==['6','2']
    centers=[j for j,s in enumerate(u['sizes']) if s==1]
    assert len(centers)==6
    std=[i+1 for i,r in enumerate(cs['6.A7']) if r[0]==6 and all(r[j]==6 for j in centers)]
    assert std==[2]
    out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
         'method':'exact rational-trace row selection and reused reviewed Ramanujan Fourier, separate from GAP',
         'standard_core_row':2,'rows':0,'spectra':0,'tables':[],'quarter_exceptions':[]}
    for name,t in ts.items():
        chars=cs[name]
        assert 'origin: ATLAS of finite groups' in t['information']
        assert len(chars)==len(t['orders'])==len(t['sizes'])
        assert all(len(r)==len(chars) for r in chars)
        assert sum(r[0]**2 for r in chars)==sum(t['sizes'])==t['order']
        if 'core' in t:
            assert t['order']==2*u['order']
            assert len(f)==len(u['orders']) and [i for i,j in enumerate(f) if j==1]==[0]
            assert all(o==t['orders'][j-1] for o,j in zip(u['orders'],f))
            assert all(sum(s for s,k in zip(u['sizes'],f) if k==j)==t['sizes'][j-1] for j in set(f))
            pm={z['prime']:z['map'] for z in t['power_maps']}
            for z in u['power_maps']:
                assert all(f[k-1]==pm[z['prime']][j-1] for j,k in zip(f,z['map']))
        rec={'name':name,'rows':[],'spectra':0}
        for i,r in enumerate(chars):
            a=r[0]
            if a<=1:continue
            if 'core' in t:
                norm=sum(s*rational_mean_abs_square(r[j-1]) for s,j in zip(u['sizes'],f))/u['order']
                assert norm.denominator==1
                if norm!=1:continue
                restriction=[r[j-1] for j in f]
                matches=[j+1 for j,rr in enumerate(cs['6.A7']) if rr==restriction]
                assert len(matches)==1
                core_row=matches[0]
            else:core_row=i+1
            minimum=a
            for j,z in enumerate(r):
                if abs_square(z)[1]==(a*a,):continue
                ev=spectrum(t,r,j);nu=a-max(ev)
                minimum=min(minimum,nu)
                if 4*nu<a:
                    out['quarter_exceptions'].append({'table':name,'row':i+1,'core_row':core_row,
                                                      'class':j+1,'degree':a,'nu':nu,'spectrum':ev})
                out['spectra']+=1;rec['spectra']+=1
            if core_row!=2:assert 4*minimum>=a
            if a==4:assert minimum==2 and name=='6.A7'
            if a==6 and core_row!=2:assert minimum>=2 and name=='6.A7'
            rec['rows'].append({'row':i+1,'core_row':core_row,'degree':a,'min_nu':minimum,
                                'min_ratio':str(F(minimum,a))})
            out['rows']+=1
        out['tables'].append(rec)
    assert (out['rows'],out['spectra'])==(57,1884)
    assert [(len(t['rows']),t['spectra']) for t in out['tables']]==[(39,1326),(18,558)]
    assert {(x['table'],x['row'],x['core_row'],x['class'],x['degree'],x['nu']) for x in out['quarter_exceptions']}=={
        ('6.A7.2',3,2,26,6,1),('6.A7.2',4,2,26,6,1)}
    assert min(r['degree'] for r in out['tables'][0]['rows'])==4
    assert all(r['degree'] in (4,6) for r in out['tables'][0]['rows'] if r['degree']<=6)
    # Uniform nonstandard tensor budget and exact small endpoints.
    assert 12*F(1,4)-2==1 and 4**2>6
    assert 12*2>2*4+6 and 12*2>2*6+6
    # Standard a=6 tensor multiplier/trace budget.
    assert 2*F(11,18)+10*F(1,6)==F(26,9)
    assert 6/(F(26,9)-2)==F(27,4)<6**2
    out['seconds']=round(time.perf_counter()-start,6)
    (B/'checked.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='tables'},indent=2))

if __name__=='__main__':main()
