#!/usr/bin/env python3
"""Apply the manually approved joins; preserve local judgments and provenance.

No inference of verdicts, theorem status, or duplication is performed here.
"""
import csv,json,re,copy,collections,datetime
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
SCOPES=['root','cote11a','cote11b','cote12c']
cfg=json.loads((BASE/'cross_scope_merges.json').read_text())
aliases={**cfg['items'],**cfg['claims'],**cfg['problems']}
refpath=BASE/'reference_aliases.json'
refaliases=json.loads(refpath.read_text()) if refpath.exists() else {}
if 'aliases' in refaliases:refaliases=refaliases['aliases']
def canonical(x,m=aliases):
 seen=set()
 while x in m:
  if x in seen:raise ValueError('Alias cycle: '+x)
  seen.add(x);x=m[x]
 return x
def uniq(a):
 out=[];seen=set()
 for x in a:
  k=json.dumps(x,ensure_ascii=False,sort_keys=True)
  if k not in seen:seen.add(k);out.append(x)
 return out
def arr(x):return x if isinstance(x,list) else ([] if x is None else [x])
idre=re.compile(r'MP-SA05-\d+|SA05-C\d+|SA05-\d+')
def remap(x):
 if isinstance(x,str):return idre.sub(lambda m:canonical(m.group()),x)
 if isinstance(x,list):return [remap(t) for t in x]
 if isinstance(x,dict):return {k:remap(v) for k,v in x.items()}
 return x
