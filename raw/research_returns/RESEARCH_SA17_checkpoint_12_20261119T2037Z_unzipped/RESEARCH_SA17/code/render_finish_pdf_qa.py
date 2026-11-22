from pathlib import Path
import fitz,json,hashlib,argparse,time
from PIL import Image,ImageDraw
from datetime import datetime,timezone
opts=argparse.ArgumentParser()
opts.add_argument('--checkpoint',type=int,default=3)
opts.add_argument('--pages',default='')
args=opts.parse_args();started=time.perf_counter()
r=Path(__file__).resolve().parents[1]
p=r/'RESEARCH_SA17_paper.pdf'; d=fitz.open(p)
pages=sorted({int(x) for x in args.pages.split(',')} if args.pages else {1,2,8,11,12,13,14,15,16,17,26,33,34,35,36,37,43,54,55,56,57,58,59,60,64,70,71,len(d)})
pages=[x for x in pages if 1<=x<=len(d)]
o=r/f'logs/pdf_qa_finish_{args.checkpoint:02d}';o.mkdir(exist_ok=True)
for k,start in enumerate(range(0,len(pages),4),1):
 c=Image.new('RGB',(1260,1810),'#dddddd')
 for j,n in enumerate(pages[start:start+4]):
  pix=d[n-1].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
  im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);im.thumbnail((610,860))
  x=(j%2)*630+(630-im.width)//2;y=(j//2)*905+28
  c.paste(im,(x,y));ImageDraw.Draw(c).text((x,y-20),'Page '+str(n),fill='black')
 c.save(o/f'spread_{k:02d}.jpg',quality=91)
log={'timestamp':datetime.now(timezone.utc).isoformat(),'pages_total':len(d),'pages_rendered':pages,'pdf_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'seconds':time.perf_counter()-started,'visual_check':'Pending human/model image inspection; rendering alone is not a check.'}
(r/f'logs/pdf_qa_finish_{args.checkpoint:02d}_render.json').write_text(json.dumps(log,indent=2)+'\n')
print(json.dumps(log))
