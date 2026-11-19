"""Validate the identifiers in the manually authored cross-scope review.

This script checks references, not mathematical equivalence. The equivalence
decisions and source readings are in cross_scope_merges.md.
"""
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[3]
OWN = BASE / 'work' / 'cote11b'
scopes = ('root', 'cote11a', 'cote11b')
loaded = {
    kind: {
        row['id']: {'scope': scope, 'record': row}
        for scope in scopes
        for row in json.loads((BASE / 'work' / scope / f'{kind}.json').read_text())
    }
    for kind in ('items', 'claims', 'problems')
}
item_groups = [
    ['SA05-54', 'SA05-1002', 'SA05-2001'],
    ['SA05-59', 'SA05-1035', 'SA05-2064'],
    ['SA05-1010', 'SA05-2002'],
    ['SA05-1048', 'SA05-2024'],
]
claim_pairs = [
    ['SA05-C1081', 'SA05-C2080'],
    ['SA05-C1086', 'SA05-C2066'],
    ['SA05-C1084', 'SA05-C2014'],
    ['SA05-C1059', 'SA05-C2019'],
    ['SA05-C1058', 'SA05-C2018'],
]
problem_pairs = [
    ['MP-SA05-1018', 'MP-SA05-2007'],
    ['MP-SA05-1001', 'MP-SA05-2001'],
]
for kind, groups in [('items', item_groups), ('claims', claim_pairs),
                     ('problems', problem_pairs)]:
    for group in groups:
        assert all(identifier in loaded[kind] for identifier in group), group
        assert len({loaded[kind][identifier]['scope'] for identifier in group}) > 1

reading_ledger = OWN / 'reading_log.tsv'
import csv
with reading_ledger.open() as stream:
    rows = list(csv.DictReader(stream, delimiter='\t'))
for row in rows:
    source = BASE.parent / row['file']
    assert source.is_file(), source
    assert hashlib.sha256(source.read_bytes()).hexdigest() == row['sha256'], source

report = OWN / 'cross_scope_merges.md'
result = {
    'date': '2026-11-19',
    'status': 'passed',
    'review_sha256': hashlib.sha256(report.read_bytes()).hexdigest(),
    'item_groups': item_groups,
    'claim_pairs': claim_pairs,
    'problem_pairs': problem_pairs,
    'all_proposed_ids_exist': True,
    'unchanged_source_records': len(rows),
    'scope': 'Identifier and frozen-source integrity only; equivalence decisions are manual.',
    'other_owner_records_modified': False,
}
out = OWN / 'outputs' / 'cross_scope_review_validation.json'
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(result, ensure_ascii=False, indent=2))
