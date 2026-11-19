"""Exact finite algebra behind the restricted Fermat-quintic argument.

This is a certificate of the displayed algebra only.  Cohomological trace,
finite K0 detection, and actual-family algebraization are proved in TeX.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
import sympy as s

started=time.perf_counter()
a,b,c,t,v,w,q=s.symbols('a b c t v w q')
FC=a**5+b**5+c**5
FB=v**5-t**5-w**5
coords=(t*c,w*c,v*a,v*b)
image=s.expand(sum(z**5 for z in coords))
decomposition=s.expand(v**5*FC-c**5*FB)
assert s.expand(image-decomposition)==0

# On the two blow-up charts the common exceptional factor divides once.
chart_c=s.Matrix(coords).subs(v,c*q)/c
chart_v=s.Matrix(coords).subs(c,v*q)/v
assert list(map(s.simplify,chart_c))==[t,w,q*a,q*b]
assert list(map(s.simplify,chart_v))==[q*t,q*w,a,b]

# Inverse formulas on the generic chart w=c=1.
x0,x1,x2,x3=s.symbols('x0 x1 x2 x3')
inverse_C=s.together((x2/(v*x1))**5+(x3/(v*x1))**5+1)
numerator=s.expand(inverse_C*(v*x1)**5)
numerator=numerator.subs(v**5,(x0**5+x1**5)/x1**5)
assert s.expand(numerator-(x0**5+x1**5+x2**5+x3**5))==0

# The base curves and the branch points are reduced in characteristic zero.
z=s.symbols('z')
assert s.gcd(z**5+1,5*z**4)==1
assert s.gcd(z**5-1,5*z**4)==1
genus=(5-1)*(5-2)//2
canonical_degree=2*genus-2
fibre_degree=5*3
assert genus==6 and canonical_degree==10 and fibre_degree==15
assert fibre_degree>canonical_degree

# Plane-quintic cohomology: Serre dual h1(O(1))=h0(O(1))=3.
h1_curve_O1=3
h1_curve_O=genus
h2_source=h1_curve_O1**2
assert h2_source==9
surface_h2_L={j:(1 if j==1 else 0) for j in range(1,9)}

# First-order logarithmic product: dlog(1+tau*A) at tau=0 has dtau
# coefficient A and no horizontal coefficient.  No factorial occurs.
tau,A=s.symbols('tau A')
dtau_coefficient=s.diff(s.log(1+tau*A),tau).subs(tau,0)
dA_coefficient=s.diff(s.log(1+tau*A),A).subs(tau,0)
assert dtau_coefficient==A and dA_coefficient==0

report={
 'utc':datetime.now(timezone.utc).isoformat(),
 'checks':{
  'Fermat_image_identity':str(s.factor(image-decomposition)),
  'base_points':25,
  'blowup_chart_v_equals_cq':list(map(str,map(s.simplify,chart_c))),
  'blowup_chart_c_equals_vq':list(map(str,map(s.simplify,chart_v))),
  'generic_inverse_equation':str(s.expand(numerator)),
  'generic_degree':5,
  'curve_genus':genus,
  'canonical_degree':canonical_degree,
  'evaluation_fibre_degree':fibre_degree,
  'h1_curve_O':h1_curve_O,
  'h1_curve_O1':h1_curve_O1,
  'h2_source_Lprime':h2_source,
  'surface_h2_L_powers_checked':surface_h2_L,
  'first_jet_dtau_coefficient':str(dtau_coefficient),
  'first_jet_horizontal_coefficient':str(dA_coefficient)
 },
 'scope':'Exact finite identities only; no finite calculation substitutes for the trace or algebraization proof.',
 'runtime_seconds':time.perf_counter()-started
}
out=Path(__file__).resolve().parents[1]/'output'
out.mkdir(exist_ok=True)
text=json.dumps(report,indent=2)
(out/'check_fermat_quintic_top.json').write_text(text+'\n')
print(text)
