"""Exact arithmetic certificates for the Part A cap counterexamples.

These are finite arithmetic checks supporting, not replacing, the analytic proofs.
"""
from fractions import Fraction as F
from time import perf_counter
from pathlib import Path
import json

start = perf_counter()
def a(length_in_two_pi):
    return (1 + F(length_in_two_pi)**2)/2
def second_jet(lengths):
    a0,a1,ai = map(a,lengths)
    return (a0+a1-ai)/(2*a0)

jets = [second_jet(x) for x in [(1,1,1),(1,2,1)]]
assert jets == [F(1,2), F(5,4)]
assert F(7,4)<F(4,3)**2<F(7,5)**2<F(3,2)**2
assert F(1024,21)>4*F(22,7)**2
assert 17>4*4
result={
    'second_jet_coefficients':[str(x) for x in jets],
    'squared_annulus_bounds':[str(x) for x in [F(7,4),F(16,9),F(49,25),F(9,4)]],
    'extremal_lower_exact':str(F(1024,21)),
    'extremal_upper_pi_bound':str(4*F(22,7)**2),
    'impossible_tensor':17,
    'universal_pants_tensor_bound':16,
    'assertions':5,
    'status':'all exact arithmetic assertions passed',
    'seconds':perf_counter()-start
}
output=json.dumps(result,indent=2)
Path(__file__).with_suffix('.out.json').write_text(output+'\n')
print(output)
