from pathlib import Path
import json,urllib.request,time,hashlib,shutil,subprocess
base=Path("/workspace/scratch/a7ef7e55112c/RESEARCH_SA23")
url="https://eqworld.ipmnet.ru/ru/library/books/GohbergKrejn1965ru.djvu"
dest=base/"sources/geometry_GohbergKrein1965.djvu"
started=time.time()
with urllib.request.urlopen(url,timeout=45) as response:
    data=response.read()
    status=response.status
dest.write_bytes(data)
log={"url":url,"status":status,"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest(),"tools":{x:shutil.which(x) for x in ["djvutxt","ddjvu","djvused","tesseract"]},"elapsed_seconds":time.time()-started}
if shutil.which("djvutxt"):
    run=subprocess.run(["djvutxt",str(dest),str(base/"notes/geometry_GohbergKrein1965_full.txt")],capture_output=True,text=True)
    log["djvutxt"]={"returncode":run.returncode,"stdout":run.stdout,"stderr":run.stderr}
(base/"logs/geometry_GohbergKrein1965_retrieval.json").write_text(json.dumps(log,ensure_ascii=False,indent=2))
print(json.dumps(log,ensure_ascii=False))

