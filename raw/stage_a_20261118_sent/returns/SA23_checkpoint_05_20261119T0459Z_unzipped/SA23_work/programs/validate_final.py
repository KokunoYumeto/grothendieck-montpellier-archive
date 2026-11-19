#!/usr/bin/env python3
"""Structural audit of assessed final registers; it does not judge mathematics."""
import csv,json,re,collections,datetime,hashlib
from pathlib import Path
W=Path(__file__).resolve().parents[1];B=W.parent
errors=[];warnings=[];checks={}
def load(name):return json.loads((W/name).read_text())
def tsv(name):
 with(W/name).open()as f:return list(csv.DictReader(f,delimiter='\t'))
def require(test,description,detail=None):
 if not test:errors.append({'check':description,'detail':detail})
def unique_ids(rows,kind):
 ids=[x['id']for x in rows];dup=[i for i,n in collections.Counter(ids).items()if n>1]
 require(not dup,kind+' IDs unique',dup);return set(ids)
fields={'items':['id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'],'claims':['id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'],'problems':['id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs']}
data={k:load('SA23_'+k+'.json')for k in fields}
sets={k:unique_ids(v,k)for k,v in data.items()}
for kind,rows in data.items():
 for r in rows:
  require(all(k in r for k in fields[kind]),kind+' required fields',r['id'])
  for key in ['statement','his_statement','fate','present_status','as_he_states','plausible_today','state_of_art','why_open','worth']:
   if key in r:require(bool(str(r[key]).strip()),kind+' nonempty '+key,r['id'])
entries=tsv('SA23_entries.tsv')
with(B/'sources/notes/NOTES_INDEX.tsv').open()as f:index=list(csv.DictReader(f,delimiter='\t'))
key='entry_id'if'entry_id'in index[0]else'id';expected={r[key]for r in index}
actual=[r['entry_id']for r in entries]
require(len(entries)==326 and len(set(actual))==326,'326 unique verdict rows',len(entries))
require(set(actual)==expected,'exact NOTES_INDEX coverage',{'missing':sorted(expected-set(actual)),'extra':sorted(set(actual)-expected)})
byitem={r['id']:r for r in data['items']}; source_owners=collections.defaultdict(list)
for i in data['items']:
 for s in i['sources']:source_owners[s].append(i['id'])
require(set(source_owners)==expected,'item source arrays cover exactly indexed entries',{'missing':sorted(expected-set(source_owners)),'extra':sorted(set(source_owners)-expected)})
require(all(len(v)==1 for v in source_owners.values()),'each indexed entry belongs to one canonical subject',{k:v for k,v in source_owners.items()if len(v)!=1})
for e in entries:
 require(e['item_id']in sets['items'],'verdict target exists',e)
 if e['item_id']in byitem:require(e['entry_id']in byitem[e['item_id']]['sources'],'entry and item source mapping agrees',e['entry_id'])
 require(bool(e['reason'].strip())and bool(e['verdict'].strip()),'verdict and reason present',e['entry_id'])
checks['indexed_entries']=len(entries)
bib=load('outputs/bibliography_audit.json');keys=set(re.findall(r'@\w+\{([^,]+)',(W/'SA23_references.bib').read_text()))
statuses={'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages','present-run refinement; not an assertion on the pages'}
for c in data['claims']:
 require(c['class']in'ABCDEF'and len(c['class'])==1,'valid fate class',c['id'])
 require(c['status_on_pages']in statuses,'canonical page status',c['id'])
 require(c['confidence']in ['high','medium','low'],'canonical confidence',c['id'])
 for i in c['items']:require(i in sets['items'],'claim item exists',(c['id'],i))
 for ref in c['refs']:require(ref in keys,'claim reference exists',(c['id'],ref))
 if not c['refs']:warnings.append({'check':'claim has no external reference key; inspect explicit identification/search limit','id':c['id'],'class':c['class']})
 require(bool(c.get('record_origin')),'explicit claim provenance',c['id'])
for q in data['problems']:
 require(bool(q['occurrences']),'problem has source occurrence',q['id'])
 require(bool(q['refs']),'problem state-of-art reference supplied',q['id'])
 for ref in q['refs']:require(ref in keys,'problem reference exists',(q['id'],ref))
 for c in q.get('claims',[]):require(c in sets['claims'],'problem claim exists',(q['id'],c))
