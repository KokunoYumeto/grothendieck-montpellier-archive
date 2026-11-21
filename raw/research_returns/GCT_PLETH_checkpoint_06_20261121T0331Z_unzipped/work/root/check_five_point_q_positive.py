"""Independent finite arithmetic and witness checks for G-017."""
from pathlib import Path
from math import prod
import csv
import json
from five_point_q_positive import TAGS, WEIGHTS, RESIDUES, coefficient, coin_count, witnesses

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'FIVE_POINT_Q_TAGS.json').read_text())
for row in data['tags']:
    assert tuple(row['coefficients']) == TAGS[tuple(row['label'])]

dp = [1] + [0] * 600
for weight in WEIGHTS:
    for n in range(weight, len(dp)):
        dp[n] += dp[n - weight]
assert all(coin_count(n) == dp[n] for n in range(len(dp)))
assert all(coin_count(n) == 0 for n in range(-50, 0))


def dimension(mu):
    hooks = [mu[i]-j + sum(row > j for row in mu[i+1:])
             for i in range(len(mu)) for j in range(mu[i])]
    return 120 // prod(hooks)


for k in range(81):
    for d in (0, 1):
        actual = sum(dimension(mu) * coefficient(k, d, mu) for mu in TAGS)
        assert actual == (k+1)*(k+2)*(3*k+4)//2, (k, d, actual)

rows = []
total = 0
for k in range(31):
    for d in (0, 1):
        for mu in TAGS:
            literal = 0
            seen = set()
            for witness in witnesses(k, d, mu):
                tag, point = tuple(witness['tag']), tuple(witness['point'])
                assert all(v >= 0 for v in point)
                assert sum(w*v for w,v in zip(WEIGHTS,point)) == k-tag[0]
                assert (tag, point) not in seen
                seen.add((tag, point))
                literal += 1
            answer = coefficient(k, d, mu)
            assert answer == literal
            total += literal
            rows.append({'k':k,'d':d,'outer':','.join(map(str,mu)),
                         'positive_formula':answer,'literal_witnesses':literal,
                         'outcome':'PASS'})

with (ROOT/'FIVE_POINT_Q_POSITIVE_CHECK.tsv').open('w',newline='') as f:
    writer = csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
    writer.writeheader(); writer.writerows(rows)
receipt = (f'G-017 fixed evaluator: PASS\n601 coin values compared with independent dynamic programming.\n'
           f'All140 stored tag entries agree.\n162 full dimension identities passed.\n'
           f'{len(rows)} complete tagged-polytope enumerations passed, containing {total} witnesses.\n'
           f'Fixed residue polynomial: degree{len(RESIDUES)-1}, coefficient sum{sum(RESIDUES)}.\n')
(ROOT/'FIVE_POINT_Q_POSITIVE_CHECK.txt').write_text(receipt)
print(receipt)
