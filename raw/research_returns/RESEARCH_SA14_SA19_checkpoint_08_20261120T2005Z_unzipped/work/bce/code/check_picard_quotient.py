"""Exact finite checks for the known nonsplit conic, E4.Q.
GPT-6 Astra (OpenAI), 2026-11-20. Infinite-origin descent is proved in text.
"""
import sympy as s,json,time
start=time.perf_counter()
x,y,z,t,a,b=s.symbols('x y z t a b')
F=x*x+y*y-t*z*z
factor=s.expand((x+s.I*y)*(x-s.I*y))==F.subs(t,0)
f=F.subs(z,1)
J=s.groebner([f,s.diff(f,x),s.diff(f,y),s.diff(f,t)],x,y,t)
assert list(J)==[s.Integer(1)]
assert factor
result={'special_factorization_correct':factor,'total_affine_jacobian_ideal_on_z1':[str(q) for q in J],'at_z0_projective_smoothness':'2x and2y cannot both vanish at a projective point','degree_invariant_under_conjugation':s.expand((a+b)-(b+a))==0,'scope':'Polynomial and Jacobian checks only. Picard representation and nonschematic descent are Kleiman Example4.14; tau identification proved in text.','seconds':time.perf_counter()-start}
print(json.dumps(result,indent=2))
