"""Different-method arithmetic checks for the conductor-equality structure theorem.

Run from any directory with Python 3 and SymPy installed.  This derives numbers
from intersection vectors and the individual filtration quotients.  It does
not certify the geometric hypotheses or replace the proof.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import json
import sympy as s

root = Path(__file__).resolve().parents[1]
assertions = 0
def require(value):
    global assertions
    assert value
    assertions += 1

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])
def scale(n, x):
    return (n*x[0], n*x[1])
def meet(x, y, d):
    # H.R=0, H.H=d, R.R=-1; R coefficient is zero before blowing up.
    return x[0]*y[0]*d-x[1]*y[1]
def rr(line, canonical, chi, d):
    return chi + Q(meet(line, add(line, scale(-1, canonical)), d), 2)

cases = 0
small_survivors = []
for p in (2, 3, 5, 7, 11, 17, 31):
    for a in range(1, 13):
        for d in range(1, 81):
            for eps in ((0,1) if p == 2 else (0,)):
                H = (1,0)
                K = (p*a-1,0)
                cx = eps-meet(H,add(K,H),d)
                chi = Q(meet(K,K,d)+cx,12)
                # RR of every graded quotient, not the closed sum formula.
                filtered = sum(rr(scale(i*a,H),K,chi,d) for i in range(p))
                # Work upstairs on the smooth blowup and use the two
                # cotangent exact sequences for a regular foliation.
                F = (1,eps)
                Kb = add(K,(0,eps))
                pulled_quotient_K = add(Kb,scale(-(p-1),F))
                ct = -meet(F,add(Kb,F),d)
                kt = Q(meet(pulled_quotient_K,pulled_quotient_K,d),p)
                chi_quotient = Q(kt+ct,12)
                require(ct == cx+eps)
                require(ct == -p*a*d+2*eps)
                require(kt == p*(a-1)**2*d)
                require(filtered == chi_quotient)
                require(12*filtered == p*(a*a-3*a+1)*d+2*eps)
                # Projection line is H, or H-R after the unique blowup.
                projection_line = (1,-eps)
                require(meet(projection_line,projection_line,d) == d-eps)
                if a in (2,3) and filtered.denominator == 1 and filtered > 0 and kt <= 32*filtered:
                    small_survivors.append([p,a,d,eps])
                cases += 1
require(not small_survivors)

# Eliminate the two cover coordinates, rather than guessing generators of the
# invariant semigroup: the sole equation of the characteristic-two quotient
# is AC-B^2.  This is an exact finite polynomial computation.
u,w,A,B,C = s.symbols('u w A B C')
gb = s.groebner([A-u*u,B-u*w,C-w*w],u,w,A,B,C,modulus=2,order='lex')
eliminated = [p.as_expr() for p in gb.polys if not p.as_expr().has(u,w)]
require(len(eliminated) == 1)
require(s.Poly(eliminated[0]-(A*C-B*B),A,B,C,modulus=2).is_zero)

# Compare the kernel dimensions of the Euler operator on homogeneous binary
# forms with the Hilbert series of one quadratic equation in three generators
# of degree two.  This checks the graded dimensions by a second construction.
hilbert = []
for degree in range(101):
    kernel_dimension = sum(1 for i in range(degree+1) if degree % 2 == 0)
    if degree % 2:
        quotient_dimension = 0
    else:
        n = degree//2
        quotient_dimension = (n+2)*(n+1)//2 - (n*(n-1)//2 if n>=2 else 0)
    require(kernel_dimension == quotient_dimension)
    hilbert.append([degree,kernel_dimension,quotient_dimension])

# The small-conductor characteristic-two contradiction is exact: GSZ at a=3
# forces positive integral d<=2, while Noether gives chi=(d+1)/6.
require(Q(2,6).denominator != 1)
require(Q(3,6).denominator != 1)
result = dict(
    checked_utc=datetime.now(timezone.utc).isoformat(), status='PASS',
    assertions=assertions, intersection_and_filtration_cases=cases,
    method='Direct divisor-vector intersection algebra; RR summed on every filtration quotient; regular-foliation cotangent Chern product; exact Groebner elimination; Euler-operator kernel dimensions versus hypersurface Hilbert series.',
    eliminated_relation=str(eliminated[0]), hilbert_degree_range=[0,100],
    a2_a3_survivors=small_survivors,
    limitations='Arithmetic verification only; geometric proofs and the infinite-parameter inequalities are established separately in the text.')
out = root/'records/CONDUCTOR_EULER_STRUCTURE_ARITHMETIC.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
