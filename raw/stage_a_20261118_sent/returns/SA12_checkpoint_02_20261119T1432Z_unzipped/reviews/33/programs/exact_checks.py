"""Exact checks of all displayed numerical calculations in the supplied cote33 leaves.
No floating-point arithmetic; E8 simple roots reconstructed from the supplied weights.
Counterexamples are conditional on literal readings, not emendations of the ink.
"""
from itertools import product,combinations
from math import factorial,prod,gcd
import sympy as s

I=s.eye(8); e=[I.row(i) for i in range(8)]; half=s.Rational(1,2)
W8=s.Matrix.vstack(2*e[7],half*(sum(e[:7],s.zeros(1,8))+5*e[7]),half*(-e[0]+sum(e[1:7],s.zeros(1,8))+7*e[7]),sum(e[2:7],s.zeros(1,8))+5*e[7],sum(e[3:7],s.zeros(1,8))+4*e[7],sum(e[4:7],s.zeros(1,8))+3*e[7],e[5]+e[6]+2*e[7],e[6]+e[7])
C8=s.Matrix([[4,5,7,10,8,6,4,2],[5,8,10,15,12,9,6,3],[7,10,14,20,16,12,8,4],[10,15,20,30,24,18,12,6],[8,12,16,24,20,15,10,5],[6,9,12,18,15,12,8,4],[4,6,8,12,10,8,6,3],[2,3,4,6,5,4,3,2]])
A8=C8.inv()*W8
assert W8*A8.T==s.eye(8)
assert A8*A8.T==C8.inv()
R8=[]
for i,j in combinations(range(8),2):
 for a,b in product([-1,1],repeat=2): R8.append(a*e[i]+b*e[j])
for signs in product([-1,1],repeat=8):
 if prod(signs)==1: R8.append(s.Matrix([list(signs)])*half)
assert len({tuple(r) for r in R8})==240
R7=[r for r in R8 if r[6]+r[7]==0]
R6=[r for r in R7 if r[6]-r[5]==0]
W7=s.Matrix.vstack(e[7]-e[6],half*(sum(e[:6],s.zeros(1,8))-2*e[6]+2*e[7]),half*(-e[0]+sum(e[1:6],s.zeros(1,8))-3*e[6]+3*e[7]),sum(e[2:6],s.zeros(1,8))+2*(e[7]-e[6]),half*(2*sum(e[3:6],s.zeros(1,8))+3*(e[7]-e[6])),e[4]+e[5]-e[6]+e[7],e[5]+half*(e[7]-e[6]))
C7=s.Matrix([[2,2,3,4,3,2,1],[2,s.Rational(7,2),4,6,s.Rational(9,2),3,s.Rational(3,2)],[3,4,6,8,6,4,2],[4,6,8,12,9,6,3],[3,s.Rational(9,2),6,9,s.Rational(15,2),5,s.Rational(5,2)],[2,3,4,6,5,4,2],[1,s.Rational(3,2),2,3,s.Rational(5,2),2,s.Rational(3,2)]])
A7=A8[:7,:]
assert C7*A7==W7 and W7*A7.T==s.eye(7)
v=e[7]-e[6]-e[5]
W6=s.Matrix.vstack(s.Rational(2,3)*v,half*(sum(e[:5],s.zeros(1,8))+v),s.Rational(5,6)*v+half*(-e[0]+sum(e[1:5],s.zeros(1,8))),sum(e[2:5],s.zeros(1,8))+v,s.Rational(2,3)*v+e[3]+e[4],s.Rational(1,3)*v+e[4])
C6=s.Matrix([[4,3,5,6,4,2],[3,6,6,9,6,3],[5,6,10,12,8,4],[6,9,12,18,12,6],[4,6,8,12,10,5],[2,3,4,6,5,4]])/3
A6=A8[:6,:]
assert C6*A6==W6 and W6*A6.T==s.eye(6)

