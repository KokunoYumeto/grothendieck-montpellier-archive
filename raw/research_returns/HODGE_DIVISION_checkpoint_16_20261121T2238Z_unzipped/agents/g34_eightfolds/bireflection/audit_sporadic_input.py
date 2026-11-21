#!/usr/bin/env python3
"""Independent peer reconstruction of D-SPOR01 finite input.

No GAP or sibling arithmetic code is imported. Polynomial reduction is
implemented with integer lists. Restriction inner products and exceptional
Fourier multiplicities use normalized rational traces/Ramanujan sums.
"""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
from math import gcd
import hashlib,json,time
import sympy as sp

BASE=Path(__file__).resolve().parent
INPUT=BASE.parent.parent/'imprimitive/sporadic/character_inputs.json'
EXPECTED='c2268f05043ed29a9048d5fe7d55b1a096e5c8615fa049b3438cca088f703edb'
X=sp.Symbol('x')

def encode(z):
    return z if isinstance(z,int) else (z[0],tuple(z[1]))


@lru_cache(None)
def cyclo(n):
    return tuple(int(v) for v in reversed(sp.Poly(sp.cyclotomic_poly(n,X),X).all_coeffs()))


def reduce_poly(v,n):
    c=cyclo(n);d=len(c)-1
    v=list(v)
    for j in range(len(v)-1,d-1,-1):
        a=v[j]
        if a:
            for k in range(d+1):v[j-d+k]-=a*c[k]
    v=v[:d]
    while v and v[-1]==0:v.pop()
    return tuple(v) or (0,)


@lru_cache(None)
def abs_square(z):
    if isinstance(z,int):return (1,(z*z,))
    n,c=z
    v=[0]*n
    for a,ca in enumerate(c):
        if ca:
            for b,cb in enumerate(c):
                if cb:v[(a-b)%n]+=ca*cb
    return n,reduce_poly(v,n)


@lru_cache(None)
def ramanujan(n,k):
    # Sum of zeta_n^(u*k) over units u; exact Mobius formula.
    return sum(d*int(sp.mobius(n//d)) for d in sp.divisors(gcd(n,k)))


@lru_cache(None)
def rational_mean_abs_square(z):
    n,c=abs_square(z)
    return F(sum(v*ramanujan(n,k) for k,v in enumerate(c)),int(sp.totient(n)))


def exponent_class(t,j,d):
    for rec in t['power_maps']:
        p=rec['prime']
        while d>1 and d%p==0:
            j=rec['map'][j]-1;d//=p
    assert d==1
    return j


def fourier_via_rational_trace(t,chi,j):
    n=t['orders'][j];e=chi[0]
    traces=[[(0,e)]]
    for r in range(1,n):
        d=gcd(n,r)
        z=chi[exponent_class(t,j,d)]
        if isinstance(z,int):traces.append([(0,z)])
        else:
            f,c=z;assert (n//d)%f==0
            traces.append([((a*(n//f)*(r//d))%n,v) for a,v in enumerate(c) if v])
    denominator=n*int(sp.totient(n))
    answer=[]
    for k in range(n):
        numerator=sum(v*ramanujan(n,(a-k*r)%n)
                      for r,tr in enumerate(traces) for a,v in tr)
        assert numerator>=0 and numerator%denominator==0
        answer.append(numerator//denominator)
    assert sum(answer)==e
    assert 4*(e-max(answer))>=e
    return answer


def main():
    start=time.time();raw=INPUT.read_bytes();sha=hashlib.sha256(raw).hexdigest()
    assert sha==EXPECTED
    data=json.loads(raw);tables={t['name']:t for t in data['tables']}
    covers=['2.B','2.Co1','Co2','Co3','3.F3+','6.Fi22','Fi23','HN','2.HS','He',
            'J1','2.J2','3.J3','J4','Ly','M','M11','2.M12','12.M22','M23','M24',
            '3.McL','3.ON','2.Ru','6.Suz','Th']
    outer=['3.F3+','6.Fi22','HN','2.HS','He','2.J2','3.J3','2.M12','12.M22',
           '3.McL','3.ON','6.Suz']
    assert set(tables)==set(covers+[s+'.2' for s in outer])
    out={'status':'PASS','source_input_sha256':sha,'tables':[],
         'method':'independent list polynomial reduction; normalized-trace restriction norms; Ramanujan Fourier',
         'total_selected_rows':0,'total_nonscalar_entries':0,'fourier_fallbacks':0,
         'minimum_degree':10**30}
    for name,t in tables.items():
        assert 'origin: ATLAS of finite groups' in t['information']
        chars=[[encode(z) for z in row] for row in t['characters']]
        nc=len(chars)
        assert nc==len(t['orders'])==len(t['sizes'])
        assert sum(t['sizes'])==t['order']
        assert sum(c[0]**2 for c in chars)==t['order']
        assert all(len(c)==nc for c in chars)
        rows=[]
        for i,c in enumerate(chars):
            if c[0]<=1:continue
            if 'core' in t:
                u=tables[t['core']];assert t['order']==2*u['order']
                # The genuine restriction's norm is rational. Its normalized
                # field trace equals itself, and commutes with this weighted sum.
                norm=sum(size*rational_mean_abs_square(c[j-1])
                         for size,j in zip(u['sizes'],t['fusion']))/u['order']
                assert norm.denominator==1 and norm>=1
                if norm!=1:continue
            rows.append(i)
        rec={'table':name,'selected_rows':[i+1 for i in rows],
             'entries':0,'fourier':[]}
        for i in rows:
            c=chars[i];e=c[0];out['minimum_degree']=min(out['minimum_degree'],e)
            for j,z in enumerate(c):
                _,a=abs_square(z)
                if a==(e*e,):continue
                rec['entries']+=1
                B=sum(abs(v) for v in a)
                if 4*B>e*e:
                    ms=fourier_via_rational_trace(t,c,j)
                    rec['fourier'].append({'row':i+1,'class':j+1,'order':len(ms),
                                           'degree':e,'nu':e-max(ms),'multiplicities':ms})
        out['total_selected_rows']+=len(rows)
        out['total_nonscalar_entries']+=rec['entries']
        out['fourier_fallbacks']+=len(rec['fourier'])
        out['tables'].append(rec)
    assert out['total_selected_rows']==3035
    assert out['total_nonscalar_entries']==473972
    assert out['minimum_degree']==6
    out['seconds']=round(time.time()-start,3)
    dest=BASE/'audit_sporadic_input.json';dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='tables'}))

if __name__=='__main__':main()
