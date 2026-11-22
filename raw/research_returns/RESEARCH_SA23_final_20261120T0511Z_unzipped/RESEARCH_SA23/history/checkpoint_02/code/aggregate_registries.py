"""Reconcile authored fragments without certifying statements or inventing events."""
from pathlib import Path
import csv,json,re
root=Path(__file__).resolve().parents[1]
headers=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
allowed={'Proved','Proved under stated hypotheses','Refuted','Known'}
rows,conflicts={},[]
for path in sorted((root/'notes').glob('*_results.csv')):
    with path.open() as f:
        for row in csv.DictReader(f):
            if row['id'] in rows and row != rows[row['id']]: conflicts.append(row['id'])
            rows[row['id']]={key:row.get(key,'') for key in headers}
master=(root/'RESEARCH_SA23_paper.tex').read_text()
names=re.findall(r'\\(?:input|InputIfFileExists)\{(sections/[^}]+)\}',master)
labels=[]
pattern=re.compile(r'\\begin\{(theorem|lemma|proposition|corollary|example|remark|definition)\}(?:\[[^\]]*\])?(.*?)\\end\{\1\}',re.S)
for name in names:
    path=root/(name if name.endswith('.tex') else name+'.tex')
    if not path.exists(): continue
    for match in pattern.finditer(path.read_text()):
        label=re.search(r'\\label\{([^}]+)\}',match.group(2))
        if label: labels.append(label.group(1))
ordered=[rows[x] for x in labels if x in rows]
with (root/'RESEARCH_SA23_results.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=headers);w.writeheader();w.writerows(ordered)
eh=['statement_id','date','who','type','outcome','where']
events,seen=[],set()
for path in sorted((root/'notes').glob('*_CHECK_EVENTS.tsv')):
    with path.open() as f:
        for row in csv.DictReader(f,delimiter='\t'):
            row={key:row.get(key,'') for key in eh};signature=tuple(row.values())
            if signature not in seen: events.append(row);seen.add(signature)
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=eh,delimiter='\t');w.writeheader();w.writerows(events)
ch,corrections=[],[]
for path in sorted((root/'notes').glob('*_corrections.tsv')):
    with path.open() as f:
        reader=csv.DictReader(f,delimiter='\t')
        for key in reader.fieldnames or []:
            if key not in ch: ch.append(key)
        corrections.extend(reader)
if corrections:
    with (root/'CORRECTIONS.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=ch,delimiter='\t');w.writeheader();w.writerows(corrections)
checked={x['statement_id'] for x in events}
audit={'numbered_labels':len(labels),'statement_rows':len(ordered),'events':len(events),
    'corrections':len(corrections),'missing_rows':[x for x in labels if x not in rows],
    'extra_rows':[x for x in rows if x not in labels],'conflicting_rows':conflicts,
    'invalid_statuses':{x:r['status'] for x,r in rows.items() if r['status'] not in allowed},
    'labels_without_events':[x for x in labels if x not in checked],
    'duplicate_labels':sorted({x for x in labels if labels.count(x)>1})}
(root/'logs'/'registry_audit.json').write_text(json.dumps(audit,indent=2)+'\n')
print(json.dumps(audit,indent=2))
