"""Exact independent arithmetic checks of cote 138, scans104–112,127,129–132.
Python3 + SymPy.  No numerical approximation is used as a certificate.
"""
from pathlib import Path
import json
import sympy as s
W=Path(__file__).resolve().parents[1]
z,c,t,x,y=s.symbols('z c t x y',real=True)
H=z**3*(z-1)**2*(z-c); g=z**2-(5*c+4)*z/6+c/2
delta=25*c*c-32*c+16; R=25*c**3-12*c**2-24*c-16
rem=s.rem(H,g,z); P=s.factor(rem.coeff(z)); Q=s.factor(rem.subs(z,0))
assert s.expand(s.diff(H,z)-6*z**2*(z-1)*g)==0
assert s.factor(P+delta*R/7776)==0
assert s.factor(Q-c*(5*c-8)*(25*c**3-6*c*c+8)/2592)==0
BezP,BezQ,gcd=s.gcdex(P,Q,c)
assert s.expand(BezP*P+BezQ*Q)==1
B=z*z+(2*c-2)*z/3+(5*c*c-4*c-4)/12
T=s.cancel((H-Q-g*g*B)/R)
assert s.denom(T)==1 or not s.denom(T).has(c)
assert s.rem(s.together(H-Q-g*g*B),R,c)==0
ct=(4+18*t+6*t*t)/25; tc=-25*c*c/36+31*c/18+s.Rational(2,9)
assert s.rem(s.together(R.subs(c,ct)),t**3-2,t)==0
assert s.rem(s.together(tc**3-2),R,c)==0
assert s.rem(s.together(tc.subs(c,ct)-t),t**3-2,t)==0
mod7=[int(R.subs(c,i))%7 for i in range(7)];assert 0 not in mod7
rootsdelta=[s.Rational(16,25)+sgn*s.Rational(12,25)*s.I for sgn in[-1,1]]
deg=[]
for cc in rootsdelta:
 uu=s.simplify((5*cc+4)/12); f=s.cancel((H/Q).subs(c,cc))
 deg.append({'c':str(cc),'u':str(uu),'f(u)':str(s.simplify(f.subs(z,uu))),'first_derivative':str(s.simplify(s.diff(f,z).subs(z,uu))),'second_derivative':str(s.simplify(s.diff(f,z,2).subs(z,uu))),'third_derivative':str(s.simplify(s.diff(f,z,3).subs(z,uu)))})
 assert s.simplify(f.subs(z,uu)-1)==0 and s.simplify(s.diff(f,z,2).subs(z,uu))==0 and s.simplify(s.diff(f,z,3).subs(z,uu))!=0
small=[z,z*z,-4*z*(z-1),z*z/(4*(z-1)),z**3,s.Rational(4,27)*z**3/(z-1),s.Rational(27,4)*z*(z-1)**2]
smallcert=[]
for f in small:
 smallcert.append({'f':str(f),'numerator':str(s.factor(s.fraction(s.cancel(f))[0])),'denominator':str(s.factor(s.fraction(s.cancel(f))[1])),'f_minus_one':str(s.factor(f-1)),'derivative':str(s.factor(s.diff(f,z)))})
f=small[-2];imag=s.factor(s.im(s.expand_complex(f.subs(z,x+s.I*y))))
expected=4*y*(2*x*(x*x+y*y)-3*x*x+y*y)/(27*((x-1)**2+y*y));assert s.simplify(imag-expected)==0
mc=z/(c*z+1-c);mcsq=s.factor(mc.subs(z,mc)-z)
assert s.factor(mcsq+z*(z-1)*c*(2-c)/((2*c-c*c)*z+(1-c)**2))==0
loop=z**4/(4*(z*z-1))
fold=(2*z**3-1)**2; clean=4*z**3*(1-z**3)
assert s.factor(fold-1)==4*z**3*(z-1)*(z*z+z+1)
# General orange formula via t=z^n: exact fibre and derivative formulas.
orange=4*t/(1+t)**2
assert s.factor(orange-1)==-(t-1)**2/(t+1)**2
assert s.simplify(s.diff(orange,t)-4*(1-t)/(1+t)**3)==0
# Intermediate remainder signs at scan108.
a=(5*c+4)/6;b=-c/2;A=(a-2)*(a-c)+b+1;D=(a-2)*b-(b+1)*c
Pr=s.expand((a**3+2*a*b)*A+(a*a+b)*D);Qr=s.expand(b*(a*a+b)*A+a*b*D)
assert s.simplify(P-Pr)==0 and s.simplify(Q-Qr)==0
out={
 'derivative_H':str(s.factor(s.diff(H,z))), 'g':str(g),'P':str(P),'Q':str(Q),
 'P_at_0':str(P.subs(c,0)),'P_at_1':str(P.subs(c,1)),
 'gcd_P_Q':str(gcd),'bezout_coeff_P':str(BezP),'bezout_coeff_Q':str(BezQ),
 'delta_roots':[str(a) for a in rootsdelta],'wrong_written_root_substitution':str(s.expand(delta.subs(c,s.Rational(16,25)+s.Rational(24,25)*s.I))),
 'res_R_delta':str(s.resultant(R,delta,c)),'res_R_Q':str(s.resultant(R,Q,c)),
 'B':str(B),'H_minus_Q_minus_g2B_div_R':str(T),
 'res_R_discB':str(s.resultant(R,s.discriminant(B,z),c)),
 'res_R_resBg':str(s.resultant(R,s.resultant(B,g,z),c)),
 'R_discriminant':str(s.discriminant(R,c)),'R_mod7_values':mod7,
 'c_from_t':str(ct),'t_from_c':str(tc),'field_identities':'All three exact reductions are zero modulo t^3−2 or R.',
 'degenerate_fibres':deg,'c_8_over_5':{'P':str(P.subs(c,s.Rational(8,5))),'Q':str(Q.subs(c,s.Rational(8,5))),'delta':str(delta.subs(c,s.Rational(8,5)))},
 'seven_small_maps':smallcert,'inverse_real_axis_imaginary_part':str(imag),
 'mobius_square_minus_identity':str(mcsq),'mobius_fixed_points_c2':str(s.solve(s.together(mc.subs(c,2)-z),z)),
 'two_loop_map':{'f':str(loop),'f_minus_one':str(s.factor(loop-1)),'derivative':str(s.factor(s.diff(loop,z))),'passport':[[4],[2,2],[2,1,1]]},
 'folded_cubic_minus_one':str(s.factor(fold-1)),'cleaned_cubic_minus_one':str(s.factor(clean-1)),
 'orange':{'t_equals':'z^n, n positive integer','F':str(orange),'F_minus_one':str(s.factor(orange-1)),'dF_dt':str(s.factor(s.diff(orange,t))),'passport':[['n','n'],['2 repeated n times'],['2 repeated n times']]},
 'alpha_beta_remainder_check':{'A':str(s.factor(A)),'D':str(s.factor(D)),'P_check':str(s.simplify(P-Pr)),'Q_check':str(s.simplify(Q-Qr))},
 'status':'All asserted exact identities passed.'}
(W/'outputs/exact_arithmetic.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(out,indent=2,ensure_ascii=False))
