#!/usr/bin/env python3
"""Peer endpoint reconstruction by restriction inner products and polynomial DFT.

Reads only the exported original character tables, never the author's selected
rows, scan output, spectrum code, or Ramanujan-spectrum implementation.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import gcd,lcm
import hashlib,importlib.util,json,time
import sympy as sp

BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('owncyc',BASE.parent/'sporadic/verify_quarter_bound.py')
cyc=importlib.util.module_from_spec(spec);spec.loader.exec_module(cyc)
INPUT=BASE.parent.parent/'g34_eightfolds/bireflection/unitary_weil/unitary_weil_inputs.json'
SPECS={'U3(3)':(6,7),'U5(2)':(10,),'U6(2)':(22,)}
NAMES=['U3(3)','U3(3).2','U5(2)','U5(2).2','U6(2)','U6(2).2','U6(2).3']

def coeff(z):return (1,(z,)) if isinstance(z,int) else z

@lru_cache(None)
def ramanujan(n,k):
    d=n//gcd(n,k)
    return int(sp.mobius(d))*int(sp.totient(n))//int(sp.totient(d))

@lru_cache(None)
def normalized_trace_product(a,b):
    na,aa=coeff(a);nb,bb=coeff(b);n=lcm(na,nb)
    value=sum(x*y*ramanujan(n,(i*(n//na)-j*(n//nb))%n)
              for i,x in enumerate(aa) if x for j,y in enumerate(bb) if y)
    return F(value,int(sp.totient(n)))

def main():
    start=time.monotonic();raw=INPUT.read_bytes();data=json.loads(raw)
    ts={t['name']:t for t in data['tables']};assert set(ts)==set(NAMES)
    chars={n:[[cyc.key(z) for z in row] for row in t['characters']] for n,t in ts.items()}
    assert [ts[n]['extension_information'] for n in SPECS]==[['','2'],['','2'],['(2^2x3)','3.2']]
    out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
         'method':'own normalized-trace restriction inner products; own integer-polynomial Fourier',
         'tables':[],'rows':0,'spectra':0,'normal_fusions':0}
    for name in NAMES:
        t=ts[name];cn=t.get('core',name);core=ts[cn];cs=chars[name]
        targets=[c for c in chars[cn] if c[0] in SPECS[cn]]
        assert 'origin: ATLAS of finite groups' in t['information']
        assert sum(t['sizes'])==sum(c[0]**2 for c in cs)==t['order']
        assert len(cs)==len(t['orders'])==len(t['sizes'])
        fusion=t.get('fusion',list(range(1,len(core['orders'])+1)))
        assert len(fusion)==len(core['orders'])
        if 'core' in t:
            assert [i for i,j in enumerate(fusion) if j==1]==[0]
            assert all(o==t['orders'][j-1] for o,j in zip(core['orders'],fusion))
            assert all(sum(s for s,k in zip(core['sizes'],fusion) if k==j)==t['sizes'][j-1] for j in set(fusion))
            pm={p['prime']:p['map'] for p in t['power_maps']}
            for p in core['power_maps']:
                assert all(fusion[k-1]==pm[p['prime']][j-1] for j,k in zip(fusion,p['map']))
            quotient=t['order']//core['order'];linear=[c for c in cs if c[0]==1]
            assert quotient in (2,3) and len(linear)==quotient
            assert any(any(any(m==1 and t['orders'][j]//gcd(k,t['orders'][j])==quotient
                               for k,m in enumerate(cyc.cyclic_multiplicities(t,c,j)))
                           for j in range(len(c))) for c in linear)
            out['normal_fusions']+=1
        rr={'table':name,'selected_rows':[],'spectra':0,'rows':[]}
        for i,c in enumerate(cs):
            a=c[0]
            if a not in SPECS[cn]:continue
            ips=[sum(s*normalized_trace_product(c[j-1],z)
                     for s,j,z in zip(core['sizes'],fusion,target))/core['order']
                 for target in targets]
            assert all(z.denominator==1 and z>=0 for z in ips)
            if 1 not in ips:continue
            assert sum(ips)==1
            rr['selected_rows'].append(i+1);out['rows']+=1
            minimum=a;minimizers=[]
            for j,z in enumerate(c):
                if cyc.squared_norm(z)==(a*a,):continue
                ms=cyc.cyclic_multiplicities(t,c,j)
                assert sum(ms)==a and all(isinstance(v,int) and v>=0 for v in ms)
                nu=a-max(ms)
                assert (5 if cn=='U5(2)' else 4)*nu>=a
                if nu<minimum:minimum=nu;minimizers=[]
                if nu==minimum:minimizers.append({'class':j+1,'order':t['orders'][j],'multiplicities':ms})
                rr['spectra']+=1;out['spectra']+=1
            # Reconstruct the Frobenius--Schur indicator directly from power2.
            pm2=next(p['map'] for p in t['power_maps'] if p['prime']==2)
            fs=sum(s*normalized_trace_product(c[j-1],1) for s,j in zip(t['sizes'],pm2))/t['order']
            assert fs==t['indicators'][i]
            if name==cn and cn in ('U5(2)','U6(2)'):assert fs in (-1,1)
            rr['rows'].append({'row':i+1,'degree':a,'min_nu':minimum,
                               'indicator':int(fs),'minimizers':minimizers})
        out['tables'].append(rr)
    assert out['rows']==17 and out['spectra']==754 and out['normal_fusions']==4
    assert [r['selected_rows'] for r in out['tables']]==[[2,3,4,5],[3,4,5,6],[2],[3,4],[2],[3,4],[4,5,6]]
    assert [z['min_nu'] for r in out['tables'] for z in r['rows']]==[2,3,2,2,2,2,3,3,2,2,2,6,6,6,6,6,6]
    # Independent endpoint arithmetic. The proof supplies monotonicity for all n,q.
    endpoint={
      'q4_n4_A_minus_3B':F(4**4-4-3*(4**3+8-1),5),
      'q7_n3_A_minus_3B':F(7**3-7-3*(7**2+14-1),8),
      'q4_n3_selfdual_3a_minus_5B':3*12-5*F(23,5),
      'q5_n3_selfdual_3a_minus_5B':3*20-5*F(17,3),
      'q2_n5_gamma':F(11-F(19,3),22)}
    assert list(endpoint.values())==[F(39,5),F(75,4),F(13),F(95,3),F(7,33)]
    assert 12*3>2*11+6 and 12*2>2*6+6
    out['endpoint_arithmetic']={k:str(v) for k,v in endpoint.items()}
    out['seconds']=round(time.monotonic()-start,3)
    (BASE/'independent_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='tables'},indent=2))

if __name__=='__main__':main()
