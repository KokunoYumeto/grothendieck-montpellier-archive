"""Independent character checks for the known rectangular square F-019."""
from pathlib import Path
from datetime import datetime, timezone
import importlib.util
import json

work = Path(__file__).resolve().parents[2]
source = work / 'computations/independent_characters.py'
spec = importlib.util.spec_from_file_location('independent_characters_for_f019', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
rows = []
for h in range(1, 7):
    for nu in module.partitions(2 * h):
        padded = tuple(nu) + (0,) * max(0, 4 - len(nu))
        expected = int(len(nu) <= 4 and len({a % 2 for a in padded}) == 1)
        actual = module.kronecker(tuple(nu), (h, h), (h, h))
        assert actual == expected, (h, nu, actual, expected)
        rows.append({'h': h, 'nu': nu, 'coefficient': actual})
result = {'finding': 'F-019', 'date_utc': datetime.now(timezone.utc).isoformat(),
          'method': 'Independent Murnaghan–Nakayama character inner product',
          'checks': len(rows), 'rows': rows, 'status': 'PASS'}
destination = Path(__file__).with_name('rectangle_square_certificate.json')
destination.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'checks': len(rows),
                  'maximum_symmetric_group_degree': 12}))
