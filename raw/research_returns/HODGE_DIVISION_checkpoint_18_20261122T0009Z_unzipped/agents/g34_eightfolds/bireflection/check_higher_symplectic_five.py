#!/usr/bin/env python3
"""Exact supplement to D-HOS07--10; no character table is used.

Universal generation, Fourier inequalities, normalizer completeness and
Hurwitz factorization are written proofs. This checks the displayed algebra
and selected full finite matrix/weight spaces, with exact arithmetic only.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import time
import sympy as s

BASE = Path(__file__).resolve().parent
started = time.perf_counter()
out = {"status": "PASS", "scope": "exact algebra and finite witnesses; universal proofs are separate"}

def simplify_matrix(a):
    return a.applyfunc(s.expand)

def form(n):
    return s.diag(*([s.Matrix([[0, 1], [-1, 0]])] * n))

def trans(v, c, j):
    return s.eye(len(v)) + c*v*(v.T*j)

def radical(e, w, z, j):
    return s.eye(len(e)) + e*(w.T*j) + w*(e.T*j) + 2*z*e*(e.T*j)

# Full symbolic line radical in the smallest natural dimension of the theorem.
j = form(4)
e = s.eye(8)[:, 0]
f = s.eye(8)[:, 1]
w = s.Matrix([0, 0, *s.symbols("w0:6")])
v = s.Matrix([0, 0, *s.symbols("v0:6")])
z, t = s.symbols("z t")
u = radical(e, w, z, j)
uv = radical(e, v, t, j)
assert simplify_matrix(u.T*j*u-j) == s.zeros(8)
bwv = (w.T*j*v)[0]
assert simplify_matrix(u*uv-radical(e, w+v, z+t+bwv/2, j)) == s.zeros(8)
assert simplify_matrix(radical(e, w, 0, j)-trans(w+e, 1, j)*trans(w, -1, j)*trans(e, -1, j)) == s.zeros(8)
assert simplify_matrix(u-trans(e, 2*z, j)*radical(e, w, 0, j)) == s.zeros(8)
opposite = radical(f, v, 0, j)
assert simplify_matrix(opposite*(f+w)-w-(1+(v.T*j*w)[0])*f) == s.zeros(8, 1)
out["symbolic_line_radical"] = {"natural_dimension": 8, "free_radical_vectors": 2, "identities": 5}

# The actual two-dimensional commutator matrix, without specializing b,c,mu.
b, c, mu = s.symbols("b c mu", nonzero=True)
j2 = s.Matrix([[0, b], [-b, 0]])
v0, v1 = s.eye(2)[:, 0], s.eye(2)[:, 1]
k = trans(v1, c/mu, j2)*trans(v0, -c, j2)
expected = s.Matrix([[1, -c*b], [-c*b/mu, 1+c*c*b*b/mu]])
assert simplify_matrix(k-expected) == s.zeros(2)
assert s.factor(k.det()) == 1
assert s.expand(s.trace(k)-2-c*c*b*b/mu) == 0
out["symbolic_commutator"] = {"trace": "2+c^2*b^2/mu", "determinant": 1}

# Small exact matrix arithmetic modulo five, independently of symbolic simplification.
P = 5
def eye(d):
    return tuple(tuple(int(i == j) for j in range(d)) for i in range(d))
def add(a,b):
    return tuple(tuple((x+y)%P for x,y in zip(r,t)) for r,t in zip(a,b))
def neg(a):
    return tuple(tuple(-x%P for x in r) for r in a)
def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b)))%P for j in range(len(b[0]))) for i in range(len(a)))
def mv(a,v):
    return tuple(sum(x*y for x,y in zip(row,v))%P for row in a)
def transpose(a):
    return tuple(zip(*a))
def power(a,k):
    r=eye(len(a))
    while k:
        if k&1:r=mul(r,a)
        a=mul(a,a); k//=2
    return r
def scalar(a,c):
    return tuple(tuple(c*x%P for x in r) for r in a)
def rank(a):
    b=[list(r) for r in a]; i=0
    for j in range(len(b[0])):
        piv=next((k for k in range(i,len(b)) if b[k][j]%P),None)
        if piv is None:continue
        b[i],b[piv]=b[piv],b[i]
        q=pow(b[i][j],-1,P); b[i]=[q*x%P for x in b[i]]
        for k in range(len(b)):
            if k!=i:
                q=b[k][j]; b[k]=[(x-q*y)%P for x,y in zip(b[k],b[i])]
        i+=1
        if i==len(b):break
    return i
def pairing(v,w,j):
    return sum(x*y for x,y in zip(v,mv(j,w)))%P
def tr(v,c,j):
    row=tuple(sum(v[k]*j[k][l] for k in range(len(v)))%P for l in range(len(v)))
    return add(eye(len(v)),tuple(tuple(c*v[i]*row[l]%P for l in range(len(v))) for i in range(len(v))))

jf=((0,1),(4,0))
parameter_cases=0
for mm,bb in product(range(1,5),repeat=2):
    target=4 if mm in (1,4) else 3
    choices=[cc for cc in range(1,5) if cc*cc*bb*bb*pow(mm,-1,5)%5==target]
    assert len(choices)==2
    for cc in choices:
        kk=((1,-cc*bb%5),(-cc*bb*pow(mm,-1,5)%5,(1+target)%5))
        assert power(kk,3 if target==4 else 2)==scalar(eye(2),-1)
        parameter_cases+=1
out["all_field_parameter_choices"]={"mu_b_pairs":16,"successful_c_choices":parameter_cases}

gl_cases=zero_form=nonzero_form=0
for data in product(range(5),repeat=4):
    hh=(data[:2],data[2:]); det=(data[0]*data[3]-data[1]*data[2])%5
    if not det:continue
    gl_cases+=1
    assert mul(mul(transpose(hh),jf),hh)==scalar(jf,det)
    vv=next((v for v in product(range(5),repeat=2) if pairing(v,mv(hh,v),jf)),None)
    if vv is None:
        zero_form+=1
        assert hh[0][1]==hh[1][0]==0 and hh[0][0]==hh[1][1]
        assert power(hh,2)==scalar(eye(2),det)
    else:
        nonzero_form+=1
        hv=mv(hh,vv); bb=pairing(vv,hv,jf)
        target=4 if det in (1,4) else 3
        cc=next(cc for cc in range(1,5) if cc*cc*bb*bb*pow(det,-1,5)%5==target)
        kk=mul(tr(hv,cc*pow(det,-1,5),jf),tr(vv,-cc,jf))
        assert power(kk,3 if target==4 else 2)==scalar(eye(2),-1)
assert (gl_cases,zero_form,nonzero_form)==(480,4,476)
out["complete_GSp2_F5"]={"matrices":gl_cases,"scalar_self_adjoint":zero_form,"nonzero_quadratic_case":nonzero_form}

# Nonsquare self-adjoint four-dimensional natural models for both multiplier values.
j4=((0,0,1,0),(0,0,0,1),(4,0,0,0),(0,4,0,0))
iso_cases=0
for mm in (2,3):
    aa=((0,mm),(1,0)); at=transpose(aa)
    hh=((0,mm,0,0),(1,0,0,0),(0,0,0,1),(0,0,mm,0))
    assert mul(mul(transpose(hh),j4),hh)==scalar(j4,mm)
    assert mul(transpose(hh),j4)==mul(j4,hh)
    assert power(hh,2)==scalar(eye(4),mm)
    for vv in product(range(5),repeat=4):
        if not any(vv):continue
        hv=mv(hh,vv)
        assert pairing(vv,hv,j4)==0
        assert rank((vv,hv))==2
        for cc in range(1,5):
            kk=mul(tr(hv,cc*pow(mm,-1,5),j4),tr(vv,-cc,j4))
            nn=add(kk,neg(eye(4)))
            assert rank(nn)==2 and mul(nn,nn)==scalar(eye(4),0)
            assert power(kk,5)==eye(4)
            iso_cases+=1
assert iso_cases==4992
out["nonsquare_self_adjoint_models"]={"multipliers":[2,3],"all_nonzero_vectors_and_parameters":iso_cases}

# Exact central-character traces for rank-two square-zero natural shears.
# A diagonal quadratic phase is the Schrödinger intertwiner, up to harmless sign.
x=s.symbols("x"); phi=s.Poly(x**4+x**3+x**2+x+1,x)
gauss=[]
for second in (1,2):
    counts=[0]*5
    for v in product(range(5),repeat=3):
        counts[(3*(v[0]**2+second*v[1]**2))%5]+=1
    poly=sum(counts[i]*x**i for i in range(5))
    conjugate=sum(counts[i]*x**((-i)%5) for i in range(5))
    norm=s.rem(s.Poly(poly*conjugate,x),phi).as_expr()
    assert norm==625
    assert max(counts)<=45
    gauss.append({"quadratic_diagonal":[1,second,0],"multiplicities":counts,"trace_absolute_squared":625})
out["rank_two_shear_carriers_degree125"]=gauss

# Involution carrier permutations and dual-weight fixed spaces in full W=F5^6.
out["involution_carriers"]=[]
for moved in (2,3):
    fixed=0
    for v in product(range(5),repeat=3):
        if all(v[i]==0 for i in range(moved)):fixed+=1
    assert fixed==5**(3-moved)
    plus=(125+fixed)//2; minus=(125-fixed)//2
    out["involution_carriers"].append({"natural_moving_rank":2*moved,"carrier_trace":fixed,"eigenspaces":[plus,minus]})

# Exact endpoint and universal monotonicity constants.
rank_two_involution=(1-F(1,5**3))/4
all_involution=(1-F(1,5**2))/4
rank_two_unipotent=F(1,2)*F(4,5)*F(4,5)
delta=F(31,250)
assert rank_two_involution==F(31,125)
assert all_involution==F(6,25)
assert rank_two_unipotent==F(8,25)
assert rank_two_involution/2==delta<all_involution
assert delta<rank_two_unipotent/2 and delta<F(1,4)
ceiling=F(6)/(10*delta-1)
assert ceiling==25 and 2*5**3==250
out["constants"]={"rank_two_involution":str(rank_two_involution),"all_involution":str(all_involution),"rank_two_unipotent":str(rank_two_unipotent),"normalizer_support":str(delta),"source_degree_ceiling":str(ceiling),"elementary_factor_degree_floor":250}

tex=BASE/"higher_odd_symplectic_five_section.tex"
content=tex.read_text()
assert content.count(r"\[")==content.count(r"\]")
assert content.count(r"\begin{proof}")==content.count(r"\end{proof}")==4
assert ",+not" not in content
out["proof_sha256"]=hashlib.sha256(tex.read_bytes()).hexdigest()
out["elapsed_seconds"]=time.perf_counter()-started
(BASE/"check_higher_symplectic_five.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