require([q['id']for q in data['problems']]==[f'MP-SA23-{n:03}'for n in range(1,len(data['problems'])+1)],'consecutive final problem IDs')
dirs=load('SA23_directions.json');unique_ids(dirs,'direction')
editorial_tasks=load('SA23_editorial_tasks.json');editorial_ids=unique_ids(editorial_tasks,'editorial task')
for d in dirs:
 for k in ['items','claims','problems']:
  require(bool(d.get(k)),'direction cites '+k,d['id'])
  for sid in d.get(k,[]):require(sid in sets[k],'direction canonical '+k,(d['id'],sid))
 for k in ['title','would_establish','known','first_step']:require(bool(d.get(k)),'direction has '+k,d['id'])
 for k in ['interest','one_run_progress']:require(isinstance(d.get(k),(int,float))and 1<=d[k]<=5,'direction score '+k,d['id'])
 for sid in d.get('editorial_tasks',[]):require(sid in editorial_ids,'direction editorial task exists',(d['id'],sid))
editorial_dirs=load('SA23_editorial_directions.json');unique_ids(editorial_dirs,'editorial direction')
for d in editorial_dirs:
 for k in ['items','claims','problems']:
  for sid in d.get(k,[]):require(sid in sets[k],'editorial direction canonical '+k,(d['id'],sid))
 for sid in d.get('editorial_tasks',[]):require(sid in editorial_ids,'editorial direction task exists',(d['id'],sid))
require([d['rank']for d in dirs]==list(range(1,len(dirs)+1)),'direction ranks consecutive')
events=tsv('CHECK_EVENTS.tsv');evset={e['statement_id']for e in events}
for kind in ['items','claims']:
 require(sets[kind]<=evset,'every '+kind+' record has a check event',sorted(sets[kind]-evset))
missing_refs=sorted(keys-evset)
if missing_refs:warnings.append({'check':'bibliography records without an event keyed exactly to the bibliography key; inspect reference_checks for metadata-only or alternative-key records','keys':missing_refs})
for e in events:require(all(str(e.get(k,'')).strip()for k in ['statement_id','date','who','type','outcome']),'complete check event',e.get('statement_id'))
fates=load('outputs/fate_coverage.json')
require(not fates['missing_claims'],'all claims have searched fate',fates['missing_claims'])
require(not fates['unknown_claim_targets'],'no orphan search-claim mappings',fates['unknown_claim_targets'])
links=tsv('SA23_links.tsv');readings=tsv('SA23_readings.tsv')
for link in links:
 require(link['kind']in ['folder','published work','our projects'],'link kind',link)
 require(all(link[k].strip()for k in ['from','to','what','evidence']),'both link ends and evidence recorded',link)
for r in readings:require(all(r[k].strip()for k in ['cote','scan','line','reading','alternative','evidence','weight','confidence']),'reading fields complete',r)
source=tsv('SA23_source_coverage.tsv');summary=load('outputs/source_coverage_summary.json')
require(len(source)==91 and summary['transcriptions']==45 and summary['transcription_lines']==38685,'source inventory counts',summary)
for row in source:
 p=B/row['file'];require(p.exists(),'source file remains available',row['file'])
 if p.exists():require(hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],'source remained unchanged',row['file'])
aliases=load('SA23_id_aliases.json')['aliases'];allids=set.union(*sets.values())|{x['id']for x in load('SA23_editorial_tasks.json')}
for old,targets in aliases.items():
 for target in targets:require(target in allids,'alias resolves to final record',(old,target))
checks.update({k:len(v)for k,v in data.items()});checks.update(directions=len(dirs),check_events=len(events),references=len(keys),links=len(links),readings=len(readings),source_files=len(source),claim_search_rows=fates['preserved_search_records'])
report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Structural audit only; individual mathematical checks and source reading are recorded separately.','checks':checks,'errors':errors,'warnings':warnings,'passed':not errors}
(W/'outputs/final_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
raise SystemExit(0 if not errors else 1)
