#!/usr/bin/env python3
"""Full orthogonal input audit, independent polynomial Fourier/trace.

Reuses only this auditor's previously reviewed polynomial Fourier engine,
not the root's Ramanujan implementation, row selections or result file.
"""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
from math import gcd
import hashlib,importlib.util,json,time
from flint import fmpz_poly

B=Path(__file__).resolve().parent
R=B.parents[2]
helper=B.parent/'audit_exceptional_small/independent_check.py'
spec=importlib.util.spec_from_file_location('own_polynomial_engine',helper)
P=importlib.util.module_from_spec(spec);spec.loader.exec_module(P)
C=P.C

@lru_cache(None)
def mean(z):
    """Normalized trace by full Galois polynomial substitution, no Mobius sum."""
    if isinstance(z,int):return F(z)
    n,coeff=z
    acc=[0]*n;units=[u for u in range(n) if gcd(u,n)==1]
    for u in units:
        for i,a in enumerate(coeff):acc[(i*u)%n]+=a
    val=fmpz_poly(acc)%C.phi(n)
    assert val.degree()<=0
    return F(int(val[0]),len(units))

@lru_cache(None)
def abs_mean(z):
    poly=C.squared_norm(z)
    if isinstance(z,int):return F(z*z)
    return mean((z[0],poly))

