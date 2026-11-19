"""Independent read-only final-register audit. No assembled files are modified."""
from pathlib import Path
from collections import Counter
import csv,io,json,re,hashlib,datetime
ROOT=Path('/workspace/scratch/594d1dc856a9')
W=ROOT/'SA04_work';F=W/'final'
names=['SA04_items.json','SA04_claims.json','SA04_problems.json','SA04_entries.tsv','SA04_readings.tsv','SA04_links.tsv','CHECK_EVENTS.tsv','SA04_references.bib','ID_ALIASES.tsv']
raw={n:(F/n).read_bytes() for n in names}
hashes={n:hashlib.sha256(v).hexdigest() for n,v in raw.items()}
def js(n):return json.loads(raw[n])
def ts(n):return list(csv.DictReader(io.StringIO(raw[n].decode()),delimiter='\t'))
I=js('SA04_items.json');C=js('SA04_claims.json');P=js('SA04_problems.json')
E=ts('CHECK_EVENTS.tsv');N=ts('SA04_entries.tsv');L=ts('SA04_links.tsv');R=ts('SA04_readings.tsv')
refs=set(re.findall(r'^@\w+\s*\{([^,]+),',raw['SA04_references.bib'].decode(),re.M))
ids={'items':{x['id'] for x in I},'claims':{x['id'] for x in C},'problems':{x['id'] for x in P},'references':refs}
checked={x['statement_id'] for x in E}
report={'snapshot_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'hashes':hashes}
report['counts']={k:len(v) for k,v in [('items',I),('claims',C),('problems',P),('entries',N),('readings',R),('links',L),('events',E),('references',refs)]}
report['missing_event_coverage']={k:sorted(v-checked) for k,v in ids.items() if k!='problems'}
report['orphan_event_ids']=sorted(checked-set().union(*ids.values()))
schemas={
'items':'id sources kind cote scans lines his_words statement reconstruction check check_reason'.split(),
'claims':'id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split(),
'problems':'id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split()}
errors=[]
for kind,data in [('items',I),('claims',C),('problems',P)]:
 if len(data)!=len(ids[kind]):errors.append([kind,'duplicate identifiers'])
 for r in data:
  if set(r)!=set(schemas[kind]):errors.append([r['id'],'schema',sorted(set(r)^set(schemas[kind]))])
enum={
'kind':set('conjecture|unproved claim|unpursued implication|idea of the earlier run|reading question|self-flagged step|withdrawn in the same text|title, date or page count|other'.split('|')),
'check':set('agrees|overstates|understates|misreads|not on the page'.split('|')),
'status_on_pages':set('proved there|proof sketched|stated without proof|corrected by himself later|false as stated|open on the pages'.split('|')),
'class':set('ABCDEF'),'confidence':{'high','medium','low'}}
for r in I+C:
 for k,vals in enum.items():
  if k in r and r[k] not in vals:errors.append([r['id'],'enum',k,r[k]])
for r in C+P:
 for key in r['refs']:
  if key not in refs:errors.append([r['id'],'missing reference',key])
for r in C:
 for key in r['items']:
  if key not in ids['items']:errors.append([r['id'],'missing item',key])
for r in P:
 for o in r['occurrences']:
  if isinstance(o,dict):
   for field,universe in [('claim',ids['claims']),('item',ids['items'])]:
    if field in o and o[field] not in universe:errors.append([r['id'],'missing occurrence '+field,o[field]])
   for key in o.get('items',[]):
    if key not in ids['items']:errors.append([r['id'],'missing occurrence item',key])
index=list(csv.DictReader((ROOT/'source/SA04_notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
if Counter(r['entry_id'] for r in N)!=Counter(r['entry_id'] for r in index):errors.append(['entries','index mismatch'])
for e in N:
 if e['item_id'] not in ids['items']:errors.append([e['entry_id'],'missing verdict item',e['item_id']])
 if e['verdict'] not in {'kept','merged','corrected','withdrawn','rests on a misreading'}:errors.append([e['entry_id'],'verdict enum',e['verdict']])
for e in L:
 if e['kind'] not in {'folder','published work','our projects'}:errors.append(['links','kind enum',e['kind']])
report['schema_identifier_errors']=errors
report['event_type_counts']=dict(Counter(r['type'] for r in E))
report['noncanonical_event_types']=[r for r in E if r['type'] not in {'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}]

def expand(s):
 if isinstance(s,list):return set(int(x) for x in s)
 out=set()
 for a,b in re.findall(r'(\d+)(?:\s*[-–]\s*(\d+))?',str(s)):
  out.update(range(int(a),int(b or a)+1))
 return out
cache={}
itemmap={r['id']:r for r in I};claimmap={r['id']:r for r in C}
def source(file):
 if file not in cache:
  p=ROOT/'source/SA04_texts'/file
  if not p.exists():return None
  lines=p.read_text().splitlines();meta=[];cote=None;scan=None
  for n,line in enumerate(lines,1):
   m=re.match(r'\s*\\cotefile\{([^}]+)\}',line)
   if m:cote=m[1];scan=None
   m=re.match(r'\s*\\scanpage\{(\d+)\}',line)
   if m:scan=int(m[1])
   structural=not line.strip() or bool(re.match(r'\s*\\(?:cotefile|scanpage)\{',line))
   meta.append({'cote':cote,'scan':scan,'content':not structural})
  cache[file]=(lines,meta)
 return cache[file]
def locs(value):
 if isinstance(value,list):
  for x in value:yield from locs(x)
  return
 s=str(value)
 matches=list(re.finditer(r'((?:pro|codex)/[^:;,\s]+\.tex)\s*:',s))
 if matches:
  for i,m in enumerate(matches):
   tail=s[m.end():matches[i+1].start() if i+1<len(matches) else len(s)]
   numeric=re.match(r'\s*([\d,;\s–-]+)',tail)
   if numeric:
    for a,b in re.findall(r'(\d+)(?:\s*[-–]\s*(\d+))?',numeric[1]):yield m[1],int(a),int(b or a)
 else:
  m=re.search(r'((?:pro|codex)/[^,;\s]+\.tex).*?\blines?\s*([\d\s;–-]+)',s)
  if m:
   for a,b in re.findall(r'(\d+)(?:\s*[-–]\s*(\d+))?',m[2]):yield m[1],int(a),int(b or a)
bad=[];mismatch=[];unparsed=[];empty=[]
def inspect(label,record,scope):
 values=record.get('lines')
 if values is None:return
 locations=list(locs(values))
 if not locations:unparsed.append([scope,label,values]);return
 wanted_cotes=set(str(record.get('cote','')).split(';'));wanted_scans=expand(record.get('scans',[]))
 actual_scans=set();actual_cotes=set();unscoped=[]
 for file,a,b in locations:
  src=source(file)
  if src is None:bad.append(dict(scope=scope,id=label,file=file,start=a,end=b,problem='missing source file'));continue
  lines,meta=src
  if a<1 or b<a or b>len(lines):bad.append(dict(scope=scope,id=label,file=file,start=a,end=b,problem='out of range',length=len(lines)));continue
  content=[m for m in meta[a-1:b] if m['content']]
  if not content:empty.append(dict(scope=scope,id=label,file=file,start=a,end=b))
  outside=sorted({m['cote'] for m in content if m['cote'] not in wanted_cotes},key=str)
  if outside:bad.append(dict(scope=scope,id=label,file=file,start=a,end=b,problem='wrong cote',expected=sorted(wanted_cotes),actual=outside))
  actual_cotes.update(m['cote'] for m in content)
  actual_scans.update(m['scan'] for m in content if m['scan'] is not None and m['cote'] in wanted_cotes)
 if wanted_scans:
  extra=actual_scans-wanted_scans;missing=wanted_scans-actual_scans
  if extra or missing:mismatch.append(dict(scope=scope,id=label,scans_declared=sorted(wanted_scans),scans_in_ranges=sorted(actual_scans),extra=sorted(extra),missing=sorted(missing)))
for kind,data in [('item',I),('claim',C)]:
 for r in data:inspect(r['id'],r,kind)
for p in P:
 for i,o in enumerate(p['occurrences']):
  if isinstance(o,dict):
   enriched=dict(o)
   parent=claimmap.get(o.get('claim')) or itemmap.get(o.get('item'))
   if 'cote' not in enriched and parent:enriched['cote']=parent['cote']
   inspect(p['id']+':'+str(i+1),enriched,'problem occurrence')
  else:
   cote=re.search(r'cote\s*([^,; ]+)',o)
   scans=re.search(r'\bscans?\s*([\d,– -]+)',o)
   inspect(p['id']+':'+str(i+1),{'cote':cote[1] if cote else '', 'scans':scans[1] if scans else [],'lines':o},'problem occurrence')
report['bad_source_intervals']=bad
report['bad_source_interval_counts']=dict(Counter(r['scope'] for r in bad))
report['bad_source_record_counts']={scope:len({r['id'] for r in bad if r['scope']==scope}) for scope in ['item','claim','problem occurrence']}
report['scan_field_discrepancies']=mismatch
report['unparsed_locators']=unparsed
report['empty_source_intervals']=empty
report['incomplete_target_locators']=[{'id':r['id'],'lines':r['lines']} for r in I if any(re.search(r'codex/K93-\d{2}(?![\d_])',x) for x in (r['lines'] if isinstance(r['lines'],list) else [r['lines']]))]
report['source_files_inspected']=sorted(cache)
report['changed_during_read']=[n for n in names if hashlib.sha256((F/n).read_bytes()).hexdigest()!=hashes[n]]
(W/'outputs/c_final_register_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ['hashes','bad_source_intervals','scan_field_discrepancies','source_files_inspected']},ensure_ascii=False,indent=2))
print('BAD_SOURCE_RECORDS', {scope:sorted({r['id'] for r in bad if r['scope']==scope}) for scope in ['item','claim','problem occurrence']})
print('SCAN_FIELD_DISCREPANCIES',json.dumps(mismatch,ensure_ascii=False))
