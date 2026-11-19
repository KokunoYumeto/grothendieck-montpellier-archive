import urllib.request, pathlib, subprocess, concurrent.futures, json, time
base=pathlib.Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/agents/reduction_descent/sources')
manifest=json.loads((base/'gdz_manifest.json').read_text())
canvases=manifest['sequences'][0]['canvases']
needed=set(range(59,79))

def one(c):
 pno=int(c['label']); img=base/f'groth1966_p{pno}.jpg'; out=img.with_suffix('')
 url=c['images'][0]['resource']['service']['@id']+'/full/1800,/0/default.jpg'
 try:
  if not img.exists():img.write_bytes(urllib.request.urlopen(url,timeout=25).read())
  subprocess.run(['tesseract',str(img),str(out),'-l','eng'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  return [pno,len(img.read_bytes()),'ok',url]
 except Exception as e:return [pno,str(e),url]
t=time.monotonic()
selected=[c for c in canvases if str(c.get('label')).isdigit() and int(c['label']) in needed]
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
 for r in ex.map(one,selected):print(json.dumps(r),flush=True)
print('seconds',time.monotonic()-t,flush=True)
