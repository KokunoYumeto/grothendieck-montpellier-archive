"""Bounded exact algebra supporting NP.1--8; not a test of genericity or Chow classes."""
from datetime import datetime,timezone
from pathlib import Path
import json,time
import sympy as sp
b=Path(__file__).resolve().parents[1]
started=datetime.now(timezone.utc).isoformat();tick=time.perf_counter();checks=[]
def check(name,ok,data=None):
 checks.append({'name':name,'passed':bool(ok),'data':data});assert ok,name
x0,x1,x2,x3,l,x,y,t,z,v,w=sp.symbols('x0 x1 x2 x3 l x y t z v w')
A=x1**2-x0*x3;B=x2**2-x1*x3+x0*x1;B2=x2**2+x0*x2-x1*x3
coords=[x0,x1,x2,x3]
det=sp.factor(sp.hessian(B+l*A,coords).det())
check('odd_characteristic_gradient_determinant',sp.expand(det+4*l*(l-1)*(l+1))==0,str(det))
red=sp.rem(det,l*l+1,l)
check('odd_root_minus_one_reduction',red==8*l,str(red))
for name,f in [('B',B2),('A_plus_B',A+B2)]:
 matrix=sp.hessian(f,coords).applyfunc(lambda q:int(q)%2)
 check('char2_gradient_'+name,int(matrix.det())%2==1,{'matrix':matrix.tolist(),'det_mod2':int(matrix.det())%2})
check('odd_affine_weierstrass',sp.expand(B.subs({x0:1,x3:x1*x1}))==x2*x2-x1**3+x1)
check('char2_affine_weierstrass',sp.expand(B2.subs({x0:1,x3:x1*x1}))==x2*x2+x2-x1**3)
for name,f in [('odd',B),('two',B2)]:
 gradients=sp.Matrix([[sp.diff(g,u).subs({x0:0,x1:0,x2:0,x3:1}) for u in coords] for g in [A,f]])
 check('infinity_gradient_independence_'+name,gradients.rank()==2,gradients.tolist())
check('first_saturated_chart_equation',sp.expand((x*y-t*z).subs({t:x*v,y:v*z},simultaneous=True))==0)
check('second_saturated_chart_equation',sp.expand((x*y-t*z).subs({x:t*w,z:w*y},simultaneous=True))==0)
counts={'12':4*6,'13':2*6,'23':2*6}
check('node_counts',sum(counts.values())==48,counts)
allocation=[counts['12']+counts['13'],counts['23'],0]
check('ordered_component_blowup_allocation',allocation==[36,12,0],allocation)
weights=[2,1,0];degrees=[weights[0]-weights[1],weights[0]-weights[2],weights[1]-weights[2]]
check('small_curve_positive_degrees',degrees==[1,2,1],degrees)
# Edges are 12,13,23, oriented from smaller to larger component.
d1=sp.Matrix([[-1,-1,0],[1,0,-1],[0,1,1]])
d2=sp.Matrix([[1]*4,[-1]*4,[1]*4])
check('dual_boundary_square_zero',d1*d2==sp.zeros(3,4))
check('dual_betti_numbers',d1.rank()==2 and d2.rank()==1,{'b0':3-d1.rank(),'b1':3-d1.rank()-d2.rank(),'b2':4-d2.rank()})
for j in range(1,4):
 a=sp.zeros(4,1);a[0]=-1;a[j]=1
 check('period_generator_'+str(j+1),d2*a==sp.zeros(3,1),list(a))
check('sextic_parameter_count',sp.binomial(9,3)==84,84)
record={'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-tick,'checks':checks,'passed':all(q['passed'] for q in checks),'scope':'Only explicit quadric gradient identities, two local chart equations, node allocation, positive small-curve degrees and the finite dual chain complex. No computer verification of generic Bertini, projective geometry, non-torsion periods, ordinary family equivalence or any Chow nonvanishing.'}
(b/'output/SNC_nonzero_period_model_certificate.json').write_text(json.dumps(record,indent=2,default=str)+'\n')
print(json.dumps(record,indent=2,default=str))
