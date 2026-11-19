"""Read-only structural audit of the assembled SA14 registers.

The output contains candidates for manual review, never inferred note verdicts.
Only files below this part's outputs directory are written.
"""
import collections,csv,datetime,hashlib,io,json,pathlib,re

B=pathlib.Path(__file__).resolve().parents[1]
W=B.parents[1]
ROOT=W.parent
names=['SA14_items.json','SA14_claims.json','SA14_problems.json','SA14_entries.tsv','SA14_readings.tsv','SA14_links.tsv','SA14_references.bib','CHECK_EVENTS.tsv','research/consolidation_aliases.json','research/entries_source.json','research/source_manifest.json','research/final_counts.json']
raw={name:(W/name).read_bytes() for name in names}
manifest={name:dict(sha256=hashlib.sha256(data).hexdigest(),bytes=len(data))for name,data in raw.items()}
def J(name):return json.loads(raw[name])
def T(name):return list(csv.DictReader(io.StringIO(raw[name].decode()),delimiter='\t'))
I=J('SA14_items.json');C=J('SA14_claims.json');P=J('SA14_problems.json');E=T('SA14_entries.tsv');R=T('SA14_readings.tsv');L=T('SA14_links.tsv');EV=T('CHECK_EVENTS.tsv')
SRC=J('research/entries_source.json');SM=J('research/source_manifest.json');A=J('research/consolidation_aliases.json')
sets={'items':{x['id']for x in I},'claims':{x['id']for x in C},'problems':{x['id']for x in P}}
aliases={k:v for cat in ('items','claims','problems')for k,v in A[cat].items()}
bib=raw['SA14_references.bib'].decode()
bibkeys=re.findall(r'(?m)^@\w+\{([^,\s]+),',bib)
refs=set(bibkeys)
issues=[]
def issue(kind,**kw):issues.append(dict(kind=kind,**kw))
def dup(xs):return {k:n for k,n in collections.Counter(xs).items()if n>1}
for kind,xs in [('items',I),('claims',C),('problems',P)]:
 for key,n in dup(x['id']for x in xs).items():issue('duplicate_id',register=kind,id=key,count=n)
for key,n in dup(bibkeys).items():issue('duplicate_bibliographic_key',key=key,count=n)
actual={e['entry_id']for e in E}
for key,n in dup(e['entry_id']for e in E).items():issue('duplicate_note_entry',id=key,count=n)
for key in sorted(set(SRC)-actual):issue('missing_note_entry',id=key)
for key in sorted(actual-set(SRC)):issue('unexpected_note_entry',id=key)
sources=collections.defaultdict(list)
for i in I:
 for s in i['sources']:
  if '#'in s:sources[s].append(i['id'])
  elif not s.startswith(('transcript:','codex-lead:')):issue('unrecognized_non_note_source',id=i['id'],source=s)
for key in sorted(set(SRC)-set(sources)):issue('note_missing_from_item_sources',id=key)
for key in sorted(set(sources)-set(SRC)):issue('unknown_note_in_item_sources',id=key)
for key,ids in sources.items():
 if len(ids)!=1:issue('note_in_multiple_items',id=key,items=ids)
for e in E:
 if e['item_id']not in sets['items']:issue('entry_item_missing',entry=e['entry_id'],target=e['item_id'])
 if sources.get(e['entry_id'])!=[e['item_id']]:issue('entry_item_source_disagrees',entry=e['entry_id'],target=e['item_id'],source_items=sources.get(e['entry_id']))
 if e['verdict']not in {'kept','merged','corrected','withdrawn','rests on a misreading'}:issue('entry_verdict_vocabulary',entry=e['entry_id'],verdict=e['verdict'])
 if not e['reason'].strip():issue('empty_entry_reason',entry=e['entry_id'])
for cat in ('items','claims','problems'):
 for old,new in A[cat].items():
  if old in sets[cat]:issue('alias_still_primary',category=cat,old=old,new=new)
  if new not in sets[cat]:issue('alias_target_missing',category=cat,old=old,new=new)
  if new in A[cat]:issue('alias_chain',category=cat,old=old,new=new)

pat=re.compile(r'(?<![A-Za-z0-9-])(?:MP-SA14-\d+|C-SA14-\d+|SA14-\d+)(?![0-9])')
allids=set().union(*sets.values())
def walk(value,path,owner):
 if isinstance(value,dict):
  for k,v in value.items():
   if k in {'source_variants','original_statement_id','original_item_id'}:continue
   walk(v,path+'.'+k,owner)
 elif isinstance(value,list):
  for n,v in enumerate(value):walk(v,path+f'[{n}]',owner)
 elif isinstance(value,str):
  for token in pat.findall(value):
   if token in aliases:issue('stale_alias_pointer',owner=owner,path=path,token=token,target=aliases[token],context=value)
   elif token not in allids:issue('unknown_identifier_in_text',owner=owner,path=path,token=token,context=value)
