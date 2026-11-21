"""Merge actual check events without upgrading their recorded check types."""
from pathlib import Path
import csv

ROOT=Path(__file__).resolve().parents[1]
fields=['statement_id','date_utc','who','model','effort','run','type','outcome','evidence']
rows=[]
for path in sorted((ROOT/'agents').glob('*/CHECK_EVENTS.tsv')):
    with path.open(newline='') as f:
        for x in csv.DictReader(f,delimiter='\t'):
            rows.append(dict(statement_id=x.get('statement_id',''),
                date_utc=x.get('date_utc',x.get('date','2026-11-21')),
                who=x.get('who',path.parent.name),
                model=x.get('model','GPT-6 Astra Pro (session identity)'),
                effort=x.get('effort','inherited; not externally exposed'),
                run=x.get('run','HODGE_DIVISION'), type=x.get('type',''),
                outcome=x.get('outcome',''),
                evidence=x.get('evidence',x.get('locator',''))))
root_events=ROOT/'research/root_check_events.tsv'
if root_events.exists():
    with root_events.open(newline='') as f:
        rows.extend(csv.DictReader(f,delimiter='\t'))
with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader()
    seen=set()
    for r in rows:
        key=tuple(r.get(k,'') for k in fields)
        if key not in seen:
            w.writerow({k:r.get(k,'') for k in fields});seen.add(key)
print(f'Merged {len(seen)} distinct check events.')
