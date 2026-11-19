"""Exact certificates for RESEARCH_SA07, GEN-3 and GEN-4.

Python 3 / SymPy; exact arithmetic only. This program verifies the finite
algebra in the examples. Zariski-density proofs are in agent_generation.md.
"""

from time import perf_counter
import sympy as s

start = perf_counter()
r = s.sqrt(2)
g = 1+r
ratio = s.simplify(g/(1-r))
print('GEN-3: F=Q, G=G_m, g=1+sqrt(2)')
print('Conjugates:', (1+r, 1-r))
print('Image of sigma(g)^(-1)g:', (s.Integer(1), ratio))
print('Nonidentity ratio = -3-2sqrt(2):', s.simplify(ratio+3+2*r) == 0)
print('Product of conjugates = -1:', s.expand((1+r)*(1-r)) == -1)
print('|ratio|>1:', bool(3+2*r > 1))
t = s.symbols('t')
phi_sigma = t/(t+1)
phi_tau = t/(t+2)
phi_tausigma = t/(t+3)
semilinear_product = phi_sigma.subs(t,t+2)*phi_tau
ordinary_product = phi_sigma*phi_tau
print('GEN-4: G=G_m, g=t, sigma(t)=t+1, tau(t)=t+2')
print('Right cocycle residual:', s.factor(semilinear_product-phi_tausigma))
print('Ordinary homomorphism residual:', s.factor(ordinary_product-phi_tausigma))
print('Exact arithmetic: no numerical precision parameter.')
print('Wall time seconds:', round(perf_counter()-start,6))
