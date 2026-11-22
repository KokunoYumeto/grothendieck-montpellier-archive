from pathlib import Path
import csv, re, hashlib, time

started = time.monotonic()
root = Path('RESEARCH_SA23')
rows = list(csv.DictReader((root/'notes/category_results.csv').open()))
sections = list((root/'sections').glob('category_*.tex'))
text = '\n'.join(p.read_text() for p in sections)
labels = re.findall(r'\\label\{(cat:[^}]+)\}', text)
assert set(labels) == {row['id'] for row in rows}
assert len(labels) == len(set(labels)) == len(rows)
assert all((root/row['where_proved']).exists() for row in rows)
allowed = {'Known', 'Proved', 'Proved under stated hypotheses', 'Refuted'}
assert all(row['status'] in allowed for row in rows)
events = list(csv.DictReader((root/'notes/category_CHECK_EVENTS.tsv').open(), delimiter='\t'))
event_ids = {row['statement_id'] for row in events}
assert set(labels) <= event_ids
bib = (root/'notes/category_references.bib').read_text()
keys = set(re.findall(r'@\w+\{([^,]+),', bib))
cites = set()
for group in re.findall(r'\\cite(?:\[[^]]*\])*\{([^}]+)\}', text):
    cites.update(x.strip() for x in group.split(','))
assert cites <= keys, cites-keys
for p in sections:
    content = p.read_text()
    for env in ['theorem', 'proposition', 'lemma', 'proof', 'enumerate']:
        assert content.count('\\begin{'+env+'}') == content.count('\\end{'+env+'}'), (p, env)
print('statement rows', len(rows), 'matching unique labels', len(labels))
print('statuses', sorted({row['status'] for row in rows}))
print('all statements have check events; all cited bibliography keys present; environments balanced')
for p in sections:
    print(p.name, p.stat().st_size, hashlib.sha256(p.read_bytes()).hexdigest())
print('seconds', time.monotonic()-started)
