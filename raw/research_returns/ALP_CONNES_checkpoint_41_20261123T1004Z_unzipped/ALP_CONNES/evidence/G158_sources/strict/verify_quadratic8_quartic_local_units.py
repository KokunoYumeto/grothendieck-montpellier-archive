"""G158 finite preparation: exact units and C4 projectors for both quadratic8 fields.

This does not certify a class group or prove a strict theorem by itself.
All original p-denominators survive until exact univariate conversion.
"""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

P=269
HERE=Path(__file__).resolve().parent

class Ring:
    def __init__(self,n,lower):
        self.n=n;self.lower={i:Q(a) for i,a in lower.items()}
        self.zero=[Q(0)]*n
        self.one=[Q(1)]+[Q(0)]*(n-1)
        self.x=[Q(0),Q(1)]+[Q(0)]*(n-2)
    def add(self,a,b):return [x+y for x,y in zip(a,b)]
    def scale(self,a,c):return [Q(c)*x for x in a]
    def mul(self,a,b):
        n=self.n;out=[Q(0)]*(2*n-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                if x and y:out[i+j]+=x*y
        for i in range(2*n-2,n-1,-1):
            for k,c in self.lower.items():out[i-n+k]-=c*out[i]
        return out[:n]
    def power(self,a,m):
        out=self.one[:]
        while m:
            if m&1:out=self.mul(out,a)
            a=self.mul(a,a);m//=2
        return out
    def compose(self,f,a):
        out=self.zero[:]
        for x in reversed(f):out=self.add(self.mul(out,a),self.scale(self.one,x))
        return out
    def horner(self,poly,a):return self.compose(list(reversed(poly)),a)

def vp(x):
    x=Q(x)
    if not x:return None
    a,b,v=abs(x.numerator),x.denominator,0
    while a%P==0:a//=P;v+=1
    while b%P==0:b//=P;v-=1
    return v

def residue(x):
    x=Q(x);assert x.denominator%P
    return x.numerator*pow(x.denominator,-1,P)%P

def add(a,b):return [(x+y)%P for x,y in zip(a,b)]
def scale(a,c):return [c*x%P for x in a]
def mul(a,b):
    n=len(a);out=[0]*n
    for i,x in enumerate(a):
        for j,y in enumerate(b[:n-i]):out[i+j]=(out[i+j]+x*y)%P
    return out
def compose(f,a):
    out=[0]*len(a)
    for x in reversed(f):
        out=mul(out,a);out[0]=(out[0]+x)%P
    return out
def logarithm(a):
    assert a[0]
    h=[]
    for n in range(len(a)-1):
        h.append(((n+1)*a[n+1]-sum(a[j]*h[n-j] for j in range(1,n+1)))
                 *pow(a[0],-1,P)%P)
    return [0]+[x*pow(n+1,-1,P)%P for n,x in enumerate(h)]

def projectors(log,b):
    orbit=[log]
    for _ in range(3):orbit.append(compose(orbit[-1],b))
    assert compose(orbit[-1],b)==orbit[0]
    result={}
    for lam in (82,187):
        value=[0]*len(log)
        for k in range(4):value=add(value,scale(orbit[k],pow(lam,-k,P)))
        assert compose(value,b)==scale(value,lam)
        result[str(lam)]={'coefficients':value,'nonzero_degrees':[i for i,x in enumerate(value) if x],
                          'nonzero':any(value)}
    return result

records=[]
sources={1:HERE/'inputs'/'odd_units.json',-1:HERE/'inputs'/'even_units.json'}
for sign in (1,-1):
    source=sources[sign];data=json.loads(source.read_text())
    R=Ring(12,{0:Q(P,1000000),6:Q(sign*417488,1000000)})
    u=R.x
    w=R.add(R.scale(R.power(u,3),Q(52811,61)),R.scale(R.power(u,9),Q(sign*125000,61)))
    t=R.mul(u,w)
    assert R.power(t,3)==R.scale(R.one,P)
    assert R.add(R.add(R.power(w,4),R.scale(R.power(w,2),sign*2*P)),R.scale(R.one,100*P))==R.zero
    bw=R.add(R.scale(R.power(w,3),Q(-sign,130)),R.scale(w,Q(-219,65)))
    bu=R.add(R.scale(u,Q(46711,15860)),R.scale(R.power(u,7),Q(sign*6250,793)))
    assert R.mul(bu,bw)==t
    assert R.compose(w,bu)==bw and R.compose(t,bu)==t
    assert R.compose(bu,bu)==R.scale(u,-1)
    bubar=list(map(residue,bu))
    assert bubar==[0,82,0,0,0,0,0,130 if sign==1 else 139,0,0,0,0]
    basis=[R.mul(R.power(t,a),R.power(w,b)) for a in range(3) for b in range(4)]
    units=[]
    for item in data['units']:
        den=int(item['common_denominator']);nums=list(map(int,item['numerators']))
        exact=R.zero[:]
        for n,bas in zip(nums,basis):exact=R.add(exact,R.scale(bas,Q(n,den)))
        poly=list(map(int,item['monic_annihilator']))
        assert poly[0]==1 and poly[-1] in (-1,1)
        assert R.horner(poly,exact)==R.zero
        vals=list(map(vp,exact));assert all(x is None or x>=0 for x in vals)
        red=list(map(residue,exact));assert red[0]
        log=logarithm(red)
        corrected=[3*x%P if n%3 else 0 for n,x in enumerate(log)]
        units.append({'unit':item['unit'],'original_denominator':den,
                      'monic_annihilator_verified':True,
                      'exact_u_coefficients':list(map(str,exact)),
                      'coefficient_p_valuations':vals,'reduction_mod_p_u12':red,
                      'normalized_log':log,'cubic_corrected_log':corrected,
                      'quartic_projectors':projectors(corrected,bubar)})
    witnesses={str(lam):[x['unit'] for x in units if x['quartic_projectors'][str(lam)]['nonzero']] for lam in (82,187)}
    assert all(witnesses.values())
    records.append({'sign':sign,'quadratic_character':'chi8' if sign==1 else 'chi_minus8',
                    'source_path':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                    'quartic_polynomial':[1,0,sign*2*P,0,100*P],
                    'u_polynomial_nonmonic':[1000000,0,0,0,0,0,sign*417488,0,0,0,0,0,P],
                    'w_in_u':list(map(str,w)),'b_u_exact':list(map(str,bu)),
                    'b_u_mod_p_u12':bubar,'b2_u_minus_u':True,
                    'units':units,'witnesses':witnesses})
result={'timestamp':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_UNIT_LOCAL_ONLY',
        'records':records,'xi_b':187,'inverse_eigenvalue_by_weight':{'66':187,'200':82},
        'scope':'Nontrivial cubic components j1,2 only; all rational denominators retained through exact conversion. One p-place e12f2 in each M.',
        'class_group_claim':False,'strict_group_claim':False,'analytic_execution':False,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
target=HERE/'quadratic8_quartic_local_unit_certificate.json'
target.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'witnesses':[r['witnesses'] for r in records],
                  'output_sha256':hashlib.sha256(target.read_bytes()).hexdigest()},indent=2))
