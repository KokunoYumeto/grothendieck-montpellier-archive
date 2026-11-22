"""Confirm prior Simon reading scope; this is not a new source-search route."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import csv
import io

ROOT = Path(__file__).resolve().parents[1]
textpath = ROOT/'notes/category_Simon1977.txt'
pdf = ROOT/'notes/category_Simon1977.pdf'
lines = textpath.read_text().splitlines()
intervals = [(1,148),(1376,1505)]
record = {'utc':datetime.now(timezone.utc).isoformat(),
          'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
          'text_sha256':hashlib.sha256(textpath.read_bytes()).hexdigest(),
          'source_url':'https://math.caltech.edu/SimonPapers/74.pdf',
          'scope':'Existing original-PDF extraction; introductory historical comments pp244-246, acknowledgment p271, added notes/references pp272-273. No new search or mathematical proof audit.',
          'extracts':[{'line_range':[a,b],'text':'\n'.join(lines[a-1:b])} for a,b in intervals]}
(ROOT/'notes/category_simon_history_scope_record.json').write_text(
    json.dumps(record,ensure_ascii=False,indent=2)+'\n')
outcome = ('Confirmed the already-completed Simon1977 introduction/added-notes/bibliography route and read acknowledgment p271 explicitly: Kato/Zalcman correspondence, Wightman/Seiler discussions, published Seiler-Simon refs31-33; no named Grothendieck letter, enclosure or supplied trace proof. Exact published references read, no new route or date-gate movement claimed. notes/category_simon_fredholm_audit.md')
events=ROOT/'notes/category_CHECK_EVENTS.tsv'
if outcome not in events.read_text():
    buffer=io.StringIO(); writer=csv.writer(buffer,delimiter='\t',lineterminator='\n')
    writer.writerow(['geo-H-history','2026-11-20','GPT-6 Astra, inherited effort, crystalline_categories','used and rechecked in this run',outcome])
    with events.open('a') as handle:handle.write(buffer.getvalue())
print(json.dumps({key:value for key,value in record.items() if key!='extracts'},indent=2))
print('EXTRACTS_SAVED',len(record['extracts']))
