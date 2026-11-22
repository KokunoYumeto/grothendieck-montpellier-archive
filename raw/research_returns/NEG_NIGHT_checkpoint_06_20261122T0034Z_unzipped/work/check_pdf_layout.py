"""Page-edge text audit plus sampled Poppler render; not a proof check."""
import argparse,json,hashlib,subprocess
from pathlib import Path
import fitz
p=argparse.ArgumentParser();p.add_argument('--tag',required=True);p.add_argument('--utc',required=True);a=p.parse_args()
source=Path('deliverables/NEG_NIGHT.pdf');doc=fitz.open(source);out=Path('work/pdf_qa');out.mkdir(exist_ok=True)
violations=[]
for i,page in enumerate(doc):
 for word in page.get_text('words'):
  x0,y0,x1,y1,text,*_=word
  if x0<25 or x1>page.rect.width-25 or y0<15 or y1>page.rect.height-15:
   violations.append({'page':i+1,'word':text,'box':[x0,y0,x1,y1]})
selected={1,len(doc)}
if a.tag=='cp06':selected.update({91,94,178,254})
for needle in ['NN-C034','NN-C035','NN-C036','NN-A035','NN-A036','NN-A037','NN-G036','NN-S017','NN-S018','NN-S019']:
 for i,page in enumerate(doc):
  if i>15 and needle in page.get_text():selected.add(i+1);break
for page in sorted(selected):
 subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','1400','-png',str(source),str(out/f'{a.tag}_page_{page:03d}')],check=True,capture_output=True)
result={'date_utc':a.utc,'pdf_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'pages':len(doc),'page_edge_violations':violations,'rendered_pages':sorted(selected),'visual_inspection':'pending explicit image viewing; text bounds alone do not verify layout','scope':'Every word box checked against25pt horizontal and15pt vertical edge exclusion; sampled pages rendered with Poppler.'}
(out/f'{a.tag}_bounds_check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