def main():
    start=time.perf_counter()
    p=R/'research/orthogonal_small_inputs.json';raw=p.read_bytes()
    sha=hashlib.sha256(raw).hexdigest()
    assert sha=='5236207618c2564af7ed4871c0f92a667664255d2e60be87f037257356669b79'
    data=json.loads(raw);tables={t['name']:t for t in data['tables']}
    expected={
     '6.O7(3)':('2/9',27),'6.O7(3).2':('11/39',78),
     'O8-(2)':('16/51',34),'O8-(2).2':('7/34',34),
     '2^2.O8+(3)':('28/65',260),'2.O8-(3)':('52/123',246),
     '2.O9(3)':('13/41',780),
     'O10+(2)':('32/93',155),'O10+(2).2':('7/31',155),
     'O10-(2)':('64/187',154),'O10-(2).2':('5/22',154),
     'O12+(2)':('128/357',651),'O12+(2).2':('5/21',651),
     'O12-(2)':('256/715',650),'O12-(2).2':('31/130',650)}
    assert set(tables)==set(expected)
    chars={name:[tuple(C.key(z) for z in row) for row in t['characters']]
           for name,t in tables.items()}
    results=[];nrows=nent=nind=nfus=0
    for name,t in tables.items():
        cc=chars[name];nc=len(cc)
        assert nc==len(t['orders'])==len(t['sizes'])==len(t['indicators'])
        assert all(len(row)==nc and isinstance(row[0],int) for row in cc)
        assert sum(row[0]**2 for row in cc)==sum(t['sizes'])==t['order']
        assert t['full_row_orthogonality_checked'] is True
        maps={z['prime']:z['map'] for z in t['power_maps']}
        for prime,mp in maps.items():
            assert len(mp)==nc and all(1<=j<=nc for j in mp)
            assert all(t['orders'][j-1]==o//gcd(o,prime) for j,o in zip(mp,t['orders']))
        for row,indicator in zip(cc,t['indicators']):
            fs=sum(size*mean(row[j-1]) for size,j in zip(t['sizes'],maps[2]))/t['order']
            assert fs==indicator and fs in [-1,0,1]
            nind+=1
        selected=[];core_rows={}
        if 'core' in t:
            u=tables[t['core']];f=t['fusion'];cs=chars[t['core']]
            assert t['order']==2*u['order']
            assert len(f)==len(u['orders'])
            assert [i for i,j in enumerate(f) if j==1]==[0]
            assert all(t['orders'][j-1]==o for j,o in zip(f,u['orders']))
            assert all(sum(size for size,j in zip(u['sizes'],f) if j==k)==t['sizes'][k-1] for k in set(f))
            for pm in u['power_maps']:
                assert all(f[j-1]==maps[pm['prime']][f[i]-1] for i,j in enumerate(pm['map']))
            for i,row in enumerate(cc):
                if row[0]<=1:continue
                norm=sum(size*abs_mean(row[j-1]) for size,j in zip(u['sizes'],f))/u['order']
                assert norm.denominator==1
                matches=[k for k,c in enumerate(cs) if c==tuple(row[j-1] for j in f)]
                assert (norm==1)==(len(matches)==1)
                if norm==1:selected.append(i);core_rows[i]=matches[0]+1
            nfus+=1
        else:
            selected=[i for i,row in enumerate(cc) if row[0]>1]
            core_rows={i:i+1 for i in selected}
        powers=[]
        for j,order in enumerate(t['orders']):
            ds=sorted({gcd(order,r) for r in range(1,order)})
            powers.append(tuple((d,C.power_class(t,j,d)) for d in ds))
        records=[];total=0;minratio=F(1);spectrum_hash=hashlib.sha256()
        for i in selected:
            row=cc[i];a=row[0];mnu=a;witness=None
            for j,z in enumerate(row):
                if C.squared_norm(z)==(a*a,):continue
                ev=P.spectrum_cached(t['orders'][j],a,tuple((d,row[k]) for d,k in powers[j]))
                nu=a-max(ev);assert nu>0
                if nu<mnu:mnu=nu;witness={'class':j+1,'order':t['orders'][j],'multiplicities':ev}
                total+=1
                spectrum_hash.update((str(i+1)+','+str(j+1)+':'+','.join(map(str,ev))+';').encode())
            minratio=min(minratio,F(mnu,a))
            records.append({'row':i+1,'degree':a,'core_row':core_rows[i],
                            'minimum_support':mnu,'ratio':str(F(mnu,a)),
                            'indicator':t['indicators'][i],'witness':witness})
        mindeg=min(cc[i][0] for i in selected)
        assert (str(minratio),mindeg)==expected[name]
        r={'name':name,'selected_rows':len(selected),'spectra':total,
           'minimum_ratio':str(minratio),'minimum_degree':mindeg,
           'all_spectra_sha256':spectrum_hash.hexdigest(),
           'records':records,'provenance':t['information']}
        results.append(r);nrows+=len(selected);nent+=total
        print(json.dumps({k:v for k,v in r.items() if k not in ['records','provenance']}),flush=True)
    assert (nrows,nent,nfus,nind)==(2938,778260,6,3141)
    o9=next(r for r in results if r['name']=='2.O9(3)')
    nonreal=[r for r in o9['records'] if r['indicator']==0]
    assert [(r['row'],r['degree'],r['ratio']) for r in nonreal]==[(224,838656,'1/2'),(225,838656,'1/2')]
    assert all(r['indicator']==1 for r in o9['records'] if r['indicator']!=0)
    assert min(F(28,65),F(52,123))/2>F(1,5)
    assert min(F(2,9),F(7,34),F(7,31),F(5,22),F(5,21),F(31,130))>F(1,5)
    assert F(6)/(12*F(1,5)-2)==15<27
    assert F(6)/(1+10*F(13,82)-2)==F(41,4)<780
    out={'status':'PASS','input_sha256':sha,
         'method':'own polynomial Fourier and direct Galois polynomial trace; no root arithmetic/row selections imported',
         'rows':nrows,'spectra':nent,'normal_fusions':nfus,'indicators':nind,
         'distinct_fourier_problems':P.spectrum_cached.cache_info().currsize,
         'tables':results,'O9_nonreal_rows':nonreal,
         'helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest(),
         'seconds':round(time.perf_counter()-start,6)}
    (B/'independent_checked.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['tables','O9_nonreal_rows']},indent=2),flush=True)

if __name__=='__main__':main()
