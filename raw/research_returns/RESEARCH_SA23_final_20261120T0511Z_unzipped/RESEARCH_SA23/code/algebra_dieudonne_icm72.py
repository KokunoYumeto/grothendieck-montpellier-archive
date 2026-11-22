from pathlib import Path
from datetime import datetime,timezone
from urllib.request import urlopen,Request
import json,time,hashlib,re
import fitz
root=Path(__file__).resolve().parents[1]
start=time.monotonic()
url='https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1966.1/ICM1966.1.ocr.pdf'
out={'started_utc':datetime.now(timezone.utc).isoformat(),'url':url,'source':'Official IMU original proceedings facsimile; web reader content-length limit, not access refusal.'}
try:
 with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 (public primary-source research)'}),timeout=25) as r:
  data=r.read();out.update(status=r.status,final_url=r.geturl(),content_type=r.headers.get('Content-Type'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 pdf=root/'sources/algebra_dieudonne_icm1966_volume.pdf';pdf.write_bytes(data)
 doc=fitz.open(pdf);out['pdf_pages']=len(doc)
 texts=[page.get_text() for page in doc]
 titles=[]
 for i,t in enumerate(texts):
  n=re.sub(r'\s+',' ',t).upper()
  if 'LES TRAVAUX DE ALEXANDER GROTHENDIECK' in n or 'LES TRAVAUX DE ALEXANDRE GROTHENDIECK' in n:
   titles.append({'physical_page':i+1,'text':t[:10000]})
 out['title_matches']=titles
 (root/'sources/algebra_dieudonne_icm1966_volume.txt').write_text('\n\f\n'.join(texts))
 pages=set(range(min(5,len(doc))))
 for h in titles:
  i=h['physical_page']-1
  if i<150:pages.update(range(max(0,i-1),min(len(doc),i+7)))
 out['renders']=[]
 for i in sorted(pages):
  path=root/f'sources/algebra_dieudonne_icm1966_page{i+1:03d}.png'
  doc[i].get_pixmap(matrix=fitz.Matrix(1.8,1.8)).save(path)
  out['renders'].append(str(path.relative_to(root)))
except Exception as e:out['error']=repr(e)
out['elapsed_seconds']=time.monotonic()-start
(root/'logs/algebra_dieudonne_icm72.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
summary={k:v for k,v in out.items() if k not in ['title_matches','renders']}
summary['title_matches']=[{'physical_page':v['physical_page'],'text_start':v['text'][:1600]} for v in out.get('title_matches',[])]
summary['renders']=out.get('renders',[])
print(json.dumps(summary,ensure_ascii=False,indent=2))
