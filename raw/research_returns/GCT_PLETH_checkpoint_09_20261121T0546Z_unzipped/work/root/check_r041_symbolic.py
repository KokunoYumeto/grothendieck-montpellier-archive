from pathlib import Path
import sympy as s
m,a,n=s.symbols('m a n',integer=True,positive=True)
k=m+1;l=a-k
UI=s.Matrix([[1,1,0]]);TI2=s.Matrix([[-1,1,2]])
UA=s.Matrix([[l+1,1,0]]);TA2=s.Matrix([[l-1,1,2]])
AA=UA-TA2/a
BB=UI-2*TI2/a+k*TA2/a**2
CC=(TI2-UI)/2-(k-1)*TI2/a+k*(k-1)*TA2/(2*a**2)
P1=AA/a;P2=(BB-P1)/a;P3=(CC+P1)/a
C=s.simplify(s.Matrix.vstack(P1,P2,P3))
expected=s.Matrix([[(a*a-a*m-a+m+2)/a**2,(a-1)/a**2,-2/a**2],[(m+2)*(2*a-m-2)/a**3,(a*a-3*a+m+2)/a**3,-2*(2*a-m-2)/a**3],[(m-1)*(m+2)*(a-m-2)/(2*a**3),-(m-1)*(2*a-m-2)/(2*a**3),(a*a-2*a*m+m*m+m-2)/a**3]])
assert s.simplify(C-expected)==s.zeros(3)
assert s.factor(C.det()-(a-m-2)*(a-m-1)**2/a**5)==0
assert s.factor(C.subs(a,m+2)[:2,:2].det()-(m-1)/(m+2)**3)==0
u=n*(n-1)/((n-2)*(n-3));v=n*(n-1)/(n-2)**2
D=s.Matrix([[1,0,0],[(m+2)*u,-6*u,0],[0,0,-4*v]])
assert s.factor(D.det()-24*u*v)==0
rel1=s.Matrix([1,m/(m+1),(1-m)/(2*(m+1))]);rel2=s.Matrix([[1,0],[0,1],[s.Rational(1,2),-1]])
M=C*D
value=(M.subs({a:m+1,n:m+1})*rel1)[0]
assert s.factor(value-(m-2)/(m-1))==0
value=(M.subs({a:m+2,n:m+2})*rel2)[:2,:].det()
assert s.factor(value+2*(m+1)*(3*m+2)/(m**3*(m+2)))==0
value=(M.subs({a:m+1,n:m+2})*rel2)[0,1]
assert s.factor(value+2*(m+2)**2*(3*m-2)/(m*m*(m-1)*(m+1)))==0
Path('work/root/R041_SYMBOLIC_MATRIX_CHECK.txt').write_text('All nine matrix entries reconstructed symbolically from the independent-row expectation table. Full determinant, finite-row rank-two minor, split-form determinant and all three endpoint reductions agree as exact rational identities in a,n,m. PASS.\n')
print('R041 all symbolic matrix entries, determinants and endpoints PASS')
