"""Exact symbolic pair/triangle formulas for the proposed permanent residue map.
This is an algebraic computation, not a proof of arbitrary-size dominance.
"""
from pathlib import Path
import sympy as s
import json,datetime
A=s.symbols('a b c d',nonzero=True)
def basis(e):
 i,j=e
 return {(i,j):s.Integer(1),(i,i):A[i]/(A[j]-A[i]),(j,j):A[j]/(A[i]-A[j])}
def raw(e,f,i):
 a,b=e;c,d=f
 if a==c or b==d:return s.Integer(0)
 U={a,b,c,d}
 if i not in U:return s.Integer(0)
 return (-A[i])**(len(U)-2)/s.prod(A[j]-A[i] for j in U-{i})
def val(e,f):return [s.factor(sum(x*y*raw(ee,ff,i) for ee,x in basis(e).items() for ff,y in basis(f).items())) for i in range(4)]
cases={'self':((0,1),(0,1)),'reverse':((0,1),(1,0)),'row':((0,1),(0,2)),'column':((0,1),(2,1)),'chain':((0,1),(1,2)),'cochain':((0,1),(2,0)),'disjoint':((0,1),(2,3))}
out={}
for name,es in cases.items():
 v=val(*es);assert s.simplify(sum(v))==0;out[name]=[str(x) for x in v];print(name,es,v)
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps({'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Exact symbolic tensor simplifications; no uniform rank theorem','a_variables':list(map(str,A)),'cases':out},indent=2)+'\n')
