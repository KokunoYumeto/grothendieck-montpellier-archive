"""Exact cyclotomic arithmetic in AM-K028; not a Hecke existence test."""
from pathlib import Path
from datetime import datetime, timezone
from math import gcd
import hashlib
import json

phi = [1, 3, 9, 15, 17, 23]
units = {a for a in range(28) if gcd(a, 28) == 1}
assert len(phi) == 6
assert set(phi).isdisjoint({-a % 28 for a in phi})
assert set(phi) | {-a % 28 for a in phi} == units
assert sum(phi) == 68
assert sum(phi) % 28 == 12
assert 28 // gcd(28, sum(phi)) == 7
assert sorted(a % 7 for a in phi) == [1, 1, 2, 2, 3, 3]
assert sum(a % 7 for a in phi) == 12
for n in range(-200, 201):
    assert ((68*n) % 28 == 0) == (n % 7 == 0)
for s in range(1, 401):
    assert ((6*s) % 7 == 0) == (s % 7 == 0)
for a in units:
    assert 28 // gcd(28, 12*a) == 7

alternative = [1, 9, 11, 15, 23, 25]
assert len(set(alternative)) == 6
assert set(alternative).isdisjoint({-a % 28 for a in alternative})
assert set(alternative) | {-a % 28 for a in alternative} == units
assert sum(alternative) == 84
assert sum(alternative) % 28 == 0
assert {a % 7 for a in alternative} == {1, 2, 4}

# 2 generates (Z/29)^*, and its order-four subgroup fixes a real degree7 field.
powers = [pow(2, i, 29) for i in range(28)]
assert len(set(powers)) == 28
subgroup = sorted(pow(2, 7*i, 29) for i in range(4))
assert subgroup == [1, 12, 17, 28]
assert 28 in subgroup

result = dict(
    result='PASS', checked_at=datetime.now(timezone.utc).isoformat(),
    scope='Finite exact CM-type residue sums, root orders, multiplicity congruences, alternative type and cyclic29 subgroup only; no character existence or full host theorem inferred.',
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    phi=phi, exponent_sum=sum(phi), root_order=7,
    alternative_type=alternative, alternative_sum=84,
    real_degree7_fixing_subgroup_mod29=subgroup,
)
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
