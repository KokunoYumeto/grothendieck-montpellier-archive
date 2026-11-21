"""Exact characteristic-polynomial certificate by a modular cyclic vector.

No characteristic-polynomial routine is called.  A nonzero Krylov
determinant modulo a checked prime proves cyclicity over Q.  Exact integer
Horner evaluation then proves the asserted degree-n monic polynomial.
Failure to exhibit a cyclic vector is inconclusive and never a PASS.
"""
from fractions import Fraction
from math import isqrt, lcm
from flint import fmpz_mat, nmod_mat


def certify_characteristic_polynomial(matrix, claimed):
    a = [[Fraction(x) for x in row] for row in matrix]
    n = len(a)
    assert n > 0 and all(len(row) == n for row in a)
    coefficients = [Fraction(x) for x in claimed]
    assert len(coefficients) == n+1 and coefficients[0] == 1
    denominator = lcm(*(x.denominator for row in a for x in row))
    integral = [[x.numerator*(denominator//x.denominator) for x in row]
                for row in a]
    assert all(Fraction(integral[i][j], denominator) == a[i][j]
               for i in range(n) for j in range(n))
    scaled = [c*denominator**j for j, c in enumerate(coefficients)]
    assert all(c.denominator == 1 for c in scaled)
    scaled = [int(c) for c in scaled]
    candidates = [([int(i == j) for i in range(n)], f'basis_{j}')
                  for j in range(min(n, 3))]
    candidates += [([1]*n, 'ones'),
                   ([i+1 for i in range(n)], 'successive'),
                   ([(i+1)**2 for i in range(n)], 'squares')]
    witness = None
    for prime in (1000003, 1000033, 1000037):
        assert prime > 1 and all(prime % t for t in range(2, isqrt(prime)+1))
        if denominator % prime == 0:
            continue
        bmod = nmod_mat(integral, prime)
        for vector, vector_name in candidates:
            current = nmod_mat([[x] for x in vector], prime)
            columns = []
            for j in range(n):
                columns.append([int(current[i, 0]) for i in range(n)])
                if j+1 < n:
                    current = bmod*current
            krylov = nmod_mat([[columns[j][i] for j in range(n)]
                               for i in range(n)], prime)
            determinant = int(krylov.det())
            if determinant:
                witness = (prime, vector, vector_name, determinant)
                break
        if witness is not None:
            break
    if witness is None:
        raise ArithmeticError('INCONCLUSIVE: no cyclic vector exhibited')
    prime, vector, vector_name, determinant = witness
    b = fmpz_mat(integral)
    v = fmpz_mat([[x] for x in vector])
    current = v
    for coefficient in scaled[1:]:
        current = b*current+coefficient*v
    assert current == fmpz_mat(n, 1), 'claimed polynomial fails exact Horner identity'
    return coefficients, {
        'dimension': n,
        'clearing_denominator': str(denominator),
        'prime': prime,
        'cyclic_vector': vector,
        'cyclic_vector_name': vector_name,
        'krylov_determinant_mod_prime': determinant,
        'exact_integer_horner_zero': True,
        'monic_degree_equals_dimension': True,
        'method': 'modular full-rank Krylov certificate and exact integer Horner identity',
    }
