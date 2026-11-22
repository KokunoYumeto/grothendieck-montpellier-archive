"""Exact convention certificates for PNEW-013 and K-024.

The all-dimensional proofs are separate. These checks use integer and
rational polynomial arithmetic only, including modular gcds.
"""
from collections import Counter
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import json
import sympy as s

x, t, z = s.symbols('x t z')
cyclotomic_cases = 0
for prime in (2, 3, 5, 7):
    for degree in range(1, 257):
        e, exponent = degree, 0
        while e % prime == 0:
            e //= prime
            exponent += 1
        power = 1 if exponent == 0 else (prime - 1) * prime ** (exponent - 1)
        lhs = s.Poly(s.cyclotomic_poly(degree, x), x, modulus=prime)
        rhs = s.Poly(s.cyclotomic_poly(e, x), x, modulus=prime) ** power
        assert lhs == rhs
        cyclotomic_cases += 1

assert s.cancel((1 + z) / (1 - z + z*z) - 1/(1 + z) - 3*z/(1 + z**3)) == 0
warning_receipts = []
for M in (4, 8, 16, 32):
    zp = t ** (M//2)
    F = (1 + zp)/(1 - zp + zp*zp) + 2*t/(1 - t)**2
    G = 1/(1 + zp) + 2*t/(1 - t)**2
    assert s.Poly(1 - zp + zp*zp, t) == s.Poly(s.cyclotomic_poly(3*M, t), t)
    numerator, denominator = s.fraction(s.cancel(F))
    assert s.gcd(denominator, s.cyclotomic_poly(M, t)) == 1
    assert s.rem(denominator, s.cyclotomic_poly(3*M, t), t) == 0
    for j in range(12*M+1):
        fbase = [1, 2, 1, -1, -2, -1][(j//(M//2))%6] if j%(M//2)==0 else 0
        gbase = (-1)**(j//(M//2)) if j%(M//2)==0 else 0
        fv, gv = fbase + 2*j, gbase + 2*j
        assert fv >= 0 and gv >= 0 and (fv-gv)%3 == 0
    warning_receipts.append({'M': M, 'only_nontrivial_F_pole_order': 3*M,
                             'G_primitive_M_residue': 2,
                             'nonnegative_congruence_checks_through': 12*M})

hook_receipts = []
for n in range(2, 9):
    M = 2 ** (n-1)
    phi = s.Poly(x ** (M//2) + 1, x, domain=s.QQ)
    w = [pow(-2, j, M) for j in range(n)]
    assert len(set(w)) == n and w[-1] == 0 and gcd(sum(w), M) == 1
    linear = Counter(w)
    repeated = Counter((2*w[i]+w[j])%M for i in range(n) for j in range(n) if i!=j)
    distinct = Counter()
    for i,j,k in combinations(range(n),3):
        distinct[(w[i]+w[j]+w[k])%M] += 2
    fixed = linear[0]+repeated[0]+distinct[0]
    assert (linear[0],repeated[0],distinct[0]) == (1,n-1,0)
    adjoint = Counter((w[i]-w[j])%M for i in range(n) for j in range(n) if i!=j)
    assert not adjoint[0]
    multiplicity = adjoint - (linear + repeated + distinct)
    # Counter subtraction removes negative entries; build signed list explicitly.
    factors = {}
    for a in range(1,M):
        exponent = adjoint[a]-linear[a]-repeated[a]-distinct[a]
        if exponent:
            factors[a] = exponent
    C = s.Poly(1,x,domain=s.QQ)
    for a, exponent in factors.items():
        fac = s.Poly(1-x**a,x,domain=s.QQ).rem(phi)
        assert s.gcd(s.Poly(fac,x,modulus=3),s.Poly(phi,x,modulus=3)).degree()==0
        if exponent < 0:
            fac = s.invert(fac,phi)
        for _ in range(abs(exponent)):
            C = (C*fac).rem(phi)
    denominator = lcm(*(int(c.q) for c in C.all_coeffs()))
    assert denominator > 0 and denominator & (denominator-1) == 0
    integral_C = s.Poly(C.as_expr()*denominator,x,domain=s.ZZ)
    assert s.gcd(s.Poly(integral_C,x,modulus=3),s.Poly(phi,x,modulus=3)).degree()==0
    if n==2:
        assert C==s.Poly(1,x,domain=s.QQ)
    if n==3:
        assert C==s.Poly((1+x)/4,x,domain=s.QQ)
    hook_receipts.append({'n':n,'M':M,'determinant_exponent':sum(w)%M,
                           'fixed_linear_hook_repeated_hook_distinct':[linear[0],repeated[0],distinct[0]],
                           'residue_numerator_coefficients_low_to_high':[int(integral_C.nth(j)) for j in range(M//2)],
                           'residue_denominator':denominator,
                           'unit_at_every_prime_over_3':True})

result={'status':'PASS','cyclotomic_reduction_cases':cyclotomic_cases,
        'exact_order_warning_examples':warning_receipts,'hook_residue_checks':hook_receipts}
destination=Path(__file__).resolve().parents[1]/'certificates/modular_pole_transfer.json'
destination.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','cyclotomic_cases':cyclotomic_cases,
                  'warning_cases':len(warning_receipts),'hook_ranks':list(range(2,9))}))
