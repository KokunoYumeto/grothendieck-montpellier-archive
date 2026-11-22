from pathlib import Path
import urllib.request,subprocess,concurrent.futures,time,json,hashlib
root=Path('/workspace/scratch/eccd14a17414/RESEARCH_SA11_work')
def one(k):
 t=time.monotonic();url=f'https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/PollackRichard/Pollack{k}.pdf';data=urllib.request.urlopen(url,timeout=45).read();p=root/f'sources/extension_Pollack{k}.pdf';p.write_bytes(data)
 subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True,capture_output=True)
 out=root/f'audit/extension_Pollack{k}_p1';subprocess.run(['pdftoppm','-f','1','-singlefile','-r','150','-png',str(p),str(out)],check=True,capture_output=True)
 subprocess.run(['tesseract',str(out)+'.png',str(out),'--psm','3'],check=True,capture_output=True)
 return {'k':k,'url':url,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'runtime_s':time.monotonic()-t,'page1':out.with_suffix('.txt').read_text()}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:results=list(ex.map(one,[8,9]))
(root/'audit/extension_fetch_goodman_output.json').write_text(json.dumps(results,indent=2))
for r in results:print(json.dumps(r),flush=True)
