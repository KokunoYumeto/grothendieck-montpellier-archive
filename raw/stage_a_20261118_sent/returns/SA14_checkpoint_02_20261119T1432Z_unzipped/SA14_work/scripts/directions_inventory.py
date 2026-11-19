"""Save a compact, reproducible inventory used to select final research directions."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
out = root / 'outputs' / 'directions_inventory.txt'
lines = []
for kind in ('claims', 'problems'):
    lines.append(f'ROOT {kind.upper()}')
    records = json.loads((root / 'parts' / 'root' / f'{kind}.json').read_text())
    for record in records:
        label = record.get('title') or record.get('modern_statement') or record.get('statement') or record.get('his_statement') or ''
        lines.append(f"{record['id']} | {label}")
lines.append('COTE60 CLASS-A ENDPOINT RECORDS')
claims = json.loads((root / 'parts' / 'lfunctions' / 'claims.json').read_text())
for record in claims:
    if record['id'] in {f'C-SA14-{n}' for n in (413,414,417,428,444,447)}:
        lines.append(json.dumps(record, ensure_ascii=False, indent=2))
out.write_text('\n'.join(lines) + '\n')
print(f'Saved {out}; {len(records)} root problems and six endpoint records included.')
