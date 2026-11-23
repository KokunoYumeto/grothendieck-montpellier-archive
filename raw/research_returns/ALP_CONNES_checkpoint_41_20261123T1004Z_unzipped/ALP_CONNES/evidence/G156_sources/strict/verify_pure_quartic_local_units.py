"""G156 finite preparation: exact units and both local C4 projectors.

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

sources={name:HERE/'inputs'/filename for name,filename in
         [('L','degree12_units.json'),('Fplus','real_quartic_units.json')]}
data={name:json.loads(path.read_text()) for name,path in sources.items()}
R=Ring(12,{0:Q(P,15625),6:Q(52186,15625)})
u=R.x
v=R.add(R.scale(R.power(u,3),Q(52811,244)),R.scale(R.power(u,9),Q(15625,244)))
t=R.mul(u,v)
assert R.power(t,3)==R.scale(R.one,P)
assert R.add(R.add(R.power(v,4),R.scale(R.power(v,2),P)),R.scale(R.one,25*P))==R.zero
bv=R.scale(R.add(R.power(v,3),R.scale(v,219)),Q(-1,65))
bu=R.add(R.scale(u,Q(46711,15860)),R.scale(R.power(u,7),Q(3125,3172)))
assert R.mul(bu,bv)==t
assert R.compose(v,bu)==bv
assert R.compose(t,bu)==t
assert R.compose(bu,bu)==R.scale(u,-1)
bubar=list(map(residue,bu))
assert bubar==[0,82,0,0,0,0,0,218,0,0,0,0]
basis=[R.mul(R.power(t,a),R.power(v,b)) for a in range(3) for b in range(4)]
records=[]
for item in data['L']['units']:
    den=int(item['common_denominator']);nums=list(map(int,item['numerators']))
    exact=R.zero[:]
    for n,bas in zip(nums,basis):exact=R.add(exact,R.scale(bas,Q(n,den)))
    poly=list(map(int,item['monic_annihilator']))
    assert poly[0]==1 and poly[-1] in (-1,1)
    assert R.horner(poly,exact)==R.zero
    valuations=list(map(vp,exact));assert all(x is None or x>=0 for x in valuations)
    reduced=list(map(residue,exact));assert reduced[0]
    log=logarithm(reduced)
    corrected=[3*x%P if n%3 else 0 for n,x in enumerate(log)]
    records.append({'unit':item['unit'],'original_denominator':den,
                    'monic_annihilator_verified':True,
                    'exact_u_coefficients':list(map(str,exact)),
                    'coefficient_p_valuations':valuations,'reduction_mod_p_u12':reduced,
                    'normalized_log':log,'cubic_corrected_log':corrected,
                    'quartic_projectors':projectors(corrected,bubar)})

S=Ring(4,{0:225*P,2:-3*P});w=S.x
bw=S.scale(S.add(S.power(w,3),S.scale(w,-657)),Q(1,195))
assert S.compose(bw,bw)==S.scale(w,-1)
bwbar=list(map(residue,bw))
plus=[]
for item in data['Fplus']['units']:
    den=int(item['common_denominator']);exact=[Q(int(n),den) for n in item['numerators']]
    poly=list(map(int,item['monic_annihilator']))
    assert poly[0]==1 and poly[-1] in (-1,1)
    assert S.horner(poly,exact)==S.zero
    valuations=list(map(vp,exact));assert all(x is None or x>=0 for x in valuations)
    reduced=list(map(residue,exact));assert reduced[0]
    log=logarithm(reduced)
    plus.append({'unit':item['unit'],'original_denominator':den,
                 'monic_annihilator_verified':True,'exact_w_coefficients':list(map(str,exact)),
                 'coefficient_p_valuations':valuations,'reduction_mod_p_w4':reduced,
                 'normalized_log':log,'quartic_projectors':projectors(log,bwbar)})

witnesses={name:{str(lam):[x['unit'] for x in rs if x['quartic_projectors'][str(lam)]['nonzero']]
                 for lam in (82,187)} for name,rs in [('nontrivial_cubic',records),('trivial_cubic',plus)]}
assert all(x for rs in witnesses.values() for x in rs.values())
result={'timestamp':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_UNIT_LOCAL_ONLY',
        'sources':{name:{'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
                   for name,path in sources.items()},
        'field12':{'uniformizer':'u=t/v','minimal_polynomial_nonmonic':[15625,0,0,0,0,0,52186,0,0,0,0,0,269],
                   'v_in_u':list(map(str,v)),'b_u_exact':list(map(str,bu)),
                   'b_u_mod_p_u12':bubar,'b2_u_minus_u':True,'e':12,'f':2,'p_places':1},
        'field4':{'uniformizer':'w','minimal_polynomial':[1,0,-807,0,60525],
                  'b_w_exact':list(map(str,bw)),'b_w_mod_p_w4':bwbar,
                  'b2_w_minus_w':True,'N_e':4,'N_f':2,'N_p_places':1},
        'psi_b':187,'inverse_eigenvalue_by_weight':{'66':187,'200':82},
        'nontrivial_cubic_units':records,'trivial_cubic_units':plus,'witnesses':witnesses,
        'class_group_claim':False,'strict_group_claim':False,'analytic_execution':False,
        'method':'Exact univariate Fraction/Horner with all rational p-denominators; differential-log recursion and full b composition.',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
target=HERE/'pure_quartic_local_unit_certificate.json'
target.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'witnesses':witnesses,
                  'output_sha256':hashlib.sha256(target.read_bytes()).hexdigest()},indent=2))
