import sympy as S
s,g=S.symbols('s g')
h=(12*g+8)*(g-1)/(g*g-g-1)
n=12*(g-1)*(3*g*g-4*g-4)/(g*(3*g*g-12*g+15))
R=12*s*s/(s*s-s-1)
P=(s*s-s-1)*(5*g*g-15*g+4)-(s+1)*g*(3*g*g-12*g+15)
checks={
'h_derivative':S.diff(h,g)+4*(2*g*g+2*g+1)/(g*g-g-1)**2,
'n_derivative':S.diff(n,g)+4*(5*g*g*((g-3)**2-2)+4*(g-1)*(3*g-5))/(g**3-4*g*g+5*g)**2,
'n_minus_h':n-h-4*(g-1)*(3*g+2)*(g*g-4*g+2)/(g*(g*g-4*g+5)*(g*g-g-1)),
'n_minus_R':n-R-12*P/((s*s-s-1)*g*(3*g*g-12*g+15)),
'P_four':P.subs(g,2*s+1)+2*s*(2*s**3+21*s*s+2*s-5),
'P_two':P.subs(g,s+1)-s*(2*s**3-10*s*s-3*s+5),
'P_three':P.subs(g,1+S.Rational(3,2)*s)-3*s*(3*s**3-59*s*s-8*s+20)/8,
'h_row_one':h.subs(g,1+s/2)-R-4*s*(s*s-s-10)/((s*s-s-1)*(s*s+2*s-4)),
'h_row_two':h.subs(g,s+1)-R+4*s*(s*s+5*s+5)/((s*s-s-1)*(s*s+s-1))
}
print({k:str(S.factor(v)) for k,v in checks.items()})
