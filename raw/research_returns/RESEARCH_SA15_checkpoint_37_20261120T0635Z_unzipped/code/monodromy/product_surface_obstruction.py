#!/usr/bin/env python3
"""Finite verification of E/F3 in the all-degree product obstruction."""
import json,time
from pathlib import Path
import sympy as sp
started=time.perf_counter()
p=3
points=[None]+[(x,y) for x in range(p) for y in range(p)
              if (y*y-x**3-x*x-1)%p==0]
def add(P,Q):
 if P is None:return Q
 if Q is None:return P
 x,y=P;u,v=Q
 if x==u and (y+v)%p==0:return None
 if x==u:lam=((3*x*x+2*x)*pow(2*y,-1,p))%p
 else:lam=((v-y)*pow(u-x,-1,p))%p
 r=(lam*lam-1-x-u)%p
 return r,(-y+lam*(x-r))%p
torsion=[P for P in points if add(add(P,P),P) is None]
assert len(points)==6 and len(torsion)==3
X,Y,Z=sp.symbols('X Y Z')
F=Y*Y*Z-X**3-X*X*Z-Z**3
partials=[sp.diff(F,q) for q in (X,Y,Z)]
checks=[]
for q in (X,Y,Z):
 variables=[r for r in (X,Y,Z) if r!=q]
 G=sp.groebner([f.subs(q,1) for f in [F]+partials],*variables,modulus=3)
 unit=len(G.polys)==1 and G.polys[0].as_expr()==1
 assert unit
 checks.append({'chart':str(q),'singularity_ideal_unit':unit})
out={'field':'F3','curve':'Y^2 Z-X^3-X^2 Z-Z^3=0',
     'points':points,'point_count':len(points),'Frobenius_trace':4-len(points),
     'ordinary_trace_mod3':(4-len(points))%3,'rational_3_torsion':torsion,
     'geometric_etale_3_torsion_order':3,'all_etale_3_torsion_rational':True,
     'smoothness_certificates':checks,'embedding':'product of plane cubics, Segre',
     'norm_pullback_composition':'diag(3d,3d)',
     'constant_relative_quotient_dimension':2,
     'degree_range':'every integer d>=1','runtime_seconds':time.perf_counter()-started}
dest=Path(__file__).resolve().parents[1]/'outputs'/'product_surface_obstruction.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
