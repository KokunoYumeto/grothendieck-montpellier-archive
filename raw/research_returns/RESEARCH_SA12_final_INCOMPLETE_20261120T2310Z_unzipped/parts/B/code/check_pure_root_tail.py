"""Exact local certificate; this is not a global surface counterexample."""
from pathlib import Path
import json
import time
import sympy as sp

started = time.perf_counter()
x,t,z,s,y,w,u = sp.symbols("x t z s y w u")
variables=(x,t,z,s,y,w,u)
mod2=lambda f: sp.Poly(sp.expand(f), *variables, modulus=2).as_expr()
checks=[]
def check(name, condition):
    assert bool(condition), name
    checks.append(name)

equation=z**2+t+x**3
check("smooth normalized source equation", mod2(sp.diff(equation,t))==1)
check("eliminate target parameter", mod2(equation.subs(t,z**2+x**3))==0)
cusp=z**2+x**3
check("cusp x derivative", mod2(sp.diff(cusp,x))==x**2)
check("cusp z derivative", mod2(sp.diff(cusp,z))==0)
check("normalization parametrization", mod2(cusp.subs({x:w**2,z:w**3}))==0)
blown=s**2*(y**2+s)
check("blowup substitution", mod2(cusp.subs({x:s,z:s*y})-blown)==0)
check("exceptional multiplicity two", sp.Poly(blown,s).terms()[-1][0][0]==2)
check("strict transform smooth", mod2(sp.diff(y**2+s,s))==1)
check("Artin Schreier derivative", mod2(sp.diff(u**2+u,u))==1)
f=1/blown
g=1/(s*y)
claimed=(1+y**3+s*y)/(s*y**2*(y**2+s))
num,den=sp.fraction(sp.together(f+g**2+g+claimed))
check("changed Artin Schreier equation", mod2(num)==0)
leading=(1+y**3)/y**4
check("simple-pole leading coefficient", sp.cancel((s*claimed).subs(s,0)-leading)==0)
check("leading coefficient nonzero", sp.Poly(1+y**3,y,modulus=2).is_zero is False)
check("strict transform misses generic tail", (y**2+s).subs(s,0)==y**2)
output={
 "statement_id":"D:pure-root-rational-tail-obstruction",
 "field":"F_2",
 "assertions":len(checks),
 "passed":len(checks),
 "runtime_seconds":time.perf_counter()-started,
 "checks":checks,
 "scope":"Local counterexample to filling rational tails; not a counterexample to global D.1 or D.2(ii)."
}
path=Path(__file__).resolve().parents[1]/"output"/"pure_root_tail.json"
path.write_text(json.dumps(output,indent=2)+"\n")
print(json.dumps(output,indent=2))
