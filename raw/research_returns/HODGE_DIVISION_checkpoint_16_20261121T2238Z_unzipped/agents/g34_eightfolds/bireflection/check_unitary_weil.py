#!/usr/bin/env python3
"""Exact reconstruction of the unitary endpoint; independent of the GAP scan."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,lcm,ceil
import hashlib,json,time
from check_a1_spectra import spectrum,encode
from audit_sporadic_input import abs_square,reduce_poly

BASE=Path(__file__).resolve().parent
P=BASE/'unitary_weil/unitary_weil_inputs.json'
SPECS={'U3(3)':(6,7),'U5(2)':(10,),'U6(2)':(22,)}
NAMES=['U3(3)','U3(3).2','U5(2)','U5(2).2','U6(2)','U6(2).2','U6(2).3']

def equal(x,y):
    if isinstance(x,int) and isinstance(y,int):return x==y
    nx,cx=(1,(x,)) if isinstance(x,int) else x
    ny,cy=(1,(y,)) if isinstance(y,int) else y
    n=lcm(nx,ny);v=[0]*n
    for j,c in enumerate(cx):v[j*(n//nx)]+=c
    for j,c in enumerate(cy):v[j*(n//ny)]-=c
    return reduce_poly(v,n)==(0,)

def main():
    start=time.monotonic();raw=P.read_bytes();data=json.loads(raw)
    ts={t['name']:t for t in data['tables']};assert set(ts)==set(NAMES)
    assert [ts[n]['extension_information'] for n in SPECS]==[['','2'],['','2'],['(2^2x3)','3.2']]
    chars={n:[[encode(v) for v in c] for c in t['characters']] for n,t in ts.items()}
    out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
         'method':'own polynomial restriction matching and complete Ramanujan Fourier; no GAP scan imported',
         'tables':[],'rows':0,'spectra':0,'normal_fusions':0}
    for name in NAMES:
        t=ts[name];cs=chars[name];cn=t.get('core',name);u=ts[cn];uc=chars[cn]
        degs=SPECS[cn];core_rows=[i for i,c in enumerate(uc) if c[0] in degs]
        assert 'origin: ATLAS of finite groups' in t['information']
        assert sum(t['sizes'])==sum(c[0]**2 for c in cs)==t['order']
        assert len(cs)==len(t['orders'])==len(t['sizes'])
        f=t.get('fusion',list(range(1,len(uc)+1)))
        if 'core' in t:
            assert [i for i,j in enumerate(f) if j==1]==[0]
            assert all(o==t['orders'][j-1] for o,j in zip(u['orders'],f))
            assert all(sum(s for s,jj in zip(u['sizes'],f) if jj==j)==t['sizes'][j-1] for j in set(f))
            pm={r['prime']:r['map'] for r in t['power_maps']}
            for r in u['power_maps']:
                assert all(f[k-1]==pm[r['prime']][j-1] for j,k in zip(f,r['map']))
            d=t['order']//u['order'];linear=[c for c in cs if c[0]==1]
            assert d in (2,3) and len(linear)==d
            assert any(any(any(v==1 and t['orders'][j]//gcd(t['orders'][j],k)==d
                               for k,v in enumerate(spectrum(t,c,j)))
                           for j in range(len(c))) for c in linear)
            out['normal_fusions']+=1
        rows=[i for i,c in enumerate(cs) if c[0] in degs and any(
            all(equal(c[j-1],z) for j,z in zip(f,uc[k])) for k in core_rows)]
        rr={'table':name,'selected_rows':[i+1 for i in rows],'spectra':0,'row_data':[]}
        for i in rows:
            c=cs[i];a=c[0];nus=[]
            for j,z in enumerate(c):
                if abs_square(z)[1]==(a*a,):continue
                ms=spectrum(t,c,j);assert sum(ms)==a and all(isinstance(x,int) and x>=0 for x in ms)
                nu=a-max(ms);assert (5 if cn=='U5(2)' else 4)*nu>=a
                nus.append(nu);rr['spectra']+=1;out['spectra']+=1
            rr['row_data'].append({'row':i+1,'degree':a,'indicator':t['indicators'][i],'min_nu':min(nus)})
            out['rows']+=1
        out['tables'].append(rr)
    assert out['rows']==17 and out['spectra']==754 and out['normal_fusions']==4
    assert [r['selected_rows'] for r in out['tables']]==[[2,3,4,5],[3,4,5,6],[2],[3,4],[2],[3,4],[4,5,6]]
    assert [z['min_nu'] for r in out['tables'] for z in r['row_data']]==[2,3,2,2,2,2,3,3,2,2,2,6,6,6,6,6,6]
    assert ts['U5(2)']['indicators'][1] in (-1,1)
    assert ts['U6(2)']['indicators'][1] in (-1,1)
    # Exact arithmetic endpoints. The written monotonicity proof supplies all n,q.
    A=lambda q,n:F(q**n-q,q+1)
    B=lambda q,n:F(q**(n-1)+2*q-1,q+1)
    a=lambda q,n,i:F(q**n+(q if i==0 else -1)*(-1)**n,q+1)
    assert A(4,4)-3*B(4,4)==F(39,5)>6
    assert A(7,3)-3*B(7,3)==F(75,4)>6
    for q in range(4,101):
        assert 2*q-F(9,(q+1)*(q+2))>0
        if q>=7:assert 2*q-3-F(6,(q+1)*(q+2))>0
    for n in range(3,101):
        assert B(3,n)<=a(3,n,1)/2
        if n>=4:assert 3*A(3,n)-5*B(3,n)==3**(n-1)-F(17,2)>12
        if n>=6:assert 4*a(2,n,1)-6*B(2,n)==F(2**n-4*(-1)**n-18,3)>=14
        if n>=7:assert 3*a(2,n,0)-5*B(2,n)==F(2**(n-1)+6*(-1)**n-15,3)>12
    assert 3*a(4,3,0)-5*B(4,3)==13>12
    assert 3*a(5,3,0)-5*B(5,3)==F(95,3)>12
    assert B(4,3)<a(4,3,1)/2 and B(5,3)<a(5,3,1)/2
    assert (a(2,5,1)-B(2,5))/(2*a(2,5,1))==F(7,33)
    assert 6/(12*F(7,33)-2)==11
    assert 12*ceil(F(7,3))>2*11+6
    assert 12*ceil(F(6,4))>2*6+6
    assert {pow(2,r,5) for r in range(4)}=={1,2,3,4}
    out['all_arithmetic_endpoints']='PASS; all-degree monotonicity in written proof'
    out['seconds']=round(time.monotonic()-start,6)
    (BASE/'check_unitary_weil.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='tables'},indent=2))

if __name__=='__main__':main()
