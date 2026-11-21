#!/usr/bin/env python3
"""Independent integer-polynomial verification of the compact CTblLib input.

No GAP process or author scan code is called.  Cyclotomic arithmetic uses
Z[x]/Phi_n(x); insufficient triangle estimates trigger exact cyclic Fourier
multiplicities reconstructed from prime power maps.
"""
from pathlib import Path
from functools import lru_cache
from math import gcd
import hashlib, json, time
import sympy as sp
from flint import fmpz_poly

BASE=Path(__file__).resolve().parent
X=sp.Symbol('X')

def key(z):
    return z if isinstance(z,int) else (z[0],tuple(z[1]))

@lru_cache(None)
def phi(n):
    return fmpz_poly(list(reversed([int(c) for c in sp.Poly(sp.cyclotomic_poly(n,X),X).all_coeffs()])))

@lru_cache(None)
def squared_norm(z):
    if isinstance(z,int): return (z*z,)
    n,c=z
    inv=[0]*n
    for j,a in enumerate(c):inv[-j%n]+=a
    p=(fmpz_poly(list(c))*fmpz_poly(inv))%phi(n)
    return tuple(map(int,p.coeffs())) or (0,)

def power_class(t,j,d):
    maps={a['prime']:a['map'] for a in t['power_maps']}
    for p,m in maps.items():
        while d%p==0 and d>1:
            j=m[j]-1;d//=p
    assert d==1
    return j

def trace_polynomial(z,n,a=1):
    v=[0]*n
    if isinstance(z,int):v[0]=z;return v
    c,coeff=z
    assert n%c==0
    for j,b in enumerate(coeff):v[(j*(n//c)*a)%n]+=b
    return v

def cyclic_multiplicities(t,chi,j):
    n=t['orders'][j];e=chi[0]
    traces=[]
    for r in range(n):
        if r==0:traces.append([(0,e)]);continue
        d=gcd(n,r);u=chi[power_class(t,j,d)]
        v=trace_polynomial(u,n,r//d)
        traces.append([(k,a) for k,a in enumerate(v) if a])
    mult=[]
    for k in range(n):
        c=[0]*n
        for r,v in enumerate(traces):
            for b,a in v:c[(b-k*r)%n]+=a
        p=fmpz_poly(c)%phi(n)
        assert p.degree()<=0
        a=int(p[0]);assert a%n==0 and a>=0
        mult.append(a//n)
    assert sum(mult)==e
    return mult

def main():
    start=time.time()
    raw=(BASE/'character_inputs.json').read_bytes()
    data=json.loads(raw);tables={t['name']:t for t in data['tables']}
    meta=json.loads((BASE/'coverage.json').read_text())['simple_groups']
    assert len(meta)==26 and len(tables)==38
    expected=set()
    for a in meta:
        expected.add(a['cover'])
        assert a['outer'] in ('','2')
        if a['outer']=='2':expected.add(a['extension'])
    assert set(tables)==expected
    author=json.loads((BASE/'quarter_scan.json').read_text())
    selected={t['name']:t['selected_rows'] for t in author['tables']}
    out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
         'method':'independent integer-polynomial norm bounds and exact power-map Fourier reconstruction',
         'tables':[],'total_rows':0,'total_entries':0,'exact_fourier_entries':0}
    minimum=10**30
    for t in data['tables']:
        chars=[[key(z) for z in c] for c in t['characters']]
        nr=len(chars)
        assert nr==len(t['orders'])==len(t['sizes'])
        assert sum(c[0]**2 for c in chars)==t['order']
        assert sum(t['sizes'])==t['order']
        assert all(len(c)==nr for c in chars)
        if 'core' in t:
            core=tables[t['core']]
            core_chars={tuple(key(z) for z in c) for c in core['characters']}
            rows=[i for i,c in enumerate(chars) if c[0]>1 and tuple(c[j-1] for j in t['fusion']) in core_chars]
            assert t['order']==2*core['order']
        else:rows=[i for i,c in enumerate(chars) if c[0]>1]
        assert [i+1 for i in rows]==selected[t['name']]
        record={'name':t['name'],'rows':len(rows),'entries':0,'fourier':[]}
        for i in rows:
            chi=chars[i];e=chi[0];minimum=min(minimum,e)
            for j,z in enumerate(chi):
                a=squared_norm(z)
                if a==(e*e,):continue
                record['entries']+=1
                if 4*sum(abs(v) for v in a)>e*e:
                    mult=cyclic_multiplicities(t,chi,j)
                    nu=e-max(mult)
                    assert 4*nu>=e,(t['name'],i+1,j+1,e,nu)
                    record['fourier'].append({'row':i+1,'class':j+1,'degree':e,'nu':nu,'multiplicities_zero_first':mult})
        out['total_rows']+=len(rows);out['total_entries']+=record['entries']
        out['exact_fourier_entries']+=len(record['fourier'])
        out['tables'].append(record)
        print(t['name'],len(rows),record['entries'],'Fourier',len(record['fourier']),flush=True)
    assert out['total_rows']==3035 and out['total_entries']==473972
    assert minimum==6
    out['minimum_nonlinear_degree']=minimum
    out['seconds']=round(time.time()-start,3)
    (BASE/'independent_quarter_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS',out['total_rows'],out['total_entries'],'Fourier',out['exact_fourier_entries'],'seconds',out['seconds'])

if __name__=='__main__':main()
