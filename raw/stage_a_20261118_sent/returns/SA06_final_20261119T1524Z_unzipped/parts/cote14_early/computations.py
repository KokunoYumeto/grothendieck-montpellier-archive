#!/usr/bin/env python3
"""Exact checks for cote14_early. Finite examples are labelled as such.

Run: python computations.py > audit/computations_output.txt
General proofs, hypothesis checks and limitations are in proof_checks.md.
"""
import sympy as s
import re
from fractions import Fraction
from pathlib import Path
def out(label,value): print(label+': '+str(value))
out('runtime','Python exact integers/rationals; SymPy '+s.__version__)
x,t,a,N,m,r,j,n,i=s.symbols('x t a N m r j n i',integer=True)
out('T01 weight after N Tate twists',a+N*m)
out('T02 infinite-intersection obstruction at m=-N-1',(m+N).subs(m,-N-1))
out('T03 cone generators solution for (1,-1)',s.solve([2*a+N-1,N+1],[a,N]))
out('T04 normalized Tate weight',(t*t).expand())
out('T05 positivity x^2-x+1 completed square',s.expand((x-s.Rational(1,2))**2+s.Rational(3,4)))
out('T06 lowest negative exponent test, t^-1 as t->0+',s.limit(t**-1,t,0,dir='+'))
out('T07 theta(GL2(g)) determinant',s.factor((s.det(s.Matrix([[a,N],[m,r]]))**-2)*s.det(s.Matrix([[a,N],[m,r]]))))
out('L01 symbolic [L,Lambda] coefficient',s.expand(j*(r-j+1)-(j+1)*(r-j)))
out('L02 symbolic Casimir eigenvalue',s.expand((2*j-r)**2+2*(2*j-r)+4*(j+1)*(r-j)))
out('L03 symbolic unit-step coefficient',s.cancel(j*(r-j+1)/(j*(r-j+1))))
for rr in range(9):
    d=rr+1; L=s.zeros(d); La=s.zeros(d); H=s.diag(*[2*jj-rr for jj in range(d)])
    for jj in range(rr): L[jj+1,jj]=1
    for jj in range(1,d): La[jj-1,jj]=jj*(rr-jj+1)
    assert L*La-La*L==H
    assert H*L-L*H==2*L
    assert H*La-La*H==-2*La
    assert H*H+2*H+4*La*L==rr*(rr+2)*s.eye(d)
out('L04 finite regression','highest weights0..8: all three sl2 brackets and Casimir passed; symbolic identities L01–L03 are the general coefficient check')
L=s.Matrix([[0,0],[1,0]]); g=s.diag(1,t)
out('L05 P1 normalizer identity',s.simplify(g*L*g.inv()-t*L)==s.zeros(2))
out('L06 cohomological degree',s.expand((2*j-n)+n))
Q=s.Matrix([[0,1,1],[1,0,1],[1,1,0]]); v=s.Matrix([1,-1,-1])
out('I01 elliptic product intersection matrix',Q.tolist())
out('I02 (Delta-F1-F2)^2',(v.T*Q*v)[0])
out('I03 degree after projective-bundle selfintersection, d=+1,-1',[-2*d for d in [1,-1]])
xx,yy,xxp,yyp=s.symbols('x y xp yp')
out('A01 box-cycle degree',1-1-1+1)
out('A02 box-cycle Albanese coordinates',[s.expand(xx-xx-yy+yy),s.expand(xxp-yyp-xxp+yyp)])
out('A03 corrected transpose cohomological target degree',s.expand(2*(n-i)+1+2*i-2*n))
out('A04 wrong displayed exponent produces degree',s.expand((n-i)+1+2*i-2*n))
out('A05 transpose cycle codimension when i+j=n+1',s.expand((i+j-n).subs(j,n+1-i)))
pi0=s.diag(1,0,0,0,0,0); pi1=s.diag(0,1,1,1,1,0); pi2=s.diag(0,0,0,0,0,1)
assert sum([pi0,pi1,pi2],s.zeros(6))==s.eye(6)
assert all(p*q==(p if k==l else s.zeros(6)) for k,p in enumerate([pi0,pi1,pi2]) for l,q in enumerate([pi0,pi1,pi2]))
out('A06 curve projector cohomology test','genus2: orthogonal idempotents sum to1; general correspondence proof in proof_checks.md')
out('A07 saturation counterexample on Z/2-valued point function',{z:(2*z)%2 for z in [0,1]})
out('A08 no 2h=id on Z/2',all((2*z)%2!=1 for z in [0,1]))
out('A09 tau-squarezero formal identity','if m*w is algebraically trivial and z=m*z0, then z*w=z0*(m*w)=0')
out('S01 quintic numerical test deg(H^3)',5)
out('S02 scalar lambda H^2 homologically0 implies lambda0',s.solve(s.Eq(5*x,0),x))
q=5; affine=[(xx,yy) for xx in range(q) for yy in range(q) if (yy*yy-xx**3-xx-1)%q==0]
count=len(affine)+1; trace=q+1-count
out('F01 E/F5 affine points',affine)
out('F02 #E(F5),trace,discriminant',(count,trace,(4+27)%5))
out('F03 normalized trace square',Fraction(trace*trace,q))
out('F04 normalized trace square is not integer',Fraction(trace*trace,q).denominator!=1)
c,d=s.symbols('c d'); refl=lambda c:s.Matrix([[-1,2*c],[0,1]])
out('R01 parallel affine reflections product',refl(d)*refl(c))
out('R01b translation length',s.expand(2*d-2*c))
aa=s.symbols('a0:4'); bb=s.symbols('b0:4'); uu=s.symbols('u0:2'); vv=s.symbols('v0:2')
A=s.Matrix(2,2,aa); B=s.Matrix(2,2,bb); u=s.Matrix(uu); v=s.Matrix(vv)
def homog(A,u):
    return A.row_join(u).col_join(s.Matrix([[0,0,1]]))
