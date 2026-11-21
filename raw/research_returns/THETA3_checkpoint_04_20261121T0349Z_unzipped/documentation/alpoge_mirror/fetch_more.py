import urllib.request,urllib.parse,json,pathlib,hashlib,concurrent.futures,datetime,sys
root=pathlib.Path(__file__).resolve().parent
sha=json.loads((root/'provenance.json').read_text())['commit']
paths=[l.strip().removeprefix('src/') for l in pathlib.Path(sys.argv[1]).read_text().splitlines() if l.strip()]
base=f'https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/{sha}/src/'
def fetch(p):
 url=base+urllib.parse.quote(p,safe="/");dest=root/p
 try:
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'THETA3-source-audit'}),timeout=45).read()
  old=dest.read_bytes() if dest.exists() else None
  dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
  return {'path':p,'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob_sha1':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),'previous_equal':old==data if old is not None else None,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 except Exception as e:return {'path':p,'url':url,'error':str(e)}
manifest=root/'pinned_manifest.json';obj=json.loads(manifest.read_text());rs={r['path']:r for r in obj['files']}
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
 for r in ex.map(fetch,paths):rs[r['path']]=r;print(r['path'],r.get('bytes',r.get('error')),flush=True)
obj['files']=list(rs.values());manifest.write_text(json.dumps(obj,indent=2))
