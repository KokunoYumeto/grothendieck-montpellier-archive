"""Exact checks of the extension worksheets; no manuscript emendation.
All variables are independent over Z unless an explicit quotient is recorded.
The local model uses E=M+L, pi(eta,zeta)=b*eta+chi*zeta.
"""
from pathlib import Path
import sympy as s,json
O=Path(__file__).resolve().parent.parent/'outputs'
chi,gamma,b1,b2,u1,u2,v1,v2=s.symbols('chi gamma b1 b2 u1 u2 v1 v2')
eta1,eta2,zeta1,zeta2,a1,a2,lam1,lam2=s.symbols('eta1 eta2 zeta1 zeta2 a1 a2 lam1 lam2')
checks=[]
def equal(name,lhs,rhs=0):
 r=s.expand(lhs-rhs);assert r==0,(name,r)
 checks.append({'check':name,'residual':str(r),'result':'PASS: exact polynomial identity'})
def U(b,c,x,y):return b*y+x*c+chi*x*y
U0=U(b1,b2,u1,u2)
Up=U(b1+chi*u1,b2+chi*u2,v1,v2)
Utot=U(b1,b2,u1+v1,u2+v2)
equal('scan130 b product changes by chi U',(b1+chi*u1)*(b2+chi*u2)-b1*b2,chi*U0)
equal('scan132 consistent plus convention cocycle',Utot,U0+Up)
mixed=s.expand(Utot-U0-U(b1-chi*u1,b2-chi*u2,v1,v2))
assert s.expand(mixed-2*chi*(u1*v2+u2*v1))==0
checks.append({'check':'scan132 inconsistent sign convention','residual':str(mixed),'witness':'chi=u1=v2=1, u2=v1=0 gives 2 over Z','result':'FAIL as a simultaneous identity; a consistent convention works'})
b,U=s.symbols('b U')
bp=b+chi*U
comm=s.expand((U-gamma*bp)-(-gamma*b-U))
assert s.expand(comm-U*(2-chi*gamma))==0
checks.append({'check':'scan126 comparison square','residual':str(comm),'hypothesis':'gamma*chi=2','result':'PASS under the stated hypothesis, without dividing by chi'})
TU=s.Matrix([[1,0],[U,1]]);Tm=s.Matrix([[1,0],[-U,1]])
assert TU.inv()==Tm
checks.append({'check':'scan128 translations and global minus','inverse':str(TU.inv()),'global_minus_difference':str(Tm-(-Tm)),'result':'T_U inverse is T_-U; a global minus changes both diagonal entries and is not the same map over Z'})
equal('scan128 complementary factor product',(-b1)*(-b2),b1*b2)
checks.append({'check':'scan128 factor/product complement','result':'Complementing both factors preserves b1*b2; complementing the output changes b to -b. These require a comparison, not a literal equality.'})
gammas=[x for x in range(4) if 2*x%4==2]
vs=[-x%4 for x in gammas]
assert gammas==[1,3] and vs==[3,1]
checks.append({'check':'choice of gamma need not be canonical','ring':'Z/4','chi':2,'b':1,'solutions_gamma':gammas,'comparison_parameters':vs,'result':'Distinct valid choices give distinct translations'})
# Local bilinear product q(x1,x2)=(eta, zeta).
eta=eta1*eta2
zeta=b1*eta1*zeta2+b2*zeta1*eta2+chi*zeta1*zeta2
pi1=b1*eta1+chi*zeta1;pi2=b2*eta2+chi*zeta2
equal('vector product respects pi',b1*b2*eta+chi*zeta,pi1*pi2)
f1=a1*eta1+lam1*zeta1;f2=a2*eta2+lam2*zeta2
ff=lam1*pi1*f2+lam2*f1*pi2-chi*f1*f2
coefficient=lam1*b1*a2+lam2*a1*b2-chi*a1*a2
equal('scans136--140 functional product descends',ff,coefficient*eta+lam1*lam2*zeta)
equal('functional product first boundary',ff.subs({eta1:0,zeta1:1}),lam1*lam2*pi2)
equal('functional product second boundary',ff.subs({eta2:0,zeta2:1}),lam1*lam2*pi1)
equal('functional product intersection',ff.subs({eta1:0,zeta1:1,eta2:0,zeta2:1}),chi*lam1*lam2)
equal('scan138 pi1 star pi2 equals chi pi',ff.subs({a1:b1,a2:b2,lam1:chi,lam2:chi}),chi*pi1*pi2)
equal('scan136 maps vanishing on L multiply with negative chi',ff.subs({lam1:0,lam2:0}),-chi*a1*a2*eta)
equal('scan140 restriction arithmetic',2*chi-chi,chi)
checks.append({'check':'scan140 literal 2-chi=1','residual':'1-chi','result':'Not an identity; true only after chi=1. Adjacent correct computation is 2*chi-chi=chi.'})
# chi=2 retraction pi restricts to 2 id_L; no inverse of two.
bb=s.symbols('bb');p=s.Matrix([[0,0],[bb,2]]) # inclusion composed with pi
sigma=s.eye(2)-p
res=s.simplify(sigma*sigma-s.eye(2));assert res==s.zeros(2)
checks.append({'check':'scan142 involution from 2-retraction','sigma_matrix':str(sigma),'square_residual':str(res),'endpoints':'-id on L, id on M','result':'PASS over Z[bb]; independent of invertibility of 2'})
# Compatible and arbitrary maps on a split chi=1 example.
# Order product coordinates (m1*m2, l1*l2). pi_i(m_i)=0, pi_i(l_i)=1.
q=lambda x,y:(x[0]*y[0],x[1]*y[1])
m=(1,0);ell=(0,1);shear=lambda x:(x[0],x[0]+x[1])
before=q(m,ell);after=q(shear(m),ell)
assert before==(0,0) and after==(0,1)
checks.append({'check':'scan144 arbitrary submodule-preserving map','ring':'any nonzero field','chi':1,'input_relation':'m1 star ell2 = 0','image_before':before,'image_after_shear':after,'result':'FAIL descent: f1(m1)=m1+ell1 fixes L1 but violates pi1 f1=f1|L pi1'})
(O/'extension_checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
print(json.dumps(checks,ensure_ascii=False,indent=2))
