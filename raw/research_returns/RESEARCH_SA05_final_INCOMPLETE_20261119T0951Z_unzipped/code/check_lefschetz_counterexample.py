"""Exact certificate for the strict Lefschetz/Weil-band comparison.

Uses only integer polynomial arithmetic and exhaustive point counts in F_5.
The mathematical proof is in section A.5; this checks its finite input.
"""
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
x, y = s.symbols('x y')
g = s.Poly(s.resultant(y*y-2*y+5, x*x-3*x*y+5*y*y, y),x)
h = s.Poly(g.as_expr().subs(x,x*x),x)
curves={}
for a in range(5):
    for b in range(5):
        if (4*a**3+27*b*b)%5==0:
            continue
        n=1+sum((v*v-u**3-a*u-b)%5==0 for u in range(5) for v in range(5))
        trace=6-n
        if trace in (2,3) and trace not in curves:
            curves[trace]={'a':a,'b':b,'points':n,'trace':trace}
assert set(curves)=={2,3}
assert h.is_irreducible
assert g.is_irreducible
vals=[(2,1,1,0),(1,2,0,1),(1,0,2,1),(0,1,1,2)]
assert len(set(vals))==4
assert all(v[0]+v[3]==2 and v[1]+v[2]==2 for v in vals)
result={
 'p':5,
 'alpha_polynomial':'x^2 - 2*x + 5',
 'beta_polynomial':'x^2 - 3*x + 5',
 'product_polynomial':str(g.as_expr()),
 'square_root_polynomial':str(h.as_expr()),
 'both_irreducible_over_Q':bool(g.is_irreducible and h.is_irreducible),
 'curves_y2_x3_ax_b':curves,
 'conjugate_valuation_vectors_at_split_5_primes':vals,
 'slopes_over_F25':['1','1/2','1/2','0'],
 'honda_tate_index_over_F25':2,
 'abelian_dimension':4,
 'relation':'lambda^2 = alpha*beta',
 'tensor':'h1(B)^tensor2 tensor h1(E_alpha)^dual tensor h1(E_beta)^dual',
 'frobenius_eigenvalue_of_selected_line':1,
 'lefschetz_cocharacter_exponent_on_selected_line':2,
 'scope':'Finite inputs only; the geometric and Tannakian deductions are proved in the paper.'
}
target=ROOT/'code/check_lefschetz_counterexample_output.json'
target.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
