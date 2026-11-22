"""Repair observed bibliography prose spacing and audit explicit access flags."""
from pathlib import Path
import datetime, hashlib, json, re, time
root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
replacements = {
    'November20,2026': 'November 20, 2026',
    'Cote1': 'Cote 1', 'cote1': 'cote 1', 'under1953': 'under 1953',
    'dated1953': 'dated 1953', "catalogue's1953": "catalogue's 1953",
    'tag0ADV': 'tag 0ADV', 'tag0CMQ': 'tag 0CMQ',
    'Lemma80.11.3': 'Lemma 80.11.3', 'lines123,140': 'lines 123, 140',
    'pp.9,13,16': 'pp. 9, 13, 16', 'p.9 reproduces': 'p. 9 reproduces',
    'pp.34--35': 'pp. 34--35', 'parts1--3': 'parts 1--3',
    'section1': 'section 1', 'section2': 'section 2', 'section4': 'section 4',
    'Proposition1': 'Proposition 1', 'equations1--4': 'equations 1--4',
    'Theorem2': 'Theorem 2', 'Theorem4': 'Theorem 4',
    'note={Complete primary text extracted': 'note={Opened: complete primary text extracted',
}
changes = []
for path in sorted((root / 'notes').glob('*_references.bib')):
    before = path.read_text()
    after = before
    applied = {}
    for old, new in replacements.items():
        count = after.count(old)
        if count:
            applied[old] = count
            after = after.replace(old, new)
    if after != before:
        path.write_text(after)
        changes.append({'file': str(path.relative_to(root)), 'replacements': applied,
                        'before_sha256': hashlib.sha256(before.encode()).hexdigest(),
                        'after_sha256': hashlib.sha256(after.encode()).hexdigest()})
missing = []
for path in sorted((root / 'notes').glob('*_references.bib')):
    text = path.read_text()
    starts = list(re.finditer(r'(?m)^@\w+\s*\{\s*([^,\s]+)\s*,', text))
    for i, match in enumerate(starts):
        body = text[match.start():starts[i + 1].start() if i + 1 < len(starts) else len(text)]
        if 'opened' not in body.casefold():
            missing.append({'key': match.group(1), 'file': str(path.relative_to(root)), 'body': body})
record = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'changes': changes, 'entries_without_literal_opened_flag': missing,
          'elapsed_seconds': time.perf_counter() - started}
(root / 'logs/root_bibliography_spacing04.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
