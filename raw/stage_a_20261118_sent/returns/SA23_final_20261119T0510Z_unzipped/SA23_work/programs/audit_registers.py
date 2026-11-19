#!/usr/bin/env python3
"""Read-only cross-register audit. It never supplies a mathematical assessment."""
import json,csv,re,collections,datetime
from pathlib import Path
W=Path(__file__).resolve().parents[1]
fields={'items':['id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'],'claims':['id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'],'problems':['id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs']}
data={k:[]for k in fields};ownerids={};errors=[];warnings=[];refs=collections.defaultdict(list);owners={}
for p in sorted((W/'parts').iterdir()):
 if not p.is_dir():continue
 owners[p.name]={}
 for kind in fields:
  f=p/(kind+'.json')
  if not f.exists():warnings.append(f'{p.name}: {kind} not yet present');continue
  x=json.loads(f.read_text());data[kind]+=x;owners[p.name][kind]=len(x)
  for a in x:
   ownerids[a['id']]=p.name
   for field in fields[kind]:
    if field not in a:errors.append([p.name,a['id'],'missing field',field])
   if kind=='claims':
    if a.get('class')not in list('ABCDEF'):errors.append([p.name,a['id'],'invalid class',a.get('class')])
    if a.get('confidence')not in ['high','medium','low']:warnings.append([p.name,a['id'],'nonstandard confidence',a.get('confidence')])
 if(p/'references.bib').exists():
  for key in re.findall(r'@\w+\{([^,]+)',(p/'references.bib').read_text()):refs[key].append(p.name)
sets={k:{x['id']for x in v}for k,v in data.items()}
for k,v in data.items():
 for sid,n in collections.Counter(x['id']for x in v).items():
  if n>1:errors.append(['ALL',sid,'duplicate '+k,n])
for c in data['claims']:
 for i in c.get('items',[]):
  if i not in sets['items']:errors.append([ownerids[c['id']],c['id'],'missing item',i])
 for r in c.get('refs',[]):
  if r not in refs:errors.append([ownerids[c['id']],c['id'],'missing reference',r])
for q in data['problems']:
 for r in q.get('refs',[]):
  if r not in refs:errors.append([ownerids[q['id']],q['id'],'missing reference',r])
for p in sorted((W/'parts').iterdir()):
 f=p/'directions.json'
 if f.exists():
  dirs=json.loads(f.read_text());owners[p.name]['directions']=len(dirs)
  for d in dirs:
   for k in ['items','claims','problems']:
    if not d.get(k):warnings.append([p.name,d.get('id'),'direction missing '+k])
    for sid in d.get(k,[]):
     if sid not in sets[k]:errors.append([p.name,d.get('id'),'unknown '+k,sid])
 elif(p/'directions.md').exists():warnings.append([p.name,'directions.json not yet present'])
entries=[]
for f in (W/'parts').glob('*/entries.tsv'):
 with f.open()as h:entries+=list(csv.DictReader(h,delimiter='\t'))
idx=Path('sources/notes/NOTES_INDEX.tsv')
with idx.open()as h:inputrows=list(csv.DictReader(h,delimiter='\t'))
idfield='entry_id'if'entry_id'in inputrows[0]else'id'
expected={x[idfield]for x in inputrows};actual={x['entry_id']for x in entries}
if len(entries)!=326 or expected!=actual:errors.append(['ALL','entries','index mismatch',{'rows':len(entries),'missing':sorted(expected-actual),'extra':sorted(actual-expected)}])
for e in entries:
 if e['item_id']not in sets['items']:errors.append(['ALL',e['entry_id'],'missing item',e['item_id']])
report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'owners':owners,'counts':{k:len(v)for k,v in data.items()},'indexed_entries':len(entries),'distinct_bib_keys':len(refs),'repeated_bib_keys':{k:v for k,v in refs.items()if len(v)>1},'errors':errors,'warnings':warnings}
(W/'outputs'/'register_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
