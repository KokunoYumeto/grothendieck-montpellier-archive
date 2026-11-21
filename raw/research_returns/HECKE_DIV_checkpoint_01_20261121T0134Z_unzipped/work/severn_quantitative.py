"""Exact small arithmetic in the quantitative Severn supplier argument.

The enormous final bound is retained as an explicit integer expression.  This
script verifies the nine-eigenvalue Weil projector, not the geometric proof.
"""
import json
from pathlib import Path
import sympy as s

w,x=s.symbols('w x')
def red(a):
    return s.rem(s.Poly(s.expand(a),w,domain=s.QQ),s.Poly(w*w+w+1,w,domain=s.QQ)).as_expr()
def redx(a):
    p=s.Poly(a,x)
    return s.expand(sum(red(v)*x**i[0] for i,v in p.terms()))

G=39191040
genus=1+G*(-2+20*(s.Rational(1,2)))/2
assert genus==156764161
alpha,alpha_bar=3+w,2-w
assert red(alpha*alpha_bar)==7
eigenvalues=[red(alpha**(8-j)*alpha_bar**j) for j in range(9)]
assert len(set(map(str,eigenvalues)))==9
inner=s.Integer(1)
for z in eigenvalues[1:8]:inner=redx(inner*(x-z))
outer=redx((x-eigenvalues[0])*(x-eigenvalues[8]))
assert not inner.has(w) and not outer.has(w)
P=s.Poly(inner*s.invert(inner,outer,x),x,domain=s.QQ)
den=int(s.ilcm(*[c.q for c in P.all_coeffs()]))
Q=s.Poly(den*P.as_expr(),x,domain=s.ZZ)
coeff=[int(Q.nth(j)) for j in range(9)]
assert all(red(Q.as_expr().subs(x,eigenvalues[j]))==(den if j in (0,8) else 0) for j in range(9))
mass=sum(abs(coeff[j])*7**(4*j) for j in range(9))

result={
 'group_order':G,
 'branch_terms':20,
 'branch_orders':[2]*20,
 'cover_genus':int(genus),
 'common_idempotent_denominator':G,
 'source_polarization_product_bound':'G^8',
 'alpha':'3+w',
 'alpha_norm':7,
 'H8_eigenvalues':[str(z) for z in eigenvalues],
 'inner_factor':str(inner),
 'outer_factor':str(outer),
 'Weil_projector_denominator':den,
 'Weil_projector_numerator_coefficients_ascending':coeff,
 'Weil_projector_degree_mass_multiplier':mass,
 'all_nine_projector_values_checked':True,
 'integer_expressions':{
  'g':'4*G+1',
  'R':'(2*G+1)*factorial(G)*G^G',
  'L':'2*g*R',
  'S0':'G^(2*g)*factorial(g)^2',
  'SB':'factorial(L/2)*S0^R',
  'k':'L/2+4',
  'B0':'(40*G)^k*binomial(k,4)*SB*factorial(8)*G^8',
  'N':'4*G^8*Delta_target',
  'B':'N^8*Weil_projector_degree_mass_multiplier*B0',
  'C':'B^4*(q_t+4*T+4)',
  'T':'integral intersection square of q_t*t',
 },
 'scope':'Small arithmetic verified; the geometric derivation is in severn_quantitative.md and requires its stated manuscript and classical inputs.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
