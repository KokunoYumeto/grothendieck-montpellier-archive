"""Consolidate manually judged problems, readings, links and reference evidence."""
from pathlib import Path
from copy import deepcopy
from collections import Counter
import json,csv,re
BASE=Path(__file__).resolve().parents[2];W=BASE/'work';D=BASE/'deliverables'
def r(p):return json.loads(p.read_text())
def w(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def uq(xs):
 out=[];seen=set()
 for x in xs:
  k=json.dumps(x,sort_keys=True,ensure_ascii=False)
  if k not in seen:seen.add(k);out.append(x)
 return out
def seq(x):return x if isinstance(x,list) else [] if x is None else [x]
idmap=r(D/'SA15_id_map.json')
groups=[('cotes5_6','P56'),('cotes6_7','P67'),('root_review','P78'),('cotes8_9_4','P894')]
problems=[]
for folder,pref in groups:
 paths=[W/folder/'problems.json'] if pref!='P78' else [W/folder/'problems_c7.json',W/folder/'problems_c8.json']
 for p in paths:
  if p.exists():problems+=r(p)
# These are substantive identities assessed from both passages, not title matches.
PROBLEM_MERGES=[]
# Cross-review restored the local finite-algebra Poincaré question and the cusp
# comparison as separate problems. Likewise integrability, the global derived
# connection and the Leray construction are related stages, not one question.
by={p['id']:p for p in problems};aliases={};merged={}
for ids,title in PROBLEM_MERGES:
 assert all(x in by for x in ids),ids
 pp=[by[x] for x in ids];z=deepcopy(pp[0]);z['title']=title;z['component_versions']=deepcopy(pp)
 z['occurrences']=uq([v for x in pp for v in seq(x['occurrences'])]);z['refs']=uq([v for x in pp for v in x['refs']])
 for field in ['as_he_states','plausible_today','state_of_art','why_open','worth']:
  z[field]='\n\n'.join('['+x['id']+'] '+(x[field] if isinstance(x[field],str) else json.dumps(x[field],ensure_ascii=False)) for x in pp)
 z['consolidation_reason']='Same question developed across the cited leaves; different coefficient, characteristic, singularity or base hypotheses remain explicit in the source-specific versions.'
 merged[ids[0]]=z
 for i in ids:aliases[i]=ids[0]
out=[]
for p in problems:
 if p['id'] in aliases and aliases[p['id']]!=p['id']:continue
 out.append(merged.get(p['id'],p))
for i,p in enumerate(out,1):idmap[p['id']]=f'MP-SA15-{i:02}'
for old,head in aliases.items():idmap[old]=idmap[head]
for p in out:p['legacy_ids']=[x for x,y in idmap.items() if y==idmap[p['id']]];p['id']=idmap[p['id']]
def remap(x):
 if isinstance(x,str):
  x=x.replace('P56-C014–C016','P56-C014–P56-C016')
  return re.sub(r'P(?:56|67|78|894)-[ICP]\d{3}',lambda m:idmap.get(m.group(),m.group()),x)
 if isinstance(x,list):return [remap(t) for t in x]
 if isinstance(x,dict):return {k:(v if k=='legacy_ids' else remap(v)) for k,v in x.items()}
 return x
w('SA15_problems.json',remap(out));w('SA15_id_map.json',idmap)
def tsv(n,rows,fields):
 with (D/n).open('w') as f:
  q=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');q.writeheader()
  for row in rows:q.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})
readings=[];links=[];events=[];evidence=[]
for folder,pref in groups:
 for name,dest in [('readings',readings),('links',links),('check_events',events)]:
  if pref=='P78':
   if name=='check_events':
    paths=[W/folder/'check_events_c7.tsv',W/folder/'check_events_c8.tsv',W/folder/'reference_check_events.tsv']
   else:paths=[W/folder/(name+'_c7.json'),W/folder/(name+'_c8.json')]
  else:paths=[W/folder/(name+'.tsv')]
  for p in paths:
   if p.exists():dest.extend(r(p) if p.suffix=='.json' else list(csv.DictReader(p.open(),delimiter='\t')))
 p=W/folder/'reference_evidence.json'
 if p.exists():
  ee=r(p)
  if isinstance(ee,dict):ee=ee.get('references',list(ee.values()))
  for e in ee:e['reviewer_package']=folder;evidence.append(e)
 # Dedicated independent cross-review events are additional to each owner's audit.
 for p in sorted((W/folder).glob('*cross*events*.tsv')):events+=list(csv.DictReader(p.open(),delimiter='\t'))

# Root-reviewed links joining two package owners' explicitly read endpoints.
p=W/'cotes5_6/root_crosslinks.tsv'
if p.exists():
 for x in csv.DictReader(p.open(),delimiter='\t'):links.append(x)
