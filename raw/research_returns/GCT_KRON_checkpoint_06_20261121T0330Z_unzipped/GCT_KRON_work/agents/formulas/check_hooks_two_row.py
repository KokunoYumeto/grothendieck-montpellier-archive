"""Independent Murnaghan--Nakayama checks of F-020 and overlap endpoints."""
from datetime import datetime, timezone
from pathlib import Path
import importlib.util
import json

work = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('independent_characters_for_f020',
                                            work / 'computations/independent_characters.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def predicted(N, k, e, f):
    if k == 0:
        return int(e == f)
    if k == 1:
        return int(abs(e - f) == 1) + int(e == f and 1 <= e <= N - 2)
    a = N - k
    return (int(e == f) * (int(k - 1 <= e <= a - 1) + int(k <= e <= a))
            + int(abs(e - f) == 1 and k - 1 <= min(e, f) <= a - 1))


rows = []
for N in range(1, 13):
    for k in range(N // 2 + 1):
        lam = (N,) if k == 0 else (N - k, k)
        for e in range(N):
            for f in range(e, N):
                left, right = (N - e,) + (1,) * e, (N - f,) + (1,) * f
                actual = module.kronecker(lam, left, right)
                expected = predicted(N, k, e, f)
                assert actual == expected, (N, k, e, f, actual, expected)
                rows.append({'N': N, 'k': k, 'e': e, 'f': f, 'coefficient': actual})

result = {'finding': 'F-020', 'date_utc': datetime.now(timezone.utc).isoformat(),
          'method': 'Independent Murnaghan–Nakayama character inner products',
          'checks': len(rows), 'maximum_N': 12, 'rows': rows,
          'printed_arxiv_overlap_counterexample': {'N': 4, 'k': 1, 'e': 1, 'f': 1,
                                                   'literal_printed_value': 2,
                                                   'character_value': 1},
          'status': 'PASS'}
destination = Path(__file__).with_name('hooks_two_row_certificate.json')
destination.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'checks': len(rows), 'maximum_N': 12,
                  'values': sorted({row['coefficient'] for row in rows})}))
