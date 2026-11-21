"""Freeze complete new model data and discover exact comparison factors."""
from pathlib import Path
from math import gcd
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
degrees = []
gcds = []
for k in (13, 15, 17):
    path = HERE / ('' if k == 13 else 'fast') / f'harmonic_k{k}_exact_exploration.json'
    data = json.loads(path.read_text())
    assert len(data['results']) == 2
    degrees.append(data)
    values = [r['comparison_value'] for r in data['results']]
    common = gcd(*values)
    factors = {str(q): int(a) for q, a in sp.factorint(common).items()}
    row = {'k': k, 'e': k+1, 'values': values, 'gcd': common,
           'factorization': factors, 'elapsed_seconds': data['elapsed_seconds']}
    gcds.append(row)
    print(json.dumps({'k': k, 'e': k+1, 'dimension': len(data['swap_signs']),
                      'elapsed_seconds': row['elapsed_seconds'],
                      'gcd_factors': factors}), flush=True)
    (HERE / 'u3_comparison_gcd_exploration.json').write_text(
        json.dumps(gcds, indent=2) + '\n')

# The unchanged model verifier is run with no factoring obligation. A
# separate recursive Lucas certificate checks these new integer gcds.
output = {'status': 'EXPLORATORY full next-weight model; exact replay pending',
          'degrees': degrees, 'comparison_gcds': []}
(HERE / 'harmonic_hecke_exact_data.json').write_text(json.dumps(output, indent=2)+'\n')
