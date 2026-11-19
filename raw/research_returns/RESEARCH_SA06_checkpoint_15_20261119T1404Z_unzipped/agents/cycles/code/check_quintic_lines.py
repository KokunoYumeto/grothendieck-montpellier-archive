#!/usr/bin/env python3
"""Exact finite certificates for C.1g; no numerical period approximation.

The mathematical proof supplies generic smoothness, Abel--Jacobi functoriality,
and non-torsion. This script checks the displayed finite algebraic data only.
"""
from __future__ import annotations

import itertools
import json
import platform
import time
from pathlib import Path

import sympy as sp


def main() -> None:
    started = time.perf_counter()
    monomials = [e for e in itertools.product(range(6), repeat=5)
                 if sum(e) == 5 and sum(e[2:]) > 0
                 and e[0]+e[1]+e[4] > 0]
    assert len(monomials) == 114
    distinguished = (0, 0, 0, 0, 5)
    assert distinguished in monomials

    x0, x1, x2, x3, x4 = x = sp.symbols("x0 x1 x2 x3 x4")
    u, v = sp.symbols("u v")
    fstar = (x2*x0**4 + x3*x0**2*x1**2 + x4*x1**4
             + x0*x2**4 + x1*x2**2*x3**2 + x4*x3**4 + x4**5)
    line0 = {x0:u, x1:v, x2:0, x3:0, x4:0}
    line1 = {x0:0, x1:0, x2:u, x3:v, x4:0}
    normal0 = [sp.diff(fstar, z).subs(line0) for z in (x2,x3,x4)]
    normal1 = [sp.diff(fstar, z).subs(line1) for z in (x0,x1,x4)]
    expected = [u**4, u**2*v**2, v**4]
    assert normal0 == expected == normal1
    target_basis = [u**(5-j)*v**j for j in range(6)]
    columns = [sp.expand(z*q) for q in expected for z in (u,v)]
    matrix = sp.Matrix([[sp.Poly(col,u,v).coeff_monomial(mon)
                         for col in columns] for mon in target_basis])
    assert matrix == sp.eye(6)

    a,b,c,d,t,s = sp.symbols("a b c d t s")
    sform = (x2-b*x3)/(d-b)
    tform = x1-a*x3-(c-a)*sform
    def qform(tvar, svar):
        return (tvar**4 + 5*c*tvar**3*svar + 10*c**2*tvar**2*svar**2
                + 10*c**3*tvar*svar**3 + 5*c**4*svar**4)
    qidentity = sp.expand(t*qform(t,s) - ((t+c*s)**5-c**5*s**5))
    assert qidentity == 0
    la = {x0:t, x1:a*s, x2:b*s, x3:s}
    lb = {x0:t, x1:t+c*s, x2:d*s, x3:s}
    restrictions = {
        "S_on_la": sp.simplify(sform.subs(la, simultaneous=True)),
        "T_on_la": sp.simplify(tform.subs(la, simultaneous=True)),
        "S_on_lb": sp.simplify(sform.subs(lb, simultaneous=True)),
        "T_on_lb": sp.simplify(tform.subs(lb, simultaneous=True)),
    }
    assert restrictions == {"S_on_la":0,"T_on_la":0,"S_on_lb":s,"T_on_lb":t}
    k0 = x1**5+x2**5+x3**5-x0*qform(tform,sform)
    ka = sp.simplify(k0.subs(la, simultaneous=True))
    kb = sp.simplify(k0.subs(lb, simultaneous=True))
    assert sp.expand(ka-s**5*(a**5+b**5+1)) == 0
    assert sp.expand(kb-s**5*(c**5+d**5+1)) == 0
    kh = sp.simplify(k0.subs(x0,0))
    assert kh == x1**5+x2**5+x3**5
    k_at_e0 = sp.simplify(k0.subs({x0:1,x1:0,x2:0,x3:0}))
    assert k_at_e0 == 0
    coordinate_matrix = sp.Matrix([
        [1,0,1,0,1],
        [0,a,1,c,0],
        [0,b,0,d,0],
        [0,1,0,1,0],
        [0,0,0,0,1],
    ])
    determinant = sp.factor(coordinate_matrix.det())
    assert determinant == d-b
    # With G in I(la union lb), G(e0)=0; hence W(q0)=1+K(e0)=1.
    assert 1+k_at_e0 == 1

    # The two principal ideal charts for the blow-up lift.
    U0,Kval,Tval,Vval = sp.symbols("U0 Kval Tval Vval", nonzero=True)
    relation = U0*Vval**4 + Tval**4*Kval
    tchart = sp.simplify(relation.subs(Kval,-U0*(Vval/Tval)**4))
    vchart = sp.simplify(relation.subs(U0,-Kval*(Tval/Vval)**4))
    assert tchart == vchart == 0

    out = {
        "identity":"GPT-6 Astra (OpenAI), cycles child, RESEARCH_SA06, 2026-11-19",
        "python_version":platform.python_version(),
        "sympy_version":sp.__version__,
        "monomial_exponent_set":monomials,
        "monomial_count":len(monomials),
        "independent_parameter_count":len(monomials)-1,
        "normalized_monomial":distinguished,
        "normal_derivative_test_polynomial":str(fstar),
        "normal_derivatives_line0":list(map(str,normal0)),
        "normal_derivatives_line1":list(map(str,normal1)),
        "normal_global_section_matrix":[[int(v) for v in row] for row in matrix.tolist()],
        "normal_matrix_determinant":int(matrix.det()),
        "interpolation_restrictions":{k:str(val) for k,val in restrictions.items()},
        "Q_identity_zero":str(qidentity),
        "K0_on_la":str(ka),
        "K0_on_lb":str(kb),
        "K0_on_H":str(kh),
        "change_of_coordinates_matrix":list(map(lambda row:list(map(str,row)),coordinate_matrix.tolist())),
        "change_of_coordinates_determinant":str(determinant),
        "K0_at_e0":str(k_at_e0),
        "blowup_relation_charts_zero":[str(tchart),str(vchart)],
        "scope":"Finite exact polynomial and linear-algebra certificates only. Generic smoothness, non-torsion and non-algebraic-equivalence are proved in quintic_lines.tex; no sampled point or period numerics are used to infer them.",
        "runtime_seconds":time.perf_counter()-started,
        "all_assertions_passed":True,
    }
    output = Path(__file__).resolve().parents[1]/"output"/"check_quintic_lines.json"
    output.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))


if __name__ == "__main__":
    main()
