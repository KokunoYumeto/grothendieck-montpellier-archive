"""Normalize event labels to the user's vocabulary without upgrading scope."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
MAP = {
    'argeted proof check': 'targeted proof check',
    'complete written-proof check': 'targeted proof check',
    'independent proof reading': 'targeted proof check',
    'documentary snapshot comparison': 'used and rechecked in this run',
    'inherited-source interface recheck': 'used and rechecked in this run',
    'primary-source interface and locator check': 'used and rechecked in this run',
    'primary-source interface recheck': 'used and rechecked in this run',
    'primary-source scope check': 'used and rechecked in this run',
    'primary-source statement and interface check': 'used and rechecked in this run',
    'source check': 'used and rechecked in this run',
    'targeted primary-source table and locator check': 'used and rechecked in this run',
    'primary theorem statement and counting-interface check': 'used and rechecked in this run',
    'primary-source and normalization interface recheck': 'used and rechecked in this run',
    'primary-source topology and field-generality check': 'used and rechecked in this run',
    'targeted independent dual-phase and finite-factor calculation': 'targeted proof check',
}
changes = []
for path in sorted((ROOT / 'modules').glob('*events.tsv')):
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        fields, rows = reader.fieldnames, list(reader)
    changed = False
    for row in rows:
        previous = row.get('type')
        if previous not in MAP:
            continue
        row['type'] = MAP[previous]
        if 'method' in row:
            row['method'] = ('Original descriptive event label: ' + previous
                             + '. ' + row['method'])
        changes.append({'event_file': str(path.relative_to(ROOT)),
                        'statement_id': row.get('statement_id'),
                        'date': row.get('date', row.get('date_utc')),
                        'previous_label': previous, 'canonical_label': MAP[previous]})
        changed = True
    if changed:
        with path.open('w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t',
                                    lineterminator='\n')
            writer.writeheader()
            writer.writerows(rows)

report_path = ROOT / 'checks' / 'event_type_normalization.json'
report = json.loads(report_path.read_text()) if report_path.exists() else []
report.append({'timestamp_utc': datetime.now(timezone.utc).isoformat(),
               'scope': 'Vocabulary normalization only. No event is upgraded to an independent re-proof; original descriptions, methods, outcomes and provenance are retained.',
               'changes': changes})
report_path.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'normalized_events': len(changes),
                  'event_files': len({x['event_file'] for x in changes}),
                  'report': str(report_path)}))
