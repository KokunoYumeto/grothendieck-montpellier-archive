#!/usr/bin/env python3
"""Exact finite algebra used in the complete proof of A5.015.

The universal nonexistence of finite Thom stratifications is proved in the
paper. This program checks the displayed identities and rank minor only.
"""
import json
import time
import sympy as s

start = time.perf_counter()
a,b,c,u,a0,t,x1,x2,x3,v1,v2,v3,du = s.symbols(
    'a b c u a0 t x1 x2 x3 v1 v2 v3 du', real=True
)
x = s.Matrix([x1,x2,x3])
v0 = s.Matrix([1-x1**2,-x1*x2,-x1*x3])
coords = s.Matrix([a,b,x1,x2,x3,u])
f = s.Matrix([a,b,u**3-b*x1])
j = f.jacobian(coords)
tests = []

def check(name, expression):
    reduced = s.factor(expression)
    assert reduced == 0, (name,reduced)
    tests.append({'name':name,'pass':True})

check('product_inverse_cube_identity', (c+b*x1).subs(c,u**3-b*x1)-u**3)
check('sphere_tangent_vector_identity', x.dot(v0)-x1*(1-x.dot(x)))
check('height_differential_identity', v0[0]-(1-x1**2))
approach = {a:a0,b:t,u:0}
for i,value in enumerate([a0,t,-t*x1]):
    check(f'approach_target_coordinate_{i+1}', f[i].subs(approach)-value)
vertical = s.Matrix([0,0,v1,v2,v3,du])
check('full_vertical_differential', (j*vertical)[2]-(3*u**2*du-b*v1))
check('approaching_vertical_differential', (j*vertical)[2].subs(approach)+t*v1)
central = s.Matrix([0,0,*v0,0])
check('central_sphere_direction_in_kernel', (j*central)[2].subs({b:0,u:0}))
check('excluded_direction_on_approach', (j*central)[2].subs(approach)+t*(1-x1**2))
u_direction = s.Matrix([0,0,0,0,0,1])
check('u_direction_in_approaching_kernel', (j*u_direction)[2].subs(approach))
a_direction = s.Matrix([1,0,0,0,0,0])
b_direction = s.Matrix([0,1,0,0,0,0])
rank_minor = s.Matrix.hstack(j*a_direction,j*b_direction,j*central).det()
check('rank_three_minor_on_approach', rank_minor.subs(approach)+t*(1-x1**2))

print(json.dumps({
    'statement_id':'A5.015','status':'PASS',
    'arithmetic':'exact rational polynomial identities via sympy',
    'test_count':len(tests),'tests':tests,
    'nonzero_minor':'-t*(1-x1**2), nonzero under the proved assumptions t>0 and |x1|<1',
    'scope':'Finite algebra only; the universal finite-stratification obstruction is proved mathematically.',
    'elapsed_seconds':time.perf_counter()-start,
},indent=2))
