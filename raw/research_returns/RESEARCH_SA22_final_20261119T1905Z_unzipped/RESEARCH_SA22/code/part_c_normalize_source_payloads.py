"""Normalize exactly the parent's authorized 11 files / 51 fields or blocks.

Preflight every original hash before writes; keep exact raw files outside the
deliverable. Preserve all unselected metadata and matching JSON/TXT pairs.
No searches, source downloads, mathematical tests, or checkpoint changes.
"""
import copy,datetime,hashlib,json,pathlib,re,time
ROOT=pathlib.Path(__file__).resolve().parents[1]
PLAN=ROOT/'checks/part_c_source_cache_plan.json'
PLAN_SHA='fb942241adada341bd6fd565c29243184c4703c9e7d03438121692c2e2f8bf5a'
CACHE=ROOT.parent/'source_reading/recorded_source_payloads'
START=datetime.datetime.now(datetime.timezone.utc).isoformat();TICK=time.perf_counter()
def sha(b):return hashlib.sha256(b).hexdigest()
def parts(ptr):return [x.replace('~1','/').replace('~0','~') for x in ptr.strip('/').split('/')]
def at(o,ptr):
 for k in parts(ptr):o=o[int(k)] if isinstance(o,list) else o[k]
 return o
def put(o,ptr,v):
 ks=parts(ptr)
 for k in ks[:-1]:o=o[int(k)] if isinstance(o,list) else o[k]
 k=ks[-1];o[int(k) if isinstance(o,list) else k]=v
def segment(s,pattern,idx):
 matches=list(re.finditer(pattern,s));bounds=[0]+[m.end() for m in matches]
 ends=[m.start() for m in matches]+[len(s)]
 return bounds[idx],ends[idx],len(bounds)
def ranges(values):
 values=sorted(set(values));out=[]
 for v in values:
  if not out or v>out[-1][1]+1:out.append([v,v])
  else:out[-1][1]=v
 return out

raw_plan=PLAN.read_bytes();assert sha(raw_plan)==PLAN_SHA
plan=json.loads(raw_plan);rows=plan['embedded_source_normalization']
assert len(rows)==11
assert sum(len(r['fields']) for r in rows)==51
by_path={r['path']:r for r in rows};prepared=[]
titles={
 'part_a567_fujiwara1992_system1_queries.json':'Algebraic Tubular Neighborhoods II (David A. Cox,1978)',
 'part_a567_fujiwara_ias_discovery_1634.json':'Report for the Academic Year1991–92 (Institute for Advanced Study)',
 'part_a567_fujiwara_ias_provenance_1635.json':'Report for the Academic Year1991–92 (Institute for Advanced Study)',
 'part_b_lieberman_variants_web_output.json':'Original mathematical passage on the standard conjectures',
 'part_c_pfluger_distinct_search1.json':'Conformal Welding (original chapter excerpt)',
}

# Validate all inputs and selected bodies before any reviewed file is changed.
for row in rows:
 p=ROOT/row['path'];raw=p.read_bytes();assert len(raw)==row['bytes'] and sha(raw)==row['sha256'],row['path']
 original=json.loads(raw);changed=copy.deepcopy(original)
 canonical=row['path']
 if p.suffix=='.txt':
  candidate=str(pathlib.PurePosixPath(row['path']).with_suffix('.json'))
  if candidate in by_path and by_path[candidate]['sha256']==row['sha256']:canonical=candidate
 reference=CACHE/pathlib.PurePosixPath(canonical).name
 field_records=[]
 for f in row['fields']:
  old=at(original,f['pointer']);assert isinstance(old,str)
  assert len(old)==f['field_characters'] and sha(old.encode())==f['field_sha256']
  record={'pointer':f['pointer'],'mode':f['mode'],'original_field_characters':len(old),'original_field_sha256':sha(old.encode()),'canonical_raw_cache_path':str(reference)}
  if f['mode']=='whole_string':
   replacement={'kind':'raw_source_text_cache_reference','raw_cache_path':str(reference),'original_json_pointer':f['pointer'],'original_characters':len(old),'original_utf8_bytes':len(old.encode()),'original_sha256':sha(old.encode()),'note':'Raw third-party source text is retained verbatim outside the deliverable; surrounding source/page and execution metadata remain unchanged.'}
  else:
   begin,end,count=segment(old,f['separator_regex'],f['zero_based_block']);block=old[begin:end]
   assert count==f['block_count'] and sha(block.encode())==f['block_sha256']
   locator={'source_line_ranges':ranges(map(int,re.findall(r'(?m)^L(\d+)',block))),'zero_based_pdf_pages':sorted(set(map(int,re.findall(r'@P(\d+)',block))))}
   metadata={'title':titles[p.name],'urls':f['urls'],'reference_ids':f['reference_ids'],'locators':locator,'raw_cache_path':str(reference),'original_json_pointer':f['pointer'],'zero_based_source_block':f['zero_based_block'],'original_block_characters':len(block),'original_block_utf8_bytes':len(block.encode()),'original_block_sha256':sha(block.encode())}
   stub='[Raw third-party source body retained in the external cache; metadata follows.]\n'+json.dumps(metadata,ensure_ascii=False,indent=2)
   replacement=old[:begin]+stub+old[end:]
   assert replacement[:begin]==old[:begin] and replacement.endswith(old[end:])
   record.update(original_block_sha256=f['block_sha256'],zero_based_block=f['zero_based_block'],source_metadata=metadata)
  put(changed,f['pointer'],replacement);field_records.append(record)
 # Exact structural equality after masking selected fields verifies all other data.
 masked_original=copy.deepcopy(original);masked_changed=copy.deepcopy(changed)
 for f in row['fields']:put(masked_original,f['pointer'],'<SELECTED>');put(masked_changed,f['pointer'],'<SELECTED>')
 assert masked_original==masked_changed
 normalized=(json.dumps(changed,ensure_ascii=False,indent=2)+'\n').encode()
 prepared.append({'row':row,'path':p,'raw':raw,'normalized':normalized,'backup':CACHE/p.name,'fields':field_records})