for rank,R,A,W,highest,exps in [(6,R6,A6,W6,half*(sum(e[:5],s.zeros(1,8))+v),[1,4,5,7,8,11]),(7,R7,A7,W7,e[7]-e[6],[1,5,7,9,11,13,17]),(8,R8,A8,W8,e[6]+e[7],[1,7,11,13,17,19,23,29])]:
 G=A*A.T
 coords=[r*A.T*G.inv() for r in R]
 assert all(all(x.q==1 for x in c) for c in coords)
 assert all(all(x>=0 for x in c) or all(x<=0 for x in c) for c in coords)
 positive=[r for r,c in zip(R,coords) if all(x>=0 for x in c)]
 rho=sum(positive,s.zeros(1,8))/2
 assert rho==sum([W.row(i) for i in range(rank)],s.zeros(1,8))
 hc=highest*A.T*G.inv()
 assert highest in R and sum(hc)==max(sum(c) for c in coords)
 # Reflection closure checked exhaustively for every root pair.
 rt={tuple(r) for r in R}
 for a in R:
  for b in R:
   reflected=b-2*(a*b.T)[0]/(a*a.T)[0]*a
   assert tuple(reflected) in rt
 nonorth=sum((highest*r.T)[0]!=0 for r in R)
 print(f'E{rank}: roots={len(R)}, rank={A.rank()}, h={len(R)//rank}, Gram determinant={G.det()}, highest height={sum(hc)}, pairings={list(highest*A.T)}, nonorthogonal={nonorth}, Weyl order={prod(m+1 for m in exps)}, exponents={exps}')
 print('  weights in supplied alpha and epsilon coordinates: all verified; rho epsilon=',list(rho),'rho alpha=',list(rho*A.T*G.inv()))
 print('  canonical root squared length=',s.Rational(1,len(R)//rank),'gamma=h²=',(len(R)//rank)**2,'all root reflections preserve root set=True')

print('E6 literal exponent equation: 51840 mod13=',51840%13)
mu=v/3
mu_coords=mu*A6.T*(A6*A6.T).inv()
print('E6 printed quotient generator mu=v/3: alpha coordinates=',list(mu_coords),'; simple-root pairings=',list(mu*A6.T))
print('E6 printed assertion 3mu in root lattice: coordinates=',list(3*mu_coords),'; integral=',all(x.q==1 for x in 3*mu_coords))
assert any(x.q!=1 for x in 3*mu_coords)
print('E6 corrected candidate omega1=2v/3: alpha coordinates=',list(2*mu_coords),'; triple integral=',all(x.q==1 for x in 6*mu_coords),'; candidate itself nonintegral=',any(x.q!=1 for x in 2*mu_coords))
print('E6 corrected-factor solutions=',[(a,12-a) for a in range(1,12) if (a+1)*(13-a)*2*6*8*12==51840])
print('E6 printed Weyl-order product=',factorial(6)*1*2*2*3*2*1*3)
bad_w7=e[5]+half*(e[5]-e[6])
print('E7 omega7 epsilon6 branch: x7+x8=',bad_w7[6]+bad_w7[7],'; dual pairings=',list(bad_w7*A7.T))
print('E8 highest root pairing alpha8=',((e[6]+e[7])*A8.row(7).T)[0])

for l in range(1,9):
 B=s.eye(l+1); simple=s.Matrix.vstack(*[B.row(i)-B.row(i+1) for i in range(l)])
 roots=[B.row(i)-B.row(j) for i in range(l+1) for j in range(l+1) if i!=j]
 hroot=B.row(0)-B.row(l)
 assert len(roots)==l*(l+1) and hroot==sum([simple.row(i) for i in range(l)],s.zeros(1,l+1))
 print(f'A{l}: roots={len(roots)}, h={l+1}, endpoint pairings={((hroot*simple.row(0).T)[0],(hroot*simple.row(l-1).T)[0])}')

u=s.Matrix([1,-1]);v2=s.Matrix([0,1]);su=s.eye(2)-2*u*u.T/(u.T*u)[0];sv=s.eye(2)-2*v2*v2.T/(v2.T*v2)[0]
g=su*sv
assert g**4==s.eye(2) and g**2!=s.eye(2)
print('B2 ordered pair: n(u,v)=',2*(u.T*v2)[0]/(u.T*u)[0],'; n(v,u)=',2*(v2.T*u)[0]/(v2.T*v2)[0],'; length ratio²=',(v2.T*v2)[0]/(u.T*u)[0],'; reflection product=',g.tolist(),'; order4')
print('Coxeter lower-bound sums: valency4=',4*s.Rational(1,4),'; labels3,3,4=',s.Rational(1,4)+s.Rational(1,4)+s.Rational(1,2),'; labels3,6=',s.Rational(1,4)+s.Rational(3,4),'; labels4,4=',2*s.Rational(1,2))
# Order3 contraction: identifying coordinates i,j in a Gram form with diagonal1 and qij=−1/2 gives new diagonal1.
print('Coxeter order3 contraction diagonal=',1+1+2*(-s.Rational(1,2)))
for n in (4,8,12):
 D=s.zeros(n)
 for j in range(n-1): D[j,j]=1;D[j,j+1]=-1
 D[n-1,n-2]=D[n-1,n-1]=1
 halfsum=s.ones(1,n)/2
 print(f'D_{n}: determinant={abs(D.det())}, halfsum norm={n}/4, halfsum coordinates on D basis=',list(halfsum*D.inv()),'; index[Dplus:D]=2; covolume1; integral Gram=True')
 assert all((D.row(i)*halfsum.T)[0].q==1 for i in range(n)) and (halfsum*halfsum.T)[0].q==1

# Sierpinski-space endomorphisms over F2: a compatible global 2x2 matrix has lower-left0 and lower-right b.
endomorphisms=[]
for a,c,b in product(range(2),repeat=3): endomorphisms.append((a,c,0,b))
diagonal=[m for m in endomorphisms if m[1]==0]
print('Product-of-stalks Sierpinski F2: sheaf endomorphisms=',len(endomorphisms),'; diagonal stalk families=',len(diagonal),'; witness [[0,1],[0,0]], restriction second coordinate gives0; extraction yields [[1,0],[0,0]].')
assert len(endomorphisms)==8 and len(diagonal)==4
print('Finite étale trace F3²→F3 kernel=',[(a,b) for a,b in product(range(3),repeat=2) if (a+b)%3==0])
print('Rank1 Z/4 local system monodromy−1: invariants=',[x for x in range(4) if (-x)%4==x],'; size2 is not4^r, hence not free Z/4.')
for n in (4,5,6):
 primitive=[a for a in range(n) if gcd(a,n)==1]
 print(f'Primitive roots scaling modulo{n}: units={primitive}; λ0 is not a generator')
print('Twist direction test n5,d1,λ2: old ζ→1; new generator2ζ→1 sends ζ→3; λ^(−1)=3, not λ=2.')
print('Filtration example A=k[t], R=(t), N0=A,Nk=0(k≥1): N′k=(t^k), R′k=(t^max(1,k)), R″k=(t^(k+1)); at k1 strict quotient dimension1.')
T=s.Symbol('T');degrees=[2,3,5]
series=s.series(prod(1/(1-T**d) for d in degrees),T,0,13).removeO().expand()
counts=[sum(1 for a in range(7) for b in range(5) for c in range(3) if 2*a+3*b+5*c==m) for m in range(13)]
assert counts==[series.coeff(T,m) for m in range(13)]
print('Weighted polynomial Hilbert-series certificate degrees2,3,5 coefficients0..12=',counts)
print('General symbolic argument: independent monomials of weighted degree m are counted by the product of geometric series; degree multiset recovered from graded indecomposables S+/(S+)².')
print('Relative duality degree reversal: j=2d−i sends i≤i0 to j≥2d−i0 exactly.')
print('Partial-range counterexample degree bookkeeping: d=1,i0=1, lower f! degrees0,1 vanish; proposed ordinary range begins2d−i0=',2*1-1,'; actual R1f* is nonconstant skyscraper. This uses geometric inputs checked in review.md, not a numerical proof of them.')
t,u=s.symbols('t u');xx=s.Matrix(s.symbols('x1 x2'));yy=s.Matrix(s.symbols('y1 y2'))
cc=s.symbols('c0:8')
def bilinear(a,b): return s.Matrix([sum(cc[4*k+2*i+j]*a[i]*b[j] for i in range(2) for j in range(2)) for k in range(2)])
def trunc(v):
 return s.Matrix([sum(coef*t**ij[0]*u**ij[1] for ij,coef in s.Poly(s.expand(w),t,u).terms() if sum(ij)<=2) for w in v])
def law(a,b): return trunc(a+b+bilinear(a,b))
invx=-t*xx+t*t*bilinear(xx,xx);invy=-u*yy+u*u*bilinear(yy,yy)
comm=law(law(law(t*xx,u*yy),invx),invy)
assert comm==trunc(t*u*(bilinear(xx,yy)-bilinear(yy,xx)))
print('Formal-group quadratic calculation: for arbitrary bilinear2-dimensional B, coefficienttu in m(m(m(tx,uy),inv(tx)),inv(uy)) is B(x,y)−B(y,x); all degree≤2 coefficients verified symbolically. Jacobi is not proved by this degree2 check.')
print('ALL EXACT ASSERTIONS PASSED; identified literal discrepancies retained for scan collation.')
