"""Apply exactly the parent-authorized second source-cache plan.

Preflight all files/ranges, back up original bytes outside the project, then
replace only the fifty specified ranges. No network or mathematical tests.
"""
import copy,datetime,hashlib,json,pathlib,time
ROOT=pathlib.Path(__file__).resolve().parents[1]
PLAN=ROOT/'checks/part_c_remaining_web_normalization_plan.json'
PLAN_SHA='f380aa4e4e727ddc844feb3349604d3944a991feef5cb79fdefaced2e4c2bfce'
CACHE=ROOT.parent/'source_reading/recorded_web_prose_second_pass'
START=datetime.datetime.now(datetime.timezone.utc).isoformat();T=time.perf_counter()
def sha(b):return hashlib.sha256(b).hexdigest()
def keys(p):return [s.replace('~1','/').replace('~0','~') for s in p.strip('/').split('/')]
def at(o,p):
 for k in keys(p):o=o[int(k)] if isinstance(o,list) else o[k]
 return o
def put(o,p,value):
 ks=keys(p)
 for k in ks[:-1]:o=o[int(k)] if isinstance(o,list) else o[k]
 k=ks[-1];o[int(k) if isinstance(o,list) else k]=value
rawplan=PLAN.read_bytes();assert sha(rawplan)==PLAN_SHA
plan=json.loads(rawplan);rows=plan['selected_ranges']
assert len(rows)==50 and len(set(r['path'] for r in rows))==15
prepared=[]
for name in sorted(set(r['path'] for r in rows)):
 rr=[r for r in rows if r['path']==name];p=ROOT/name;raw=p.read_bytes()
 assert len(raw)==rr[0]['file_bytes'] and sha(raw)==rr[0]['file_sha256'],name
 old=json.loads(raw);new=copy.deepcopy(old);records=[];cache=CACHE/p.name
 for pointer in sorted(set(r['pointer'] for r in rr)):
  field=at(old,pointer);selected=sorted((r for r in rr if r['pointer']==pointer),key=lambda r:r['field_start_character'])
  assert sha(field.encode())==selected[0]['field_sha256']
  cursor=0;pieces=[];unchanged=[]
  for r in selected:
   a,b=r['field_start_character'],r['field_end_character']
   assert cursor<=a<b<=len(field)
   body=field[a:b]
   assert len(body)==r['selected_characters'] and len(body.encode())==r['selected_utf8_bytes'] and sha(body.encode())==r['selected_sha256']
   untouched=field[cursor:a];pieces.append(untouched);unchanged.append({'original_start':cursor,'original_end':a,'sha256':sha(untouched.encode())})
   metadata={k:r[k] for k in ['header','reference_ids','urls','source_line_numbers','zero_based_block','mode','selected_characters','selected_utf8_bytes','selected_sha256']}
   metadata.update(raw_cache_path=str(cache),original_json_pointer=pointer,original_field_start_character=a,original_field_end_character=b)
   stub='[Third-party source prose retained verbatim in the external cache; provenance metadata follows.]\n'+json.dumps(metadata,ensure_ascii=False,indent=2)
   pieces.append(stub);records.append({'pointer':pointer,'original_field_sha256':sha(field.encode()),'metadata':metadata});cursor=b
  untouched=field[cursor:];pieces.append(untouched);unchanged.append({'original_start':cursor,'original_end':len(field),'sha256':sha(untouched.encode())})
  replacement=''.join(pieces)
  # Every even-indexed segment is copied directly from the original field;
  # this verifies exact retention of all unselected catalogue/body portions.
  assert len(pieces)==2*len(selected)+1
  assert all(sha(pieces[2*i].encode())==s['sha256'] for i,s in enumerate(unchanged))
  put(new,pointer,replacement)
  records.append({'pointer':pointer,'unselected_segments':unchanged,'new_field_sha256':sha(replacement.encode())})
 oldmasked=copy.deepcopy(old);newmasked=copy.deepcopy(new)
 for pointer in set(r['pointer'] for r in rr):put(oldmasked,pointer,'<SELECTED_CONTENT_FIELD>');put(newmasked,pointer,'<SELECTED_CONTENT_FIELD>')
 assert oldmasked==newmasked
 cooked=(json.dumps(new,ensure_ascii=False,indent=2)+'\n').encode()
 prepared.append({'path':p,'name':name,'raw':raw,'cooked':cooked,'backup':cache,'records':records})
# All exact raw backups are verified before any in-project replacement.
CACHE.mkdir(parents=True,exist_ok=True)
for x in prepared:
 if x['backup'].exists():assert x['backup'].read_bytes()==x['raw']
 else:
  with x['backup'].open('xb') as f:f.write(x['raw'])
 assert sha(x['backup'].read_bytes())==sha(x['raw'])
for x in prepared:assert x['path'].read_bytes()==x['raw']
files=[]
for x in prepared:
 x['path'].write_bytes(x['cooked']);assert x['path'].read_bytes()==x['cooked']
 files.append({'path':x['name'],'original_bytes':len(x['raw']),'original_sha256':sha(x['raw']),'raw_backup_path':str(x['backup']),'raw_backup_sha256':sha(x['backup'].read_bytes()),'normalized_bytes':len(x['cooked']),'normalized_sha256':sha(x['cooked']),'range_and_retention_records':x['records']})
manifest={'operation':'Exact parent-authorized second source-cache normalization; complete preflight and external raw backups before writes; all unselected metadata/body spans preserved. No earlier manifest or archive changed.','started_utc':START,'plan_path':str(PLAN.relative_to(ROOT)),'plan_sha256':PLAN_SHA,'selected_ranges':50,'files':files,'network_requests':0,'mathematical_checks':0,'direct_exclusion_files_edited':0,'prior_archives_edited':0}
dest=ROOT/'checks/part_c_remaining_web_normalization_manifest.json';assert not dest.exists()
dest.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
out={'started_utc':START,'runtime_seconds':time.perf_counter()-T,'normalized_files':len(files),'selected_ranges':50,'original_bytes':sum(r['original_bytes'] for r in files),'normalized_bytes':sum(r['normalized_bytes'] for r in files),'manifest_path':str(dest.relative_to(ROOT)),'manifest_sha256':sha(dest.read_bytes()),'raw_backup_directory':str(CACHE),'network_requests':0,'mathematical_checks':0,'direct_exclusion_files_edited':0,'prior_archives_edited':0}
(ROOT/'code/part_c_normalize_remaining_web_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
