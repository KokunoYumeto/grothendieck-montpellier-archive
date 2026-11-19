"""Render every final PDF page with Poppler and create indexed contact sheets."""
from pathlib import Path
import subprocess,time,json,hashlib,math
import fitz
from PIL import Image,ImageOps,ImageDraw
start=time.perf_counter()
root=Path(__file__).resolve().parents[1]
pdf=root/'RESEARCH_SA10_paper.pdf'
out=root/'qa'; pages=out/'pages'; sheets=out/'contact'
pages.mkdir(parents=True,exist_ok=True);sheets.mkdir(parents=True,exist_ok=True)
run=subprocess.run(['pdftoppm','-r','110','-png',str(pdf),str(pages/'page')],capture_output=True,text=True)
if run.returncode:
    print(run.stdout); print(run.stderr);raise SystemExit(run.returncode)
doc=fitz.open(pdf)
keywords={
 'B3 heading':'B3.1',
 'B5 shape':'B5.6',
 'B6 presentation':'B6.3',
 'C1 moduli':'C1.04',
 'C2 resolution':'C2.05',
 'C3 criterion':'C3.04',
 'C4 collars':'C4.05',
 'C5 Cannon':'C5.03',
 'C5 regularity':'C5.05',
 'C5 matrix':'C5.08',
 'Bibliography heading':'References',
 'Bibliography source path':'literature',
 'Bibliography B56 path':'references_B56'
}
matches={key:[] for key in keywords}
for i,page in enumerate(doc,1):
    txt=page.get_text()
    for key,word in keywords.items():
        if word in txt: matches[key].append(i)
images=sorted(pages.glob('page-*.png'))
assert len(images)==len(doc),(len(images),len(doc))
for batch in range(math.ceil(len(images)/12)):
    canvas=Image.new('RGB',(900,1392),'#d9dce0');draw=ImageDraw.Draw(canvas)
    for offset,p in enumerate(images[batch*12:(batch+1)*12]):
        im=Image.open(p).convert('RGB');im.thumbnail((284,320))
        x=(offset%3)*300+(300-im.width)//2;y=(offset//3)*348+20
        canvas.paste(im,(x,y));draw.text(((offset%3)*300+10,(offset//3)*348+4),f'PDF page {batch*12+offset+1}',fill='black')
    canvas.save(sheets/f'contact-{batch+1:02d}.png')
data={'pdf':pdf.name,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
      'pages':len(doc),'dpi':110,'rendered_images':[str(p.relative_to(root)) for p in images],
      'contact_sheets':[str(p.relative_to(root)) for p in sorted(sheets.glob('*.png'))],
      'keyword_page_locators':matches,'runtime_seconds':time.perf_counter()-start,
      'visual_approval':False,'note':'Rendering and text location only. Human-style image inspection must be recorded separately.'}
(out/'render_manifest.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in data.items() if k not in ['rendered_images']},indent=2))
