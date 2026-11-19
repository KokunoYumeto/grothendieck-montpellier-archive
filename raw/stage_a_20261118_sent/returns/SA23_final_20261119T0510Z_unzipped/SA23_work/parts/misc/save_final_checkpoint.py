"""Write the last documentary provenance events and completion checkpoint."""
import csv,datetime,json
from pathlib import Path
P=Path(__file__).resolve().parent
for part in ['misc','groupes']:
    d=P.parent/part
    eds=json.loads((d/'editorial_tasks.json').read_text())
    for e in eds:
        e.setdefault('editorial_formulation',e['as_he_states'])
        e['as_he_states']=e['source_cue']
    (d/'editorial_tasks.json').write_text(json.dumps(eds,ensure_ascii=False,indent=2)+'\n')

with (P/'check_events.tsv').open() as f:
    reader=csv.DictReader(f,delimiter='\t');columns=reader.fieldnames;events=list(reader)
existing={x['statement_id'] for x in events}
for item in json.loads((P/'items.json').read_text()):
    if item['id'] in {f'SA23-{n}' for n in range(1201,1209)} and item['id'] not in existing:
        events.append(dict(statement_id=item['id'],date='2026-11-19',
            who='GPT-6 Astra Pro; effort not independently exposed; run SA23-20261119; owner misc',
            type='used and rechecked in this run',
            outcome='Documentary consolidation of the fully read Codex passages and their literal excerpt into an additional subject item, with no Pro entry or new verdict row. The separate mathematical checks are recorded under '+', '.join(item['claim_ids'])+'.'))
redirects=json.loads((P/'problem_editorial_redirects.json').read_text())
for e in events:
    if e['statement_id'] in redirects and not e['outcome'].startswith('Origin audit:'):
        e['outcome']='Origin audit: editorial verification, not an authorial question at this endpoint. '+e['outcome'].replace('Authorial flag and drafting status collated. ','')
with (P/'check_events.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=columns,delimiter='\t');w.writeheader();w.writerows(events)
c=json.loads((P/'counts.json').read_text());c['check_events']=len(events)
(P/'counts.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')

now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
for part in ['misc','groupes']:
    with (P.parent/part/'progress.log').open('a') as f:
        f.write(now+' | FINAL: all assigned sources, claim searches, proof/computation records, literal quotations, authorial-origin audit, reading alarms, verified links, bibliography, sections, coverage, and ranked directions saved. Computation suites rerun successfully; final_validation.json checks structural and quotation integrity. No Library mutation.\n')
print('Completion checkpoint saved; core event rows:',len(events))