def getrows(p):return list(csv.DictReader(p.open(),delimiter='\t')) if p.exists() else []
def write_tsv(name,rows,fields):
 with (BASE/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
def write_json(name,data):(BASE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def refmapkey(k):return canonical(k,refaliases)
def join_records(kind):
 original=[]
 for sc in SCOPES:
  for x in json.loads((BASE/'work'/sc/(kind+'.json')).read_text()):
   x=copy.deepcopy(x);x['consolidation_scope']=sc;original.append(x)
 index={x['id']:x for x in original}
 if len(index)!=len(original):raise ValueError('Duplicate original ID in '+kind)
 for old,new in cfg[kind].items():
  if old not in index or new not in index:raise ValueError(('Missing approved alias endpoint',old,new))
 groups=collections.defaultdict(list)
 for x in original:groups[canonical(x['id'])].append(x)
 result=[]
 for key,group in groups.items():
  base=copy.deepcopy(index[key]);others=[x for x in group if x['id']!=key]
  base['aliases']=[x['id'] for x in others]
  if others:
   base['source_occurrences']=[{k:copy.deepcopy(x.get(k)) for k in ['id','consolidation_scope','cote','scans','lines','sources','his_words','his_statement','status_on_pages','check','check_reason','attribution','author'] if k in x} for x in group]
   base['parallel_formulations']=[{k:copy.deepcopy(x.get(k)) for k in ['id','statement','reconstruction','fate','class','status_on_pages','computation','as_he_states','plausible_today','state_of_art','why_open','worth'] if k in x} for x in others]
  if kind=='items':
   base['sources']=uniq([s for x in group for s in x['sources']])
  if kind=='claims':
   base['items']=uniq([canonical(s) for x in group for s in x['items']])
   base['computation']=uniq([x['computation'] for x in group]) if others else base['computation']
   base['search_ids']=uniq([s for x in group for s in (x.get('search_ids',[]) or ['SEARCH-'+x['id']])])
   if key in cfg.get('claim_overrides',{}):
    base.update(copy.deepcopy(cfg['claim_overrides'][key]));base['present_status']='As of 2026-11-19: '+base['fate']
  if kind=='problems':
   base['occurrences']=uniq([o for x in group for o in x['occurrences']])
   base['claims']=uniq([canonical(c) for x in group for c in x.get('claims',x.get('claim_ids',[]))])
   base.pop('claim_ids',None)
  if kind!='problems':
   cs=uniq([c for x in group for c in arr(x.get('cote'))]);base['cote']=cs[0] if len(cs)==1 else cs
   base['scans']=uniq([s for x in group for s in arr(x.get('scans'))])
   base['lines']=uniq([s for x in group for s in arr(x.get('lines'))])
  if 'refs' in base:base['refs']=uniq([refmapkey(r) for x in group for r in x.get('refs',[])])
  oldaliases=base['aliases'];oldocc=copy.deepcopy(base.get('source_occurrences'));oldform=copy.deepcopy(base.get('parallel_formulations'));oldsearch=copy.deepcopy(base.get('search_ids'))
  base=remap(base);base['aliases']=oldaliases
  # Search IDs identify performed queries, not claims. Preserve the original
  # row identifiers while canonicalizing their separate claim_ids pointers.
  if oldsearch is not None:base['search_ids']=oldsearch
  # Preserve the original ID inside the audit copies; live structured pointers above are canonical.
  if oldocc:base['source_occurrences']=oldocc
  if oldform:base['parallel_formulations']=oldform
  result.append(base)
 return sorted(result,key=lambda x:int(re.search(r'(\d+)$',x['id']).group()))
items=join_records('items');claims=join_records('claims');problems=join_records('problems')
suppath=BASE/'work/cote11b/refinement_claims.json'
targetpath=BASE/'work/cote11b/event_target_corrections.json'
targetcorrections=json.loads(targetpath.read_text()) if targetpath.exists() else {}
if suppath.exists():
 for x in json.loads(suppath.read_text()):
  x=remap(copy.deepcopy(x));x['refs']=uniq([refmapkey(k) for k in x['refs']])
  if any(c['id']==x['id'] for c in claims):raise ValueError('Duplicate supplemental ID '+x['id'])
  claims.append(x)
for c in claims:
 if c['id'] in targetcorrections:
  c['refined_statement']=canonical(targetcorrections[c['id']]['refined_id'])
  c['refinement_audit']=targetcorrections[c['id']]
 if c['id']=='SA05-C3008':
  c['lines'][0]['lines']='168,178-180'
  c['locator_audit']='The exact strict-level phrase occurs at physical line168;178–180 contains its subsequent estimate. Both were reread in the final audit.'
 if c['id']=='SA05-C1081':
  c['status_on_pages']='not asserted on the supplied pages; earlier-run comparison lead'
  for o in c.get('source_occurrences',[]):
   if o['id']=='SA05-C2080':
    o['original_author_field']=o.get('author')
    o['author']='Earlier-run comparison lead concerning Grothendieck; the target cote16 passage was not supplied.'
    o['attribution']='Not a directly witnessed manuscript assertion; qualified to agree with the canonical survivor.'
problem_index={x['id']:x for x in problems}
# The late problem had two questions. Only its global occurrence is an alias
# of MP18; the local question remains in MP3010 with its own coefficient target.
p18=problem_index['MP-SA05-18'];p3010=problem_index['MP-SA05-3010']
local_occ=[o for o in p18['occurrences'] if o.get('scan')==120 and o.get('file','').endswith('MPL_12_099-149_transcription.tex')]
p18['occurrences']=[o for o in p18['occurrences'] if o not in local_occ]
p18['claims']=[c for c in p18['claims'] if c!='SA05-C3030']
p3010['occurrences']=uniq(p3010['occurrences']+local_occ)
p3010['claims']=uniq(p3010['claims']+['SA05-C3030'])
for p in [p18,p3010]:
 p['partial_merge_note']='Original MP-SA05-3004 is split: scan108/global SA05-C75 belongs to MP-SA05-18; scan120/local SA05-C3030 belongs to MP-SA05-3010. The original parallel formulation is retained only as documentary provenance.'
item_index={x['id']:x for x in items}
for part in cfg.get('item_source_partitions',[]):
 src=item_index[part['primary']];dst=item_index[part['target']]
 src['sources']=[s for s in src['sources'] if s not in part['sources']]
 dst['sources']=uniq(dst['sources']+part['sources'])
 src.setdefault('source_partition_notes',[]).append(part)
 dst.setdefault('source_partition_notes',[]).append(part)
for name,data in [('SA05_items.json',items),('SA05_claims.json',claims),('SA05_problems.json',problems)]:write_json(name,data)

entries=[]
for sc in SCOPES:
 for x in getrows(BASE/'work'/sc/'entries.tsv'):
  if x['verdict']=='merged into item':x['verdict']='merged'
  old=x['item_id'];x['item_id']=cfg.get('entry_overrides',{}).get(x['entry_id'],canonical(old))
  if old!=x['item_id']:
   if x['verdict']=='kept':x['verdict']='merged'
   x['reason']+=' Cross-package consolidation: '+old+' → '+x['item_id']+'; the original read judgment is preserved in the scope records and source_occurrences.'
  entries.append(x)
index=getrows(BASE.parent/'sources/notes/NOTES_INDEX.tsv')
order={x['entry_id']:i for i,x in enumerate(index)}
entries.sort(key=lambda x:order[x['entry_id']])
write_tsv('SA05_entries.tsv',entries,['entry_id','item_id','verdict','reason'])

readings=[];links=[];events=[];searchrows=[];unavailable=[];unverified_reference_leads=[]
for sc in SCOPES:
 p=BASE/'work'/sc
 readings+=getrows(p/'readings.tsv')
 for rowno,row in enumerate(getrows(p/'links.tsv'),1):
  # Exact manually reviewed rows, not keyword inference of verification.
  if (sc=='cote11a' and 1<=rowno<=27) or (sc=='cote12c' and 7<=rowno<=11):
   row['run_names']='Earlier note/context source';row['status']='Source endpoint read; named archive endpoint unavailable in this part'
   unavailable.append(row)
  else:links.append(row)
 if sc=='cote11b':
  links+=getrows(p/'our_projects_links.tsv');unavailable+=getrows(p/'unverified_link_leads.tsv')
 events+=getrows(p/'CHECK_EVENTS.tsv')
 for row in getrows(p/'search_log.tsv'):
  searchrows.append({'scope':sc,'search_id':row.get('search_id',''),
   'claim_ids':row.get('claim_ids',row.get('claim_id','')),
   'record_json':json.dumps(row,ensure_ascii=False)})
events+=getrows(BASE/'work/cote12c/crossreview/CHECK_EVENTS.tsv')
events+=getrows(BASE/'work/cote11b/refinement_CHECK_EVENTS.tsv')
for row in getrows(BASE/'work/cote11b/refinement_reference_checks.tsv'):
 events.append({'statement_id':row['reference_key'],'date':row['date'],
  'who':'GPT-6 Astra Pro; cote11b independent refinement audit',
  'type':'used and rechecked in this run',
  'outcome':'Reopened '+row['url']+' at '+row['locator']+'. '+row['checked_extent']+' Limits: '+row['limits']})
for row in getrows(BASE/'work/cote11b/refinement_search_log.tsv'):
 searchrows.append({'scope':'cote11b/refinement-audit','search_id':row.get('search_id',''),
  'claim_ids':row.get('claim_ids',row.get('claim_id','')),'record_json':json.dumps(row,ensure_ascii=False)})
for row in getrows(BASE/'work/cote12c/crossreview/search_log.tsv'):
 searchrows.append({'scope':'cote12c/crossreview','search_id':row.get('search_id',''),
  'claim_ids':row.get('claim_ids',row.get('claim_id','')),'record_json':json.dumps(row,ensure_ascii=False)})
# Fresh bibliography checks have their actual, limited scope; they are not
# described as independent proofs of the referenced mathematical results.
ref_audit_targets={'RA-CHECK-02':['R-DM1982'],'RA-CHECK-03':['R-MilneReport2026'],
 'RA-CHECK-04':['R-Faltings1983','Faltings1986Finiteness'],'RA-CHECK-05':['SGA3II'],
 'RA-CHECK-06':['SGA3Publisher'],'RA-CHECK-07':['SGA3XII'],
 'RA-CHECK-08':['EGAII1961','Oda1969'],'RA-CHECK-09':['GIT1982','GIT1994Metadata'],
 'RA-CHECK-10':['R-Hua2026']}
for row in getrows(BASE/'work/cote11a/reference_alias_checks.tsv'):
 for key in ref_audit_targets.get(row['event_id'],[]):
  events.append({'statement_id':key,'date':row['date'],'who':'GPT-6 Astra Pro; cote11a bibliography audit',
   'type':'used and rechecked in this run','outcome':row['actual_check']+'; '+row['evidence']+'. '+row['proof_status']})
events.append({'statement_id':'Delzant1962','date':'2026-11-19',
 'who':'GPT-6 Astra Pro; cote11a external-reference audit','type':'used and rechecked in this run',
 'outcome':'Attached offprint title, author and colophon re-read; secondary exact citation corroborated, but no original external record opened. Strict bibliography note=unverified. See work/cote11a/delzant_external_reference_audit.json. This is access and provenance verification, not a new proof audit.'})
for row in getrows(BASE/'work/cote11a/reference_delzant_search_log.tsv'):
 searchrows.append({'scope':'cote11a/reference-audit','search_id':row['event_id'],'claim_ids':'Delzant1962',
  'record_json':json.dumps(row,ensure_ascii=False)})
for row in links:
 if row['to']=='Demazure1971Motifs:§3Proposition1;SGA4:IV7.5 backward locator':
  lead=copy.deepcopy(row);lead['to']='SGA4:IV7.5 backward locator'
  lead['evidence']='A backward reference in the checked Demazure passage; direct retrieval of the exact SGA4 endpoint failed. This endpoint is unverified and excluded from checked links.'
  unverified_reference_leads.append(lead)
  row['to']='Demazure1971Motifs:§3Proposition1'
  row['evidence']='The source manuscript passage and Demazure §3 Proposition1 were both read. The unverified SGA4 backward locator is separately retained in SA05_unverified_reference_leads.tsv.'
readings=uniq([remap(x) for x in readings]);links=uniq([remap(x) for x in links])
expanded_events=[]
for e in events:
 subjects=[s.strip() for s in e['statement_id'].split(';') if s.strip()]
 if len(subjects)>1:
  for subject in subjects:
   if not re.fullmatch(r'SA05-C\d+',subject):raise ValueError('Unexpected compound event subject '+e['statement_id'])
   one=copy.deepcopy(e);one['statement_id']=subject
   one['outcome']+=' This statement was one subject of the shared independent calculation; its exact scope is recorded in the cited review.'
   expanded_events.append(one)
 else:expanded_events.append(e)
events=expanded_events
for e in events:
 e['statement_id']=canonical(e['statement_id']);e['statement_id']=refmapkey(e['statement_id']);e['outcome']=remap(e['outcome'])
 if e['type'].startswith('refuted') and e['statement_id'] in targetcorrections:
  fix=targetcorrections[e['statement_id']];target=canonical(fix['refined_id'])
  old=e['outcome']
  old=re.sub(r'(?i)(refined statement:|refined |refinement/correct scope in)\s*SA05-C\d+(?:\.statement)?',lambda m:m.group(1)+' '+target,old)
  e['outcome']=old+' Authoritative refined statement: '+target+'. Final target audit: '+fix['reason']
events=uniq(events)
for r in searchrows:r['claim_ids']=remap(r['claim_ids'])
write_tsv('SA05_readings.tsv',readings,['cote','scan','line','reading','alternative','evidence','weight','confidence'])
write_tsv('SA05_links.tsv',links,['kind','from','to','what','evidence','note_ids'])
write_tsv('SA05_project_leads.tsv',[x for x in links if x['kind']=='our projects'],['kind','from','to','what','evidence','note_ids'])
write_tsv('SA05_unavailable_archive_leads.tsv',unavailable,['kind','from','to','what','evidence','note_ids','run_names','status'])
write_tsv('SA05_unverified_reference_leads.tsv',unverified_reference_leads,['kind','from','to','what','evidence','note_ids'])
write_tsv('CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])
write_tsv('SA05_searches.tsv',searchrows,['scope','search_id','claim_ids','record_json'])
write_json('SA05_aliases.json',{'items':cfg['items'],'claims':cfg['claims'],'problems':cfg['problems'],'references':refaliases,'source_partitions':cfg.get('item_source_partitions',[]),'problem_partial_overlap':cfg.get('problem_partial_overlap',{}),'decision_basis':cfg['decision_basis']})

def normstatus(x):
 s=x['status_on_pages'].lower()
 if s.startswith('current reconstruction'):return 'current-run refinement'
 if s.startswith('not '):return 'comparison or explicitly rejected inference, not an assertion on the pages'
 if 'historical recollection' in s:return 'historical/documentary statement'
 if 'false' in s:return 'false as stated under the recorded interpretation'
 if s.startswith('corrected by'):return 'corrected or withdrawn by the author'
 for p in ['proved there','proof sketched','stated without proof','open on the pages']:
  if s.startswith(p):return p
 return s
for c in claims:c['status_category']=normstatus(c)
write_json('SA05_claims.json',claims)
counts={'entries':len(entries),'items':len(items),'claims':len(claims),'problems':len(problems),
 'readings':len(readings),'links':len(links),'project_leads':sum(x['kind']=='our projects' for x in links),
 'separate_unavailable_archive_leads':len(unavailable),'events':len(events),'search_rows':len(searchrows),
 'separate_unverified_reference_leads':len(unverified_reference_leads),
 'verdicts':dict(collections.Counter(x['verdict'] for x in entries)),
 'item_kinds':dict(collections.Counter(x['kind'] for x in items)),
 'claim_classes':dict(sorted(collections.Counter(x['class'] for x in claims).items())),
 'claim_statuses':dict(collections.Counter(x['status_category'] for x in claims)),
 'merged_item_aliases':len(cfg['items']),'merged_claim_aliases':len(cfg['claims']),'merged_problem_aliases':len(cfg['problems'])}
write_json('counts.json',counts)
(BASE/'programs/outputs/consolidate.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'counts':counts},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(counts,ensure_ascii=False))
