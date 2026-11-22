"""Exact finite checks for the D10 coefficient/elliptic example and D7 caveat.

The C2 example addresses the common-refinement convention only; the program
explicitly verifies its failure of the stronger parallel-equalizer condition.
"""
import itertools, json, pathlib, time
start=time.monotonic()
F=list(itertools.product(range(5),repeat=2))
def add(x,y):return ((x[0]+y[0])%5,(x[1]+y[1])%5)
def mul(x,y):return ((x[0]*y[0]+3*x[1]*y[1])%5,(x[0]*y[1]+x[1]*y[0])%5)
def power(x,n):
    result=(1,0)
    for _ in range(n):result=mul(result,x)
    return result
assert all((a*a+2)%5 for a in range(5))
roots=[x for x in F if power(x,3)==(1,0)]
assert len(roots)==3 and all(x==(1,0) or power(x,2)!= (1,0) for x in roots)
assert all(sum(mul(x,y)==(1,0) for y in F)==1 for x in F if x!=(0,0))
def group_ring_mul(x,y):return ((x[0]*y[0]+x[1]*y[1])%5,(x[0]*y[1]+x[1]*y[0])%5)
plus=(3,3);minus=(3,2)
assert group_ring_mul(plus,plus)==plus
assert group_ring_mul(minus,minus)==minus
assert group_ring_mul(plus,minus)==(0,0)
assert tuple((x+y)%5 for x,y in zip(plus,minus))==(1,0)
points=[(x,y) for x in range(3) for y in range(3) if (y*y-x**3+x)%3==0]
singular=[(x,y) for x,y in points if (-3*x*x+1)%3==0 and (2*y)%3==0]
assert not singular
two_torsion=[P for P in points if P[1]==0]
assert (0,0) in two_torsion and len(two_torsion)==3
# Homogeneous F=Y^2 Z-X^3+XZ^2 has unique point [0:1:0] at infinity.
# Its Z-derivative there is Y^2+2XZ=1, so that point is nonsingular.
infinity=(0,1,0)
assert (infinity[1]**2 + 2*infinity[0]*infinity[2])%3==1
id2=(0,1);swap=(1,0)
intertwiners=[]
for a in itertools.permutations(range(2)):
    if all(a[id2[x]]==swap[a[x]] for x in range(2)):intertwiners.append(a)
assert intertwiners==[]
H=range(2)
P2_orbits=[{(0,0),(1,1)},{(0,1),(1,0)}]
assert set.union(*P2_orbits)==set(itertools.product(H,H))
assert all({((a+1)%2,(b+1)%2) for a,b in orbit}==orbit for orbit in P2_orbits)
assert not any(h==(1+h)%2 for h in H)
out={'F25':{'polynomial':'X^2+2 over F5','elements':25,'nonzero_inverse_checks':24,'third_roots':roots},
     'C2_group_algebra':{'plus_idempotent':plus,'minus_idempotent':minus,'orthogonal':True},
     'elliptic_F3':{'equation':'y^2=x^3-x','affine_points':points,'singular_affine_points':singular,'nonzero_two_torsion':two_torsion,'projective_point_at_infinity_nonsingular':True},
     'C2_common_refinement_counterexample':{'first_component_intertwiners':intertwiners,'regular_product_orbits':[sorted(o) for o in P2_orbits],'parallel_equalizer_condition':False,'scope':'common refinements, not strict cofilteredness'},
     'runtime_seconds':round(time.monotonic()-start,6)}
path=pathlib.Path(__file__).with_name('check_examples_extended_output.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
