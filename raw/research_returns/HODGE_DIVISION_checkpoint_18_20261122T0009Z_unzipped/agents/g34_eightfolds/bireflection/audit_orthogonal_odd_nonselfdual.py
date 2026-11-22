#!/usr/bin/env python3
"""Independent exact supplement for D-OL12--13, no author imports.

Norm distributions are obtained by convolution of directly counted binary
and unary value distributions, not by the author's vector enumeration.
The universal normalizer/source proof is checked separately in the report.
"""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from itertools import product
import hashlib,json,time
import sympy as s

started=time.perf_counter()
here=Path(__file__).resolve().parent
proof=here.parents[1]/'imprimitive/orthogonal_lowlevels/orthogonal_odd_nonselfdual_section.tex'
sha=hashlib.sha256(proof.read_bytes()).hexdigest()
assert sha=='0ed85dfb4a94ac000e411e22a2c9735157c2bd8fa606ff4d7c507c66cf8f2921'

def convolution(a,b,q):
    out=[0]*q
    for i,j in product(range(q),repeat=2):out[(i+j)%q]+=a[i]*b[j]
    return out

rows=[]
q3_failure=None
for q in (3,5,7,11,13,17,19,23,31):
    h=[0]*q
    for x,y in product(range(q),repeat=2):h[x*y%q]+=1
    nonsquare=next(x for x in range(1,q) if pow(x,(q-1)//2,q)==q-1)
    even=[1]+[0]*(q-1)
    for planes in range(1,13):
        even=convolution(even,h,q)
        assert even[0]==q**(2*planes-1)+(q-1)*q**(planes-1)
        assert all(x==q**(2*planes-1)-q**(planes-1) for x in even[1:])
        for coeff in (1,nonsquare):
            line=[0]*q
            for z in range(q):line[coeff*z*z%q]+=1
            odd=convolution(even,line,q)
            assert odd[0]==q**(2*planes)
            for t in range(1,q):
                leg=1 if pow(coeff*t%q,(q-1)//2,q)==1 else -1
                assert odd[t]==q**(2*planes)+leg*q**planes
            fixed=[even[0]-1]+even[1:]
            total=[odd[0]-1]+odd[1:]
            fractions=[F(a,b) for a,b in zip(fixed,total)]
            if q>=5 and planes>=10:assert max(fractions)<F(1,4)
            if q==3 and planes==11 and coeff==1:
                q3_failure=fractions[0]
                assert q3_failure>F(1,3)
            rows.append({'q':q,'hyperbolic_planes':planes,'line_coefficient':coeff,'maximum_fixed_fraction':str(max(fractions))})

# A different, larger symbolic signed-action model than the author's.
dim=13
B=s.zeros(dim)
pairs=[(0,12),(1,2),(3,4),(5,6),(7,8),(9,10)]
for i,j in pairs:B[i,j]=B[j,i]=1
B[11,11]=2
Id=s.eye(dim)
g=-Id.copy();g[11,11]=1
reflection_product=Id
spin=1
for i,j in pairs:
    for sign in (1,-1):
        v=s.zeros(dim,1);v[i]=1;v[j]=sign
        norm=(v.T*B*v)[0]/2
        R=Id-v*(v.T*B)/norm
        assert R.T*B*R==B and R*R==Id and R.det()==-1
        reflection_product=reflection_product*R
        spin*=norm
assert reflection_product==g and spin==1 and g.det()==1
BW=B[1:12,1:12]
A=-g[1:12,1:12]
assert (A-s.eye(11)).rank()==1
v=s.Matrix(s.symbols('v0:11'))
w=s.Matrix(s.symbols('w0:11'))
def U(v):
    z=Id.copy()
    z[0,1:12]=-v.T*BW
    z[1:12,12]=v
    z[0,12]=-(v.T*BW*v)[0]/2
    return z
assert (U(v).T*B*U(v)-B).applyfunc(s.expand)==s.zeros(dim)
assert (U(v)*U(w)-U(v+w)).applyfunc(s.expand)==s.zeros(dim)
assert (g*U(v)*g-U(A*v)).applyfunc(s.expand)==s.zeros(dim)

fixed_bound=(F(1,5)+F(1,5**9))/(1-F(1,5**9)-F(1,5**19))
delta=(1-F(19,20)**9)/2
ceiling=6/(12*delta-2)
assert fixed_bound<F(1,4)
assert F(1,6)<delta<F(3,16)
assert 27<ceiling<28
assert (1135-1)//2==567==7*9**2
assert (F(1,2**18)/(1-F(1,4**9)-F(1,4**19)))<F(1,4)
assert q3_failure==F(29525,88574)

out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-started,'proof_sha256':sha,'norm_distribution_count':len(rows),'norm_distributions':rows,'symbolic_signed_pair_dimension':dim,'reflection_count':12,'spinor_norm_representative':int(spin),'weight_moving_rank':1,'uniform_fixed_fraction_bound':str(fixed_bound),'delta':str(delta),'degree_ceiling':str(ceiling),'q3_rank_one_failure':{'W_dimension':23,'fraction':str(q3_failure),'exceeds':'1/3'},'scope':'Independent exact distribution convolution, thirteen-dimensional symbolic radical/reflection identities and rational constants. Universal group-normalizer, primary-source and geometric arguments are separately audited; no finite extrapolation.'}
(here/'audit_orthogonal_odd_nonselfdual.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='norm_distributions'},indent=2))
