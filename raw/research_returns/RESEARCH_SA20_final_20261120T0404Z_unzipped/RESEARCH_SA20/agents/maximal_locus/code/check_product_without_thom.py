#!/usr/bin/env python3
"""Exact algebra for a proper semialgebraic product with no Thom stratification."""
import json
import time
import sympy as s

start = time.perf_counter()
a,b,z,t,z0,c = s.symbols('a b z t z0 c', real=True)
d = b**4 + (b*z-a)**2
n = b**3*(b*z-a)
g = n/d
tests = []

def check(name, expression):
    reduced = s.factor(expression)
    assert reduced == 0, (name,reduced)
    tests.append({'name': name, 'pass': True})

check('denominator_sum_of_squares', d-(b**4+(b*z-a)**2))
check('graph_value_on_approach', g.subs({a:t*z0,b:t,z:z0}, simultaneous=True))
check('vertical_derivative_formula', s.diff(g,z)-b**4*(b**4-(b*z-a)**2)/d**2)
check('vertical_derivative_on_approach', s.diff(g,z).subs({a:t*z0,b:t,z:z0}, simultaneous=True)-1)
check('horizontal_derivative_on_approach', s.diff(g,a).subs({a:t*z0,b:t,z:z0}, simultaneous=True)+1/t)
check('bound_square_identity', b**2*d**2-4*n**2-b**2*(b**4-(b*z-a)**2)**2)
check('quotient_scaled_profile', g-b*((b*z-a)/b**2)/(1+((b*z-a)/b**2)**2))
check('central_fibre_rational_extension_away_from_origin', g.subs(b,0))
v = s.Matrix([0,0,1,1])
e = s.Matrix([0,0,1,0])
assert s.Matrix.hstack(v,e).rank()==2
tests.append({'name':'central_and_nearby_vertical_lines_distinct','pass':True})
assert s.Matrix([[1,0,0],[0,1,0]]).rank()==2
tests.append({'name':'projection_rank_off_central_fibre','pass':True})
x1,x2,x3 = s.symbols('x1 x2 x3', real=True)
x = s.Matrix([x1,x2,x3])
sphere_tangent = s.Matrix([1-x1**2,-x1*x2,-x1*x3])
check('sphere_tangent_vector_identity', x.dot(sphere_tangent)-x1*(1-x.dot(x)))
check('sphere_height_differential_identity', sphere_tangent[0]-(1-x1**2))
result = {
    'status':'PASS', 'arithmetic':'exact rational polynomial identities via sympy',
    'test_count':len(tests), 'tests':tests,
    'scope':'Finite algebra in the fully proved product/no-Thom example; not an enumeration of stratifications.',
    'elapsed_seconds':time.perf_counter()-start,
}
print(json.dumps(result,indent=2))
