"""Exact unit-group checks used in A15; no theta-incidence assertion."""
from math import gcd
from pathlib import Path
import json


def check(n):
    assert n > 1 and n % 2
    units = {a for a in range(n) if gcd(a, n) == 1}
    powers = []
    a = 1
    while a not in powers:
        powers.append(a)
        a = 2*a % n
    assert a == 1
    generated = set(powers) | {(-a) % n for a in powers}
    assert generated <= units
    # Independent finite closure, rather than relying only on the union.
    closure, frontier = {1}, [1]
    while frontier:
        a = frontier.pop()
        for b in (2*a % n, -a % n):
            if b not in closure:
                closure.add(b)
                frontier.append(b)
    assert closure == generated
    return dict(n=n, phi=len(units), order_of_2=len(powers),
                minus_one_in_powers_of_2=n-1 in powers,
                generated_size=len(generated),
                generates_all_units=generated == units,
                powers_of_2=powers, generated_residues=sorted(generated))


rows = [check(n) for n in (15, 21, 35, 45, 33, 105)]
assert [r['generates_all_units'] for r in rows] == [True]*4 + [False]*2
result = {'status': 'PASS', 'scope': 'unit groups only; no theta search',
          'checks': rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
