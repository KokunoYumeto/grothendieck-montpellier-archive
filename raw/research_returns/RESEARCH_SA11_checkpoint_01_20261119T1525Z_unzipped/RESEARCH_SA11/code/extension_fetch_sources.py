from pathlib import Path
import urllib.request,subprocess,time,json,hashlib
base=Path('/workspace/scratch/eccd14a17414/RESEARCH_SA11_work')
sources=[('SZ1993_preprint','https://www.mi.fu-berlin.de/math/groups/discgeom/ziegler/Preprintfiles/020PREPRINT.pdf'),('SZ1993_published','https://link.springer.com/content/pdf/10.1007/BF02573961.pdf'),('MRG1993','https://link.springer.com/content/pdf/10.1007/BF02573981.pdf'),('BKS1994','https://www.ams.org/journals/proc/1994-122-02/S0002-9939-1994-1205482-0/S0002-9939-1994-1205482-0.pdf')]
log=[]
for name,url in sources:
 start=time.monotonic()
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  data=urllib.request.urlopen(req,timeout=45).read()
  p=base/'sources'/('extension_'+name+'.pdf');p.write_bytes(data)
  if data[:4]!=b'%PDF': raise ValueError('Response was not PDF')
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
  result={'name':name,'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'status':'downloaded','runtime_s':time.monotonic()-start}
 except Exception as e: result={'name':name,'url':url,'status':'failed','error':str(e),'runtime_s':time.monotonic()-start}
 log.append(result); print(result,flush=True)
(base/'audit/extension_fetch_sources_output.json').write_text(json.dumps(log,indent=2))
