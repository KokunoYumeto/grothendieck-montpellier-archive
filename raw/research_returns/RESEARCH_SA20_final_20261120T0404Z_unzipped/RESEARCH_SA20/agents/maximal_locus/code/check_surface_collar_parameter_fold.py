#!/usr/bin/env python3
"""Exact finite certificate for the parameter-fold example in A5.016.

This checks the three affine pieces, boundary matching, and three distinct
preimages with certified region inequalities. It does not prove the PL collar
or surface approximation theorems; their complete proofs are in the text.
"""
import json
import time
import sympy as sp

started = time.perf_counter()
a, t, rho = sp.symbols('a t rho', real=True)
alpha, beta = sp.symbols('alpha beta', positive=True)
pieces = [3*t, 2*a-t, t]
tests = []

def zero(name, expression):
    reduced = sp.factor(expression)
    assert reduced == 0, (name, reduced)
    tests.append({'name': name, 'pass': True, 'kind': 'exact identity'})

def positive(name, expression):
    # These substitutions cover 0<a<1/2 and 0<rho<1 over any RCF.
    rational = sp.cancel(expression.subs({
        a: alpha/(2*(1+alpha)), rho: beta/(1+beta)
    }))
    numerator, denominator = sp.fraction(rational)
    for polynomial in (numerator, denominator):
        coefficients = sp.Poly(polynomial, alpha, beta).coeffs()
        assert coefficients and all(c > 0 for c in coefficients), (
            name, rational, coefficients
        )
    tests.append({'name': name, 'pass': True,
                  'kind': 'positive rational function',
                  'certificate': str(rational)})

for index, slope in enumerate([3, -1, 1]):
    zero(f'affine_piece_{index+1}_slope', sp.diff(pieces[index], t)-slope)
zero('first_second_boundary_match',
     pieces[0].subs(t, a/2)-pieces[1].subs(t, a/2))
zero('second_third_boundary_match',
     pieces[1].subs(t, a)-pieces[2].subs(t, a))
zero('zero_boundary_height', pieces[0].subs(t, 0))
zero('parameter_zero_positive_branch', pieces[2].subs(a, 0)-t)

level = a*(1+rho/2)
roots = [level/3, 2*a-level, level]
for index, root in enumerate(roots):
    zero(f'preimage_{index+1}_height', pieces[index].subs(t, root)-level)

positive('level_above_a', level-a)
positive('level_below_three_a_over_two', 3*a/2-level)
positive('first_root_above_zero', roots[0])
positive('first_root_below_a_over_two', a/2-roots[0])
positive('second_root_above_a_over_two', roots[1]-a/2)
positive('second_root_below_a', a-roots[1])
positive('third_root_above_a', roots[2]-a)
positive('third_root_below_one', 1-roots[2])
positive('second_root_minus_first', roots[1]-roots[0])
positive('third_root_minus_second', roots[2]-roots[1])
positive('third_root_minus_first', roots[2]-roots[0])

print(json.dumps({
    'statement_id': 'A5.016', 'status': 'PASS',
    'test_count': len(tests), 'tests': tests,
    'arithmetic': 'exact rational identities and positive-coefficient certificates',
    'parameterization': 'a=alpha/(2*(1+alpha)), rho=beta/(1+beta), alpha,beta>0',
    'scope': 'Finite algebra for the parameter-fold example only; collar and surface theorems are proved mathematically.',
    'elapsed_seconds': time.perf_counter()-started,
}, indent=2))
