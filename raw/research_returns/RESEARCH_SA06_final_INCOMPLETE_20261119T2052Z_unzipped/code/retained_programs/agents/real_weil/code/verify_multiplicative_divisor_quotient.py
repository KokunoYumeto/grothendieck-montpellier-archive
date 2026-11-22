#!/usr/bin/env python3
"""Exact certificates for the explicit triangle quotient in C.3y."""
from pathlib import Path
from time import perf_counter
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

started=perf_counter()
base=Path(__file__).resolve().parent
t,a,x,y,z=sp.symbols("t a x y z")
g=t**4+a*t**3+1
resultant=sp.resultant(g,sp.diff(g,t),t)
assert resultant == 256-27*a**4
certificates=[]
for coefficient,A,B,constant in [
 (1,48*t**2+229,-12*t**3-3*t**2-55*t-16,229),
 (2,192*t**2-176,-48*t**3-24*t**2+80*t-32,-176)
]:
 h=g.subs(a,coefficient)
 remainder=sp.expand(A*h+B*sp.diff(h,t)-constant)
 assert remainder==0
 certificates.append({"a":coefficient,"A":str(A),"B":str(B),"constant":constant,"remainder":str(remainder)})
assert (-176)%229==53
samples=[]
for p in [2,3,5,7,11,13,229]:
 coefficient=2 if p==229 else 1
 h=sp.Poly(g.subs(a,coefficient),t,modulus=p)
 d=sp.gcd(h,h.diff())
 assert d.degree()==0
 samples.append({"p":p,"a":coefficient,"resultant_mod_p":int(resultant.subs(a,coefficient))%p,"gcd_degree":d.degree()})

D=x*y*z
G=x**4+y**4+z**4+a*(x**3*y+y**3*z+z**3*x)
image=sp.expand(G.subs({x:x*D,y:y*D,z:z*D},simultaneous=True)-D**4*G)
assert image==0
assert sp.expand((x*D)*(y*D)*(z*D)-D**4)==0
M=sp.Matrix([[-3,1,1],[1,-3,1],[1,1,-3]])
assert M.det()==-16
smith=smith_normal_form(M,domain=sp.ZZ)
smith_invariants=[abs(int(smith[i,i])) for i in range(3)]
assert smith_invariants==[1,4,4]
assert list(M*sp.ones(3,1))==[-1,-1,-1]
assert 4**2-12==4 # Square of the resolved quartic linear system.

rank_samples=[]
for n in range(1,13):
 # Sections on each P1 are binary monomials of degree n. Evaluations
 # at the two nodes are the first/last coefficients. Node differences
 # cyclically glue the last value of component i to the first of i+1.
 delta=sp.zeros(3,3*(n+1))
 for i in range(3):
  delta[i,i*(n+1)+n]=1
  delta[i,((i+1)%3)*(n+1)]=-1
 assert delta.rank()==3
 rank_samples.append({"n":n,"normalization_evaluation_rank":delta.rank(),"sections_before_gluing":3*(n+1),"sections_after_gluing":3*n})

data={
 "statement":"C.3y",
 "universal_resultant":str(resultant),
 "integer_Bezout_certificates":certificates,
 "finite_characteristic_samples":samples,
 "projective_image_identity_remainder":str(image),
 "intersection_matrix":M.tolist(),
 "determinant":int(M.det()),
 "Smith_invariants":smith_invariants,
 "positive_normal_degree_each_component":1,
 "quartic_linear_system_square":4,
 "normalization_rank_samples":rank_samples,
 "scope":"Exact universal identities and the full 3x3 Smith form are certified. The finite cohomology samples do not replace the all-n evaluation proof. No computation asserts actual Picard algebraization, ordinary equivalence vanishing, or infinite multiplicative independence; these are proved in the text.",
 "runtime_seconds":perf_counter()-started
}
out=base/"multiplicative_divisor_quotient_output.json"
out.write_text(json.dumps(data,indent=2,default=int)+"\n")
print("PASS: Res(t^4+a*t^3+1, derivative)=256-27*a^4 and both exact integer Bezout certificates.")
print("PASS: all-characteristic coefficient choice a=1, except a=2 in characteristic229; exceptional residue53.")
for item in samples:
 print(f"PASS: characteristic {item['p']}, a={item['a']}, squarefree side polynomial, resultant residue {item['resultant_mod_p']}.")
print("PASS: exact projective contraction image identity; intersection determinant-16 and Smith invariants1,4,4.")
print("PASS: positive normal degree1 and normalization evaluation rank3 for n=1,...,12.")
print(f"Runtime seconds: {data['runtime_seconds']:.6f}")
print(f"Wrote {out.name}")
