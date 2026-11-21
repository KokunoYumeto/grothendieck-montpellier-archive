#!/usr/bin/env python3
"""Exact exterior calculation for the mixed HYM identity SF-E811.4.

This certifies a generic real primitive (1,1) form, not merely examples.
The holonomy/descent and stable-bundle arguments are proved separately.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as S

DIM=8

def wedge(a,b):
    out={}
    for m,c in a.items():
        for n,d in b.items():
            if m&n:
                continue
            parity=sum((n&((1<<i)-1)).bit_count()
                       for i in range(DIM) if m>>i&1)
            key=m|n
            out[key]=out.get(key,0)+(-1)**parity*c*d
    return {k:S.expand(v) for k,v in out.items() if S.expand(v)!=0}

def add(*forms):
    out={}
    for f in forms:
        for k,v in f.items():out[k]=out.get(k,0)+v
    return {k:S.expand(v) for k,v in out.items() if S.expand(v)!=0}

def scale(c,f):return {k:c*v for k,v in f.items()}
def one(i):return {1<<i:1}
def pair(i,j):return wedge(one(i),one(j))

e=[pair(2*i,2*i+1) for i in range(4)]
omega1=add(e[0],e[1])
omega2=add(e[2],e[3])
omega=add(omega1,omega2)
volume={255:1}
x1,x2,x3=S.symbols('x1 x2 x3',real=True)
xs=[x1,x2,x3,-x1-x2-x3]
alpha=add(*(scale(x,e0) for x,e0 in zip(xs,e)))
params=[x1,x2,x3]
mixed=[]
pure=[]
for i,j in combinations(range(4),2):
    b,c=S.symbols(f'b{i+1}{j+1} c{i+1}{j+1}',real=True)
    s=add(pair(2*i,2*j+1),pair(2*j,2*i+1))
    t=add(pair(2*i,2*j),pair(2*i+1,2*j+1))
    assert wedge(s,s)==scale(-2,wedge(e[i],e[j]))
    assert wedge(t,t)==scale(-2,wedge(e[i],e[j]))
    alpha=add(alpha,scale(b,s),scale(c,t))
    params.extend([b,c])
    (mixed if i<2<=j else pure).extend([b,c])

assert len(params)==15 and len(mixed)==8 and len(pure)==4
raw=wedge(wedge(wedge(alpha,alpha),omega1),omega2).get(255,0)
rhs=2*((x1+x2)**2+sum(v*v for v in mixed))
assert S.expand(-raw-rhs)==0

Q=S.hessian(rhs,params)/2
assert Q.rank()==9
assert len(Q.nullspace())==6
assert set(Q.eigenvals())=={S.Integer(0),S.Integer(2),S.Integer(4)}
assert Q.eigenvals()=={S.Integer(0):6,S.Integer(2):8,S.Integer(4):1}

# The primitive four-dimensional Hodge-star energy constant.
normsq=sum(v*v for v in xs)+2*sum(v*v for v in params[3:])
raw_full=wedge(wedge(alpha,alpha),wedge(omega,omega)).get(255,0)
assert S.expand(-raw_full-2*normsq)==0

# Pure eigenspace square has zero mixed pairing and nonzero ample pairing.
C=scale(S.Rational(1,2),add(wedge(omega1,omega1),wedge(omega2,omega2)))
assert not wedge(wedge(C,omega1),omega2)
assert wedge(C,wedge(omega,omega))=={255:4}

out={
 "status":"PASS",
 "arithmetic":"exact symbolic rational/integer exterior algebra",
 "real_primitive_11_dimension":15,
 "mixed_quadratic_form":str(S.factor(rhs)),
 "mixed_energy_matrix_rank":9,
 "mixed_energy_matrix_eigenvalues":{"0":6,"2":8,"4":1},
 "zero_locus":"all8 mixed coefficients0 and x1+x2=0; each block primitive",
 "full_primitive_energy_constant":2,
 "balanced_C_mixed_pairing":0,
 "balanced_C_ample_pairing_in_unit_coordinates":4,
 "limits":"Does not certify HYM existence, holonomy algebra descent, or any geometric nonexistence theorem by itself."
}
Path(__file__).with_name('rm_curvature_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
