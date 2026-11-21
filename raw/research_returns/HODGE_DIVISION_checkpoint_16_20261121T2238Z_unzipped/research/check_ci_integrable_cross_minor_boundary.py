"""Root exact certificate for an actual integrable CI boundary example."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import combinations
import hashlib,json,time
import sympy as s
t0=time.perf_counter();F=s.Rational
J=s.Matrix.hstack(s.Matrix([1,0,-F(3,5),-F(8,5)]),s.Matrix([0,1,1,1]),s.Matrix([1,0,-F(9,5),-F(16,5)]),s.Matrix([0,1,2,3]))
pi=s.zeros(4);pi[0,1]=1;pi[1,0]=-1
eta=s.zeros(4);eta[2,3]=1;eta[3,2]=-1
p=J*pi*J.T;q=J*eta*J.T
pairs=list(combinations(range(4),2))
assert [p[i,j] for i,j in pairs]==[1,1,1,F(3,5),F(8,5),1]
assert [q[i,j] for i,j in pairs]==[1,2,3,F(9,5),F(16,5),1]
assert J.det()==-F(4,5) and p.rank()==q.rank()==2
z=s.symbols('x y z w');ell=J*s.Matrix(z)
actual=s.Matrix([s.expand(v**2) for v in ell]).jacobian(z)
assert actual==2*s.diag(*ell)*J
a=s.symbols('l1:5');D=s.diag(*a)
P=4*D*p*D;Q=4*D*q*D
def residue(f):
 return s.expand(sum(c*s.prod(x**n for x,n in zip(a,mon)) for mon,c in s.Poly(s.expand(f),*a).terms() if all(n<2 for n in mon)))
for i,j in pairs:
 for k,l in pairs:
  assert residue(P[i,j]*Q[k,l]-Q[i,j]*P[k,l])==0
def wedge(U,V):
 return s.expand(U[0,1]*V[2,3]-U[0,2]*V[1,3]+U[0,3]*V[1,2]+U[2,3]*V[0,1]-U[1,3]*V[0,2]+U[1,2]*V[0,3])
socle=-F(64,5)*s.prod(a)
assert residue(wedge(P,Q))==socle
assert residue((2*D*J).det())==socle
assert socle!=0 and all(residue(x*socle)==0 for x in a)
assert residue(wedge(P,P))==residue(wedge(Q,Q))==0
out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-t0,'J_determinant':str(J.det()),'length':16,'embedding_dimension':4,'ordered_pair_minors_checked':len(pairs)**2,'Jacobian_socle':str(socle),'scope':'Actual formal-gradient CI counterexample to unrestricted scalar-cross-minor inference only; no companion-matrix solution or module deformation asserted.','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('ci_integrable_cross_minor_boundary_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
