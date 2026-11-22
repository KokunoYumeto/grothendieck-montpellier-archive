"""Read-only deliverable hygiene inventory; no source requests or mathematical tests.

Creates its own inventories only. Never rewrites an input or immutable checkpoint.
Long embedded strings are identified by field pointer, size and hash, never copied.
"""
import csv, datetime, hashlib, json, pathlib, re, time

ROOT=pathlib.Path(__file__).resolve().parents[1]
START=datetime.datetime.now(datetime.timezone.utc).isoformat(); TICK=time.perf_counter()
SELF_PREFIX='part_c_source_cache_hygiene'
RAW_DIRECT={
 'notes/a567_review_Solynin1999.txt':'raw_nonuser_literature_text',
 'notes/part_c_archive_index.html':'raw_public_archive_html',
 'notes/original_scans_a567/hoshi_rims1558_pdf_56.png':'raw_nonuser_literature_page',
 'notes/original_scans_a567/hoshi_rims1558_pdf_61.png':'raw_nonuser_literature_page',
 'notes/original_scans_a567/hoshi_rims1558_pdf_65.png':'raw_nonuser_literature_page',
}

def digest(b): return hashlib.sha256(b).hexdigest()
def pointer(path): return '/'+ '/'.join(str(x).replace('~','~0').replace('/','~1') for x in path)
def strings(obj,path=()):
 if isinstance(obj,str): yield path,obj
 elif isinstance(obj,dict):
  for k,v in obj.items(): yield from strings(v,path+(k,))
 elif isinstance(obj,list):
  for i,v in enumerate(obj): yield from strings(v,path+(i,))
def current_filter(rel):
 p=pathlib.PurePosixPath(rel)
 if '__pycache__' in p.parts or 'tex-runtime' in p.parts:return False
 if p.parts[0]=='qa' and not p.name.startswith('paper'):return False
 if p.parts[0]=='sources' and p.suffix not in {'.bib','.json','.csv','.tsv','.out','.log','.ris'}:return False
 return p.suffix not in {'.zip','.fmt'} and rel!='CHECKPOINT_CONTENTS.txt'

inventory=[]; fields=[]; plain=[]; jsons=0
for p in sorted(ROOT.rglob('*')):
 if not p.is_file(): continue
 rel=p.relative_to(ROOT).as_posix(); parts=p.relative_to(ROOT).parts
 if parts[0]=='sources' or '__pycache__' in parts or 'tex-runtime' in parts:continue
 if p.name.startswith(SELF_PREFIX) or rel.startswith('checks/part_c_embedded_source_'):continue
 category=None; data=None
 if rel in RAW_DIRECT: category=RAW_DIRECT[rel]
 elif parts[0]=='qa':
  if p.name.startswith('paper'):category='generated_paper_QA'
  elif p.name.startswith(('cote','part_b_c2_scan','part_c_functor_scan')):category='user_manuscript_page'
  else:category='raw_nonuser_literature_QA'
 elif rel.startswith('notes/original_scans_a567/'):
  category='user_manuscript_page'
 elif parts[0]=='notes' and p.suffix in {'.txt','.html','.pdf','.png','.jpg','.jpeg','.djvu'}:
  category='other_note_file_manual_review'
 elif parts[0]=='code' and p.suffix in {'.json','.txt','.out'}:
  data=p.read_bytes()
  try: obj=json.loads(data)
  except (ValueError,UnicodeDecodeError):
   if len(data)>1000:
    plain.append({'path':rel,'bytes':len(data),'sha256':digest(data)})
   continue
  jsons+=1; hits=[]
  for path,s in strings(obj):
   last=next((str(x) for x in reversed(path) if isinstance(x,str)),'')
   if len(s)>=500 and (re.search(r'text|body|html|frontmatter|abstract|description|summary|content|excerpt|ocr',last,re.I) or ('content' in path and last=='text')):
    hits.append({'path':rel,'pointer':pointer(path),'characters':len(s),'utf8_bytes':len(s.encode()),'field_sha256':digest(s.encode()),'field_type':'catalogue_description_or_abstract' if re.search(r'abstract|description|summary',last,re.I) else 'embedded_text_body'})
  if hits:
   fields.extend(hits); category='embedded_body_fields_manual_classification'
 if category:
  if data is None:data=p.read_bytes()
  st=p.stat()
  inventory.append({'path':rel,'category':category,'bytes':len(data),'sha256':digest(data),'currently_included':current_filter(rel),'mtime_ns':st.st_mtime_ns})

inv=ROOT/'checks/part_c_source_cache_inventory.tsv'
with inv.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['path','category','bytes','sha256','currently_included','mtime_ns'],delimiter='\t');w.writeheader();w.writerows(inventory)
fp=ROOT/'checks/part_c_embedded_source_fields.tsv'
with fp.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['path','pointer','characters','utf8_bytes','field_sha256','field_type'],delimiter='\t');w.writeheader();w.writerows(fields)
counts={}
for r in inventory:
 c=counts.setdefault(r['category'],{'files':0,'bytes':0,'currently_included_files':0});c['files']+=1;c['bytes']+=r['bytes'];c['currently_included_files']+=int(r['currently_included'])
out={'started_utc':START,'runtime_seconds':time.perf_counter()-TICK,'scope':'Read-only current-project inventory outside sources/. No source requests, mathematical tests, input edits or checkpoint changes. Embedded strings are represented only by pointers/counts/hashes. Heuristic hits require manual classification.','network_requests':0,'mathematical_checks':0,'json_payload_files_inspected':jsons,'inventory_file':str(inv.relative_to(ROOT)),'inventory_sha256':digest(inv.read_bytes()),'embedded_fields_file':str(fp.relative_to(ROOT)),'embedded_fields_sha256':digest(fp.read_bytes()),'embedded_field_count':len(fields),'counts':counts,'unparsed_large_text_outputs_for_manual_review':plain}
dest=ROOT/'code/part_c_source_cache_hygiene_output.json';dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
