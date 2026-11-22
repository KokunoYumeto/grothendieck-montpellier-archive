#!/usr/bin/env python3
"""Independent D-HOS07--10 arithmetic; no author code/data imported."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json,hashlib,time
import sympy as sp
from flint import nmod_mat
t0=time.perf_counter()
out={'status':'PASS','scope':'Independent symbolic and finite algebra; universal proof checked separately'}
# Build the 6-dimensional radical from its action on basis columns,
# rather than the author's outer-product expression.
B=sp.diag(*[sp.Matrix([[0,1],[-1,0]]) for _ in range(3)])
I=sp.eye(6); e=I[:,0]; f=I[:,1]
w=sp.Matrix([0,0,*sp.symbols('w1:5')])
v=sp.Matrix([0,0,*sp.symbols('v1:5')])
z,t=sp.symbols('z t')
def u(w,z):
    ans=sp.eye(6)
    ans[:,1]=f+w+2*z*e
    for col in range(2,6):
        ans[:,col]=I[:,col]+(w.T*B*I[:,col])[0]*e
    return ans
def eq(a,b): return all(sp.expand(x)==0 for x in a-b)
def tv(v,c): return I+c*v*(v.T*B)
assert eq(u(w,z).T*B*u(w,z),B)
assert eq(u(w,z)*u(v,t),u(w+v,z+t+(w.T*B*v)[0]/2))
assert eq(u(w,0),tv(w+e,1)*tv(w,-1)*tv(e,-1))
assert eq(u(w,z),tv(e,2*z)*u(w,0))
swap=sp.diag(sp.Matrix([[0,-1],[1,0]]),sp.eye(4))
uf=swap*u(v,0)*swap.inv()
assert eq(uf*(f+w),w+(1+(v.T*B*w)[0])*f)
out['symbolic_radical']={'natural_dimension':6,'exact_identities':5}

P=5
def M(rows): return nmod_mat(rows,5)
def ident(n): return M([[int(i==j) for j in range(n)] for i in range(n)])
def column(v): return M([[int(x)] for x in v])
def trans(v,c,J):
    return ident(len(v))+int(c)*(column(v)*(column(v).transpose()*J))
def pair(v,w,J):
    return int((column(v).transpose()*J*column(w))[0,0])
J2=M([[0,1],[4,0]]); I2=ident(2)
full=0; cases=0; square=0; nonsquare=0; allzero=0
for entries in product(range(5),repeat=4):
    h=M([entries[:2],entries[2:]])
    mu=int(h.det())
    if not mu: continue
    full+=1
    assert h.transpose()*J2*h==mu*J2
    found=False
    for v0 in product(range(5),repeat=2):
        if not any(v0): continue
        hv=tuple(int(x) for x in h*column(v0))
        b=pair(v0,hv,J2)
        if not b: continue
        found=True
        target=4 if mu in (1,4) else 3
        cs=[c for c in range(1,5) if c*c*b*b*pow(mu,-1,5)%5==target]
        assert len(cs)==2
        for c in cs:
            tx=trans(v0,c,J2)
            k=h*tx*h.inv()*tx.inv()
            direct=trans(hv,c*pow(mu,-1,5),J2)*trans(v0,-c,J2)
            assert k==direct and int(k.det())==1
            assert int(k[0,0]+k[1,1])==(2+target)%5
            assert k**(3 if mu in (1,4) else 2)==4*I2
            cases+=1
            square+=int(mu in (1,4)); nonsquare+=int(mu in (2,3))
    if not found:
        allzero+=1
        assert h[0,1]==h[1,0]==0 and h[0,0]==h[1,1]
assert full==480 and allzero==4
out['all_GSp2_vectors_parameters']={'matrices':full,'scalar_cases':allzero,
 'nonzero_quadratic_vector_parameter_cases':cases,'square_multiplier':square,'nonsquare_multiplier':nonsquare}

J4=M([[0,0,1,0],[0,0,0,1],[4,0,0,0],[0,4,0,0]])
I4=ident(4); zero=M([[0]*4 for _ in range(4)])
isocases=0
for mu in (2,3):
    h=M([[0,mu,0,0],[1,0,0,0],[0,0,0,1],[0,0,mu,0]])
    assert h*h==mu*I4 and h.transpose()*J4==J4*h
    assert h.transpose()*J4*h==mu*J4
    for v0 in product(range(5),repeat=4):
        if not any(v0):continue
        hv=tuple(int(x) for x in h*column(v0))
        assert pair(v0,hv,J4)==0
        # Two-column independence checked by all 2x2 minors.
        assert any((v0[i]*hv[j]-v0[j]*hv[i])%5 for i in range(4) for j in range(i))
        for c in range(1,5):
            tx=trans(v0,c,J4)
            k=h*tx*h.inv()*tx.inv()
            N=k-I4
            assert N*N==zero and k**5==I4
            # For a square-zero endomorphism of dimension4, a nonzero 2x2
            # minor proves rank exactly2 without importing rank elimination.
            assert any(int(N[i,r]*N[j,s]-N[i,s]*N[j,r]) for i in range(4) for j in range(i) for r in range(4) for s in range(r))
            isocases+=1
assert isocases==4992
out['selfadjoint_nonsquare']={'full_vector_parameter_cases':isocases}

# Every symmetric 2x2 quadratic phase over F5, all nontrivial central
# additive characters. Exact cyclotomic norm via circular convolution.
carriers=Counter(); maxmult=Counter()
for a,b,c in product(range(5),repeat=3):
    if (a,b,c)==(0,0,0):continue
    rank=2 if (a*c-b*b)%5 else 1
    for psi in range(1,5):
        counts=[0]*5
        for x,y in product(range(5),repeat=2):
            counts[(psi*(a*x*x+2*b*x*y+c*y*y))%5]+=1
        conv=[sum(counts[i]*counts[(i-j)%5] for i in range(5)) for j in range(5)]
        assert len(set(conv[1:]))==1
        assert conv[0]-conv[1]==5**(4-rank)
        carriers[rank]+=1
        maxmult[rank]=max(maxmult[rank],max(counts))
        if rank==2:assert max(counts)<=9
assert carriers=={1:96,2:400}
out['all_symmetric_phase_carriers_degree25']={
 'rank1_cases':carriers[1],'rank2_cases':carriers[2],
 'rank1_max_eigenspace':maxmult[1],'rank2_max_eigenspace':maxmult[2],
 'trace_square_by_rank':{'1':125,'2':25}}
# Exact parity-permutation eigenspaces at the smallest n=4 endpoint.
parities=[]
for moved in (2,3):
    fixed=sum(all(v[i]==0 for i in range(moved)) for v in product(range(5),repeat=3))
    eigenspaces=((125+fixed)//2,(125-fixed)//2)
    assert fixed==5**(3-moved)
    parities.append({'moved_Schrodinger_coordinates':moved,'fixed':fixed,'eigenspaces':eigenspaces})
out['involution_carriers_degree125']=parities

delta=F(31,250)
assert (1-F(1,125))/4==2*delta
assert (1-F(1,25))/4==F(6,25)>delta
assert F(1,2)*(1-F(1,5))**2==F(8,25)
assert F(4,25)>delta
assert 1+10*delta==F(56,25)
assert F(6)/(10*delta-1)==25
assert 2*5**3==250>25
out['normalizer_support']=str(delta)
out['source_ceiling']=25
out['degree_floor']=250
proof=Path('HODGE_DIVISION_work/agents/g34_eightfolds/bireflection/higher_odd_symplectic_five_section.tex')
out['proof_sha256']=hashlib.sha256(proof.read_bytes()).hexdigest()
out['seconds']=round(time.perf_counter()-t0,9)
Path(__file__).with_name('independent_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

