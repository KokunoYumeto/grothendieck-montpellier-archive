"""Discovery of recursive Lucas witnesses; verification is separate."""
from pathlib import Path
from math import gcd
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
targets = set()
for name in ('u3_comparison_gcd_exploration.json', 'combined_exploration.json'):
    for row in json.loads((HERE/name).read_text()):
        targets.update(map(int, row['factorization']))
nodes = {}


def build(n):
    if n in nodes:
        return
    if n == 2:
        nodes[n] = {'n': 2, 'factors_n_minus_1': {}, 'witness': None}
        return
    factors = {int(q): int(a) for q, a in sp.factorint(n-1).items()}
    for q in factors:
        build(q)
    for witness in range(2, n):
        if pow(witness, n-1, n) == 1 and all(
                gcd(pow(witness, (n-1)//q, n)-1, n) == 1 for q in factors):
            nodes[n] = {'n': n, 'factors_n_minus_1': factors, 'witness': witness}
            return
    raise ValueError('No Lucas witness')


for n in sorted(targets):
    build(n)
out = {'targets': sorted(targets), 'nodes': [nodes[n] for n in sorted(nodes)]}
(HERE/'prime_certificates.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'targets': len(targets), 'recursive_nodes': len(nodes),
                  'largest_target': max(targets)}))
