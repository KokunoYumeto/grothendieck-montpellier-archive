#!/usr/bin/env python3
"""Independent exact first-jet and exterior audit for SF-E825.

No author code is imported. Generic function derivatives are retained in
the variable-b calculation. Global descent and semiregularity remain
proof obligations, not claims made by this finite symbolic certificate.
"""
from pathlib import Path
import sympy as s
import hashlib,json,time

B=Path(__file__).resolve().parent
PROOF=B.parent.parent/'sixfolds/rm_free_summand_overlap_draft.md'
coords=s.symbols('x y t z');x,y,t,z=coords
pc=s.symbols('p01 p02 p03 p12 p13 p23')
Pi=s.zeros(4);pos=0
for i in range(4):
 for j in range(i+1,4):Pi[i,j]=pc[pos];Pi[j,i]=-pc[pos];pos+=1

def bracket(a,b):
 return s.expand(sum(Pi[i,j]*s.diff(a,coords[i])*s.diff(b,coords[j]) for i in range(4) for j in range(4)))

def pb(A,C):return s.Matrix(A.rows,C.cols,lambda i,j:sum(bracket(A[i,k],C[k,j])/2 for k in range(A.cols)))
def eq(A,C):return all(s.expand(a-c)==0 for a,c in zip(A,C))
def onS(a):return s.simplify(a.subs({x:0,y:0},simultaneous=True))
def Vprojection(M):return s.Matrix([[onS(-s.diff(M[0,0],y)),onS(s.diff(M[1,1],x))]])

def wedge(a,b):
 out={}
 for I,ai in a.items():
  for J,bj in b.items():
   if I&J:continue
   sign=(-1)**sum((I>>(k+1)).bit_count() for k in range(8) if J>>k&1)
   out[I|J]=s.expand(out.get(I|J,0)+sign*ai*bj)
 return {I:a for I,a in out.items() if a!=0}

def interior(a,k):
 out={}
 for I,c in a.items():
  if I>>k&1:out[I^(1<<k)]=(-1)**(I&((1<<k)-1)).bit_count()*c
 return out

