#!/usr/bin/env python3
"""Independent full exterior-algebra checks for the E819 actual example.

The universal deformation and finite-perfect trace proof is audited in prose;
this computation checks the rank36 example in all256 exterior coordinates,
not just in the author's two-variable quotient.
"""
from pathlib import Path
from math import factorial
import hashlib, json
import sympy as s


def clean(a):
    return {k: s.simplify(v) for k, v in a.items() if s.simplify(v) != 0}


def add(*xs):
    out = {}
    for x in xs:
        for k, v in x.items():
            out[k] = out.get(k, 0) + v
    return clean(out)


def scale(a, c):
    return clean({k: c * v for k, v in a.items()})


def wedge(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            if i & j:
                continue
            inversions = sum((j & ((1 << k) - 1)).bit_count() for k in range(8) if i >> k & 1)
            out[i | j] = out.get(i | j, 0) + (-1) ** inversions * x * y
    return clean(out)


def exp(a):
    term = {0: s.Integer(1)}
    out = dict(term)
    for k in range(1, 5):
        term = wedge(term, a)
        out = add(out, scale(term, s.Rational(1, factorial(k))))
    return out


def theta(H):
    return add(*[scale(wedge({1 << (2*i): 1}, {1 << (2*j+1): 1}), H[i,j])
                 for i in range(4) for j in range(4)])


def contract(a, v):
    out = {}
    for mask, c in a.items():
        for k, x in enumerate(v):
            if x and mask >> k & 1:
                sign = (-1) ** ((mask & ((1 << k) - 1)).bit_count())
                key = mask ^ (1 << k)
                out[key] = out.get(key, 0) + c * x * sign
    return clean(out)


u = s.sqrt(2)
A = s.Matrix([[1,1],[1,-1]])
U = s.diag(A,A)
S = s.diag(1,1,-1,-1)
I = s.eye(4)
assert U*U == 2*I and U*S == S*U
tp, tm = theta((I+U/u)/2), theta((I-U/u)/2)
X, Y = theta(S), theta(U*S)
x, y = scale(add(X,scale(Y,1/u)),s.Rational(1,2)), scale(add(X,scale(Y,-1/u)),s.Rational(1,2))
assert add(wedge(x,x),wedge(tp,tp)) == {}
assert add(wedge(y,y),wedge(tm,tm)) == {}
assert wedge(wedge(x,x),wedge(y,y)) == {255:4}
H = add(scale(add(exp(X),exp(scale(X,-1))),6),
        scale(add(exp(scale(Y,s.Rational(1,2))),exp(scale(Y,s.Rational(-1,2)))),12))
E = add(H,{255:-2})
q=s.Rational(2,3)
vp=add({0:1},scale(wedge(tp,tp),-q/2))
vm=add({0:1},scale(wedge(tm,tm),-q/2))
v=wedge(vp,vm)
assert E == scale(v,36)
assert E[0] == 36 and E[255] == 16
assert wedge(E,E)[255] == 2304
cap_checks=[]
for sign in (1,-1):
    root=sign*u-1
    v1=[1,0,root,0,0,0,0,0]
    v2=[0,0,0,0,1,0,root,0]
    form=tp if sign==1 else tm
    eta=contract(contract(scale(wedge(form,form),s.Rational(1,2)),v1),v2)
    assert eta
    cap=contract(contract(v,v1),v2)
    assert add(cap,scale(wedge(eta,v),q)) == {}
    cap_checks.append({'eigenvalue_sign':sign,'eta_nonzero':True,'cap_kernel':True})
T0=s.Matrix([[1,0],[1,1+s.I]])
T=s.diag(T0,T0)
pull=s.simplify(T.conjugate().T*U*S*T)
assert pull==s.diag(2,-2,-2,2)
assert s.simplify(T.det()*s.conjugate(T.det()))==4
proof=Path(__file__).resolve().parents[2]/'sixfolds/rm_local_quantization_obstruction_draft.md'
out={'status':'PASS','scope':'full256-coordinate exterior algebra, cap kernels, integral pullback and actual Chern identities; not a computational proof of categorical deformation',
     'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
     'rank':int(E[0]),'top_character_integral':int(E[255]),'self_Euler':int(wedge(E,E)[255]),
     'full_hull_character':{str(k):str(z) for k,z in H.items()},
     'full_nonpure_character':{str(k):str(z) for k,z in E.items()},
     'both_independent_cap_kernels':cap_checks,'isogeny_degree':4,'extension_space_dimension':6*36*34,
     'author_program_imported':False}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if not k.startswith('full_')},indent=2))
