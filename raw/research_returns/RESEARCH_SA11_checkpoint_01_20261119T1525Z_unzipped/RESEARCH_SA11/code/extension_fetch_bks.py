from pathlib import Path
import urllib.request,subprocess,time,json,hashlib,shutil
base=Path('/workspace/scratch/eccd14a17414/RESEARCH_SA11_work')
url='https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Billera/BilleraKapranovSturmfels.pdf'
start=time.monotonic();data=urllib.request.urlopen(url,timeout=45).read()
p=base/'sources/extension_BKS1994.pdf';p.write_bytes(data)
subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
print(json.dumps({'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'runtime_s':time.monotonic()-start,'tesseract':shutil.which('tesseract')}))