# Preserve JSON/TXT equality where the historical originals were identical.
prepared_by_path={x['row']['path']:x for x in prepared}
pair_checks=[]
for item in prepared:
 if item['path'].suffix=='.txt':
  jp=str(pathlib.PurePosixPath(item['row']['path']).with_suffix('.json'))
  if jp in prepared_by_path and item['raw']==prepared_by_path[jp]['raw']:
   assert item['normalized']==prepared_by_path[jp]['normalized']
   pair_checks.append([jp,item['row']['path']])

# All backups are complete and verified before the first in-project replacement.
CACHE.mkdir(parents=True,exist_ok=True)
for item in prepared:
 b=item['backup']
 if b.exists():assert b.read_bytes()==item['raw'],str(b)
 else:
  with b.open('xb') as f:f.write(item['raw'])
 assert sha(b.read_bytes())==item['row']['sha256']
for item in prepared:assert sha(item['path'].read_bytes())==item['row']['sha256']
records=[]
for item in prepared:
 item['path'].write_bytes(item['normalized'])
 assert item['path'].read_bytes()==item['normalized']
 records.append({'path':item['row']['path'],'original_bytes':len(item['raw']),'original_sha256':sha(item['raw']),'raw_backup_path':str(item['backup']),'raw_backup_sha256':sha(item['backup'].read_bytes()),'normalized_bytes':len(item['normalized']),'normalized_sha256':sha(item['normalized']),'selected_fields_or_blocks':item['fields']})

manifest={'operation':'Parent-authorized normalization only. Every original input/hash and selected field/block verified before writes; every raw backup verified before first replacement. All unselected metadata and matching JSON/TXT pairs preserved.','started_utc':START,'plan_path':str(PLAN.relative_to(ROOT)),'plan_sha256':PLAN_SHA,'records':records,'identical_json_txt_pairs_verified':pair_checks,'direct_exclusion_files_edited':0,'optional_thumbnail_fields_edited':0,'network_requests':0,'mathematical_checks':0}
dest=ROOT/'checks/part_c_source_cache_normalization_manifest.json';dest.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
out={'started_utc':START,'runtime_seconds':time.perf_counter()-TICK,'normalized_files':len(records),'normalized_fields_or_blocks':sum(len(r['selected_fields_or_blocks']) for r in records),'original_bytes':sum(r['original_bytes'] for r in records),'normalized_bytes':sum(r['normalized_bytes'] for r in records),'json_txt_pairs_verified':len(pair_checks),'manifest_path':str(dest.relative_to(ROOT)),'manifest_sha256':sha(dest.read_bytes()),'raw_backup_directory':str(CACHE),'network_requests':0,'mathematical_checks':0,'checkpoint_files_changed':0,'direct_exclusion_files_edited':0,'optional_thumbnail_fields_edited':0}
output=ROOT/'code/part_c_normalize_source_payloads_output.json';output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
