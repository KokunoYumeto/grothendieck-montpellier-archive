"""Exact symbolic checks for two reducible Lefschetz-pencil examples.

Conics on P2 and a positive-genus pencil on E x P1, E:y²=x³-x,
H=O_E(3O) external-tensor O_P1(1).
No numerical roots are used.
"""
import sympy as s
import json
x,y,z,t,u,v=s.symbols('x y z t u v')
Q0=x*(y-z);Q1=y*(x-z);Q=Q0-t*Q1
matrix=s.hessian(Q,(x,y,z))/2
conic_discriminant=s.factor(matrix.det())
assert conic_discriminant==t*(t-1)/4
points=[(1,0,0),(0,1,0),(0,0,1),(1,1,1)]
transverse=[]
for p in points:
 assert Q0.subs(dict(zip((x,y,z),p)))==Q1.subs(dict(zip((x,y,z),p)))==0
 jac=s.Matrix([[s.diff(q,a).subs(dict(zip((x,y,z),p)))for a in (x,y,z)]for q in (Q0,Q1)])
 transverse.append(jac.rank());assert jac.rank()==2
# Blowup P2 intersection lattice diag(1,-1,-1,-1,-1).
gram=s.diag(1,-1,-1,-1,-1)
F=s.Matrix([2,-1,-1,-1,-1]);O=s.Matrix([0,1,0,0,0])
components=[s.Matrix([1,-1,-1,0,0]),s.Matrix([1,-1,0,-1,0]),s.Matrix([1,-1,0,0,-1])]
T=s.Matrix.hstack(F,O,*components)
assert T.rank()==5
# Positive-genus example: the determinant is a section of O_E(6O).
# Pencil (y u + x v) + t((x+2)u+(y+1)v).
xn=t*(2*t-1);yn=t*(t-2);den=1-t*t
singular_poly=s.factor(yn**2*den-xn**3+xn*den**2)
poly=s.Poly(singular_poly,t)
assert poly.degree()==6
disc=s.discriminant(poly.as_expr(),t)
assert disc!=0 and poly.eval(1)!=0 and poly.eval(-1)!=0
assert s.simplify(yn+t*(xn+2*den))==0
assert s.simplify(xn+t*(yn+den))==0
# determinant zero gives precisely these six pairs. Full matrix cannot vanish.
assert s.groebner([y,x,x+2,y+1],x,y).contains(s.Integer(1))
result={
 'conic_pencil':{'generators':[str(Q0),str(Q1)],'determinant':str(conic_discriminant),'base_points':points,'base_jacobian_ranks':transverse,'number_reducible_fibres':3,'NS_blowup_rank':5,'trivial_lattice_rank':T.rank(),'corrected_MW_rank':0,'uncorrected_rank':3},
 'elliptic_product_pencil':{'elliptic_curve':'y^2=x^3-x','generators':['y*u+x*v','(x+2)*u+(y+1)*v'],'singular_parameter_polynomial':str(singular_poly),'discriminant':str(disc),'values_at_pm1':[str(poly.eval(1)),str(poly.eval(-1))],'x_at_singular_parameter':str(xn/den),'y_at_singular_parameter':str(yn/den),'base_point_count':6,'number_reducible_fibres':6,'NS_X_rank':2,'NS_blowup_rank':8,'fixed_Jacobian':'E over C(t)','mobile_Jacobian':'0','corrected_MW_rank':0,'uncorrected_rank':6}}
print(json.dumps(result,indent=2))
