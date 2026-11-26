"""(i) Arithmetic identities and inequalities used in Section 6 of P5 (run's P-F56/P-F57 constants).
a0805369bae2ebddc (Claude Opus 5.5 at effort high), 25 Nov 2026."""
import sympy as sp
from math import comb
n=sp.symbols('n')
C=lambda a,b: sp.binomial(a,b)
B=C(n-3,2)-1
e1=sp.expand(sp.expand_func(3*B-C(n-2,3)+(n-4)+(n-2)**2))
e2=sp.expand(sp.expand_func(C(n-2,3)-(n-4)-2*B-C(n-1,2)))
ok1 = sp.simplify(e1-(-n**3/6+4*n**2-sp.Rational(107,6)*n+19))==0
ok2 = sp.simplify(e2-(n**3/6-3*n**2+sp.Rational(71,6)*n-11))==0
# (P-F57f8): first four terms <= n^3/6 + 4n^2 for n>=5
l=n-1
e3=sp.expand(sp.expand_func(C(n,3)+sp.Rational(3,2)*l*(l+1)+3*l+2*n**2))
ok3 = all(e3.subs(n,k) <= sp.Rational(k**3,6)+4*k**2 for k in range(5,2000))
# increment count and S_n count
ok4 = all(1+(comb(k-2,2)-1)+(k-3)+1==comb(k-1,2) for k in range(5,200))
ok5 = all((k-1)+comb(k,3)-(k-2)-1==comb(k,3) for k in range(4,200))
# delta_n <= 2^{-n^3/12} for n >= 48
ok6 = all(-k**3/6+4*k**2-107*k/6+19 <= -k**3/12 for k in range(48,5000))
# Q_n start bound
ok7 = all(k-1+(k-3)*comb(k,3)+2*k**3 <= k**4 for k in range(4,2000))
line=f"(i) Section 6 constants: delta-poly {ok1}, I_n(b_n)-poly {ok2}, f8 bound {ok3}, increment count {ok4}, |S_n| {ok5}, delta_n<=2^(-n^3/12) n>=48 {ok6}, Q_n<=2^(n^4) {ok7}"
print(line); open('p5_checks_output.txt','a',encoding='utf-8').write(line+'\n')
