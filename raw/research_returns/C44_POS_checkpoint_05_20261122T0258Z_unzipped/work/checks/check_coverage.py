"""Register and assembly consistency only; this script is not a proof check."""
from pathlib import Path
import csv
import datetime
import hashlib
import json
import re

root = Path(__file__).resolve().parents[2]
paper = (root / 'deliverables/C44_POS.tex').read_text()
events = list(csv.DictReader((root / 'deliverables/CHECK_EVENTS.tsv').open(), delimiter='\t'))
ids = set(re.findall(r'C44-[A-Z]+[0-9]+[a-z]?', paper))
def expand(label):
    answer = set(re.findall(r'C44-[A-Z]+[0-9]+[a-z]?', label))
    if 'C44-' in label:
        answer.update('C44-' + s for s in re.findall(r'(?<=[/ ,;])[A-Z]+[0-9]+[a-z]?', label))
    return answer
covered = set().union(*(expand(e['statement_id']) for e in events))
manifest = json.loads((root / 'work/assembly_manifest.json').read_text())
changes = []
for entry in manifest['parts']:
    path = root / entry['path']
    current = hashlib.sha256(path.read_bytes()).hexdigest()
    if current != entry['sha256']:
        changes.append({'path': entry['path'], 'assembled': entry['sha256'], 'current': current})
result = {
    'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope': 'Identifier coverage and assembled-source hashes only; not mathematical verification.',
    'ids': sorted(ids), 'missing': sorted(ids - covered),
    'assembled_source_changes': changes, 'events': len(events),
}
(root / 'work/checks/coverage_audit.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'ids': len(ids), 'missing': result['missing'], 'assembled_source_changes': changes, 'events': len(events)}))
if result['missing'] or changes:
    raise SystemExit(1)
