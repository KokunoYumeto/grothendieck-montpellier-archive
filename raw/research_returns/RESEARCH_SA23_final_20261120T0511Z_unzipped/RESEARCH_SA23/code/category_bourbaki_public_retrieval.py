from pathlib import Path
import urllib.request, json, hashlib, time, concurrent.futures
root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
jobs=[
 ('portal','https://archives-bourbaki.ahp-numerique.fr/','html'),
 ('delsarte_list','https://iecl.univ-lorraine.fr/wp-content/uploads/2021/04/DELSARTE_archives_numeros_de_redactions_bourbaki_2005.pdf','pdf'),
 ('wayback_available','https://archive.org/wayback/available?url=http%3A%2F%2Fsites.mathdoc.fr%2Farchives-bourbaki%2FPDF%2F179_nbr_082.pdf','json')
]
def fetch(job):
 name,url,suffix=job; started=time.monotonic()
 try:
  with urllib.request.urlopen(url,timeout=25) as response:
   data=response.read()
   record={'name':name,'url':url,'final_url':response.url,'status':response.status,'type':response.headers.get('Content-Type'),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
  target=root/f'notes/category_bourbaki_{name}.{suffix}'
  target.write_bytes(data)
  record.update(saved=str(target),seconds=time.monotonic()-started)
 except Exception as error: record={'name':name,'url':url,'error_type':type(error).__name__,'error':str(error),'seconds':time.monotonic()-started}
 return record
for record in concurrent.futures.ThreadPoolExecutor(max_workers=3).map(fetch,jobs): print(json.dumps(record),flush=True)
