#!/usr/bin/env python3
"""Independent polynomial-Fourier audit of the complete root A7 inputs.

No root checker, selected-row list, scan, or Ramanujan helper is imported.
All cyclotomic arithmetic is performed in Z[X]/Phi_n(X).
"""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
from math import gcd,lcm
import json,hashlib,time
import sympy as sp
from flint import fmpz_poly

B=Path(__file__).resolve().parent
SRC=B.parents[2]/'research/a7_cores'
X=sp.Symbol('X')

@lru_cache(None)
def cyclo(n):
    return fmpz_poly([int(c) for c in reversed(sp.Poly(sp.cyclotomic_poly(n,X),X).all_coeffs())])

def conductor(z):return 1 if isinstance(z,int) else z[0]

def polynomial(z,n,power=1):
    out=[0]*n
    if isinstance(z,int):out[0]=z
    else:
        m,co=z;assert n%m==0
        for j,a in enumerate(co):out[(j*(n//m)*power)%n]+=a
    return fmpz_poly(out)%cyclo(n)

def equal(z,w):
    n=lcm(conductor(z),conductor(w))
    return polynomial(z,n)==polynomial(w,n)

def scalar_value(z,a):
    n=conductor(z)
    return (polynomial(z,n)*polynomial(z,n,-1))%cyclo(n)==fmpz_poly([a*a])

def power_index(t,j,k):
    for x in t['power_maps']:
        p=x['prime']
        while k>1 and k%p==0:
            j=x['map'][j]-1;k//=p
    assert k==1
    return j

def eigenvalues(t,row,j):
    n=t['orders'][j];a=row[0];traces=[]
    for k in range(n):
        if k==0:traces.append(fmpz_poly([a]));continue
        d=gcd(n,k)
        traces.append(polynomial(row[power_index(t,j,d)],n,k//d))
    ans=[]
    for ell in range(n):
        poly=fmpz_poly()
        for k,tr in enumerate(traces):
            mon=[0]*n;mon[-ell*k%n]=1
            poly+=(tr*fmpz_poly(mon))%cyclo(n)
        poly%=cyclo(n)
        assert poly.degree()<=0
        num=int(poly[0]);assert num>=0 and num%n==0
        ans.append(num//n)
    assert sum(ans)==a
    return ans

def main():
    start=time.perf_counter();raw=(SRC/'inputs.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='185c2a90af296395c33ad8c7c5e839fadba5fffaeda3aacac2d99c8d20c906ab'
    data=json.loads(raw);tables={t['name']:t for t in data['tables']}
    assert set(tables)=={'6.A7','6.A7.2'}
    core=tables['6.A7'];outtab=tables['6.A7.2'];f=outtab['fusion']
    assert core['extension_information']==['6','2']
    center=[j for j,s in enumerate(core['sizes']) if s==1];assert len(center)==6
    std=[i+1 for i,r in enumerate(core['characters']) if r[0]==6 and all(equal(r[j],6) for j in center)]
    assert std==[2]
    assert outtab['order']==2*core['order'] and [i for i,k in enumerate(f) if k==1]==[0]
    assert all(o==outtab['orders'][k-1] for o,k in zip(core['orders'],f))
    assert all(sum(s for s,k in zip(core['sizes'],f) if k==j)==outtab['sizes'][j-1] for j in set(f))
    for a in core['power_maps']:
        b=next(x for x in outtab['power_maps'] if x['prime']==a['prime'])
        assert all(f[i-1]==b['map'][j-1] for i,j in zip(a['map'],f))
    out={'status':'PASS independent polynomial Fourier','input_sha256':hashlib.sha256(raw).hexdigest(),
         'root_code_imported':False,'rows':0,'spectra':0,'standard_core_row':2,'tables':[], 'quarter_exceptions':[]}
    for name,t in tables.items():
        assert 'origin: ATLAS of finite groups' in t['information']
        assert len(t['characters'])==len(t['orders'])==len(t['sizes'])
        assert all(len(r)==len(t['orders']) for r in t['characters'])
        assert sum(r[0]**2 for r in t['characters'])==sum(t['sizes'])==t['order']
        rec={'name':name,'rows':[],'spectra':0}
        for i,r in enumerate(t['characters']):
            a=r[0]
            if a<=1:continue
            if name=='6.A7':label=i+1
            else:
                matches=[k+1 for k,c in enumerate(core['characters']) if all(equal(r[j-1],v) for j,v in zip(f,c))]
                if not matches:continue
                assert len(matches)==1;label=matches[0]
            minimum=a
            for j,z in enumerate(r):
                if scalar_value(z,a):continue
                m=eigenvalues(t,r,j);nu=a-max(m);minimum=min(minimum,nu)
                out['spectra']+=1;rec['spectra']+=1
                if 4*nu<a:out['quarter_exceptions'].append({'table':name,'row':i+1,'core_row':label,'class':j+1,'degree':a,'nu':nu,'multiplicities':m})
            if label!=2:assert 4*minimum>=a
            if a<=6 and label!=2:assert a in (4,6) and minimum>=2 and name=='6.A7'
            rec['rows'].append({'row':i+1,'core_row':label,'degree':a,'min_support':minimum});out['rows']+=1
        out['tables'].append(rec)
    assert (out['rows'],out['spectra'])==(57,1884)
    assert [(len(x['rows']),x['spectra']) for x in out['tables']]==[(39,1326),(18,558)]
    assert [(x['table'],x['row'],x['core_row'],x['class'],x['degree'],x['nu']) for x in out['quarter_exceptions']]==[
        ('6.A7.2',3,2,26,6,1),('6.A7.2',4,2,26,6,1)]
    assert sorted(x['multiplicities'] for x in out['quarter_exceptions'])==[[1,5],[5,1]]
    assert min(r['degree'] for r in out['tables'][0]['rows'])==4
    assert 2*F(11,18)+10*F(1,6)==F(26,9)
    assert 6/(F(26,9)-2)==F(27,4)<36
    assert 12*2>2*6+6 and 4*4>6
    out['proof_sha256']=hashlib.sha256((SRC/'a7_section.tex').read_bytes()).hexdigest()
    out['seconds']=round(time.perf_counter()-start,6)
    (B/'audit_a7_core.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='tables'},indent=2))

if __name__=='__main__':main()