def main():
 start=time.perf_counter();v=s.Matrix([-y,x]);w=s.Matrix([[x,y]]);d=v*w;P=pc[0]
 correction=s.Rational(3,2)*P*s.eye(2)
 assert eq(d*v,s.zeros(2,1)) and eq(pb(d,v)+correction*v,s.zeros(2,1))
 # Full overlap, from an independent four-coordinate bivector.
 G0=t*s.eye(2);G1=t**3*s.eye(2);G2=s.Matrix([[t**4]])
 dj=t**2*d;vj=t*v;Pj=bracket(t*x,t*y)
 O=G0*(s.Rational(3,2)*Pj*s.eye(2))-correction*G1+pb(G0,dj)-pb(d,G1)
 O1=pb(G1,vj)-pb(v,G2)
 assert eq(O*vj+d*O1,s.zeros(2,1))
 alpha,beta=bracket(t,x),bracket(t,y)
 zeta=s.Matrix([-beta,alpha]);row=s.Matrix([[alpha,beta]])
 assert eq(O/t**3,(s.Rational(1,2)*zeta*w+s.Rational(7,2)*v*row)/t)
 assert eq(Vprojection(O/t**3),s.Rational(7,2)*row/t)
 # Completely varying b, including all tangential derivatives.
 b=s.Matrix([[s.Function('b1')(*coords),s.Function('b2')(*coords)]])
 tb=(b*v)[0];delta=v*b;jb=s.Matrix([b[1],-b[0]])
 Ob=delta*correction-correction*(tb*s.eye(2))+pb(delta,d)-pb(d,tb*s.eye(2))
 c=sum(bracket(b[l],v[l]) for l in range(2))
 AA=s.Matrix([v[i]*c+sum(v[l]*bracket(b[l],v[i]) for l in range(2)) for i in range(2)])
 BB=s.Matrix([[sum(v[l]*bracket(b[l],w[k]) for l in range(2)) for k in range(2)]])
 variable=s.Rational(1,2)*AA*w+v*BB
 assert eq(Ob-P*(v*b-jb*w),variable)
 assert all(onS(a)==0 for a in list(AA)+list(BB))
 assert eq(Vprojection(Ob),s.Matrix([[P*onS(b[0]),P*onS(b[1])]]))
 # Scalar plus nilpotent gives the derivative of ell modulo I^2.
 a=s.Function('a')(*coords)
 Oa=s.Matrix(2,2,lambda i,j:bracket(a,d[i,j]))
 ell=a+tb
 assert eq(Vprojection(Oa+Ob),s.Matrix([[onS(bracket(ell,x)),onS(bracket(ell,y))]]))
 # Every factorization through a free summand is killed by ell.
 m=s.Matrix(s.symbols('m1 m2'));pm=(w*m)[0]
 bm=s.Matrix([[m[1],-m[0]]])
 assert eq(m*w-pm*s.eye(2),v*bm) and s.expand(pm+(bm*v)[0])==0
 # Full degree-zero product includes the off-diagonal free contribution.
 a0,a1,c0=s.symbols('a0 a1 c0');bb=s.Matrix([s.symbols('bb1 bb2')]);cc=s.Matrix([s.symbols('cc1 cc2')])
 bbv=(bb*v)[0];ccv=(cc*v)[0]
 a2=a0*a1+c0*pm
 b2=a0*cc+a1*bb+bbv*cc+c0*bm
 assert s.expand(a2+(b2*v)[0]-(a0+bbv)*(a1+ccv))==0
 # Rank-three determinant derivation identity, with independent first jets.
 aa=s.symbols('a0:9');ee=s.symbols('e0:9');A=s.Matrix(3,3,aa);E=s.Matrix(3,3,ee)
 jet=s.symbols('jet')
 assert s.expand(s.trace(A.adjugate()*E)-s.diff((A+jet*E).det(),jet).subs(jet,0))==0
 # Full sixteen-variable simultaneous (1,1) kernel.
 cv=s.symbols('c0:16');C={};theta={}
 for i in range(4):
  theta[(1<<i)|(1<<(4+i))]=1
  for j in range(4):C[(1<<i)|(1<<(4+j))]=cv[4*i+j]
 CD=wedge(C,theta)
 plus=interior(interior(CD,0),1);minus=interior(interior(CD,2),3)
 assert all(I&15==0 and I.bit_count()==2 for I in set(plus)|set(minus))
 polys=list(plus.values())+list(minus.values())
 matrix=s.Matrix([[s.diff(p,c) for c in cv] for p in polys])
 expected=[cv[0]+cv[5],cv[10]+cv[15]]+[cv[4*i+j] for i in range(4) for j in range(4) if (i<2)!=(j<2)]
 target=s.Matrix([[s.diff(p,c) for c in cv] for p in expected])
 assert matrix.rank()==target.rank()==matrix.col_join(target).rank()==10
 theta2=wedge(theta,theta)
 assert interior(interior(theta2,0),1) and interior(interior(theta2,2),3)
 top=wedge(wedge(theta2,theta),C)
 assert len(top)==1
 topcoeff=list(top.values())[0]
 assert s.expand(topcoeff-6*(cv[0]+cv[5]+cv[10]+cv[15]))==0
 result={'status':'PASS independent symbolic and exterior audit',
         'reviewed_proof_sha256':hashlib.sha256(PROOF.read_bytes()).hexdigest(),
         'author_code_imported':False,'generic_bivector_coefficients':6,
         'variable_b':'two unrestricted smooth formal functions of all four coordinates; exact derivative-boundary formula verified',
         'frame_U_coefficient':'1/2','frame_V_coefficient':'7/2',
         'endomorphism_ell':'full free-factor product cancellation verified',
         'determinant_rank':3,'class_matrix_variables':16,'simultaneous_kernel_codimension':10,
         'kernel':'two primitive traces plus eight mixed-block entries',
         'limits':'Does not prove global Cech descent, categorical Hochschild compatibility, a finite action, or any semiregular seed.',
         'seconds':round(time.perf_counter()-start,6)}
 (B/'audit_free_summand_overlap.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))

if __name__=='__main__':main()
