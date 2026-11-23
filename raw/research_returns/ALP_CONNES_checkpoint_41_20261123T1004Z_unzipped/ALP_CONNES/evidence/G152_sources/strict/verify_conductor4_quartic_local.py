"""Exact G152 field/unit/local check; no class or strict theorem by itself.

All tensor denominators are retained through exact Q[u] conversion.
The seven monic unit relations are checked by a new univariate Horner
calculation, independently of the source regular-matrix calculation.
"""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

P, N = 269, 12
HERE = Path(__file__).resolve().parent
SOURCE = HERE/'inputs'/'all_units_exact_certificate.json'

def vp(x):
    x=Q(x)
    if not x:return None
    a,b,v=abs(x.numerator),x.denominator,0
    while a%P==0:a//=P;v+=1
    while b%P==0:b//=P;v-=1
    return v

def residue(x):
    x=Q(x)
    assert x.denominator%P
    return x.numerator*pow(x.denominator,-1,P)%P

class Ring:
    def __init__(self):
        self.a=Q(P*(75-P),15625)
        self.b=Q(P,15625)
        self.zero=[Q(0)]*N
        self.one=[Q(1)]+[Q(0)]*(N-1)
        self.u=[Q(0),Q(1)]+[Q(0)]*(N-2)
    def add(self,x,y):return [a+b for a,b in zip(x,y)]
    def scale(self,x,a):return [Q(a)*z for z in x]
    def mul(self,x,y):
        out=[Q(0)]*(2*N-1)
        for i,a in enumerate(x):
            for j,b in enumerate(y):
                if a and b:out[i+j]+=a*b
        for i in range(2*N-2,N-1,-1):
            out[i-N]-=self.b*out[i]
            out[i-6]-=self.a*out[i]
        return out[:N]
    def power(self,x,n):
        out=self.one[:]
        while n:
            if n&1:out=self.mul(out,x)
            x=self.mul(x,x);n//=2
        return out
    def compose(self,f,g):
        out=self.zero[:]
        for a in reversed(f):
            out=self.add(self.mul(out,g),self.scale(self.one,a))
        return out

def add(x,y):return [(a+b)%P for a,b in zip(x,y)]
def scale(x,a):return [a*b%P for b in x]
def mul(x,y):
    out=[0]*N
    for i,a in enumerate(x):
        for j,b in enumerate(y[:N-i]):out[i+j]=(out[i+j]+a*b)%P
    return out
def compose(f,g):
    out=[0]*N
    for a in reversed(f):
        out=mul(out,g);out[0]=(out[0]+a)%P
    return out
def logarithm(v):
    assert v[0]
    # Differential recursion U H=U', integrated term by term.  All
    # denominators 1,...,11 are units in F_269.
    h=[]
    for n in range(N-1):
        target=(n+1)*v[n+1]-sum(v[j]*h[n-j] for j in range(1,n+1))
        h.append(target*pow(v[0],-1,P)%P)
    return [0]+[h[n]*pow(n+1,-1,P)%P for n in range(N-1)]

data=json.loads(SOURCE.read_text())
assert data['C']==25*P
R=Ring()
w=R.add(R.scale(R.power(R.u,3),Q(52811,244)),
        R.scale(R.power(R.u,9),Q(-15625,244)))
t=R.mul(R.u,w)
assert R.power(t,3)==R.scale(R.one,P)
assert R.add(R.add(R.power(w,4),R.scale(R.power(w,2),-P)),R.scale(R.one,25*P))==R.zero
bw=R.scale(R.add(R.power(w,3),R.scale(w,-219)),Q(1,65))
bu=R.add(R.scale(R.u,Q(46711,15860)),R.scale(R.power(R.u,7),Q(-3125,3172)))
assert R.mul(bu,bw)==t
assert R.compose(w,bu)==bw
assert R.compose(t,bu)==t
assert R.compose(bu,bu)==R.scale(R.u,-1)
bubar=[residue(x) for x in bu]
assert bubar==[0,82,0,0,0,0,0,51,0,0,0,0]
basis=[R.mul(R.power(t,a),R.power(w,b)) for a in range(3) for b in range(4)]
units=[]
for item in data['units']:
    nums=list(map(int,item['numerators']))
    den=int(item['common_denominator'])
    exact=R.zero[:]
    for n,bas in zip(nums,basis):exact=R.add(exact,R.scale(bas,Q(n,den)))
    vals=[vp(x) for x in exact]
    assert all(v is None or v>=0 for v in vals)
    reduced=[residue(x) for x in exact]
    assert reduced[0]
    poly=list(map(int,item['monic_annihilator']))
    assert poly[0]==1 and poly[-1] in (-1,1)
    value=R.zero[:]
    for n in poly:value=R.add(R.mul(value,exact),R.scale(R.one,n))
    assert value==R.zero
    log=logarithm(reduced)
    corrected=[3*x%P if n%3 else 0 for n,x in enumerate(log)]
    orbit=[corrected]
    for _ in range(3):orbit.append(compose(orbit[-1],bubar))
    assert compose(orbit[-1],bubar)==orbit[0]
    projectors={}
    for lam in (82,187):
        proj=[0]*N
        for k in range(4):proj=add(proj,scale(orbit[k],pow(lam,-k,P)))
        assert compose(proj,bubar)==scale(proj,lam)
        projectors[str(lam)]={'coefficients':proj,
                              'nonzero_degrees':[n for n in range(1,N) if proj[n]],
                              'nonzero':any(proj[1:])}
    units.append({'unit':item['unit'],'original_denominator':den,
                  'exact_u_coefficients':list(map(str,exact)),
                  'coefficient_p_valuations':vals,
                  'reduction_mod_p_u12':reduced,'normalized_log':log,
                  'cubic_corrected_log':corrected,'quartic_projectors':projectors,
                  'monic_integral_annihilator_verified':True,
                  'constant_coefficient':poly[-1]})
witnesses={str(lam):[z['unit'] for z in units if z['quartic_projectors'][str(lam)]['nonzero']]
           for lam in (82,187)}
assert all(witnesses.values())
result={'timestamp':datetime.now(timezone.utc).isoformat(),
        'status':'PASS_EXACT_UNIT_AND_LOCAL_ONLY','source_path':str(SOURCE),
        'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'uniformizer':'u=t/w','minimal_polynomial_nonmonic':[15625,0,0,0,0,0,-52186,0,0,0,0,0,269],
        'w_in_u':list(map(str,w)),'b_u_exact':list(map(str,bu)),'b_u_mod_p_u12':bubar,
        'b2_u_minus_u':True,'xi_b':187,
        'residue_to_inverse_quartic_eigenvalue':{'66':187,'200':82},
        'units':units,'witnesses':witnesses,
        'local_scope':'One p-place of M with e12f2; global C3/C4 projectors before localization.',
        'class_group_claim':False,'strict_group_claim':False,
        'method':'Exact Q[u] conversion and Horner; all rational denominators retained; differential logarithm recursion in F269[u]/u12.',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
target=HERE/'conductor4_quartic_local_certificate.json'
target.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'witnesses':witnesses,
                  'output_sha256':hashlib.sha256(target.read_bytes()).hexdigest()},indent=2))
