"""Link historical statement IDs to exact labels without inventing events."""
from pathlib import Path
import csv,json,re

root=Path(__file__).resolve().parent
rows=list(csv.DictReader((root/'results.csv').open()))
events=list(csv.DictReader((root/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
out=[]
for row in rows:
    for label in re.findall(r'(?:prop|lem|cor|thm|ex):d-[a-z-]+',row['where_proved']):
        for e in events:
            if e['statement_id']==row['id']:
                out.append({
                    'old_statement_id':row['id'],
                    'exact_label':label,
                    'date':e['date'],
                    'who':e['who'],
                    'type':e['type'],
                    'outcome':'Cross-reference only; original statement ID '+row['id']+'. '+e['outcome'],
                    'scope':row['statement'],
                })
fields=['old_statement_id','exact_label','date','who','type','outcome','scope']
with (root/'statement_label_crosswalk.tsv').open('w',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t')
    writer.writeheader();writer.writerows(out)
text=(root.parent/'sections/part_d.tex').read_text()
labels=set(re.findall(r'\\label\{((?:prop|lem|cor|thm|ex):d-[a-z-]+)\}',text))
covered={r['exact_label'] for r in out}
result={
 'scope':'No new check event is asserted. Dates, author and type are copied unchanged from the original matching event. Multiple labels reflect the explicit where_proved field.',
 'main_numbered_labels':sorted(labels),
 'covered_labels':sorted(covered),
 'missing_labels':sorted(labels-covered),
 'crosswalk_rows':len(out),
 'original_events_preserved':len(events),
}
assert not result['missing_labels'], result
(root/'statement_label_crosswalk_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
