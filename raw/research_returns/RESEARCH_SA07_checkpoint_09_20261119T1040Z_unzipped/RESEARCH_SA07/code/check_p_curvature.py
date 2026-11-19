"""Exact p-th-power calculation on the universal vector extension chart.
The coordinate is t = zeta(u)-s, so D_a(t)=-x-a.
All arithmetic is rational or in a polynomial ring over a finite field.
"""
import sympy as S
x,y,t,g2,g3,a=S.symbols('x y t g2 g3 a')
f=4*x**3-g2*x-g3

def red(expr,p=None):
    expr=S.rem(S.Poly(S.expand(expr),y),S.Poly(y*y-f,y)).as_expr()
    if p:
        expr=S.Poly(expr,x,y,t,g2,g3,a,domain=S.QQ).clear_denoms()[1] if False else expr
        poly=S.Poly(expr,x,y,t,g2,g3,a,domain=S.QQ)
        out=0
        for powers,c in poly.terms():
            num,den=c.as_numer_denom()
            coeff=(int(num)*pow(int(den),-1,p))%p
            mon=1
            for var,e in zip((x,y,t,g2,g3,a),powers): mon*=var**e
            out+=coeff*mon
        expr=S.expand(out)
    return expr

def D(expr,p=None):
    return red(y*S.diff(expr,x)+(6*x*x-g2/S.Integer(2))*S.diff(expr,y)-(x+a)*S.diff(expr,t),p)

print('General characteristic 5 identity: D_a^5 = 2*g2*D_a + (3*g3-2*g2*a)*(-d/dt).')
for var in (x,y,t):
    lhs=var
    for _ in range(5): lhs=D(lhs,5)
    rhs=2*g2*D(var,5)-(3*g3-2*g2*a)*S.diff(var,t)
    assert red(lhs-rhs,5)==0,(var,lhs,rhs)
    print(var, '=', lhs)
print('PASS general p=5 vector-field identity')
print('CM model g2=30, g3=28, h=1/2 at p=5:')
assert (30**3-27*28**2)%5!=0
coef=red(3*g3-2*g2*a,5).subs({g2:30,g3:28,a:S.Rational(1,2)})
assert int(coef)%5==4
print('D_h^5 = 4*(-d/dt); horizontal coefficient vanishes, vertical coefficient is 4.')
print('PASS explicit good-reduction failure of restricted-Lie stability')

# Independent finite-field calculation for several primes on the fixed CM curve.
def red_fixed(expr,p,G2,G3):
    ff=4*x**3-G2*x-G3
    r=S.rem(S.Poly(S.expand(expr),y),S.Poly(y*y-ff,y)).as_expr()
    return S.Poly(r,x,y,modulus=p).as_expr()
def DE(expr,p,G2,G3):
    return red_fixed(y*S.diff(expr,x)+(6*x*x-G2*pow(2,-1,p))*S.diff(expr,y),p,G2,G3)
print('CM fixed model: p, H_p, C_p, C_p-H_p/2 (all in F_p)')
for p in (5,7,11,13,17,19,23,29,31,41):
    xx=x
    for _ in range(p-1): xx=DE(xx,p,30,28)
    poly=S.Poly(xx,x,y,modulus=p)
    H=int(poly.coeff_monomial(x))%p
    C=int(poly.coeff_monomial(1))%p
    assert red_fixed(xx-H*x-C,p,30,28)==0
    H_expected=int(S.Poly((4*x**3-30*x-28)**((p-1)//2),x,modulus=p).coeff_monomial(x**(p-1)))%p
    assert H==H_expected
    print(p,H,C,(C-H*pow(2,-1,p))%p)
print('PASS all finite-field derivation and Hasse-coefficient checks')
