"""Exact rational certificate for the formal square-mollifier kernel.

This verifies only algebra, polynomial domination and beta integration.
The analytic asymptotic linking the kernel to zeta-zero moments must
be separately proved and reviewed.  No host timestamp is recorded.
"""
from pathlib import Path
from fractions import Fraction
import json
import sympy as s

a,b,c=s.symbols("a b c")
l=s.symbols("l1:5");r=s.symbols("r1:5")
variables=s.symbols("u1 u2 v1 v2")
def trunc(f,degree):
    pp=s.Poly(s.expand(f),a,b,c)
    return sum(co*a**mon[0]*b**mon[1]*c**mon[2]
               for mon,co in pp.terms() if sum(mon)<=degree)
def EL(x):return 1+sum(l[k-1]*x**k for k in range(1,5))
def ER(x):return 1+sum(r[k-1]*x**k for k in range(1,5))
def ex(x):return sum(x**k/s.factorial(k) for k in range(5))
numerator=trunc(b*(a-c)*EL(b)*ER(a)*ER(c)
          -a*(b+c)*ex(-a-b)*EL(-a)*ER(-b)*ER(c)
          +c*(a+b)*ex(-b-c)*EL(-c)*ER(a)*ER(-b),6)
quotient,remainder=s.div(numerator,(a+b)*(b+c)*(a-c),a,b,c)
assert remainder==0
ii=s.expand(quotient).coeff(a,1).coeff(b,1).coeff(c,1)
jj,remainder=s.div(trunc(EL(b)*ER(a)-ex(-a-b)*EL(-a)*ER(-b),3),
                  a+b,a,b,c)
assert remainder==0
jj=s.expand(jj).coeff(a,1).coeff(b,1)
substitutions={}
for k in range(1,5):
    substitutions[l[k-1]]=sum(
        s.binomial(s.Rational(1,2),j)*s.binomial(s.Rational(1,2),k-j)*
        variables[0]**j*variables[1]**(k-j) for j in range(k+1))
    substitutions[r[k-1]]=sum(
        s.binomial(s.Rational(1,2),j)*s.binomial(s.Rational(1,2),k-j)*
        variables[2]**j*variables[3]**(k-j) for j in range(k+1))
poly=s.Poly(s.expand((jj+2*ii).subs(substitutions)),*variables)
z=s.symbols("S");d,e=s.symbols("D E")
rem=s.symbols("x1 x2 y1 y2")
nu=s.Rational(1,4)
q=0
for mon,co in poly.terms():
    term=co*nu**(sum(mon)-1)
    for x,k in zip(rem,mon):
        cc=s.simplify(2*s.sqrt(s.pi)/s.gamma(s.Rational(3,2)+k))
        term*=cc*x**k*(1-x/(s.Rational(3,2)+k))
    q+=term
dd,ee=s.symbols("d e")
raw=s.Poly(s.expand(q.subs({
    rem[0]:(z+dd)/2,rem[1]:(z-dd)/2,
    rem[2]:(z+ee)/2,rem[3]:(z-ee)/2})),dd,ee)