for kind,xs in [('items',I),('claims',C),('problems',P)]:
 for x in xs:
  walk(x,kind,x['id'])
  for field,cat in [('items','items'),('claims','claims'),('claim_ids','claims')]:
   for target in x.get(field,[]):
    if target not in sets[cat]:issue('missing_structured_pointer',owner=x['id'],field=field,target=target)
  for key in x.get('refs',[]):
   if key not in refs:issue('missing_reference_key',owner=x['id'],key=key)
for n,row in enumerate(R,2):walk(row,'readings',f'row{n}')
for n,row in enumerate(L,2):
 walk(row,'links',f'row{n}')
 for token in filter(None,re.split(r'[;\s]+',row.get('note_ids',''))):
  if token not in SRC:issue('link_note_id_not_found',row=n,token=token)
 if row['kind']=='our projects' and 'QUARANTINED'not in row['evidence'].upper():issue('project_row_not_quarantined',row=n,record=row)

files={pathlib.Path(x['file']).name:dict(x,path=ROOT/'sources'/x['file'])for x in SM}
for base,rec in files.items():
 data=rec['path'].read_bytes();rec['actual_lines']=len(data.decode().splitlines())
 if hashlib.sha256(data).hexdigest()!=rec['sha256']:issue('source_manifest_hash_mismatch',file=base)
 if rec['actual_lines']!=rec['lines']:issue('source_manifest_line_count_mismatch',file=base,manifest=rec['lines'],actual=rec['actual_lines'])

filepat=re.compile(r'(?P<file>[A-Za-z0-9_/-]+_transcription\.tex)\s*:\s*(?P<loc>[^A-Za-z\n\[\]()]*)')
range_pat=re.compile(r'(\d+)(?:\s*[–—-]\s*(\d+))?')
locator_count=0
def loc(value,owner,field):
 global locator_count
 if isinstance(value,list):
  for v in value:loc(v,owner,field)
 elif isinstance(value,dict):
  if 'file'in value and 'first'in value and 'last'in value:
   locator_count+=1;base=pathlib.Path(value['file']).name
   if base not in files:issue('locator_file_missing',owner=owner,field=field,locator=value);return
   r=files[base];first=int(value['first']);last=int(value['last'])
   if first<1 or last<first or last>r['actual_lines']:issue('locator_bounds',owner=owner,field=field,locator=value,maxline=r['actual_lines'])
   if 'scan'in value:
    matching=[s for s in r['scans']if str(s['scan'])==str(value['scan'])]
    if not matching:issue('locator_scan_missing',owner=owner,field=field,locator=value)
    elif not any(first>=s['line']and last<=s['end_line']for s in matching):issue('locator_scan_range_mismatch',owner=owner,field=field,locator=value,scan_ranges=matching)
  else:
   for k,v in value.items():
    if k in {'lines','line','occurrences'}:loc(v,owner,field+'.'+k)
 elif isinstance(value,str):
  matches=list(filepat.finditer(value))
  if not matches and value.strip():issue('unparsed_locator_for_review',owner=owner,field=field,locator=value)
  for m in matches:
   base=pathlib.Path(m['file']).name
   if base not in files:issue('locator_file_missing',owner=owner,field=field,locator=m[0]);continue
   for a,b in range_pat.findall(m['loc']):
    locator_count+=1;first=int(a);last=int(b or a)
    if first<1 or last<first or last>files[base]['actual_lines']:issue('locator_bounds',owner=owner,field=field,locator=m[0],first=first,last=last,maxline=files[base]['actual_lines'])
for kind,xs in [('items',I),('claims',C)]:
 for x in xs:
  if not x.get('lines'):issue('empty_locator_for_review',owner=x['id'],item_kind=x.get('kind'),check=x.get('check'),statement=x.get('statement'))
  loc(x.get('lines'),x['id'],'lines')
for x in P:loc(x['occurrences'],x['id'],'occurrences')
for n,row in enumerate(R,2):loc(row.get('line'),f'readings row{n}','line')
eventids={x['statement_id']for x in EV}
for key in sorted(sets['items']|sets['claims']|refs-eventids):
 if key not in eventids:issue('missing_check_event',id=key)
counts=dict(entries=len(E),items=len(I),claims=len(C),problems=len(P),readings=len(R),links=len(L),bibkeys=len(bibkeys),check_events=len(EV),note_packages=dict(collections.Counter(k.split('#')[0]for k in SRC)),links_by_kind=dict(collections.Counter(x['kind']for x in L)),locator_segments_checked=locator_count)
for key in ['entries','items','claims','problems','readings','links','check_events']:
 if J('research/final_counts.json').get(key)!=counts[key]:issue('stale_final_counts',field=key,register=counts[key],reported=J('research/final_counts.json').get(key))
changed=[name for name,data in raw.items()if (W/name).read_bytes()!=data]
result=dict(recorded_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),read_only=True,manifest=manifest,changed_during_read=changed,counts=counts,issue_counts=dict(collections.Counter(x['kind']for x in issues)),candidates=issues)
(B/'outputs/final_crossregister_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k]for k in ['recorded_at_utc','changed_during_read','counts','issue_counts']},ensure_ascii=False,indent=2))
