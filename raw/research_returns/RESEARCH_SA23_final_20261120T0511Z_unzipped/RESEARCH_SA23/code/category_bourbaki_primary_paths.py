from pathlib import Path
import urllib.request, hashlib, json, time, subprocess, concurrent.futures
root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
jobs=[
 ('current','https://sites.mathdoc.fr/archives-bourbaki/PDF/179_nbr_082.pdf'),
 ('historical','http://portail.mathdoc.fr/archives-bourbaki/PDF/179_nbr_082.pdf')
]
def fetch(job):
 name,url=job; started=time.monotonic()
 try:
  with urllib.request.urlopen(url,timeout=25) as response:
   data=response.read()
   record={'name':name,'url':url,'final_url':response.url,'status':response.status,'type':response.headers.get('Content-Type'),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
  target=root/f'notes/category_bourbaki_nbr082_{name}.download'
  target.write_bytes(data)
  record.update(saved=str(target),seconds=time.monotonic()-started,pdf_magic=data[:5]==b'%PDF-')
 except Exception as error: record={'name':name,'url':url,'error_type':type(error).__name__,'error':str(error),'seconds':time.monotonic()-started}
 return record
for record in concurrent.futures.ThreadPoolExecutor(max_workers=2).map(fetch,jobs): print(json.dumps(record),flush=True)
source=root/'sources/root_paumier2014_schwartz.pdf'
command=['pdftoppm','-f','65','-l','65','-singlefile','-scale-to','2200','-png',str(source),str(root/'notes/category_bourbaki_paumier_page065')]
result=subprocess.run(command,capture_output=True,timeout=40)
print(json.dumps({'command':command,'returncode':result.returncode,'stderr':result.stderr.decode(errors='replace')}),flush=True)
command=['pdfinfo','-url',str(source)]
result=subprocess.run(command,capture_output=True,timeout=40)
out=root/'notes/category_bourbaki_paumier_pdf_links.txt'; out.write_bytes(result.stdout)
print(json.dumps({'command':command,'returncode':result.returncode,'saved':str(out),'stdout_bytes':len(result.stdout),'stderr':result.stderr.decode(errors='replace')}),flush=True)
