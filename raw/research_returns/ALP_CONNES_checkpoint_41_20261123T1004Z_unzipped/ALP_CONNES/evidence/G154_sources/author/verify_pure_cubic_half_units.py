"""G154: exact descent of two already certified units to Q(z), z^6=269.

This is a unit/local and elementary finite-bound calculation only.
No analytic class computation or complete unit basis is used.
"""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib

P, N = 269, 6
HERE=Path(__file__).resolve().parent
SOURCE=HERE/'inputs'/'G152_exact_units.json'

class Ring:
    zero=[Q(0)]*N
    one=[Q(1)]+[Q(0)]*(N-1)
    z=[Q(0),Q(1)]+[Q(0)]*(N-2)
    @staticmethod
    def add(x,y):return [a+b for a,b in zip(x,y)]
    @staticmethod
    def scale(x,a):return [Q(a)*b for b in x]
    @staticmethod
    def mul(x,y):
        out=[Q(0)]*(2*N-1)
        for i,a in enumerate(x):
            for j,b in enumerate(y):out[i+j]+=a*b
        for k in range(2*N-2,N-1,-1):out[k-N]+=P*out[k]
        return out[:N]
    @classmethod
    def power(cls,x,n):
        out=cls.one[:]
        while n:
            if n&1:out=cls.mul(out,x)
            x=cls.mul(x,x);n//=2
        return out
    @classmethod
    def horner(cls,coeff,x):
        out=cls.zero[:]
        for a in coeff:out=cls.add(cls.mul(out,x),cls.scale(cls.one,a))
        return out

def polynomial_product(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def polynomial_power(a,n):
    out=[1]
    for _ in range(n):out=polynomial_product(out,a)
    return out

def residue(q):
    q=Q(q);assert q.denominator%P
    return q.numerator*pow(q.denominator,-1,P)%P

def logarithm(v):
    assert v[0]
    h=[]
    for n in range(N-1):
        target=(n+1)*v[n+1]-sum(v[j]*h[n-j] for j in range(1,n+1))
        h.append(target*pow(v[0],-1,P)%P)
    return [0]+[h[n]*pow(n+1,-1,P)%P for n in range(N-1)]

data=json.loads(SOURCE.read_text())
R=Ring();t=R.power(R.z,2);s=R.power(R.z,3)
assert R.power(t,3)==R.scale(R.one,P)
assert R.power(s,2)==R.scale(R.one,P)
w2=R.scale(R.add(R.scale(R.one,P),R.scale(s,13)),Q(1,2))
assert R.add(R.add(R.power(w2,2),R.scale(w2,-P)),R.scale(R.one,25*P))==R.zero
records=[]
polys={1:[1,164,-1],4:[1,-2914392,2292660952446,496180748942476,-1175165153940,13982965350,-1]}
expected={1:[-82,0,0,-5,0,0],4:[485732,-142367,-19217,29620,-8682,-1171]}
for index in (1,4):
    item=data['units'][index-1]
    nums=list(map(int,item['numerators']));den=int(item['common_denominator'])
    assert item['unit']==index
    assert all(nums[4*a+1]==nums[4*a+3]==0 for a in range(3))
    value=R.zero[:]
    for a in range(3):
        factor=R.add(R.scale(R.one,Q(nums[4*a],den)),R.scale(w2,Q(nums[4*a+2],den)))
        value=R.add(value,R.mul(R.power(t,a),factor))
    assert value==list(map(Q,expected[index]))
    assert R.horner(item['monic_annihilator'],value)==R.zero
    assert R.horner(polys[index],value)==R.zero
    assert polynomial_power(polys[index],6 if index==1 else 2)==item['monic_annihilator']
    v=list(map(residue,value));log=logarithm(v)
    if index==1:
        corrected=log
        assert log==[0,0,0,128,0,0]
        conjugate=[a if n%2==0 else -a for n,a in enumerate(value)]
        assert R.mul(value,conjugate)==R.scale(R.one,-1)
    else:
        corrected=[3*a%P if n%3 else 0 for n,a in enumerate(log)]
        assert log==[0,237,34,222,243,125]
    projected=[2*a%P if n%2 else 0 for n,a in enumerate(corrected)]
    assert projected==([0,0,0,256,0,0] if index==1 else [0,77,0,0,0,212])
    records.append({'source_unit':index,'original_denominator':den,
                    'exact_z_coefficients':expected[index],
                    'short_monic_unit_relation':polys[index],
                    'source_relation_is_power_of_short_relation':True,
                    'source_and_short_relations_verified_by_Horner':True,
                    'reduction_mod_p_z6':v,'normalized_log':log,
                    'cubic_corrected_log':corrected,
                    'b_minus_projected_log':projected,
                    'cubic_component':'trivial' if index==1 else 'nontrivial'})
divisors=[sum(n%d==0 for d in range(1,n+1)) for n in range(1,19)]
assert sum(divisors)==58<P
assert 4*807<9*19**2
out={'timestamp':datetime.now(timezone.utc).isoformat(),
     'status':'PASS_EXACT_INHERITED_UNIT_AND_LOCAL_ONLY',
     'source_path':str(SOURCE),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
     'field':'z^6=269; t=z^2,sqrt269=z^3,w^2=(269+13z^3)/2',
     'local_scope':'Unique M0 p-place e6f2; full pth-power principal logarithms have valuation at least7.',
     'units':records,'quadratic_ideal_bound':{'discriminant':-807,'bound_less_than':19,'divisor_counts_1_to18':divisors,'sum':58,'inequality_4D_less_than_9x19sq':[4*807,9*19**2]},
     'class_theorem_claim_by_script':False,'analytic_execution':False,
     'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
target=HERE/'pure_cubic_half_unit_certificate.json'
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'projectors':[r['b_minus_projected_log'] for r in records],
                  'output_sha256':hashlib.sha256(target.read_bytes()).hexdigest()},indent=2))
