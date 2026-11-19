"""Finite exact checks for the separately proved completion counterexample."""
from time import perf_counter

started = perf_counter()

def valuation(n, prime):
    assert n != 0
    result = 0
    while n % prime == 0:
        n //= prime
        result += 1
    return result

print('M=C_lc(Z_3,Z), Fh(x)=h(x+1); completion C(Z_3,Z_3)')
for s in range(13):
    actual = valuation(pow(4, 3**s)-1, 3)
    assert actual == s+1
    print(f's={s}: v3(4^(3^s)-1)={actual}')

previous = None
for r in range(1, 11):
    modulus = 3**r
    period = 3**(r-1)
    values = [pow(4, x, modulus) for x in range(period)]
    assert values[0] == 1
    assert all(values[(x+1) % period] == (4*values[x]) % modulus
               for x in range(period))
    if previous is not None:
        old_modulus, old_values = previous
        assert all(values[x] % old_modulus == old_values[x % len(old_values)]
                   for x in range(period))
    print(f'r={r}: period={period}, modulus={modulus}, '
          'all eigenrelations and adjacent reductions checked, h_r(0)=1')
    previous = modulus, values

print('These finite checks accompany the written proof, not an inference of it.')
print('FROBENIUS_COMPLETION_CERTIFICATE_COMPLETE')
print(f'elapsed_seconds={perf_counter()-started:.6f}')
