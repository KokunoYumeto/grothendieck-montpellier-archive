"""Exact checks of two source-audit issues; no higher-Chow search is simulated.

The graph calculation is a counterexample to finiteness of a generic-point
closure.  The Kerr--Yang check proves degeneracy of the displayed W2 terms;
it does not claim to have implemented every admissibility or boundary test.
"""
from fractions import Fraction
from math import factorial
from time import perf_counter
import sympy as s

start = perf_counter()
print('Generic-point graph: u*y-v*x=0 in P1_[u:v] x A2_[x:y].')
x, y, u, v, t = s.symbols('x y u v t')
graph = u*y-v*x
chart_u = s.expand(graph.subs({u:1,v:t}))
chart_v = s.expand(graph.subs({v:1,u:t}))
print('Chart u=1:', chart_u, '; eliminate y to obtain Q[x,t].')
print('Chart v=1:', chart_v, '; eliminate x to obtain Q[y,t].')
assert chart_u == y-t*x and chart_v == t*y-x
q=2
p1=[(1,a) for a in range(q)]+[(0,1)]
fibres={}
for xx in range(q):
    for yy in range(q):
        fibres[(xx,yy)]=[(uu,vv) for uu,vv in p1 if (uu*yy-vv*xx)%q==0]
print('F_2 fibres:',fibres)
assert len(fibres[(0,0)])==3
assert all(len(points)==1 for point,points in fibres.items() if point!=(0,0))
print('At x=y=0 the equation is identically zero: entire P1, dimension one.')
print('Thus the graph closure is not quasi-finite or finite over A2.')

print('\nKerr--Yang published Section4D: N=2; substituting u=s*v.')
u,v,z=s.symbols('u v s')
for n in [4,5,6]:
    ts=s.symbols('t1:'+str(n-2))  # n-3 parameters
    product=s.prod(a**2 for a in ts)
    numerator=s.prod(u-a**2*v for a in ts)
    ordinary=s.cancel(numerator/((u-product*v)*(u-v)**(n-4)))
    last=s.cancel(numerator*(u-v/product)/(u-v)**(n-2))
    expected_ordinary=s.cancel(s.prod(z-a**2 for a in ts)/((z-product)*(z-1)**(n-4)))
    expected_last=s.cancel(s.prod(z-a**2 for a in ts)*(z-1/product)/(z-1)**(n-2))
    assert s.cancel(ordinary.subs(u,z*v)-expected_ordinary)==0
    assert s.cancel(last.subs(u,z*v)-expected_last)==0
    ordinary_coords=[v*a**2/u for a in ts]+[v/u,u/(v*product)]
    last_coords=[v*a**2/u for a in ts]+[v/(u*product),u/v]
    for f in [ordinary,last]+ordinary_coords+last_coords:
        assert s.diff(s.cancel(f.subs(u,z*v)),v)==0
    print('n=',n,'ordinary ratio=',expected_ordinary,'last ratio=',expected_last)
    print('Every coordinate except final v-1 is independent of v: TRUE.')
print('Since v-1 independently parametrizes the final cube, these W2 terms are degenerate.')
print('This establishes that specific defect, not a complete all-n boundary calculation.')

print('\nNormalization diagnostic only, using the claimed small denominator epsilon_n:')
for n in [3,5,7]:
    eps=2 if n==3 else n-3
    index=Fraction(eps*(2**(n-1)-1),factorial(n-1))
    print('n=',n,'epsilon=',eps,'formal index when |C_n|=1:',index)
print('Nonintegral values diagnose an incompatible premise; no claim about |C_n| is inferred.')
print('The repaired construction clears actual coefficients and includes (n-1)! instead.')
print('Elapsed seconds:',round(perf_counter()-start,6))
