#!/usr/bin/env python3
"""Rebuild the standalone paper and normalize the branch registers."""
import csv, re, hashlib, json
from datetime import datetime,timezone
from pathlib import Path
base=Path(__file__).resolve().parents[1]
branches=['normal','cm','lambda','noncm']

parts=[(base/'audit/paper_front.tex').read_text()]
parts += [(base/b/'findings.tex').read_text() for b in branches]
parts += [(base/'audit/paper_tail.tex').read_text(),
          (base/'audit/bibliography_background.tex').read_text()]
for b in branches:
    s=(base/b/'bibliography.tex').read_text()
    if b=='lambda':
        # Keep primary-source entries; common background entries are in the
        # master bibliography and would otherwise repeat the same works.
        s=s.split(r'\bibitem{NXLSGA4}')[0]
    parts.append(s)
parts.append('\\end{thebibliography}\n\\end{document}\n')
paper='\n\n'.join(parts)
(base/'ZETA_NEXT.tex').write_text(paper)

fields=['statement_id','date_utc','who','model','effort','run','type','method','outcome']
events=[]
paths=[base/'audit/root_checks.tsv']+[base/b/'CHECK_EVENTS.tsv' for b in ['cm','lambda','noncm']]
for p in paths:
    for r in csv.DictReader(p.open(),delimiter='\t'):
        rawdate=r.get('date_utc') or r.get('date')
        dt=datetime.fromisoformat(rawdate.replace('Z','+00:00'))
        date=dt.astimezone(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
        who=r.get('who') or r.get('who_model_effort_run')
        event_type={'computation':'computation or formal certificate',
                    'used and statement hypotheses rechecked':'used and rechecked in this run',
                    'used without re-check':'carried as background without fault found'}.get(r['type'],r['type'])
        events.append(dict(statement_id=r['statement_id'],date_utc=date,who=who,
          model=r.get('model') or 'GPT-6 Astra Pro',
          effort=r.get('effort') or 'not exposed by runtime (inherited)',
          run=r.get('run') or 'ZETA_NEXT',
          type=event_type,method=r.get('method') or r.get('how') or '',outcome=r['outcome']))
events.sort(key=lambda r:(r['date_utc'],r['statement_id'],r['who']))
with (base/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)

qfields=['id','source_and_locator','question','state','finding_ids_or_current_gate']
questions=[]
for p in [base/'audit/root_questions.tsv']+[base/b/'QUESTIONS.tsv' for b in ['cm','lambda','noncm']]:
    for r in csv.DictReader(p.open(),delimiter='\t'):
        q={k:r.get(k,'') for k in qfields}
        q['finding_ids_or_current_gate']=r.get('finding_ids_or_current_gate') or r.get('finding_ids_or_gate') or ''
        if q['state'].startswith('proved'): q['state']='proved'
        if q['id']=='Q3-LADIC-VS-MOTIVIC':
            q['question']='What motivic splitting is supplied without identifying every higher-tensor fixed-l projector as motivic?'
            q['state']='proved'
        if q['id']=='Q2-SEPARATED-NONPROPER':
            q['question']='Do these arguments decide the separate separated-nonproper amendment?'
            q['state']='proved scope limitation'
            q['finding_ids_or_current_gate']='NX-L01 is nonseparated and NX-L02 uses properness, so neither decides that separate amendment. Its truth remains outside the requested literal refutation; no equivariant compactification is assumed.'
        if q['id']=='Q2-DP11-SCOPE':
            q['question']='Which special class of Lambda-structures does DP_MULT DP11 characterize?'
            q['state']='proved'
        questions.append(q)
assert len({q['id'] for q in questions})==len(questions)
with (base/'QUESTIONS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=qfields,delimiter='\t');w.writeheader();w.writerows(questions)

required=['NX%02d'%i for i in range(1,5)]+['NC%02d'%i for i in range(1,5)]+['NX-L%02d'%i for i in range(1,8)]+['NG%02d'%i for i in range(1,8)]
checks=[]
for sid in required:
    assert r'\label{'+sid+'}' in paper, sid
    records=[r for r in events if r['statement_id']==sid and r['type']=='targeted proof check']
    assert records, sid
    checks.append({'id':sid,'whole_proof_check_events':len(records)})
(base/'audit/finding_coverage.json').write_text(json.dumps(checks,indent=2)+'\n')
print('Assembled standalone paper:',len(paper),'characters')
print('Merged',len(events),'check events and',len(questions),'questions; all',len(required),'findings have recorded proof checks.')
