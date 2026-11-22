#!/usr/bin/env python3
"""Aggregate actual recorded checks without upgrading their event types."""
import csv, json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
fields=['statement_id','date_utc','who_model_effort_run','type','outcome','locator','detail','sha256','event_source']
rows=[]
for path in sorted((root/'agents').glob('*CHECK_EVENTS.tsv')):
    with path.open(newline='') as f:
        for r in csv.DictReader(f,delimiter='\t'):
            rows.append({
                'statement_id':r['statement_id'],
                'date_utc':r.get('date_utc',r.get('date','')),
                'who_model_effort_run':r.get('who_model_effort_run',r.get('who','')),
                'type':r.get('type',''), 'outcome':r.get('outcome',''),
                'locator':r.get('locator',''),
                'detail':r.get('scope',r.get('detail','')),
                'sha256':r.get('sha256',''),
                'event_source':str(path.relative_to(root)),
            })
for path in sorted((root/'checks').glob('*.json')):
    data=json.loads(path.read_text())
    if not isinstance(data,list):
        data=data.get('events',[])
    for r in data:
        if 'statement_id' not in r: continue
        rows.append({
            'statement_id':r['statement_id'],
            'date_utc':r.get('date_utc',r.get('date','')),
            'who_model_effort_run':r.get('who_model_effort_run',r.get('who','')),
            'type':r.get('type',''), 'outcome':r.get('outcome',''),
            'locator':r.get('locator',r.get('proof_file','')),
            'detail':r.get('detail',''),
            'sha256':r.get('sha256',r.get('reviewed_sha256','')),
            'event_source':str(path.relative_to(root)),
        })
rows.sort(key=lambda r:(r['date_utc'],r['statement_id'],r['event_source']))
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    out=csv.DictWriter(f,fieldnames=fields,delimiter='\t')
    out.writeheader();out.writerows(rows)
print(json.dumps({'events':len(rows),'statements_with_events':len({r['statement_id'] for r in rows}),'file':'CHECK_EVENTS.tsv'}))
