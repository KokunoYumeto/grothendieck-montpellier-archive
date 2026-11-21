"""Combine auditable module registers without changing their event meanings."""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
FIELDS_E = ['statement_id','date','who','type','outcome','method','source_locator','event_file']
FIELDS_Q = ['id','source_locator','question','state','finding_ids','current_gate','approaches','next_step','question_file']

def read(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def write(path, fields, rows):
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)

events=[]
for path in sorted((ROOT/'modules').glob('*events.tsv')):
    for row in read(path):
        r={k:row.get(k,'') for k in FIELDS_E}
        r['date']=row.get('date',row.get('date_utc',''))
        r['source_locator']=row.get('source_locator',row.get('evidence',''))
        r['method']=row.get('method','See exact outcome and source locator; no additional check type inferred.')
        r['event_file']=str(path.relative_to(ROOT))
        assert all(r[k] for k in ['statement_id','date','who','type','outcome']), (path,row)
        events.append(r)
write(ROOT/'CHECK_EVENTS.tsv',FIELDS_E,events)

questions=[]
for path in sorted((ROOT/'modules').glob('*questions.tsv')):
    for row in read(path):
        r={k:row.get(k,'') for k in FIELDS_Q}
        r['id']=row.get('id',row.get('question_id',''))
        r['source_locator']=row.get('source_locator',row.get('locator',row.get('context',row.get('evidence',''))))
        r['state']=row.get('state',row.get('status',''))
        r['finding_ids']=row.get('finding_ids',row.get('result_ids',''))
        r['current_gate']=row.get('current_gate',row.get('current_answer',row.get('finding_or_gate',row.get('exact_remaining_gate',row.get('progress','')))))
        r['approaches']=row.get('approaches',row.get('method',row.get('attempted_route','')))
        r['next_step']=row.get('next_step',row.get('remaining_work',''))
        if not r['finding_ids']:
            r['finding_ids']='; '.join(dict.fromkeys(re.findall(r'MA-[A-Z]+-[0-9]+(?:[–-]+[0-9]+)?',' '.join(str(v) for v in row.values()))))
        if not r['source_locator']:
            r['source_locator']=str(path.relative_to(ROOT))
        r['question_file']=str(path.relative_to(ROOT))
        assert all(r[k] for k in ['id','question','state']), (path,row)
        questions.append(r)
ids=[r['id'] for r in questions]
assert len(set(ids))==len(ids), 'Duplicate question IDs must be resolved explicitly.'
write(ROOT/'QUESTIONS.tsv',FIELDS_Q,questions)
report={'events':len(events),'questions':len(questions),'unique_question_ids':len(set(ids)),
        'event_sources':len(set(r['event_file'] for r in events)),
        'status':'PASS','scope':'Register structure and preservation only; not a mathematical proof check.'}
(ROOT/'checks/register_assembly.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
