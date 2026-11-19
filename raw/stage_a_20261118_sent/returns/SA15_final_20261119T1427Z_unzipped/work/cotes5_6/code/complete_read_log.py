"""Record the already completed full doubts-register reading once."""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'source_read_log.tsv'
rows=list(csv.DictReader(path.open(),delimiter='\t'));fields=list(rows[0])
source='sources/SA15_notes/pro/MPL_5+6_001-037_doubts.md'
if not any(r['source']==source for r in rows):
    text=(ROOT.parents[1]/source).read_text()
    rows.append(dict(source=source,cote='',scan='',file_lines=f'1–{len(text.splitlines())}',reading='Full mathematical doubts register and shared encoding conventions read; no scans supplied; mathematical alternatives remain unresolved',date_utc='2026-11-19',who='GPT-6 Astra Pro; effort not exposed; SA15-20261119/cotes5_6'))
    with path.open('w') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
print('Doubts-register reading is present in source_read_log.tsv.')
