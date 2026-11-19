#!/usr/bin/env python3
"""Assemble individually assessed records using an explicitly authored consolidation plan.

This program supplies no mathematical verdict, literature classification or merge decision.
Run from the workspace containing sources/ and SA23_work/ after every owner is complete.
"""
import json,csv,re,copy,collections,datetime,sys
from pathlib import Path
W=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(W/'integration'))
from id_rewrite_helper import rewrite_ids
ORDER=['analysis_curves','root','ega','forms','hyperplanes','groupes','spaces','bt','misc']
P=[W/'parts'/x for x in ORDER]
PLAN=json.loads((W/'integration'/'consolidation_plan.json').read_text())
def unique(xs):
 out=[];seen=set()
 for x in xs:
  k=json.dumps(x,ensure_ascii=False,sort_keys=True)
  if k not in seen:seen.add(k);out.append(x)
 return out
def seq(x):return x if isinstance(x,list)else[x]
def apply_record_update(out,spec):
 # Snapshot once, before the first explicit scope update. A later append must
 # neither replace that original nor recursively snapshot previous snapshots.
 protected={'id','source_records','integration_record_before_update','integration_updates','integration_update_reasons'}
 sets=spec.get('set_fields',{});appends=spec.get('append_fields',{})
 assert out['id']==spec['id'],('Update target mismatch',out['id'],spec['id'])
 assert not(set(sets)|set(appends))&protected,('Protected record field',spec['id'])
 assert not set(sets)&set(appends),('Set/append collision',spec['id'])
 if 'integration_record_before_update'not in out:
  out['integration_record_before_update']=copy.deepcopy(out)
 for field,value in sets.items():out[field]=copy.deepcopy(value)
 for field,value in appends.items():
  old=out.get(field)
  old_values=[]if old is None else seq(old)
  new_values=[]if value is None else seq(value)
  out[field]=unique(copy.deepcopy(old_values)+copy.deepcopy(new_values))
 out.setdefault('integration_updates',[]).append(copy.deepcopy(spec))
 reasons=out.setdefault('integration_update_reasons',[])
 if spec['reason']not in reasons:reasons.append(spec['reason'])
 # Retain the legacy prose field while preserving every update's rationale.
 out['integration_update_reason']='\n\n'.join(reasons)
