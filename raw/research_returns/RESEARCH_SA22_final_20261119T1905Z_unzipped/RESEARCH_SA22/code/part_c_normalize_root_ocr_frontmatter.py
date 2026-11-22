"""Apply exactly the authorized165-field root OCR cache normalization.

Only the target JSON is replaced. Its TXT companion and all unselected JSON
values remain unchanged. No retrieval or mathematical checks are performed.
"""
import copy,datetime,hashlib,json,pathlib,time
ROOT=pathlib.Path(__file__).resolve().parents[1]
PLAN=ROOT/'checks/part_c_root_ocr_frontmatter_plan.json'
PLAN_SHA='a9b418e6a3fae5e242d43992635e6cb0f780197de4f59e74fda1504219575c5e'
MANIFEST=ROOT/'checks/part_c_root_ocr_frontmatter_normalization_manifest.json'
OUTPUT=ROOT/'code/part_c_normalize_root_ocr_frontmatter_output.json'
START=datetime.datetime.now(datetime.timezone.utc).isoformat();T=time.perf_counter()
def sha(b):return hashlib.sha256(b).hexdigest()
assert not MANIFEST.exists() and not OUTPUT.exists(),'Do not overwrite an earlier execution record.'
planraw=PLAN.read_bytes();assert sha(planraw)==PLAN_SHA;plan=json.loads(planraw)
target=plan['target'];P=ROOT/target['path'];raw=P.read_bytes()
assert len(raw)==target['bytes'] and sha(raw)==target['sha256']
companion=plan['companion'];TXT=ROOT/companion['path'];txtraw=TXT.read_bytes()
assert len(txtraw)==704==companion['bytes'] and sha(txtraw)==companion['sha256']
old=json.loads(raw);new=copy.deepcopy(old);fields=target['fields'];assert len(fields)==165
BACKUP=pathlib.Path(plan['raw_backup_proposal'])
replacements=[]
for row in fields:
 i=row['record_index'];assert row['pointer']==f'/results/{i}/frontmatter'
 s=old['results'][i]['frontmatter'];assert isinstance(s,str)
 assert len(s)==row['original_characters'] and len(s.encode())==row['original_utf8_bytes'] and sha(s.encode())==row['original_sha256']
 replacement={'kind':'raw_source_frontmatter_cache_reference','raw_cache_path':str(BACKUP),'original_json_pointer':row['pointer'],'original_characters':row['original_characters'],'original_utf8_bytes':row['original_utf8_bytes'],'original_sha256':row['original_sha256']}
 new['results'][i]['frontmatter']=replacement
 replacements.append({'identifier':row['identifier'],**replacement})
oldmasked=copy.deepcopy(old);newmasked=copy.deepcopy(new)
for row in fields:
 i=row['record_index'];oldmasked['results'][i]['frontmatter']='<SELECTED_RAW_CACHE>';newmasked['results'][i]['frontmatter']='<SELECTED_RAW_CACHE>'
assert oldmasked==newmasked,'Unselected JSON value changed.'
normalized=(json.dumps(new,ensure_ascii=False,indent=2)+'\n').encode()
# Exact original backup is complete and verified before the only source edit.
BACKUP.parent.mkdir(parents=True,exist_ok=True)
if BACKUP.exists():assert BACKUP.read_bytes()==raw
else:
 with BACKUP.open('xb') as f:f.write(raw)
assert sha(BACKUP.read_bytes())==target['sha256']
assert P.read_bytes()==raw and TXT.read_bytes()==txtraw
P.write_bytes(normalized);assert P.read_bytes()==normalized
assert TXT.read_bytes()==txtraw
after=json.loads(P.read_bytes())
for row in fields:after['results'][row['record_index']]['frontmatter']='<SELECTED_RAW_CACHE>'
assert after==oldmasked
manifest={'operation':'Exact parent-authorized single-file frontmatter normalization; all165fields and original file hash preflighted; exact external backup verified before edit; all other JSON values and TXT bytes verified unchanged.','started_utc':START,'plan_path':str(PLAN.relative_to(ROOT)),'plan_sha256':PLAN_SHA,'target_path':target['path'],'original_bytes':len(raw),'original_sha256':sha(raw),'raw_backup_path':str(BACKUP),'raw_backup_sha256':sha(BACKUP.read_bytes()),'normalized_bytes':len(normalized),'normalized_sha256':sha(normalized),'selected_fields':165,'replacements':replacements,'unselected_json_values_equal':True,'companion':{'path':companion['path'],'bytes':len(txtraw),'sha256':sha(txtraw),'byte_identical_after':True},'original_total_seconds_preserved':old['seconds'],'network_requests':0,'mathematical_checks':0,'other_existing_files_edited':0,'theorem_or_source_status_changes':0}
with MANIFEST.open('x') as f:f.write(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
out={'started_utc':START,'runtime_seconds':time.perf_counter()-T,'normalized_files':1,'selected_fields':165,'original_bytes':len(raw),'normalized_bytes':len(normalized),'original_sha256':sha(raw),'normalized_sha256':sha(normalized),'manifest_path':str(MANIFEST.relative_to(ROOT)),'manifest_sha256':sha(MANIFEST.read_bytes()),'raw_backup_path':str(BACKUP),'txt_companion_unchanged':True,'unselected_json_values_equal':True,'network_requests':0,'mathematical_checks':0,'other_existing_files_edited':0,'theorem_or_source_status_changes':0}
with OUTPUT.open('x') as f:f.write(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
