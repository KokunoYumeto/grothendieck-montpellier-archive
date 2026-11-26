#!/usr/bin/env python3
"""Exact, small arithmetic checks for the exposed p=37 research note.

This is not an L-value, Mordell-Weil-rank, or Sha certificate.
Only Python standard-library integer/rational arithmetic is used.
"""
import json
from fractions import Fraction
from math import comb

p = 37
s = 10
S = [b for b in range(1, p) if b + (s*b) % p < p]
H = [h for h in range(1, p) if sorted((h*b) % p for b in S) == S]
assert H == [1, 10, 26]
g = next(a for a in range(2, p) if len({pow(a, k, p) for k in range(p-1)}) == p-1)
assert g == 2
T = [j for j in range(12) if pow(g, j, p) in S]
assert T == [0, 1, 2, 3, 4, 11]
T_stabilizer = [h for h in range(12) if sorted((t+h) % 12 for t in T) == T]
assert T_stabilizer == [0]
quartic_counts = [sum(t % 4 == i for t in T) for i in range(4)]
assert quartic_counts == [2, 1, 1, 2]

# Shu's r=1,s=10,t=26,delta=1 tame test, carried out modulo p^2.
z = pow(10, 10, p*p) * pow(-11, 26, p*p) % (p*p)
qz = ((pow(z, p-1, p*p)-1)//p) % p
assert z == 581 and qz == 0
# Independent Gross--Rohrlich tame test.
m = sum(pow(b, -1, p) for b in S)
assert m == 333 and m % p == 0
legendre_two = pow(2, (p-1)//2, p)
assert legendre_two == p-1

# The coordinates of the order-three symmetry use 10^2+10+1=3*37.
assert s*s+s+1 == 3*p
# In the displayed c^2 and c^3 formulas, y^100 = y^26*x^2*(1-x)^20
# and y^260 = y*x^7*(1-x)^70, using y^37=x*(1-x)^10.
assert divmod(100, p) == (2, 26)
assert divmod(260, p) == (7, 1)
# Riemann--Hurwitz: g(C)=18, two points of ramification index 3.
gC = (p-1)//2
gB = ((2*gC-2-4)//3 + 2)//2
assert gB == 6 and 2*gC-2 == 3*(2*gB-2)+4

dlogs = {pow(g, k, p): k for k in range(p-1)}
assert dlogs[26] == 12 and dlogs[10] == 24
assert dlogs[26] % 3 == dlogs[10] % 3 == 0
assert {dlogs[h] % 9 for h in H} == {0, 3, 6}
# c acts as 10 on the rational 37-torsion branch divisor.
assert pow(10, 3, 37) == 1 and 10 != 1
assert (1+10+26) % 37 == 0
assert (2-10-26) % 37 == 3

# Exact Bernoulli computation records why a regular-prime formula is unavailable.
B = [Fraction(1)]
for n in range(1, 35):
    B.append(-sum(Fraction(comb(n+1, k))*B[k] for k in range(n))/Fraction(n+1))
irregular = [n for n in range(2, 35, 2) if B[n].numerator % p == 0]
assert irregular == [32]

print(json.dumps({
    'status': 'PASS: exact structural arithmetic only',
    'prime': p, 'curve_exponents': [1,10,26],
    'CM_type_on_Q_zeta37': S, 'CM_type_stabilizer': H,
    'primitive_generator_mod37': g, 'descended_CM_type_mod12': T,
    'descended_type_translation_stabilizer': T_stabilizer,
    'counts_over_quartic_CM_subfield': quartic_counts,
    'Shu_tame_argument_mod1369': z, 'Fermat_quotient_mod37': qz,
    'Gross_Rohrlich_m': m, 'Legendre_2_mod37': -1,
    'genera_C_B': [gC,gB],
    'dlogs_of_10_26': [dlogs[10],dlogs[26]],
    'global_twist_order_needed': 9,
    'rational_branch_torsion_c_eigenvalue': 10,
    'irregular_Bernoulli_indices': irregular,
    'B32': [B[32].numerator,B[32].denominator],
    'not_certified': ['central L-value', 'exact rank', 'Sha finiteness']
}, indent=2))