def dump(name,x):(W/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def read_tsv(f):
 if not f.exists():return[]
 with f.open()as h:return list(csv.DictReader(h,delimiter='\t'))
def write_tsv(name,fields,rows):
 with(W/name).open('w')as h:
  wr=csv.DictWriter(h,fieldnames=fields,delimiter='\t');wr.writeheader();wr.writerows({k:r.get(k,'')for k in fields}for r in rows)
original={kind:[x for p in P for x in json.loads((p/(kind+'.json')).read_text())]for kind in ['items','claims','problems']}
owner={x['id']:p.name for p in P for kind in original for x in json.loads((p/(kind+'.json')).read_text())}
aliases={};merge_events=[]
def combine(kind,records):
 byid={x['id']:copy.deepcopy(x)for x in records};base=copy.deepcopy(byid);removed=set()
 for spec in PLAN.get(kind[:-1]+'_merges',[]):
  target=spec['target'];assert target in byid,target
  out=byid[target]
  group=copy.deepcopy(out.get('source_records',[base[target]]))
  for sid in spec['sources']:
   assert sid in base,(kind,sid)
   group.append(base[sid]);removed.add(sid)
   aliases.setdefault(sid,[]).append(target)
  group=unique(group)
  out['source_records']=copy.deepcopy(group)
  out.setdefault('consolidation_reasons',[]).append(spec['reason'])
  if kind=='items':
   for key in ['sources','scans','lines','cote']:
    out[key]=unique([v for x in group for v in seq(x[key])])
   out['his_words']='\n\n'.join(f"Witness {x['id']} (cote {x['cote']}): {x['his_words']}"for x in group)
   out['check_reason']+=' Cross-folder consolidation: '+spec['reason']+' Individual checks are retained in source_records and entry verdicts.'
   out['reconstruction']+=' Consolidation joins the explicitly compared witnesses; it does not alter their readings.'
  elif kind=='claims':
   for key in ['items','refs','scans','lines','cote']:
    out[key]=unique([v for x in group for v in seq(x[key])])
   out['source_occurrences']=unique([dict(source_record_id=x['id'],cote=x['cote'],scans=x['scans'],lines=x['lines'],status_on_pages=x['status_on_pages'],statement=x['statement'])for x in group])
   out['his_statement']='\n\n'.join(f"Witness {x['id']} (cote {x['cote']}): {x['his_statement']}"for x in group)
   out['computation']=[dict(source_record_id=x['id'],assessment=x['computation'])for x in group]
   out['additional_witness_fates']=[dict(source_record_id=x['id'],fate=x['fate'],fate_date=x['fate_date'],present_status=x['present_status'],refs=x['refs'],classification=x['class'])for x in group[1:]]
  else:
   for key in ['occurrences','refs','claims']:
    if any(key in x for x in group):out[key]=unique([v for x in group for v in seq(x.get(key,[]))])
   out['as_he_states']='\n\n'.join(f"Witness {x['id']}: {x['as_he_states']}"for x in group)
   out['state_of_art']='\n\n'.join(unique(x['state_of_art']for x in group))
  for field,value in spec.get('overrides',{}).items():out[field]=value
  merge_events.append(dict(statement_id=target,date='2026-11-19',who='GPT-6 Astra Pro; effort not independently exposed; SA23-20261119/root integration',type='used and rechecked in this run',outcome='Manual cross-folder consolidation: '+', '.join(spec['sources'])+' -> '+target+'. '+spec['reason']))
 assert not(removed&{s['target']for s in PLAN.get(kind[:-1]+'_merges',[])}),'Plan must use final canonical targets, not a merge chain.'
 return[x for sid,x in byid.items()if sid not in removed]
data={k:combine(k,v)for k,v in original.items()}
original_editorial=[x for p in P if(p/'editorial_tasks.json').exists()for x in json.loads((p/'editorial_tasks.json').read_text())]
for task in original_editorial:
 old=task.get('original_id')
 if old:
  assert old not in {q['id']for q in data['problems']},('Editorial task still in authorial problem index',old)
  aliases.setdefault(old,[]).append(task['id'])
for spec in PLAN.get('record_updates',[]):
 kind=spec['kind'];records={x['id']:x for x in data[kind]};out=records[spec['id']]
 apply_record_update(out,spec)
 merge_events.append(dict(statement_id=out['id'],date='2026-11-19',who='GPT-6 Astra Pro; effort not independently exposed; SA23-20261119/root integration',type='used and rechecked in this run',outcome='Explicit source-based scope update: '+spec['reason']))
for k in aliases:aliases[k]=unique(aliases[k])
# Only problem IDs are renumbered. Mathematical claim and subject identifiers remain stable.
problem_renumber={x['id']:f'MP-SA23-{n:03}'for n,x in enumerate(data['problems'],1)}
for old,new in problem_renumber.items():aliases.setdefault(old,[]).append(new)
def resolve(sid,seen=None):
 seen=set()if seen is None else seen
 if sid not in aliases:return[sid]
 assert sid not in seen,('Cyclic ID map',sid)
 return unique([y for x in aliases[sid]for y in resolve(x,seen|{sid})])
aliases={k:resolve(k)for k in list(aliases)}
known_original_ids={x['id']for rows in original.values()for x in rows}
def rewrite_text(t):
 # Expand registered ranges and compact comma tails before replacing merged or
 # renumbered IDs. The helper does not infer IDs from years or prose numbers.
 return rewrite_ids(t,aliases,known_original_ids,kinds=('problem','claim','item'))
def rewrite(x,key=''):
 if key in ['source_records','source_record_id','original_id','original_ids','aliases','his_words','his_statement','integration_record_before_update','integration_updates','pre_origin_audit_record']:return x
 if isinstance(x,str):return rewrite_text(x)
 if isinstance(x,list):
  if key in ['items','claims','problems']:
   return unique([z for y in x for z in(resolve(y)if isinstance(y,str)else[rewrite(y)])])
  return[rewrite(y)for y in x]
 if isinstance(x,dict):
  out={}
  for k,v in x.items():
   if k in ['item','claim','problem']and isinstance(v,str)and v in aliases and len(aliases[v])>1:
    out[k+'s']=resolve(v);out['original_'+k+'_id']=v
   else:out[k]=rewrite(v,k)
  return out
 return x
data={k:[rewrite(x)for x in v]for k,v in data.items()}
# Canonical status values are manually supplied by source readers, with exact
# equivalences for the three owners whose existing values already use the schema.
fixed={'corrected by himself later (both places)':'corrected by himself later','not asserted in this precise form; present-run refinement':'present-run refinement; not an assertion on the pages','present-run refinement':'present-run refinement; not an assertion on the pages'}
standard={'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages','present-run refinement; not an assertion on the pages'}
for c in data['claims']:
 old=c['status_on_pages'];category=c.get('status_category',fixed.get(old,old))
 category=fixed.get(category,category)
 assert category in standard,(c['id'],'needs manually assigned status_category',category)
 c['status_detail']=old;c['status_on_pages']=category;c['status_category']=category
 c.setdefault('record_origin','present-run refinement'if category.startswith('present-run refinement')else'source assertion')
for kind,x in data.items():dump('SA23_'+kind+'.json',x)
dump('SA23_id_aliases.json',{'purpose':'Resolve pre-integration IDs in the preserved owner files. Values may have multiple targets only for explicitly split compound assertions. Source_records retain their original identifiers and wording.','aliases':aliases,'problem_renumbering':problem_renumber,'manual_plan':'integration/consolidation_plan.json'})
entries=[x for p in P for x in read_tsv(p/'entries.tsv')]
for e in entries:
 old=e['item_id'];new=resolve(old);assert len(new)==1,(e['entry_id'],new);e['item_id']=new[0]
 if old!=new[0]:
  e['reason']+=' Final source-based consolidation: '+old+' is merged into '+new[0]+'.'
  if e['verdict'].lower().startswith('kept'):e['verdict']='merged'
write_tsv('SA23_entries.tsv',['entry_id','item_id','verdict','reason'],entries)
readings=[rewrite(x)for p in P for x in read_tsv(p/'readings.tsv')]
links=[rewrite(x)for p in P for x in read_tsv(p/'links.tsv')]
links+=rewrite(PLAN.get('additional_links',[]))
write_tsv('SA23_readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],readings)
lf=['kind','from','to','what','evidence','note_ids']
write_tsv('SA23_links.tsv',lf,links)
write_tsv('SA23_project_leads.tsv',lf,[x for x in links if x['kind']=='our projects'])
events=[]
for p in P:
 for f in sorted(p.glob('*check_events.tsv')):
  for row in read_tsv(f):
   targets=resolve(row['statement_id'])
   for sid in targets:
    e=rewrite(row);e['statement_id']=sid
    if sid!=row['statement_id']:e['outcome']='Original record '+row['statement_id']+'; '+e['outcome']
    if len(targets)>1:
     e['outcome']='Component-level concordance only; the preserved original compound event had type ['+row['type']+']. Its outcome applies only to the component identified in integration/consolidation_plan.json, and is not a new independent proof or a refutation of every target. '+e['outcome']
     e['type']='used and rechecked in this run'
    events.append(e)
events+=rewrite(merge_events);events=unique(events)
write_tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
documents=[x for p in P if(p/'document_records.json').exists()for x in json.loads((p/'document_records.json').read_text())]
dump('SA23_document_records.json',rewrite(documents))
editorial=original_editorial
dump('SA23_editorial_tasks.json',rewrite(editorial))
# Every direction is already authored. The sort combines the two explicit scores;
# it creates no new task, priority rationale or purported result.
directions=[]
for p in P:
 ds=json.loads((p/'directions.json').read_text())
 for localn,d in enumerate(ds,1):
  d=rewrite(d);d['owner']=p.name
  d.setdefault('id',f'D-SA23-{p.name}-{localn:02}')
  d.setdefault('would_establish',d.get('residual',d.get('goal','')))
  assert d['would_establish'],(p.name,d['id'],'missing goal/residual')
  directions.append(d)
editorial_directions=[]
for p in P:
 if (p/'editorial_directions.json').exists():
  ds=json.loads((p/'editorial_directions.json').read_text())
  assert isinstance(ds,list),(p.name,'editorial directions must be a list')
  for d in ds:
   d=rewrite(d);d['owner']=p.name
   d['ranking_scope']='Editorial follow-up outside the Stage6 authorial-problem ranking.'
   editorial_directions.append(d)
direction_by_id={d['id']:d for d in directions+editorial_directions};removed_directions=set()
assert len(direction_by_id)==len(directions)+len(editorial_directions),'Duplicate main/editorial direction IDs'
for spec in PLAN.get('direction_consolidations',[]):
 assert spec['target']in {d['id']for d in directions},'Consolidated target needs an actual authorial question'
 target=direction_by_id[spec['target']];group=[copy.deepcopy(target)]+[copy.deepcopy(direction_by_id[s])for s in spec['sources']]
 if 'source_titles'in spec:assert [direction_by_id[s]['title']for s in spec['sources']]==spec['source_titles'],spec
 target['source_directions']=group;target['consolidation_reason']=spec['reason']
 for key in ['items','claims','problems','editorial_tasks']:target[key]=unique([sid for d in group for sid in d.get(key,[])])
 target['known']=' '.join(unique(d['known']for d in group))
 target.update(spec.get('overrides',{}));removed_directions.update(spec['sources'])
directions=[d for d in directions if d['id']not in removed_directions]
editorial_directions=[d for d in editorial_directions if d['id']not in removed_directions]
dump('SA23_editorial_directions.json',editorial_directions)
edmd=['# Editorial follow-up tasks outside the Stage6 ranking','','These directions retain useful reader verification and documentary tasks after the question-origin audit. They do not assert an otherwise unattested authorial question. No direction is developed here.','']
for d in editorial_directions:
 edmd +=['## '+d['id']+'. '+d['title'],'','Sources: '+', '.join(d.get('items',[])+d.get('claims',[])+d.get('problems',[])+d.get('editorial_tasks',[]))+'.','', 'Would establish: '+d.get('would_establish',d.get('residual',d.get('goal',''))),'','Known and residual: '+d.get('known',''),'','First concrete step: '+d.get('first_step',''),'']
(W/'SA23_editorial_directions.md').write_text('\n'.join(edmd)+'\n')
def progress(d):return d.get('feasible_progress_in_one_run',d.get('feasibility',d.get('progress')))
for d in directions:
 assert isinstance(d.get('interest'),(int,float)),(d.get('id'),'interest')
 assert isinstance(progress(d),(int,float)),(d.get('id'),'progress')
 d['one_run_progress']=progress(d)
directions.sort(key=lambda d:(-d['interest'],-d['one_run_progress'],d['id']))
for n,d in enumerate(directions,1):d['rank']=n
dump('SA23_directions.json',directions)
md=['# SA23 research directions','', 'These are ranked task specifications. None is developed into a new research project in this dossier. The primary ordering is mathematical interest, with plausible progress in one several-hour run as the second ordering. Scores are independent, from 1 (low) to 5 (high). A highly feasible editorial correction can therefore remain below a more consequential mathematical question.','', '| Rank | Direction | Interest | One-run progress |','|---:|---|---:|---:|']
for d in directions:md.append(f"| {d['rank']} | {d['title']} | {d['interest']}/5 | {d['one_run_progress']}/5 |")
for d in directions:
 md +=['',f"## {d['rank']}. {d['title']}",'',f"ID: {d['id']}. Interest {d['interest']}/5; one-run progress {d['one_run_progress']}/5.",'','Sources: '+', '.join(d['items']+d['claims']+d['problems']+d.get('editorial_tasks',[]))+'.','',d.get('origin','The direction is this run’s proposed follow-up; its source question and any reader verification components are separately identified.'),'', 'Would establish: '+d['would_establish'],'','Known and residual: '+d['known'],'','First concrete step: '+d['first_step']]
(W/'SA23_directions.md').write_text('\n'.join(md)+'\n')
# Bibliography is assembled by the separately auditable parser/merge program.
assert(W/'SA23_references.bib').exists(),'Run build_final_bibliography.py first.'
counts={'entries':len(entries),'items':len(data['items']),'indexed_subjects':sum(bool(x['sources'])for x in data['items']),'additional_subjects':sum(not x['sources']for x in data['items']),'claims':len(data['claims']),'problems':len(data['problems']),'readings':len(readings),'links':len(links),'quarantined_project_leads':sum(x['kind']=='our projects'for x in links),'directions':len(directions),'check_events':len(events),'document_records':len(documents),'editorial_tasks':len(editorial),'entry_verdicts':dict(collections.Counter(x['verdict']for x in entries)),'item_kinds':dict(collections.Counter(x['kind']for x in data['items'])),'claim_classes':dict(collections.Counter(x['class']for x in data['claims'])),'claim_statuses':dict(collections.Counter(x['status_on_pages']for x in data['claims'])),'claim_origins':dict(collections.Counter(x['record_origin']for x in data['claims'])),'source_owner_counts':{p.name:{k:len(json.loads((p/(k+'.json')).read_text()))for k in original}for p in P}}
dump('outputs/final_counts.json',counts)
counts['editorial_directions']=len(editorial_directions)
counts['explicitly_nonmathematical_authorial_question_records']=sum(q.get('count_as_authorial_mathematical_problem')is False for q in data['problems'])
dump('outputs/final_counts.json',counts)
overview=(W/'integration'/'overview.md').read_text()
sections=[]
for p in P:
 s=rewrite_text((p/'section.md').read_text())
 # Source sections use either H1/H2 or H2/H3. Normalize just the heading level.
 if re.search(r'^# ',s,re.M):s=re.sub(r'^(#+) ',lambda m:'#'+m.group(1)+' ',s,flags=re.M)
 sections.append(s)
stats=['## Counts and audit results','', 'Counts below are after the explicitly documented cross-folder consolidations. The preserved owner files show their earlier local counts; use this table for the final totals.','', '| Register | Final count |','|---|---:|']
for k in ['entries','items','indexed_subjects','additional_subjects','claims','problems','explicitly_nonmathematical_authorial_question_records','readings','links','quarantined_project_leads','directions','editorial_directions','check_events','document_records','editorial_tasks']:stats.append('| '+k.replace('_',' ')+' | '+str(counts[k])+' |')
for key,title in [('entry_verdicts','Entry verdicts'),('item_kinds','Subject kinds'),('claim_classes','Claim classes'),('claim_statuses','Claim status on the pages'),('claim_origins','Origin of claim records')]:
 stats+=['',f'### {title}','','| Category | Count |','|---|---:|']
 stats+=['| '+str(k).replace('|','/')+' | '+str(v)+' |'for k,v in sorted(counts[key].items())]
stats+=['','The final validation report is `outputs/final_validation.json`. It checks exact index coverage, references, source files, canonical IDs, directions, check-event coverage and packaging. Structural checks supplement the individual readings and mathematical judgments; they do not generate them.']
(W/'SA23_dossier.md').write_text(rewrite_text(overview)+'\n\n'+'\n\n'.join(sections)+'\n\n'+'\n'.join(stats)+'\n')
print(json.dumps({'counts':counts,'aliases':len(aliases),'manual_merge_events':len(merge_events)},ensure_ascii=False))
