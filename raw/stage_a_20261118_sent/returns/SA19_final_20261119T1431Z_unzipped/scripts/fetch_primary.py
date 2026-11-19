"""Download a cited primary-source PDF for local reading; never bundle it as our work."""
import argparse,hashlib,pathlib,urllib.request,json,subprocess,datetime
p=argparse.ArgumentParser();p.add_argument('url');p.add_argument('out');a=p.parse_args()
out=pathlib.Path(a.out);out.parent.mkdir(parents=True,exist_ok=True)
data=urllib.request.urlopen(a.url,timeout=25).read();out.write_bytes(data)
r=subprocess.run(['pdftotext','-layout',str(out),str(out.with_suffix('.txt'))],capture_output=True,text=True)
print(json.dumps({'url':a.url,'file':str(out),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'pdftotext_exit':r.returncode,'stderr':r.stderr,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()},ensure_ascii=False))
