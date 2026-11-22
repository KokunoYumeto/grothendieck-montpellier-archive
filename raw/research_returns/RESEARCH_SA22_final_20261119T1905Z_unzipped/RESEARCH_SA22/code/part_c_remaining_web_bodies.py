"""Read-only inventory of saved MCP web source blocks; no retrieval or tests.

Records identifiers/counts/hashes only, never recopies a source body. The
result is an audit aid, not a proposed blanket deletion or normalization.
"""
import datetime, hashlib, json, pathlib, re, time
ROOT=pathlib.Path(__file__).resolve().parents[1]
START=datetime.datetime.now(datetime.timezone.utc).isoformat(); T=time.perf_counter()
def sha(b): return hashlib.sha256(b).hexdigest()
def escape(s): return str(s).replace('~','~0').replace('/','~1')
def walk(x, p=''):
 if isinstance(x,dict):
  for k,v in x.items():
   q=p+'/'+escape(k)
   if k=='content' and isinstance(v,list):
    for i,c in enumerate(v):
     if isinstance(c,dict) and c.get('type')=='text' and isinstance(c.get('text'),str):
      yield q+'/'+str(i)+'/text',c['text']
   yield from walk(v,q)
 elif isinstance(x,list):
  for i,v in enumerate(x): yield from walk(v,p+'/'+str(i))
rows=[]; file_count=0
for f in sorted((ROOT/'code').iterdir()):
 if f.suffix.lower() not in {'.json','.txt','.out'} or not f.is_file(): continue
 try: raw=f.read_bytes(); data=json.loads(raw)
 except (ValueError,UnicodeDecodeError): continue
 fields=list(walk(data))
 if not fields: continue
 file_count+=1
 for pointer,text in fields:
  if not re.search(r'【turn\w+】|Source: (?:open|click|find)|\[wordlim ',text): continue
  blocks=re.split(r'\n-{8,}\n',text)
  for i,block in enumerate(blocks):
   if not block.strip(): continue
   lines=block.strip().splitlines(); header=lines[0]
   refs=sorted(set(re.findall(r'turn[\w]+',block)))
   urls=sorted(set(re.findall(r'https?://[^\s<>\]\)"\\]+',block)))
   # A normalized body already contains its own cache reference; do not treat
   # the metadata stub as a remaining raw source body.
   normalized=('Raw third-party source body retained in the external cache' in block)
   rows.append({'path':str(f.relative_to(ROOT)),'file_bytes':len(raw),'file_sha256':sha(raw),'pointer':pointer,'field_sha256':sha(text.encode()),'zero_based_block':i,'block_count':len(blocks),'block_characters':len(block),'block_words':len(block.split()),'block_sha256':sha(block.encode()),'header':header,'reference_ids':refs,'urls':urls,'already_normalized':normalized})
dest=ROOT/'checks/part_c_remaining_web_body_inventory.json'
dest.write_text(json.dumps({'snapshot_utc':START,'scope':'Existing code JSON/TXT/OUT only; actual MCP content/text fields with web provenance markers. Metadata inventory, not an exclusion or authorization.','blocks':rows},ensure_ascii=False,indent=2)+'\n')
out={'started_utc':START,'runtime_seconds':time.perf_counter()-T,'files_with_mcp_content':file_count,'source_blocks_inventoried':len(rows),'already_normalized_blocks':sum(r['already_normalized'] for r in rows),'inventory_path':str(dest.relative_to(ROOT)),'inventory_sha256':sha(dest.read_bytes()),'network_requests':0,'mathematical_checks':0,'reviewed_files_changed':0}
(ROOT/'code/part_c_remaining_web_bodies_output.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