for name,dest in [('root_link_supplement.tsv',links),('sga7_check_events.tsv',events)]:
 p=W/'cotes6_7'/name
 if p.exists():dest.extend(csv.DictReader(p.open(),delimiter='\t'))
for p in sorted((W/'global_audit').glob('*cross_events.tsv')):
 events.extend(csv.DictReader(p.open(),delimiter='\t'))
p=W/'global_audit/comparison_links.tsv'
if p.exists():links.extend(csv.DictReader(p.open(),delimiter='\t'))
p=W/'root_review/additional_readings.tsv'
if p.exists():readings.extend(csv.DictReader(p.open(),delimiter='\t'))

# Do not turn bibliographic identity into a verified mathematical endpoint.
verified_links=[];unverified_links=[];project_links=[]
for x in links:
 x=remap(x)
 if x.get('kind')=='bibliography':x['kind']='published work'
 if x.get('kind')=='our projects':project_links.append(x);continue
 if 'DemazureGabriel1970 II' in x.get('to',''):unverified_links.append(x);continue
 verified_links.append(x)
for folder,_ in groups:
 for name in ['unverified_links.tsv','external_leads.tsv','project_links.tsv','project_leads.tsv','our_projects.tsv']:
  p=W/folder/name
  if p.exists():
   for x in csv.DictReader(p.open(),delimiter='\t'):
    (project_links if x.get('kind')=='our projects' or 'project' in name else unverified_links).append(remap(x))

assert all(x.get('kind') in ['folder','published work'] and all(x.get(k) for k in ['from','to','what','evidence','note_ids']) for x in verified_links), 'A main link lacks a checked endpoint, its evidence, or source IDs.'
tsv('SA15_readings.tsv',uq(remap(readings)),['cote','scan','line','reading','alternative','evidence','weight','confidence'])
tsv('SA15_links.tsv',uq(verified_links),['kind','from','to','what','evidence','note_ids'])
tsv('SA15_unverified_links.tsv',uq(unverified_links),['kind','from','to','what','evidence','note_ids'])
tsv('SA15_project_leads.tsv',uq(project_links),['kind','from','to','what','evidence','note_ids'])

# Normalize evidence records without erasing inspection limitations.
refs={}
for e in evidence:
 key=e.get('key',e.get('id'));assert key,e
 if 'fields' in e:fields=deepcopy(e['fields'])
 else:
  fields={'author':e.get('authors',e.get('author','')),'title':e.get('title',''),'year':str(e.get('year','')),'url':e.get('url',''),'note':e.get('note','verified' if e.get('verified') else 'unverified')}
  if e.get('doi'):fields['doi']=e['doi']
 fields={k:str(v) for k,v in fields.items() if v is not None and str(v)}
 if key not in refs:refs[key]={'key':key,'fields':fields,'inspections':[]}
 else:
  for k,v in fields.items():
   if k not in refs[key]['fields'] or k in ['journal','pages','volume','doi','publisher','booktitle','series']:refs[key]['fields'][k]=v
  if fields.get('note')=='verified':refs[key]['fields']['note']='verified'
 refs[key]['inspections'].append(e)
for key,x in refs.items():
 assert x['fields'].get('note') in ['verified','unverified'],(key,x)
 if key=='Liu2025':x['fields']['author']='Haohao Liu'
 if key=='Hua2026':x['fields']['author']='Michel Hua'
bib=[]
for key,x in sorted(refs.items()):
 # Protect braces in untrusted bibliographic title strings while retaining math.
 fields=x['fields'];bib.append('@misc{'+key+',\n'+',\n'.join('  '+k+' = {'+v.replace('\n',' ')+'}' for k,v in fields.items())+'\n}\n')
(D/'SA15_references.bib').write_text('\n'.join(bib))
w('SA15_reference_evidence.json',list(refs.values()))
for ev in events:
 if ev['type'].startswith('refuted'):
  named=re.findall(r'P(?:56|67|78|894)-C\d{3}|CL-SA15-\d+',ev['type'])
  if named:ev['outcome']='Refined statement: '+', '.join(named)+'. '+ev['outcome']
  ev['type']="refuted, with the refined statement's id"
tsv('CHECK_EVENTS.tsv',remap(events),['statement_id','date','who','type','outcome'])
stats=dict(problems=len(out),raw_problems=len(problems),readings=len(uq(readings)),verified_links=len(uq(verified_links)),unverified_link_leads=len(uq(unverified_links)),project_leads=len(uq(project_links)),references=len(refs),verified_references=sum(x['fields']['note']=='verified' for x in refs.values()),check_events=len(events))
w('SA15_aux_counts.json',stats);print(json.dumps(stats,ensure_ascii=False))
