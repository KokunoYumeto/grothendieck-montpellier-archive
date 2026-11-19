#!/usr/bin/env python3
from pathlib import Path
import csv,json,re,collections
P=Path(__file__).parent
claims=json.loads((P/'claims.json').read_text());items=json.loads((P/'items.json').read_text());problems=json.loads((P/'problems.json').read_text());cert=json.loads((P/'computation_outputs.json').read_text());bib=json.loads((P/'bibliography_records.json').read_text())
editorial=json.loads((P/'editorial_tasks.json').read_text());directions=json.loads((P/'directions.json').read_text());editorial_directions=json.loads((P/'editorial_directions.json').read_text())
def tab(f):return list(csv.DictReader((P/f).open(),delimiter='\t'))
entries=tab('entries.tsv');readings=tab('readings.tsv');links=tab('links.tsv');events=tab('check_events.tsv');search=[json.loads(x) for x in (P/'search_log.jsonl').read_text().splitlines()]
ids={x['id'] for x in claims};iids={x['id'] for x in items};bids={x['key'] for x in bib};names={x['name'] for x in cert};errors=[]
for seq,name in [(claims,'claims'),(items,'items'),(problems,'problems'),(editorial,'editorial tasks')]:
 if len({x['id'] for x in seq})!=len(seq):errors.append('Duplicate '+name+' ID')
assert len(entries)==82
assert len({x['entry_id'] for x in entries})==82
for x in entries:
 if x['item_id'] not in iids:errors.append('Unknown entry item '+x['item_id'])
required=['id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence']
for x in claims:
 for k in required:
  if k not in x:errors.append(x['id']+' missing '+k)
 for k in x['refs']:
  if k not in bids:errors.append(x['id']+' unknown ref '+k)
 for k in x['items']:
  if k not in iids:errors.append(x['id']+' unknown item '+k)
 for k in x['computation']['certificate_search_labels']:
  if k not in names:errors.append(x['id']+' missing certificate '+k)
 fate=next((r for r in search if r['id']=='FATE-'+x['id']),None)
 if not fate or not fate['search_operations']:errors.append(x['id']+' has no fate-search operations')
 if not any(e['statement_id']==x['id'] for e in events):errors.append(x['id']+' missing check event')
for x in problems+editorial:
 for k in ['id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs']:
  if k not in x:errors.append(x['id']+' missing '+k)
 for k in x['refs']:
  if k not in bids:errors.append(x['id']+' unknown ref '+k)
 for k in x.get('claims',[]):
  if k not in ids:errors.append(x['id']+' unknown claim '+k)
pids={p['id'] for p in problems};edids={p['id'] for p in editorial}
for x in problems:
 if not x.get('source_cue') or not x.get('count_as_authorial_mathematical_problem'):errors.append(x['id']+' lacks authorial problem provenance')
for x in editorial:
 if bool(x.get('original_id'))==bool(x.get('source_problem_id')):errors.append(x['id']+' needs exactly one redirect/split origin')
 if x.get('original_id') in pids:errors.append(x['id']+' whole redirect still in MP register')
 if x.get('source_problem_id') and x['source_problem_id'] not in pids:errors.append(x['id']+' missing retained source problem')
for x in directions+editorial_directions:
 if not set(x['items'])<=iids or not set(x['claims'])<=ids:errors.append(x['id']+' invalid item/claim link')
 if not set(x['problems'])<=pids or not set(x['editorial_tasks'])<=edids:errors.append(x['id']+' invalid MP/ED link')
 if x in directions and not x['problems']:errors.append(x['id']+' Stage6 direction without authorial problem')
 if x in editorial_directions and x['problems']:errors.append(x['id']+' editorial-only direction has MP dependency')
for i in items:
 if not any(e['statement_id']==i['id'] for e in events):errors.append(i['id']+' missing event')
for b in bib:
 if b['note'] not in ['verified','unverified']:errors.append(b['key']+' invalid access marker')
 for k in ['title','author','url','annote']:
  if not b[k]:errors.append(b['key']+' empty '+k)
 if not any(e['statement_id']==b['key'] for e in events):errors.append(b['key']+' missing event')
report=dict(date='2026-11-19',entries=len(entries),items=len(items),claims=len(claims),problems=len(problems),readings=len(readings),links=len(links),certificates=len(cert),references=len(bib),check_events=len(events),search_records=len(search),entry_verdicts=dict(collections.Counter(x['verdict'] for x in entries)),classes=dict(collections.Counter(x['class'] for x in claims)),page_statuses=dict(collections.Counter(x['status_on_pages'] for x in claims)),links_by_kind=dict(collections.Counter(x['kind'] for x in links)),bibliography_access=dict(collections.Counter(x['note'] for x in bib)),errors=errors)
report.update(editorial_tasks=len(editorial),directions=len(directions),editorial_directions=len(editorial_directions))
(P/'validation_output.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='page_statuses'},ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
