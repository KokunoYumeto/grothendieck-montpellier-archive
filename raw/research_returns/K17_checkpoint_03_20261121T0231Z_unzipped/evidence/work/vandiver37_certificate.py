"""An exact, reproducible certificate for Vandiver at p=37.

Mathematical criterion: J. P. Buhler and D. Harvey,
Irregular primes to 163 million, section 4, pp. 4--5 of
https://arxiv.org/pdf/0912.2121 (published Math. Comp. 80 (2011), 2435--2444),
with the printed exponent corrected by Hart--Harvey--Ong,
Irregular primes to two billion, section 7, p. 13,
https://arxiv.org/pdf/1605.02398.
For every irregular even k in 2,...,p-3, it suffices to find a prime q=1 mod p
and a nontrivial pth root zeta mod q such that
 [product_{c=1}^{(p-1)/2} (zeta^(c/2)-zeta^(-c/2))^(c^(p-1-k))]
 ^((q-1)/p) != 1 mod q, with halves interpreted modulo p.
Here zeta=107 and z=16 is its unique square root in the order-37 subgroup.
Thus the factors below z^c-z^(-c) implement the corrected formula exactly.

No third-party Python dependencies. Two distinct exact calculations of
Bernoulli residues and two distinct modular-product evaluations are compared.
The citation supplies the number-theoretic criterion; this is a finite
arithmetic certificate, not a formalization of that criterion.
"""

from fractions import Fraction
from math import comb, factorial, isqrt, prod


def prime_by_trial_division(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def bernoulli_rational(nmax):
    # Sum_{j=0}^n binom(n+1,j) B_j = 0 for n>0; B_1=-1/2.
    values = [Fraction(1)]
    for n in range(1, nmax + 1):
        values.append(-sum(Fraction(comb(n + 1, j)) * values[j]
                           for j in range(n)) / (n + 1))
    return values


def bernoulli_by_series_mod_p(nmax, p):
    # Invert sum x^j/(j+1)! modulo p and multiply nth coefficient by n!.
    # nmax+1<p ensures every denominator is invertible.
    assert nmax + 1 < p
    exponential_quotient = [pow(factorial(j + 1), -1, p)
                            for j in range(nmax + 1)]
    inverse = [1]
    for n in range(1, nmax + 1):
        inverse.append(-sum(exponential_quotient[j] * inverse[n - j]
                            for j in range(1, n + 1)) % p)
    return [inverse[n] * factorial(n) % p for n in range(nmax + 1)]


def slow_power(base, exponent, modulus):
    # Deliberately different from built-in repeated-squaring exponentiation.
    result = 1
    for _ in range(exponent):
        result = result * base % modulus
    return result


def main():
    p, q, z = 37, 149, 16
    assert prime_by_trial_division(p) and prime_by_trial_division(q)
    assert q % p == 1 and z % q != 1 and pow(z, p, q) == 1
    zeta, half = pow(z, 2, q), pow(2, -1, p)
    assert zeta == 107 and half == 19
    assert pow(zeta, half, q) == z
    exact = bernoulli_rational(p - 3)
    residues = [int(b.numerator) * pow(int(b.denominator), -1, p) % p
                for b in exact]
    assert residues == bernoulli_by_series_mod_p(p - 3, p)
    irregular = [k for k in range(2, p - 2, 2) if residues[k] == 0]
    assert irregular == [32]
    print('p =', p, '; q =', q, '; zeta =', zeta, '; square root s =', z)
    print('Both p and q prime by trial division; zeta and s have exact order p mod q.')
    print('Corrected HHO normalization: half = 19 mod 37; zeta^half = s = 16 mod149.')
    print('Even Bernoulli residues B_2,...,B_34 mod 37:')
    print([residues[k] for k in range(2, p - 2, 2)])
    print('Irregular indices =', irregular)
    print('Bernoulli recurrence and independent series inversion agree.')
    for k in irregular:
        factors = [(pow(z, c, q) - pow(z, -c, q)) % q
                   for c in range(1, (p - 1) // 2 + 1)]
        corrected_factors = [
            (pow(zeta, half*c, q) - pow(zeta, -half*c, q)) % q
            for c in range(1, (p - 1) // 2 + 1)]
        assert corrected_factors == factors
        value = prod(pow(factor, c ** (p - 1 - k), q)
                     for c, factor in enumerate(factors, 1)) % q
        final_residue = pow(value, (q - 1) // p, q)
        # Reducing exponents mod p changes V by a pth power, so its
        # ((q-1)/p)th power is unchanged. Evaluate that power termwise.
        alternate = prod(slow_power(factor,
                                   ((q - 1) // p) * pow(c, p - 1 - k, p),
                                   q)
                         for c, factor in enumerate(factors, 1)) % q
        assert final_residue == alternate == 142
        assert value == 48 and final_residue != 1
        print('k =', k, '; factors =', factors)
        print('V =', value, '; V^((q-1)/p) mod q =', final_residue)
        print('Termwise repeated-multiplication check agrees.')
    print('PASS: the cited Vandiver criterion applies to p=37.')


if __name__ == '__main__':
    main()
