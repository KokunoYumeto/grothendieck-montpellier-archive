"""Fetch/extract remaining exact primary-source pages; preserve command outputs."""
from pathlib import Path
import os,subprocess,json,urllib.request
R=Path(__file__).resolve().parents[1]
O=R/'work/early/references'; O.mkdir(exist_ok=True)
env=dict(os.environ,OMP_THREAD_LIMIT='1')
events=[]
for pg in [470,471]:
 stem=O/f'sga7_page_{pg}'
 commands=[['pdftoppm','-f',str(pg),'-l',str(pg),'-scale-to','2200','-png','-singlefile',str(R/'work/reference_pdfs/sga7-1.pdf'),str(stem)],['tesseract',str(stem)+'.png',str(stem),'-l','eng','--psm','3']]
 for cmd in commands:
  r=subprocess.run(cmd,capture_output=True,text=True,env=env)
  events.append(dict(command=cmd,returncode=r.returncode,stdout=r.stdout,stderr=r.stderr))
url='https://mat.uab.cat/~pubmat/fitxers/download/FileType:pdf/FolderName:v26(3)/FileName:26382_01.pdf'
try:
 target=O/'cenkl_porter_1982.pdf'
 urllib.request.urlretrieve(url,target)
 events.append(dict(url=url,target=str(target),bytes=target.stat().st_size))
 cmd=['pdftotext','-layout',str(target),str(target.with_suffix('.txt'))]
 r=subprocess.run(cmd,capture_output=True,text=True)
 events.append(dict(command=cmd,returncode=r.returncode,stdout=r.stdout,stderr=r.stderr))
except Exception as e:events.append(dict(url=url,error=repr(e)))
print(json.dumps(events,ensure_ascii=False,indent=2))
