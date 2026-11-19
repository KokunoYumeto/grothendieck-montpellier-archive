"""Structural completeness check; not a mathematical proof test."""
import json,csv
from pathlib import Path
p=Path(__file__).resolve().parent
c=json.loads((p/'claims.json').read_text());i=json.loads((p/'items.json').read_text())
ps=json.loads((p/'problems.json').read_text());refs=json.loads((p/'reference_checks.json').read_text())
rk={x['key'] for x in refs}
logs=[json.loads(x) for x in (p/'search_log.jsonl').read_text().splitlines()]
ev=list(csv.DictReader((p/'check_events.tsv').open(),delimiter='\t'))
e=list(csv.DictReader((p/'entries.tsv').open(),delimiter='\t'))
assert (len(c),len(i),len(e),len(ps))==(74,53,53,23)
assert all(set(x['refs'])<=rk for x in c+ps)
assert len({x['id'] for x in c+i+ps})==len(c+i+ps)
searched={k for x in logs if x.get('query') for k in x.get('claim_ids',[])}
assert {x['id'] for x in c}<=searched
checked={x['statement_id'] for x in ev}
assert {x['id'] for x in c+i+ps}<=checked and rk<=checked
assert 'ALL ASSERTIONS PASSED' in (p/'computations/check_misc_output.txt').read_text()
assert '\x00' not in (p/'section.md').read_text()
print('ALL CORE INTEGRITY CHECKS PASSED')
print((p/'counts.json').read_text())
print('section_words',len((p/'section.md').read_text().split()))
print('directions',7)
