from pathlib import Path
import concurrent.futures, datetime, hashlib, json, re, urllib.request, urllib.error

BASE=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
SOURCES={
 'geotoppos_index': 'https://www.geotoppos.org/pdf-archive.html',
 'course1973_metadata': 'https://archive.org/metadata/topologicalvecto00grot',
 'course_request_notice': 'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/Ask.pdf',
}
def retrieve(item):
 name,url=item
 record={'name':name,'url':url}
 try:
  response=urllib.request.urlopen(url,timeout=35)
  content=response.read()
  text=content.decode('utf-8',errors='replace')
  record.update(status=response.status,final_url=response.url,content_type=response.headers.get('content-type'),bytes=len(content),sha256=hashlib.sha256(content).hexdigest())
  suffix='.pdf' if name=='course_request_notice' else '.json' if name.endswith('metadata') else '.html'
  dest=BASE/'sources'/('geometry_editorial_'+name+suffix)
  dest.write_bytes(content)
  record['cache']=str(dest.relative_to(BASE))
  if name=='geotoppos_index':
   record['script_sources']=re.findall(r'<script[^>]+src=[\"\']([^\"\']+)',text)
   record['FDF_lines']=[line for line in text.splitlines() if 'FDF' in line or 'fetch(' in line]
  if name.endswith('metadata') and response.status==200:
   data=json.loads(content)
   record['metadata']=data.get('metadata',{})
   record['files']=[{k:f.get(k) for k in ['name','format','private','size']} for f in data.get('files',[])]
 except Exception as exc:
  record['error']=repr(exc)
 return record
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 records=list(pool.map(retrieve,SOURCES.items()))
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'records':records,'scope':'Public metadata and linked request notice only; no account, email, or controlled full text accessed.'}
(BASE/'logs/geometry_editorial_retrieval.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False))
