#!/usr/bin/env python3
"""Exact finite certificates for C.3at; no numerical smoothness tests.

Universal existence is proved in the TeX.  This checks sample small primes,
including primes dividing the Calabi--Yau degree, by Groebner bases in every
projective chart over a finite coefficient field.
"""
import itertools
import json
from pathlib import Path
import time
from datetime import datetime, timezone
import sympy as s

started = time.perf_counter()
root = Path(__file__).resolve().parent

def coeff_hasse(F, xs, p):
    return s.Poly(s.expand(F**(p-1)), *xs).coeff_monomial(
        s.prod(x**(p-1) for x in xs))

def candidate(p, r, lam, field_polynomial=None):
    m = r + 2
    xs = s.symbols('x0:'+str(m))
    if m % p:
        base = sum(x**m for x in xs)
        kind = 'Fermat'
    else:
        base = sum(xs[i]**(m-1)*xs[i+1] for i in range(m-1)) + xs[-1]**m
        kind = 'triangular'
    F = base + lam*s.prod(xs)
    h = coeff_hasse(F, xs, p)
    if field_polynomial is None:
        h = int(h) % p
    else:
        h = s.rem(h, field_polynomial, lam, modulus=p)
    if h == 0:
        return None
    partials = [s.diff(F,x) for x in xs]
    charts = []
    for i, x in enumerate(xs):
        vars_ = tuple(y for y in xs if y != x)
        equations = [s.expand(g.subs(x,1)) for g in [F]+partials]
        if field_polynomial is not None:
            vars_ += (lam,)
            equations.append(field_polynomial)
        G = s.groebner(equations, *vars_, modulus=p)
        unit = len(G.polys) == 1 and G.polys[0].as_expr() == 1
        charts.append(unit)
        if not unit:
            return None
    return {'p':p,'r':r,'N':r+2,'degree':m,'base':kind,'lambda':str(lam),
            'field_polynomial':str(field_polynomial) if field_polynomial is not None else None,
            'equation':str(F),'hasse_coefficient':str(h),
            'projective_chart_unit_ideals':charts,'passed':all(charts)}

cases=[]
for p,r in [(2,2),(3,2),(5,2),(7,2),(2,3),(3,3),(5,3)]:
    found=None
    for lam in range(p):
        found=candidate(p,r,lam)
        if found:
            break
    prime_exhausted = found is None
    if found is None:
        u=s.Symbol('u')
        for a,b in itertools.product(range(p),repeat=2):
            g=u*u+a*u+b
            if not s.Poly(g,u,modulus=p).is_irreducible:
                continue
            found=candidate(p,r,u,g)
            if found:
                break
    if found:
        found['prime_field_search_exhausted']=prime_exhausted
    cases.append(found or {'p':p,'r':r,'prime_and_quadratic_search_exhausted':True,
                           'note':'The universal construction allows larger finite extensions.'})

result={'timestamp_utc':datetime.now(timezone.utc).isoformat(),
        'purpose':'Finite exact smoothness and nonzero Hasse checks only; universal proof is separate.',
        'cases':cases,
        'verified_cases':sum(bool(c.get('passed')) for c in cases),
        'runtime_seconds':time.perf_counter()-started}
out=root/'check_ordinary_cy_boundary_output.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
