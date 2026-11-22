from pathlib import Path
import urllib.request,concurrent.futures,subprocess,os,hashlib,json,time
base=Path("/workspace/scratch/a7ef7e55112c/RESEARCH_SA23")
runtime=Path("/tmp/geometry_djvu_runtime")
runtime.mkdir(exist_ok=True)
packages=["djvulibre-bin_3.5.28-2.2~deb12u1_amd64.deb","libdjvulibre21_3.5.28-2.2~deb12u1_amd64.deb"]
def fetch(name):
    url="https://deb.debian.org/debian/pool/main/d/djvulibre/"+name
    with urllib.request.urlopen(url,timeout=40) as r:data=r.read();status=r.status
    p=runtime/name;p.write_bytes(data)
    proc=subprocess.run(["dpkg-deb","-x",str(p),str(runtime)],capture_output=True,text=True)
    return {"url":url,"status":status,"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest(),"extract":{"code":proc.returncode,"stdout":proc.stdout,"stderr":proc.stderr}}
started=time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:results=list(ex.map(fetch,packages))
env=os.environ.copy();env["LD_LIBRARY_PATH"]=str(runtime/"usr/lib/x86_64-linux-gnu")
proc=subprocess.run([str(runtime/"usr/bin/djvutxt"),str(base/"sources/geometry_GohbergKrein1965.djvu"),str(base/"notes/geometry_GohbergKrein1965_full.txt")],env=env,capture_output=True,text=True)
log={"packages":results,"djvutxt":{"code":proc.returncode,"stdout":proc.stdout,"stderr":proc.stderr},"elapsed_seconds":time.time()-started}
(base/"logs/geometry_djvu_runtime.json").write_text(json.dumps(log,ensure_ascii=False,indent=2))
print(json.dumps(log,ensure_ascii=False))

