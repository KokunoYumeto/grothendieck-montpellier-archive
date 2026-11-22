"""Correct prose spacing in the report generator; preserve mathematical content."""
from pathlib import Path
import datetime, hashlib, json, time
root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
path = root / 'code/write_report.py'
before = path.read_text()
changes = {
    'Bourbaki91': 'Bourbaki 91', 'June1957': 'June 1957',
    'printing is1966': 'printing is 1966', 'with1955 copyright': 'with 1955 copyright',
    'original1977': 'original 1977', 'the1956': 'the 1956', 'The1956': 'The 1956',
    'the150': 'the 150', 'cote1': 'cote 1', 'physical26': 'physical 26',
    'Physical2,3,4': 'Physical 2, 3, 4', 'pencil1,2,5': 'pencil 1, 2, 5',
    'footers1,2,3': 'footers 1, 2, 3', 'the1953': 'the 1953',
    'numbers as the1953': 'numbers as the 1953', 'before1959': 'before 1959',
    'PartA': 'Part A', 'conditionP': 'condition P', 'ICM1970': 'ICM 1970',
    'SGA6': 'SGA 6', 'separate1953': 'separate 1953',
    'Four-element dual numbers:64 triples,16 pairs;16 source and32 target':
    'Four-element dual numbers: 64 triples, 16 pairs; 16 source and 32 target',
    'algebra:64 Leibniz': 'algebra: 64 Leibniz',
    'All6 permutations,36 products,216': 'All 6 permutations, 36 products, 216',
    'algebra:512 associativity triples,64 coproduct products, all8':
    'algebra: 512 associativity triples, 64 coproduct products, all 8',
    'all3 affine': 'all 3 affine', 'basis{1}': 'basis {1}',
}
counts = {}
after = before
for old, new in changes.items():
    count = after.count(old)
    if count:
        counts[old] = count
        after = after.replace(old, new)
path.write_text(after)
record = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'changed_occurrences': counts, 'semantic_change': False,
          'before_sha256': hashlib.sha256(before.encode()).hexdigest(),
          'after_sha256': hashlib.sha256(after.encode()).hexdigest(),
          'elapsed_seconds': time.perf_counter() - started}
(root / 'logs/root_report_spacing04.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
