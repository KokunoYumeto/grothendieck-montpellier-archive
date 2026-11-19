"""Exact generic checks for the Cartier coefficient formula; no numerical periods.

Represent a regular function as A(x)+B(x)y, y^2=P(x).  Delta has pair
formula (A,B) -> (P*B'+P'/2*B,A').  Work over F_p[g2,g3,x].
The proof for all primes is in agent_elliptic.md; finite checks verify signs
and the coefficient extraction independently of the Cartier proof.
"""
import sympy as S

x,g2,g3=S.symbols('x g2 g3')
P=4*x**3-g2*x-g3

for p in (5,7,11,13,17,19):
    def red(v):
        return S.Poly(S.expand(v),x,g2,g3,modulus=p).as_expr()
    def delta(pair):
        A,B=pair
        return red(P*S.diff(B,x)+pow(2,-1,p)*S.diff(P,x)*B),red(S.diff(A,x))
    power=S.Poly(S.expand(P**((p-1)//2)),x)
    H=red(power.coeff_monomial(x**(p-1)))
    K=red(power.coeff_monomial(x**(p-2)))
    current=(x,S.Integer(0))
    for _ in range(p-1): current=delta(current)
    assert red(current[0]-H*x+K)==0 and current[1]==0
    following=delta(current)
    assert following[0]==0 and red(following[1]-H)==0
    print(f'p={p}: H_p={H}; K_p={K}')
    print('  PASS delta^(p-1)(x)=H_p*x-K_p and delta^p(x)=H_p*y')

print('Thus D_a^p=H_p*D_a-(K_p+a*H_p)*V, with V=-d/dt.')
print('All checks use generic g2,g3; smoothness is needed by the geometric proof.')
