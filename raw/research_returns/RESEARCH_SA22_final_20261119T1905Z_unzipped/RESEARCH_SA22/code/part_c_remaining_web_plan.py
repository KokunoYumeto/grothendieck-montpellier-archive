"""Prepare a second exact source-prose normalization plan, read-only.

Manual classifications distinguish prose from factual bibliographies/holdings.
This script stores identifiers, offsets and hashes, not the selected raw prose.
"""
import datetime,hashlib,json,pathlib,re,time
ROOT=pathlib.Path(__file__).resolve().parents[1]
START=datetime.datetime.now(datetime.timezone.utc).isoformat();T=time.perf_counter()
def sha(b):return hashlib.sha256(b).hexdigest()
def at(o,p):
 for k in p.strip('/').split('/'):o=o[int(k)] if isinstance(o,list) else o[k]
 return o
inventory=json.loads((ROOT/'checks/part_c_remaining_web_body_inventory.json').read_text())
by={(r['path'],r['zero_based_block']):r for r in inventory['blocks']}
whole={
 'part_a567_fujiwara1992_system1_queries.json':[2,3,6],
 'part_a567_fujiwara1992_targeted_queries.json':[2,4],
 'part_a567_fujiwara_contemporary_ias_refs.json':[3,5,6],
 'part_a567_fujiwara_distinct_search_1633.json':[1,3,11,17,20],
 'part_a567_fujiwara_ias_discovery_1634.json':[2,9],
 'part_a567_pfluger_offprint_domain_query.json':[0,7],
 'part_a567_pfluger_offprint_institutional_queries.json':[4,5],
 'part_a567_pfluger_offprint_queries.json':[4,6,8,9],
 'part_a567_pfluger_offprint_variant_queries.json':[9,13],
 'part_a567_pfluger_offprint_variant_verification.json':[7],
 'part_b_lieberman_variants_web_output.json':[0,1,3,4,5,6,7,8,9],
 'part_c_pfluger_distinct_search3.json':[1,3,8],
}
selected=[]
def add(name,i,mode,pattern=None):
 path='code/'+name;r=by[(path,i)];p=ROOT/path;raw=p.read_bytes()
 assert len(raw)==r['file_bytes'] and sha(raw)==r['file_sha256']
 obj=json.loads(raw);field=at(obj,r['pointer']);assert sha(field.encode())==r['field_sha256']
 sep=list(re.finditer(r'\n-{8,}\n',field));starts=[0]+[m.end() for m in sep];ends=[m.start() for m in sep]+[len(field)]
 begin,end=starts[i],ends[i];block=field[begin:end];assert sha(block.encode())==r['block_sha256']
 targets=[(0,len(block))] if mode=='whole_source_block' else [(m.start(),m.end()) for m in re.finditer(pattern,block,re.M)]
 assert targets,(name,i,pattern)
 for a,b in targets:
  text=block[a:b]
  selected.append({'path':path,'file_bytes':len(raw),'file_sha256':sha(raw),'pointer':r['pointer'],'field_sha256':r['field_sha256'],'mode':mode,'zero_based_block':i,'block_count':r['block_count'],'block_sha256':r['block_sha256'],'field_start_character':begin+a,'field_end_character':begin+b,'selected_characters':b-a,'selected_utf8_bytes':len(text.encode()),'selected_sha256':sha(text.encode()),'header':r['header'],'reference_ids':r['reference_ids'],'urls':r['urls'],'source_line_numbers':list(map(int,re.findall(r'(?m)^L(\d+):',text))),'reason':'Actual third-party narrative, abstract, mathematical excerpt or policy prose. Preserve external raw bytes and replace only this selected range with source provenance metadata.'})
for name,inds in whole.items():
 for i in inds:add(name,i,'whole_source_block')
# Bibliographies, catalogue entries, forms and holdings remain byte-for-byte;
# select only the actual prose paragraphs/lines mixed into these five blocks.
for i in [0,2]:add('part_a567_fujiwara_ias_queries_1637.json',i,'prose_span',r'^> The author considers[^\n]*')
add('part_b_lieberman_archival_queries1_output.json',8,'prose_span',r'"In 1862,[\s\S]*?\(DSB VI p\. 307\)')
add('part_c_pfluger_distinct_search3.json',2,'prose_span',r'#### The Indian Mathematical Society[^\n]*')
add('root_public_catalogues_open_web.json',1,'prose_span',r'^L(?:280|281|282|287|355|356|357|358):[^\n]*')
files=sorted(set(r['path'] for r in selected))
# Offsets are nonoverlapping in each content/text field; applying descending
# offsets preserves all unselected data, including mixed catalogue content.
for path in files:
 rr=sorted((r for r in selected if r['path']==path),key=lambda r:r['field_start_character'])
 for a,b in zip(rr,rr[1:]):assert a['field_end_character']<=b['field_start_character'],path
plan={'snapshot_utc':START,'scope':'Read-only exact second proposal. All selected ranges occur in actual MCP web content/text fields. No authored/certificate output is selected. Pure bibliographic/holdings/identifier records and unselected mixed-record data remain intact. Parent authorization is required before replacement.','selection_count':len(selected),'selected_file_count':len(files),'whole_source_blocks':sum(r['mode']=='whole_source_block' for r in selected),'prose_spans':sum(r['mode']=='prose_span' for r in selected),'selected_utf8_bytes':sum(r['selected_utf8_bytes'] for r in selected),'files':files,'selected_ranges':selected,'brief_snippets_retained_note':'Incidental very short snippets in otherwise factual bibliography, provenance, funding, access or holdings records are not treated as substantial source bodies. Source headings, author names, identifiers, dates and menu/form entries are retained.','network_requests':0,'mathematical_checks':0,'reviewed_files_changed':0}
dest=ROOT/'checks/part_c_remaining_web_normalization_plan.json';dest.write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
out={'started_utc':START,'runtime_seconds':time.perf_counter()-T,'plan_path':str(dest.relative_to(ROOT)),'plan_sha256':sha(dest.read_bytes()),'selected_files':len(files),'selected_ranges':len(selected),'whole_source_blocks':plan['whole_source_blocks'],'prose_spans':plan['prose_spans'],'selected_utf8_bytes':plan['selected_utf8_bytes'],'network_requests':0,'mathematical_checks':0,'reviewed_files_changed':0}
(ROOT/'code/part_c_remaining_web_plan_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
