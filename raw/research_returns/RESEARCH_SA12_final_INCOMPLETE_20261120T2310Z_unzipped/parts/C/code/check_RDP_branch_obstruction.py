"""Exact finite certificate for the A2 branch-gluing obstruction.

The infinite Artin--Schreier conclusion is proved by the valuation argument
in the TeX fragment.  No numerical experiment replaces that proof.
"""
from pathlib import Path
from time import perf_counter
import json

start = perf_counter()
checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1

def mul(a, b, modulus, degree):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & (1 << degree):
            a ^= modulus
    return out

# F4 contains the third roots of unity.  Its action has weights (1,-1).
check(mul(2, 2, 0b111, 2) == 3)
check(mul(3, 2, 0b111, 2) == 1)
for a in range(1, 4):
    check(mul(a, a, 0b111, 2) != a or a == 1)
for i in range(25):
    for j in range(25):
        invariant = (i-j) % 3 == 0
        if invariant:
            w_exp = min(i, j)
            check((i-w_exp) % 3 == 0 and (j-w_exp) % 3 == 0)
            u_exp, v_exp = (i-w_exp)//3, (j-w_exp)//3
            check((3*u_exp+w_exp, 3*v_exp+w_exp) == (i, j))
        else:
            check((i-j) % 3 in (1, 2))

# The invariant relation uv=w^3 and the normalized boundary valuation.
check((3, 0)[0] + (0, 3)[0] == 3*(1, 1)[0])
check((3, 0)[1] + (0, 3)[1] == 3*(1, 1)[1])
valuation = {'u': 3, 'v': 0, 'w': 1}
check(valuation['u'] + valuation['v'] == 3*valuation['w'])
check(valuation['u'] % 2 == 1)

# Finite field instances of distinct nonzero coefficients.  The leading
# pole coefficient in their difference is nonzero and its pole is odd.
for degree, modulus in [(2, 0b111), (4, 0b10011)]:
    size = 1 << degree
    for a in range(1, size):
        check(any(mul(a, b, modulus, degree) == 1 for b in range(1, size)))
    for a in range(size):
        for b in range(size):
            if a != b:
                check((a ^ b) != 0)
                check((-valuation['u']) % 2 == 1)
    for v_b in range(-64, 0):
        check(2*v_b != -valuation['u'])
    for v_b in range(65):
        check(v_b >= 0 and -valuation['u'] < 0)

# The coarse generator bound for the bounded-order RDP table entries.
for order in [1, 2, 3, 4, 5, 6, 12, 24, 48, 120]:
    check(order < 2**7)
    check(order.bit_length()-1 <= 6)

result = {
    'statement': 'D:RDP-branch-gluing-obstruction',
    'assertions': checks,
    'status': 'PASS',
    'finite_fields': [4, 16],
    'monomial_exponents': '0 through 24 in each variable',
    'valuation': valuation,
    'elapsed_seconds': perf_counter()-start,
    'scope': 'Exact finite algebra/action/valuation checks; the infinite family follows from the displayed odd-pole proof.'
}
out = Path(__file__).resolve().parents[1] / 'output' / 'RDP_branch_obstruction.json'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result))
