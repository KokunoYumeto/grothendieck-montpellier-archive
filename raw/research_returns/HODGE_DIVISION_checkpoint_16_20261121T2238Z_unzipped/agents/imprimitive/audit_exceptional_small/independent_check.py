#!/usr/bin/env python3
"""Independent full exceptional-table spectra via cyclotomic polynomials.

Does not import the root's scan, selected rows, spectrum routine or output.
Reuses the auditor's previously fully reviewed integer-polynomial helper.
"""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as Q
from math import gcd
import hashlib, importlib.util, json, time
from flint import fmpz_poly

B=Path(__file__).resolve().parent
R=B.parents[2]
H=B.parent/'sporadic/verify_quarter_bound.py'
spec=importlib.util.spec_from_file_location('own_cyclotomic',H)
C=importlib.util.module_from_spec(spec);spec.loader.exec_module(C)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

@lru_cache(None)
def spectrum_cached(n,a,powers):
    """Exact Fourier in Z[X]/Phi_n, using only gcd-power character values."""
    dvals=dict(powers);traces=[[(0,a)]]
    for r in range(1,n):
        d=gcd(n,r);poly=C.trace_polynomial(dvals[d],n,r//d)
        traces.append([(i,c) for i,c in enumerate(poly) if c])
    ans=[]
    for k in range(n):
        z=[0]*n
        for r,terms in enumerate(traces):
            for i,c in terms:z[(i-k*r)%n]+=c
        v=fmpz_poly(z)%C.phi(n)
        assert v.degree()<=0 and int(v[0])%n==0 and int(v[0])>=0
        ans.append(int(v[0])//n)
    assert sum(ans)==a
    return tuple(ans)

def main():
    start=time.monotonic();p=R/'research/exceptional_small_inputs.json'
    assert sha(p)=='625618617ad0b6268b8898cc39e7e04afb6ae55f8639686347a0b9cf8d244a21'
    D=json.loads(p.read_text());tabs={t['name']:t for t in D['tables']}
    assert set(tabs)=={'2.F4(2)','2.F4(2).2','F4(3)','E6(2)','(2^2x3).2E6(2)'}
    chars={n:[tuple(C.key(z) for z in row) for row in t['characters']] for n,t in tabs.items()}
    out=[];nrows=nent=0
    for name,t in tabs.items():
        cc=chars[name];nc=len(cc)
        assert nc==len(t['sizes'])==len(t['orders'])==len(t['indicators'])
        assert all(len(row)==nc and isinstance(row[0],int) for row in cc)
        assert sum(row[0]**2 for row in cc)==sum(t['sizes'])==t['order']
        maps={z['prime']:z['map'] for z in t['power_maps']}
        for prime,mp in maps.items():
            assert len(mp)==nc and all(1<=j<=nc for j in mp)
            assert all(t['orders'][j-1]==o//gcd(o,prime) for j,o in zip(mp,t['orders']))
        if 'core' in t:
            core=tabs[t['core']];f=t['fusion'];cs=set(chars[t['core']])
            assert t['order']==2*core['order']
            assert len(f)==len(core['orders'])
            assert all(t['orders'][j-1]==o for j,o in zip(f,core['orders']))
            assert all(sum(s for s,j in zip(core['sizes'],f) if j==k)==t['sizes'][k-1] for k in set(f))
            for pm in core['power_maps']:
                assert all(f[j-1]==maps[pm['prime']][f[i]-1] for i,j in enumerate(pm['map']))
            selected=[i for i,row in enumerate(cc) if row[0]>1 and tuple(row[j-1] for j in f) in cs]
        else:selected=[i for i,row in enumerate(cc) if row[0]>1]
        power_classes=[]
        for j,n in enumerate(t['orders']):
            ds=sorted({gcd(n,r) for r in range(1,n)})
            power_classes.append(tuple((d,C.power_class(t,j,d)) for d in ds))
        records=[];total=0;minratio=Q(1);mindeg=min(cc[i][0] for i in selected)
        spectrum_hash=hashlib.sha256()
        for i in selected:
            row=cc[i];a=row[0];mnu=a;witness=None
            for j,z in enumerate(row):
                if C.squared_norm(z)==(a*a,):continue
                ev=spectrum_cached(t['orders'][j],a,tuple((d,row[k]) for d,k in power_classes[j]))
                nu=a-max(ev);assert nu>0
                if nu<mnu:mnu=nu;witness={'class':j+1,'order':t['orders'][j],'multiplicities':ev}
                total+=1;spectrum_hash.update((str(i+1)+','+str(j+1)+':'+','.join(map(str,ev))+';').encode())
            minratio=min(minratio,Q(mnu,a))
            records.append({'row':i+1,'degree':a,'minimum_support':mnu,'ratio':str(Q(mnu,a)),'witness':witness})
        expected={'2.F4(2)':('4/13',52),'2.F4(2).2':('4/13',52),
                  'F4(3)':('32/73',6643),'E6(2)':('512/1241',2482),
                  '(2^2x3).2E6(2)':('8/19',1938)}
        assert (str(minratio),mindeg)==expected[name]
        rec={'name':name,'rows':len(selected),'spectra':total,'minimum_ratio':str(minratio),
             'minimum_degree':mindeg,'all_spectra_sha256':spectrum_hash.hexdigest(),
             'provenance':t['information'],'records':records}
        out.append(rec);nrows+=len(selected);nent+=total
        print(json.dumps({k:v for k,v in rec.items() if k not in ('records','provenance')}),flush=True)
    assert (nrows,nent)==(1639,1007457)
    # Direct F4(2) quarter support and the other three core ratios >2/5
    # give at least a fifth through the rank-commutator inequality.
    assert Q(4,13)>Q(1,5)
    assert min(Q(32,73),Q(512,1241),Q(8,19))/2>Q(1,5)
    assert Q(6)/(12*Q(1,5)-2)==15<52
    result={'status':'PASS','input_sha256':sha(p),'arithmetic_helper_sha256':sha(H),
            'method':'independent integer-polynomial Fourier with exact gcd-power caching',
            'rows':nrows,'spectra':nent,'tables':out,'distinct_spectra':spectrum_cached.cache_info().currsize,
            'seconds':round(time.monotonic()-start,6)}
    (B/'independent_check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='tables'},indent=2),flush=True)

if __name__=='__main__':main()
