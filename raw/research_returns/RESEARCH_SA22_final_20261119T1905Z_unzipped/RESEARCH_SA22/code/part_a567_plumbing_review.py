"""Independent rational check of the cross-ratio witness in A1-hinich-counterexample.

The global bijectivity argument is recorded in notes/part_a567.md.
This check uses quotient differentiation directly, without SymPy or residues.
"""
from fractions import Fraction as Q
import json

A, B, R, C = Q(420,569), Q(3,4), Q(3,2), Q(10)
t0, slope, radius = Q(9,11), Q(11,9), Q(11,10)
assert slope*t0 == 1
assert 0 < A < B < Q(9,10)
assert R > radius
assert abs(C) > radius and abs(2*R-C) > radius
c = (R-C)**2
a, b = (R-A)**2, (R-B)**2
da, db = -2*slope*A*(R-A), -2*slope*B*(R-B)
dda, ddb = 2*slope*slope*A*A, 2*slope*slope*B*B
first_numerator = da*(b-c)-(a-c)*db
assert first_numerator == 0
second = (dda*(b-c)-(a-c)*ddb)/(b-c)**2
assert second == Q(271040,371353867)
assert second != 0
assert len({a,b,c}) == 3
print(json.dumps({
    "status":"PASS",
    "method":"Exact Fraction arithmetic; quotient rule independent of the root's symbolic/residue script.",
    "first_derivative_numerator":str(first_numerator),
    "second_derivative":str(second),
    "cross_ratio_at_critical_parameter":str((a-c)/(b-c)),
    "retained_first_piece":"|z|<9/(10|t|), hence |(11t/9)z|<11/10",
    "second_piece_complement":"phi(closed disc of radius (11/10)|t|)",
    "overlap":"phi({(11/10)|t|<|u|<11/10})",
    "coverage_and_injectivity":"The retained images cover P1 and their intersection is exactly the identified annulus; phi is injective on |u|<11/10 since the other equality would require u+v=3."
},indent=2))
