"""Exact arithmetic only for AM-K027; not a display or theta verification."""
from fractions import Fraction
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json


def digit_length(n, p=11):
    assert n >= 0
    ans = 0
    while n:
        n //= p
        ans += 1
    return ans


def digit_sum(n, p=11):
    assert n >= 0
    ans = 0
    while n:
        n, rem = divmod(n, p)
        ans += rem
    return ans


def factorial_value(n, p=11):
    total = 0
    while n:
        n //= p
        total += n
    return total


def ceil_fraction(x):
    return -((-x.numerator) // x.denominator)


k, m, d = 6, 2, 1796
S = k + m - 1 + m * (d - 1)
Q = S**3 + 2
assert Q == 46539457175
expected = [
    (1675420458300, 1372581866, 1373293082, 167542045704),
    (1008044642410500, 825838183001, 826051784873, 100804464197676),
]
records = []
for j in range(m):
    a, b = k + j*d, k + (j+1)*d
    nu = [Q*(2*j+1)]*k
    for h in range(j, 0, -1):
        nu += [2*h*Q]*d
    assert len(nu) == a
    assert set(map(digit_length, nu)) == {11}
    D = 6*sum(nu)
    row_error = 6*b*sum(map(digit_length, nu))
    highest_error = 6*a*sum(map(digit_length, nu))
    row_lower = ceil_fraction(Fraction(D, 1220) - row_error)
    highest_lower = ceil_fraction(Fraction(D, 1220) - highest_error)
    Rj = k*j + d*j*(j+1)//2
    upper = 6*k*factorial_value(Q) + 6*Rj*factorial_value(2*Q)
    assert (D, row_lower, highest_lower, upper) == expected[j]
    assert 0 < row_lower <= highest_lower <= upper
    records.append(dict(j=j, a=a, b=b, degree=D,
                        selected_row_digit_error=row_error,
                        highest_digit_error=highest_error,
                        selected_row_lower=row_lower,
                        highest_lower=highest_lower,
                        highest_upper=upper))

# Independent exact Legendre and growing-degree normalization checks.
for n in range(3000):
    assert factorial_value(n) == (n-digit_sum(n))//10
for D0, c0 in [(1, 0), (36, 0), (1675420458300, 167542045704)]:
    for r in range(30):
        T = 122*11**r + D0
        upper = Fraction(11**r-1, 10) + c0
        assert upper - Fraction(T, 1220) == c0-Fraction(1, 10)-Fraction(D0, 1220)

result = dict(
    result="PASS",
    checked_at=datetime.now(timezone.utc).isoformat(),
    scope="Exact baseline degree/digit/factorial bounds and normalization identities only; no theta, display, or asymptotic theorem inferred from finite tests.",
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    Q=Q,
    records=records,
    exact_legendre_cases=3000,
    exact_normalization_cases=90,
)
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
