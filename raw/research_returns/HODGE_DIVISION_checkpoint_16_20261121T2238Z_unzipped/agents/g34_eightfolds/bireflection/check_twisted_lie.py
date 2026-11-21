#!/usr/bin/env python3
"""Exact Suzuki/Ree input audit using independent rational/Fourier arithmetic."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,time
from check_a1_spectra import spectrum,encode
from audit_sporadic_input import rational_mean_abs_square,abs_square

BASE=Path(__file__).resolve().parent
P=BASE/'twisted_lie/twisted_character_inputs.json'
EXPECTED={"2^2.Sz(8)","2^2.Sz(8).3","R(27)","2F4(2)'","2F4(8)"}

def main():
    start=time.time();raw=P.read_bytes();data=json.loads(raw)
    ts={t['name']:t for t in data['tables']};assert set(ts)==EXPECTED
    metadata={t['name']:t for t in data['core_metadata']}
    assert set(metadata)=={'Sz(8)','R(27)',"2F4(2)'",'2F4(8)'}
    assert metadata['Sz(8)']['extension_info']==['2^2','3']
    assert metadata['R(27)']['extension_info']==['','3']
    assert metadata["2F4(2)'"]['extension_info']==['','2']
    assert metadata['2F4(8)']['extension_info']==['','3']
    chars={n:[[encode(v) for v in row] for row in t['characters']] for n,t in ts.items()}
    out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
         'method':'independent rational restriction norms, complete Ramanujan spectra for Suzuki, coefficient-L1 bounds for all Ree/Tits values',
         'tables':[],'rows':0,'entries':0,'spectral_entries':0,'trace_entries':0}
    for name,t in ts.items():
        if name=='2F4(8)':assert 'source: Gunter Malle' in t['information']
        else:assert 'origin: ATLAS of finite groups' in t['information']
        cs=chars[name]
        assert len(cs)==len(t['orders'])==len(t['sizes'])
        assert sum(c[0]**2 for c in cs)==sum(t['sizes'])==t['order']
        rows=[]
        for i,c in enumerate(cs):
            if c[0]<=1:continue
            if 'core' in t:
                u=ts[t['core']]
                norm=sum(s*rational_mean_abs_square(c[j-1]) for s,j in zip(u['sizes'],t['fusion']))/u['order']
                assert norm.denominator==1
                if norm!=1:continue
            rows.append(i)
        if 'core' in t:
            u=ts[t['core']];f=t['fusion'];assert t['order']==3*u['order']
            assert len(f)==len(u['orders'])
            assert [i for i,j in enumerate(f) if j==1]==[0]
            assert all(o==t['orders'][j-1] for o,j in zip(u['orders'],f))
            assert all(sum(s for s,jj in zip(u['sizes'],f) if jj==j)==t['sizes'][j-1] for j in set(f))
            pm={r['prime']:r['map'] for r in t['power_maps']}
            for r in u['power_maps']:
                assert all(f[k-1]==pm[r['prime']][j-1] for j,k in zip(f,r['map']))
        rec={'table':name,'rows':len(rows),'minimum_degree':min(cs[i][0] for i in rows),'entries':0,'row_data':[]}
        for i in rows:
            c=cs[i];a=c[0];values=[];rr={'row':i+1,'degree':a}
            for j,z in enumerate(c):
                if abs_square(z)[1]==(a*a,):continue
                if 'Sz(8)' in name:
                    ms=spectrum(t,c,j);nu=a-max(ms);assert 4*nu>=a
                    values.append(F(nu,a));out['spectral_entries']+=1
                else:
                    l1=abs(z) if isinstance(z,int) else sum(abs(v) for v in z[1])
                    assert 4*l1<=a
                    values.append(F(l1,a));out['trace_entries']+=1
                rec['entries']+=1;out['entries']+=1
            rr['bound']=str(min(values) if 'Sz(8)' in name else max(values))
            rec['row_data'].append(rr);out['rows']+=1
        rec['bound']=str(min(F(r['bound']) for r in rec['row_data']) if 'Sz(8)' in name else max(F(r['bound']) for r in rec['row_data']))
        out['tables'].append(rec)
    assert out['rows']==213 and out['entries']==15471
    assert out['spectral_entries']==1330 and out['trace_entries']==14141
    assert [t['minimum_degree'] for t in out['tables']]==[14,14,703,26,64638]
    assert [t['bound'] for t in out['tables']]==['3/7','3/7','26/703','3/13','449/32319']
    # Exact large-field constants. The elementary polynomial proof handles
    # every q>=32; the first admissible values are retained here as witnesses.
    assert 5**2<32 and F(1,4)<F(9,32)  # sqrt32>5
    assert 1-F(9,32)==F(23,32)
    assert 6/(12*F(23,128)-2)==F(192,5)
    assert 14**2>F(192,5) and 124>F(192,5) and 26>24
    out['large_field_minima_at_first_parameters']={
        'Suzuki32':(32-1)*4,
        'Ree243':243**2-243+1,
        'large_Ree32':(32-1)*4*(32+1)**2*(32**2-32+1),
    }
    out['seconds']=round(time.time()-start,3)
    (BASE/'check_twisted_lie.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='tables'}))

if __name__=='__main__':main()