assert all(i%2==j%2==0 for (i,j),co in raw.terms())
q=s.Poly(sum(co*d**(i//2)*e**(j//2)
             for (i,j),co in raw.terms()),d,e)
q0=q.coeff_monomial(1);cd=q.coeff_monomial(d)
cc=2-s.Rational(3,4)*z
aa=-(q.coeff_monomial(d*d)+q.coeff_monomial(d**3)*d)
bb=s.cancel((q0+cd*d-q.as_expr())/e).subs(e,0) if False else \
   -cc-s.cancel((q.as_expr()-q.as_expr().subs(e,0))/e)
assert s.expand(q0+cd*d-cc*e-q.as_expr()-d*d*aa-e*bb)==0

def bernstein(poly,variables):
    pp=s.Poly(s.expand(poly),*variables)
    degrees=pp.degree_list()
    coeff={}
    from itertools import product
    for kk in product(*(range(n+1) for n in degrees)):
        v=0
        for jj,cj in pp.terms():
            if all(j<=k for j,k in zip(jj,kk)):
                v+=cj*s.prod(s.binomial(k,j)/s.binomial(n,j)
                            for n,k,j in zip(degrees,kk,jj))
        coeff[kk]=v
    return coeff

u,v,w=s.symbols("u v w")
cert=[]
for half in (0,1):
    ZZ=u if half==0 else 2-u
    for name,expr in (
        ("A",aa.subs({z:ZZ,d:u*u*v}, simultaneous=True)),
        ("B",bb.subs({z:ZZ,d:u*u*v,e:u*u*w}, simultaneous=True))
    ):
        passed=False
        for pieces in (1,2,4,8,16,32):
            lo=None
            for j in range(pieces):
                p=expr.subs(u,(j+u)/pieces)
                cs=bernstein(p,(u,v,w))
                mm=min(cs.values())
                lo=mm if lo is None else min(lo,mm)
                if mm<0:break
            if lo is not None and lo>=0 and j==pieces-1:
                cert.append((half,name,pieces,str(lo)))
                passed=True;break
        assert passed,(half,name,"Bernstein positivity not certified")

# Nonnegativity of the row-only upper bound after dropping column cuts.
# Here D <= min(S,2-S)^2 and E <= (2-S)^2.
for half in (0,1):
    ZZ=u if half==0 else 2-u
    expr=(q0+cd*(z if half==0 else 2-z)**2-cc*(2-z)**2).subs(z,ZZ)
    for pieces in (1,2,4,8,16,32):
        lows=[min(bernstein(expr.subs(u,(j+u)/pieces),(u,)).values())
              for j in range(pieces)]
        if min(lows)>=0:
            cert.append((half,"row-upper-nonnegative",pieces,str(min(lows))))
            break
    else:raise AssertionError("row upper nonnegativity not certified")
assert max(bernstein(cd.subs(z,2*u),(u,)).values())<0

r,t=s.symbols("r t")
integrand=(z*(q0+cd*(r-t)**2-cc*s.Rational(2,3)*(r*r+t*t))/2).subs(z,2-r-t)
ip=s.Poly(s.expand(integrand),r,t)
upper=sum(co*s.rf(s.Rational(1,2),i)/s.rf(2,i)*
          s.rf(s.Rational(1,2),j)/s.rf(2,j)
          for (i,j),co in ip.terms())/4
first=s.Rational(1543,2304)
assert upper==s.Rational(1505515846753,536481792000)
pi_lower=s.Rational(314159,100000)
machin_lower=16*sum((-1)**j*s.Rational(1,(2*j+1)*5**(2*j+1))
                   for j in range(4))-s.Rational(4,239)
assert machin_lower>pi_lower
assert upper/pi_lower<2*first*first
a_star=first-s.Rational(1,2000)
b_star=upper/pi_lower+s.Rational(1,2000)
p_eta=s.Rational(1,2)/(1-s.Rational(1,2500))
assert 0<a_star<1 and 0<b_star<1
assert a_star*a_star-b_star*p_eta>s.Rational(1,2000)
sign_fraction=s.Rational(1,2500)*s.Rational(1,4000)**2/(4*81)
assert sign_fraction>s.Rational(1,10**14)
result={
 "scope":"exact formal-kernel certificate only; analytic moment theorem separately required",
 "first_constant":str(first),
 "second_upper_numerator_over_pi":str(upper),
 "pi_lower":str(pi_lower),
 "strict_gap_using_pi_lower":str(2*first*first-upper/pi_lower),
 "machin_pi_lower":str(machin_lower),
 "a_star":str(a_star),"b_star":str(b_star),
 "phase_margin":str(a_star*a_star-b_star*p_eta),
 "sign_fraction_rational":str(sign_fraction),
 "bernstein_certificates":cert,
 "formal_kernel_monomials":len(poly.terms()),
 "status":"PASS"
}
Path(__file__).with_name("square_mollifier_kernel_certificate.json").write_text(
    json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
