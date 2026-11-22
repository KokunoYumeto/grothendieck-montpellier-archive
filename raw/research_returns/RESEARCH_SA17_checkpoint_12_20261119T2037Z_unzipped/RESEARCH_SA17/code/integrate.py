"""Merge the research components; preserve all component audit records.

Run from any directory. This is packaging only, not mathematical verification.
"""
from pathlib import Path
import csv, json, re, time
from datetime import datetime, timezone

start = time.perf_counter()
root = Path(__file__).resolve().parents[1]
for name, pattern, delimiter in [
    ('RESEARCH_SA17_results.csv', 'results_*.csv', ','),
    ('CHECK_EVENTS.tsv', 'checks_*.tsv', '\t'),
]:
    files = sorted(root.glob(pattern))
    rows, fields = [], None
    for file in files:
        with file.open(newline='') as stream:
            reader = csv.DictReader(stream, delimiter=delimiter)
            if fields is None:
                fields = reader.fieldnames
            assert fields == reader.fieldnames, (file, fields, reader.fieldnames)
            rows.extend(reader)
    with (root/name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(rows)

bibliographies = sorted((root/'references').glob('*.bib'))
bibtext = '\n\n'.join(p.read_text() for p in bibliographies)
keys = re.findall(r'@\w+\s*\{\s*([^,]+),', bibtext)
assert len(keys) == len(set(keys)), 'Duplicate bibliography keys'
(root/'RESEARCH_SA17_references.bib').write_text(bibtext)
labels = {}
for path in sorted((root/'sections').glob('*.tex')):
    for label in re.findall(r'\\label\{([^}]+)\}', path.read_text()):
        assert label not in labels, ('duplicate label', label)
        labels[label] = str(path.relative_to(root))
result = {
    'timestamp': datetime.now(timezone.utc).isoformat(),
    'scope': 'metadata merge and duplicate-key checks only',
    'bibliography_entries': len(keys),
    'latex_labels': len(labels),
    'seconds': time.perf_counter()-start,
}
(root/'logs/integration.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result))
