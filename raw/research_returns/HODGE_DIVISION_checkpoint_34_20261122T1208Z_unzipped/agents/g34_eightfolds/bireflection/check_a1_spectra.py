#!/usr/bin/env python3
"""Independent all-spectrum reconstruction of the 33 small-A1 tables."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
from math import gcd
import hashlib,json,time
import sympy as sp
from audit_sporadic_input import encode,rational_mean_abs_square,ramanujan,abs_square

BASE=Path(__file__).resolve().parent
P=BASE/'a1/a1_character_inputs.json'
EXPECTED={
    '2.A5':['2.A5.2'], '2.L3(2)':['2.L3(2).2'],
    'L2(8)':['L2(8).3'], '6.A6':['6.A6.2_1','6.A6.2_2'],
    '3.A6':['3.A6.2_3'],
    '2.L2(11)':['2.L2(11).2'], '2.L2(13)':['2.L2(13).2'],
    'L2(16)':['L2(16).2','L2(16).4'],
    '2.L2(17)':['2.L2(17).2'], '2.L2(19)':['2.L2(19).2'],
    '2.L2(23)':['2.L2(23).2'],
    '2.L2(25)':['2.L2(25).2_1','2.L2(25).2_2'],
    'L2(25)':['L2(25).2_3'],
    '2.L2(27)':['2.L2(27).2','2.L2(27).3','2.L2(27).6'],
}


@lru_cache(None)
def reconstruct(n,traces):
    den=n*int(sp.totient(n))
    ms=[]
    for k in range(n):
        a=sum(c*ramanujan(n,(b-k*r)%n)
              for r,t in enumerate(traces) for b,c in t)
        assert a>=0 and a%den==0
        ms.append(a//den)
    return tuple(ms)


def spectrum(t,c,j):
    n=t['orders'][j];e=c[0];tr=[((0,e),)]
    for r in range(1,n):
        d=gcd(n,r);jj=j;dd=d
        for rec in t['power_maps']:
            p=rec['prime']
            while dd>1 and dd%p==0:
                jj=rec['map'][jj]-1;dd//=p
        assert dd==1
        z=c[jj]
        if isinstance(z,int):tr.append(((0,z),))
        else:
            f,cs=z;assert (n//d)%f==0
            tr.append(tuple(((b*(n//f)*(r//d))%n,a) for b,a in enumerate(cs) if a))
    ms=reconstruct(n,tuple(tr));assert sum(ms)==e
    return ms


def main():
    started=time.time();raw=P.read_bytes()
    sha=hashlib.sha256(raw).hexdigest()
    assert sha=='5ed905449e1f6f64f3eb18b27a213fc5c72e0731dbd591670166e8763ad7fc88'
    data=json.loads(raw);tables={t['name']:t for t in data['tables']}
    assert len(tables)==33
    assert set(tables)==set(EXPECTED)|{x for xs in EXPECTED.values() for x in xs}
    fusions_checked=0
    for core,names in EXPECTED.items():
        u=tables[core];assert 'core' not in u
        for name in names:
            t=tables[name];assert t['core']==core
            fusion=t['fusion'];assert len(fusion)==len(u['orders'])
            assert t['order']//u['order'] in (2,3,4,6)
            assert t['order']%u['order']==0
            assert [i for i,j in enumerate(fusion) if j==1]==[0]
            assert all(o==t['orders'][j-1] for o,j in zip(u['orders'],fusion))
            for j in set(fusion):
                assert sum(s for s,k in zip(u['sizes'],fusion) if k==j)==t['sizes'][j-1]
            powers={rec['prime']:rec['map'] for rec in t['power_maps']}
            for rec in u['power_maps']:
                assert all(fusion[k-1]==powers[rec['prime']][j-1]
                           for j,k in zip(fusion,rec['map']))
            fusions_checked+=1
    assert fusions_checked==19
    out={'status':'PASS','input_sha256':sha,'method':'independent rational-trace row selection and Ramanujan Fourier on every nonscalar entry',
         'complete_table_identifiers_checked':len(tables),'normal_core_fusions_checked':fusions_checked,
         'tables':[],'rows':0,'entries':0,'quarter_failures':[],'fifth_failures':[]}
    for name,t in tables.items():
        assert 'origin: ATLAS of finite groups' in t['information']
        chars=[[encode(z) for z in c] for c in t['characters']]
        assert len(chars)==len(t['orders'])==len(t['sizes'])
        assert sum(c[0]**2 for c in chars)==sum(t['sizes'])==t['order']
        rows=[]
        for i,c in enumerate(chars):
            if c[0]<=1:continue
            if 'core' in t:
                u=tables[t['core']]
                norm=sum(s*rational_mean_abs_square(c[j-1])
                         for s,j in zip(u['sizes'],t['fusion']))/u['order']
                assert norm.denominator==1
                if norm!=1:continue
            rows.append(i)
        record={'table':name,'rows':[]}
        for i in rows:
            c=chars[i];e=c[0];ratios=[];out['rows']+=1
            for j,z in enumerate(c):
                _,a=abs_square(z)
                if a==(e*e,):continue
                ms=spectrum(t,c,j);nu=e-max(ms);ratios.append(F(nu,e));out['entries']+=1
                w={'table':name,'row':i+1,'class':j+1,'degree':e,'nu':nu,'multiplicities_zero_first':ms}
                if 4*nu<e:out['quarter_failures'].append(w)
                if 5*nu<e:out['fifth_failures'].append(w)
            record['rows'].append({'row':i+1,'degree':e,'minimum_nu_over_degree':str(min(ratios))})
        out['tables'].append(record)
    assert out['rows']==654 and out['entries']==18922
    assert not out['fifth_failures']
    assert len(out['quarter_failures'])==4
    assert {(w['table'],w['row'],w['class'],w['degree'],w['nu']) for w in out['quarter_failures']}=={
        ('6.A6.2_1',3,20,5,1),('6.A6.2_1',4,20,5,1),
        ('6.A6.2_1',5,21,5,1),('6.A6.2_1',6,21,5,1)}
    # Identify their core restrictions independently from the complete rows.
    u=tables['6.A6'];ext=tables['6.A6.2_1'];uc=[[encode(z) for z in c] for c in u['characters']]
    out['exception_core_rows']=[]
    for i in [2,3,4,5]:
        restriction=[encode(ext['characters'][i][j-1]) for j in ext['fusion']]
        matches=[k+1 for k,c in enumerate(uc) if c==restriction]
        assert len(matches)==1
        assert all(restriction[j]==5 for j,s in enumerate(u['sizes']) if s==1)
        out['exception_core_rows'].append(matches[0])
    out['fifth_budget']=[e for e in range(3,16) if 12*((e+4)//5)<=2*e+6]
    assert out['fifth_budget']==[3,4,5,9,10,15]
    out['seconds']=round(time.time()-started,3)
    (BASE/'check_a1_spectra.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='tables'}))

if __name__=='__main__':main()
