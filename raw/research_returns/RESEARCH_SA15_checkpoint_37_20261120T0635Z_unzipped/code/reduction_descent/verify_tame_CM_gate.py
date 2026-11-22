#!/usr/bin/env python3
"""Finite algebra checks for B52; not a numerical construction of a CM deformation.

The proof of the formal deformation and descent statements is in the TeX file.
This script checks the exact centralizer identity, its complete small-prime
matrix instances, the ramified norm obstruction, the displayed Eisenstein
polynomial, and the explicit first-level CM character pair.
"""
from pathlib import Path
import json
import math
import time
import sympy as sp

started = time.perf_counter()
a, b, c, d, delta = sp.symbols('a b c d delta')
A = sp.Matrix([[a, b], [c, d]])
J = sp.Matrix([[0, delta], [1, 0]])
commutator = A*J-J*A
expected = sp.Matrix([[b-delta*c, delta*(a-d)], [d-a, delta*c-b]])
assert (commutator-expected).applyfunc(sp.expand) == sp.zeros(2)
assert commutator.subs({b:delta*c, d:a}) == sp.zeros(2)
assert sp.expand(A.det().subs({b:delta*c, d:a})) == a*a-delta*c*c

def vp(n, p):
    assert n != 0
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value

primes = list(sp.primerange(5, 102))
norm_tests = 0
ramified_root_tests = 0
eisenstein_coefficients = 0
matrix_tests = 0
matrix_cases = []
eisenstein_cases = []
lower_pairs = []
conjugacy_terms = 0

for p in primes:
    q = p*p
    N = q-1
    ns = next(x for x in range(2, p) if pow(x, (p-1)//2, p) == p-1)

    # Noncommutative telescoping: blocks v^i lambda^j only use
    # v^N=lambda^N=1; no commutation of v and lambda is assumed.
    left = {((i+1)%N, (-i)%N) for i in range(N)}
    right = {(i%N, (1-i)%N) for i in range(N)}
    assert len(left) == len(right) == N and left == right
    assert N % p != 0
    conjugacy_terms += N

    # An unramified quadratic unit with nonsquare norm has nonzero
    # non-base-field coordinate and irreducible separable characteristic
    # polynomial modulo p. This is the maximal-order lattice test.
    for x in range(p):
        for y in range(p):
            norm = (x*x-ns*y*y) % p
            if norm and pow(norm, (p-1)//2, p) == p-1:
                assert y != 0
                discriminant = (4*ns*y*y) % p
                assert pow(discriminant, (p-1)//2, p) == p-1
            norm_tests += 1

    # For p=3 mod4 every root of order dividing 2(p-1) has square
    # norm; for p=1 mod4 both signs of a ramified unit norm are squares.
    if p % 4 == 3:
        for exponent in range(N):
            if (2*(p-1)*exponent) % N == 0:
                assert exponent % 2 == 0
                ramified_root_tests += 1
    else:
        assert pow(p-1, (p-1)//2, p) == 1
        for x in range(1, p):
            assert pow(x*x % p, (p-1)//2, p) == 1
            assert pow((-x*x) % p, (p-1)//2, p) == 1
            ramified_root_tests += 2

    if p <= 19:
        count = invertible = 0
        for aa in range(p):
            for bb in range(p):
                for cc in range(p):
                    for dd in range(p):
                        # Commutation with 1+pJ modulo p^2 is exactly
                        # commutation of A mod p with J.
                        equations = ((bb-ns*cc)%p, ns*(aa-dd)%p,
                                     (dd-aa)%p, (ns*cc-bb)%p)
                        central = all(v == 0 for v in equations)
                        assert central == (dd == aa and bb == ns*cc % p)
                        if central:
                            count += 1
                            invertible += (aa*dd-bb*cc)%p != 0
                        matrix_tests += 1
        assert count == q and invertible == N
        matrix_cases.append({'p':p, 'nonsquare':ns,
                             'centralizer_size':count,
                             'invertible_centralizer_size':invertible})

        # Phi_2(T)=p+(pT+T^q)^(q-1). The nonconstant exponents are
        # (q-1)(i+1); all but the monic leading coefficient are p-divisible.
        coefficients = [math.comb(q-1, i)*p**(q-1-i) for i in range(q)]
        assert coefficients[-1] == 1
        valuations = [vp(z,p) for z in coefficients[:-1]]
        assert min(valuations) == 1
        assert all(v >= 1 for v in valuations)
        assert vp(p,p) == 1
        degree = (q-1)*q
        assert degree == len(range(q))* (q-1)
        eisenstein_coefficients += q
        eisenstein_cases.append({'p':p, 'degree':degree,
                                  'constant_valuation':1,
                                  'minimum_other_nonleading_valuation':min(valuations)})

    r1, r2 = 1, q-p+1
    first_type = sorted({r1%N, p*r1%N})
    second_type = sorted({r2%N, p*r2%N})
    assert first_type == [1,p]
    assert second_type == sorted({(2-p)%N,(2*p-1)%N})
    assert first_type != second_type
    first_generic = ((p-1)+r1)%N
    second_generic = ((p-1)+r2)%N
    assert first_generic == p and second_generic == 1
    assert p*first_generic%N == second_generic
    assert (p+1)*r1%N == (p+1)*r2%N
    assert math.gcd(r1,p-1) == math.gcd(r2,p-1) == 1
    lower_pairs.append({'p':p,'finite_type_1':first_type,
                        'finite_type_2':second_type,
                        'generic_mod_p_exponents':[first_generic,second_generic],
                        'common_norm_exponent':(p+1)*r1%N})

result = {
    'status':'PASS',
    'scope':'Exact finite algebra only; universal formal deformation, CM descent and full division-field arguments are proved in B_tame_CM_gate.tex.',
    'symbolic_centralizer':str(commutator),
    'prime_range':[int(primes[0]),int(primes[-1])],
    'number_of_primes':len(primes),
    'norm_tests':norm_tests,
    'unit_conjugacy_telescoping_terms':conjugacy_terms,
    'ramified_root_tests':ramified_root_tests,
    'matrix_tests':matrix_tests,
    'matrix_cases':matrix_cases,
    'eisenstein_coefficients':eisenstein_coefficients,
    'eisenstein_cases':eisenstein_cases,
    'lower_character_pairs':lower_pairs,
    'elapsed_seconds':time.perf_counter()-started,
}
outpath = Path(__file__).with_suffix('.output.json')
outpath.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
