from pathlib import Path
import urllib.request, json, hashlib, time
root=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
url='https://sites.mathdoc.fr/archives-bourbaki/'
started=time.monotonic()
try:
    with urllib.request.urlopen(url,timeout=35) as response:
        data=response.read()
        record={'url':url,'final_url':response.url,'status':response.status,'content_type':response.headers.get('Content-Type'),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
    target=root/'notes/category_bourbaki_mathdoc_home.html'
    target.write_bytes(data)
    record.update(saved=str(target),seconds=time.monotonic()-started)
except Exception as error:
    record={'url':url,'error_type':type(error).__name__,'error':str(error),'seconds':time.monotonic()-started}
print(json.dumps(record,indent=2))
