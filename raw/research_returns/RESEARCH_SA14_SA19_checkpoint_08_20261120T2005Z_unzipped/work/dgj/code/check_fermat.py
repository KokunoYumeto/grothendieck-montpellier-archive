"""Finite algebra checks for the explicitly specified Fermat quartic.
The infinite-order assertion is Bloch1984, Theorem4.1, not a computation.
"""
import json, time
from pathlib import Path
import sympy as s
start=time.perf_counter()
x,y,z=s.symbols('x y z')
f=x**4+y**4-z**4
partials=[s.diff(f,v) for v in (x,y,z)]
charts={}
for v in (x,y,z):
    remaining=[w for w in (x,y,z) if w!=v]
    G=s.groebner([p.subs(v,1) for p in partials]+[f.subs(v,1)],*remaining,domain=s.QQ)
    charts[str(v)+'=1']=[str(p) for p in G.polys]
    assert G.contains(s.Integer(1))
assert f.subs({x:1,y:0,z:1})==0
out={'equation':str(f),'field':'algebraic closure of Q','basepoint':[1,0,1],
     'singular_ideal_chart_groebner_bases':charts,'smooth':True,
     'plane_curve_genus':(4-1)*(4-2)//2,
     'minus_one_action_on_H4':(-1)**4,
     'noncomputational_dependency':'Bloch1984 Introduction p95 and Theorem4.1 p104',
     'elapsed_seconds':time.perf_counter()-start}
Path(__file__).with_name('check_fermat_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
