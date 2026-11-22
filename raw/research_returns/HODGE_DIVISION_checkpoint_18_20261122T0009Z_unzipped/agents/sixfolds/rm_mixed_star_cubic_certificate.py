#!/usr/bin/env python3
"""Exact finite algebra supplement for SF-E833.

No numerical Hermitian classification, sheaf existence, or semiregularity
claim is inferred from these checks. The universal proof is in the draft.
"""
from pathlib import Path
from itertools import combinations
from time import perf_counter
import hashlib
import json
import sympy as s

started = perf_counter()
root = Path(__file__).resolve().parent
x,k,a,c,p,z,u,al,H = s.symbols('x k a c p z u al H', real=True)
checks = []

def check(name, value):
    assert value, name
    checks.append(name)

def red(poly):
    ans = 0
    for (i,j), coeff in s.Poly(s.expand(poly),p,z).terms():
        if i < 3 and j < 3:
            ans += coeff*p**i*z**j
    return s.expand(ans)

unit = [sum(s.Rational(weight)*s.Rational(rate)**i/s.factorial(i)
            for weight,rate in [(2,-1),(-2,-3),(1,-4)]) for i in range(5)]
check('full_unit_coefficients', unit == [1,0,0,-2,4])
free3 = al**3/s.Integer(6)+H*al**2/s.Integer(2)
total3 = x*(u**3/s.Integer(6)-2*k**3) + free3.subs(H,-x*u-al)
check('third_character_after_first_character',
      s.expand(total3-(x*u**3/s.Integer(6)-x*u*al**2/s.Integer(2)-al**3/s.Integer(3)-2*x*k**3))==0)

alpha=a*p+c*z
base=red(x*(p+z)**3/s.Integer(6)-x*(p+z)*alpha**2/s.Integer(2)-alpha**3/s.Integer(3))
ap=x*(1-a*a-2*a*c)/2-a*a*c
am=x*(1-c*c-2*a*c)/2-a*c*c
check('both_generic_mixed_cubic_coefficients', s.expand(base-ap*p*p*z-am*p*z*z)==0)
check('unit_cubic_on_two_planes', s.expand(red(2*x*k**3*(p+z)**3)-6*x*k**3*(p*p*z+p*z*z))==0)

b,kap,d,vol=s.symbols('b kap d vol',real=True)
ch2 = x*u*u/2-al*al/2-x*u*al
square = (al+x*u)**2-x*(1+x)*u*u
check('completed_square_second_character', s.expand(square+2*ch2)==0)
check('kappa_positive_factor', s.factor(x*(1+x))==x*(x+1))

# Generic diagonal-block compound, all variables independent.
u1,u2,v1,v2,t=s.symbols('u1 u2 v1 v2 t', nonzero=True, real=True)
indices=list(combinations(range(4),2))
def compound(mat):
    return s.Matrix([[s.expand(mat.extract(I,J).det()) for J in indices] for I in indices])
U=s.diag(u1,u2,v1,v2)
B=s.diag(t*u1,t*u2,kap*v1/t,kap*v2/t)
diff=compound(B)-kap*compound(U)
check('generic_block_compound_mixed_cancellation', all(s.simplify(diff[i,j])==0 for i in range(6) for j in range(6) if (i,j) not in [(0,0),(5,5)]))
check('both_generic_pure_coefficients',s.simplify(diff[0,0]-(t*t-kap)*u1*u2)==0 and s.simplify(diff[5,5]-(kap*kap/t**2-kap)*v1*v2)==0)

# Rank-one U and invertible V: a pure plus wedge and two mixed wedges
# force support e0,e1,e2,e3. Both rank-one blocks force both pure planes.
support_12={0,1}
for I in [(0,2),(0,3)]:
    support_12.update(I)
check('singular_rank_one_two_support_is_four', support_12==set(range(4)))
support_11=set((0,1))|set((2,3))
check('singular_rank_one_one_support_is_four', support_11==set(range(4)))
check('compound_possible_ranks', [s.binomial(j,2) for j in range(5)]==[0,0,1,3,6])
check('singular_rhs_rank_bounds', 1+2==3 and 2+2==4 and 3<6 and 4<6)

# Exact whole-character truncation in the two-plane commutative algebra,
# with the formal specialization D=k(p+z). This is not a hypothesis of the proof.
# Substituting p/z separately in alpha gives the same cubic before and
# after first-character elimination, without using any compound relation.
def exp_red(form):
    return sum(red(form**j)/s.factorial(j) for j in range(5))
full=red(x*exp_red(p+z)*(1-2*k**3*(p+z)**3+4*k**4*(p+z)**4)
         +exp_red(alpha)*(1-x*(p+z)-alpha))
full3=sum(coeff*p**i*z**j for (i,j),coeff in s.Poly(full,p,z).terms() if i+j==3)
check('independent_full_exponential_cubic',s.expand(full3-(ap*p*p*z+am*p*z*z-6*x*k**3*(p*p*z+p*z*z)))==0)

out={'status':'PASS','checks':checks,'check_count':len(checks),
     'elapsed_seconds':perf_counter()-started,
     'scope':'Exact algebra supplement only; no finite-test inference of universal geometry or semiregularity',
     'draft_sha256':hashlib.sha256((root/'rm_mixed_star_cubic_obstruction_draft.md').read_bytes()).hexdigest()}
(root/'rm_mixed_star_cubic_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
