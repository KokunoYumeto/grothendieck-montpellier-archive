"""Two exact expansions of one residue-kernel coefficient; no prime scan."""
from math import comb, isqrt
from pathlib import Path
import hashlib
import json

N = 10


def mul(a, b):
    c = [0] * (N + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b[:N + 1 - i]):
            c[i + j] += x * y
    return c


def power(a, n):
    c = [1] + [0] * N
    for _ in range(n):
        c = mul(c, a)
    return c


def inv(a):
    assert a[0] == 1
    b = [1] + [0] * N
    for n in range(1, N + 1):
        b[n] = -sum(a[j] * b[n - j] for j in range(1, n + 1))
    return b


theta = [1] + [0] * N
for j in range(1, isqrt(N) + 1):
    theta[j * j] = 2
eta = [1] + [0] * N
for k in range(1, N // 2 + 1):
    a = [0] * (N + 1)
    for j in range(min(12, N // (2 * k)) + 1):
        a[2 * k * j] = (-1) ** j * comb(12, j)
    eta = mul(eta, a)
ratio = mul(eta, inv(power(theta, 12)))
first = [0] + [-4096 * x for x in ratio[:N]]

# Independent cusp calculation from R=256(2-T)/(T-1)^2,
# T=G/Theta, G|A=G, and Theta|A=16q(1+q^2+q^6+...)^4.
odd = [0] * (N + 1)
for j in range(N + 1):
    if j * (j + 1) <= N:
        odd[j * (j + 1)] = 1
ThetaA = [0] + [16 * x for x in power(odd, 4)[:N]]
sigma = lambda n: sum(d for d in range(1, n + 1) if n % d == 0)
G = [1] + [24 * sigma(n) - (48 * sigma(n // 2) if n % 2 == 0 else 0)
           for n in range(1, N + 1)]
numerator = [256 * x for x in mul(ThetaA, [2 * x - y for x, y in zip(ThetaA, G)])]
denominator = power([x - y for x, y in zip(G, ThetaA)], 2)
second = mul(numerator, inv(denominator))
assert first == second
assert first[10] == 166601228288 and first[10] % 83 == 26
assert 83 - 4 * 10 == 43 and 166 % 83 == 0
report = {
    'finding_id': 'KT-WEIGHT-TWO-KERNEL-NONFACTORIZATION',
    'p': 83, 'D': -43, 'j': 10,
    'kernel_coefficients_q0_to_q10': first,
    'independent_expansions_equal': True,
    'kernel_q10': first[10], 'kernel_q10_mod83': first[10] % 83,
    'beta3_exact_imported_from_checked_p83_certificate': 166,
    'beta3_mod83': 0,
    'scope': 'This particular residue kernel does not vanish on the third-value zero set. No universal nonexistence or simultaneous-unit conclusion.',
    'status': 'PASS',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
