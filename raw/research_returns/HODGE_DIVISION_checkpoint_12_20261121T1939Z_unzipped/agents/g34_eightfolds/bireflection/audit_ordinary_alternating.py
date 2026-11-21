#!/usr/bin/env python3
"""Independent complete ordinary A6 spectral audit for HD-ALT-01.

Uses our rational Ramanujan-Fourier implementation, not root's
cyclotomic-polynomial arithmetic. All spectra are computed before comparison.
"""
from pathlib import Path
from fractions import Fraction
import hashlib,json
from check_a1_spectra import spectrum,encode

BASE=Path(__file__).resolve().parent
WORK=BASE.parents[2]
P=WORK/'agents/imprimitive/sporadic/alternating_cover_inputs.json'

def main():
    raw=P.read_bytes();data=json.loads(raw)
    assert hashlib.sha256(raw).hexdigest()=='d41d9bcb33344ce8d655dd83aa90f4a58ffc4f00a5cd22271c72895c22e7d26c'
    t=next(t for t in data['tables'] if t['name']=='2.A6')
    z=next(j for j,s in enumerate(t['sizes']) if s==1 and t['orders'][j]==2)
    rows=[];count=0
    for i,rawc in enumerate(t['characters']):
        c=[encode(v) for v in rawc]
        if c[0]<=1 or c[z]!=c[0]:continue
        entries=[]
        for j,s in enumerate(t['sizes']):
            if s==1:continue
            ms=spectrum(t,c,j);nu=c[0]-max(ms)
            assert 5*nu>=2*c[0]
            entries.append({'class':j+1,'order':t['orders'][j],
                            'multiplicities_zero_first':list(ms),'nu':nu})
            count+=1
        rows.append({'row':i+1,'degree':c[0],
                     'minimum_nu_over_degree':str(min(Fraction(r['nu'],c[0]) for r in entries)),
                     'entries':entries})
    assert count==66
    assert [r['degree'] for r in rows]==[5,5,8,8,9,10]
    assert [r['minimum_nu_over_degree'] for r in rows]==['2/5','2/5','1/2','1/2','4/9','2/5']
    root=json.loads((WORK/'research/alternating_local_certificate.json').read_text())
    assert len(root['rows'])==len(rows)
    for ar,rr in zip(rows,root['rows']):
        assert (ar['row'],ar['degree'])==(rr['row'],rr['degree'])
        assert len(ar['entries'])==len(rr['entries'])
        for a,r in zip(ar['entries'],rr['entries']):
            assert a['class']==r['class']
            assert a['multiplicities_zero_first']==r['multiplicities_zero_first']
            assert a['nu']==r['moving_rank']
    out={'status':'PASS','method':'independent Ramanujan Fourier; no root arithmetic imported',
         'input_sha256':hashlib.sha256(raw).hexdigest(),'entries':count,'rows':rows}
    (BASE/'audit_ordinary_alternating.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'}))

if __name__=='__main__':main()
