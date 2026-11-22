#!/usr/bin/env python3
"""Merge independently maintained statement/check/bibliography fragments."""
import csv, pathlib
root=pathlib.Path(__file__).resolve().parents[1]
header=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
rows=[]
for path in sorted((root/'notes').glob('*results.csv')):
    with path.open(newline='') as f:
        for record in csv.DictReader(f):
            # Two component writers used explicit alternative column names.
            # This field-by-field map retains their exact values in the
            # user-requested register schema.
            aliases={'id':'statement_id','statement':'claim',
                     'where_proved':'proof_location','depends_on':'dependencies'}
            row={key:record.get(key,record.get(aliases.get(key,''),''))
                 for key in header}
            if not row['id'] or not row['statement'] or not row['status']:
                raise ValueError(f'Incomplete statement record in {path}: {record}')
            rows.append(row)
ids=[row['id'] for row in rows]
if len(ids)!=len(set(ids)):
    raise ValueError('Duplicate statement identifiers in component registers')
with (root/'RESEARCH_SA08_C3_D031_results.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=header,extrasaction='ignore'); writer.writeheader(); writer.writerows(rows)
events=[]
event_header=['statement_id','date','who','type','outcome']
for path in sorted((root/'notes').glob('*CHECK_EVENTS.tsv')):
    with path.open(newline='') as f:
        events.extend(csv.DictReader(f,delimiter='\t'))
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=event_header,delimiter='\t',extrasaction='ignore'); writer.writeheader(); writer.writerows(events)
bib='\n\n'.join(path.read_text() for path in sorted((root/'notes').glob('*references.bib')))
(root/'RESEARCH_SA08_C3_D031_references.bib').write_text(bib+'\n')
print(f'{len(rows)} statement records; {len(events)} check events; bibliography fragments merged.')
