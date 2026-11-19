#!/usr/bin/env python3
"""Export the explicit source-access notes; infer no unrecorded opening."""
from pathlib import Path
import csv
import re

out = Path(__file__).resolve().parent.parent
text = (out / 'RESEARCH_SA07_references.bib').read_text()

def field(entry, name):
    match = re.search(r'\b' + re.escape(name) + r'\s*=\s*\{', entry, re.I)
    if not match:
        return ''
    start = match.end()
    depth = 1
    for i in range(start, len(entry)):
        if entry[i] == '{' and (i == 0 or entry[i-1] != '\\'):
            depth += 1
        elif entry[i] == '}' and (i == 0 or entry[i-1] != '\\'):
            depth -= 1
            if depth == 0:
                return re.sub(r'\s+', ' ', entry[start:i]).strip()
    raise ValueError('Unbalanced field: ' + name)

rows = []
for entry in re.split(r'(?=@\w+\s*\{)', text):
    key = re.match(r'@\w+\s*\{\s*([^,]+),', entry)
    if not key:
        continue
    note = field(entry, 'note')
    low = note.lower()
    if 'partly opened' in low or 'not obtained' in low and 'opened' in low:
        status = 'PARTLY OPENED; requested missing portion explicitly recorded'
    elif 'not obtained' in low or 'not opened' in low:
        status = 'NOT OBTAINED'
    elif 'opened' in low:
        status = 'OPENED at the recorded locators'
    else:
        status = 'ACCESS STATUS STILL REQUIRES EXPLICIT RECORD'
    rows.append([key.group(1), field(entry, 'author'), field(entry, 'title'),
                 field(entry, 'year'), status, field(entry, 'url'), note])

with (out / 'LITERATURE_RECORD.tsv').open('w') as f:
    writer = csv.writer(f, delimiter='\t', lineterminator='\n')
    writer.writerow(['source_key','author','title','edition_year','access_status',
                     'source_url','exact_locators_and_attempts'])
    writer.writerows(rows)
print('Source records:', len(rows))
print('Entries without explicit status:', sum('STILL REQUIRES' in r[4] for r in rows))