assert s.simplify(homog(A,u)*homog(B,v)-homog(A*B,A*v+u))==s.zeros(3)
out('R02 homogenization composition','general symbolic affine maps in dimension2: H(A,u)H(B,v)=H(AB,Av+u); general-dimensional block proof in proof_checks.md')
def E(d,a,b):
    M=s.zeros(d);M[a,b]=1;return M
B2=[E(2,a,b) for a in range(2) for b in range(2)]
B3=[E(3,a,b) for a in range(3) for b in range(3)]
tensorbasis=[s.kronecker_product(A,B) for A in B2 for B in B3]
out('M01 End(Q2) tensor End(Q3) matrixbasis rank',s.Matrix.hstack(*[M.reshape(36,1) for M in tensorbasis]).rank())
unknowns=s.symbols('u0:36'); U=s.Matrix(6,6,unknowns)
def centralizer_dim(generators):
    eqs=[]
    for M in generators:eqs.extend(list(U*M-M*U))
    A,_=s.linear_eq_to_matrix(eqs,unknowns)
    return 36-A.rank()
out('M02 centralizer of I2 tensor M3 dimension',centralizer_dim([s.kronecker_product(s.eye(2),B) for B in B3]))
out('M03 centralizer of M2 tensor I3 dimension',centralizer_dim([s.kronecker_product(A,s.eye(3)) for A in B2]))
out('Mscope','finite split matrix examples; sheaf and arbitrary-ring assertions require the local/Morita proof, not these dimensions alone')
for rr in range(1,5):
    sep=sum((s.kronecker_product(E(rr,k,0),E(rr,0,k).T) for k in range(rr)),s.zeros(rr*rr))
    mu=sum((E(rr,k,0)*E(rr,0,k) for k in range(rr)),s.zeros(rr))
    assert mu==s.eye(rr)
    for a in range(rr):
        for b in range(rr):
            mat=E(rr,a,b)
            assert s.kronecker_product(mat,s.eye(rr))*sep==s.kronecker_product(s.eye(rr),mat.T)*sep
out('M04 matrix separability element','ranks1..4: multiplication=sum E_i1 E_1i=1 and (a tensor1)e=(1 tensor a^op)e; general matrix-unit proof in proof_checks.md')
qa,qb,qc,qd=s.symbols('qa qb qc qd',real=True)
qmat=s.Matrix([[qa+s.I*qb,qc+s.I*qd],[-qc+s.I*qd,qa-s.I*qb]])
qbar=s.Matrix([[qa-s.I*qb,-qc-s.I*qd],[qc-s.I*qd,qa+s.I*qb]])
norm=qa**2+qb**2+qc**2+qd**2
assert s.simplify(qmat*qbar-norm*s.eye(2))==s.zeros(2)
assert s.simplify(qbar*qmat-norm*s.eye(2))==s.zeros(2)
out('M05 quaternion norm identity',str(s.simplify(qmat*qbar)))
out('M05 implication','over R the norm is positive for every nonzero quaternion; H is division, whereas M2(R) has zero divisors, so H is central simple but not split')
root=Path(__file__).resolve().parents[3]
src=root/'source/SA06_texts/pro/MPL_14_002-044_transcription.tex'
if src.exists():
    scans=list(map(int,re.findall(r'\\scanpage\{(\d+)\}',src.read_text())))
    out('D01 retained scans',scans);out('D02 retained scan count',len(scans))
    out('D03 absent scans in2..44',sorted(set(range(2,45))-set(scans)))
