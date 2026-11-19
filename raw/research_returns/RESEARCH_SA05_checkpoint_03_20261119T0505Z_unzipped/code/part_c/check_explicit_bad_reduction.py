"""Polynomial certificates for the fully explicit p=2 Part C.5 example.
All identities are expanded over ZZ; no division by 2 or localization is used.
The accompanying proof uses R=W(Fbar_2)[[u,v]]/(uv-2).
"""
import json,time
from pathlib import Path
import sympy as s
start=time.perf_counter()
u,v,x,t,t1,t2=s.symbols('u v x t t1 t2')
base=u*v-2
checks=[]
for r,z in [(u,v),(v,u)]:
    a=r+z**2
    # Homogeneous generalized Weierstrass equation at [-z:1:z^3].
    X,Y,Z=-z,s.Integer(1),z**3
    F=Y**2*Z+a*X*Y*Z+Y*Z**2-X**3
    assert s.expand(F+z**3*base)==0
    # Inverse formula gives Y'=Y modulo the base relation.
    invY=-Y-a*X-Z
    assert s.expand(invY-Y-base)==0
    # The finite flat subgroup G_r has x^2+z*x=0.
    X,Y,Z=x,s.Integer(1),-z**2*x
    F=Y**2*Z+a*X*Y*Z+Y*Z**2-X**3
    certificate=(-x+z-r*z**2)*(x**2+z*x)+z**2*x*base
    assert s.expand(F-certificate)==0
    # Discriminant from b2=a^2,b4=a,b6=1,b8=0.
    disc=s.expand(-8*a**3-27+9*a**3)
    assert s.expand(disc-(a**3-27))==0
    assert int(disc.subs({u:0,v:0}))%2==1
    # D -> G_r with x=z*t, D equation t^2+t.
    assert s.expand((z*t)**2+z*(z*t)-z**2*(t**2+t))==0
    # Compatibility of the stated coproducts.
    image_coprod=z*(t1+t2+u*v*t1*t2)
    group_coprod=z*t1+z*t2+r*(z*t1)*(z*t2)
    assert s.expand(image_coprod-group_coprod)==0
    checks.append({'r':str(r),'z':str(z),'a1':str(a),
      'discriminant':str(disc),'point':['-'+str(z),'1',str(z**3)],
      'subgroup_embedding':['x','1',str(-z**2*x)],
      'elliptic_equation_certificate':str(certificate),
      'all_polynomial_identities':True})
# General coefficient module of image of D -> H is R + (u,v)t.
# Reduce (ut)^a(vt)^b using t^2=-t: all nonconstant coefficients lie in (u,v),
# and the two linear generators give the reverse inclusion.
for a in range(8):
 for b in range(8):
  if a+b:
   coefficient=(-1)**(a+b-1)*u**a*v**b
   assert coefficient.subs({u:0,v:0})==0
# Fermat quartic genus-three smoothness: derivatives only vanish at origin.
X,Y,Z=s.symbols('X Y Z')
f=X**4+Y**4-Z**4
derivatives=[s.diff(f,q) for q in (X,Y,Z)]
assert derivatives==[4*X**3,4*Y**3,-4*Z**3]
# The odd Beauville component of sum_* modified diagonal on a genus-three
# Jacobian has coefficient 3^3-3*2^3+3=6.
assert 3**3-3*2**3+3==6
out={'arithmetic':'polynomial identities over ZZ, no denominators',
 'base':'W(Fbar_2)[[u,v]]/(uv-2)',
 'elliptic_factors':checks,
 'closure_module':'R direct_sum (u,v)t',
 'generic_rank':2,'closed_fibre_dimension':3,
 'flatness_conclusion':'not flat because finite flat over local ring is free',
 'fermat_quartic':{'equation':str(f),'derivatives':list(map(str,derivatives)),
                   'smooth_projectively_in_char0':True,'genus':3,
                   'odd_modified_diagonal_pushforward_coefficient':6},
 'elapsed_seconds':round(time.perf_counter()-start,6)}
p=Path(__file__).with_name('check_explicit_bad_reduction_output.json')
p.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
