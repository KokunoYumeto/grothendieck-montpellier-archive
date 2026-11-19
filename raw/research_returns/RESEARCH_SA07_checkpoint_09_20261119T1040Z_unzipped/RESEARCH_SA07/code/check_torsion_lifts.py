"""Exact three-torsion lift on the non-CM curve y^2=4x^3-4x-1."""
import sympy as S
x,y,t=S.symbols('x y t')
f=4*x**3-4*x-1
psi=3*x**4-6*x**2-3*x-1
# The duplication slope in short Weierstrass coordinates is m=(3x^2-1)/y.
assert S.expand((3*x**2-1)**2-3*x*f)==-psi
assert S.resultant(f,psi,x)!=0
# Thus x(2P)=m^2-2x=x and y(2P)=-y at psi=0, so 3P=O.
# The compact fiber is t=-m/3. Therefore x=3t^2.
fiber_polynomial=S.expand(psi.subs(x,3*t**2))
assert fiber_polynomial==243*t**8-54*t**4-9*t**2-1
print('PASS duplication identity: m^2=3x at the three-division polynomial.')
print('resultant(y^2 equation at y=0, three-division polynomial)=',S.resultant(f,psi,x))
print('PASS point has exact order 3 and nonzero y.')
print('Compact lift fiber t=-(3*x^2-1)/(3*y) satisfies',fiber_polynomial,'=0.')
r=[v for v in S.nroots(psi,maxsteps=100) if abs(S.im(v))<S.Rational(1,10)**10 and 1<float(S.re(v))<2][0]
s=S.sqrt(f.subs(x,r))
tval=-(3*r*r-1)/(3*s)
print('For the unique root 1<x<2, (x,y,t) approximately:',r.evalf(16),s.evalf(16),tval.evalf(16))
print('Discriminant=37; j=110592/37 is nonintegral, hence curve is non-CM.')
