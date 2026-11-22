from pathlib import Path
import urllib.request, urllib.parse, datetime, time, concurrent.futures, json

base=Path('/workspace/scratch/9c53b536a97f/RESEARCH_SA22')
queries=[
 ('ia_thesis_author','creator:Lieberman AND (title:cycles OR title:algebraic)'),
 ('ia_thesis_year','title:("Algebraic cycles") AND year:1966'),
 ('ia_volume_without_year','title:("American Journal of Mathematics") AND (volume:90 OR title:90 OR identifier:*1968*)')
]
targets=[]
for label,query in queries:
 params=[('q',query),('fl[]','identifier'),('fl[]','title'),('fl[]','date'),('fl[]','creator'),('fl[]','volume'),('fl[]','access-restricted-item'),('rows','100'),('output','json')]
 targets.append((label,'https://archive.org/advancedsearch.php?'+urllib.parse.urlencode(params)))
for label,pattern in [('cdx_stable','www.jstor.org/stable/2373533*'),('cdx_pdf','www.jstor.org/stable/pdf/2373533.pdf*')]:
 targets.append((label,'https://web.archive.org/cdx/search/cdx?'+urllib.parse.urlencode({'url':pattern,'output':'json','collapse':'urlkey','fl':'timestamp,original,statuscode,mimetype,digest'})))
def fetch(target):
 label,url=target;t=time.perf_counter();r={'label':label,'url':url}
 try:
  with urllib.request.urlopen(url,timeout=40) as f:
   body=f.read();r.update(http_status=f.status,bytes=len(body),response=json.loads(body))
 except Exception as e:r['error']=repr(e)
 r['elapsed_seconds']=time.perf_counter()-t;return r
t=time.perf_counter();started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:results=list(pool.map(fetch,targets))
report={'started_utc':started,'elapsed_seconds':time.perf_counter()-t,'scope':'Five public catalogue metadata queries; no content, restricted files or authentication. CDX suffix-star patterns check stable article and conventional PDF paths; earlier internal-star empty searches are not absence evidence.','results':results}
payload=json.dumps(report,indent=2)
(base/'code/part_c_lieberman_archive_metadata_output.json').write_text(payload+'\n')
(base/'code/part_c_lieberman_archive_metadata_output.txt').write_text(payload+'\n')
print(payload)
