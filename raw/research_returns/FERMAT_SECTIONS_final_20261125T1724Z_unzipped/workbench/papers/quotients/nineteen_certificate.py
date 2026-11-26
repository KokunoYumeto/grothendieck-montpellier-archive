"""Certified nineteenth-exponent central derivative.

Run the companion exact CM witness replay first. This program uses integer
Euler coefficients, Arb contour integrals and explicit absolute tails only.
The proof and exact root-number convention are in the companion paper.
"""
from pathlib import Path
import argparse, hashlib, json, math, time
from flint import arb, acb, ctx

BASE = Path(__file__).resolve().parent

def sieve(limit):
    spf = list(range(limit+1))
    for p in range(2, math.isqrt(limit)+1):
        if spf[p] == p:
            for n in range(p*p, limit+1, p):
                if spf[n] == n:
                    spf[n] = p
    return [p for p in range(2, limit+1) if spf[p] == p], spf

def order19(p):
    r, f = p % 19, 1
    while r != 1:
        r = r*p % 19
        f += 1
    return f

def quadratic_trace(p):
    choices = []
    for b in range(math.isqrt(4*p//19)+1):
        square = 4*p-19*b*b
        a = math.isqrt(square)
        if a*a == square and (a-b) % 2 == 0:
            for signed in {a, -a}:
                if (p*signed*10-pow(p, 6, 19)) % 19 == 0:
                    choices.append(signed*p)
    assert len(set(choices)) == 1, (p, choices)
    return choices[0]

def coefficients(limit, split_file):
    primes, spf = sieve(limit)
    splits = {}
    for line in split_file.read_text().splitlines():
        p, polynomial, witness = json.loads(line)
        assert p not in splits and len(polynomial) == 7
        assert polynomial[0] == 1 and polynomial[-1] == p**3
        splits[p] = polynomial
    assert set(splits) == {p for p in primes if p % 19 in (1, 7, 11)}
    prime_powers, locals_ = {}, {}
    for p in primes:
        power, exponent = p, 0
        while power <= limit:
            exponent += 1
            power *= p
        if p == 19:
            polynomial, order = [1], None
        else:
            order = order19(p)
            if order in (1, 3):
                polynomial = splits[p]
            elif order in (2, 6):
                polynomial = [1, 0, 3*p, 0, 3*p*p, 0, p**3]
            elif order == 18:
                polynomial = [1, 0, 0, 0, 0, 0, p**3]
            else:
                assert order == 9
                polynomial = ([1, 0, 0, -quadratic_trace(p), 0, 0, p**3]
                              if exponent >= 3 else [1])
        inverse = [1]
        for d in range(1, exponent+1):
            inverse.append(-sum(polynomial[j]*inverse[d-j]
                                for j in range(1, min(d, len(polynomial)-1)+1)))
        prime_powers[p] = inverse
        if any(inverse[1:]):
            locals_[str(p)] = {'order_mod19': order, 'Euler_polynomial': polynomial}
    coefficients_ = [0]*(limit+1)
    coefficients_[1] = 1
    for n in range(2, limit+1):
        p, m, e = spf[n], n, 0
        while m % p == 0:
            m //= p
            e += 1
        coefficients_[n] = coefficients_[m]*prime_powers[p][e]
    assert all(not coefficients_[n] for n in range(1, limit+1) if n % 19 not in (1, 7, 11))
    return {'limit': limit, 'local_factors': locals_,
            'nonzero_coefficients': [(n, a) for n, a in enumerate(coefficients_) if a],
            'split_file_sha256': hashlib.sha256(split_file.read_bytes()).hexdigest()}

def root_number():
    ninth = acb(0, 2*arb.pi()/9).exp()
    answer = acb(0)
    for j in range(18):
        u = pow(2, j, 19)
        sign = 1 if pow(u, 9, 19) == 1 else -1
        answer += sign*ninth**(6*j)*acb(0, 2*arb.pi()*6*u/19).exp()
    answer *= acb(0, 1)/arb(19).sqrt()
    assert (answer*answer.conjugate()).real.contains(1)
    return answer

def zeta_cm(sigma):
    # The degree-six field has characters chi_(3j), j=0,...,5 modulo19.
    eighteenth = acb(0, 2*arb.pi()/18).exp()
    answer = acb(sigma.zeta())
    for k in (3, 6, 9, 12, 15):
        value = sum((eighteenth**(k*j)*acb(sigma).zeta(arb(pow(2, j, 19))/19)
                     for j in range(18)), acb(0))/acb(19)**sigma
        answer *= value
    assert answer.imag.contains(0)
    return answer.real

def certificate(data, precision):
    ctx.prec = precision
    B = (arb(19)/(2*arb.pi()))**3
    logB = B.log()
    discrete_log = {pow(2, j, 19): j for j in range(18)}
    ninth = acb(0, 2*arb.pi()/9).exp()
    terms = [(arb(a)/arb(n)**3, arb(n).log(), ninth**discrete_log[n % 19])
             for n, a in data['nonzero_coefficients']]
    imaginary = acb(0, 1)
    def derivative_integrand(t, analytic):
        it = imaginary*t
        z = 2+it
        total = sum((w*(-it*ln).exp() for w, ln, chi in terms), acb(0))
        return (z+1).gamma()**3/z**2*B**2*(it*logB).exp()*total
    def twist_integrand(t, analytic):
        it = imaginary*t
        zp, zm = 2+it, 2-it
        plus, minus = acb(0), acb(0)
        for weight, logarithm, chi in terms:
            exponential = (-it*logarithm).exp()
            plus += weight*chi*exponential
            minus += weight*chi/exponential
        return ((zp+1).gamma()**3/zp*B**2*(it*logB).exp()*plus
                +(zm+1).gamma()**3/zm*B**2*(-it*logB).exp()*minus)
    derivative_integral, twist_integral = acb(0), acb(0)
    for j in range(24):
        derivative_integral += acb.integral(derivative_integrand, j, j+1,
            abs_tol=arb('1e-13'), rel_tol=arb('1e-13'), eval_limit=30000)
        twist_integral += acb.integral(twist_integrand, j, j+1,
            abs_tol=arb('1e-13'), rel_tol=arb('1e-13'), eval_limit=30000)
        print(json.dumps({'interval': j, 'derivative_partial': str(2/arb.pi()*derivative_integral.real),
                          'twist_half_partial': str(twist_integral/(2*arb.pi()))}), flush=True)
    derivative_truncated = 2/arb.pi()*derivative_integral.real
    first_truncated = twist_integral/(2*arb.pi())
    S = sum(abs(w) for w, ln, chi in terms)
    m, T = 16, arb(24)
    gamma_bound = arb(3+m).gamma()**3
    vertical_half = B**2*S*gamma_bound/(arb.pi()*3*m*T**(3*m))
    vertical_derivative = 2*B**2*S*gamma_bound/(arb.pi()*(3*m+1)*T**(3*m+1))
    sigma, k = arb(11)/10, 4
    zeta = zeta_cm(sigma)
    coefficient_half = arb(k+1).gamma()**3*B**k*arb(data['limit'])**(sigma-k-arb(1)/2)*zeta
    coefficient_derivative = 2*coefficient_half/k
    first_error = (vertical_half+coefficient_half).upper()
    first = first_truncated+acb(arb(0, first_error), arb(0, first_error))
    derivative = derivative_truncated+arb(0, (vertical_derivative+coefficient_derivative).upper())
    w = root_number()
    central = first+w*first.conjugate()
    norm_squared = (central*central.conjugate()).real
    product = derivative*norm_squared
    return {'arithmetic_mode': 'Arb integration and explicit absolute tails', 'precision': precision,
            'coefficient_count': len(terms), 'scale': str(B), 'root_number_exact_enclosure': str(w),
            'zeta_CM_1p1': str(zeta), 'derivative_truncated': str(derivative_truncated),
            'twist_half_truncated': str(first_truncated), 'vertical_half_bound': str(vertical_half),
            'vertical_derivative_bound': str(vertical_derivative),
            'coefficient_half_bound': str(coefficient_half),
            'coefficient_derivative_bound': str(coefficient_derivative),
            'A_derivative_interval': str(derivative), 'twist_central_interval': str(central),
            'twist_norm_squared_interval': str(norm_squared),
            'J_derivative_product_interval': str(product),
            'positive_product': bool(product > 0)}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=16384)
    parser.add_argument('--split-file', type=Path, default=BASE/'nineteen_split_witnesses.txt')
    parser.add_argument('--output', type=Path, default=BASE/'nineteen_certificate.json')
    parser.add_argument('--precision', type=int, default=128)
    args = parser.parse_args()
    started = time.time()
    ctx.prec = args.precision
    data = coefficients(args.limit, args.split_file)
    data['certificate'] = certificate(data, args.precision)
    assert data['certificate']['positive_product'], 'Positive derivative not certified'
    data['elapsed_seconds'] = time.time()-started
    args.output.write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps({key: value for key, value in data.items()
                      if key not in ('local_factors', 'nonzero_coefficients')}, indent=2))
