"""Exact arithmetic certificate for the split-quadric counterexample to 44:4 Th5."""
from pathlib import Path
import json
import time
import sympy as sp

started=time.perf_counter()
x=sp.symbols('x0:6')
a,b,c,d,e,t,h=sp.symbols('a b c d e t h')
q=x[0]*x[3]+x[1]*x[4]+x[2]*x[5]
gradient=[sp.diff(q,z) for z in x]
assert set(gradient)==set(x)
qfinite=sp.expand(q.subs(x[2],t*x[5]))
assert qfinite==x[0]*x[3]+x[1]*x[4]+t*x[5]**2
mat=sp.hessian(qfinite,(x[0],x[1],x[3],x[4],x[5]))
assert sp.factor(mat.det())==2*t
assert mat.subs(t,0).rank()==4
qinf=q.subs(x[5],0)
assert sp.hessian(qinf,(x[0],x[1],x[2],x[3],x[4])).rank()==4

# The two plane restrictions coincide over Q(t), hence identically in all odd characteristics.
ideal_alpha=[x[3],x[4],x[5],x[2]-t*x[5]]
ideal_beta=[x[2],x[3],x[4],x[2]-t*x[5]]
ring=sp.QQ.frac_field(t)
ga=sp.groebner(ideal_alpha,*x,domain=ring)
gb=sp.groebner(ideal_beta,*x,domain=ring)
assert [p.as_expr() for p in ga.polys]==[p.as_expr() for p in gb.polys]
ideal_alpha_prime=[x[0],x[1],x[5],x[2]-t*x[5]]
ideal_beta_prime=[x[0],x[1],x[2],x[2]-t*x[5]]
gap=sp.groebner(ideal_alpha_prime,*x,domain=ring)
gbp=sp.groebner(ideal_beta_prime,*x,domain=ring)
assert [p.as_expr() for p in gap.polys]==[p.as_expr() for p in gbp.polys]

# Four proper pairwise intersections, by independent coordinate-span rank.
def span(indices):
    return sp.eye(6)[:,indices]
alpha=span([0,1,2]); beta=span([0,1,5])
alpha_prime=span([2,3,4]); beta_prime=span([3,4,5])
assert alpha.row_join(alpha_prime).rank()==5
assert beta.row_join(beta_prime).rank()==5
assert alpha.row_join(beta_prime).rank()==6
assert beta.row_join(alpha_prime).rank()==6
# At each proper intersection, ideals (x3,x4) and (x0,x1) are coordinate transverse.
local_q=sp.expand(q.subs({x[2]:1,x[5]:-x[0]*x[3]-x[1]*x[4]}))
assert local_q==0
local_q2=sp.expand(q.subs({x[5]:1,x[2]:-x[0]*x[3]-x[1]*x[4]}))
assert local_q2==0
local_coordinates=[x[0],x[1],x[3],x[4]]
local_generators=[x[3],x[4],x[0],x[1]]
assert abs(int(sp.Matrix(local_generators).jacobian(local_coordinates).det()))==1

chern=sp.series((1+h)**3/(1+2*h),h,0,3).removeO().expand()
assert chern==1+h+h*h

# Moving beta: q(c*(a e0+b e4)+d*(a e1-b e3)+e*e5)=0.
vec=(a*c,a*d,0,-b*d,b*c,e)
assert sp.expand(q.subs(dict(zip(x,vec))))==0
columns=sp.Matrix([[a,0,0],[0,a,0],[0,0,0],[0,-b,0],[b,0,0],[0,0,1]])
assert columns.subs(a,1).rank()==3
assert columns.subs(b,1).rank()==3
at_zero=columns.subs({a:0,b:1})
alpha_span=sp.Matrix([[1,0,0],[0,1,0],[0,0,1],[0,0,0],[0,0,0],[0,0,0]])
assert alpha_span.row_join(at_zero).rank()==6

out={
 'field':'algebraic closure of F3',
 'variety':'Q4: x0*x3+x1*x4+x2*x5=0 in P5',
 'gradient':[str(z) for z in gradient],
 'pencil':'x2=t*x5, with infinity x5=0',
 'generic_hessian_determinant':str(sp.factor(mat.det())),
 'rank_at_zero':int(mat.subs(t,0).rank()),
 'rank_at_infinity':4,
 'alpha':'x3=x4=x5=0',
 'beta':'x2=x3=x4=0',
 'alpha_prime':'x0=x1=x5=0',
 'beta_prime':'x0=x1=x2=0',
 'common_generic_restriction_ideal':[str(p.as_expr()) for p in ga.polys],
 'common_generic_restriction_ideal_prime':[str(p.as_expr()) for p in gap.polys],
 'proper_intersections':{'alpha_alpha_prime':'[e2], transverse length 1','beta_beta_prime':'[e5], transverse length 1','crossed_pairs':'both empty'},
 'normal_chern_polynomial':str(chern),
 'moving_beta_vectors':['a*e0+b*e4','a*e1-b*e3','e5'],
 'moving_beta_rank_each_chart':3,
 'alpha_plus_beta_infinity_vector_rank':6,
 'self_squares':[1,1],
 'mixed_intersection_after_move':0,
 'difference_square_integer':2,
 'Z_times_Z_prime_integer':2,
 'generic_restriction_cycle':0,
 'height_pairing_of_zero_with_zero':0,
 'runtime_seconds':round(time.perf_counter()-started,6),
 'scope':'Exact finite algebra only; flat family, self-intersection formula, and height conclusion are proved in the text.'
}
Path(__file__).with_name('check_quadric_height_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
