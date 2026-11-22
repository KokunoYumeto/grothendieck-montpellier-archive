"""B87: exact shared-quotient, coefficient, and p=5 point-field checks.

The field constructions and all-prime coefficient lemma are proved in the
accompanying text.  This finite certificate reconstructs the complete four-row
valuation table and the exhaustive two-by-two ramification-line alternatives;
it does not search over unbounded ramification breaks or infer realizability.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
from itertools import product
from fractions import Fraction
from math import comb
import json
import time
import sympy as sp

started = time.perf_counter()
counts = Counter()
p, A, t, u = sp.symbols('p A t u')
J = A + (p-1)*t
D0 = J+u
assert sp.expand((D0-A)-(u+(p-1)*t)) == 0
assert sp.expand((A+p*u)-(J+u)-(p-1)*(u-t)) == 0
assert sp.expand(((u+1)+(p-1)*(t+1))/p-1-(D0-A)/p) == 0
counts['uniform_symbolic_coefficient_and_quotient_identities'] = 3

# Independently check the binomial fact used in the fixed-coefficient lemma.
# This range is a finite supplement only, not its uniform proof.
for prime in (5, 7, 11):
    for degree in range(1, 301):
        q = degree
        first = 1
        while q % prime == 0:
            q //= prime
            first *= prime
        assert all(comb(degree, j) % prime == 0 for j in range(1, first))
        assert comb(degree, first) % prime != 0
        counts['literal_binomial_first_terms'] += 1

prime, N, e, q = 5, 24, 20, 25
eL = N*e
eE = q*eL
rows = []
high_lines = {1: 'e1', 2: 'e2'}
parameters = {1: 25, 2: 75}
for field, target_line in ((1, 'e1'), (2, 'e2')):
    for model, B in parameters.items():
        low, high = Fraction(B, prime), (prime+1)*e-B
        target = high if high_lines[model] == target_line else low
        # Actual inverse polygon: (0,target), (1,eL), (5,(p-1)B), (25,0).
        # Both interior vertices lie strictly above its unique segment.
        for x, y in ((1, eL), (prime, (prime-1)*B)):
            assert y > target*(q-x)/q
            counts['inverse_polygon_strict_vertices'] += 1
        point_valuation = q * Fraction(target, q)
        assert point_valuation.denominator == 1
        point_valuation = int(point_valuation)
        assert point_valuation % prime == 0 and point_valuation % q != 0
        Dlow, Dhigh = int(q*low), q*high
        assert 0 < Dlow < Dhigh < eE
        high_displacement = 'diagonal' if high_lines[model] == target_line else 'off'
        forced_quotient_break = Fraction(Dlow-point_valuation, prime)
        assert forced_quotient_break.denominator == 1
        rows.append({'field': field, 'model': model, 'A': point_valuation,
                     'D0': Dlow, 'D1': Dhigh, 'high_displacement_line': high_displacement,
                     'forced_larger_break_if_last_line_differs': int(forced_quotient_break)})
        counts['actual_point_coordinate_rows'] += 1
assert [(r['A'], r['D0'], r['D1']) for r in rows] == [
    (95, 125, 2375), (15, 375, 1125),
    (5, 125, 2375), (45, 375, 1125)]
assert [r['forced_larger_break_if_last_line_differs'] for r in rows] == [6, 72, 24, 66]
assert eE == 12000

# Literal first-layer spaces <E12,E21,diag(a,b)> for all 16 possible
# nonzero diagonal coordinates.  Point kernels and the common diagonal
# quotient are checked on every vector, not merely on the three generators.
for a, b in product(range(1, prime), repeat=2):
    mats = {(z*a % prime, x, y, z*b % prime): (x, y, z)
            for x, y, z in product(range(prime), repeat=3)}
    assert len(mats) == prime**3
    eval1 = {(M[0], M[2]) for M in mats}
    eval2 = {(M[1], M[3]) for M in mats}
    assert len(eval1) == len(eval2) == q
    ker1 = {coords for M, coords in mats.items() if (M[0], M[2]) == (0, 0)}
    ker2 = {coords for M, coords in mats.items() if (M[1], M[3]) == (0, 0)}
    assert ker1 == {(x, 0, 0) for x in range(prime)}
    assert ker2 == {(0, y, 0) for y in range(prime)}
    assert {((M[0]*pow(a,-1,prime)) % prime,
             (M[3]*pow(b,-1,prime)) % prime)
            for M in mats} == {(z,z) for z in range(prime)}
    for M, coords in mats.items():
        x, y, z = coords
        assert (M[0], M[2]) == (a*z % prime, y)
        assert (M[1], M[3]) == (x, b*z % prime)
        counts['literal_first_layer_vectors'] += 1
    counts['nonzero_diagonal_spaces'] += 1

# In the tame quotient F/L, eta^5=zeta, so character weight is 5*break.
break_residues = {}
for weight in (0, 6, 18):
    residues = [j for j in range(N) if prime*j % N == weight]
    assert residues == [weight]
    break_residues[str(weight)] = residues
    counts['tame_break_residue_classes'] += 1
# Check the two distinct eigenspaces are the only stable F5-lines.
lines = [{((c*x)%prime,(c*y)%prime) for c in range(prime)}
         for x,y in [(1,j) for j in range(prime)]+[(0,1)]]
for ratio in (2,3):
    stable = [line for line in lines
              if {(x, ratio*y % prime) for x,y in line} == line]
    assert len(stable) == 2
    assert stable[0] == {(c,0) for c in range(prime)}
    assert stable[1] == {(0,c) for c in range(prime)}
    counts['tame_stable_line_checks'] += len(lines)

# Exhaust the four geometric last-line possibilities, using exact inequalities
# rather than a finite search for the (a priori unbounded) diagonal break d.
branches = []
for last1,last2 in product(('diagonal','off'), repeat=2):
    if last1 == 'off':
        off1 = rows[0]['forced_larger_break_if_last_line_differs']
        assert off1 == 6 < N
        reason = 'E1 off would require 6>d>=24'
    else:
        diagonal = rows[1]['forced_larger_break_if_last_line_differs']
        assert diagonal == 72
        if last2 == 'diagonal':
            diagonal2 = rows[2]['forced_larger_break_if_last_line_differs']
            assert diagonal2 == 24 != diagonal
            reason = 'The same diagonal field would have breaks 72 and24'
        else:
            off2 = rows[3]['forced_larger_break_if_last_line_differs']
            assert off2 == 66 < diagonal
            reason = 'E2 off would require 66>72'
    branches.append({'E1_last': last1, 'E2_last': last2,
                     'excluded': True, 'reason': reason})
    counts['exhaustive_last_line_branches'] += 1

out = {'status':'PASS', 'actual_utc':datetime.now(timezone.utc).isoformat(),
       'runtime_seconds':time.perf_counter()-started, 'counts':dict(counts),
       'valuation_rows':rows, 'mixed_characteristic_cutoff':eE,
       'tame_break_residues':break_residues, 'last_line_branches':branches,
       'scope':'Exact four-row Newton and displacement reconstruction, all 16 first-layer diagonal choices, '
               'all four last-line choices and exact tame residues. The 900 literal binomial rows '
               'are a finite supplement to the separately written uniform coefficient proof. '
               'No actual full congruence image is constructed or excluded; no other residual sector is settled.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
