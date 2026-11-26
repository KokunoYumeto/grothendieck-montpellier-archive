#!/usr/bin/env python3
"""Independent exact arithmetic checks for Paper 2, pp. 78--81.

Written before execution. This verifies displayed rational identities and the
finite numerical table; it does not verify geometry or prove an infinite search.
"""
import json
import sympy as sp

s, g, d = sp.symbols("s g d")
h = (12*g + 8)*(g - 1)/(g*g - g - 1)
n = 12*(g - 1)*(3*g*g - 4*g - 4)/(g*(3*g*g - 12*g + 15))
R = 12*s*s/(s*s - s - 1)
P = (s*s - s - 1)*(5*g*g - 15*g + 4) - (s + 1)*g*(3*g*g - 12*g + 15)
checks = {}

def identity(label, lhs, rhs):
    residual = sp.factor(lhs-rhs)
    assert residual == 0, (label, residual)
    checks[label] = {"residual": str(residual), "verified": True}

identity("h derivative", sp.diff(h,g), -4*(2*g*g+2*g+1)/(g*g-g-1)**2)
identity("n derivative", sp.diff(n,g), -4*(5*g*g*((g-3)**2-2)+4*(g-1)*(3*g-5))/(g**3-4*g*g+5*g)**2)
identity("n minus h", n-h, 4*(g-1)*(3*g+2)*(g*g-4*g+2)/(g*(g*g-4*g+5)*(g*g-g-1)))
identity("n minus R", n-R, 12*P/((s*s-s-1)*g*(3*g*g-12*g+15)))
identity("P at ell four", P.subs(g,2*s+1), -2*s*(2*s**3+21*s*s+2*s-5))
identity("hyperelliptic ell one", h.subs(g,1+s/2)-R, 4*s*(s*s-s-10)/((s*s-s-1)*(s*s+2*s-4)))
identity("hyperelliptic ell two", h.subs(g,1+s)-R, -4*s*(s*s+5*s+5)/((s*s-s-1)*(s*s+s-1)))
identity("P at ell two", P.subs(g,s+1), s*(2*s**3-10*s*s-3*s+5))
identity("P at ell three", P.subs(g,1+3*s/2), sp.Rational(3,8)*s*(3*s**3-59*s*s-8*s+20))
identity("n at six", n.subs(g,6), sp.Rational(800,51))
identity("conductor six external difference", sp.Rational(300,19)-sp.Rational(800,51), sp.Rational(100,969))
identity("conductor six internal difference numerator", (300*d/(19*d+1)-sp.Rational(800,51))*51*(19*d+1), 100*d-800)

table=[]
for p in [3,5,7,11,13,17,19,23,29,31]:
    candidates=[]
    for a in range(5,2*p+2):
        if a%2==1 and (a+1)%(p-1)==0:
            candidates.append((a,1,(a+1)//2))
        if a>=7 and (2*a)%(p-1)==0:
            candidates.append((a,2,a))
        if a>=21 and a%2==1 and (3*a-1)%(p-1)==0:
            candidates.append((a,3,(3*a-1)//2))
    minimum=min(a for a,ell,genus in candidates)
    rows=[{"ell":ell,"genus":genus} for a,ell,genus in candidates if a==minimum]
    expected={3:5,5:7,7:5,11:9,13:11}.get(p,(p-1)//2)
    assert minimum==expected,(p,minimum,expected)
    table.append({"p":p,"minimum_a":minimum,"surviving_rows":rows})

print(json.dumps({"sympy_version":sp.__version__,"scope":"Exact displayed identities on pp.78--81 and the ten-prime numerical table; no geometric computation.","checks":checks,"sample_table":table,"all_assertions_passed":True},indent=2))
