#!/usr/bin/env python3
"""Exact local resolution and holomorphic norm checks for SF-E822.

The generic local functions are symbolic; no individual surface is numerically
sampled. The globalization, determinant-degree and semiregularity arguments
remain mathematical proofs, not computational assertions.
"""
from pathlib import Path
import json
import sympy as s

root = Path(__file__).resolve().parent
z = s.symbols('z0:4')
f, g = s.Function('f')(*z), s.Function('g')(*z)
p = s.symbols('p01 p02 p03 p12 p13 p23')
pairs = [(i,j) for i in range(4) for j in range(i+1,4)]


def bracket(a,b):
    if a == 0 or b == 0:
        return s.S.Zero
    return s.expand(sum(c*(s.diff(a,z[i])*s.diff(b,z[j])
                           -s.diff(a,z[j])*s.diff(b,z[i]))
                        for c,(i,j) in zip(p,pairs)))


P = bracket(f,g)
checks = []
for m in (1,2,3):
    I, O = s.eye(m), s.zeros(m)
    E = s.Matrix(m,m,lambda i,j:s.Function(f'E{m}_{i}{j}')(*z))
    d1 = s.BlockMatrix([[-g*I,O,O],[f*I,O,O],[-E,f*I,g*I]]).as_explicit()
    d2 = s.BlockMatrix([[O],[-g*I],[f*I]]).as_explicit()
    assert d1*d2 == s.zeros(3*m,m)
    correction = s.Matrix(3*m,m,lambda i,j:s.expand(
        sum(bracket(d1[i,k],d2[k,j])/2 for k in range(3*m))))
    target = s.BlockMatrix([[O],[O],[-P*I]]).as_explicit()
    assert s.simplify(correction-target) == s.zeros(3*m,m)
    assert not any(v.has(*list(E)) for v in correction)
    E0 = s.Matrix(m,m,s.symbols(f'e{m}_0:{m*m}'))
    h2 = s.Matrix(3*m,m,s.symbols(f'h{m}_0:{3*m*m}'))
    d1red = s.BlockMatrix([[O,O,O],[O,O,O],[-E0,O,O]]).as_explicit()
    A = h2[:m,:]
    target_red = s.BlockMatrix([[O],[O],[-E0*A]]).as_explicit()
    assert d1red*h2 == target_red
    checks.append({'rank':m,'ordinary_square_zero':True,
                   'star_square_bottom':'-P*I','E_derivatives_present':False,
                   'reduced_nullhomotopy_bottom':'-E*A'})


def wedge(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():
            if i&j:
                continue
            inv=sum((j&((1<<r)-1)).bit_count() for r in range(8) if (i>>r)&1)
            k=i|j
            out[k]=s.simplify(out.get(k,0)+(-1)**inv*x*y)
    return {k:v for k,v in out.items() if v != 0}


def add(a,b):
    out=a.copy()
    for k,v in b.items():out[k]=s.simplify(out.get(k,0)+v)
    return {k:v for k,v in out.items() if v != 0}


tp={3:s.I,12:s.I}
tm={48:s.I,192:s.I}
t=add(tp,tm)
t2=wedge(t,t)
op={5:s.S.One}; om={80:s.S.One}
bp={10:s.S.One}; bm={160:s.S.One}
gram=s.Matrix([[wedge(t2,wedge(a,b)).get(255,0)
                for b in (bp,bm)] for a in (op,om)])
assert gram == 2*s.eye(2)
vol=wedge(wedge(tp,tp),wedge(tm,tm)).get(255,0)
assert vol == 4
out={'result':'PASS','convention':'right modules with column-map matrices',
     'local_checks':checks,'generic_bivector_coefficients':6,
     'normal_bracket':str(P),'surface_norm_gram':[[str(x) for x in gram.row(i)] for i in range(2)],
     'theta_plus_squared_theta_minus_squared_top':int(vol),
     'limitation':'Only symbolic resolution/star-square/reduced-homotopy and exterior norm identities are checked. Exactness, global gluing, determinant degree and all-action semiregularity exclusion are proved in the text and require independent review.'}
(root/'rm_coupled_surface_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['result','local_checks','surface_norm_gram']},indent=2))
