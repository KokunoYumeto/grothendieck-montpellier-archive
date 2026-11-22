from pathlib import Path
import urllib.request,urllib.error,hashlib,time,json,datetime,subprocess
root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
url='https://grothendieck.umontpellier.fr/162-1.pdf'
dest=root/'sources/category_montpellier_162-1.pdf'
start=time.perf_counter()
try:
    with urllib.request.urlopen(url,timeout=40) as r:
        content=r.read()
        record={'url':url,'final_url':r.url,'status':r.status,'content_type':r.headers.get('Content-Type'),'bytes':len(content),'sha256':hashlib.sha256(content).hexdigest(),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed':time.perf_counter()-start}
    if not content.startswith(b'%PDF-'):
        dest=dest.with_suffix('.response')
        record['not_pdf']=True
    dest.write_bytes(content)
    record['saved']=str(dest)
    print(json.dumps(record),flush=True)
    if dest.suffix=='.pdf':
        result=subprocess.run(['pdfinfo',str(dest)],capture_output=True,text=True)
        print(json.dumps({'command':['pdfinfo',str(dest)],'status':result.returncode,'stdout':result.stdout,'stderr':result.stderr}),flush=True)
except Exception as e:
    print(json.dumps({'url':url,'error':type(e).__name__,'message':str(e),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed':time.perf_counter()-start}),flush=True)
